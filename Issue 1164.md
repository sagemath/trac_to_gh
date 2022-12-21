# Issue 1164: Error in tutorial documentation about %hist

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2007-11-13 22:12:25

Assignee: tba

In the interactive tutorial for SAGE, page "3.1 Your SAGE session", the documentation should make it clear that the %hist command does not work in the SAGE notebook, and that one cannot type in %hist and assume that it will work. It should also be noted that __ and _oh do not work in the notebook (although _ does).

Also, in the line "The PATHhastheSAGEbindirectoryatthefront,soifyourungp,gap,singular,maxima,etc.,yougettheversionsincludedwithSAGE. 
", it looks like an end-maths-environment symbol has been omitted.


---

Comment by mhansen created at 2007-12-06 21:17:38

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-06 21:17:38

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2007-12-07 21:58:31

Apply #1348 first.


---

Attachment

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-09 11:58:45

Merged in 2.9.alpha2.


---

Comment by mabshoff created at 2007-12-09 11:58:45

Resolution: fixed
