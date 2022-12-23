# Issue 7881: Make polynomials respect the _gcd framework so that they can use coercion in gcds

Issue created by migration from https://trac.sagemath.org/ticket/7881

Original creator: robertwb

Original creation time: 2010-01-09 19:56:16

Assignee: AlexGhitza

CC:  roed

In support of #7585


---

Attachment

I'm all for using the coercion model more, but I don't like the fact that this hides the important docstrings about ZZ[x] and RR[x] in the underscore methods.


---

Comment by robertwb created at 2010-01-09 19:58:56

Changing status from new to needs_work.


---

Comment by robertwb created at 2010-05-25 06:48:21

Changing status from needs_work to needs_info.


---

Comment by robertwb created at 2010-05-25 06:48:21

I think this is taken care of with #383.


---

Comment by davidloeffler created at 2010-10-03 15:46:30

Changing status from needs_info to needs_review.


---

Comment by davidloeffler created at 2010-10-03 15:46:30

I propose closing this as "duplicate".


---

Comment by robertwb created at 2010-10-04 16:19:31

I concur.


---

Comment by davidloeffler created at 2010-10-04 16:41:53

Release manager: please close this as duplicate (and don't merge the patch).


---

Comment by davidloeffler created at 2010-10-04 16:41:53

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-04 22:01:19

Resolution: duplicate
