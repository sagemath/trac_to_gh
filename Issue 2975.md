# Issue 2975: opening ports to conservative -- breaks on some os x systems

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-20 21:09:11

Assignee: boothby

on bsd.math and fermat this happens but shouldn't.  I'm sure it is my fault.


```
sage: inotebook()
The notebook files are stored in: /Users/was/.sage//sage_notebook
WARNING: Running the notebook insecurely may be dangerous.
Make sure you know what you are doing.
Port 8000 is already in use.
Trying next port...
Port 8001 is already in use.
Trying next port...
Port 8002 is already in use.
Trying next port...
Port 8003 is already in use.
Trying next port...
Port 8004 is already in use.
Trying next port...
Port 8005 is already in use.
Trying next port...
Port 8006 is already in use.
Trying next port...
Port 8007 is already in use.
Trying next port...
Port 8008 is already in use.
Trying next port...
Port 8009 is already in use.
Trying next port...
```



---

Attachment


---

Comment by mhansen created at 2008-04-21 03:49:26

Works for me on 64-bit Linux.


---

Comment by mabshoff created at 2008-04-21 04:06:22

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 04:06:22

Merged in Sage 3.0.rc1
