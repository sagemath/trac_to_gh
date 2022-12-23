# Issue 6021: Implement period lattices for elliptic curves over CC

Issue created by migration from https://trac.sagemath.org/ticket/6021

Original creator: cremona

Original creation time: 2009-05-11 14:10:05

Assignee: was

CC:  robertwb

Keywords: elliptic curve periods

For elliptic curves over number fields we currently only support the period lattice for real embeddings.  here we will implement the same for complex embeddings too (using the complex AGM method to compute the basis).


---

Comment by cremona created at 2009-05-11 16:43:21

The patch does what was proposed.

I added an is_real() method to mpfr reals (returning True of course) also, for convenience.


---

Comment by robertwb created at 2009-05-11 19:36:22

It looks good so far. Is there any reason we're still using Pari to compute in the real embedding case rather than just doing it all ourself?


---

Comment by cremona created at 2009-05-11 20:00:48

Replying to [comment:3 robertwb]:
> It looks good so far. Is there any reason we're still using Pari to compute in the real embedding case rather than just doing it all ourself? 

Well,  in either case we are using pari for the agm (real and complex cases)!  In the real case one has to be a bit careful to get the real and im periods properly, but I certainly know how to do that.  So I could put that in if you thought it better (but I will not have time until Wednesday...)

John


---

Comment by cremona created at 2009-05-13 11:47:21

There have been additional comments about this on sage-nt. As a result I am adding to the patch, providing also (1) normalization of periods, (2) local implementation in the real case as an option instead of calling pari.
 
There will be an additional patch, so I have downgraded this to "not ready for review".


---

Comment by cremona created at 2009-05-13 14:14:46

With the new patch we now have a native implementation for real embeddings, which is the default with 'pari' as an option.  The period computation itself is devolved to a couple of internal functions.  Also, a normalisation function is included and one can ask for either a basis or normalised basis (these being different only for real embeddings).  The documentation is complete.

One thing which could be done is to cache the computed periods (with care so that if the user asks again with higher precision they do get recomputed).

The second patch was slightly premature (I had forgotten doctests for the two internal functions) so should be replaced by the third one, to be applied after the first, based on 3.4.2.


---

Comment by robertwb created at 2009-05-15 00:32:48

Looks good to me. Works as advertised and well documented. Nice work.


---

Comment by mabshoff created at 2009-05-15 06:04:14

Unsurprisingly this causes a bunch of numerical noise problems:

```
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/rational_field.py # 1 doctests failed
        sage -t -long devel/sage/sage/schemes/elliptic_curves/period_lattice.py # 11 doctests failed
```

Some of them are quite disturbing:

```
File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/schemes/elliptic_curves/period_lattice.py", line 439:
    sage: Ls[2]._compute_periods_complex(100)
Expected:
    (1.9072648860892726204877126889 - 1.3404778596244020430694806590*I,
    -1.9072648860892726204877126889 - 1.3404778596244020430694806590*I)
Got:
    (-1.9072648860892727038846028695 - 1.3404778596244020695699736749*I,
     -1.9072648860892727038846028695 + 1.3404778596244020695699736749*I)
```

I.e. notice that for the real part above *11* digits are different.

Thoughts?

Cheers,

Michael


---

Comment by cremona created at 2009-05-15 07:16:13

Maybe it's a 32/64 thing (I only tested on 32-bit, my fault).

I will look into it.


---

Attachment

Replaces all previous; based on 4.0.alpha0


---

Comment by cremona created at 2009-05-17 16:57:02

There was some 32/64 fuzz, which I have fixed, but there were also some bugs in the precision handling, which have also been fixed.

The new patch trac_6021_new.patch replaces all previous, and is based on 4.0.alpha0.  I tested the problem files on both 32- and 64-bit.


---

Comment by robertwb created at 2009-05-18 21:33:25

Why are there so many ...'s? Since we're no longer using Pari (unless we explicitly ask for it) the result should be deterministic and platform independent. (We are using Pari for complex agm, but not for real agm, but it seems to return exactly the same thing both 64- and 32-bit systems).


