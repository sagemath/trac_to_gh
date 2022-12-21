# Issue 599: sage -valgrind log file is placed in bad location.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-06 17:25:55

Assignee: malb or mabshoff




---

Comment by burcin created at 2007-09-06 17:34:01

change location of valgrind output


---

Attachment

On IRC it was suggested the place should be $HOME/.sage/sage-memcheck.$PID

Sep 06 19:25:58 <malb>  I vote for $HOME/.sage/sage-memcheck.PID
Sep 06 19:26:23 <wstein>        #599: +1


---

Comment by mabshoff created at 2007-09-06 18:59:42

Resolution: fixed
