# Issue 5940: graph theory -- bug in is_circular_planar

Issue created by migration from https://trac.sagemath.org/ticket/5940

Original creator: was

Original creation time: 2009-04-29 17:03:47

Assignee: rlm


```
sage: g = graphs.KrackhardtKiteGraph()
sage: g.is_circular_planar()
Traceback...
IndexError: list index out of range
```



---

Attachment


---

Comment by rlm created at 2009-05-18 20:35:02

The offending example needs to be added as a doctest. Otherwise, positive review.


---

Comment by rlm created at 2009-05-18 20:45:49

Apply instead.


---

Attachment


---

Comment by ekirkman created at 2009-05-18 20:49:36

Thanks for posting the patch with the doctest.  Looks good to me.


---

Comment by mabshoff created at 2009-05-19 20:13:42

Merged trac_5940-ref_fix.patch only in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 20:13:42

Resolution: fixed
