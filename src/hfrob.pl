#! /usr/local/bin/perl -Tw
#
# This tool ...

use 5.008;

use strict;
use File::Basename;
use Getopt::Long;
Getopt::Long::Configure("bundling");

use Log::Log4perl qw/:easy/;
Log::Log4perl->easy_init($ERROR);

###
### Constants
###

use constant TRUE => 1;
use constant FALSE => 0;

use constant EXIT_FAILURE => 1;
use constant EXIT_SUCCESS => 0;

###
### Globals
###

my $PROGNAME = basename($0);

###
### Subroutines
###

# function : init
# purpose  : initialize variables, parse command line options;
# inputs   : none
# returns  : void, may exit under certain conditions

sub init() {
	my ($ok);

	if (!scalar(@ARGV)) {
		error("I have nothing to do.  Try -h.", EXIT_FAILURE);
		# NOTREACHED
	}

	$ok = GetOptions(
			 "help|h" 	=> \$OPTS{'h'},
			 "pretty|p=s" 	=> \$OPTS{'p'},
			 "verbose|v+" 	=> sub {
				 		my $level = $WARN;
				 		$OPTS{'v'}++;
						delete($OPTS{'q'});
						if ($OPTS{'v'} > 3) {
							$level = $TRACE;
						} elsif ($OPTS{'v'} > 2) {
							$level = $DEBUG;
						} elsif ($OPTS{'v'} > 1) {
							$level = $INFO;
						}
						Log::Log4perl->easy_init($level);
					}
			 );

	if (scalar(@ARGV)) {
		error("I can't deal with spurious arguments after flags.  Try -h.", EXIT_FAILURE);
		# NOTREACHED
	}

	if ($OPTS{'h'} || !$ok) {
		usage($ok);
		exit(!$ok);
		# NOTREACHED
	}
}


# function : verbose
# purpose  : print a message if given verbosity is set
# input    : a string and a verbosity level

sub verbose($;$) {
	my ($msg, $level) = @_;
	my $char = "=";

	return unless $OPTS{'v'};

	$char .= "=" x ($level ? ($level - 1) : 0 );

	if (!$level || ($level <= $OPTS{'v'})) {
		print STDERR "$char> $msg\n";
	}
}


###
### Main
###

init();

exit($RETVAL);
