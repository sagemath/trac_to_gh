# Issue 5874: [with patch, needs review] Fix readline build on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/5874

Original creator: pjeremy

Original creation time: 2009-04-23 08:47:52

Assignee: mabshoff

CC:  chet.ramey@case.edu

Chase shared library name difference on FreeBSD. Without this patch, the build claims that expected files don't exist.


---

Attachment


---

Comment by mhansen created at 2009-06-20 02:26:26

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-06-20 02:26:26

Looks good to me.

The spkg with the patch incorporated is at http://sage.math.washington.edu/home/mhansen/readline-5.2.p7.spkg


---

Comment by pjeremy created at 2009-06-27 08:18:49

Cc maintainer.  Apologies for neglecting this before


---

Comment by rlm created at 2009-07-02 23:07:32

Resolution: fixed
