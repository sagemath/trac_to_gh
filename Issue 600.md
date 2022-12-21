# Issue 600: sage -t --optional multi_polynomial_element.py takes *way* too  ram

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-06 17:48:58

Assignee: was

It takes nearly a gig at some points, which is bad on a system like my laptop.  This is quite painful.


---

Comment by mabshoff created at 2007-12-18 09:27:05

I think this has been fixed. Can anybody confirm?

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 04:02:43

As of Sage 2.11 this doctest is broken. I assume that #2171 might fix the issue.

Cheers,

Michael


---

Comment by mhansen created at 2009-01-22 14:37:04

I just ran this and measured memory usage under top and it was fine / hardly noticeable.  I'm going to mark this as invalid.


---

Comment by mhansen created at 2009-01-22 14:37:04

Resolution: invalid
