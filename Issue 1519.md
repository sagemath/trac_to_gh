# Issue 1519: hg problem -- This should work but doesn't: sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/1514/trac-1514.patch?format=raw')

Issue created by migration from https://trac.sagemath.org/ticket/1519

Original creator: was

Original creation time: 2007-12-15 05:52:18

Assignee: was

Doing

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/1514/trac-1514.patch?format=raw')
```


should work, but doesn't, because of the ?stuff at the end.  Fix this.

How to test the patch: Try applying a patch or bundle by pasting in the URL to the raw format as in the example above. 


---

Attachment


---

Comment by was created at 2007-12-15 06:20:09

Note -- there is no easy way to doctest this, since it requires existence of a specific file on the internet with a funny ? in its filename..., and to apply that patch to a repository...


---

Comment by mabshoff created at 2007-12-15 11:00:00

looks good to me and is quite useful.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-15 11:06:36

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 11:06:36

Resolution: fixed
