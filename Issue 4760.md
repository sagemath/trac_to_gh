# Issue 4760: [with patch, needs review] dsage_interface doctests broken

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-12-11 14:51:54

Assignee: gfurnish

The doctests in dsage_interface are disabled and do not work properly when enabled.  This patch fixes these issues.  


---

Attachment


---

Comment by mhansen created at 2008-12-11 15:03:43

All tests pass for me after #4745 and this patch.  I think the doctests should still be rewritten to use start_all since that should be the preferred way to do things.


---

Comment by gfurnish created at 2008-12-11 15:04:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-11 15:47:09

The following comment in the file should definitely be deleted:

```
3	3	Doctesting of this file is disabled because it fails in so many ways it is even funny. 
4	4	See http://trac.sagemath.org/sage_trac/ticket/3593 for two of the four ways I've
<SNIP> 
```

I will do so via a referee patch.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-12-11 15:55:42

Merged both patches in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-11 15:55:42

Resolution: fixed
