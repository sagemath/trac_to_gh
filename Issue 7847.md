# Issue 7847: Emptying the trash in Firefox 3.5.6 displays a "Forbidden  No referer found. Forbidden." page

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-05 03:41:39

Assignee: was

CC:  was timdumol jhpalmieri jason

This is also a problem in IE8 on Windows XP.

This is a follow-up to #5100.


---

Attachment

"No referer" workaround.  sagenb repo.


---

Comment by mpatel created at 2010-01-05 04:02:06

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-05 04:02:06

The patch works for me and should not affect browsers that do include the referer.  I don't know if we can use just the workaround for all browsers.


---

Comment by timdumol created at 2010-01-17 19:10:02

Makes Worksheet_emptytrash accept only POST requests, and adds the requisite form.


---

Attachment

Good job fixing the problem, but unfortunately your patch means anyone can cause you to empty your trash.

The reason for the HTTP-Referer check was actually security. Without it, anyone could have sent you a link to http://localhost:8000/emptytrash (or http://sagenb.org/emptytrash) and empty one's trash. This was clearly the wrong approach though.

This new patch accepts only POST requests, which should be much more secure.


---

Comment by mpatel created at 2010-01-18 05:02:49

Great catch.  That's definitely the way to go.  I've checked that this works in multiple browsers on Linux and Windows XP.

To the release manager: Apply only [attachment:trac_7847-empty-trash-no-referer.patch]


---

Comment by mpatel created at 2010-01-18 05:02:49

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-19 03:31:58

Resolution: fixed
