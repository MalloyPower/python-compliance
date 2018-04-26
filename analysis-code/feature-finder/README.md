# Feature-finder

This directory contains code to recognize and count the 3x features 
in Python 2x. Counting is accomplished in the parser file, parse.y.

The directory was initialized using the stable version of our Python
2.7 front-end - see the 'parser' directory.  Actions are then added to
parse.y to enable recognition of 3.x features already incorporated
into the 2.7 Python parser.  

The detected features include:

  1. curly brackets for set syntax
  2. Dictionary and set comprehensions
  3. Extra parens are illegal for function parameters

#3 is by far the most difficult because parens are legal in so many
situations. But the basic idea is that (1) extra parens are legal
in 2x but illegal in 3x, and (2) 2x is supposed to give a warning
about extra parens but 3x should give a syntax error, as specified by:

https://docs.python.org/3/whatsnew/2.7.html

BTW: I have not received a warning for extra parens using the 2.7.12 
interpreter that's default on my linux 16.04 platform.


For example, the following is legal in 3x:

   x = ((1+2))/5


  def f(x, y):
    print(x, y[0], y[1])
  f(2, (3, 4))

but the following is illegal:

   def f(a, (b,c)):
     pass

   def g(a, ((b))):
     pass

   def h(a, (b)):
     pass

Since parens are used in so many expressions, including tuple
construction, the grammar productions for parens are recursive.
Thus, to recognize "extra parens" that receive a warning in 2x
but are illegal in 3x, we need to pass information up the semantic
stack using $$, $1, etc.

