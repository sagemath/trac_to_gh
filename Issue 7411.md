# Issue 7411: improve the speed of inverse RSK

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-11-08 14:01:29

Assignee: mhansen

CC:  hivert mhansen sage-combinat

Keywords: Robinson-Schensted

The main improvement comes from the use of a binary search, just as in #7408.


---

Comment by ylchapuy created at 2009-11-08 14:04:15

needs #7408


---

Attachment


---

Comment by ylchapuy created at 2009-11-08 14:04:55

Changing status from new to needs_review.


---

Comment by hivert created at 2009-11-08 16:46:53

This in indeed a very good idea ! I'm frustrated I didn't get it myself :-) 

Patch is good and ready to go. 

Cheers,

Florent


---

Comment by hivert created at 2009-11-08 16:46:53

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-12 06:32:55

Resolution: fixed
