# A corpus of Python programs

For this paper we analysed several sets of Python programs.  The whole
set is rather large, so we don't hold the actual programs here, but we
do supply information on how to replicate the corpus.


## Qualitas:

We used the same applications as the original, but the most up-to-date
versions in each case.  Since these all came from github, look in
[qualitas.csv](./qualitas.csv)
for the URL and the SHA of the commit we were using.


## The programs studied by Chen et al.

For those downloaded from GitHub, details are in [linchen.csv](./linchen.csv)

* SEKE 2015:<br/>
  5 in Qualitas: Django Matplotlib Numpy Scipy Tornado<br/>
  Need to get 2 more: Boto and Bzr<br/>
  Bzr was not on git, so we used:
  https://launchpad.net/bzr/2.7/2.7.0/+download/bzr-2.7.0.tar.gz
* SATE 2016: django ipython matplotlib scipy numpy<br/>
  all part of anaconda or Qualitas.<br/>
* ICSME 2016 (10 applications)<br/>
  5 in Qualitas: Django Tornado Numpy Scipy Sympy<br/>
  Need to get 5 more: Pylearn2 Pandas Nltk Beets Mopidy<br/>
* ICSE 2017: Scipy<br/>
  downloaded anaconda3, Anaconda3-4.3.1-Linux-x86_64<br/>
  analysed /pkgs folder, URL and SHA listed in [anaconda.txt](./anaconda.txt)
  (this file is 'urls' from the anaconda distribution).


## The applications studied by Destefanis et al

5 were done already: Biopython Calibre Matplotlib Py-Pandas Sage<br/>

Just needed five more, all from GitHub, and details in
[destefanis.csv](./destefanis.csv)


## The list of "Notable Ports" from getpython3.com

Three already in Qualitas: Django, Pyramid, NumPy, SciPy<br/>
One in Chen et al: Pandas<br/>
Downloaded the others, list in [getpython3.txt](./getpython3.txt)


## The top 20 "most starred" and top 20 "most forked" on GitHub

All from GitHub, details in [top20-github.csv](./top20-github.csv)


