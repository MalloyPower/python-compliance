# Data for the tables/figures in the paper

## table1-passrates

The pass rate for each application for each version of PyComply.

There's a file in here for each 'suite' of programs; each file has one
row per application, one column per Python version.  The number is the
percentage of this application's files that passed that particular
version of PyComply.  The last column is the total number of files in
the application.

The paper only shows more recent Python versions, but these files have
all the Python versions in the 2.x and 3.x series.  There are some
quirks: for example, 2.7.2 is slightly different from 2.7, and 2.4.3
is slightly different from 2.4.  Also, later Pythons like 3.5 are
actually 3.5.0 etc.


## fig3-commits.csv

The percentage of commits for each application in the Qualitas corpus,
for each version in the Python 3 series.  The percentage is
'on-or-after', hence the repeats.  The last column is the total number
of commits in the git repo for that application.

## fig4-compliance.csv

One row per Qualitas application, one column for each year from
2005-2016 inclusive.  The data shows the Python version we got the
best pass rate for, and that pass rate in parentheses.  There's a dash
if we didn't get a version from that year: in Fig 4 we just copy the
value from the previous year, since this is thus the compliant version
for that year too.

## table2-backport.csv

The backported 3.x features; this is a count of the number of them
that occur.

## table3-backport.csv

The 3.x backported features; this is a count of the number of files
that contain at least one such feature.

