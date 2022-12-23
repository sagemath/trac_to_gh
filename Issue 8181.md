# Issue 8181: cannot coerce residue field back to p-adic ring

Issue created by migration from https://trac.sagemath.org/ticket/8181

Original creator: dmharvey

Original creation time: 2010-02-03 23:35:50

Assignee: roed

CC:  roed mjo

I should be able to coerce elements of the residue field of a p-adic ring back into the ring, but I can't:


```
sage: R.<z> = Zq(9)
sage: F = R.residue_class_field()
sage: F
Finite Field in z0 of size 3^2
sage: a = F.gen()
sage: R(a)
---------------------------------------------------------------------------
TypeError
```




---

Comment by dmharvey created at 2010-02-03 23:36:33

see also the thread:

http://groups.google.com/group/sage-support/browse_thread/thread/ce14b31005ec053a


---

Comment by mjo created at 2012-01-13 19:46:42

This works now:


```
sage: R.<z> = Zq(9)
sage: F = R.residue_class_field()
sage: F
Finite Field in z0 of size 3^2
sage: a = F.gen()
sage: R(a)
z + O(3)
```


I can create a patch with a doctest, but I don't know if the result is correct. Does it look about right?


---

Comment by saraedum created at 2016-03-20 20:46:22

Changing status from new to needs_review.


---

Comment by saraedum created at 2016-03-20 20:46:22

It was fixed in the meantime. A added a standard test for it.


---

Comment by saraedum created at 2016-03-20 20:47:32

New commits:


---

Comment by aly.deines created at 2016-03-21 15:59:03

Changing status from needs_review to positive_review.


---

Comment by aly.deines created at 2016-03-21 15:59:03

Looks good.


---

Comment by aly.deines created at 2016-03-23 15:25:06

Changing keywords from "" to "sd71".


---

Comment by aly.deines created at 2016-03-23 17:43:45

Changing keywords from "sd71" to "days71".


---

Comment by jdemeyer created at 2016-04-04 16:51:02

Doesn't apply according to the patchbot.


---

Comment by jdemeyer created at 2016-04-04 16:51:02

Changing status from positive_review to needs_work.


---

Comment by roed created at 2016-11-20 01:03:19

Fixed the merge problem.
----
New commits:


---

Comment by roed created at 2016-11-20 01:03:19

Changing status from needs_work to needs_review.


---

Comment by saraedum created at 2016-11-30 01:42:22

Changing status from needs_review to positive_review.


---

Comment by saraedum created at 2016-11-30 01:42:44

The increase in startup reported by the patchbot is just noise.


---

Comment by vbraun created at 2016-12-01 22:32:49

Resolution: fixed
