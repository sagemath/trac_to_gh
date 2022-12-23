# Issue 2291: [with patch, needs additional work] Laurent Polynomial Rings

Issue created by migration from https://trac.sagemath.org/ticket/2291

Original creator: roed

Original creation time: 2008-02-24 10:24:07

Assignee: roed

CC:  jbandlow@gmail.com

Jason Bandlow requested Laurent polynomial rings.  I've implemented them.  They need doctests, and need to have some NotImplementedErrors implemented.  :-)


---

Attachment

Initial implementation


---

Comment by mhansen created at 2008-02-25 10:28:04

Changing assignee from roed to mhansen.


---

Comment by mhansen created at 2008-02-25 10:28:04

I'm working on polishing this up.


---

Comment by mhansen created at 2008-02-25 10:28:04

Changing status from new to assigned.


---

Comment by roed created at 2008-02-26 10:58:02

second patch, on top of first.


---

Attachment

third patch, on top of second.


---

Attachment

Simple fix to exponent(); mostly just making sure i understand the patch process


---

Attachment

improved init and coefficient, added doctests


---

Comment by mabshoff created at 2008-04-12 12:38:06

Resolution: duplicate


---

Comment by mabshoff created at 2008-04-12 12:38:06

Mike Hansen and Jason Bandlow improved David Roe's original code. That code has been posted at #2895, so I am closing this ticket as a dupe.

Cheers,

Michael
