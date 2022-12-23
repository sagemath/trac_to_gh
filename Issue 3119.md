# Issue 3119: elliptic curves -- implement gens function for non-integral models

Issue created by migration from https://trac.sagemath.org/ticket/3119

Original creator: was

Original creation time: 2008-05-07 04:23:04

Assignee: was

The following should now be trivial to support given all the cool transformations of models code that John Cremona and Robert Bradshaw added to Sage.   Just transform the curve to minimal form, find the isomorphism explicitly, then transform the answers back. 

```
sage: E = EllipticCurve([-3/8,-2/3])
sage: E.gens()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/Users/was/edu/2007-2008/sage/homework/5/<ipython console> in <module>()

/Users/was/build/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in gens(self, verbose, rank1_search, algorithm, only_use_mwrank, proof)
   1349         # end if (not_use_mwrank)
   1350         if not self.is_integral():
-> 1351             raise NotImplementedError, "gens via mwrank only implemented for curves with integer coefficients."
   1352         if algorithm == "mwrank_lib":
   1353             misc.verbose("Calling mwrank C++ library.")

<type 'exceptions.NotImplementedError'>: gens via mwrank only implemented for curves with integer coefficients.
```


See how trivial this will now be to implement:

```
sage: F = E.minimal_model()
sage: phi = F.isomorphism_to(E)
sage: [phi(z) for z in F.gens()]
[(10/9 : 29/54 : 1)]
```


What could be easier?



---

Comment by cremona created at 2008-05-26 13:39:49

In fact it is even easier than that!  For about 6 months mwrank has had the ability to deal with non-integral and non-minimal models.  In this case simply commenting out lines 1350 and 1351 in ell_rational_field.py produces this:

```
sage: E = EllipticCurve([-3/8,-2/3])
sage: E.gens()
[(10/9 : 29/54 : 1)]
```


Patch coming up.


---

Attachment

The attached patch fixes the (spurious) error caused by an unnecessary testing for a case (non-integral curves) which are in fact well handled by mwrank.  At the same time I deleted the first TODO item from gens() since non-minimal models are similarly catered for.

Two new doctests illustrate the successful running of gens() on non-integral and non-minimal curves.

One small other thing:  when gens() calls mwrank it passes the command-line parameter "-p 100" which helps curves with large coefficients and 2-torsion and is otherwise harmless.  This is pending a more intelligent handling of mwrank options in gens() (which is nontrivial since gens() needs to parse the output from mwrank and this is seriously affected by what parameters the user passes!).

In fact it would be much better to avoid the mwrank console at all for gens() and just use the library.  This is in progress (see #1949)


---

Comment by cremona created at 2008-05-26 17:48:33

Apply after first patch


---

Attachment

Another patch (to be applied after previous) fixing two other things:

First:  I finally got rid of the terrible behaviour of the mwrank_EllipticCurve constructor with non-integral input.  It now throws an error.  [Although mwrank can take non-integral elliptic curves in some circumstances, this will require more work.]

Second:  There was a bug in the gens() function for 

Before:

```
sage: E=EllipticCurve('389a1').change_weierstrass_model([1/20,0,0,0])
sage: E.gens(algorithm="mwrank_lib")
[(0 : 1 : 0), (0 : 1 : 0)]
```

which is not just wrong but very wrong!

After:

```
sage: E=EllipticCurve('389a1').change_weierstrass_model([1/20,0,0,0])
sage: E.gens(algorithm='mwrank_lib')
[(-400 : 8000 : 1), (0 : -8000 : 1)]
```



---

Comment by cremona created at 2008-05-26 20:55:59

Comment:  The one-line change to wrap.cc which (really) fixes the bug exemplified above is actually unnecessary in the sense that there was an underlying bug in eclib which should be fixed instead.  The currect code still works, however.

Technical detail:  eclib provides support for non-minimal and non-integral curves via a slight subterfuge whereby the curve actually worked is integral and minimal, and a scaling factor is stored.   mwrank itself (and all other executables in eclib) manage this fine: they construct the two_descent object using a vector of 5 rationals rather than a curvedata type.  The constructor from a curvedata type is still there and is the one used by Sage -- but it forgot to set the scale factor to 1.  This messes up the points returned by member function getbasis().   The currect fix is to have sage call getpbasis() instead (which does not do this scaling) which is OK if and only if the model was integral to start with.  Which it is, currently, since we do not yet have a constructor for mwrank_EllipticCurve which takes non-integral rationals.

I'll be fixing eclib in due course.


---

Attachment

Extra patch added to fix the same bug in a better way.  Now wrap.cc should not need to be changed -- just checking...


---

Attachment

Latest patch trac-3119a.patch undoes one change in the original patch (the one-line change to wrap.cc) since the same thing is fixed better by patching eclib.  I have tested this, so I hope it is clear.


---

Comment by craigcitro created at 2008-06-15 21:42:09

Changing keywords from "" to "editor_wstein".


---

Comment by was created at 2008-06-16 00:34:05

this is the *fourth* patch to the sage main repo that has to be applied


---

Attachment

REFEREE REPORT:

Excellent.  However there are several doctest failures after applying the patches:

```
D-69-91-137-77:~ was$ sage -t d/sage/sage/schemes/elliptic_curves/ell_rational_field.pysage -t  d/sage/sage/schemes/elliptic_curves/ell_rational_field.py
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 145:
    sage: E.gens()         # causes actual rank to be computed
Expected:
    [(0 : -1 : 1)]
Got:
    [(0 : 0 : 1)]
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 147:
    sage: E.rank()         # the correct rank
Expected:
    1
Got:
    99
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 1413:
    sage: E.gens()
Expected:
    [(0 : -1 : 1)]
Got:
    [(0 : 0 : 1)]
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 1538:
    sage: Q=5*P; Q
Expected:
    (1/4 : -3/8 : 1)
Got:
    (1/4 : -5/8 : 1)
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 1540:
    sage: E.saturation([Q])
Expected:
    ([(0 : -1 : 1)], '5', 0.0511114075779915)
Got:
    ([(0 : 0 : 1)], '5', 0.0511114075779915)
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 252:
    sage: E.gens()
Expected:
    [(-2 : 3 : 1), (-7/4 : 25/8 : 1), (1 : -1 : 1)]
Got:
    [(-2 : 3 : 1), (-1 : 3 : 1), (0 : 2 : 1)]
**********************************************************************
5 items had failures:
   2 of   6 in __main__.example_2
   1 of   4 in __main__.example_32
   2 of   5 in __main__.example_35
   1 of   6 in __main__.example_62
   1 of   8 in __main__.example_7
***Test Failed*** 7 failures.
For whitespace errors, see the file /Users/was/s/tmp/.doctest_ell_rational_field.py
	 [47.8 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  d/sage/sage/schemes/elliptic_curves/ell_rational_field.py
Total time for all tests: 47.8 seconds
```


}}}


