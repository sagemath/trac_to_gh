# Issue 8144: SageTeX is not actually installed under SAGE_LOCAL

Issue created by migration from https://trac.sagemath.org/ticket/8144

Original creator: mvngu

Original creation time: 2010-02-01 18:14:12

Assignee: tbd

CC:  ddrake

Keywords: sagetex

Ticket #7617 adds SageTeX as a standard spkg. However, despite modifying the spkg dependency rules in `SAGE_ROOT/spkg/install` and `SAGE_ROOT/spkg/standard/deps` to account for this new package, SageTeX isn't actually installed at all in Sage 4.3.2.alpha1. This was reported on [sage-devel](http://groups.google.com/group/sage-devel/msg/fa6ed48cba5037e0).


---

Comment by jhpalmieri created at 2010-02-01 22:43:43

Changing priority from major to blocker.


---

Comment by jhpalmieri created at 2010-02-01 22:43:43

I think you just need to add a line for sagetex to the "all" section of deps.  See the attached patch and new version of deps.


---

Comment by jhpalmieri created at 2010-02-01 22:43:43

Changing status from new to needs_review.


---

Attachment


---

Comment by ddrake created at 2010-02-01 23:41:34

That does the trick. Positive review.


---

Comment by ddrake created at 2010-02-01 23:41:34

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-02 20:55:29

Resolution: fixed


---

Comment by mvngu created at 2010-02-02 20:55:29

Copied [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8144/deps) to `SAGE_ROOT/spkg/standard` and replaced the previous version of `deps` with this one.
