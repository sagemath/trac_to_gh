# Issue 5103: setup.py: dependency checking does not ignore comments

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-26 16:44:25

Assignee: mabshoff

**

Hello,

reading the code, I see another problem if ones has the following line in its .pyx:


```
cimport mod#mycomment
```


I such a case, we'll look for a dependency mod#mycomment.pxd instead of mod.pxd.

Otherwise, the patch solves the aforementioned problems.

Cheers



---

Comment by craigcitro created at 2009-01-26 16:49:21

This is a dupe of #5104.


---

Comment by craigcitro created at 2009-01-26 16:49:21

Resolution: duplicate
