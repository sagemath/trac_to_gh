# Issue 7829: implement hex for real numbers

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-03 05:37:30

Assignee: AlexGhitza


```
sage: float(e).hex()
'0x1.5bf0a8b145769p+1'
sage: RR(e).hex()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
AttributeError: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'hex'
```


There should probably be a __hex__ method as well, so hex(2.3) works. 


---

Comment by mmezzarobba created at 2014-05-29 07:07:43

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-05-29 07:07:43

New commits:


---

Comment by mmezzarobba created at 2014-05-29 07:07:43

Changing component from algebra to basic arithmetic.


---

Comment by git created at 2014-05-29 07:16:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by robertwb created at 2014-05-29 16:14:51

Does the C string need to be freed in the error case as well? In that case you could use a finally clause (and just "return s")

Could you add a test showing that hex(RR(x)) works too?


---

Comment by jkeitel created at 2014-05-29 18:46:02

Just a short comment: I think the new syntax for exceptions should be used, i.e. `raise RuntimeError("...")`.


---

Comment by git created at 2014-05-30 07:55:03

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mmezzarobba created at 2014-05-30 07:56:28

Replying to [comment:3 robertwb]:
> Does the C string need to be freed in the error case as well?

As far as I understand, no, it doesn't.

> Could you add a test showing that hex(RR(x)) works too?

Done.


Replying to [comment:4 jkeitel]:
> I think the new syntax for exceptions should be used, i.e. raise RuntimeError("...").

Fixed, thanks!


---

Comment by robertwb created at 2014-06-04 07:24:17

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-06-04 14:48:09

Resolution: fixed
