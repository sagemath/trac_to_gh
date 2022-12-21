# Issue 4805: S_integral points failure (possible p-adic precision problem)

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-12-15 16:59:44

Assignee: was

CC:  tnagel mardaus roed

Keywords: elliptic curve

After #4741 we still have this problem:

```
sage: EllipticCurve("7690e1").S_integral_points([13,2])
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (178, 0))

---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/john/<ipython console> in <module>()

/home/john/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in S_integral_points(self, S, mw_base, both_signs, verbose, proof)
   5062             while not p_prec_ok:
   5063                 try:
-> 5064                     mw_base_p_log.append([mp_temp*(pts.padic_elliptic_logarithm(p,precision=p_prec)) for pts in mw_base])
   5065                     p_prec_ok=True
   5066                 except (PrecisionError, ZeroDivisionError, TypeError):

/home/john/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.pyc in padic_elliptic_logarithm(self, p, precision)
   1399         t = -x/y
   1400         v = t.valuation()
-> 1401         phi = Ep.formal().log(prec=1+precision//v)
   1402         return phi(t)/f
   1403 

/home/john/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/formal_group.pyc in log(self, prec)
    348            -- David Harvey (2006-09-10): rewrote to use differential
    349         """
--> 350         return self.differential(prec-1).integral().add_bigoh(prec)
    351 
    352     def inverse(self, prec=20):

/home/john/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/sage/rings/power_series_ring_element.so in sage.rings.power_series_ring_element.PowerSeries.add_bigoh (sage/rings/power_series_ring_element.c:5413)()

/home/john/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/sage/rings/power_series_ring.pyc in __call__(self, f, prec, check)
    324             v = sage_eval(f.Eltseq())
    325             return self(v) * (self.gen(0)**f.Valuation())
--> 326         return self.__power_series_class(self, f, prec, check=check)
    327         
    328     def construction(self):

/home/john/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/sage/rings/power_series_poly.so in sage.rings.power_series_poly.PowerSeries_poly.__init__ (sage/rings/power_series_poly.c:2160)()

/home/john/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.truncate (sage/rings/polynomial/polynomial_element.c:27152)()

/home/john/sage-3.2.2.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.pyc in __getslice__(self, i, j)
    372             j = len(self._relprecs) + j
    373             if j < 0:
--> 374                 raise IndexError, "list index out of range"
    375         if i >= j:
    376             return Polynomial_padic_capped_relative_dense(self.parent(), [])

IndexError: list index out of range
```




---

Attachment


---

Comment by cremona created at 2009-01-18 17:29:34

I worked on this in Dec 08 and while the result is not perfect it does fix the immediate problems.  Mainly, finding the p-adic elliptic log of a point (on a curve over QQ) to specified precision may require the working precision to be increased.  [Simple example:  if the valuation of the discriminant is N then don't try changing the base field to Qp(N-1) as the equation will look singular.]

The fixes in the patch do two things: in a few places where it's clear that the precision must be at least something, then increase it to that thing.  Otherwise there is a lot of try/expect wrapping with the precision being doubled if necessary, both in the log function itself and in the (currently only) function which calls it, namely S_integral_points().

This code has been tested by running S_integral_points() on lots of curves in the database with a variety of sets S.

To help improve the p-adic log function, a new function for points has_good_reduction(self,P) has been defined.

The patch (trac_4805.patch) is based on 3.2.3.


---

Comment by roed created at 2009-01-24 12:35:35

file: ell_point.py
function: has_good_reduction
the docstring has_good_reduction allows P = None, but the code doesn't (and it's not doctested).

        if K is rings.QQ: 
            pi = P 
        else:
            pi = K.uniformizer(P)
occurs twice (1063 and 1077)


function: padic_elliptic_logarithm
docstring should change to reflect the new default precision 
The explanation for the precision should be clarified: it's not the precision of the result, rather something slightly less.  Even better: change the code so that the answer returned actually has the given precision.  You should also specify whether this precision is relative or absolute (it's probably absolute).  Using "absprec = 20" in the function arguments would clarify this.
Once the definition of precision is clarified, I think the ValueErrors be able to be eliminated (if you're trying to return an answer of a given precision, just increase the precision whenever you would otherwise hit a ValueError.

file: ell_rational_field.py
function: S_integral_points
The NOTE should be modified to take this patch into account.
line 5103: You shouldn't have bare except blocks.  Figure out what kinds of exceptions you want to catch, and list them explicitly.


---

Comment by cremona created at 2009-01-24 17:41:23

All fair comments, what I provided was a deliberate compromise so that the application I wanted (S-integral points) worked instead of crashing, while not having time to do a proper and thorough job on p-adic elliptic logs.  I still don't and will not for another two months probably, so unless someone else wants to do the work required by the reviewer we'll keep shipping Sage with code which crashes.


---

Comment by mabshoff created at 2009-01-24 17:49:07

Given John's last comment I would like to merge this now and open a followup ticket to deal with the problem later. Fixing the crash now with somewhat suboptimal code is better than shipping broken code.

Roed: Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 06:09:06

John,

can you make the easy changes that Roed requested and then open another ticket for the heavy lifting he wants implemented? I am willing to give this a positive review then and take the heat in case things go wrong :)

Cheers,

Michael


---

Comment by cremona created at 2009-02-02 18:07:00

Replying to [comment:5 mabshoff]:
> John,
> 
> can you make the easy changes that Roed requested and then open another ticket for the heavy lifting he wants implemented? I am willing to give this a positive review then and take the heat in case things go wrong :)

OK, I'll do that as soon as I can.  Then we might want to ping one of our p-adic experts to do a better job.


> 
> Cheers,
> 
> Michael


---

Attachment

Apply after previous


---

Comment by cremona created at 2009-02-02 21:20:39

The second patch should be applied after the first, which still applies ok to 3.3.alpha3 (with some fuzz).  It does the following:

   1. In has_good_reduction() I added the originally intended behaviour when P=None to match the docstring, and added two doctests (one over Q, one over a number field) which test this.  In this function I also deleted the duplicated lines of code.

   2. In padic_elliptic_logarithm() I changed the parameter name from precision to absprec, corrected the docstring, and added a TODO note admitting the function's imperfections.

   3. In S_integral_points() I removed the now redundant NOTE and fixed the bare "except".

I think that's it and hope that RoeD will allow this through, with the admission that a new version of padic_elliptic_logarithm() which handles precision better would certainly be desirable.


---

Comment by cremona created at 2009-02-04 22:47:59

roed, are you there?


---

Comment by was created at 2009-02-06 13:53:53

Hi,

It looks to me like John addressed all of David's comments.  He didn't make the output precision specified by prec, which would have required changing the algorithm, and that's fine by me (and in fact makes sense to me, given that it is clearly documented).

Assuming this passes all tests, I'm fine with it getting a positive review.


---

Comment by mabshoff created at 2009-02-06 22:05:03

Replying to [comment:9 was]:

> Assuming this passes all tests, I'm fine with it getting a positive review. 

Doctests on sage.math do pass with both patches applied, so I am changing this to a positive review as indicated by William.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 22:05:30

Resolution: fixed


---

Comment by mabshoff created at 2009-02-06 22:05:30

Merged both patches in Sage 3.3.alpha6.

Cheers,

Michael
