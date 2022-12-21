# Issue 3321: Matrix.visualize_structure is too dark/messed up

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-05-28 13:38:50

Assignee: cwitty

Consider this example

```
sage: A = MatrixSpace(GF(2),2000,2000)(1)
sage: A.visualize_structure()
```


I've attached the output to this ticket (hint: the scaling is to blame) Somehow I believe Tom Boothby would have an easy time to fix this so I CC him :-)


---

Comment by malb created at 2008-05-28 13:39:48

png output which is way too dark (it should be white)


---

Attachment


---

Attachment

shows that the bug was indeed fixed


---

Comment by ddrake created at 2009-01-22 08:16:11

This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)


---

Comment by mabshoff created at 2009-01-22 10:51:07

Replying to [comment:2 ddrake]:
> This fixes the bug and the code is fine, but in the docstring I have a minor quibble: you remove a warning about libpng problems on OS X. If those problems haven't been fixed, we should leave the warning in the docstring. I'll give this a positive review if you put the little warning back (or show that the problem was fixed!)

The problem has been fixed, which is the reason the libpng.dylib problem pops up with various external packages. It was the tradeoff between the Sage library passing doctests and external code working, so I chose Sage. Hence this is positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 08:34:54

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 08:34:54

Resolution: fixed
