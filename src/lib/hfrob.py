"""hfrob -- frob the hobknobbin good

mumble mumble mumble

"""

import ConfigParser

import getopt
import logging
import os
import re
import stat
import string 
import subprocess
import sys

###
### Classes
###

class Frobber(object):
    """An h-frobber

    The main interface of the 'hfrob' program.  Its member functions are used to
    run the program, it's private members are (mostly) configuration options
    that can be set via the command-line.
    """

    EXIT_ERROR = 1
    EXIT_SUCCESS = 0

    def __init__(self):
        """Construct a Frobber object with default values."""

        self.__opts = {
                    "cfg_file" : "/etc/hfrobrc",
                    "pretty"   : False
                    "verbosity" : logging.WARNING
                 }

        self.__frobbed = {}
        self.__cfg_section = "hfrob"


    def _setVerbosity(self, f):
        """set the verbosity based on the given factor"""

        n = int(f)
        v = self.getOpt("verbosity")

        if (v > logging.INFO):
            v = logging.INFO
        if (n > 1):
           # XXX: magic number; logging uses specific numbers, but
           # has no specified increment 
           v -= (5 * n)

        # The logging module treats 0 as 'unset'.
        if v < 1:
            v = 1
        self.setOpt("verbosity", v)
        logging.basicConfig(level=self.getOpt("verbosity"),
                            format='%(message)s')


    class Usage(Exception):
        """A simple exception that provides a usage statement and a return code."""

        def __init__(self, rval):
            self.err = rval
            self.msg = 'Usage: %s [-hpv]\n' % os.path.basename(sys.argv[0])
            self.msg += '\t-h  print this message and exit\n'
            self.msg += '\t-p  be pretty\n'
            self.msg += '\t-v  be verbose\n'


    def getOpt(self, opt):
        """Retrieve the given configuration option.

        Returns:
            The value for the given option if it exists, None otherwise.
        """

        try:
            r = self.__opts[opt]
        except ValueError:
            r = None

        return r


    def parseOptions(self, inargs):
        """Parse given command-line options and set appropriate attributes.

        Arguments:
            inargs -- arguments to parse

        Returns:
            the list of arguments remaining after all flags have been
            processed

        Raises:
            Usage -- if '-h' or invalid command-line args are given
        """

        try:
            opts, args = getopt.getopt(inargs, "c:hl:v")
        except getopt.GetoptError:
            raise self.Usage(self.EXIT_ERROR)

        for o, a in opts:
            if o in ("-c"):
                self.setOpt("cfg_file", a)
            if o in ("-h"):
                raise self.Usage(self.EXIT_SUCCESS)
            if o in ("-l"):
                vlists = []
                if ("vlists" in self.__frobbed):
                    vlists = self.getOpt("vlists")
                vlists.append(a)
                self.setOpt("vlists", vlists)
            if o in ("-v"):
                self._setVerbosity(1)

        return args


    def setOpt(self, opt, val):
        """Set the given option to the provided value"""

        self.__opts[opt] = val
        self.__frobbed[opt] = val


    def verifyOptions(self):
        """make sure that all given options (from command-line or config file) are
        valid"""

        for opt in self.__list_opts:
            if self.__opts[opt]:
                self.__opts[opt] = self.__opts[opt].split()

        for opt in self.__int_opts:
            if type(self.__opts[opt]) is not int:
                try:
                    self.__opts[opt] = string.atoi(self.__opts[opt])
                except ValueError:
                    logging.error("Invalid value for configuration option '%s': %s"
                        % (opt, self.__opts[opt]))
                    raise

###
### A 'main' for the hfrob(1) program.
###

def main(args):
    """Run the hfrob(1) program.
        
    Arguments:
        args -- command-line arguments
    """

    try:
        frobber = Frobber()
        try:
            args = frobber.parseOptions(args)
        except frobber.Usage, u:
            if (u.err == frobber.EXIT_ERROR):
                out = sys.stderr
            else:
                out = sys.stdout
                out.write(u.msg)
                sys.exit(u.err)
	            # NOTREACHED

        try:
            frobber.parseConfig(frobber.getOpt("cfg_file"))
            frobber.verifyOptions()
        except Exception, e:
            logging.error(e)
            sys.exit(frobber.EXIT_ERROR)
            # NOTREACHED

    except KeyboardInterrupt:
        # catch ^C, so we don't get a "confusing" python trace
        sys.exit(frobber.EXIT_ERROR)
