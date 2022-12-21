# Issue 7117: [with patch, needs review] latex fix for RIF

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-10-04 20:53:10

Assignee: cwitty

From IRC:

```
By the way, if I evaluate "jsmath(RIF)" in the notebook, jsMath complains: "Unknown control sequence '\I'". 
Is there a missing macro definition?
```

It looks to me as though the `_latex_` method for RIF has been defined in terms of '\\I' for a long time, and it has not worked since at least Sage 3.4.  The attached patch changes it from "\\I \\R" to "\\Bold{I} \\Bold{R}".


---

Comment by mhansen created at 2009-10-05 03:48:25

Looks good to me.


---

Attachment


---

Comment by mhansen created at 2009-10-15 08:36:07

Resolution: fixed


---

Comment by mhansen created at 2009-10-15 08:36:07

I had to do a minor rebasing and attached the new patch.
