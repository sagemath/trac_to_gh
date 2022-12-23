# Issue 4429: notebook -- wrong display of message " Please enable cookies and try again."

Issue created by migration from https://trac.sagemath.org/ticket/4429

Original creator: was

Original creation time: 2008-11-03 01:17:40

Assignee: boothby

CC:  mhansen

It was reported in sage-support, and I just experienced it myself, that sometimes the sage notebook will give an error on login:

```
Please enable cookies and try again.
```

even though cookies are enabled.   When this just happened to me, I tried
several times to login and it would not work -- always giving that error.
Then I tried deleting all cookies in the cookie cache, and login worked fine.
Thus somehow we're getting the above error when there is a stale cookie.
This is somewhat difficult to replicate, but there is definitely a major
bug here.  Possibly reading the code in the notebook that produces
that message, would produce by pure thought what the problem is.


---

Comment by timdumol created at 2009-12-06 13:52:50

The message now reads: "Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again," which I think is clear enough. This should probably be closed.


---

Comment by was created at 2009-12-09 16:26:55

Resolution: fixed


---

Comment by was created at 2009-12-09 16:26:55

OK.  I would really like to fix the problem though, since this should never happen when cookies are enabled.  It happens a lot for me when I try safari on os x.
