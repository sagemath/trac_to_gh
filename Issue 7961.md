# Issue 7961: Make recognition of runpath/develpath in editmodule more robust

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2010-01-17 02:41:47

Assignee: nbruin

Currently, the code that recognizes a source file is part of the sage library and hence is run from a different location than where the edit copy lives, is broken due to the python2.5 -> python2.6 upgrade. Attached fixes this problem and makes matching more robust so that it won't break the next time. To illustrate the problem, currently we have

```
sage: sage.misc.edit_module.file_and_line(edit)
('/usr/local/sage/4.3/local/lib/python2.6/site-packages/sage/misc/edit_module.py', 194)
```

which obviously is NOT the file to edit. It should be `.../sage/devel/...` instead. Attached patch fixes this.



---

Attachment

making misc.edit_module pathname mangling more robust


---

Comment by nbruin created at 2010-01-17 02:46:43

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-17 10:01:23

LGTM.


---

Comment by timdumol created at 2010-01-17 10:01:23

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 00:55:34

Resolution: fixed
