# Issue 7286: After installing sphinx-0.6.3.p1.spkg, error occurs during docbuild

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-10-25 03:53:47

Assignee: mabshoff

> 11:24 < williamstein> I tried "sage -upgrade" on a clean install (the systemwide one) on geom.math.

> 11:24 < williamstein> It fails with:

> 11:24 < williamstein>   File "/usr/local/sage/local/lib/python2.6/site-packages/Sphinx-0.6.3-py2.6.egg/sphinx/environment.py", line 204, in frompickle

> 11:24 < williamstein>     env = pickle.load(picklefile)

> 11:24 < williamstein> AttributeError: 'module' object has no attribute 'RedirStream'


---

Comment by timdumol created at 2009-10-25 03:58:25

Has the updated package: http://sage.math.washington.edu/home/timdumol/sphinx-0.6.3.p2.spkg


---

Comment by timdumol created at 2009-10-25 03:58:25

Changing status from new to needs_review.


---

Comment by was created at 2009-10-25 04:21:12

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-10-25 04:21:38

Resolution: fixed
