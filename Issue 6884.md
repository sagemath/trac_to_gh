# Issue 6884: notebook doctest failures in Sage 4.1.2.alpha0 on mod.math

Issue created by migration from https://trac.sagemath.org/ticket/6884

Original creator: mvngu

Original creation time: 2009-09-04 07:45:12

Assignee: boothby

CC:  timdumol

The following doctests failed in Sage 4.1.2.alpha0 on mod.math:

```
sage -t -long devel/sage-main/sage/server/notebook/notebook.py # 12 doctests failed
sage -t -long devel/sage-main/sage/server/notebook/worksheet.py # 5 doctests failed
```

This was reported at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5370af4b74c5ca3c) thread. A full log is attached with this ticket.


---

Attachment

doctest log on mod.math


---

Comment by mpatel created at 2009-09-05 14:09:47

Update MANIFEST.in to include all Jinja templates.


---

Attachment

I apologize for missing this.


---

Attachment

Corrected ticket number in patch filename. Apply only this patch.


---

Comment by mpatel created at 2009-09-07 11:35:33

If the "manifest" patch at #6568 fixes the doctest failures, please close this ticket.


---

Comment by mvngu created at 2009-09-07 16:19:48

Resolution: fixed


---

Comment by mvngu created at 2009-09-07 16:19:48

The doctest failures are fixed by the patch `trac_6568-manifest.patch` at #6568.
