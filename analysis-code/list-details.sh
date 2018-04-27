#!/bin/bash

# Go through the git logs for the Qualitas suite applications
# and extract some basic details for each application.

# Print (to the $OUTFILE) the following (one line per app):
# - application name
# - no. of .py files 
# - no. of (thousands of) lines in these .py files (wc -l)
# - date of first commit
# - no of commits (excluding 2018)


# Get the Qualitas root dir :
QDIR=`python3 qualitas.py 2017`
DATADIR=`python3 data_dir.py`

# This is the file that the numbers are written to:
OUTFILE=${DATADIR}/details.txt
rm -f $OUTFILE

echo "Application Version & Files & KNBL & Version & First Commit & No of Commits\\\\ \n"  >>$OUTFILE

TAG_TEMP=`mktemp`

pushd $QDIR
for app in *; do
    if [ -d $app ]; then
        echo Processing $app
        pushd $app >/dev/null
        # Count files, lines, nonblank-lines:
        num_files=`find . -name '*.py' | wc -l`
        tot_lines=`(find . -name '*.py' -print0 | xargs -0 cat) | wc -l`
        # We need to filter out Unicode etc. before grep gets at it:
        nb_lines=`(find . -name '*.py' -print0 \
                    | xargs -0 iconv -c -t us-ascii//TRANSLIT) \
                    | grep -v  '^\s*$' | wc -l`
        nb_k_lines=`echo $nb_lines | awk  '{printf("%.0f", $1/1000);}'`
        # Get dates for newest tags:
        # This doesn't quite work, so I did it semi-manually in the end.
#        git for-each-ref --sort=taggerdate refs/tags \
#            --format '%(authordate:short) & %(refname:short)' | sort -g \
#            | grep -v '& 2017' | grep -v '^\s*&' >$TAG_TEMP
#            --format '%(tag) & %(taggerdate:short)' refs/tags \
#        newest_tag=`tail -n1 $TAG_TEMP`
        # Get date of oldest (first) commit:
        first_commit_id=`git rev-list --max-parents=0 HEAD`
        first_commit_date=`git show -s --format=%cd --date=short $first_commit_id | sort | head -n1`
        # Count total number of commits on all branches:
        num_commits=`git log --all --format=%cd --date=short | grep -v '^2018' | wc -l`
        # Now print a row of the table
        printf "%13s & %5s & %5s & & %10s & %7s\\\\\\ \n" \
               $app $num_files $nb_k_lines \
               $first_commit_date $num_commits \
               >>$OUTFILE
        popd >/dev/null
    fi
done
popd

echo Done. Output written to $OUTFILE


