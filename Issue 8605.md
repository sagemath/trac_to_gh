# Issue 8605: upgrade SageTeX spkg to 2.2.5

Issue created by migration from https://trac.sagemath.org/ticket/8605

Original creator: ddrake

Original creation time: 2010-03-25 12:43:19

Assignee: tbd

I've made a couple improvements to SageTeX in the last few months, and it's time for an upgrade. The new version automatically falls back to making PNGs if making EPS or PDF files fails, and includes Nicolas Thiéry's sageexample environment. Please review and test!

spkg available at http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.2.5.spkg


---

Comment by ddrake created at 2010-03-25 12:43:41

Changing status from new to needs_review.


---

Comment by jason created at 2010-03-30 03:44:13

Things seem to work as advertised.  The new example.tex contains documentation for the new features and the pdf output seems to be exactly what is wanted.

Looks good to me.


---

Comment by jason created at 2010-03-30 03:44:13

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-03-30 03:51:18

merging this should close #8489.


---

Comment by jhpalmieri created at 2010-04-23 17:12:56

Merged into 4.4.alpha2.


---

Comment by jhpalmieri created at 2010-04-23 17:12:56

Resolution: fixed
