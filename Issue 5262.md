# Issue 5262: L-series attached to modular forms has a major bug in how it computes the sign of the functional equation

Issue created by migration from https://trac.sagemath.org/ticket/5262

Original creator: was

Original creation time: 2009-02-14 00:47:10

Assignee: craigcitro

This is wrong:


```

The following computation should produce identical values in the last
line:

E=EllipticCurve('37b2')
h=E.modular_form()
Lh = h.cuspform_lseries()
LE=E.lseries()
h.elliptic_curve()==E, Lh(1), LE(1)

The output is:

(True, 0, 0.725681061936153)
```


This is because the Atkin-Lehner sign is computed wrong in sage/modular/modform/element.py.  In fact, there one finds the code:

```
            m = ModularSymbols(N,l,sign=1)
            n = m.cuspidal_subspace().new_subspace()
            e = (-1)**(l/2)*n.atkin_lehner_operator().matrix()[0,0]
```


Notice that m has absolutely nothing to do with the modular form! 

The right fix is to implement an atkin_lehner_eigenvalue(...) function for modularforms, and that should in turn be implemented correctly, and should be called from the cuspform_lseries command.


---

Comment by mabshoff created at 2009-02-14 02:53:17

I already opened #5247 for this as I mentioned in the email, but I am closing that one as a dupe since this ticket has the better description.

This is not a ReST ticket, so bumping it to 3.4.1.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-05-01 08:03:00

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-05-01 08:03:00

Changing assignee from craigcitro to davidloeffler.


---

Comment by davidloeffler created at 2009-05-01 11:23:43

patch against 3.4.2.rc0


---

Attachment

Turns out there were actually two separate bugs: one for level 1 forms (which came up whenever the weight was not a multiple of 4) and one for forms of higher level. I've fixed both, and added doctests to check that they're fixed.


---

Comment by craigcitro created at 2009-05-07 09:47:33

So I think this patch looks pretty good by eye ... but I tried to apply it to a clean 3.4.2.rc0 tree, and I got some merge failures. David, could you just check to make sure you've got the right version posted and I'll go ahead and review this? (The merge failures don't seem too hard to sort out, but it'll probably still be faster for David than me.)


---

Comment by davidloeffler created at 2009-05-07 10:13:16

The merge failures are because the patch depends on my patch for #4357; I forgot to mention this in the description. Sorry. (This was because I independently implemented an "atkin_lehner_eigenvalue" function for newforms as part of fixing 4357, and then realised that this could be used to fix this one as well.)


---

Comment by craigcitro created at 2009-05-08 07:48:02

Two thumbs up! I don't even see anything to nitpick about. Merge away!


---

Comment by mabshoff created at 2009-05-11 08:16:36

Resolution: fixed


---

Comment by mabshoff created at 2009-05-11 08:16:36

Merged in Sage 4.0.alpha0.

Cheers,

Michael
