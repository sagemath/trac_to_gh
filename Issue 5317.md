# Issue 5317: DeprecationWarning in pickle_jar is not pre-determined

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-20 06:38:39

Assignee: mabshoff

The output of deprecation warnings can vary:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc3/devel/sage-main/sage/structure/sage_object.pyx", line 682:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    Successfully unpickled 448 objects.
    Failed to unpickle 0 objects.
**********************************************************************
```

I have hit this once for literally thousands of doctest runs so far, so I don't think this will be a big problem.

Cheers,

Michael


---

Comment by tscrim created at 2014-08-07 00:54:56

This was fixed at some point.


---

Comment by tscrim created at 2014-08-07 00:54:56

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-08-10 20:20:44

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-20 20:32:54

Resolution: fixed
