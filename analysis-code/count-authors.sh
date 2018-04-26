#!/bin/bash

# Go through the git logs for the Qualitas suite applications
# and extract information on the number of authors for each application.
# Print (to the $OUTFILE) the following:
#  application name
#  no. of authors (with at least one file commit of any kind)
#  no. of authors with no. of file commits greater than a cutoff
#  no. of authors who had created (added) a file (i.e. not just edited)

# Authors are printed using "%ae" - i.e. by email address, not by name.


# Get the Qualitas root dir :
QDIR=`python3 qualitas.py 2017`

# This is the file that the numbers are written to:
OUTFILE=`pwd`/data/authors.txt
rm -f $OUTFILE

TEMP_OUT=`mktemp`

# File-creators are the ones where the file diff shows "A" (for added):
CREATORS=--diff-filter=A

# Authors with less than this no of commits will be ignored in fields:
CUTOFF_VALUES="5 10 50 100 500 1000"

printf "# %13s %s %s %s\n" App All Creators "$CUTOFF_VALUES" >> $OUTFILE

pushd $QDIR
for app in *; do
    if [ -d $app ]; then
        echo Processing $app
        pushd $app >/dev/null
        git log --pretty="%ae" | sort | uniq -c >$TEMP_OUT
        auth_all=`cat $TEMP_OUT | wc -l`
        auth_create=`git log $CREATORS --pretty="%ae" | sort | uniq | wc -l`
        printf "%13s & %5d & %5d" $app $auth_all $auth_create >> $OUTFILE
        for CUTOFF in $CUTOFF_VALUES; do
            auth_cutoff=`cat $TEMP_OUT | \
                 awk -v cutoff=$CUTOFF \
                 '{if ($1>=cutoff) printf("%d %s\n", $1, $2);}' | wc -l`
            printf "& %5d" $auth_cutoff>>$OUTFILE
        done
        echo " \\\\"  >> $OUTFILE
        popd >/dev/null
    fi
done
popd >/dev/null

echo Done. Output written to `basename $OUTFILE`


