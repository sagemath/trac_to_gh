# Issue 7703: S-units, S-class groups, and selmer groups of etale algebras

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-12-16 05:06:57

Assignee: was

CC:  cremona craigcitro was robertwb

This is part of the machinery necessary for the descent method described by Schaefer and Stoll.


---

Comment by rlm created at 2009-12-16 05:12:19

This depends on #7595 and #7616.


---

Comment by rlm created at 2009-12-16 05:16:17

Until we can figure out #7616, this will have to sit...


---

Comment by rlm created at 2009-12-16 05:16:17

Changing status from new to needs_info.


---

Comment by cremona created at 2009-12-16 09:12:07

I have only just started to look at this -- not a review as yet!

Question:  why the "lift" methods for number field elements?  It appears to do exactly the same as polynomial():

```
sage: x = polygen(QQ)
sage: K.<a> = NumberField(x^3-2)
sage: b = K.random_element(); b
1/16*a^2 + 3*a + 1
sage: b.polynomial()
1/16*x^2 + 3*x + 1
```

On the other hand, I never thought that polynomial() was  a good name...


---

Comment by rlm created at 2009-12-16 18:06:46

In the relative number field case, `lift` gives a polynomial over the intermediate field, not over QQ.


---

Comment by rlm created at 2009-12-16 19:06:27

I suppose that `relative_polynomial` might be an appropriate name, too.


---

Comment by cremona created at 2009-12-16 20:14:54

Replying to [comment:5 rlm]:
> I suppose that `relative_polynomial` might be an appropriate name, too.

Fair enough, thanks for anwering.  One reason I never liked "polynomial" was that it is easy to confuse with either minimal or characteristic poly, both of which are intrinsic, whereas polynomial/lift depend on how the field is presented.  "lift" is fine by me.


---

Comment by rlm created at 2009-12-19 02:15:36

I finally figured out the right fix for #7616, so this is ready for review (as is 7616... )


---

Comment by rlm created at 2009-12-19 02:15:36

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2009-12-19 02:32:26

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-19 05:23:00

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2009-12-20 17:30:31

Partial Review (The dependencies need to have positive reviews at least first, I think, so I have looked at the code but not yet done any testing which I am looking forward to doing).

This looks extremely useful, both for rlm's motivating application (m-descent on elliptic curves over number fields, something I have a great deal of interest in) and others (for example, finding all elliptic curves defined over a number field K with good reduction outside S).   I implemented something similar in Magma for m=4 and m=6 (and also for m prime just for practice, though Magma's pSelmerGroup code by Claus Fieker is quite sophisticated.

The hard part of this is really invisible in the pari code.  That is not a criticism, just a clue for anyone else looking into this and working out where the S-class group and S-units are really found!  And working out how to interface with that successfully is non-trivial, so hats off to rlm for doing this.

It will be even better when Sage-s abelian groups are properly usable for the output from these functions (and for unit groups and class groups more generally, and lots of other stuff).  When that day comes we'll want to add functionality such as:  if I give you an element of `K<sup>*/(K</sup>*)^m` representing an element of K(S,m), can you give me the corresponding abstract group element of K(S,M)?  (It is setting things up so that that is efficient which makes Claus's Magma code so much more complicated.  I'm sure that is doable, since Claus told me that the hardest part is expressing a unit in terms of fundamental units and we already have that in Sage, from wrapping the appropriate pari function).

Some minor points:

    1. Line 1010 says

```
for g in D.ideal([a for a in p.gens()]).gens(): # this line looks a bit silly, due to inconsistency over QQ - see # 7596 
```

Could you not replace [a for a in p.gens()] by p.gens() ?

    2. Lines 1087-8 (and some similar places):

```
prod_ideal_gen = [] 
for j in xrange(i): 
      prod_ideal_gen.append(0) 
```

could presumable be replaced by prod_ideal = [0]*i ?

These are trivialities.  Now let's get the dependencies sorted!


---

Comment by rlm created at 2010-01-02 14:40:01

The dependencies are now all positively reviewed, and I've addressed your comments above in a separate patch (to make for easier editing... I can flatten them later).


---

Comment by cremona created at 2010-01-06 11:54:34

pre-final review:

As I was having trouble with 4.3.1.alpha0 I applied the following to a fresh clone of 4.3:
    1. trac_7616_alt.patch  (already merged in 4.3.alpha0)
    2. trac_7595.patch               (with positive review)
    3. trac_7595-failures.patch      (ditto)
    4. trac_7836-CRT.patch           (ditto)
    5. trac_7703.patch
    6. trac_7703-lists.patch
