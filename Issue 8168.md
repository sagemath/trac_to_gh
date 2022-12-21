# Issue 8168: Keyword option to keep reset() from detaching all attached files

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-03 09:58:21

Assignee: tbd

With this option, one can put `reset(attached=False)` at the top of an attached file.  This resets the global variables and interfaces but not the list of attached files.  Otherwise, the file detaches itself.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/7a43d2944dc35674#).


---

Comment by mpatel created at 2010-02-03 10:00:47

Add keyword option `attached=True` to `reset`.  sage repo.


---

Comment by mpatel created at 2010-02-03 10:05:54

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-02-03 10:28:59

V2 makes the `attached=False` the default.


---

Comment by mpatel created at 2010-02-03 10:29:53

Same as previous, except with default `attached=False`.  Apply just one patch.


---

Attachment

Note: With V2, attaching a file that contains `reset(attached=True)` does not immediately detach the file.  This happens because `sage.misc.preparser.load` `exec`s the file _before_ updating the attached files dictionary.


---

Comment by mpatel created at 2010-02-16 21:56:01

V2 rebased for #378.  Apply only this patch.


---

Attachment

V3 is V2 rebased for #378.


---

Comment by mpatel created at 2010-06-23 01:29:21

Note to potential reviewers:  V2 of the patch should apply cleanly to 4.4.4.alpha1.  V3 is based on #378, but that ticket needs work.


---

Attachment


---

Comment by mhansen created at 2011-12-18 10:20:09

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2011-12-18 10:20:09

I rebased this and think it looks okay.  Apply only  trac_8168-attached_reset.4.patch.


---

Comment by jdemeyer created at 2011-12-22 13:06:15

Resolution: fixed
