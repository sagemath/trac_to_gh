# Issue 361: implement tate's algorithm over number fields.

Issue created by migration from https://trac.sagemath.org/ticket/361

Original creator: was

Original creation time: 2007-05-07 16:18:33

Assignee: was

See attached file.

```
From John Cremona:

Sorry I promised this a while ago.

This is essentially the file I gave to Magma in '02 or '03 which became
their package/Geometry/CrvEll/minmodel.m after a bit of work by Nils
Bruin and Geoff Bailey.  From what I can tell their changes are only
cosmetic (e.g. replacing my intrinsic with function somewhere, and also
fiddling with the input & output parameters to make the order of terms
consistent with other Magma functions.

Apart from that I just replaced UniformizingParameter() with
MyUniformizingParameter() as explained in the comment.

You can do what you like with this now!

John
```



---

Comment by was created at 2007-05-07 16:18:49

Implementation of tate's algorithm in MAGMA


---

Attachment


---

Comment by roed created at 2007-10-09 13:11:25

Changing assignee from was to roed.


---

Comment by roed created at 2007-10-09 13:11:25

Changing status from new to assigned.


---

Comment by cremona created at 2008-04-07 19:39:00

This was implemented ages ago and so can be closed.


---

Comment by mabshoff created at 2008-04-07 19:41:20

Resolution: fixed


---

Comment by mabshoff created at 2008-04-07 19:41:20

Fixed as per John Cremona's request.

Cheers,

Michael
