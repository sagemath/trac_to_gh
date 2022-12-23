# Issue 196: sage signal handler -- ctrl-c interrupt, etc.

Issue created by migration from https://trac.sagemath.org/ticket/196

Original creator: was

Original creation time: 2007-01-19 09:54:09

Assignee: was

Somewhat bizarrely, the SAGE _sig_on/_sig_off signal handling code
appears to be completely not doing anything at all.  Weird!  This is a
major bug that must be fixed before SAGE-2.0. 


---

Comment by malb created at 2007-01-20 00:16:48

Changing assignee from was to malb.


---

Comment by malb created at 2007-01-20 00:16:48

I believe to have fixed this bug in

csage: rev6
sage_source: rev2493


---

Comment by was created at 2007-01-21 21:51:43

Resolution: fixed


---

Comment by was created at 2007-01-21 21:51:43

Martin Albrecht fixed this -- it will be in SAGE-1.8.
