# Issue 8324: Reconcile sage.misc.sageinspect and sagenb.misc.sageinspect

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-22 03:50:36

Assignee: was

CC:  jhpalmieri

The module `sage.misc.sageinspect` is missing several recent changes to `sagenb.misc.sageinspect`.

Note: SageNB has its own `sageinspect` so that it can stand alone.

Related: #2064.


---

Comment by mpatel created at 2010-02-22 03:54:21

sagenb repo.


---

Comment by mpatel created at 2010-02-22 04:06:09

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-02-22 04:08:39

I guess outside (non-Sage) projects delete some doctests?


---

Comment by jhpalmieri created at 2010-02-24 22:01:36

I suppose this "depends" on #8244: it adds a bit to sagenb.misc.sageinspect.py from the patch there.  Overall, it looks fine: just the obvious changes.  Is there a good way to run doctests on all of sagenb?  The new sageinspect passes doctests with Sage installed, and I think it should without the rest of the Sage library, but I haven't checked it.

> I guess outside (non-Sage) projects delete some doctests?

I'm not sure what this refers to.


---

Comment by mpatel created at 2010-02-25 05:05:08

You can run `make test` or `make ptest` in the root of the sagenb repository or run `sage -t -sagenb`, say, but these assume Sage is installed.

I'm not aware of an easy way to doctest the standalone notebook.  We only recently got the tests to run with Sage (cf. #7650).

Several notebook doctests and some `import`s not wrapped in `try-except` clauses refer to Sage modules.  It seems that most of the Sage-dependent doctests in `sagenb.misc.sageinspect` test Cython introspection, but right now, the notebook doesn't include Cython modules.  I don't know if outside projects depend on these Cython-related features.


---

Comment by jhpalmieri created at 2010-02-25 05:17:18

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 03:01:06

Is this ticket meant to have the milestone "Sage 4.3.4"? In any case, it could only be closed once the relevant patch is merged in the SageNB repository, which is managed by the upstream SageNB team.


---

Comment by jhpalmieri created at 2010-03-03 22:00:58

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-03-03 22:03:07

Here's a new patch; apply on top of the old one.  This changes one line to fix the doctest failure in 4.3.4.alpha0: `sage_getsourcelines(matrix,True)[1])` used to return 33, and now it returns 34.


---

Comment by jhpalmieri created at 2010-03-03 22:03:07

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-03-03 22:07:46

(This new patch is supposed to fix one of the bugs listed at #8430.  Only the "new" patch needs reviewing.)


---

Attachment

apply on top of other patch


---

Comment by mpatel created at 2010-03-04 07:16:35

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-03-04 22:51:07

Resolution: fixed
