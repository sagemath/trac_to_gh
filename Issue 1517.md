# Issue 1517: Make sure a minimum of space is available to build component

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-15 02:35:11

Assignee: was

Many people have run out of disc space while building Sage. So check in `sage-spkg` if at least K MB are free on the partition we are building Sage in. K should be a couple hundred Megabytes in my opinion ;) We might also print a warning once we go below another, higher threshold. 

Cheers,

Michael


---

Comment by jdemeyer created at 2013-06-13 12:31:10

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-06-13 12:31:10

It's not the job of Sage to check filesystem space. Besides, this looks very hard to do in a portable way.


---

Comment by jdemeyer created at 2013-06-13 12:31:26

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-19 12:21:20

Resolution: wontfix
