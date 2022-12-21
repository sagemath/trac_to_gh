# Issue 1327: 2.8.14/Solaris: scipy import error - fortran compiler related

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-28 22:20:19

Assignee: jkantor

On a Solaris box woth gfortran I get odd import errors with scipy:

```
File "test.py", line 6:
    : from scipy import optimize
Exception raised:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/sage-2.8.14/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        from scipy import optimize###line 6:
    : from scipy import optimize
      File "/tmp/Work-mabshoff/sage-2.8.14/local/lib/python2.5/site-packages/scipy/optimize/__init__.py", line 11, in <modul
e>
        from lbfgsb import fmin_l_bfgs_b
      File "/tmp/Work-mabshoff/sage-2.8.14/local/lib/python2.5/site-packages/scipy/optimize/lbfgsb.py", line 30, in <module>
        import _lbfgsb
    ImportError: ld.so.1: /tmp/Work-mabshoff/sage-2.8.14/local/bin/python: fatal: relocation error: file /tmp/Work-mabshoff/
sage-2.8.14/local/lib/python/site-packages/scipy/optimize/_lbfgsb.so: symbol G77_etime_0: referenced symbol not found
```


Cheers,

Michael


---

Comment by jkantor created at 2007-12-01 19:48:22

I think this will fix this, not tested though since I don't have solaris

http://sage.math.washington.edu/home/jkantor/spkgs/numpy-20071020-1.0.3.1.p2.spkg


---

Comment by mabshoff created at 2007-12-01 22:27:47

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 22:27:47

Merged in 2.8.15.alpha2.

Works on Solaris :)
