# Issue 6721: spell-check all modules under sage/media

Issue created by migration from https://trac.sagemath.org/ticket/6721

Original creator: mvngu

Original creation time: 2009-08-10 04:13:58

Assignee: tba

As the subject says.


---

Comment by mvngu created at 2009-08-11 12:32:44

based on Sage 4.1.1.rc2


---

Attachment

I ran `sage -merge <ticket_number> -t directory` and started the notebook without problems.


---

Comment by mpatel created at 2009-08-14 07:28:02

I suppose I should run `sage -t -long -optional -randorder` later with all spelling patches applied.


---

Comment by mpatel created at 2009-08-14 07:35:53

I also ran `sage -docbuild reference html --jsmath` without Sphinx warnings or errors.


---

Comment by mvngu created at 2009-08-14 07:56:51

Resolution: fixed
