# Issue 9360: Sage 4.4.4 numerical noise in mwrank.pyx on 32-bit cicero

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-28 17:44:54

Assignee: jason, jkantor


```
Hi folks,

Doctesting Sage 4.4.4 on cicero.skynet, a 32-bit Pentium 4 machine, I
got the following numerical noise:

sage -t -long "devel/sage/sage/libs/mwrank/mwrank.pyx"
**********************************************************************
File "/tmp/mvngu/sage-4.4.4-9338-pycrypto/devel/sage/sage/libs/mwrank/mwrank.pyx",
line 340:
   sage: E.silverman_bound()
Expected:
   6.5222617951910102
Got:
   6.5222617951910111
**********************************************************************
File "/tmp/mvngu/sage-4.4.4-9338-pycrypto/devel/sage/sage/libs/mwrank/mwrank.pyx",
line 372:
   sage: E.silverman_bound()
Expected:
   6.5222617951910102
Got:
   6.5222617951910111

--
Regards
Minh Van Nguyen
```



---

Comment by was created at 2010-06-28 17:50:45

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-06-28 17:59:26

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-28 17:59:26

Looks good.

For the pedants out there, this number is a no-way strict upper bound on something and it makes no sense to worry about the low order bits.


---

Comment by rlm created at 2010-06-29 16:16:59

Resolution: fixed
