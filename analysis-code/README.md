This is basically a test harness for pycomply: the goal is to manage
building and running pycomply over some test input, and to record the
results.

The main program here is qualitas_test.py; as arguments you can give
ti a Python version and an application (sub-directory actually) in the
Qualitas corpus.  If you don't give it these, it will run all versions
over all applications: this may take a while.

You need to set the path to your version of this corpus in the file
qualitas.py: see the variable QUALITAS_ROOT there.


Example:
        python3 qualitas_test.py 2.7 3.5 gramps django


The output is a latex table showing the percentage pass rate for each
application and each version.



