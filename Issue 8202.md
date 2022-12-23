# Issue 8202: Allow raw HTML in jsMath's \hbox{}

Issue created by migration from https://trac.sagemath.org/ticket/8202

Original creator: mpatel

Original creation time: 2010-02-06 19:58:18

Assignee: was

CC:  rbeezer

We can do this by setting `safeHBoxes` to 0 in `sagenb/data/sage/js/jsmath.js`.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/b56eb3ec554642ce).


---

Comment by mpatel created at 2010-02-06 20:00:36

Disable jsMath's `safeHBoxes` option.  sagenb repo.


---

Attachment

I've attached a patch that only disables jsMath's safe `\hbox{}` setting.  Feel free to ignore it!


---

Comment by mpatel created at 2010-02-06 20:03:34

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-06 20:05:10

The patch should apply cleanly to SageNB 0.7.4 (cf. #8051), which will be part of Sage 4.3.2.  But it may also work with SageNB 0.6.


---

Comment by rbeezer created at 2010-02-07 04:40:10

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-02-07 04:40:10

Replying to [comment:2 mpatel]:
> The patch should apply cleanly to SageNB 0.7.4 (cf. #8051), which will be part of Sage 4.3.2.  But it may also work with SageNB 0.6.

I've tested this on 4.3.1 with SageNB 0.7.4 (cf. #8051).  It behaves as expected with patch applied (and behavior reverts when I pop it off).  This is a big help with rendering my textbook-conversion experiments.  Thanks for the help.

Positive review.

Rob


---

Comment by mpatel created at 2010-02-10 18:31:37

Resolution: fixed
