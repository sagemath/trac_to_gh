# Issue 5615: [with patch, not ready for review] use labels-as-values for fast_callable under gcc

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-26 06:55:34

Assignee: cwitty

This patch uses gcc's labels-as-values extension to (theoretically) speed up the instruction dispatch.  Unfortunately, on my 32-bit x86 laptop, it's about the same speed as before the patch (maybe a little slower).  I think this is due to poor instruction scheduling (that gcc can't fix with -fno-strict-aliasing), but trying to move the instructions around by hand makes the problem worse (it adds register pressure, which makes the register allocator do very bad things on 32-bit x86).

Doctests do NOT pass, and the patch is not fully documented. (I believe the patch works; the doctests that fail are looking at fast_callable internals that changed.) 


---

Attachment
