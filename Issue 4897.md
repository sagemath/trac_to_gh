# Issue 4897: integral_points() misses some points

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-12-31 10:42:46

Assignee: was

CC:  tnagel mardaus

Keywords: elliptic curve integral points

Francois Glineur reported to me that for the elliptic curve "20160bg2" not all integral points are found.

```
sage: E=EllipticCurve('20160bg2')
sage: [P[0] for P in E.integral_points()]
[-24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 186, 1476, 2034, 67246]
```

while Magma gives

```
> E:=EllipticCurve([0, 0, 0, -468, 2592]);
> Sort([P[1] : P in IntegralPoints(E)]);
[ -24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 168, 186, 381, 
1476, 2034, 67246 ]
```

so we are missing x=168 and x=381.

The curve has rank 2 and full 2-torsion.
The point Q=(168,2160) is the unique integral point its coset modulo torsion and I think that is why it is being missed.  In fact it seems incredible that this has not been seen before in all the testing which was done!

I therefore think that the function  integral_points_with_bounded_mw_coeffs() is at fault, and will fix it.




---

Comment by tnagel created at 2008-12-31 11:07:18

That's really incredible that we hadn't noticed this bug during our tests.
Please let me know if I can help with fixing this bug.

Greetings Tobias


---

Comment by cremona created at 2008-12-31 11:45:55

It was not that function in the end, but the point_preprocessing function.

```
Here's the problem (and it is not in the function I thought it was.

The curve 20160bg2 has two real components.  The generators in the database are
P1=(-18,72) and P2=(-14,0) which are both on the non-identity
component.   Preprocessing replaces those by P1+P2, 2*P1 (which
generate a subgroup H of index 2) and the LLL-reduction changes that
to use Q1=P1+P2=(36,-180) and Q2=-P1+P2=(1476,-56700).

The missing point (168,2160) is 2*P1+P2+T where T is the torsion point
(6,0).  This is not in H (even up to torsion).

A better way to do the preprocessing here is to take a torsion point
on the egg (e.g. T=(6,0)) and add that to the generators.  Similarly,
if there is a torsion point on the egg (necessarily of even order)
then we should add it to any of the generators which are on the egg.
Only if all torsion points are on the identity component should we do
what we currently do.
```


I have implemented this change and am currently testing.  Patch up later today!


---

Attachment

The patch is based on 3.2.2 + #4901 (which has a positive review but is not yet merged).

It does what was promised above, i.e. corrects the function  point_preprocessing().  A doctest is added with example from Francois Glineur.  In addition, I reran every single curve in the database (as reported to sage-nt) and have uploaded the revised files to my web page:  in about 1% of cases (over 8000 curves) there are more integral points than before.

The only file touched here is schemes/elliptic_curves/ell_rational_field.py, which is one of the ones which has already been sphinxified (see #4926) so this patch will need to be merged with that one at some point.


---

Comment by cremona created at 2009-01-04 17:46:18

Sorry, that should have said: based on 3.2.3.final + #4901.  Strictly, it does not depend on #4901, but it was in testing this patch extensively that the bug fixed in #4901 was found.


---

Comment by tnagel created at 2009-01-11 10:17:58

This patch looks pretty good!

The patch apllies correctly and all doctest pass.
Additional tests didn't show any defects -> positive review.

Greetings
Tobias


---

Comment by mabshoff created at 2009-01-12 00:57:17

This patch causes a doctest failure without the database installed:

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 4305:
    sage: [P[0] for P in EllipticCurve('20160bg2').integral_points()]
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_109[14]>", line 1, in <module>
        [P[Integer(0)] for P in EllipticCurve('20160bg2').integral_points()]###line 4305:
    sage: [P[0] for P in EllipticCurve('20160bg2').integral_points()]
      File "/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/constructor.py", line 124, in EllipticCurve
        return ell_rational_field.EllipticCurve_rational_field(x)
      File "/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 121, in __init__
        X = sage.databases.cremona.CremonaDatabase()[label]
      File "/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/databases/cremona.py", line 349, in __getitem__
        return self.elliptic_curve(N)
      File "/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/databases/cremona.py", line 487, in elliptic_curve
        raise RuntimeError, "No such elliptic curve in the database (note: use lower case letters!)"
    RuntimeError: No such elliptic curve in the database (note: use lower case letters!)
**********************************************************************
```


Thoughts?

Cheers,

Michael


---

Comment by cremona created at 2009-01-12 09:23:51

Oops, just change `E=EllipticCurve('20160bg2')` to 
`E=EllipticCurve([0,0,0,-468,2592])`
in that doctest.  It should suffice to edit the patch itself.


---

Comment by mabshoff created at 2009-01-12 11:06:38

John's patch with his suggested fix integrated.


---

Attachment

Replying to [comment:7 cremona]:
> Oops, just change `E=EllipticCurve('20160bg2')` to 
> `E=EllipticCurve([0,0,0,-468,2592])`
> in that doctest.  It should suffice to edit the patch itself.

Yep, I should have thought of that. trac_4897.2.patch does exactly that.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-12 11:08:08

Resolution: fixed


---

Comment by mabshoff created at 2009-01-12 11:08:08

Merged in Sage 3.3.alpha0


---

Comment by cremona created at 2009-01-12 11:25:53

Thanks for fixing that for me!  John
