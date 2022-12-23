# Issue 8100: running the notebook should not change the working directory

Issue created by migration from https://trac.sagemath.org/ticket/8100

Original creator: jhpalmieri

Original creation time: 2010-01-27 23:45:50

Assignee: was

In sage-4.3.2.alpha0 (and all earlier versions I can remember), running the notebook changes my working directory:

```
sage: pwd
'/Users/palmieri'
sage: notebook()
The notebook files are stored in: sage_notebook.sagenb
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
...
^C
...
sage: pwd
'/Users/palmieri/.sage'
```




---

Comment by mpatel created at 2010-02-05 13:12:07

Restore working directory when `notebook` returns.  sagenb repo.


---

Comment by mpatel created at 2010-02-05 13:17:25

Changing status from new to needs_review.


---

Attachment

Patch attached.


---

Comment by jhpalmieri created at 2010-02-05 15:55:23

Looks good to me; restores my working directory to whatever it was before running `notebook()`.


---

Comment by jhpalmieri created at 2010-02-05 15:55:23

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 18:33:00

Resolution: fixed
