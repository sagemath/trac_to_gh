# Issue 2097: aspect_ratio option to show() for function plots does not work correctly

Issue created by migration from https://trac.sagemath.org/ticket/2097

Original creator: moretti

Original creation time: 2008-02-08 02:04:14

Assignee: moretti


```
plot(x^2, (x, -10, 10)).show(aspect_ratio=1)
```


outputs a figure which is wide and short. It should be skinny and tall.


---

Comment by moretti created at 2008-02-08 02:09:46

Fixed in the attached patch.


---

Attachment


---

Comment by cwitty created at 2008-02-09 21:23:07

This patch makes a doctest fail; my attached patch fixes the doctest.

Other than that, it looks good.  (The code looks good, it fixes the problem, and (after my patch) doctests still pass in sage/plots/.)

Apply both patches.


---

Comment by mabshoff created at 2008-02-12 18:29:06

Resolution: fixed


---

Attachment

Merged both patches in Sage 2.10.2.alpha0
