# Issue 3674: Implement integral point finding for elliptic curves over Q

Issue created by migration from https://trac.sagemath.org/ticket/3674

Original creator: cremona

Original creation time: 2008-07-18 17:19:43

Assignee: was

CC:  mardaus@students.uni-mainz.de

The problem of enumerating integral and S-integral points on elliptic curves over Q and over number fields is one which it would be wonderful to have implemented in Sage.  Magma has this over Q (for general S), but no package has the general case (except possibly in code for Simath written by E.Hermann).

I suggested this as a good problem for a Masters student to work on after the Sage Days in Bristol in November 2007.   After that, Tobias Nagel & Michael Mardaus (students at Mainz) started to work on it.  At my suggestion they started with the easiest case: integral points over Q (i.e. S=\emptyset).  They have just sent me this, and I am about to start testing it:

Dear John,

we just finished our work (or at least part one of it).
As you explained to us we put our code into ell_rational_field.py. So a new function 'integral_points(self, mw_base='auto', tors_points='auto')' is provided after a rebuild of sage.

Our testcases are also attached to the mail. If you load self_test.sage you have a funtion called 'test_integral_points'. Call it by test_integral_points('all') to test 12 testcases, which mean several curves and changes in the generators of the Mordell-Weil base. (As an overview we made an excel-sheet with the computation time, but it is only one run and not statistically correct evaluated ;) )
We are not sure if all the functionality should be written in ell_rational_field.py as we did or if it should be swaped out to somewhere.

We hope you are satisfied with our work.

Greetings
Tobias and Michael

I will attach a patch file created from the attachments they sent me shortly.

John Cremona



---

Comment by cremona created at 2008-07-18 19:12:37

Not a patch (yet)


---

Attachment

In 3.0.5 I replaced sage/schemes/elliptic_curves/ell_rational_field.py with the file emailed to me
and it built fine.

Comments:
    1. The docstring says that parameter tors_points should be either 'auto' or a list of all the torsion points; but 'auto' causes tors_points to be assigned to generators for the torsion.  So the docstring should change "all torsion points" to "generators for the torsion subgroup".
    2. The output is a set.  I think it should be a sorted list.  (Sorting is important to give consistency across platforms, etc.)
    3. Why this?

```
        if (r == 0) and (len_tors == 0):
            raise RuntimeError, 'Both base points and torsions points are not specified'
```

If the curve has trivial MW group then this is what you would expect, so why not just return the empty list?
    4. Your way of checking that the supplied points lie on the curve (the code with "trash") looks weird to me.  Why not just check that sel==P.curve() for each point P?  And this need only be done when the user has supplied the points.
    5. is_int():  there are more Sage-like ways of doing this, such as try: x==ZZ(x).
    
That's all I'll write for now.  You have done some great work here, but what I think I will do is rewrite it a bit myself and post a new patch based on that.
 

```
            if j == 0:
```

should be if self.j_invariant()==0 ?  j is undefined here.  Also, since height_of_curve() might be useful in other places I would make this a separate function for the class.


---

Comment by cremona created at 2008-07-19 13:29:06

Dear John,

thanks to your answer and your advise.
I'm sorry to write you an email instead of replying to the trac ticket (but I'm not sure how to do that).
I made some comments on your mail below:

>Betreff: Re: [SAGE] #3674: Implement integral point finding for elliptic curves over Q
>
>#3674: Implement integral point finding for elliptic curves over Q
>---------------------------+------------------------------------------------
 >Reporter:  cremona        |        Owner:  was
 >    Type:  enhancement    |       Status:  new
> Priority:  major          |    Milestone:
>Component:  number theory  |   Resolution:
> Keywords:                 |
>---------------------------+------------------------------------------------
>Comment (by cremona):
>
 >In 3.0.5 I replaced sage/schemes/elliptic_curves/ell_rational_field.py
 >with the file emailed to me
 >and it built fine.
>
> Comments:
>     1. The docstring says that parameter tors_points should be either
> 'auto' or a list of all the torsion points; but 'auto' causes tors_points
> to be assigned to generators for the torsion.  So the docstring should
> change "all torsion points" to "generators for the torsion subgroup".

your right that was a bit imprecise of us

>     2. The output is a set.  I think it should be a sorted list.  (Sorting
> is important to give consistency across platforms, etc.)

we didn't thought of the problem that a set might make across platforms

>     3. Why this?
> {{{
>         if (r == 0) and (len_tors == 0):
>             raise RuntimeError, 'Both base points and torsions points are
> not specified'
> }}}
> If the curve has trivial MW group then this is what you would expect, so
> why not just return the empty list?

yes, there is a mistake. We thought this would be impossible so we raised an Error

