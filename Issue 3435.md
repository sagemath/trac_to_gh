# Issue 3435: physically delete GSL BLAS so that nothing can link against it

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-06-16 00:34:34

Assignee: mabshoff

CC:  slelievre




---

Comment by jason created at 2010-03-17 05:56:56

Changing type from defect to task.


---

Comment by aapitzsch created at 2014-07-25 23:23:14

Why nothing should link against GSL BLAS?


---

Comment by slelievre created at 2018-11-04 23:54:54

This was solved by #15685 where BLAS and LAPACK were replaced by ATLAS.

Then OpenBLAS was introduced as an optional package in #20129 and made standard in in #20096.


---

Comment by slelievre created at 2018-11-04 23:54:54

Changing keywords from "" to "blas".


---

Comment by slelievre created at 2018-11-04 23:54:54

Changing status from new to needs_review.


---

Comment by slelievre created at 2018-11-04 23:56:19

Note also that BLAS linking was removed from Cython modules in #18777.


---

Comment by chapoton created at 2018-11-30 20:46:56

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2018-11-30 20:46:56

very old stuff indeed, obsolete


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid
