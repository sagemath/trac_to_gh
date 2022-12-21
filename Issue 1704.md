# Issue 1704: [with patch] replace _DivPolyContext by _multiply_point

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-01-06 23:19:41

Assignee: was

This patch replaces the `_DivPolyContext` class with a new function `_multiply_point`. The main downside of the original `_DivPolyContext` is that it's very recursive, and I started overflowing python's stack for some large problems I needed to play with. The new function is not recursive, and also turns out to be slightly faster.



---

Attachment


---

Comment by ncalexan created at 2008-01-20 06:53:12

I can't speak to mathematical correctness, but the patch looks good to me.  Apply.


---

Comment by mabshoff created at 2008-01-21 05:52:54

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 05:52:54

Merged in Sage 2.10.1.alpha1
