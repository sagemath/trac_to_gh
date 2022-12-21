# Issue 2421: .round(), .floor(), .ceil(), and .trunc() on RealNumber should have the same return type

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-07 15:23:43

Assignee: somebody

Currently the `RealNumber` methods .round() and .trunc() return `RealNumber`, but .floor() and .ceil() return `Integer`.  I think that all four methods should return `Integer`.


---

Attachment


---

Comment by dfdeshom created at 2008-03-10 20:18:31

Changing status from new to assigned.


---

Comment by dfdeshom created at 2008-03-10 20:18:31

Changing assignee from somebody to dfdeshom.


---

Comment by malb created at 2008-03-12 09:41:01

patch looks good. I say apply.


---

Comment by mabshoff created at 2008-03-12 19:41:26

Didier, please submit mercurial patches in the future so you will get proper credit for your patches in the changelog. In this case it was too late and now credit goes to me :(

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-12 19:41:47

Resolution: fixed


---

Comment by mabshoff created at 2008-03-12 19:41:47

Merged in Sage 2.10.4.alpha0
