# Issue 3265: some doctests leave files in $SAGE_ROOT/devel/sage

Issue created by migration from https://trac.sagemath.org/ticket/3265

Original creator: mabshoff

Original creation time: 2008-05-21 13:35:15

Assignee: failure

Some doctests [likely notebook related] leave files in $SAGE_ROOT/devel/sage:

```
hg status
? sage/server/docs-0.html
? sage/server/docs-1.html
? sage/server/docs-2.html
? sage/server/notebook/a.txt
```

This is problematic for two reasons:
 * temp files should be written to SAGE_TESTDIR since that is guaranteed to be writable, i.e. when you run doctests on an install that is not owned by the current user
 * it leaves crap in the default tree ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-21 14:16:44

Mmmh, with the proto patch from #3267 the "sage/server/docs-X.html" files are no longer created.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-13 18:31:02

Resolution: duplicate


---

Comment by mabshoff created at 2008-06-13 18:31:02

This is a dupe of #3412.

Cheers,

Michael
