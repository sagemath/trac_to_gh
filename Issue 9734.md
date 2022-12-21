# Issue 9734: METATICKET Doc test failures on 32-bit Solaris 10 and 32-bit OpenSolaris on x86 CPUs.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-12 16:09:46

Assignee: drkirkby

CC:  jsp jhpalmieri

Although the 32-bit SPARC version of Sage passes all doc tests, there are still issues on 32-bit versions of Solaris/OpenSolaris on x86 hardware. This ticket summaries lists only failures on 32-bit builds, versions on x86 processors. 

64-bit versions have far more failures, and will need another ticket to address them. 



---

Comment by drkirkby created at 2010-08-15 23:50:39

I discovered the GFAN issues were a mistake on my part, so #9736 was closed as invalid, and those doctest failures can be ignored. 

Dave


---

Comment by jdemeyer created at 2015-09-07 06:11:56

All linked tickets are closed, so I guess we can close this.


---

Comment by jdemeyer created at 2015-09-07 06:11:56

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-07 06:12:02

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 13:58:43

Resolution: fixed
