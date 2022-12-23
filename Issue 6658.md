# Issue 6658: digits() claims it defaults to base 2, but it defaults to base 10

Issue created by migration from https://trac.sagemath.org/ticket/6658

Original creator: ddrake

Original creation time: 2009-07-30 03:03:24

Assignee: somebody


```
sage: x = 1729
sage: x.digits()
[9, 2, 7, 1]
```

but the docstring for `digits()` claims it defaults to base 2. The attached patch fixes this; thanks to Yasuhide NUMATA at the *-combinat meeting for noticing this. I would have shown him how to make a patch and upload it to trac, but their wireless network was down at the time.


---

Comment by ddrake created at 2009-07-30 03:34:12

Changing status from new to assigned.


---

Comment by ddrake created at 2009-07-30 03:34:12

Changing assignee from somebody to ddrake.


---

Attachment

I also edited a bit of the docstring.


---

Comment by ddrake created at 2009-07-30 03:34:12

Changing component from basic arithmetic to documentation.


---

Comment by timdumol created at 2009-07-30 12:34:33

Applied the patch on r12658. Doctest passed, seems ok.


---

Comment by mvngu created at 2009-08-03 06:08:20

Resolution: fixed
