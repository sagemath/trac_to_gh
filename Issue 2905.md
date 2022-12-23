# Issue 2905: Various speedups

Issue created by migration from https://trac.sagemath.org/ticket/2905

Original creator: gfurnish

Original creation time: 2008-04-13 06:02:46

Assignee: gfurnish

This patch moves some things to cpdef and fixes various slowdowns.


---

Attachment


---

Comment by gfurnish created at 2008-04-13 06:06:29

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-04-13 06:09:35


```
<gfurnish> I changed from __domain to _domain because homspace uses MI so there is no easy way to cython it, but that makes it easy to grab the attribute directly for places in coercion where speed matters
<mabshoff> ok
<gfurnish> the other change was -O2 spyx's
<mabshoff> yeah, saw that
<gfurnish> and finally I moved to a try->except instead of a has_key in coercion in parent.pyx
<mabshoff> :)
<gfurnish> maybe I should just paste those three sentences into the description
```



---

Comment by mabshoff created at 2008-04-13 07:40:05

Patch passes doctest on Sage 3.0.alpha4. Somebody else needs to take a closer look and figure out of all of this is a good idea.

Cheers,

Michael


---

Comment by cwitty created at 2008-04-13 17:54:38

It all looks good to me.  testall passes (on 3.0 alpha3), the new code in parent.pyx is equivalent and plausibly faster (although I didn't benchmark it), and reducing optimization on .spyx files from -O3 to -O2 is good.


---

Comment by mabshoff created at 2008-04-13 18:35:54

Resolution: fixed


---

Comment by mabshoff created at 2008-04-13 18:35:54

Merged in Sage 3.0.alpha5
