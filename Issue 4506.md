# Issue 4506: planarity ignores error code when adding edge

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-13 01:21:30

Assignee: rlm

CC:  ekirkman bober

The planarity code ignores errors when adding edges.  This patch also shortcuts the planarity checking when adding an edge returns the NONPLANAR code.


---

Attachment


---

Comment by mabshoff created at 2008-11-13 03:27:29

The patch here ought to add a doctest :)

Cheers,

Michael


---

Comment by jason created at 2008-11-13 03:55:31

I don't see what to doctest.  I personally didn't come across any errors, I'm just adding the checking as good programming practice.  As for the shortcut in the nonplanar case, I'm just doing exactly what Boyer does in his C program.  The program gave the correct answers before, now it just doesn't worry about finding a kuratowski subgraph if it is not needed.

Again, I didn't see any errors before, so I can't put in a doctest that didn't work before, but does after the patch.  This is pro-active bugfixing, not reactive bugfixing :).


---

Comment by robertwb created at 2008-11-13 23:27:17

It looks good to me. 

Unless one knows how to make the C program fail (out of memory?) I don't see what doctest to add. The result is the same, so I think the existing doctests cover it.


---

Comment by mabshoff created at 2008-11-14 03:30:53

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-14 03:30:53

Resolution: fixed