>     4. Your way of checking that the supplied points lie on the curve (the
> code with "trash") looks weird to me.  Why not just check that
> sel==P.curve() for each point P?  And this need only be done when the user
> has supplied the points.

The code with trash is more or less the same, because the function .point() raises an Error
if the specified point is not in the curve. We haven't looked at the function .curve()

>     5. is_int():  there are more Sage-like ways of doing this, such as
> try: x==ZZ(x).

We also thought that there must be better ways of checking the type but because we
weren't so familiar (its becoming better and better but sage is so large that it takes some
time we get deep into it)

> That's all I'll write for now.  You have done some great work here, but
> what I think I will do is rewrite it a bit myself and post a new patch
> based on that.

Thanks. So we shouldn't fix what you commented on here ?

 >{{{
 >            if j == 0:
 >}}}
> should be if self.j_invariant()==0 ?  j is undefined here.

At runtime j is defined so it seems no problem to us

>  Also, since height_of_curve() might be useful in other places I would make this a
> separate function for the class.

If you're going do this you need self.j_invariant() that's right.

I would also suggest to make complex_elliptic_logarithm() a seperate function in the class
of Rational Points on Elliptic curves or isn't it a useful functionality?
If so I can make the necessary additional changes.


Now in the following weeks, Michael and I will go on with the problem of S-integral point
finding.

Best wishes
Tobias


---

Comment by cremona created at 2008-07-19 13:31:44

Dear Tobias (and Michael)

For trac:  write to Michael Abshoff (see sage-devel emails) and ask
him for an account.  Your username can be anything to easily identify
you, and the password can be anything insecure -- it is just to avoid
spam.

