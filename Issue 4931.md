# Issue 4931: [with patch, needs review] Sage 3.2.3.final: Fix various Solaris 10 build issues in the Sage library

Issue created by migration from https://trac.sagemath.org/ticket/4931

Original creator: mabshoff

Original creation time: 2009-01-03 04:47:39

Assignee: mabshoff

There are a couple buglets in the Sage library that cause build issues on Solaris. The attached patch fixes those.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-03 04:47:46

Changing status from new to assigned.


---

Comment by was created at 2009-01-03 04:53:18

I read the patch.  Positive review if it still works on linux.


---

Attachment


---

Comment by was created at 2009-01-03 06:32:12

I found some major breakage exposed by actually looking at the code. See #4932. 

With the attached referee followup patch this gets positive review.


---

Attachment


---

Comment by mabshoff created at 2009-01-03 06:42:49

The referee patch passes doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-03 06:43:03

Resolution: fixed


---

Comment by mabshoff created at 2009-01-03 06:43:03

Merged both patches in Sage 3.2.3.final
