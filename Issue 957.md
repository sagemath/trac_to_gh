# Issue 957: scipy is misbuilt on os x

Issue created by migration from https://trac.sagemath.org/ticket/957

Original creator: was

Original creation time: 2007-10-21 05:57:34

Assignee: was

Importing linsolve breaks on os x right now (I've removed the test
that exposes this for sage-2.8.8, but want this fixed. 


```
bsd0:~/s was$   sage -t  devel/sage-main/sage/numerical/test.py
sage -t  devel/sage-main/sage/numerical/test.py             **********************************************************************
File "test.py", line 9:
    : from scipy import linsolve
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        from scipy import linsolve###line 9:
    : from scipy import linsolve
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/__init__.py", line 5, in <module>
        import umfpack
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/umfpack/__init__.py", line 3, in <module>
        from umfpack import *
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/linsolve/umfpack/umfpack.py", line 11, in <module>
        import scipy.sparse as sp
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/sparse/__init__.py", line 5, in <module>
        from sparse import *
      File "/Users/was/s/local/lib/python2.5/site-packages/scipy/sparse/sparse.py", line 14, in <module>
        from scipy.sparse.sparsetools import cscmux, csrmux, \
    ImportError: cannot import name cscmux
```



---

Comment by was created at 2007-10-21 12:38:37

From Josh:

```
Thats odd, I have a sage-2.8.2 on OSX where all the commands in
numerical/test.py work fine.

Did something change in the scipy package to make it use umfpack for
sparse stuff. By default it uses superlu, but it can use umfpack.

Only think I can think of at the moment, did the order of scipy and cvxopt
change, cvxopt builds umfpack, but scipy was building before cvxopt so
wasn't using cvxopt's umfpack.
```



---

Comment by mabshoff created at 2007-11-03 12:11:14

What is the current status of this?

Cheers,

Michael


---

Comment by jkantor created at 2007-11-21 02:10:01

On a fresh install based on 2.8.13.rc1, I cannot duplicate this bug. Since I never could, could someone else using OSX verify that 

from scipy import linsolve 
from scipy import sparse 

do not raise exceptions so we can close this bug.


---

Comment by mabshoff created at 2007-11-22 23:23:10

it also work for me with 2.8.13.rc2 on a G4 on 10.4, so close this.


---

Comment by mabshoff created at 2007-11-22 23:23:10

Resolution: fixed
