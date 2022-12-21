# Issue 4846: Doctesting should create an empty init.sage if it doesn't exist

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-12-21 09:25:01

Assignee: mabshoff

CC:  craigcitro

Often when we do fix IPython related problems things break when init.sage is present. So make doctesting create an empty init.sage so that this is potentially caught.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 11:42:38

There are doctests in 3.2.2 that fail with an init.sage, so all we need to do is to add the check if it is missing in sage-sage when running doctests and then create an empty one to detect this particular bug.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-26 23:21:26

Changing status from new to assigned.


---

Attachment


---

Comment by burcin created at 2008-12-26 23:50:31

After pestering mabshoff on IRC about this a little, I am convinced this is a good quick solution to avoid most init.sage problems we missed during some of the recent releases. Positive review. :)


---

Comment by mabshoff created at 2008-12-26 23:53:41

Resolution: fixed


---

Comment by mabshoff created at 2008-12-26 23:53:41

Merged in Sage 3.2.3.final
