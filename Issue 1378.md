# Issue 1378: add ssh-client (i.e., ssh-keygen) as a required package in various places in the docs.

Issue created by migration from https://trac.sagemath.org/ticket/1378

Original creator: was

Original creation time: 2007-12-03 06:25:02

Assignee: tba


```
no, there was no ssh-keygen installed, after installation (on Debian
Etch ssh-keygen is provided by the package ssh-client) it works
perfectly now without options, just notebook(),

this should be annotated in the installation manual in the list of
required packages,
and the possibility notebook(secure=false) if it's not installed

thank you very much....
```



---

Comment by mhansen created at 2007-12-06 05:44:16

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2007-12-06 05:44:16

Changing assignee from tba to mhansen.


---

Comment by mabshoff created at 2007-12-09 10:18:18

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-09 10:18:30

Resolution: fixed


---

Comment by mabshoff created at 2007-12-09 10:18:30

Merged in 2.9.alpha2.
