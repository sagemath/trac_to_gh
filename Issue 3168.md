# Issue 3168: Source introspection does not work for outside Cython extensions

Issue created by migration from https://trac.sagemath.org/ticket/3168

Original creator: dunfield

Original creation time: 2008-05-12 19:34:17

Assignee: cwitty

If you take a simple Cython extension module and install it in into SAGE via

```
sage -python setup.py install
```

source introspection will not work.   

This appears to caused by two things

1) cython is invoked without the "-p" option

2) the relevant *pyx files are not put somewhere that the Sage interpreter can find them.

Attached is a minimal Cython module illustrating the problem.   Source introspection can be made to work via


```
sage -cython -p introtest.pyx
sage -python setup.py install
cp introtest.pyx $SAGEROOT/devel/sage/
}}


---

Attachment

Minimal example


---

Comment by dunfield created at 2008-05-12 19:35:14

Minimal example


---

Attachment


---

Comment by dunfield created at 2008-05-12 19:36:49

Changing priority from trivial to minor.


---

Comment by AlexGhitza created at 2009-01-23 02:46:35

Changing type from defect to enhancement.