all with no problems.  Tested all sage/rings/number_fields successfully.

Now I'm going to try out the code for a bit before returning soon for (I hope) a positive review.


---

Comment by cremona created at 2010-01-06 12:16:41

As soon as I tried out an example of my own I hit a problem -- the functions S_class_group(), S_unit_group() and selmer_group() only apply to objects of type 'sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing_field' and not to number fields!  The first thing I wanted to do was

```
sage: K.<a> = QuadraticField(-23)
sage: K.selmer_group([],3)
```

and that does not work, you have to form the polynomial ring K[] and then quotient out the generator x to get something isomorphic to K which has forgotten that it is a number field.

Can we not design things so that number fields are a special case of etale algebras in a slightly more transparent way?  Failing that, can we not implement the three functions just mentioned for number fields directly?  This is what I would need!

If that would be easy, I suggest adding it right now before merging this in.  But if there are difficulties, I could be persuaded to get this in now as it is as long as there was a clear TODO and a new ticket to do what I want.

I have therefore tagged the ticket as "needs work", but you (rlm) should feel free to argue for the second option, put it back to "needs review" and (if I am convinced by the argument ;)) will come back to give it a positive review.


---

Comment by cremona created at 2010-01-06 12:16:41

Changing keywords from "" to "number fields selmer groups".


---

Comment by cremona created at 2010-01-06 12:16:41

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-01-06 14:39:23

I agree. What I would suggest is to implement S-units and S-class groups for number fields, and then just factor out that code in the polynomial quotient rings (i.e. there, just do NFComponent.S_units(...) and have the real work going on in number fields). I'll post a patch later on which does this.


---

Comment by cremona created at 2010-01-06 14:50:35

Replying to [comment:14 rlm]:
> I agree. What I would suggest is to implement S-units and S-class groups for number fields, and then just factor out that code in the polynomial quotient rings (i.e. there, just do NFComponent.S_units(...) and have the real work going on in number fields). I'll post a patch later on which does this.

I'm glad you agree -- sorry to have suggested more work when you have already done so much.  I'll be happy to review any new patch, of course.


---

Comment by rlm created at 2010-01-14 00:08:11

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-01-14 11:32:28

I applied all the following except the first to 4.3.1.alpha1 since I have not yet built a 4.3.1.alpha2.

   1. trac_7616_alt.patch (merged in 4.3.1.alpha0)
   2. trac_7595.patch (merged in 4.3.1.alpha2)
   3. trac_7595-failures.patch (ditto)
   4. trac_7836-CRT.patch (ditto)
   5. trac_7703.patch
   6. trac_7703-lists.patch 
   7. trac_7703-nf.patch

The patches applied fine.

I had some test failures in polynomial_quotient_ring which at a glance look like just whitespace:

