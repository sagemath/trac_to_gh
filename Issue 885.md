# Issue 885: 2.8.7-alpha0: doctest failure in rings/morphism.pyx (loads/dumps)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-13 20:23:36

Assignee: failure

On sage.math:

```
File "morphism.pyx", line 312:
    sage: c == loads(dumps(c))
Expected:
    True
Got:
    False
```



---

Attachment

Changed class RingHomomorphism_im_gens to use _cmp_c_impl (this is necessary to make Python subclasses compare correctly).


---

Comment by was created at 2007-10-14 22:56:00

Resolution: fixed
