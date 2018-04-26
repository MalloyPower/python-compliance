from collections import OrderedDict
from datetime import date

# Python major releases:
s1_releases = [
	('1.6', date(2000, 9, 5)),
	('1.5', date(1998, 2, 17)),
	('1.4', date(1996, 10, 25)),
        ]
s2_releases = [
	('2.7', date(2010, 7, 4)),
	('2.6', date(2008, 10, 1)),
	('2.5', date(2006, 9, 19)),
	('2.4', date(2004, 11, 30)),
	('2.3', date(2003, 7, 29)),
	('2.2', date(2001, 12, 21)),
	('2.1', date(2001, 4, 15)),
	('2.0', date(2000, 10, 16)),
        ]
s3_releases = [
	('3.6', date(2016, 12, 23)),
	('3.5', date(2015, 9, 13)),
	('3.4', date(2014, 3, 16)),
	('3.3', date(2012, 9, 29)),
	('3.2', date(2011, 2, 20)),
	('3.1', date(2009, 6, 27)),
	('3.0', date(2008, 12, 3)),
        ]

# Store releases in an ordered dictionary, newest version first
releases = OrderedDict(sorted(s1_releases+s2_releases+s3_releases,
                              key=lambda r:r[1], reverse=True))


def get_releases(filter=None):
    ''' Return a list of major version names, in version order '''
    versions = [v for v in releases.keys()
                if not filter or v.startswith(filter)]
    return sorted(versions)

def version_at(adate, filter=None):
    ''' Return the most recent Python release available at the given date '''
    for ver, rel_date in releases.items():
        if adate > rel_date and (not filter or ver in filter):
            return ver
    return None # Earlier than the earliest release!

def print_versions(filter=None):
    for ver, rel_date in releases.items():
        if (not filter) or ver.startswith(filter):
            nicedate = rel_date.strftime('%Y-%m-%d')
            print(ver, ':', nicedate)

# Just testing
if __name__ == '__main__':
    print_versions()
    for yr in range(1995, 2017):
        print('At end of', yr, 'it was', (version_at(date(yr, 12, 31))))
    