```
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 649:
    sage: S.S_class_group([])
Expected:
    [((3/8*xbar^2 + 93/8,
       -3/8*a*xbar^2 - 93/8*a, 3/16*xbar^3 - 3/16*xbar^2 + 93/16*xbar - 93/16,
       (-1/16*a + 1/8)*xbar^3 + (-1/16*a + 1/8)*xbar^2 + (-31/16*a + 31/8)*xbar - 31/16*a + 31/8),
      6,
      (1/16*a - 101/16)*xbar^3 + (187/16*a + 65/16)*xbar^2 + (31/16*a - 3131/16)*xbar + 5797/16*a + 2031/16),
     ((-1/4*xbar^2 - 23/4,
       (1/8*a - 1/8)*xbar^2 + 23/8*a - 23/8,
       -1/16*xbar^3 + 1/16*xbar^2 - 23/16*xbar + 23/16,
       1/16*a*xbar^3 - 1/16*a*xbar^2 + 23/16*a*xbar - 23/16*a),
      6,
      1/16*xbar^3 + 1/16*xbar^2 + 23/16*xbar + 39/16),
     ((-5/4*xbar^2 - 115/4,
       5/4*a*xbar^2 + 115/4*a,
       -5/16*xbar^3 - 5/16*xbar^2 - 115/16*xbar - 115/16,
       1/16*a*xbar^3 + 13/16*a*xbar^2 + 23/16*a*xbar + 299/16*a),
      2,
      5/16*xbar^3 - 33/16*xbar^2 + 115/16*xbar - 743/16)]
Got:
    [((3/8*xbar^2 + 93/8, -3/8*a*xbar^2 - 93/8*a, 3/16*xbar^3 - 3/16*xbar^2 + 93/16*xbar - 93/16, (-1/16*a + 1/8)*xbar^3 + (-1/16*a + 1/8)*xbar^2 + (-31/16*a + 31/8)*xbar - 31/16*a + 31/8), 6, (1/16*a - 101/16)*xbar^3 + (187/16*a + 65/16)*xbar^2 + (31/16*a - 3131/16)*xbar + 5797/16*a + 2031/16), ((-1/4*xbar^2 - 23/4, (1/8*a - 1/8)*xbar^2 + 23/8*a - 23/8, -1/16*xbar^3 - 3/16*xbar^2 - 23/16*xbar - 69/16, 1/16*a*xbar^3 + (1/16*a - 1/8)*xbar^2 + 23/16*a*xbar + 23/16*a - 23/8), 6, 1/16*xbar^3 + 1/16*xbar^2 + 23/16*xbar + 39/16), ((-5/4*xbar^2 - 115/4, 5/4*a*xbar^2 + 115/4*a, -5/16*xbar^3 - 5/16*xbar^2 - 115/16*xbar - 115/16, 1/16*a*xbar^3 + 13/16*a*xbar^2 + 23/16*a*xbar + 299/16*a), 2, 5/16*xbar^3 - 33/16*xbar^2 + 115/16*xbar - 743/16)]
**********************************************************************
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 671:
    sage: S.S_class_group([K.ideal(a)])
Expected:
    [((3/8*xbar^2 + 93/8,
       -3/8*a*xbar^2 - 93/8*a,
       3/16*xbar^3 - 3/16*xbar^2 + 93/16*xbar - 93/16,
       (-1/16*a + 1/8)*xbar^3 + (-1/16*a + 1/8)*xbar^2 + (-31/16*a + 31/8)*xbar - 31/16*a + 31/8),
      6,
      (1/16*a - 101/16)*xbar^3 + (187/16*a + 65/16)*xbar^2 + (31/16*a - 3131/16)*xbar + 5797/16*a + 2031/16),
     ((-1/4*xbar^2 - 23/4,
       (1/8*a - 1/8)*xbar^2 + 23/8*a - 23/8,
       -1/16*xbar^3 + 1/16*xbar^2 - 23/16*xbar + 23/16,
       1/16*a*xbar^3 - 1/16*a*xbar^2 + 23/16*a*xbar - 23/16*a),
      2,
      -1/8*xbar^2 - 15/8)]
Got:
    [((3/8*xbar^2 + 93/8, -3/8*a*xbar^2 - 93/8*a, 3/16*xbar^3 - 3/16*xbar^2 + 93/16*xbar - 93/16, (-1/16*a + 1/8)*xbar^3 + (-1/16*a + 1/8)*xbar^2 + (-31/16*a + 31/8)*xbar - 31/16*a + 31/8), 6, (-1/16*a + 101/16)*xbar^3 + (-187/16*a - 69/16)*xbar^2 + (-31/16*a + 3131/16)*xbar - 5797/16*a - 2123/16), ((-1/4*xbar^2 - 23/4, (1/8*a - 1/8)*xbar^2 + 23/8*a - 23/8, -1/16*xbar^3 - 3/16*xbar^2 - 23/16*xbar - 69/16, 1/16*a*xbar^3 + (1/16*a - 1/8)*xbar^2 + 23/16*a*xbar + 23/16*a - 23/8), 2, -1/8*xbar^2 - 15/8)]
**********************************************************************
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 760:
    sage: S.class_group()
Expected:
    [((1/12*xbar^2 + 47/12,
       1/48*xbar^3 - 1/48*xbar^2 + 47/48*xbar - 47/48),
      3,
      -1/48*xbar^3 - 5/48*xbar^2 - 47/48*xbar - 187/48),
     ((-1/12*xbar^2 - 23/12,
       -1/48*xbar^3 - 1/48*xbar^2 - 23/48*xbar - 23/48),
      5,
      -1/48*xbar^3 - 7/48*xbar^2 - 23/48*xbar - 113/48)]
Got:
    [((1/12*xbar^2 + 47/12, 1/48*xbar^3 - 1/48*xbar^2 + 47/48*xbar - 47/48), 3, -1/48*xbar^3 - 5/48*xbar^2 - 47/48*xbar - 187/48), ((-1/12*xbar^2 - 23/12, -1/48*xbar^3 - 1/16*xbar^2 - 23/48*xbar - 23/16), 5, -1/48*xbar^3 + 11/48*xbar^2 - 23/48*xbar + 301/48)]
**********************************************************************
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 776:
    sage: S.class_group()
Expected:
    [((3/8*xbar^2 + 93/8,
       -3/8*a*xbar^2 - 93/8*a, 3/16*xbar^3 - 3/16*xbar^2 + 93/16*xbar - 93/16,
       (-1/16*a + 1/8)*xbar^3 + (-1/16*a + 1/8)*xbar^2 + (-31/16*a + 31/8)*xbar - 31/16*a + 31/8),
      6,
      (1/16*a - 101/16)*xbar^3 + (187/16*a + 65/16)*xbar^2 + (31/16*a - 3131/16)*xbar + 5797/16*a + 2031/16),
     ((-1/4*xbar^2 - 23/4,
       (1/8*a - 1/8)*xbar^2 + 23/8*a - 23/8,
       -1/16*xbar^3 + 1/16*xbar^2 - 23/16*xbar + 23/16,
       1/16*a*xbar^3 - 1/16*a*xbar^2 + 23/16*a*xbar - 23/16*a),
      6,
      1/16*xbar^3 + 1/16*xbar^2 + 23/16*xbar + 39/16),
     ((-5/4*xbar^2 - 115/4,
       5/4*a*xbar^2 + 115/4*a,
       -5/16*xbar^3 - 5/16*xbar^2 - 115/16*xbar - 115/16,
       1/16*a*xbar^3 + 13/16*a*xbar^2 + 23/16*a*xbar + 299/16*a),
      2,
      5/16*xbar^3 - 33/16*xbar^2 + 115/16*xbar - 743/16)]
Got:
    [((3/8*xbar^2 + 93/8, -3/8*a*xbar^2 - 93/8*a, 3/16*xbar^3 - 3/16*xbar^2 + 93/16*xbar - 93/16, (-1/16*a + 1/8)*xbar^3 + (-1/16*a + 1/8)*xbar^2 + (-31/16*a + 31/8)*xbar - 31/16*a + 31/8), 6, (1/16*a - 101/16)*xbar^3 + (187/16*a + 65/16)*xbar^2 + (31/16*a - 3131/16)*xbar + 5797/16*a + 2031/16), ((-1/4*xbar^2 - 23/4, (1/8*a - 1/8)*xbar^2 + 23/8*a - 23/8, -1/16*xbar^3 - 3/16*xbar^2 - 23/16*xbar - 69/16, 1/16*a*xbar^3 + (1/16*a - 1/8)*xbar^2 + 23/16*a*xbar + 23/16*a - 23/8), 6, 1/16*xbar^3 + 1/16*xbar^2 + 23/16*xbar + 39/16), ((-5/4*xbar^2 - 115/4, 5/4*a*xbar^2 + 115/4*a, -5/16*xbar^3 - 5/16*xbar^2 - 115/16*xbar - 115/16, 1/16*a*xbar^3 + 13/16*a*xbar^2 + 23/16*a*xbar + 299/16*a), 2, 5/16*xbar^3 - 33/16*xbar^2 + 115/16*xbar - 743/16)]
**********************************************************************
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 846:
    sage: L.S_units([])
Expected:
    [(-1/2*a + 1/2, 6),
     ((1/3*a - 1)*b^2 + 4/3*a*b + 5/6*a + 7/2, +Infinity),
     ((1/3*a + 1)*b^2 + (-2/3*a - 2)*b + 5/6*a + 7/2, +Infinity)]
Got:
    [(-1/2*a + 1/2, 6), ((-1/3*a - 1)*b^2 + (2/3*a - 2)*b + 13/6*a + 1/2, +Infinity), ((-1/3*a + 1)*b^2 - 4/3*a*b - 4/3*a - 3, +Infinity)]
**********************************************************************
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 850:
    sage: L.S_units([K.ideal(1/2*a - 3/2)])
Expected:
    [((-1/6*a - 1/2)*b^2 + (1/3*a + 1)*b - 2/3*a - 2, +Infinity),
     (-1/2*a + 1/2, 6),
     ((-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2, +Infinity),
     ((-1/3*a - 1)*b^2 + (2/3*a - 2)*b + 13/6*a + 1/2, +Infinity)]
Got:
    [((1/6*a - 1/2)*b^2 + (-1/3*a + 1)*b + 2/3*a - 2, +Infinity), (-1/2*a + 1/2, 6), ((-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2, +Infinity), ((1/3*a + 1)*b^2 + (-2/3*a - 2)*b + 5/6*a + 7/2, +Infinity)]
**********************************************************************
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 855:
    sage: L.S_units([K.ideal(2)])
Expected:
    [((1/6*a - 1/2)*b^2 + (-1/3*a + 1)*b + 1/6*a - 3/2, +Infinity),
     ((1/6*a + 1/2)*b^2 + (-1/3*a - 1)*b + 1/6*a + 3/2, +Infinity),
     ((-1/2*a + 1/2)*b^2 + (a - 1)*b - 3/2*a + 3/2, +Infinity),
     (-1/2*a + 1/2, 6),
     ((-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2, +Infinity),
     ((-1/3*a + 1)*b^2 - 4/3*a*b - 4/3*a - 3, +Infinity)]
Got:
    [((1/2*a + 1/2)*b^2 + (-a - 1)*b + 3/2*a + 3/2, +Infinity), ((1/6*a + 1/2)*b^2 + (-1/3*a - 1)*b + 1/6*a + 3/2, +Infinity), ((1/6*a + 1/2)*b^2 + (-1/3*a - 1)*b + 2/3*a + 1, +Infinity), (-1/2*a + 1/2, 6), ((-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2, +Infinity), ((-1/3*a + 1)*b^2 - 4/3*a*b - 4/3*a - 3, +Infinity)]
**********************************************************************
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 910:
    sage: L.units()
Expected:
    [(-1/2*a + 1/2, 6),
     ((1/3*a - 1)*b^2 + 4/3*a*b + 5/6*a + 7/2, +Infinity),
     ((-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2, +Infinity)]
Got:
    [(-1/2*a + 1/2, 6), ((-1/3*a - 1)*b^2 + (2/3*a - 2)*b + 13/6*a + 1/2, +Infinity), ((-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2, +Infinity)]
**********************************************************************
File "/home/jec/sage-4.3.1.alpha1/devel/sage-7703/sage/rings/polynomial/polynomial_quotient_ring.py", line 917:
    sage: L.unit_group().gens()
Expected:
    [-1/2*a + 1/2,
     (1/3*a - 1)*b^2 + 4/3*a*b + 5/6*a + 7/2,
     (-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2]
Got:
    [-1/2*a + 1/2, (-1/3*a - 1)*b^2 + (2/3*a - 2)*b + 13/6*a + 1/2, (-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2]
**********************************************************************
4 items had failures:
   2 of  24 in __main__.example_18
   2 of  26 in __main__.example_19
   3 of  19 in __main__.example_20
   2 of  21 in __main__.example_21
***Test Failed*** 9 failures.
For whitespace errors, see the file /home/jec/.sage//tmp/.doctest_polynomial_quotient_ring.py
	 [15.9 s]
```


