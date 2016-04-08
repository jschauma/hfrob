#! /usr/bin/env python2.7
#
# This tool ...

# The entire functionality of the hfrob(1) tool is
# found in the moo.hfrob.Frobber class.  This script
# just invokes the 'main' function provided by
# moo.hfrob.

###
### Main
###

if __name__ == "__main__":
    import sys
    from moo.hfrob import main
    main(sys.argv[1:])
