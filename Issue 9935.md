# Issue 9935: add sage.symbolic.function_factory to the reference manual

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-09-17 20:22:12

Assignee: mvngu

I couldn't find sage.symbolic.function_factory.function in the reference manual.  It looks like it is already formatted correctly.  It just needs to be added into an appropriate place somewhere in sage/devel/sage/doc/en/reference/*.rst (maybe calculus.rst?)


---

Attachment


---

Comment by mvngu created at 2010-09-19 11:34:07

The attachment [attachment:trac_9936-symbolic-functions.patch] adds the module `sage.symbolic.function_factory` to the reference manual, under the calculus chapter.


---

Comment by mvngu created at 2010-09-19 11:34:07

Changing status from new to needs_review.


---

Comment by niles created at 2010-09-21 16:58:37

Changing status from needs_review to positive_review.


---

Comment by niles created at 2010-09-21 16:58:37

Indeed, `calculus.rst` seems like the right place to put this.  The patch applies cleanly, and the documentation compiles without warnings; the html output looks good too, so positive review


---

Comment by mpatel created at 2010-09-28 09:10:09

Resolution: fixed
