# Issue 7502: lazy import module

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-11-20 09:20:53

Assignee: was

This is something I came up with when trying to reduce sage start up time. 


```
2.033 sage.all (None)
0.407 sage.server.all (sage.all)
0.404 notebook.all (sage.server.all)
0.365 sage.server.notebook.notebook (notebook.all)
...
```


Now notebook() needs to be in the global namespace, but usually the entire notebook server does not need to be loaded. I'm sure there's other trimming we could do here as well. 

It's unclear what level to put this in, but I would think sage.server.notebook.all would be a good place (e.g. we could lazily import interact.*, sage_email.*, and lazily import notebook and inotebook). That could cut down startup time by 25%. 


---

Attachment


---

Comment by mpatel created at 2010-01-28 05:58:19

Somewhat related: #8102 + #8107 reduce the startup time by cutting unnecessary imports.


---

Comment by mpatel created at 2010-01-28 05:58:34

By the way, is this up for review?


---

Comment by robertwb created at 2010-01-28 19:15:16

Yes.


---

Comment by robertwb created at 2010-01-28 19:15:16

Changing status from new to needs_review.


---

Attachment

Also map tab completion.  Add to reference manual. Rebased vs. 4.3.2.alpha0. Replaces previous.


---

Comment by mpatel created at 2010-01-30 03:39:48

My review is positive, but someone should review the changes in v2.


---

Comment by robertwb created at 2010-01-30 05:28:19

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-01-30 05:28:19

Thanks. Yes, your additions look good as well.


---

Comment by mvngu created at 2010-01-30 23:54:04

Merged [7502-lazy-import.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7502/7502-lazy-import.2.patch).


---

Comment by mvngu created at 2010-01-30 23:54:04

Resolution: fixed
