# Issue 8221: blank space at bottom of worksheet missing

Issue created by migration from https://trac.sagemath.org/ticket/8221

Original creator: jason

Original creation time: 2010-02-09 15:45:41

Assignee: was

There used to be blank space (via CSS) at the bottom of the notebook that would prevent interacts from jumping when updated.  See  #4963 for the CSS code that was used and the reason for it.  In 4.3.2, it seems that the blank space was removed.



---

Attachment

Big blank space at bottom of live worksheets.  sagenb repo.


---

Comment by mpatel created at 2010-02-14 03:36:01

Changing status from new to needs_review.


---

Comment by awebb created at 2010-03-07 13:42:34

Works as advertised. I tried before/after with a worksheet with an interact as the last block. In this case the cell about is fairly large. The page would jump significantly every time the interact updated. Adding the space stopped the jumping.

Is there a suitable place to document this? Other than in trac? I can see this as something that can get changed as people forget the reason for it. Perhaps just a suitable comment in the source is all that is needed.  

Adam


---

Comment by awebb created at 2010-03-07 13:54:23

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-03-09 05:10:02

Resolution: fixed


---

Comment by mpatel created at 2010-03-09 05:10:02

Possibly in `sagenb.notebook.interact`, I think.  The space is useful for other reasons, of course, but we should try to fix the flickering interact problem.  I had what _may_ be a promising solution at #7908.  I'll try to rebase it in the near future.
