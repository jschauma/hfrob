#! /usr/local/bin/python
#
# A unittest for functionality in hfrob.py.

import sys
sys.path.append("../lib/")

import ConfigParser
import logging
import unittest

import hfrob

class TestHfrob(unittest.TestCase):

    def setUp(self):
        self.hfrob = hfrob.Frobber()


    def testDefaults(self):
        cfg_opts = {
                    "cfg_file" : "/etc/hfrobrc",
                    "pretty"   : False,
                    "verbosity" : logging.WARNING
                 }

        for key, val in cfg_opts.iteritems():
            self.assertEqual(self.hfrob.getOpt(key), val)


    def testUsageHelp(self):
        opts = [ "-h" ]
        # -h triggers usage
        self.assertRaises(hfrob.Frobber.Usage, self.hfrob.parseOptions, opts)
        try:
            self.hfrob.parseOptions(opts)
        except hfrob.Frobber.Usage, u:
            self.assertEqual(hfrob.Frobber.EXIT_SUCCESS, u.err)


    def testUsageAddList(self):
        opts = [ "-l", "/dev/null", "-l", "/whatever" ]
        vlist = [ "/dev/null", "/whatever" ]
        self.hfrob.parseOptions(opts)
        self.assertEqual(self.hfrob.getOpt("vlists"), vlist)


if __name__ == '__main__':
	unittest.main()
