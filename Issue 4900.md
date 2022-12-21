# Issue 4900: New BSGS point counting on elliptic curves over finite fields

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-01-01 15:34:17

Assignee: was

Keywords: elliptic curves finite fields

Point counting on elliptic curves where the j-invariant is not in the prime field has been implemented up to now via the same function that determines the group structure.  The reason was that "Mestre's trick" does not always work over non-prime fields (specifically, over F_q where q is square there are always counterexamples).  I worked out how to extend Mestre to the general case about 9 months ago but did not want to contribute the resulting code until it was written up.  That has now been done, in a 4-page note joint with Drew Sutherland.  (See http://www.warwick.ac.uk/staff/J.E.Cremona/papers/MestreNote.pdf;  it should be on ArXiV early January 2009).

The current patch implements this in a new function cardinality_bsgs().  This will always be used in computing the cardinality of curves whose j-invariant is not in the prime field.  Over prime fields it can be used by giving algorithm='bsgs' to the cardinality() function.  [The old use of algorithm='bsgs' is renamed algorithm='pari' since that's the option to call pari, which is only over prime fields.]

This also means that the abelian_group() function is simpler since it always computes the cardinality first, which simplifies that code.

Lastly, the new code uses quadratic twists, and the quadratic_twist() funtion in ell_generic.py can now be called with no twisting parameter for curves over finite fields, with the single exception of characteristic 2 and j=0.

The patch applies to 3.2.2 and has been tested on lots of curves (including all the -long tests in sage/schemes/elliptic_curves).


---

Attachment


---

Comment by malb created at 2009-01-01 21:56:49

* it seems the docstring for the option 'all' lacks a mention of 'bsgs' (it only mentions 'pari' and 'sea'
 * I'm not sure about the current policy w.r.t. renaming stuff ('bsgs' -> 'pari'). Would this break existing code?
 * maybe the debug printing should be handled using `verbose()`?
 * is the `if debug` around `assert foo` necessary?


---

Comment by cremona created at 2009-01-01 22:36:55

Replying to [comment:2 malb]:
>  * it seems the docstring for the option 'all' lacks a mention of 'bsgs' (it only mentions 'pari' and 'sea'

OK.  Actually the 'all' option does not work at all as advertised since the cached value is used.  I had to comment out the cache retrieval lines to test.

I think a better way of managing this would be for the individual methods to have separate functions which do _not_ use the cached value (as in the new functions cardinality_bsgs()) and then the main user function cardinality() can call whichever version the user wants (but use the cached value if available; perhaps only if the user does not specify an algorithm to use).

>  * I'm not sure about the current policy w.r.t. renaming stuff ('bsgs' -> 'pari'). Would this break existing code?

I checked and there's nothing in Sage itself affected.  In other places algorithm=pari is used and it makes more sense to me than to second-guess what algorithm the current version of pari uses.

>  * maybe the debug printing should be handled using `verbose()`?
>  * is the `if debug` around `assert foo` necessary?

I have no strong feelings.  The assertions are there for debugging purposes.  I prefer this way of commenting lines out;  I could delete them, but then it will be more hassle next time there is a bug.


---

Comment by cremona created at 2009-01-02 14:06:10

I made this "not ready for review" since Drew has made some very helpful suggestions which should help the efficiency main function in this patch.  At the same time I am dealing with the trivialities raised by malb's non-review ;)


---

Comment by cremona created at 2009-01-04 19:18:19

Testing has revealed a bug (an embarrassing one in code of mine) in _p_primary_torsion_basis() as exemplified here:

```
 sage: p=10^60+3201
sage: K=GF(p)
sage: a=804515977734860566494239770982282063895480484302363715494873
sage: b=584772221603632866665682322899297141793188252000674256662071
sage: E=EllipticCurve(K,[0,a,0,b,0])
sage: E.cardinality().factor()
2^17 * 13115567671 * 581705246972988608203110387504181554514650287
sage: E._p_primary_torsion_basis(2)

[[(656068448840236768725810484116830935925716002501543862440466 : 324360550482744921974063628110267202720852104214117741680354 : 1),
  2],
 [(21059802536298599082171845328893691100757301985761775129713 : 0 : 1), 1]]
```

Here the 2-sylow subgroup has structure 2^16 * 2 but E._p_primary_torsion_basis(2) only gives 2<sup>2*2</sup>1.  I know what the problem is and am working out how to fix it.

NB This function is called in ell_torsion.py in computing torsion groups over number fields, which is rather likely to give wrong answers (though not over Q where pari is used ;)) until this is fixed.  So I will make this a separate ticket marked "major defect"!


---

Attachment

The new patch replaces the old.  It is based on 3.2.3+#4926 which means that both the files touched (ell_generic.py and ell_finite_field.py) are fully sphinxified.  It does the following:
   1. Implements the new point-counting algorithm much as before.
   2. Adds a preliminary computation of l-power torsion for l in [2,3,5] (depending on the size q of the field) which (when non-trivial) helps the bsgs routine for finding the order of random points.  This part revealed a bad bug in _p_primary_torsion() which was posted at #4937, but note that...
   3. The bug in #4937 is fixed here.
   4. Following malb's comments I have separated out functions cardinality_sea() and cardinality_pari() to be separate functions, as is cardinality_bsgs().  None of these caches the result.  The main functions cardinality(), which has the algorithm parameter ('heuristic' by default) does cache.  The 'all' option still does not work as advertised because of the caching (but then it never did).  I think it should be done away with since testing should be done independently using the cardinality_*() functions directly.  The old cardinality_from_group() function is now redundant and has been deleted (please don't ask me to deprecate it!)
   5. The abelian_group() function is now cleaner and simpler since in all cases the group order is known at the start.

So I have broken some rules by having this patch deal with #4937 too;  by the time I realised, it was too late to separate the two.  As a consolation I'll add a patch at #4937, based on this one, which adds the doctest which (as usual) I forgot.


---

Comment by cremona created at 2009-01-07 11:56:11

Based on 3.2.3 without REST conversion


---

Attachment

trac_4900.patch should be identical to the previous one except that it is based on 3.2.3 vanilla without the sphinx/rest converted doctests.


---

Comment by roed created at 2009-01-24 14:39:29

Looks good to me.  One typo (combinarion).  I read through the paper and the code and didn't find any obvious errors.  I tried a few examples and the results seemed reasonable.


---

Comment by cremona created at 2009-01-24 17:44:54

Same as previous without the typo


---

Attachment

Replying to [comment:8 roed]:
> Looks good to me.  One typo (combinarion).  I read through the paper and the code and didn't find any obvious errors.  I tried a few examples and the results seemed reasonable.

Thanks.  I added a patch which corrects the typo, otherwise is identical to the last one.


---

Comment by mabshoff created at 2009-01-24 19:55:39

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 19:55:39

Merged trac_4900_typo.patch only in Sage 3.3.alpha2.

Cheers,

Michael
