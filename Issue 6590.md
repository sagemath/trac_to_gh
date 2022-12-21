# Issue 6590: [with patch, needs review] Cython __new__ should be __cinit__

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-07-22 14:21:15

Assignee: tbd

This changed a while back, but as long as the old form is in the library we won't be able to really implement a (Python-style) `__new__` and also people will keep using it in new code by analogy. 


---

Attachment

How come the some of the new __cinit__ functions have different signatures from the corresponding __init__ functions?  I thought the signatures should be the same, or at least the __cinit__ should have a *args or **kwds to accept the arguments passed to __init__


In particular, I refer to sage/libs/ntl/ntl_mat_GF2.pyx, sage/libs/ntl/ntl_mat_ZZ.pyx,  sage/matrix/matrix_integer_2x2.pyx, etc.


---

Comment by robertwb created at 2009-07-25 10:55:56

If no __init__ parameters are not needed by __cinit__ they can simply be omitted. This saves on argument-parsing code, especially as **kwds needs to construct an empty dictionary each time. Also note that __cinit__ is called on PY_NEW, so the savings here is really nice. (Essentially, `__cinit__(self)` is implicitly `__cinit__(self, *args, **kwds)` where *args and **kwds are not parsed because they're not needed.


---

Attachment

rebased against sage-4.1.1, apply instead of previous patch


---

Comment by AlexGhitza created at 2009-08-17 14:07:36

Positive review.  I had to rebase it against sage-4.1.1 since it didn't apply cleanly.


---

Comment by mvngu created at 2009-08-24 13:06:16

Merged `6590-cinit_rebased.patch`.


---

Comment by mvngu created at 2009-08-24 13:06:16

Resolution: fixed