---

Comment by cremona created at 2008-06-16 13:23:41

William -- my patches to sort this one out included a (tiny) patch to eclib source code which I posted here.  Without that patch the issue is *not* fixed.  Can you confirm whether or not you were testing with a patched eclib?  John


---

Comment by was created at 2008-06-19 23:03:51

Yes, I had that fix applied.  Does everything *definitely* work for you with that patch applied?


---

Comment by cremona created at 2008-06-20 20:33:29

I applied all 4 patches to a fresh install of 3.0.3.rc0, which I believe is the same as 3.0.3.  I did not apply the eclib patch which I assumed had been already applied to 3.0.3 (if Michael reads this could he confirm?).  And there were no problems:

```
john@ubuntu%sage -t /home/john/sage-3.0.3.rc0/devel/sage-3119/sage/schemes/elliptic_curves/ell_rational_field.py 
sage -t  devel/sage-3119/sage/schemes/elliptic_curves/ell_rational_field.py
	 [112.5 s]
}}} 
So this is rather mysterious.

Incidentally some of those tests are taking a bit long.


---

Comment by cremona created at 2008-06-22 16:58:37

Double check:
    * New build of 3.0.3
    * new clone set up
    * Apply the four patches attached excluding the eclib one
    * Rebuild eclib after applying the eclib patch
Now all doctests pass in ell_rational_field and so does the one above which definitely does not work without eclib being correctly patched.

Hence I humbly ask that the reviewer re-checks!


---

Comment by cremona created at 2008-06-23 21:14:43

The newly patched eclib at  http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20080310.p3.spkg contains several small fixes *including* the eclib.patch attached to this ticket already.


---

Comment by mabshoff created at 2008-06-25 08:28:57

I have split of the spkg to #3509.

Cheers,

Michael


---

Comment by cremona created at 2008-06-28 15:59:33

*New* simpler patch replacing all previous ones for this ticket


---

Attachment

I have combined and simplified the confusion of earlier patches, so now only *one* need to be applied: sage-3119-new.patch.  This is based in version 3.0.4.alpha0.  Note that it requires  eclib-20080310.p3 which is not in 3.0.4.alpha0 but is in alpha1 (the one which did not build) so reviewers should test with 3.0.4.alpha2 (or later). If run with the older eclib, the doctests in ell_rational_field.py still pass but take about 4 times as long (proving that the patch to eclib is not quite as trivial as it appears).


---

Comment by cremona created at 2008-08-09 08:26:49

I have checked that this patch still applies cleanly and passes tests with 3.1.alpha0.

It is a *very simple* patch -- the serious change happened in eclib and has already been merged.

Please will someone help put this to bed!


---

Comment by ncalexan created at 2008-08-10 21:01:23

This works for me with 3.0.6.  The sage library patch looks good; I haven't checked the already merged changes to eclib.

Apply!


---

Comment by mabshoff created at 2008-08-11 01:45:26

Patch looks good to me, but there is a minimal doctest issue related to numerical noise that I fixed:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha1/tmp/ell_rational_field.py", line 1475:
    sage: EllipticCurve([0, 0, 1, -79, 342]).regulator(proof=False)  # long time (seconds)
Expected:
    14.7905275701310
Got:
    14.7905275701311
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-08-11 02:05:02

Merged in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-11 02:05:02

Resolution: fixed
