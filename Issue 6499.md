# Issue 6499: minor formatting and typo in the script sage-location

Issue created by migration from https://trac.sagemath.org/ticket/6499

Original creator: mvngu

Original creation time: 2009-07-09 11:26:43

Assignee: cwitty

Keywords: sage-location

Take a binary distribution of Sage, uncompress it, and start up Sage for the first time. You should see something similar to the following in your terminal:

```
[mvngu@sage sage-4.1.rc1-x86_64-Linux]$ ./sage 
----------------------------------------------------------------------
----------------------------------------------------------------------
The SAGE install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH (please wait at
most a few minutes)...
Do not interrupt this.
```

The message line starting with "Regenerating Python.pyo..." overflows the standard terminal width, which is 80 characters. And the name "SAGE" should be changed to "Sage". This is no big deal, I know, but it occasional annoys me, especially the said long message line.


---

Attachment

based on Sage 4.1.rc1


---

Comment by mvngu created at 2009-07-09 11:48:06

After applying the patch `trac_6499.patch`, you should get something like the following:

```
[mvngu@sage sage-4.1.rc1-x86_64]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
The Sage install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(please wait at most a few minutes)...
Do not interrupt this.
```



---

Comment by mvngu created at 2009-07-16 14:35:20

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:21:04

Resolution: fixed
