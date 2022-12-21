# Issue 5006: the hg script installed by install_script() does not pass parameters correctly

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-18 05:10:24

Assignee: cwitty

The script currently is:
{{{#!/bin/sh
sage -hg $*
```

But this is broken when running something like

```
hg ci -u "User Foo"
```


Cheers,

Michael


---

Comment by jdemeyer created at 2010-10-10 21:27:56

This seems to be fixed.


---

Comment by jdemeyer created at 2010-10-10 21:27:56

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-12-03 06:56:58

Resolution: worksforme
