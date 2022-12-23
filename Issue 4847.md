# Issue 4847: [with patch, needs review] Remove deadwood: sage/functions/elementary.py and sage/rings/interval.py

Issue created by migration from https://trac.sagemath.org/ticket/4847

Original creator: mabshoff

Original creation time: 2008-12-21 15:49:08

Assignee: mabshoff

CC:  wdj

The two files in question are ancient (2006 or earlier), not imported and deprecated. So let's get rid of them.

Cheers,

Michael


---

Attachment

After applying the patch, deleting the build directory followed by a "sage -ba" all doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 15:52:31

Changing status from new to assigned.


---

Comment by mhampton created at 2008-12-21 16:03:17

These files are clearly old and untested.  Interval.py is deprecated by its own author and it seems fine to remove it.  It is less clear to me that elementary.py is totally redundant, it would be good if David Joyner could explicitly comment on its usefulness.  Otherwise it looks reasonable to get rid of these.


---

Comment by mhampton created at 2008-12-21 16:04:30

David, can you comment on elementary.py?
Thanks,
Marshall


---

Comment by was created at 2008-12-22 22:06:35


```
14:03 < wstein> The interval.py file I wrote, and can be safely deleted.
14:03 < wstein> It was deprecated and it has been > 6 mnths.
14:04 < mabs> Well, I had never seen that file, which should tell you something :)
14:05 < wstein> The elementary functions thing is totally of a different nature.
14:05 < wstein> I very much doubt it has been replaced by something newer.
14:05 < wstein> And it's very useful for differential equations teaching.
14:05 < wstein> At least that was the intention.
14:05 < wstein> But I personally don't have interest in that.
14:06 < wstein> Best thing would be to delete it and have David -- if he cares -- submit a new
14:06 < wstein> patch that adds back a version that fully works.
```



---

Comment by mabshoff created at 2008-12-22 22:19:09

Merged in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-22 22:19:09

Resolution: fixed


---

Comment by wdj created at 2008-12-23 00:07:40

Sorry, for the late reply. I read some of these comments but missed the request to comment on this. 

Comments: I am unconvinced by the usefulness of the code in elementary.py (which I wrote, so I can be as critical as I want:-). It was written way before the excellent code implementing the symbolic expression rings. As William said, it was motivated by solving constant coefficient ODEs using the method of undetermined coefficients/annihilators. It was also motivated by a desire to experiment with ways to implement differential operator rings, but it does this unconvincingly as well. (I don't want to say "it does this badly" because it might be that rings of differential operators should be implemented as a method for the SR class - I don't know.)

Bottom line - I agree elementary should be dumped. However, I'm very interested in alternative approaches anyone comes up with, especially ones that implement differential operator rings properly.
