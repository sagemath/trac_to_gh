# Issue 7498: Do *not* import matplotlib at sage startup.

Issue created by migration from https://trac.sagemath.org/ticket/7498

Original creator: robertwb

Original creation time: 2009-11-20 06:34:07

Assignee: was

CC:  was

Despite the warning


```
## IMPORTANT: Do *not* import matplotlib at module scope.  It takes a
## surprisingly long time to initialize itself.  It's better if it is
## imported in functions, so it only gets started if it is actually
## going to be used.
```


it's gotten back in there again. There should be a test. 


---

Attachment


---

Comment by robertwb created at 2009-11-20 06:41:03

Changing status from new to needs_review.


---

Comment by was created at 2009-11-20 12:37:56

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-11-20 12:37:56

This patch is weird.  It has a 3-liner that does what this ticket is about, but then it also has a bunch of other complicated unrelated code.  Hmm?


---

Comment by robertwb created at 2009-11-20 17:33:02

The diff is odd, try looking at before and after. There's a class that extends a class from matplotlib, which I moved to inside a function body so I didn't have to import it on startup.


---

Comment by robertwb created at 2009-11-20 18:59:24

Changing status from needs_work to needs_review.


---

Attachment

Robert's changes look good, but it looks like we also need to make some changes in plot_field3d.py.

I've attached a patch for that.


---

Comment by hivert created at 2009-12-01 09:22:28

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-12-01 09:22:28

Patch trac_7498-review.patch is ok => Positive review.


---

Comment by mhansen created at 2009-12-01 09:24:54

Resolution: fixed
