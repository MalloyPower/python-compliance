''' Goal: roll-back a Qualitas application to a given date,
    and then test this with the front-ends.
    Select the date based on a Python version.
'''

import os
import sys
import subprocess
import shutil

import platform
from git import Repo

import qualitas
import qualitas_test
import git_query

TEMP_BRANCH_NAME = 'jpower_rollback_crazyexperiment' # Should be distinctive

def restore_one(qapp, old_head):
    ''' Put the GIT repo for an app back the way you found it.
        Specifically, restore HEAD to master, and delete rollback branch.
    '''
    try:
        repo = Repo(qualitas.file_for(qapp))
        with repo.config_writer():
            repo.head.reference = old_head
            repo.head.reset(index=True, working_tree=True)
            repo.git.branch('-D', TEMP_BRANCH_NAME)  # delete the temp branch
    except (Exception) as err:
        print('### Unable to restore', qapp)
        print(err)


def rollback_one(repo, qapp, tagname):
    ''' Roll an app back to the given tag (point the HEAD at it).
        So we can undo later, make a branch called TEMP_BRANCH_NAME for this.
        Return the original HEAD (mostly 'master').
    '''
    with repo.config_writer():
        old_head = repo.heads[0]  # Mostly 'master' but not always
        tagref = repo.tags[tagname]
        new_branch = repo.create_head(TEMP_BRANCH_NAME, tagref)
        repo.head.reference = new_branch
        repo.head.reset(index=True, working_tree=True)
    return old_head

def rollback_all(pyversion, qualapps):
    ''' Roll-back all the apps in qualapps to the date of pyversion.
        Silently ignore an app if it has no release for pyversion.
        Return a list of what you did, so we can restore them later.
    '''
    rolledback = [ ] # List of (app, head-name) pairs
    for qapp in qualapps:
        latest = git_query.get_latest_for(qapp, pyversion)
        if not latest:  # App was not released back then
            continue
        try:
            repo = Repo(qualitas.file_for(qapp))
            print('Roll', qapp, 'back to version', latest[0], 'of', latest[1])
            old_head = rollback_one(repo, qapp, latest[0])
            if old_head:
                details = '%s & %s & %s' % (qapp, latest[0], latest[1])
                rolledback.append((qapp, old_head, details))
        except (Exception) as err:
            print('### Unable to rollback', qapp)
    return rolledback


def test_at_pyversion(pyversion, qualapps):
    rolledback = rollback_all(pyversion, qualapps)
    qualapps = [qapp for (qapp,_,_) in rolledback]
    labels = [details for (_,_,details) in rolledback]
    test_with = qualitas_test.SERIES2
    try:
        percs = qualitas_test.test_all(test_with, qualapps)
        qualitas_test.print_latex_table(test_with, qualapps,
                                        qualitas.get_root_dir(),
                                        percs, labels)
    except: # Want to make sure I do 'restore_one' no matter what...
        print('Exception running test harness', file=sys.stderr)
    for qapp, old_head, _ in rolledback:
        restore_one(qapp, old_head)


def test_at_commit(pyvers, qapp, acommit):
    percs = [ ]
    repo = Repo(qualitas.file_for(qapp))
    old_head = repo.heads[0]  # Mostly 'master' but not always
    repo.head.reset(commit=acommit, index=True, working_tree=True)
    try:
        percs = qualitas_test.test_all(pyvers, [qapp])
    except: # Want to make sure I do 'restore_one' no matter what...
        print('Exception running test harness', file=sys.stderr)
    # Now, put it back the way you found it:
    repo.head.reference = old_head
    repo.head.reset(index=True, working_tree=True)
    repo.close()
    return percs[0] # One entry for each Python version we tried
      
        
if __name__ == '__main__':
    versions, qualapps = qualitas_test.get_pyvers_qualapps(sys.argv[1:])
    # Only test series 2 Pythons...
    versions = [v for v in versions if v in qualitas_test.SERIES2]
    for pyver in versions:
        test_at_pyversion(pyver, qualapps)
