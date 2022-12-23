# Issue 2659: Elliptic curve cardinality sometimes Rational with bad consequences for efficiency

Issue created by migration from https://trac.sagemath.org/ticket/2659

Original creator: cremona

Original creation time: 2008-03-24 12:01:44

Assignee: was

Some of the code for computing the cardinality of an elliptic curve over a non-prime finite field manages to cache a value of type Rational  instead of Integer.  [This is caused by norms from orders being of type Rational -- see #2653.]

As a consequence the code for computing orders of points can fail to make use of the cached group order which sloes it down a lot (it has to use bsgs).

Example:  before patching (2.11.alpha1)

```
sage: E=EllipticCurve(GF(next_prime(2**30)**2,'a'),[1,1])
sage: P=E.random_point()
sage: E.cardinality()
1152921512387208375
sage: P.order() #long time
...
sage: E.abelian_group() # long time
...
```


After patching:

```
sage: E=EllipticCurve(GF(next_prime(2**30)**2,'a'),[1,1])
sage: E.cardinality()
1152921512387208375
sage: P=E.random_point()
sage: P.order()
1152921512387208375
sage: E.abelian_group()

(Multiplicative Abelian Group isomorphic to C1152921512387208375,
 ((181097701*a + 46508078 : 638908311*a + 187734235 : 1),))
```

 -- all very fast.

Attached patch should apply to 2.11.alpha1.


---

Attachment


---

Attachment


---

Comment by robertwb created at 2008-03-26 11:40:42

The attached is (I believe) a simpler solution to the issue, after applying the patches for #2653 it is as fast as forceably casting everything to be an integer. 

There is other stuff in `9029.patch` that should possibly be extracted, however.


---

Comment by cremona created at 2008-03-26 22:22:49

If Robert's patch quite certainly always results in the cached order being Integer then I am happy to remove the casts from my patch.

He is right to observe that I slipped in a second tweak in my patch, which I did while investigating the example cited.  Although that tweak is desirable, it reveals that some more thought needs to be put in to deciding the exact strategy to carry out in determining the group order, group structure and individual point orders, since they are all very interrelated.  That really needs to be thought through.

I also have waiting: a patch for abelian_group() which sppeds up the place where linear_relation() is called;  and some more code for the cases j=0 and j=1728 (for characteristics other than 2 and 3).  I had been planning to keep drip-feeding these in as I have time to code and test them, rather than going for another big bang.


---

Attachment


---

Attachment

Despite the patch at #2653 making sure that the trace of Frobenius is always Integer and not Rational, the trace (and hence the cardinality) still sometimes ended up as Rational.

9122.patch followed by 9123.patch sorts this out, and also tidies up the handling of the exceptional cases where Frobenius is actually an Integer and the Frobenius Order is Z.  With added doctests.
The first two patches on this ticket can now be ignored; the latter two are based on 2.11.

NB The handling of cardinality in case j=0 and j=1728 is still incomplete but will be patched separately.


---

Comment by mhansen created at 2008-04-04 21:46:40

Only apply 9123.patch.  The changes in 9122.patch are in #210.


---

Comment by cremona created at 2008-04-04 21:57:27

Replying to [comment:6 mhansen]:
> Only apply 9123.patch.  The changes in 9122.patch are in #210.

That's right, sorry about that.  Thanks for reviewing #21- so quickly (and positively)!  John


---

Comment by mabshoff created at 2008-04-04 22:43:24

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 22:43:24

Resolution: fixed
