# Issue 5394: [with patch, needs review] Remove the remnants of the docs from sage-ptest and make it ignore the devel/sage/build directory

Issue created by migration from https://trac.sagemath.org/ticket/5394

Original creator: mhansen

Original creation time: 2009-02-27 17:14:13

Assignee: cwitty




---

Attachment

Excellent, couldn't have done it better myself :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-27 23:07:33

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-27 23:07:33

Resolution: fixed


---

Comment by mabshoff created at 2009-02-28 12:19:57

This patch actually does not ignore the bits in build and I am not quite sure why the patch doesn't work.

Mike: Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 12:35:52

Ok, figured it out - reviewer patch coming up.

Cheers,

Michael


---

Attachment

Oops, the reviewer patch had some debug output in it. I removed that in the tree and did another checkin.

Cheers,

Michael
