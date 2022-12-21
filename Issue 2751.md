# Issue 2751: [with patch, needs review] multivariate polynomials i_homogeneous

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-04-01 13:18:31

Assignee: malb




---

Attachment


---

Comment by jbmohler created at 2008-04-02 16:53:23

I observe that the doc-tests do not actually run this code due to the fact that is_homogeneous is overridden (as it should be) in MPolynomial_libsingular.  Indeed, the only way I can find to actually run this code in normal use is:

```
sage: R.<x,y>=BooleanPolynomialRing(2)
sage: x.is_homogeneous()
...
<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.pbori.BooleanMonomial' object has no attribute 'degree'
```

and that fails.

I am of two minds:

 *1) This method should be implemented special for the BooleanPolynomial and the generic implementation left unneeded and unwritten

 *2) Or, the above bug should be fixed.

My preference is choice 1 since it seems it is generally possible to implement this function in a much faster way when you know the data layout.

Or, is there some use of this function that I'm missing?


---

Comment by malb created at 2008-04-02 17:12:14

That means that I forgot to submit the degree method, sorry bout that. I think both (1) and (2) should be implemented such that there are fall-back default implementations for most stuff.


---

Attachment


---

Comment by malb created at 2008-04-04 11:35:36

The attached patch addresses Joel's critique.


---

Comment by jbmohler created at 2008-04-04 16:37:04

On the basis of what I see in the patch, I think I give a positive review.  However, the patch doesn't apply cleanly and I'm not at all sure what was intended with the unapplied hunk.


---

Comment by malb created at 2008-04-04 16:44:06

Replying to [comment:5 jbmohler]:
> However, the patch doesn't apply cleanly and I'm not at all sure what was intended 
> with the unapplied hunk.

What version are you using 2.11 or 3.0.alpha0?


---

Comment by mabshoff created at 2008-04-04 17:06:18

The do apply cleanly [the second patch with slight offsets] to my tree:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha1/devel/sage$ patch -p1  < trac_2751_mpoly_is_homogenous.patch
patching file sage/rings/polynomial/multi_polynomial.pyx
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha1/devel/sage$ patch -p1  < trac_2751_mpoly_is_homogenous_addon.patch
patching file sage/rings/polynomial/multi_polynomial.pyx
patching file sage/rings/polynomial/pbori.pyx
Hunk #1 succeeded at 1432 (offset -120 lines).
Hunk #2 succeeded at 1443 (offset -120 lines).
```


All doctests pass. Is that enough for a positive review from jbmoehler?

Cheers,

Michael


---

Comment by jbmohler created at 2008-04-04 20:37:02

Yes, passing doc-tests are sufficient (I was using 2.11) (I wasn't aware that 3.0 and gotten that far already -- sorry about that)


---

Attachment


---

Comment by mabshoff created at 2008-04-04 20:59:29

Re 2751-2.patch:

```
[22:22] <mhansen> mabshoff: I got a doctest failure with 2751.
[22:22] <mabshoff> ok. Which one?
[22:23] <mhansen> The second patch -- P.<x,y> = PolynomialBooleanRing() fails.
[22:23] <mabshoff> That depends on another patch I merged.
[22:24] <mhansen> Ahh, I see.  Then ignore my new patch.
[22:24] <mabshoff> There is a simplification patch for the PolyBoRi constructor
[22:24] <mabshoff> :)
[22:24] <mhansen> Yep, that should be done.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-04-04 22:15:17

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-04 22:15:17

Resolution: fixed
