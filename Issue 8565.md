# Issue 8565: atan2(-pi,0) throws "divide by zero"

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-03-20 10:33:22

Assignee: burcin

Keywords: pynac

From sage-devel:


```
the summary is:
-------------------
atan2(3,0)   --> 1/2*pi
atan2(-3,0)  --> -1/2*pi
atan2(pi,0)  --> 1/2*pi
atan2(-pi,0) -->  RuntimeError: power::eval(): division by zero
--------------------
```


sage-devel thread is here:

http://groups.google.com/group/sage-devel/t/317e6bfe11fabb4

also reported on sage-support:

http://groups.google.com/group/sage-support/t/02f3446e68381346



---

Comment by burcin created at 2010-04-02 14:48:19

add doctests


---

Attachment

The pynac package at #8644 includes the patches that were merged in `GiNaC` to fix this problem. attachment:trac_8565-neg_pi.patch adds doctests for the fix.

This ticket now depends on #8644.


---

Comment by burcin created at 2010-04-02 14:52:12

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-04-09 11:09:42

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2010-04-09 11:09:42

Installs fine, all tests passed, works ad advertised. Positive review and thanks for fixing.


---

Comment by was created at 2010-04-29 04:13:43

Resolution: fixed
