# Issue 2204: Integrate Karim Belabas's HNF bug fix for pari

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-18 18:09:16

Assignee: mabshoff

Reported by William via the pari bug tracker:

```
---------- Forwarded message ----------
From: Karim Belabas <Karim.Belabas`@`math.u-bordeaux1.fr>
Date: Feb 18, 2008 2:49 AM
Subject: Re: Bug#741: Fwd: bug in PARI's mathnf function
To: William Stein <wstein`@`gmail.com>, 741-close`@`pari.math.u-bordeaux.fr


* William Stein [2008-02-16 23:47]:
> > Package: pari
> > Version: 2.3.3
[...]
> > PARI sometimes puts negative numbers in the *output* of mathnf(a, 1)[0],
> > which is a bug.

Indeed.

> >   * I didn't use mathnf(b) directly (the default option), since
> > already for a 20x18 matrix it
> > is too slow to be useful.

As documented.

[ Actually, I am going to change this: I don't see the point in defaulting
to a slow routine; let mathnf choose depending on the matrix size.
It should either call matdetint + mathnfmod, or mathnf(,1) ]

> >   * I'm guessing maybe mathnf(b, 1) uses the modular hnf modulo the
> >   determinant.

Actually, no; mathnfmod does that.

> > If not, maybe you just need to add mutliples of rows until everything
> > is correctly normalized.

We do that, with one optimization too many which sometimes cancelled the
normalization step ( when the kernel is non trivial and we are "lucky":
a coefficient which we want to set to 0 is already 0 ).

It is fixed in both stable and unstable branches. I am attaching the
(trivial) patch.

Thanks for your report !

    K.B.
--
Karim Belabas                  Tel: (+33) (0)5 40 00 26 17
IMB, Universite Bordeaux 1     Fax: (+33) (0)5 40 00 69 50
351, cours de la Liberation    http://www.math.u-bordeaux.fr/~belabas/
F-33405 Talence (France)       http://pari.math.u-bordeaux.fr/  [PARI/GP]
```



---

Attachment

This patch needs to be applied to the pari.spkg


---

Comment by mabshoff created at 2008-02-18 18:41:05

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/pari-2.3.3.p0.spkg

contains the patch, adds support for 64 bit OSX. Builds fine on Linux and OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-18 18:41:05

Changing status from new to assigned.


---

Comment by was created at 2008-02-18 18:58:21

apply this patch to the sage hg repo; it adds a test to matrix/tests.py to ensure that the bug is (and stays) fixed.


---

Attachment

trac-2204.patch looks good to me. With it applied and the new pari.spkg doctests in `sage/matrix/tests.py` pass, so positive review (also from was for the spkg).

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-18 19:05:11

Resolution: fixed


---

Comment by mabshoff created at 2008-02-18 19:05:11

Merged in Sage 2.10.2.alpha1
