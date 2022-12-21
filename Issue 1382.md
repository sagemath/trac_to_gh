# Issue 1382: conversion of sage matrices to mathematica is just completely totally broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-03 17:09:37

Assignee: was

We have


```
sage: n = matrix(QQ, 3, range(9))
sage: n._mathematica_init_()
'{{0},{1},{2},{3},{4},{5},{6},{7},{8}}'
```


but we should have


```
sage: n = matrix(QQ, 3, range(9))
sage: n._mathematica_init_()
'{{0,1,2},{3,4,5},{6,7,8}}'
```






---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by TimothyClemans created at 2008-02-17 00:31:35

Changing assignee from was to TimothyClemans.


---

Comment by TimothyClemans created at 2008-02-17 00:31:35

Changing status from new to assigned.


---

Attachment


---

Comment by ncalexan created at 2008-02-17 01:13:40

This will not work, since it does not appear to be recursive.  For example:


```
sage: var('x, y, z, b')
(x, y, z, b)
sage: f = sin(x^2) + y^z
sage: f
y^z + sin(x^2)
sage: f._mathematica_init_()
'(Sin[(x) ^ (2)]) + ((y) ^ (z))'
sage: M = matrix(1, 2, [f, f^2]); M
[    y^z + sin(x^2) (y^z + sin(x^2))^2]
```


Also, please post a unified patch making it easy to see just the total changes.


---

Attachment

(this one by William and Timothy) apply this patch right after applying 1382_2.patch


---

Attachment


---

Comment by ncalexan created at 2008-02-23 01:04:43

Patch looks good, I say apply.

Is _mathematica_init_ guaranteed not to require Mathematica?  If not, some more doctests need to be declared optional.  Otherwise, looks good.


---

Comment by was created at 2008-02-23 01:06:52

> Is _mathematica_init_ guaranteed not to require Mathematica? 

Yes.  It returns a string is must not call Mathematica. 

William


---

Comment by mabshoff created at 2008-02-24 19:59:57

Somebody ought to clue be in 

 * which patches to apply in which order (the comments are unclear)
 * if all problems regarding optional doctests are solved, i.e. the last comment by William

Cheers,

Michael


---

Comment by was created at 2008-02-24 20:39:37

Michael.  Apply 1382_2.patch then 1382_5-part2of2.patch.  And the comment about optional is not applicable since _mathematica_init_ should never depend on mathematica.


---

Comment by TimothyClemans created at 2008-02-24 20:48:27

William's patch seems to be editing 1382_5.patch. task_1832_2.patch depends on ticket_1382.patch and it doesn't have lines like "return mathematica.mathematica(tuple(self))" which are in 1382_5.patch and show up in red on http://trac.sagemath.org/sage_trac/attachment/ticket/1382/1382_5-part2of2.patch


---

Comment by mabshoff created at 2008-02-24 21:05:12

The patches at this ticket are a mess either way: For task_1832_2.patch I need to ticket_1382.patch. But at that point 1382_5-part2of2.patch doesn't apply cleanly. So, in conclusion: Please post a single patch that has all the changes and that applies cleanly against 2.10.2. To do that merge the fixes back by hand, do not just post a bundle with all patches applied. 

Cheers,

Michael


---

Comment by was created at 2008-02-24 21:13:31

I made a typo.  Simply apply 

  * 1382_5.patch
  * 1382_5-part2of2.patch. 

That's it.  2 patches.   They should not be flattened. 

William


---

Comment by mabshoff created at 2008-02-24 21:25:13

Resolution: fixed


---

Comment by mabshoff created at 2008-02-24 21:25:13

Merged 1382_5.patch and 1382_5-part2of2.patch in Sage 2.10.3.alpha0. Thanks William for the clarification.
