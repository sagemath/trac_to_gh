# Issue 8092: init.sage not attached in worksheets

Issue created by migration from https://trac.sagemath.org/ticket/8092

Original creator: mpatel

Original creation time: 2010-01-27 10:09:52

Assignee: was

CC:  was

From the main notebook help page:

   The file `$HOME/.sage/init.sage` is attached on startup if it exists.

But the file is not `attach`ed --- try evaluating `attached_files()`.  This is a follow-up to #7514.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/856f02edb25e8781#), [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/320d494175d46012).


---

Comment by mpatel created at 2010-01-27 13:05:31

Attach `DOT_SAGE/init.sage`.  sagenb repo.


---

Comment by mpatel created at 2010-01-27 13:09:54

Changing status from new to needs_review.


---

Attachment

The attached patch seems to work for me.  `DOT_SAGE/init.sage` is equivalent to `os.environ['SAGE_STARTUP_FILE']` (see `SAGE_LOCAL/bin/ipy_profile_sage.py`).


---

Comment by was created at 2010-01-27 18:04:07

Oops!

```
except KeyError, IOError:
```

should be

```
except (KeyError, IOError):
```


This is one of those very annoying tricky mistakes people make with Python exceptions...


---

Comment by was created at 2010-01-27 18:04:07

Changing status from needs_review to needs_work.


---

Attachment

Fixes Oops!  Replaces previous.


---

Comment by mpatel created at 2010-01-28 01:48:20

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-03-19 08:29:20

LGTM.


---

Comment by timdumol created at 2010-03-19 08:29:20

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-05-04 04:44:29

Resolution: fixed
