# Issue 4783: [with patch; needs review] email -- create an "email" command, so users can easily notify themselves when their sage programs have completed some task

Issue created by migration from https://trac.sagemath.org/ticket/4783

Original creator: was

Original creation time: 2008-12-13 16:22:34

Assignee: cwitty

This was inspired by three things:

 1. I want a little script that will automatically email me whenever sagenb.org or any other website I manage stops responding for a certain amount of time.  

 2. Users every so often complain that sage.math doesn't have sendmail installed, so they can't put in code like `os.system('mail ...')`.  I.e., also, often people start a big computation, and it would be useful for them to get an email when it finishes.

 3. When I run the sage buildbot, it might be nice if the buildbot script could use sage to email me a summary of all failed tests (?).


---

Attachment


---

Comment by mabshoff created at 2008-12-14 05:47:20

Resolution: fixed


---

Comment by mabshoff created at 2008-12-14 05:47:20

Merged in Sage 3.2.2.rc0
