# Issue 7727: optimized_representation fails,

Issue created by migration from https://trac.sagemath.org/ticket/7727

Original creator: syazdani

Original creation time: 2009-12-17 20:50:02

Assignee: davidloeffler

The following code fails with cryptid PariError:

```
sage: L.<a>=NumberField(x^3+2/3*x+3)
sage: L.optimized_representation()
```


The exact failure happens on the command f.polred(2), but I'm not sure what's wrong with it.


---

Comment by chapoton created at 2013-08-20 13:04:55

This is related to #252


---

Comment by mmezzarobba created at 2018-03-23 08:52:22

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2018-03-23 08:52:22

Fixed in #252, which also adds a similar test.


---

Comment by mmezzarobba created at 2018-03-23 08:52:32

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix
