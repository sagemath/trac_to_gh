# Issue 7104: [with patch, needs review] Add config.py back to the reference manual.

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-10-04 02:13:53

Assignee: tba

Ticket #6556 adds a much-needed, module-level docstring to `sage/server/notebook/config.py`.  It should be in the Sage reference manual.

See [sage-devel](http://groups.google.com/group/sage-devel/msg/b07018c5c407edc4).


---

Comment by mpatel created at 2009-10-04 02:19:46

Add the notebook key-bindings module to the reference manual.  Apply to sage repository.


---

Attachment


---

Comment by mpatel created at 2009-10-04 02:21:00

Changing priority from trivial to major.


---

Comment by mpatel created at 2009-10-04 07:01:23

Oops.  I think we need to account for all modules affected by the notebook separation (cf. #6983).


---

Comment by awebb created at 2009-10-07 19:17:10

Changing status from needs_review to positive_review.


---

Comment by awebb created at 2009-10-07 19:17:10

Works with sage -docbuild reference html. ~! Adam


---

Comment by was created at 2009-10-19 06:25:59

I'm confused.  This is just adding to the reference manual pages about the old notebook code, which isn't even used anymore.  I don't understand what the point is.


---

Comment by was created at 2009-10-19 06:26:23

(Of course, it can't really hurt for now, I guess, except to mislead people...)


---

Comment by was created at 2009-10-19 06:28:16

Changing component from documentation to notebook.


---

Comment by was created at 2009-10-19 06:28:16

I didn't realize this is old.  It'll need to be rebased against http://nb.sagemath.org/.


---

Comment by was created at 2009-11-11 19:46:48

Changing status from positive_review to needs_work.


---

Comment by was created at 2009-11-11 19:46:48

changing to needs work, since it needs to be rebased/redone.


---

Comment by mpatel created at 2009-11-12 01:28:48

Replying to [comment:7 was]:
> changing to needs work, since it needs to be rebased/redone. 
Please see #7367.


---

Comment by was created at 2009-11-12 04:55:26

Resolution: fixed


---

Comment by was created at 2009-11-12 04:55:26

This is fixed by #7367, so I'm closing this.
