# Issue 3430: 3.0.3.rc0: doctest failure in server/notebook/interact.py

Issue created by migration from https://trac.sagemath.org/ticket/3430

Original creator: mabshoff

Original creation time: 2008-06-15 21:34:06

Assignee: failure


```
sage -t -long devel/sage/sage/server/notebook/interact.py   
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.3.rc0/tmp/interact.py", line 526:
    sage: sage.server.notebook.interact.InputBox('theta', 1).render()
Expected:
    '<input type=\'text\' value=\'1\' width=200px onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"theta\\", ..., sage.server.notebook.interact.standard_b64decode(\\""+encode64(this.value)+"\\"), globals())")\'></input>'
Got:
    '<input type=\'text\' value=\'1\' size=80 onchange=\'interact(0, "sage.server.notebook.interact.update(0, \\"theta\\", 16, sage.server.notebook.interact.standard_b64decode(\\""+encode64(this.value)+"\\"), globals())")\'></input>'
**********************************************************************
```



---

Comment by mabshoff created at 2008-06-15 21:34:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-15 21:34:22

Changing assignee from failure to mabshoff.


---

Attachment


---

Comment by mabshoff created at 2008-06-16 04:51:56

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-16 04:52:23

Resolution: fixed


---

Comment by mabshoff created at 2008-06-16 04:52:23

Merged in Sage 3.0.3.rc0
