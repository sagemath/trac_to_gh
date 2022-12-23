# Issue 793: wrapper for hyperelliptic curve zeta functions

Issue created by migration from https://trac.sagemath.org/ticket/793

Original creator: dmharvey

Original creation time: 2007-10-02 19:32:58

Assignee: was

Even though we have functionality for computing zeta functions of hyperelliptic curves, the `HyperellipticCurve` curve object itself doesn't yet have a method like `zeta_function`. This shouldn't be hard to do (over prime fields at least), using code in `sage/schemes/hyperelliptic_curves/frobenius.pyx` and `sage/schemes/elliptic_curves/monsky_washnitzer.py`.



---

Comment by dmharvey created at 2007-10-03 16:49:36

see also #811


---

Comment by kedlaya created at 2008-11-25 19:24:09

See also #965. I've had several requests for this functionality, so it would be great if several of us could spend some time getting this ready for prime time.


---

Attachment


---

Comment by dmharvey created at 2009-03-17 19:18:14

Very basic wrapper attached. This is code by Nick Alexander and myself. Sample:


```
sage: R.<x> = PolynomialRing(GF(10007))
sage: H = HyperellipticCurve(x^7 + x + 1)
sage: time H.frobenius_polynomial()
CPU times: user 1.62 s, sys: 0.01 s, total: 1.63 s
Wall time: 1.63 s
x^6 + 4*x^5 + 21884*x^4 - 99088*x^3 + 218993188*x^2 + 400560196*x + 100210147034
```



---

Comment by GeorgSWeber created at 2009-03-31 18:04:22

Looks good to me.

Tested against Sage-3.4.1.alpha0.


---

Comment by mabshoff created at 2009-03-31 21:41:43

Several of the internal methods need doctests - the coverage of this patch is not even close to 100%.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 22:54:46

But at least the doctests that are there pass for me in my 3.4.1.rc0 merge tree.

Cheers,

Michael


---

Comment by dmharvey created at 2009-04-01 06:07:22

Does this mean that if I combine all the functions into one megalithic unreadable function, it would pass review without writing any more doctests?


---

Comment by mabshoff created at 2009-04-01 06:18:23

Replying to [comment:9 dmharvey]:
> Does this mean that if I combine all the functions into one megalithic unreadable function, it would pass review without writing any more doctests?

Technically yes, but I would not consider this the cleanest solution :)

Cheers,

Michael


---

Comment by dmharvey created at 2009-04-01 08:10:07

I consider them to be tested indirectly by the main function.


---

Comment by was created at 2009-04-01 12:50:33

> I consider them to be tested indirectly by the main function. 

So are you refusing to doctest your functions and expect this patch to sit in limbo into either somebody else does it for you or the policy of the sage project for the last two years changes?

> Does this mean that if I combine all the functions into one megalithic 
> unreadable  function, it would pass review without writing any more doctests? 

Not from me. 

 -- William


---

Comment by dmharvey created at 2009-04-01 13:34:36

I just noticed that the code does not take advantage of the symmetry of the zeta function and so uses a p-adic precision about twice as high as necessary. I withdraw the patch.


---

Comment by GeorgSWeber created at 2009-04-01 18:35:26

Unfortunate.

The code was excellently commented, in fact the comments of the internal functions were so good, it just slipped by me that the mandatory doctesting lines were missing. (Which IMHO are trivial to add in this patch.)

And if it is difficult to find "special" doctests for internal functions, one always has the possibility to do (another slightly modified instance of) the "outer" computation as a test and write "#implicit doctest" as comment. This serves the intended purpose (and I strongly guess neither Michael, nor William, would object). All in all, another to-be-better-documented issue.

With regard to the p-adic precision, I'd say "functionality first and optimizations later" (the patch as-is is mathematically correct :-) ), but that's my own personal opinion.

Cheers,
gsw


---

Attachment

Let's try again. New patch should be applied on top of the old.

Georg: regarding the precision, I am preparing for a talk on Friday, and the slowdown caused by the p-adic precision overestimates actually made a big difference to the presentation.


---

Comment by GeorgSWeber created at 2009-04-01 21:03:28

SCORE devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py: 100% (6 of 6)

Looks even better to me.

And good luck for your presentation!

Cheers, gsw


---

Comment by mabshoff created at 2009-04-01 23:54:00

Resolution: fixed


---

Comment by mabshoff created at 2009-04-01 23:54:00

Merged both patches in Sage 3.4.1.rc0.

Cheers,

Michael
