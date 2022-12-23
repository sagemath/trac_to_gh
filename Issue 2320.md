# Issue 2320: sage -server, sage -worker, sage -dsage broken

Issue created by migration from https://trac.sagemath.org/ticket/2320

Original creator: yi

Original creation time: 2008-02-26 17:46:08

Assignee: yi

These shorthands are broken right now because of changes to the dsage scripts. We need to either 

1) remove these shorthands
2) fix them




---

Comment by yi created at 2008-02-29 06:38:43

patch for SAGE_ROOT/local/bin/sage-sage


---

Attachment

I've attached the patch, after applying it make sure to chmod +x sage-dsage-*. This is against the hg_scripts repository.


---

Comment by yi created at 2008-02-29 06:48:16

Changing status from new to assigned.


---

Comment by yi created at 2008-03-02 01:43:57

Reassigning to William for review since he's the man behind sage-sage :-)


---

Comment by yi created at 2008-03-02 01:43:57

Changing assignee from yi to was.


---

Comment by yi created at 2008-03-02 01:43:57

Changing status from assigned to new.


---

Comment by was created at 2008-03-02 08:10:56

> Reassigning to William for review since he's the man behind sage-sage :-)

What are you talking about?  sage-sage is an incomprehensible disaster :-)

 -- William


---

Comment by mabshoff created at 2008-03-14 17:37:44

Patch looks good to me. Positive review. I assume I need to apply #2322 also to make this work.


---

Comment by mabshoff created at 2008-03-14 17:41:44

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 17:41:44

Merged in Sage 2.10.4.alpha0
