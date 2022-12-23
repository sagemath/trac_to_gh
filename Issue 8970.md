# Issue 8970: conversion of integer mods to Gap

Issue created by migration from https://trac.sagemath.org/ticket/8970

Original creator: davidloeffler

Original creation time: 2010-05-14 20:57:25

Assignee: AlexGhitza

The code to convert elements of integer mod rings into Gap elements is needlessly complicated, and also very broken when the modulus isn't prime. 


---

Attachment

patch against 4.4.1


---

Comment by davidloeffler created at 2010-05-15 18:34:56

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-05-15 18:34:56

Here's a patch, which takes care of conversion in both directions.


---

Comment by rlm created at 2010-06-22 16:40:37

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-22 16:40:37

Looks good to me.


---

Comment by mpatel created at 2010-07-20 09:26:03

Resolution: fixed
