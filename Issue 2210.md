# Issue 2210: make checkversion.pl complain about old XCode releases

Issue created by migration from https://trac.sagemath.org/ticket/2210

Original creator: mabshoff

Original creation time: 2008-02-19 18:01:31

Assignee: mabshoff

Many build problems on OSX reported to sage-devel and sage-support are due to old or even ancient XCode releases. One contributing factor seems to be that Apple's update service does not automatically update XCode.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-19 18:01:43

Changing status from new to assigned.


---

Comment by jdemeyer created at 2012-03-20 22:30:49

This is now taken care of by the prereq script.


---

Comment by jdemeyer created at 2012-03-20 22:30:49

Changing status from new to needs_review.


---

Comment by kini created at 2012-05-16 14:13:08

Doesn't that mean we should close this ticket and not just set it to needs_review?


---

Comment by kini created at 2012-05-16 14:13:08

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-05-21 08:04:24

Resolution: worksforme
