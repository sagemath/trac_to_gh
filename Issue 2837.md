# Issue 2837: [witch patch, needs review] use twisted-8.0.1's blockingCallFromThread

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-04-07 00:14:16

Assignee: yi

This patch makes use of the official blockingCallFromThread method in twisted.internet.threads instead of the one supplied by dsage.


---

Attachment

Applies and passes tests on 3.0.alpha1 + new twisted spkg.


---

Comment by mabshoff created at 2008-04-07 01:23:49

Resolution: fixed


---

Comment by mabshoff created at 2008-04-07 01:23:49

Merged in Sage 3.0.alpha2
