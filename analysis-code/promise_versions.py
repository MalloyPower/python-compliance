# These are the Qualitas system versions as used in the Promise paper.
# In most cases I got these from the spreadsheet, but for some (noted below)
# this was blank, and I had to get them from Fig 1 of the APSEC 2015 paper.
# In some cases the tag was slightly incorrect, so I edited it.


import os
import sys

# Uses GitPython: https://github.com/gitpython-developers/GitPython
from git import Repo
from git.exc import InvalidGitRepositoryError

import git_query
import qualitas


promisever = {
    'EventGhost' : 'v0.4.1.r1640',
    'Pillow' : '2.8.1',
    'Pyro4' : '4.35',
    'VisTrails' : 'v2.2-pre',
    'Zope' : '2.13.22',
    'astropy' : 'v1.0rc1',
    'biopython' : 'biopython-165',
    'buildbot' : 'v0.9.0-pre',
    'calibre' : 'v2.23.0',
    'cherrypy' : '3.5.0',
    'cinder' : '2015.1.0b3',
    'django' : '1.7a2',
    'emesene' : 'v2.12.9',
    'exaile' : '3.4.4',
    'globaleaks' : 'v2.60.63',
    'gramps' : 'v2.90.0-beta',  # changed from 'gramps-2.90.0-beta',
    'gtg' : 'v0.3.1',  # changed from '0.3.1',
    'heat' : '2015.1.0rc1',
    'ipython' : 'rel-3.0.0',
    'kivy' : '1.9.0',
    'magnum' : '2015.1.0b2',
    'mailman' : '0.6c9',
    'manila' : '2015.1.0b3',
    'matplotlib' : 'v1.4.3',
    'miro' : 'v6.0',
    'networkx' : 'networkx-1.9.1',
    'neutron' : '2015.1.0b3',
    'nova' : '2015.1.0b3',
    'numpy' : 'pre-removal-numpybook',
    'pathomx' : 'v3.0.0a',
    'pip' : '6.1.1',
    'portage' : 'v2.2.18',
    'pygame' : 'release_1_9_1release',  # from the APSEC paper, changed from '1.9.1'
    'pyobjc' : 'pyobjc-3.0.4',  # from the APSEC paper, changed from '3.0.4'
    'pyramid' : '1.5',
    'python-api' : '1.6.12',
    'quodlibet' : 'release-3.0.1', # from the APSEC paper, changed from '3.0.1'
    'sabnzbd' : '0.7.11',
    'sage' : '6.5',
    'scikit-image' : 'v0.11.0',
    'scikit-learn' : '0.16-branching',
    'sympy' : 'sympy-0.7.6',
    'tg2' : 'tg2.3.4',
    'tornado' : 'v4.1.0',
    'trac' : '1.0',   # from the APSEC paper
    'tryton' : '3.4.0',
    'twisted' : 'twisted-15.0.0', # from the APSEC paper, changed from '15.0.0'
    'veusz' : 'veusz-1.22',
    'vpython-wx' : 'v6.11',
    'web2py' : 'R-2.10.3',
    'wxPython' : '1.5', 
}



def get_tag_date(qapp, tagname):
    ''' Return a date corresponding to this tagged release.
        If not found, return a list of possible alternatives.
    '''
    # Open the GIT repo if it's there:
    try:
        repo = Repo(qualitas.file_for(qapp))
    except InvalidGitRepositoryError as err:
        return (False, [])
    alternatives = [ ]
    for tagref in repo.refs:
        refname,refdate = git_query.tagref2namedate(repo, tagref)
        if refname == tagname:
            return (True, refdate)
        else:
            if refdate.year in [2014, 2015]:
                alternatives.append((refname,refdate))
    return (False, alternatives)


if __name__ == '__main__':
    apps = sorted(promisever.keys(), key=lambda s: s.lower())
    for qapp in apps:
        ver = promisever[qapp]
        print(qapp, ver, end=' ')
        found, date = get_tag_date(qapp, ver)
        if found:
            print(date)
        else:
            print('Not found!!!', '%d alternatives:' % len(date),
                  ['%s of %s' % nd for nd in date[:10]])

            