Everything else is fine.


---

Comment by cremona created at 2010-01-14 11:32:28

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-01-14 16:48:46

It's not quite white space, usually it's some difference like cbar --> -xbar. I keep fixing these doctests, but maybe this means that they are dependent on the platform...?


---

Comment by cremona created at 2010-01-14 17:10:19

It looks like pure white space to me!

This was tested on a 64-bit ubuntu machine.  I'll try again on a 32-bit to see if that makes any difference.


---

Comment by rlm created at 2010-01-14 17:23:49

Replying to [comment:20 cremona]:
> It looks like pure white space to me!

Example, in the last one:

```
Expected: [-1/2*a + 1/2, (1/3*a - 1)*b^2 + 4/3*a*b + 5/6*a + 7/2,         (-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2]
     Got: [-1/2*a + 1/2, (-1/3*a - 1)*b^2 + (2/3*a - 2)*b + 13/6*a + 1/2, (-1/3*a + 1)*b^2 + (2/3*a - 2)*b - 5/6*a + 7/2]
```


Since I've got the build farm going, I guess I can try this on each platform to see what happens...


---

Comment by cremona created at 2010-01-14 17:30:35

It's rather common for pari to give different output on different machines, especially 32/64.  This hit me in the past (e.g. when doing unit groups over number fields).  I cannot remember how I resolved it.  The output depends on the history of what has been computed in the past -- just the sort of thing which will come up in a big way if we ever institute William's random-order-of-doctesting!


---

Comment by rlm created at 2010-01-16 05:41:18

Replaces previous patches


---

Attachment

This works for at least two distinct sets of output, so if it's a 32-64 bit issue, this should take care of it.


---

Comment by rlm created at 2010-01-16 05:42:25

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-01-16 14:33:59

I'll check this out as soon as my builds of 4.3.1.rc0 have finished.


---

Comment by cremona created at 2010-01-16 18:17:08

The new patch applies fine on 4.3.1.rc0 and all tests in rings/polynomial and rings/number_field pass on both 32 and 64 bit. OK!


---

Comment by cremona created at 2010-01-16 18:17:08

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-18 22:14:52

Resolution: fixed
