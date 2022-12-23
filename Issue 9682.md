# Issue 9682: fix a bug in message error in perfect mathings

Issue created by migration from https://trac.sagemath.org/ticket/9682

Original creator: vferay

Original creation time: 2010-08-04 03:59:47

Assignee: sage-combinat

CC:  hivert

everything is in the title

[[[
sage: PerfectMatching(6)
...
NameError: global name 'sage' is not defined
]]]


---

Attachment


---

Comment by vferay created at 2010-08-04 05:15:52

Changing status from new to needs_review.


---

Attachment

Patch good to go !


---

Comment by hivert created at 2010-08-04 05:23:31

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-07 05:52:58

Should I merge only [attachment:trac_9682_fix_perfectmatching_error_message_vf.patch]?


---

Comment by mpatel created at 2010-08-08 04:25:08

Replying to [comment:3 mpatel]:
> Should I merge only [attachment:trac_9682_fix_perfectmatching_error_message_vf.patch]?

Oops, I missed the note in the description.  Sorry!


---

Comment by mpatel created at 2010-08-09 09:49:22

Resolution: fixed


---

Comment by chapoton created at 2017-07-19 08:25:15

name with accent
