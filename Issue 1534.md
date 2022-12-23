# Issue 1534: Purge java3d from extcode

Issue created by migration from https://trac.sagemath.org/ticket/1534

Original creator: robertwb

Original creation time: 2007-12-16 07:24:54

Assignee: was

Once #1533 is done, we need to remove the files from extcode. This should be done is such a way that the history of the (several MB) jar files is purged, I'm still looking for the best way to do this. 


---

Comment by robertwb created at 2007-12-16 07:24:58

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-12-16 07:24:58

Changing status from new to assigned.


---

Comment by cwitty created at 2007-12-16 19:24:24

See http://www.selenic.com/pipermail/mercurial/2007-May/013256.html for some brief discussion of the question.  The answer seems to be to use "hg clone -r" and "hg transplant".

Be sure to test "sage -upgrade" when you make this change.


---

Comment by robertwb created at 2007-12-17 18:58:45

Looks good. We need to make sure that if developers work on extcode they don't merge this stuff back in though.


---

Comment by was created at 2008-01-19 18:38:34

I had lots of problems trying to use hg transplant, which just doesn't work for me.

cwitty remarks: Looks like what we really want is http://www.selenic.com/pipermail/mercurial/2006-June/008878.html ; too bad it seems like nobody's touched it since mid-2006.


---

Comment by jason created at 2010-03-17 05:18:20

Changing type from defect to task.


---

Comment by aapitzsch created at 2014-08-19 16:45:53

There is no java3d in SAGE_EXTCODE.


---

Comment by aapitzsch created at 2014-08-19 16:45:53

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-08-26 19:24:57

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-29 18:33:34

Resolution: fixed
