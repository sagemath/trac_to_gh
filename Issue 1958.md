# Issue 1958: [with patch, needs review] fix problems with ANSI codes in sage0.py

Issue created by migration from https://trac.sagemath.org/ticket/1958

Original creator: craigcitro

Original creation time: 2008-01-28 04:36:50

Assignee: craigcitro

There were some annoying doctest failures in sage0.py in 2.10.1.rc1, which are due to weird issues with ANSI codes ending up in the result of eval(). This parses them to get the correct answer.

I think there's possibly a deeper readline issue here, but that's mostly wild speculation.


---

Attachment


---

Comment by craigcitro created at 2008-01-28 04:40:06

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-28 06:37:38

There is some more info on #1942, which now has been closed as a dupe of this ticket.

Cheers,

Michael


---

Attachment

Attached a better band-aid for this, at wstein's suggestion.


---

Comment by craigcitro created at 2008-01-28 07:04:49

Note: you only want the second patch; it's a *replacement* for the first, not in addition to.


---

Comment by jsp created at 2008-01-28 11:36:24

Worked for me on Fedoa 7:



```
sage -t  devel/sage-main/sage/interfaces/sage0.py           ^[[?1034h
         [7.1 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.1 seconds

```


How about the extra escape code on each test line?


---

Comment by mabshoff created at 2008-01-29 12:43:52

Resolution: fixed


---

Comment by mabshoff created at 2008-01-29 12:43:52

Merged 1958-bandaid-v2.patch in Sage 2.10.1.rc3
