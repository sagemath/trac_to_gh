# Issue 9764: matrix2.pyx: replace "x < 1e-15" by "abs(x) < 1e-15"

Issue created by migration from https://trac.sagemath.org/ticket/9765

Original creator: jhpalmieri

Original creation time: 2010-08-18 22:14:49

Assignee: AlexGhitza

In matrix2.pyx, there is a doctest (line 6406):

```
            sage: all(imag(e) < 1.1e-15 for e in eigs)
```

We should replace "imag(e)" by "abs(imag(e))".

The attached patch depends on #9760.



---

Comment by jhpalmieri created at 2010-08-18 22:16:48

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-08-23 01:16:05

The test still passes on bsd, redhawk, sage, and t2.math.


---

Comment by mpatel created at 2010-08-23 01:16:05

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-23 22:17:30

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-08-24 02:48:01

Resolution: fixed
