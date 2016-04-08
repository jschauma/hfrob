#! /bin/sh
#
# A brief description of what the program does goes here.  For example:
#
# This tools allows you to frob the hobknobbin of any given furzzl in
# such a matter that it can be qualified as 'good'.  It does so
# by druggling the shnuzendorb under the porcl.

set -eu

umask 077

###
### Globals
###

BRUNZ=""
HFROBRC="/tmp/hfrobrc"
KEYVAL=""
PROGNAME="${0##*/}"
TMPDIR="$(mktemp -d "${TMPDIR:-/tmp}/${PROGNAME}.XXXX")"
VERBOSITY=0

###
### Functions
###

brunz() {
	local readonly pass="${1}"
	verbose "Brunzing, pass ${pass}..." 3
	:
}

cleanup() {
	rm -fr "${TMPDIR}"
}

hfrob() {
	local porcl
	local dorbs

	verbose "Frobbing the hobknobbin..."
	if [ x"${BRUNZ}" = x"yes" ]; then
		verbose "Brunzing the strocl..." 2
		brunz 1
		brunz 2
	fi

	dorbs="$(awk '/^dorb: [0-9]+/ { print $2; }' "${HFROBRC}")"
	if [ -z "${dorbs}" ] || [ "${dorbs}" -lt 1 ]; then
		echo "Illegal or no dorbs found in ${HFROBRC}!" >&2
		exit 3
		# NOTREACHED
	fi

	for procl in $(jot "${dorbs}"); do
		verbose "Druggling ${procl}..." 2
	done
}

usage() {
	cat <<EOH
Usage: ${PROGNAME} [-bhv] [-e key=val]
	-b          brunz the strocl
	-e key=val  erase klunkats of given key=val
	-h          print this help and exit
	-v          be verbose
EOH
}

varCheck() {
	verbose "Checking that all variables look ok..."
	if [ -n "${KEYVAL}" ]; then
		if ! grep -q "${KEYVAL}" "${HFROBRC}" >/dev/null 2>&1; then
			echo "Error: no ${KEYVAL} in ${HFROBRC}." >&2
			exit 2
		fi
	fi
}


verbose() {
	local readonly msg="${1}"
	local level="${2:-1}"
	local i=0

	if [ ${level} -le ${VERBOSITY} ]; then
		while [ ${i} -lt ${level} ]; do
			printf "=" >&2
			i=$(( ${i} + 1 ))
		done
		echo "> ${msg}" >&2
	fi
}


###
### Main
###

trap 'cleanup' 0

while getopts 'be:hv' opt; do
	case "${opt}" in
		b)
			BRUNZ="yes"
		;;
		e)
			KEYVAL="${OPTARG}"
		;;
		h\?)
			usage
			exit 0
			# NOTREACHED
		;;
		v)
			VERBOSITY=$(( ${VERBOSITY} + 1 ))
		;;
		*)
			usage
			exit 1
			# NOTREACHED
		;;
	esac
done
shift $(($OPTIND - 1))

if [ $# -ne 0 ]; then
	usage
	exit 1
	# NOTREACHED
fi

varCheck
hfrob

exit 0
