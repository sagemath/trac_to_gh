# Issue 2439: ZZ.random_element() crashes Sage with probability 2^-31

Issue created by migration from https://trac.sagemath.org/ticket/2439

Original creator: cwitty

Original creation time: 2008-03-09 17:40:22

Assignee: cwitty

ZZ.random_element() does an integer divide by zero once every 2<sup>31</sup> calls.

I'll make a patch as soon as my rc3 build finishes.


---

Attachment


---

Comment by cwitty created at 2008-03-09 18:45:31

The attached patch fixes the crash, fixes other crashes in related code, and deletes some dead code.


---

Comment by mabshoff created at 2008-03-09 19:01:31

Patch looks good to me. Good that cwitty found a very unlikely bug to hit :)


---

Comment by mabshoff created at 2008-03-09 19:03:29

Merged in Sage 2.10.3.rc4


---

Comment by mabshoff created at 2008-03-09 19:04:00

Resolution: fixed


---

Comment by mabshoff created at 2008-03-09 19:04:00

Merged in Sage 2.10.3.rc4 - and this time I am closing the ticket, too.
