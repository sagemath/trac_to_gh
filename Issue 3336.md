# Issue 3336: DyckWords(n) should use an iterator

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-05-30 00:44:34

Assignee: ddrake

CC:  sage-combinat

Currently, DyckWords(n) creates a list, which uses a lot of memory and is slow. See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/8b739bb399f2e3d4).


---

Comment by ddrake created at 2008-05-30 06:42:50

Patch attached.


---

Attachment

Looks good.  Thanks for this Dan!  I also added it to 2144.


---

Comment by mabshoff created at 2008-05-31 05:56:41

Resolution: fixed


---

Comment by mabshoff created at 2008-05-31 05:56:41

Merged in Sage 3.0.3.alpha1
