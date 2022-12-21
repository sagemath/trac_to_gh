# Issue 6475: Notebook error page after deleting data file

Issue created by migration from Trac.

Original creator: khorton

Original creation time: 2009-07-07 18:22:15

Assignee: wstein

CC:  was acleone mpatel

Keywords: notebook delete file error

If I delete a data file using the notebook (Data... pop up menu -> file name -> delete file name link), the file is deleted, but the browser then goes to a blank page titled "Error | Sage Notebook". The browser is Safari 4 on OS X 10.5, in case that makes a difference.

William Stein reported on Sage-Support:

I've seen this.  This definitely didn't used to happen.  Somebody introduced this bug a few months ago.  Please report it to trac.  I'll fix it in September/October when I work on the notebook, if nobody beats me to it.




---

Comment by mpatel created at 2009-12-14 17:35:10

Is this still a problem, in 4.3.rc0?


---

Comment by timdumol created at 2010-01-19 10:54:37

Changes the title of the successful delete page


---

Attachment


---

Comment by timdumol created at 2010-01-19 10:54:49

Changing status from new to needs_review.


---

Comment by acleone created at 2010-01-19 12:56:24

Changing status from needs_review to positive_review.


---

Comment by acleone created at 2010-01-19 12:56:24

LGTM.


---

Comment by mpatel created at 2010-01-25 01:02:39

Resolution: fixed
