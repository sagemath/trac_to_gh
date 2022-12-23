# Issue 3834: notebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!

Issue created by migration from https://trac.sagemath.org/ticket/3834

Original creator: was

Original creation time: 2008-08-13 06:23:47

Assignee: boothby

notebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!

This is a major showstopper bug.

And it's either my fault (or Timothy Clemans), but probably me. 

The solution will be to rewrite how full text search works to just look at the filesystem.
I'm guessing right now it is suddenly doing something really stupid as a result of the 
optimizations I made recently to the notebook.


---

Attachment


---

Comment by mabshoff created at 2008-08-15 09:54:47

I am happy with this patch. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-15 09:55:50

Resolution: fixed


---

Comment by mabshoff created at 2008-08-15 09:55:50

Merged in Sage 3.1.rc0
