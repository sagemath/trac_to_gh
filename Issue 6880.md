# Issue 6880: docstrings and @cached_method -- if you used cached_method then docstring displays wrong file, etc.

Issue created by migration from https://trac.sagemath.org/ticket/6880

Original creator: was

Original creation time: 2009-09-03 17:22:16

Assignee: tba

If you used the ``@`cached_method` decorator when defining a function in the Sage library, then get help about it (either in the notebook or command line), the File: field lis as follows:


```
File:           /.../local/lib/python2.6/site-packages/sage/misc/cachefunc.py
```


That's of course technically right, but very wrong/misleading for the user, who maybe wants to know more.  We should add specialized code to IPython and the notebook to correct for this. 


---

Comment by SimonKing created at 2012-06-25 09:09:34

This problem has already been fixed (by some work in sage.misc.sageinspect - sorry, I am too lazy to look up the ticket number). For example:

```
sage: P.<x,y> = QQ[]
sage: I = P*[x,y]
sage: I.groebner_basis?
Type:           CachedMethodCaller
Base Class:     <type 'sage.misc.cachefunc.CachedMethodCaller'>
String Form:    Cached version of <function groebner_basis at 0x1507b18>
Namespace:      Interactive
Loaded File:    /home/simon/SAGE/sage-5.0/local/lib/python2.7/site-packages/sage/misc/cachefunc.so
Source File:    /home/simon/SAGE/sage-5.0/devel/sage/sage/misc/cachefunc.so
Definition:     I.groebner_basis(self, algorithm='', deg_bound=None, mult_bound=None, prot=False, *args, **kwds)
Docstring:
    File: sage/rings/polynomial/multi_polynomial_ideal.py (starting at line 3476)
...
```


Hence, we can close this.


---

Comment by SimonKing created at 2012-06-25 09:09:34

Changing status from new to needs_review.


---

Comment by SimonKing created at 2012-06-25 09:09:58

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-07-04 07:17:21

Resolution: worksforme
