# Issue 1684: Intelligent indentation when user presses "enter".

Issue created by migration from https://trac.sagemath.org/ticket/1684

Original creator: boothby

Original creation time: 2008-01-04 23:24:15

Assignee: boothby

Common IDE feature:  

 1. if the cursor is in an indented block, pressing "enter" should add a line which has the same indentaion as the previous line.
 1. if the cursor is in a line with, for example, an "if" statement, pressing enter should increase indentation on the next line.



---

Comment by boothby created at 2008-01-04 23:26:34

First installment, implements item 1.


---

Attachment

Patch ruins IE compatability, do not use.  :(


---

Comment by craigcitro created at 2008-06-20 04:27:45

Changing keywords from "" to "editor_wstein".


---

Comment by jason created at 2008-07-19 18:42:01

I'm not sure of your logic to accomplish #2 (I couldn't seem to find it in the bundle), but it seems that it would be easy to just indent more on the next line if the current line ends in a ":".


---

Comment by mabshoff created at 2008-11-04 20:25:10

There is also an attempt to do this at #4440.

Cheers,

Michael


---

Comment by boothby created at 2009-01-22 00:02:08

Resolution: invalid


---

Comment by boothby created at 2009-01-22 00:02:08

Replaced by #4440.