I have started editing your code, and I think it would be most
efficient if I did some more work on that before handing it back to
you.  If you don't like that, tell me right away as I can easily stop:
all I have done so far is to separate out the height of a curve
(which will be useful elsewhere.  Elliptic log will certainly be
useful elsewhere.

Other comments about your internal functions:

    * `extract_realroots()`:  you should be able to give the `roots()` function
a field and it will only give roots in that field.  then this would
bbe unnecessary.

   * `in_egg()`:  this should be an external function, and should be replaced
by something exact (discrete):  see the very last section of
http://www.warwick.ac.uk/staff/J.E.Cremona/papers/component.pdf.

   * `search_points()`:  should use the function `elliptic_curve.list_x()` to
give one or all points with a given x-coordinate.  Which would make it
much shorter:  for example, to list all points with integral x between
10 and 50 this works:

```
sage: sum([E.lift_x(x,all=True) for x in range(10,50)],[])
[(11 : 35 : 1),
 (11 : -36 : 1),
 (14 : 51 : 1),
 (14 : -52 : 1),
 (21 : 95 : 1),
 (21 : -96 : 1),
 (37 : 224 : 1),
 (37 : -225 : 1)]
```


That's enough for now.  I will paste this into the trac ticket too.

It might be a good idea to wait until this function is finished and
reviewed before working too seriously on the S-integral case.  I think
it would be easier to implement that once you know the final form of
the case you have already done.  But anyway you can certainly start to
work on that while I tidy up what you have done so far.

John


---

Attachment

Based on 3.0.4


---

Comment by cremona created at 2008-07-20 07:16:23

The patch sage-trac3674a.patch is a first version after some working by me.  It needs more work still (e.g. `elliptic_logarithm()` needs doctests) but I cannot spend more time on it for a while and I wanted Tobias and Michael to see what I had done so far.


---

Comment by tnagel created at 2008-07-21 10:07:25

Replying to [comment:4 cremona]:
> The patch sage-trac3674a.patch is a first version after some working by me.  It needs more work still (e.g. `elliptic_logarithm()` needs doctests) but I cannot spend more time on it for a while and I wanted Tobias and Michael to see what I had done so far.

Dear John,

it is very informative to look at the changes you made. We hadn't such a deep knowledge how to work with sage (e.g. computing the roots).
To make a little contribution I have written the doctests for the elliptic_logarithm()

```
EXAMPLES:
    sage: E=EllipticCurve('37a')
    sage: [E.lift_x(x).elliptic_logarithm() for x in range(-1,2)]
    [0.204680500375771 + 1.22569469099340*I, 0.929592715285396 + 1.22569469099340*I, 1.85918543057079]
         
    sage: [E.lift_x(x).elliptic_logarithm(precision=100) for x in range(-1,2)]
    [0.20468050037577260661641194608 + 1.2256946909933950304271124159*I, 0.92959271528539567440519934446 + 1.2256946909933950304271124159*I, 1.8591854305707913488103986889]
```


Greetings
Tobias


---

Comment by cremona created at 2008-07-21 11:00:44

Replaces earlier patch -- applies to 3.0.4


---

Attachment

The patch sage-trac3674.patch supercedes the earlier one and should be applied to 3.0.4 (or, I hope 3.0.5, 3.0.6).

From the code supplied by Tobias and Michael I moved elliptic_logarithm() and on_identity_component() to ell_points.py since they are more generally useful, and included doctests for these.  I edited the code for integral_points quite a lot without changing the algorithm, mainly better handling of floating point numbers and use of some Sage functions rather than reinvent wheels in a few places.

One change to functionality is that by default only one of each pair P, -P is output;  this can be changed using both_signs=True.

The elliptic logarithm doctests have been checked against pari's ellpointtoz() function, and the integral points on 5077a1 with Magma (which revealed a Magma bug, duly reported).


---

Comment by cremona created at 2008-07-21 13:54:47

The second patch sage-trac3674b.patch adds a function antilogarithm() for elliptic curves over Q, which is an inverse to elliptic_logarithm().  A `ValueError` is raised if the input complex number z does not lead to a rational point (which can happen for precision reasons, or if z is not the elliptic log of a rational point).

Note 1:  elliptic_logarithm() is a method of the class `EllipticCurvePoint_field` -- though only implemented for subfields of RR, such as CC.  Whereas antilogarithm() is a method of class `EllipticCurve_rational_field`.  It might be possible to arrange this differently.

Note 2:  antilogarithm() just calls ellztopoint() from the pari library.  But the way that function is wrapped does not allow the passing of a precision parameter, which it should.


---

Attachment

For CC read QQ in the above.


---

Attachment

fix so e.integral_points() works when e.rank() >= 1.


---

Comment by was created at 2008-07-29 20:46:26

REFEREE REPORT:

This is a wonderful contribution to Sage!    

Since we're writing professional quality code here, there are several quality and consistency issues that need to be addressed.  Please see below. 

1. CODE:

```
+        """The rational point (if any) associated to this complex number
+           (inverse of elliptic logarithm)
```

should be

```
         """
         The rational point (if any) associated to this complex number
         (inverse of elliptic logarithm).
```

Notice the period at the end of the sentence and not starting right after """ (a Sage convention). 

 * In `def antilogarithm(self, z, prec=53):` you don't document the prec input parameter.

 * The warning doesn't explain to me at all what the significance of it is.  What does that warning imply?

```
+           WARNING: At present (3.0.4) it is not possible to pass the
+           precision parameter to ellztopoint!
```


 * In antilogorithm there is

```
+        except:
```

One should NEVER have a naked except: unless there is a very good reason for it.
Much better is to do "except TypeError" or whatever other specific exceptions there.

 * This is bad code in the `integral_points` function:

```
+                try:
+                    assert P.curve() is self
+                except:
+                    raise ValueError, "points are not on the correct curve"
```

Why not just

```
if P.curve() is not self:
     raise ValueError, "points are not on the current curve"
```

In fact, you *should* probably do:

```
if P.curve() != self:
     raise ValueError, "points are not on the current curve"
```

Make sure you know the difference between is and == (and 'is not' and !=). 

 * Similar remarks about

```
+        try:
+            assert self.is_integral()
+        except:
+            raise ValueError, "integral_points() can only be called on an integral model"
```

 
 * This will tex wrong (especially the subscript for H_q):

```
+        def search_remaining_points():
+            """Returns list of integral points on curve E written as
+               linear combination of n times the mordell-weil base
+               points and torsion points (n is bounded by H_q, which
+               will be computed at runtime)
```



 * In torsion_points:

```
+    def torsion_points(self, flag=0):
+        """
+        Returns the torsion points of this elliptic curve as a sorted list.
+
+        INPUT:
+            flag -- (default: 0)  chooses PARI algorithm:
+              flag = 0: uses Doud algorithm
+              flag = 1: uses Lutz-Nagell algorithm
```

it would be vastly more consistent with sage to replace the `flag=[integer]` parameter by an `algorithm=string` parameter.  Everywhere else in Sage we use algorithm instead of flag and set it to a string, which makes reading code much easier. 

 * The first sentence of a docstring should be a sentence (or two); in particular, end in a period:

```
+    def height(self, precision=53):
+        """Returns real height of this elliptic curve
+        This is used in integral_points()
```


 * Here:

```
+    def integral_points(self, mw_base='auto', both_signs=False):
+        """
+        Computes all integral points (up to sign) on the elliptic
+        curve E which has Mordell-Weil basis mw_base.
+        
+        INPUT:
+            self -- EllipticCurve_Rational_Field
+            mw_base -- list of EllipticCurvePoint generating the
+                       Mordell-Weil group of E
+                    (default: 'auto' - calls self.gens())
+
+            both_signs -- True/False (default False): if True the
+                       output contains both P and -P, otherwise only
+                       one of ecah pair.
```

There is an extra newline that shouldn't be there.  Also, one never explicitly lists self in the INPUT's in Sage docstrings.

 * This will look very bad when latex'd for the reference manual:

```
+        HINTS:
+            - The complexity increases exponentially in the rank of curve E.
+            - It can help if you try another Mordell-Weil base, because the
+            computation time depends on this, too.   
```






2. ROBUSTNESS:
I just made a little loop over elliptic curves, to see if I could find a bug, and quickly found numerous curves where integral_points "hangs forever".  I didn't investigate to see what's going on.  All I know about complexity is that Magma computes the integral points on the same curves almost immediately.

The three curves for which this new code "hangs forever" are: 79a1, 117a2, and 205a1.
Magma finds the integral points instantly:

```
sage: e = EllipticCurve('79a1')
sage: m = magma(e)
sage: m.IntegralPoints()
[ (0 : 0 : 1), (1 : 0 : 1), (-2 : 1 : 1), (33 : -210 : 1) ]
sage: e = EllipticCurve('117a2')
sage: m = magma(e)
sage: m.IntegralPoints()
[ (5 : -3 : 1), (-7 : 3 : 1), (2 : 3 : 1), (-4 : -12 : 1), (6 : -10 : 1), (32 : 159 : 1), (9 : 15 : 1) ]
sage: m = magma(EllipticCurve('205a1'))
sage: m
Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 22*x + 44 over Rational Field
sage: m.IntegralPoints()
[ (2 : -4 : 1), (3 : -2 : 1), (-1 : 8 : 1), (12 : 31 : 1), (2 : 1 : 1) ]
```



Also, even worse, when I control-c'd out of running 205a1 from Sage I got a SIGBUS exception:

```
sage: sage: for E in cremona_optimal_curves([80..300]):
          print E.cremona_label(); print E.integral_points()
...     
...
205a1
^C

------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

D-69-91-158-184:~ was$ 
```



---

Comment by cremona created at 2008-07-30 00:13:59

Many thanks for the very detailed, helpful and constructive comments, William!  Almost all the points you raise are about things introduced by me and not by the people who did the real work, so I'll take the blame for all that.  The one exception to that remark, I think, is the hanging on test cases, which I'll blame on the real implementors -- but help debug if I can.

I'll try to do some work on this soon.  There's something about being in a Marriott Residence Inn of an evening which makes Sage development seem just the right thing to do...


---

Attachment

replaces earlier sage-trac3674c.patch


---

Comment by cremona created at 2008-07-30 02:05:56

The new patch sage-trac3674c.2.patch replaces sage-trac3674c.patch.

I have dealt with all (I hope) of the stylistic points raised in the review (if not, I will of course do more in that direction).

Of the curves which had been reported as hanging, only the third hung for me, but I tracked the problem down to an over-strict test for ending an AGM loop in elliptic_logarithm() -- I had made a necessary change in one branch of a split on the sign of the discriminant but not in the other.
So I think the hanging problem is fixed.

However, there is more debugging to do which I want to hand back to the original implementers!   I ran all curves in the database in order like this:

```
sage: CDB=CremonaDatabase()  
sage: for E in CDB.iter(range(11,1000)):  print E.label(), E.integral_points()
```

and all went well until a runtime error in '289a3'.  The low_bound variable becomes 0 which leads to H_q_new being Infinity.

Secondly, I found lots of curves where fewer integral points were listed than by magma.
For example:

```
sage: e = EllipticCurve('117a2')
sage: e.integral_points()       
[(-4 : 15 : 1), (2 : 3 : 1), (6 : 3 : 1), (9 : 15 : 1)]
sage: m = magma(e)              
sage: m.IntegralPoints()        
[ (5 : -3 : 1), (-7 : 3 : 1), (2 : 3 : 1), (-4 : -12 : 1), (6 : -10 : 1), (32 : 159 : 1), (9 : 15 : 1) ]
```


So there is something wrong here too.

Over to you, Tobias and Michael!


---

Attachment


---

Comment by cremona created at 2008-07-30 03:55:25

sage-trac3674d.patch fixes a problem with rank 0 curves (it was returning the 0 point and both signs even when both_signs=False).


---

Comment by tnagel created at 2008-07-30 07:58:02

We will start debugging and hopefully fix the problem soon.


---

Attachment

Replaces ALL above patches


---

Comment by cremona created at 2008-08-07 21:16:29

The *new* patch sage-trac3674new.patch replaces all earlier ones, and should apply to 3.0.6.

Summary: If E is an elliptic curve over Q then E.integral_points() returns all integral points on E.   Related and other functions have been included:
    1. In ell_generic there's now a function is_x_coord() similar to lift_x() which just returns a boolean, True iff there's a point on E with given x-coord, defined over E's base field.
    2. In ell_point there are new functions for points on curves over Q:  is_on_identity_component(), elliptic_logarithm().
    3. In ell_rational_field there are functions height_pairing_matrix() and height() as well as integral_points().

I hope everything is properly doctested, but no doubt there will still be some glitches, hopefully minor.

I also tested that the patch applies cleanly to 3.1.rc0.  Not all doctests in sage/schemes/elliptic_curves pass: I will look into these now.


---

Attachment


---

Comment by cremona created at 2008-08-07 21:31:21

OK, so there's an extra mini patch:  I forgot to include one changed file in my attempt to merge all changes into a single patch.

Apply also sage-trac3674new-extra.patch and now all tests in elliptic_curves pass.

There may be some other failures since (on was's suggestion) I changed the interface to torsion_subgroup() to use an string parameter 'algorithm' instead of a numerical flag.

This is now ready for review.


---

Attachment

Apply this after the preceding two to 3.0.6 or 3.1.rc0


---

Comment by cremona created at 2008-08-08 16:47:39

Further testing revealed some more precision bugs.  The patch sage-trac3674new-extra2.patch fixes these and also makes one internal function much more efficient.  This version tests fine on all database curves up to 5478j1 where there's a new bug which I will let Michael and Tobias fix.

I have left the "needs review" tag on since it would still be worthwhile for someone to review this pending a fix of that bug.  I was planning to test in on *all* curves in the database (it only takes 50s to do the ones of conductor up to 1000), but I haven't checked the results with Magma past conductor 1000 since Magma is much too slow (mainly because it has to compute the MW generators).


---

Comment by ncalexan created at 2008-08-11 00:48:08

There are still issues.

The doctests do not pass for me: Mac OS X 10.4, Core 2 duo.  I get:


```
sage -t ell_rational_field.py
sage -t  3.0.6/devel/sage-nca/sage/schemes/elliptic_curves/ell_rational_field.py**********************************************************************
File "/Users/ncalexan/sage/tmp/ell_rational_field.py", line 3792:
    sage: a=E.integral_points([P1,P2,P3]); a
Expected:
    [(-3 : 0 : 1), (-2 : 3 : 1), (-1 : 3 : 1), (0 : 2 : 1), (1 : 0 : 1), (2 : 0 : 1), (3 : 3 : 1), (4 : 6 : 1), (8 : 21 : 1), (11 : 35 : 1), (14 : 51 : 1), (21 : 95 : 1), (37 : 224 : 1), (52 : 374 : 1), (93 : 896 : 1), (342 : 6324 : 1), (406 : 8180 : 1), (816 : 23309 : 1)]
Got:
    [(-3 : 0 : 1), (-2 : 3 : 1), (-1 : 3 : 1), (0 : 2 : 1), (1 : 0 : 1), (2 : 0 : 1), (3 : 3 : 1), (4 : 6 : 1), (21 : 95 : 1)]
**********************************************************************
File "/Users/ncalexan/sage/tmp/ell_rational_field.py", line 3795:
    sage: a = E.integral_points([P1,P2,P3], verbose=True)
Expected:
    Using mw_basis  [(2 : 0 : 1), (4 : 6 : 1), (114/49 : -720/343 : 1)]
    e1,e2,e3:  -3.01243037259331 1.06582054769620 1.94660982489710
    Minimal eigenvalue of height pairing matrix:  0.472730555831538
    x-coords of points on compact component with  -3 <=x<= 1
    set([0, -1, -3, -2, 1])
    x-coords of points on non-compact component with  2 <=x<= 6
    set([2, 3, 4])
    starting search of remaining points using coefficient bound  6
    x-coords of extra integral points:
    set([2, 3, 4, 37, 406, 8, 11, 14, 816, 52, 21, 342, 93])
    Total number of integral points: 18
Got:
    Using mw_basis  [(2 : 0 : 1), (4 : 6 : 1), (114/49 : -720/343 : 1)]
    e1,e2,e3:  -3.01243037259330 1.06582054769621 1.94660982489710
    Minimal eigenvalue of height pairing matrix:  0.472730555831536
    x-coords of points on compact component with  -3 <=x<= 1
    set([0, -1, -3, -2, 1])
    x-coords of points on non-compact component with  2 <=x<= 6
    set([2, 3, 4])
    starting search of remaining points using coefficient bound  6
    x-coords of extra integral points:
    set([2, 21])
    Total number of integral points: 9
**********************************************************************
File "/Users/ncalexan/sage/tmp/ell_rational_field.py", line 3812:
    sage: a=E.integral_points(both_signs=True); a
Expected:
    [(-3 : -1 : 1), (-3 : 0 : 1), (-2 : -4 : 1), (-2 : 3 : 1), (-1 : -4 : 1), (-1 : 3 : 1), (0 : -3 : 1), (0 : 2 : 1), (1 : -1 : 1), (1 : 0 : 1), (2 : -1 : 1), (2 : 0 : 1), (3 : -4 : 1), (3 : 3 : 1), (4 : -7 : 1), (4 : 6 : 1), (8 : -22 : 1), (8 : 21 : 1), (11 : -36 : 1), (11 : 35 : 1), (14 : -52 : 1), (14 : 51 : 1), (21 : -96 : 1), (21 : 95 : 1), (37 : -225 : 1), (37 : 224 : 1), (52 : -375 : 1), (52 : 374 : 1), (93 : -897 : 1), (93 : 896 : 1), (342 : -6325 : 1), (342 : 6324 : 1), (406 : -8181 : 1), (406 : 8180 : 1), (816 : -23310 : 1), (816 : 23309 : 1)]
Got:
    [(-3 : -1 : 1), (-3 : 0 : 1), (-2 : -4 : 1), (-2 : 3 : 1), (-1 : -4 : 1), (-1 : 3 : 1), (0 : -3 : 1), (0 : 2 : 1), (1 : -1 : 1), (1 : 0 : 1), (2 : -1 : 1), (2 : 0 : 1), (3 : -4 : 1), (3 : 3 : 1), (4 : -7 : 1), (4 : 6 : 1)]
**********************************************************************
1 items had failures:
   3 of  12 in __main__.example_100
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/ncalexan/sage/tmp/.doctest_ell_rational_field.py
	 [60.5 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  3.0.6/devel/sage-nca/sage/schemes/elliptic_curves/ell_rational_field.py
Total time for all tests: 60.5 seconds
```


Also, as jcremona points out:


```
sage: EllipticCurve('5478j1').integral_points()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/Users/ncalexan/sage-3.0.6/devel/sage-nca/<ipython console> in <module>()

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in integral_points(self, mw_base, both_signs, verbose)
   4114             #LLL - implemented in sage - operates on rows not on columns 
   4115             m_LLL = m.LLL()
-> 4116             m_gram = m_LLL.gram_schmidt()[0]
   4117             b1_norm = R(m_LLL.row(0).norm())
   4118     

/Users/ncalexan/sage-3.0.6/devel/sage-nca/matrix2.pyx in sage.matrix.matrix2.Matrix.gram_schmidt (sage/matrix/matrix2.c:20026)()

/Users/ncalexan/sage/local/lib/python/site-packages/sage/modules/misc.py in gram_schmidt(B)
     55     for i in range(1,n):
     56         for j in range(i):
---> 57             mu[i,j] = B[i].dot_product(Bstar[j]) / (Bstar[j].dot_product(Bstar[j]))
     58         Bstar.append(B[i] - sum(mu[i,j]*Bstar[j] for j in range(i)))
     59     return Bstar, mu

/Users/ncalexan/sage-3.0.6/devel/sage-nca/element.pyx in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9326)()

/Users/ncalexan/sage-3.0.6/devel/sage-nca/coerce.pxi in sage.structure.element._div_c (sage/structure/element.c:16760)()

/Users/ncalexan/sage-3.0.6/devel/sage-nca/integer.pyx in sage.rings.integer.Integer._div_c_impl (sage/rings/integer.c:8814)()

/Users/ncalexan/sage-3.0.6/devel/sage-nca/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class._div (sage/rings/integer_ring.c:3991)()

ZeroDivisionError: Rational division by zero
```


The problem is that a singular matrix is being sent into gram_schmidt -- namely [[0, 0], [1, 1]].  I don't think that will ever work.


---

Attachment


---

Comment by ncalexan created at 2008-08-11 00:49:54

I have attached the patch I used, `3674-jcremona-integral-points.patch`, just for completeness.  I think that it alone can be applied and is the correct point to start fixing the existing bugs.


---

Comment by cremona created at 2008-08-11 08:15:21

I must have messed up in my attempt to simplify a series of patches into one, and sent something incomplete.  I'll sort that out, but I'll be off line all day today so it will not be immediate.

We know about the singular matrix problem with 5478j1;  Michael and Tobias are looking to fix that.


---

Attachment


---

Attachment


---

Comment by cremona created at 2008-08-12 19:08:33

Debugging after initial review has finished, and three new (small) patches are the result.

Apply the following to 3.1.alpha1 in order:

```
sage-trac3674new.patch
sage-trac3674new-extra.patch
sage-trac3674new-extra2.patch
sage-trac3674new-extra4.patch
sage-trac3674new-extra3.patch
sage-trac3674new-extra5.patch
```

Apologies for having 6 patches but last time I tried to merge them and messed up.  You should find that all doctests in sage.schemes.elliptic_curves.ell_rational_field.py pass.  We have also checked that (1) for all database curves up to conductor 1000 the results agree with Magma; (2) the code runs fine for all the 64687 curves of conductor up to 10000 (which takes under 32m on my laptop).  If you want to rerun those tests, first install the optional database since otherwise it will be much slower as the MW groups will need to be computed too.

Hoping for a review in time for 3.1!

John, Michael and Tobias


---

Comment by was created at 2008-08-13 07:23:02

REFEREE REPORT:

* Applying in this order to 3.0.6 works fine (note that it does not work with 3.1.alpha1, i.e., there are conflicts, but that's ok.)

```
sage-trac3674new.patch
sage-trac3674new-extra.patch
sage-trac3674new-extra2.patch
sage-trac3674new-extra3.patch
sage-trac3674new-extra4.patch
sage-trac3674new-extra5.patch
```


I applied all the patches under OS X and had the following errors when doctesting the elliptic_curves directory.  Maybe you could fix things so they pass?  E.g., maybe they are the result of randomness, etc. 

```
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ell_point.py
**********************************************************************
File "/Users/was/s/tmp/ell_point.py", line 479:
    sage: Q = 5*E.1; Q
Expected:
    (-2739/1444 : 22161/54872 : 1)
Got:
    (-2739/1444 : -77033/54872 : 1)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_22
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/was/s/tmp/.doctest_ell_point.py

	 [11.4 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ell_padic.py
	 [2.5 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ell_modular_symbols.py
	 [3.5 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ell_number_field.py
	 [9.6 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ell_finite_field.py
	 [15.4 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ell_generic.py
	 [22.9 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ell_field.py
	 [3.3 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ec_database.py
	 [2.9 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/constructor.py
	 [3.5 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/cm.py
	 [2.5 s]
sage -t  devel/sage-integral_points/sage/schemes/elliptic_curves/ell_rational_field.py
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 3780:
    sage: a = E.integral_points([P1,P2,P3], verbose=True)
Expected:
    Using mw_basis  [(2 : 0 : 1), (4 : 6 : 1), (114/49 : -720/343 : 1)]
    e1,e2,e3:  -3.01243037259331 1.06582054769620 1.94660982489710
    Minimal eigenvalue of height pairing matrix:  0.472730555831538
    x-coords of points on compact component with  -3 <=x<= 1
    [-3, -2, -1, 0, 1]
    x-coords of points on non-compact component with  2 <=x<= 6
    [2, 3, 4]
    starting search of remaining points using coefficient bound  6
    x-coords of extra integral points:
    [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]
    Total number of integral points: 18
Got:
    Using mw_basis  [(2 : 0 : 1), (4 : 6 : 1), (114/49 : -720/343 : 1)]
    e1,e2,e3:  -3.01243037259330 1.06582054769621 1.94660982489710
    Minimal eigenvalue of height pairing matrix:  0.472730555831536
    x-coords of points on compact component with  -3 <=x<= 1
    [-3, -2, -1, 0, 1]
    x-coords of points on non-compact component with  2 <=x<= 6
    [2, 3, 4]
    starting search of remaining points using coefficient bound  6
    x-coords of extra integral points:
    [2, 3, 4, 8, 11, 14, 21, 37, 52, 93, 342, 406, 816]
    Total number of integral points: 18
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 146:
    sage: E.gens()         # causes actual rank to be computed
Expected:
    [(0 : -1 : 1)]
Got:
    [(0 : 0 : 1)]
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 148:
    sage: E.rank()         # the correct rank
Expected:
    1
Got:
    99
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 1399:
    sage: E.gens()
Expected:
    [(0 : -1 : 1)]
Got:
    [(0 : 0 : 1)]
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 1576:
    sage: Q=5*P; Q
Expected:
    (1/4 : -3/8 : 1)
Got:
    (1/4 : -5/8 : 1)
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 1578:
    sage: E.saturation([Q])
Expected:
    ([(0 : -1 : 1)], '5', 0.0511114075779915)
Got:
    ([(0 : 0 : 1)], '5', 0.0511114075779915)
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 2313:
    sage: E.cremona_label()
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field.
Got:
    '10351a1'
**********************************************************************
File "/Users/was/s/tmp/ell_rational_field.py", line 253:
    sage: E.gens()
Expected:
    [(-2 : 3 : 1), (-7/4 : 25/8 : 1), (1 : -1 : 1)]
Got:
    [(-2 : 3 : 1), (-1 : 3 : 1), (0 : 2 : 1)]
**********************************************************************
6 items had failures:
   1 of  12 in __main__.example_100
   2 of   6 in __main__.example_2
   1 of   4 in __main__.example_32
   2 of   5 in __main__.example_36
   1 of   6 in __main__.example_63
   1 of   8 in __main__.example_7
***Test Failed*** 8 failures.
For whitespace errors, see the file /Users/was/s/tmp/.doctest_ell_rational_field.py

	 [52.7 s]

The following tests failed:
```



---

Comment by cremona created at 2008-08-13 08:24:40

I think that is all explainable by either decimal randomness, or the kind of thing I was fixing in #3793.  I'll see what I can do.


---

Comment by cremona created at 2008-08-13 08:36:03

Replying to [comment:22 cremona]:
> I think that is all explainable by either decimal randomness, or the kind of thing I was fixing in #3793.  I'll see what I can do.

I don't understand your comment about 3.0.6 vs. 3.1.alpha1.  Before I posted the latest patches I *did* apply all 6 in order to a fresh clone of a 3.1.alpha 1 build, and all applied with no issues at all.

There's some mystery here, and inconsistency which is making it very hard to iron out these last doctests.


---

Attachment


---

Comment by cremona created at 2008-08-13 09:01:00

Two things:  (1) for the doctests to work you need to have already applied the patch to #3793.  (2) I replaced some least significant decimal digits by ... to avoid decimal fuzz.

Please can you check this again?


---

Comment by was created at 2008-08-13 09:09:06

OK, everything works now and I'm happy with this code.  POSITIVE REVIEW.


---

Comment by mabshoff created at 2008-08-13 16:01:29

Hi John,

with the "new" patches applied up to number 6 I see the following doctest failures on sage.math:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/rational_torsion.py # 8 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/lseries_ell.py # 10 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 17 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 18 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 44 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/sha.py # 23 doctests failed
```

They all seem to be of the form

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_generic.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/tmp/ell_generic.py", line 308:
    sage: E.torsion_subgroup().gens()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[2]>", line 1, in <module>
        E.torsion_subgroup().gens()###line 308:
    sage: E.torsion_subgroup().gens()
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 2409, in torsion_subgroup
        self.__torsion_subgroup = rational_torsion.EllipticCurveTorsionSubgroup(self, algorithm)
      File "/scratch/mabshoff/release-cycle/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/rational_torsion.py", line 59, in __init__
        G = self.__E.pari_curve().elltors(flag) # pari_curve will return the curve of maximum known precision
      File "gen.pyx", line 4647, in sage.libs.pari.gen.gen.elltors (sage/libs/pari/gen.c:17124)
    TypeError: an integer is required
**********************************************************************
1 items had failures:
```



---

Comment by mabshoff created at 2008-08-13 16:46:19

Hi,

I am an idiot and forgot to apply one patch in the series. Sorry - I should sleep more ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 17:15:24

Hi,

the doctests now pass, but there is the following issue: Due to using the symbolic sqrt, ceil and floor the time to doctest sha.py double from 22 to 45 seconds (not long) and the time to doctest  it long goes from 4 minutes to 10.5. The extra time seems to be mostly spend in clisp. A number of other doctests also show similar increase in time. I have made this isssue a blocker for 3.1 at #3837, but the patches will be merged shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 17:27:16

Resolution: fixed


---

Comment by mabshoff created at 2008-08-13 17:27:16

Merged 

 * sage-trac3674new.patch
 * sage-trac3674new-extra.patch
 * sage-trac3674new-extra2.patch
 * sage-trac3674new-extra3.patch
 * sage-trac3674new-extra4.patch
 * sage-trac3674new-extra5.patch
 * sage-trac3674new-extra6.patch

in Sage 3.1.alpha2


---

Comment by cremona created at 2008-08-13 21:53:18

I know what this is -- on Williams's suggestion (insistence!) in his review I made a change entirely independent of the integral points stuff, namely that in the torsion_subgroup function the algorithm parameter should change from being an integer to a string.  And so there are problems all over the place with other functions which call that one.

I can fix all that, but it might not be tonight since I've just got home after an evening out.  First thing tomorrow, I promise!


---

Comment by cremona created at 2008-08-14 08:09:11

Replying to [comment:27 mabshoff]:
> Hi,
> 
> I am an idiot and forgot to apply one patch in the series. Sorry - I should sleep more ;)
> 
> Cheers,
> 
> Michael

Michael,

Could you confirm that there are no problems after all with those "sage -t -long" tests?  They work for me.

John


---

Comment by mabshoff created at 2008-08-14 14:18:26

Replying to [comment:31 cremona]:
> Replying to [comment:27 mabshoff]:
> > Hi,
> > 
> > I am an idiot and forgot to apply one patch in the series. Sorry - I should sleep more ;)
> > 
> > Cheers,
> > 
> > Michael
> 
> Michael,
> 
> Could you confirm that there are no problems after all with those "sage -t -long" tests?  They work for me.
> 
> John

Hi John,

yes, after applying all patches "sage -t -long" passes. Otherwise I would not have closed this ticket as fixed :)

Cheers,

Michael
