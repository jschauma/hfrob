This directory contains contains template files which
I tend to use to bootstrap a new tool.

The README for a new tool would normally look
something like this:

# hfrob -- frob the hobknobbin good

The hfrob tool allows you to frob the hobknobbin of
any given furzzl in such a matter that it can be
qualified as 'good'.  It does so by druggling the
shnuzendorb under the porcl.

This is particularly useful in the context of [your
tools' consistification](https://www.netmeister.org/blog/consistent-tools.html).

Installation
============

To install the command and manual page somewhere
convenient, run `make install`; the Makefile defaults
to '/usr/local' but you can change the PREFIX:

```
$ make PREFIX=~ install
```

Documentation
=============

Please see the manual page for all details:

```
NAME
     hfrob -- frob the hobknobbin good

SYNOPSIS
     hfrob [-bhv] [-e [key[=val][,key[=val],...]]]

DESCRIPTION
     The hfrob tool allows you to frob the hobknobbin of any given furzzl in
     such a matter that it can be qualified as 'good'.	It does so by drug-
     gling the shnuzendorb under the porcl.

OPTIONS
     The following options are supported by hfrob:

     -b		 Also brunz the strocl.	 See section DETAILS for details.

     -e key=val	 When frobbing, erase all klunkats that contain the given key-
		 value pair.

     -h		 Display help and exit.

     -v		 Be verbose.  Can be specified multiple times.

DETAILS
     As you all know, all furrzls need their hobknobbin frobbed with some reg-
     ularity.  hfrob will perform all the steps involved in this laborsome
     process:

     First it shuffles the cruxors, generates the friesen-dot-list, then drug-
     gles the shnuzendorb under the porcl.

     Brunzing of the strocl is optional, and only done if hfrob is passed the
     -b flag.  The user may be asked to validate the new strocl before it
     actually is brunzed.

EXAMPLES
     The following examples illustrate common usage of this tool.

     To frob the hobknobbins of all furrzls starting with an 'a' and generat-
     ing output into the file troysl:

	   hfrob -a -d troysl

EXIT STATUS
     The hfrob utility exits 0 on success, and >0 if an error occurs.

ENVIRONMENT
     The following environment variables affect the execution of this tool:

     CHUCK_NORRIS  The level at which to brunze the strocl.  If not given,
		   hfrob will default to 3.

SEE ALSO
     ifrob(1), long_strocl(3)

HISTORY
     hfrob was originally written by Jan Schaumann <jschauma@netmeister.org>
     in December 2007.

BUGS
     Please file bugs and feature requests by emailing the author.
```
