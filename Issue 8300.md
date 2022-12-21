# Issue 8300: native algdep with proof option

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-02-19 01:41:38

Assignee: was

CC:  was

Using the properties of LLL and a height bound, we can prove (given sufficient precision) that an integer relation of bounded height either doesn't exist or is unique. This is needed, e.g.,  for provable computations of Heegner points though could be useful elsewhere as well. It is also faster.  


---

Comment by robertwb created at 2010-02-19 01:42:48

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-04-05 16:42:53

Looks good, applies to 4.3.5 (with a small amount of fuzz).  Tests in sage/rings all pass.  Docs build and look good.  I did some random testing of my own and the results seem fine.

Small question:  why does algdep? not display the docstring?  algdep?? works fine though.


---

Comment by cremona created at 2010-04-05 16:42:53

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 20:07:23

Merged in 4.4.alpha0:

 - 8300-algdep-proof.patch


---

Comment by jhpalmieri created at 2010-04-15 20:07:23

Resolution: fixed
