# Issue 4690: [with patch; needs review] Sage hangs on derivative of piecewise function

Issue created by migration from https://trac.sagemath.org/ticket/4690

Original creator: pbutler

Original creation time: 2008-12-04 01:22:32

Assignee: burcin

Derivatives of piecewise functions where some piece uses multiplication causes Sage to hang. Example code:


```
Piecewise([[(0,1), x * 2]]).derivative()
```


It hangs waiting for Maxima to return a result, which is because the expression it sends to Maxima is not formatted properly.


---

Attachment

Patch file for piecewise derivative


---

Comment by mabshoff created at 2008-12-04 01:24:34

Paul,

please make sure to assign a milestone. Usually that is the next open one.

Cheers,

Michael


---

Comment by mhansen created at 2008-12-04 08:29:12

Looks good to me.  This can go in.

But, piecewise.py needs some _MAJOR_ work for which I will open up a new ticket.


---

Comment by mabshoff created at 2008-12-04 14:12:42

Paul,

in the future please post hg patches and not diffs, i.e. check in your changes and then export a patch. In this case I have committed the changes in your name so that the credit in the hg log is properly assigned.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 14:13:06

Resolution: fixed


---

Comment by mabshoff created at 2008-12-04 14:13:06

Merged in Sage 3.2.2.alpha0
