#!/bin/bash

# Go through the git logs for the Qualitas suite applications
# and count the commits corresponding to each Python 3.x release.
# The release dates are in python_versions.py, we have a counter for each one.
# Print one line per app, with the 7 release counts and the total count.

# NB: 2017 data is excluded, and the total includes commits before 3.0.

# The Qualitas root dir :
QDIR=`python3 qualitas.py`

# This is the file that the numbers are written to:
OUTFILE=`pwd`/data/commit-data.csv
rm -f $OUTFILE

TAG_TEMP=`mktemp`

# These are the dates of the Python 3.x releases, starting with the latest:
releases=(`python3 -c 'import python_versions; python_versions.print_versions("3.")' | awk '{printf("%s ", $3)}'`)

len=${#releases[*]}

declare -a counters

pushd $QDIR
for app in *; do
    if [ -d $app ]; then
        echo Processing $app
        pushd $app >/dev/null
        # Get the dates for all pre-2017 commits:
        git log --all --format=%cd --date=short | grep -v 2017 | sort >$TAG_TEMP
        # Initialise an array of counters, one for each release:
        for (( i=0; i<len; i++ )); do counters[$i]=0; done
        # Now process commit dates and increment counters as appropriate:
        for commitdate in `cat $TAG_TEMP`; do
            for (( i=0; i<len; i++ )); do
                rdate=${releases[$i]}
                if [ ! $commitdate \< $rdate ]; then
                    counters[$i]=$((counters[$i]+1))
                fi
            done
        done
        # Counts now done for this app, so print a line to the output file:
        printf "%13s" $app >>$OUTFILE
        for (( i=0; i<len; i++ )); do
            printf " %6s" ${counters[$i]} >>$OUTFILE
        done
        # Total number of (non-2017) commits:
        echo "  "`cat $TAG_TEMP | wc -l` >>$OUTFILE
        popd >/dev/null
    fi
done
popd >/dev/null


echo Done. Output written to `basename $OUTFILE`


