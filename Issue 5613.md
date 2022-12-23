# Issue 5613: [with patch; needs review] fix url to sage hg server; hg_sage.bundle(...)

Issue created by migration from https://trac.sagemath.org/ticket/5613

Original creator: was

Original creation time: 2009-03-26 02:32:40

Assignee: schilly

The command

```

  sage: hg_sage.send('foo.hg')
```

was broken because http://www.sagemath.org/hg/sage-main on the new server is now at http://hg.sagemath.org/sage-main/.  The attached patch fixes this.


---

Attachment


---

Comment by mabshoff created at 2009-03-26 20:31:24

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-26 20:33:04

Resolution: fixed


---

Comment by mabshoff created at 2009-03-26 20:33:04

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
