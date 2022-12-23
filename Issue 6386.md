# Issue 6386: [with patch, needs review] Implement elliptic exponential

Issue created by migration from https://trac.sagemath.org/ticket/6386

Original creator: cremona

Original creation time: 2009-06-22 18:09:09

Assignee: was

CC:  robertwb

Keywords: elliptic curve

The elliptic exponential is the inverse to the elliptic log, i.e. it is the Weierstrass parametrization CC/L -> E(CC) for an elliptic curve.

The patch implements this as a member function of the PeriodLattice_ell class.  It works for all period lattices, real or not.  Currently it is accessible via a member function for elliptic curves over Q;  I'll make it work over number fields too, but ona separate ticket.  [At present it would already work for real embeddings;  shortly a rigorously justified elliptic log for non-real embeddings will also be ready.]

The hard work is done by pari's ellwp0() function, which was already wrapped, but to get the precision right that had to be slightly changed.


---

Attachment

Applies to 4.0.2


---

Comment by robertwb created at 2009-06-25 10:16:15

For the most part this looks good, and specifically I wasn't able to find any precision issues. 

* I think the elliptic exponential should actually return a point on E(C), not just a tuple (x,y)

* The docstring in elliptic exponential about to_Weierstrass is wrong. (Maybe it could be to_curve, default True to give something on E(C), false returning the raw `(wp(z), wp'(z))`.

* The `antilogarithm` shouldn't simply discard the imaginary part: 


```
sage: E = EllipticCurve('389a')
sage: z0 = CC(1.76776906963, 0.303020775118)
sage: E.elliptic_exponential(z0)
(1.00012725137998 + 1.00002216580174*I,
 0.000229106700941339 + 2.00010160734906*I)
sage: E.antilogarithm(z0, 10)
(1 : 0 : 1)
```



---

Comment by cremona created at 2009-06-25 12:09:53

Replying to [comment:2 robertwb]:
> For the most part this looks good, and specifically I wasn't able to find any precision issues. 
> 
> * I think the elliptic exponential should actually return a point on E(C), not just a tuple (x,y)

OK, I'll do that.  I literally had not tried that!

> 
> * The docstring in elliptic exponential about to_Weierstrass is wrong. (Maybe it could be to_curve, default True to give something on E(C), false returning the raw `(wp(z), wp'(z))`.

I'll check that out.

> 
> * The `antilogarithm` shouldn't simply discard the imaginary part: 
> 
> {{{
> sage: E = EllipticCurve('389a')
> sage: z0 = CC(1.76776906963, 0.303020775118)
> sage: E.elliptic_exponential(z0)
> (1.00012725137998 + 1.00002216580174*I,
>  0.000229106700941339 + 2.00010160734906*I)
> sage: E.antilogarithm(z0, 10)
> (1 : 0 : 1)
> }}}

My reasoning is that you only use this function when you have reason to believe that the result is actually a rational point, so in particular it is real.  Can I just clarify the docstring?  Note that this function is never going to be able to give a provable result, at best it will retrun a rational point whose elliptic log is close to the input value, but it is still a useful thing to have.


---

Comment by cremona created at 2009-06-25 16:07:49

Apply after previous


---

Attachment

I have done the first thing requested, delivering a point in E(CC) or E(RR) in cases where it is possible to tell that the point is real.  I had to use "check=False" since the returned x,y do not necessarily satisfy the equation to the given precision.  I'm not sure what the problem was in the second point, but I changed the name of the parameter to "to_curve" and fixed a typo in the docstring (it said True instead of False, or possibly the other way round, at one point -- this might have caused the confusion).

I have left the third point, with the explanation given above!


---

Comment by robertwb created at 2009-06-26 04:47:21

Looks good. Using check=False is fine, there's really no way around it. 

I understand your point, but I would be more comfortable if for antilogarithm you at least bounded the magnitude of the imaginary part as a function of the error in the real part. Also, it has undesirable behavior when x or y (or both) are supposed to be 0, but are off by machine epsilon. Neither of these are regressions to what was there before, and I like the doctests, so I'm not stuck on this. 

Positive review pending acceptance of the tiny patch above.


---

Comment by robertwb created at 2009-06-26 05:02:24

Wait, I take that back. There's still some issues: 

* `E.elliptic_exponential(z)` gives a tuple while `E.period_lattice().elliptic_exponential()` gives a point. They should both at least be consistent, and I think the latter is better. 

* When you use check=False, you have to give projective coordinates because it doesn't check to add the 1 at the end.


---

Comment by robertwb created at 2009-06-26 05:52:40

apply after other two


---

Attachment

OK, I resolved the issues above, and while I was at it modified antilogarithm to look at the imaginary parts. Now I need a review from you.


---

Comment by cremona created at 2009-06-26 08:41:45

I agree with all the changes you made -- thanks for all the attention to detail!  the sequence of 3 patches applies fine to 4.0.2 and relevant tests pass on 32 and 64 bit, so I'll give this a positive review.  [Note to release manager: Robert positively reviewed my two patches modulo his and I approve of his!]


---

Comment by boothby created at 2009-06-27 02:15:50

Doctest failure when applied to 4.1.alpha1 -- this one looks pretty easy.


```
sage -t -long devel/sage/sage/symbolic/pynac.pyx
**********************************************************************
File "/space/boothby/sage-4.1.alpha1/devel/sage-main/sage/symbolic/pynac.pyx", line 850:
    sage: py_imag(RR(1))
Expected:
    0
Got:
    0.000000000000000
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_22
***Test Failed*** 1 failures.
For whitespace errors, see the file /space/boothby/sage-4.1.alpha1/tmp/.doctest_pynac.py
         [2.1 s]
```



---

Comment by robertwb created at 2009-06-27 02:56:24

Hmm... actually I didn't know that imag(z) worked before. Perhaps an exact zero is better to return here after all...


---

Comment by cremona created at 2009-06-27 14:20:24

Robert, I think this was caused by something you added?  Namely, that x.imag() when x is a RealField element is now not an exact zero but 0 in that realfield.  I'm not at all sure what's best here -- perhaps consult on sage-devel?


---

Comment by robertwb created at 2009-06-27 17:15:37

Yep, this was due to the method I added. I'm changing it back to what it used to be.


---

Attachment

apply after all others


---

Comment by cremona created at 2009-06-28 11:26:26

I applied all four patches successfully to 4.1.alpha2, and all tests pass (even with testall I only got the same failures as with a vanilla 4.1.alpha2).  Let's go!


---

Comment by rlm created at 2009-07-03 18:14:43

Resolution: fixed
