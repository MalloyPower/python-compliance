### PyComply

This is the source code for PyComply: basically a parser and scanner
for various versions of Python 2 and Python 3.  Default behaviour of
PyComply is to report any syntax errors and some (very) basic counts.
It sets an appropriate error code when it completes: this is important
when we're just looking for pass/fail rates.

This is really intended to be run using the qualitas_test.py test
harness, but it can work stand-alone.  The parsers/ and scanners/
sub-directories contain flex and bison files for the various versions.
So we copy a pair of these into this directory, and just do a 'make'
here, which then builds the executable (rather unimaginatively called
'run').

Apart from the multiplicity of versions, this is all very standard,
and (we hope) will work for any standard combination of flex, bison
and your C compiler (we use gcc).
