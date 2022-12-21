# Issue 4113: [with patch, needs review] Doctest failure in free_module.py

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-09-14 06:29:58

Assignee: craigcitro

I added a doctest in #4091 without realizing that it might differ from architecture to architecture, even though this was the reason for adding it. I've added # random and some explanation. 


---

Attachment


---

Comment by mabshoff created at 2008-09-14 06:51:45

Patch is good, I was about to post the same fix :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 09:12:38

Merged in Sage 3.1.2.rc3


---

Comment by mabshoff created at 2008-09-14 09:12:38

Resolution: fixed
