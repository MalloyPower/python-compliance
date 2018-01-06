#!/bin/bash

# Go through the git logs for the Qualitas suite applications
# and list the *tagged* commits for each app (before 2017).

# Mark the first (most recent) one with a '#', but list a few more
# in case this isn't a release (need to inspect the log manually).

# I'm looking for the 'most recent', so I list the top 20 for each app.
MAX_TAGS=20  

# Get the Qualitas root dir:
QDIR=`python3 qualitas.py`

# This is the file that the numbers are written to:
OUTFILE=`pwd`/data/tag-details.txt
rm -f $OUTFILE

pushd $QDIR
for app in *; do
    if [ -d $app ]; then
        echo Processing $app
        pushd $app >/dev/null
        printf "# %13s " $app" " >>$OUTFILE
        # Get the tags, look for a number, heep most recent ${MAX_TAGS}
        git log --tags --simplify-by-decoration --pretty="format:%cd %D" --date=short \
            | grep -v '^2017' | grep ' .*[0-9.]' \
            | sort -r | head -n${MAX_TAGS} >>$OUTFILE
        echo " " >>$OUTFILE
        popd >/dev/null
    fi
done
popd >/dev/null

echo Done. Output written to `basename $OUTFILE`
echo Try doing:  grep '^#' $OUTFILE

