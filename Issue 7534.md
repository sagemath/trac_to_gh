# Issue 7534: Add a deprecation message at the top of most sage.server.* files

Issue created by migration from https://trac.sagemath.org/ticket/7534

Original creator: mpatel

Original creation time: 2009-11-26 07:20:52

Assignee: boothby

CC:  timdumol was

To avoid confusion, we should add a message to the top of each *old* Sage notebook .py file stating that one should work on [SageNB](http://nb.sagemath.org/) instead.

This should be a patch to the core Sage library.



---

Comment by mpatel created at 2009-11-26 07:57:48

How about

```
This file is part of the OLD Sage notebook and is NOT actively developed,
maintained, or supported.  As of Sage v4.1.2, all notebook development has
moved to the separate Sage Notebook project:

http://nb.sagemath.org/

The new notebook is installed in Sage as a spkg (e.g., sagenb-0.3.spkg).

Please visit the project's home page for more information, including directions on
obtaining the latest source code.  For notebook-related development and support,
please consult the sage-notebook discussion group:

http://groups.google.com/group/sage-notebook
```

?


---

Comment by mpatel created at 2009-11-26 22:00:17

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/be3318a5770bf8f4).


---

Comment by timdumol created at 2009-11-30 06:26:05

Adds the recommended deprecation message (with typo correction)


---

Comment by timdumol created at 2009-11-30 06:26:20

Changing status from new to needs_review.


---

Attachment

This should do the job.


---

Comment by mhansen created at 2009-12-02 19:20:20

This causes some failures in tests in sage/server/


---

Comment by mhansen created at 2009-12-02 19:20:20

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2009-12-02 19:23:21


```
        sage -t  devel/sage-main/sage/server/notebook/notebook_object.py # 4 doctests failed
```



---

Comment by was created at 2009-12-10 01:29:14

Replying to [comment:5 mhansen]:
> {{{        sage -t  devel/sage-main/sage/server/notebook/notebook_object.py # 4 doctests failed
> }}}

Since the code isn't being run and is officially "deprecated", one option is to put a nodoctest.py file in the directory (or #nodoctest at the top of the file) so that the code isn't tested.


---

Comment by mpatel created at 2009-12-10 12:16:05

Adds `nodoctest.py` files.  Replacement patch.


---

Attachment

V2 suppresses doctesting for the "deprecated" files.


---

Comment by mpatel created at 2009-12-10 12:17:29

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-12-10 18:21:52

Looks good to me now.


---

Comment by was created at 2009-12-10 18:21:52

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-14 16:31:20

Resolution: fixed
