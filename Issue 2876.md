# Issue 2876: sage/server/notebook/twist.py doctest fails when dsage certificates are not present

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-04-11 04:52:50

Assignee: boothby

Since it's trying to use https, the notebook object will try to generate a self signed certificate when one is not present already. This doesn't work with doctesting since we can't expect user interaction. The fix switches the notebook server to use http instead. It looks like robert did a good job of disabling creating accounts so I don't see any new security holes created by this. 


---

Comment by yi created at 2008-04-11 05:12:45

Cwitty pointed out that if you use the secure=False option, one gets logged on automatically. Does anyone know of an easy way to turn that feature off when doctesting?


---

Attachment

Works perfectly.


---

Comment by mabshoff created at 2008-04-12 00:11:36

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-12 00:11:36

Resolution: fixed
