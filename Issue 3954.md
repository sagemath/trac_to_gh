# Issue 3954: bug in elliptic curve period_lattice

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-26 09:03:39

Assignee: was

CC:  alexghitza


```
Hi,

Is this a bug or am I doing something stupid? I get different
precisions the first and second time I run the same command.

----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.6, Release Date: 2008-07-30                       |
| Type notebook() for the GUI, and license() for information.        |
sage: E = EllipticCurve('37a')
sage: E.period_lattice().basis(prec=30)

(2.993458646231959629832009979452508177797583791370132985340523378563250356987,

2.451389381986790060854224831866525225349617289144796614656471406129152899999*I)
sage: E.period_lattice().basis(prec=30)

(2.9934586462319596298320099794525081777975837913701329853405233785632503569866829041203940673970514734358405271049472881941443872373720252543753766710932613753043332505965246252164473069072694510749057806365610445781725817135182427934263132488980086942438020870431669315,

2.4513893819867900608542248318665252253496172891447966146564714061291528999992568928911321280291810887126842188696618479754751998666167558016789381647830306324546902881738259304962523119593946698932473794558796569481958707269691493740581897037588157844669302474334546641*I)


Best regards,

Håkan
```


This is definitely a bug.  The output precision should be as given by the prec option.  The bug is caused by a mistake in the caching code, surely.   This will likely be easy to fix.


---

Attachment

As William pointed out, this was a caching problem.  The bug was actually in E.pari_curve, where the (somewhat convoluted) code logic did not agree with the specification from the docstring.  I've rewritten that code in a way that makes sense (to me) and that works.  I've added a doctest to pari_curve(), but also to period_lattice().basis(), illustrating both the issue reported here and the actual bug.

I noticed that the next function, E.pari_mincurve, has the exact same problem, and I fixed it in the exact same way.  Finally, pari_mincurve and pari_curve are clearly parallel functions that should have the same behavior for consistency, but they didn't.  So I changed pari_mincurve to behave just like pari_curve.


---

Comment by cremona created at 2008-09-03 19:52:08

I applied this to 3.1.2.alpha4 + both patches for 3377 + both patches for 1115 (which have already been merged into 3.1.2.rc0), and miraculously they worked fine (just a little fuzz).  That was lucky since all these patches involve pari precision, pari curves, and period lattice precision.

All doctests in sage.schemes.elliptic_curves pass, and the patch looks good.  I say it should pass.


---

Comment by mabshoff created at 2008-09-04 01:31:35

Merged in Sage 3.1.2.rc0


---

Comment by mabshoff created at 2008-09-04 01:31:35

Resolution: fixed


---

Comment by cremona created at 2008-09-04 16:53:07

There's still something strange going on which I'm going to have to wait until 3.1.2.rc0 since I've messed up my 3.1.2.alpha4 (ok, so I could rebuild it and apply all those patches...):

```
sage: E = EllipticCurve('37a')                     
sage: E.period_lattice().basis(prec=30)[0].parent()
Real Field with 896 bits of precision
sage: E.period_lattice().basis(prec=100)[0].parent()
Real Field with 3136 bits of precision
```

I discovered this after seeing that #1903 was a duplicate.

If mabshoff could run the above code with the latest rc0 build then we'd know if there was something needing to fix or not.


---

Comment by AlexGhitza created at 2008-09-04 23:35:42

This weird behavior was there before the patch as well.  Now, after the patch, it is weird but consistent :)

There's definitely a problem in communicating with pari regarding precision.  Part of it is that pari rounds up to the next word, so it often gives you a bit more precision than you asked for.  But there's more going on than just that, probably somewhere in the interface code.

Strictly speaking, this ticket was about consistency of the period_lattice functions.  The issue that John found seems to be orthogonal to this, so I'm opening a new ticket for it: #4064.


---

Comment by cremona created at 2008-09-05 08:11:39

Replying to [comment:6 AlexGhitza]:
> This weird behavior was there before the patch as well.  Now, after the patch, it is weird but consistent :)
> 
> There's definitely a problem in communicating with pari regarding precision.  Part of it is that pari rounds up to the next word, so it often gives you a bit more precision than you asked for.  But there's more going on than just that, probably somewhere in the interface code.
> 
> Strictly speaking, this ticket was about consistency of the period_lattice functions.  The issue that John found seems to be orthogonal to this, so I'm opening a new ticket for it: #4064.

Thanks, Alex.  I'm looking into it.
