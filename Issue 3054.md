# Issue 3054: copying a graph doesn't copy _pos or _boundary

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-29 20:40:10

Assignee: rlm

This means that changing the position of nodes in the copy will affect the original.


---

Attachment

With #3054 and #3055 applied, doctests pass in the graphs/ directory.


---

Comment by rlm created at 2008-04-29 21:43:50

Have not run doctests, but I support this fix.


---

Comment by mabshoff created at 2008-04-30 02:16:42

#3054 and #3055 applied to my current merge tree doctest clean. So I am considering this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-30 02:17:36

Resolution: fixed


---

Comment by mabshoff created at 2008-04-30 02:17:36

Merged in Sage 3.0.1.alpha1
