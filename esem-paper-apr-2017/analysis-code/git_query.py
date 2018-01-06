# This is where I do most of the rooting around in the Git repos.
# Uses GitPython: https://github.com/gitpython-developers/GitPython

import os
import sys
from datetime import date

from git import Repo  # GitPython

import qualitas
import python_versions


class CategoriseDates:
    '''Receive application release dates, store them based on the Python
       release that was 'current' at that date.
    '''
    def __init__(self, pyversions, name, datelist=[]):
        self.name = name
        self.pyversions = pyversions
        # Map Python versions to no of commits for that version:
        self.dates = {k:0 for k in self.pyversions}
        self.earlier = 0 # Count dates outside the range
        for rdate in datelist:
            self.add_date(rdate)
    def add_date(self, rdate):
        ''' File this release date under the appropriate Python version '''
        ver = python_versions.version_at(rdate, self.pyversions)
        if ver:
            self.dates[ver] += 1
        else:  # date not in the range for these releases
            self.earlier += 1
    def count_date(self):
        ''' Return list with no. of releases for each python version '''
        return[self.dates[pyver] for pyver in self.pyversions]
    def count_cumulative(self):
        ''' Return list with no. of releases *on or after* each version '''
        on_or_after = []
        for i,pyver in enumerate(self.pyversions):
            me_or_after = [self.dates[v] for v in self.pyversions[i:]]
            on_or_after.append(sum(me_or_after))
        return on_or_after
    def __getitem__(self, key):
        return self.dates.get(key, 0)
    def get_total(self):
        return sum(self.dates.values())
    def get_counted(self):
        return self.get_total() + self.earlier
    def __str__(self):
        vers = sorted(self.dates.keys())
        return ','.join(['%s:%d' % (v,self.dates[v]) for v in vers])
            

def get_tagged_commits(qapp):
    ''' Return (commit,name) pairs for this application's tagged releases '''
    repo = Repo(qualitas.file_for(qapp))
    ct_dict = { tr.commit:tr for tr in repo.tags }
    return ct_dict


def tagref2namedate(repo, tagref):
    ''' Return (name,date) pair for a given tagref '''
    this_name = tagref.name
    this_commit = tagref.commit # More details in the commit
    if this_commit:
        this_date = date.fromtimestamp(this_commit.committed_date)
        return (this_name, this_date)
    return None

def get_tag_dates(qapp):
    ''' Return (name,date) pairs for this application's tagged releases '''
    repo = Repo(qualitas.file_for(qapp))
    # Now collect the data from the 'tagged' commits:
    ndlist = [tagref2namedate(repo, tagref) for tagref in repo.tags]
    return [nd for nd in ndlist if nd]  # Filter out any blanks

def get_latest_for(qapp, pyver):
    ''' Return tag for the latest version of app matching a Python version.
        Can return None if there is no such version of the app.
    '''
    datelist = get_tag_dates(qapp)
    pyseries = python_versions.get_releases(pyver[0])
    pd = CategoriseDates(pyseries, qapp, datelist)
    if len(pd[pyver]) == 0: # No releases for this version
        return None
    latest = max(pd[pyver], key=lambda r:r[1]) # Sort on date
    return latest

def count_commits(qapp):
    ''' Return the total number of (unique) commits in a repo '''
    counted = set()
    repo = Repo(qualitas.file_for(qapp))
    for c in repo.iter_commits():
        if not c in counted:
            #print(c.binsha, c.committed_date)
            counted.add(c.binsha)
    return len(counted)

def latest_commit(repo):
    ''' Return the latest commit inn  a repo '''
    latest = None
    for c in repo.iter_commits():
        if (not latest) or c.committed_date > latest.committed_date:
            latest = c
    return c

def categorise_tags(pyvers, qapp):
    ''' Return count of number of tags for each Python version'''
    datelist = get_tag_dates(qapp)
    pd = CategoriseDates(pyvers, qapp, datelist)
    return (pd.count_date(), pd.get_counted())

def categorise_commits(pyvers, qapp):
    ''' Return cumulative number of commits on-or-after each Python version'''
    repo = Repo(qualitas.file_for(qapp))
    pd = CategoriseDates(pyvers, qapp)
    counted = set()
    for c in repo.iter_commits():
        if not c in counted:
            pd.add_date(date.fromtimestamp(c.committed_date))
            counted.add(c)
    return (pd.count_cumulative(), pd.get_counted())


### Printing routines ###

def latex_table_row(data, effect=None, want_hline=False):
    lstr = lambda s: ('\\text%s{%s}' % (effect,s)) if effect else str(s)
    row_str = ' & '.join([lstr(d) for d in data]) + '\\\\'
    if want_hline:
        row_str += '\n\\hline'
    return row_str

def print_date_counts(pyvers, qualapps, num_and_perc, categorise):
    perc = lambda c,t: 0 if t==0 else round(c*100/t)
    print('\\begin{tabular}{l*{%d}{c}r}' % len(pyvers))
    titles = ['Application'] + pyvers + ['Total']
    print(latex_table_row(titles, 'bf', True))
    for qapp in qualapps:
        counts, row_tot = categorise(pyvers, qapp)
        if num_and_perc: #Print number, shade by percentage
            this_row = ['\\shadeper{%d}{%d}' % (d, perc(d, row_tot))
                        for d in counts]
        else:  # Just print the percentage
            this_row = ['%d' % perc(d, row_tot) for d in counts]
        this_row = [qapp] + this_row + [row_tot]
        print(latex_table_row(this_row))
    print('\\hline')
    print('\\end{tabular}')


if __name__ == '__main__':
    full_suite = qualitas.get_dirnames()
    qualapps = [ ]
    for arg in sys.argv[1:]:
        if arg in full_suite:
            qualapps.append(arg)
        else:
            safe_print('Unkown argument: "%s"' % arg, sys.stderr)
            sys.exit(1)
    if qualapps == []: # None specified, so test *all* the applications
        qualapps = full_suite
    pyvers = python_versions.get_releases('3')
    print_date_counts(pyvers, qualapps, False, categorise_commits)
    
