# Issue 7758: doctest failure on OS X 10.5 intel due to randomization

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-24 07:52:44

Assignee: tbd


```
sage -t -long "devel/sage/sage/numerical/mip.pyx"**********************************************************************
File "/Users/wstein/build/sage-4.3.rc1/devel/sage/sage/numerical/mip.pyx", line 364:
    sage: p.show()
Expected:
    Maximization:
      x0 + x1
    Constraints:
      -3*x0 + 2*x1 <= 2
    Variables:
      x1 is a real variable (min=0.0, max=+oo)
      x0 is a real variable (min=0.0, max=+oo)
Got:
    Maximization:
      x0 + x1
    Constraints:
      -3*x0 + 2*x1 <= 2
    Variables:
      x0 is a real variable (min=0.0, max=+oo)
      x1 is a real variable (min=0.0, max=+oo)

```



---

Comment by was created at 2009-12-24 07:55:47

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2009-12-24 07:59:32

I merged this into 4.3.rc2 anyways, since 4.3 is lingering forever.   I'm leaving this as "needs review" though.


---

Attachment


---

Comment by ncohen created at 2009-12-24 22:26:16

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-25 10:01:40

Resolution: fixed