---

Comment by cremona created at 2009-05-19 07:54:15

Good question.

I knew we use pari for complex agm and had assumed we also did for real agm.  I suggest that first we implement complex agm in native Sage, to remove that variable.

Here are the steps:  

   1. compute 2-division poly over the number field (exact)
   2. embed the coeffs into RR or CC (depends on the embedding precision)
   3. find its roots in RR or CC (depends on precision)
   4. compute some square roots (ditto)
   5. compute some AGMs
   6. take reciprocals and multiply by pi

What should be done is to find out exactly at what point things differ.


---

Comment by robertwb created at 2009-05-19 08:21:21

I'm headed to bed soon, but I think Pari is involved in the root finding.


---

Attachment

Apply after previous


---

Comment by cremona created at 2009-05-22 15:04:28

apply after previous two


---

Attachment

OK, so I have added two new patches:  embed_qqbar.patch is independent of the others, and adds functionality to the refine_embedding() function for embeddings of number fields to allow extending any embedding into RR or CC to an embedding into AA or QQbar (choosing the correct root).  Then cperiods.patch uses that to rethink how precision is handled for period lattices (real and complex):  the embedding supplied by the user is only used to determine which embedding is wanted, not its precision (which is ignored).  the lattice converts this (on construction) into an embedding into AA or QQbar, which it keeps.  Then the period-finding functions do as much as they can exactly (i.e. in AA or QQbar), up as far as computing sqrt(ei-ej) where e1,e2,e3 are the roots of the 2-division polynomial (so these expressions may have degree 6* the degree of the field);  only then are they converted into RR or CC (with the correct precision) for the transcendental step of computing AGMs.

To test this I removed the "..." which worried robertwb and reran the doctests -- they now all pass and agree on both 32 and 64-bit machines.

I think this is a good strategy to use for number field embeddings (a.k.a. infinite places): separate the information "which place" from the information "what precision".

If this is approved, I will use the same tactic to improve the precision of the elliptic log (since the next thing on this agenda is to implement complex elliptic logs).


---

Comment by robertwb created at 2009-05-26 18:38:29

Looks good. I like the idea of using AA/QQbar for embeddings as well.


---

Comment by cremona created at 2009-05-26 21:10:35

Thanks Robert.  I'm now working on moving the elliptic log code into the Lattice class, which certainly depends on this but there's no reason to delay this.


---

Comment by cremona created at 2009-05-27 21:24:00

Yet another patch, to be applied after the previous ones.

   1. Better handling of precision.  The algebraic quantities needed for both periods and elliptic logs are now cached.  Then period and log computations just have to coerce into the appropriate Real/ComplexField, and do the transcendental part via agm.
   2. Elliptic log implementation now moved into period lattice class (except for the algorithm="pari" case which is unchanged).  Also available via call i.e. as L.elliptic_logarithm(P) or just L(P).  Uses an extended agm function which has been separated off.
   3. Earlier precision issues with a difficult example are fixed;  we get all the same digits as pari, and faster.  To do this we compute the extended AGM in double the required precision and then revert to desired precision at the end.  (I tried adding 10 or 20 bits of precision, but that nasty example (18074g1) needs more).

The only remaining thing is to implement elliptic logs for non-real lattices.  This is not hard to do but harder to justify!  Before I do that, to test it  I need to implement the reverse of the elliptic log -- using Weierstrass P-functions and derivative to go from z mod L back to P(x,y) with complex coords in general.

Apologies for adding this after a positive review (which applies to the first three patches only).  So: the first 3 patches have a positive review, while the 4th does not (yet).


---

Comment by robertwb created at 2009-06-03 07:03:38

I moved the last patch to #6193, as it's really starting to implement new functionality (though there is some good cleanup/precision handling of this code as well).


---

Comment by mhansen created at 2009-06-03 20:56:34

Resolution: fixed


---

Comment by mhansen created at 2009-06-03 20:56:34

Merged all three patches in 4.0.1.rc0.


---

Comment by cremona created at 2009-12-17 10:29:36

See also #7719.
