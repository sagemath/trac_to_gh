# Issue 3072: sage -i numeric-24.2 (and all other experimental packages) fails

Issue created by migration from https://trac.sagemath.org/ticket/3072

Original creator: was

Original creation time: 2008-05-01 14:20:19

Assignee: mabshoff

The problem is in local/bin/sage-download_package which checks for an error in the download very stupidly.  This needs to be rewritten.  The basic question is how to use urllib to tell whether a URL is valid or is a 404 not found. 

The thing that triggered this problem is that sagemath.org's server configuration somehow changed, which changed the error page displayed on failure. 


---

Comment by mabshoff created at 2008-05-01 14:32:12

Changing priority from major to blocker.


---

Attachment


---

Comment by mabshoff created at 2008-05-02 11:41:40

Resolution: fixed


---

Comment by mabshoff created at 2008-05-02 11:41:40

Merged in Sage 3.0.1.rc0
