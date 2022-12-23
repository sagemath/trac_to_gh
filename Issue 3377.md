# Issue 3377: [with patch, needs review] torsion for elliptic curves over number fields

Issue created by migration from https://trac.sagemath.org/ticket/3377

Original creator: wuthrich

Original creation time: 2008-06-06 17:16:06

Assignee: was


 
 It computes the torsion subgroup of an elliptic curve over a number field. The method is the usual idea: Find an upper bound for the order, by considering a few reductions of the elliptic curve at places of small residue fields. Then construct the points by finding roots of the division polynomials over the number field.

 This patch changes the file ell_number_field.py and adds a file ell_nf_torsion.py.


 (sorry, if I am doing something wrong here : I am a trac-newbie !)


---

Attachment


---

Comment by cremona created at 2008-06-06 18:48:26

I'll be very happy to review this over the weekend.  Thanks, Chris!


---

Comment by cremona created at 2008-06-07 16:20:18

Replacement for previous .py file (as a proper hg patch)


---

Attachment

1. I applied the first patch ok to 3.0.3.alpha1, then copied the second non-patch .py file into place, added it to the repository and re-exported it to make the second genuine patch attached (ell_nf_torsion.patch).

2. Doctests passed except for one error caused by a missing blank line at line 165 of ell_number_field.py.

3. The new file ell_nf_torsion.py and old file rational_torsion.py should probably be merged;  and certainly delete from the latter the lines

```
TODO:
    -- Torsion subgroups over number fields!
```


4. The function reduce() to reduce an e.c. at a place is very useful.  But it doesn't work for e.c.s defined over Q.  Rather than hack this code to work over Q I suggest adding a reduction method (function) in ell_rational_field.py just like the new one.  I can do this.

More to follow.... I am planning to add a further patch with some minor changes.


---

Comment by cremona created at 2008-06-09 08:28:20

Apply after previous


---

Attachment

The patch trac3377-extra1.patch adds some doctests (not yet complete) and a few minor changes to the code just for clarity.

   * I think that it might be cleaner to use the P.division_points() functionality recently added by William instead of using the division polynomials directly.  But when I tried this I hit a bug (#3383) so this idea will have to wait until that is fixed.  For example, where the p-torsion is cyclic (the usual case) one could just pick a p-torsion point and keep dividing it by p until that is no longer possible, to get the one generator.

   * The has_x() function would be useful as a member function of the generic elliptic curve class

   * The torsion_bound() function is perhaps more naturally a member of the ell_number_field  class?

   * Is the intention for this to replace the code in rational_torsion.py?  That is not clear.  I would say that there should be special code for the rational field, but that the two cases could be included in the same file;  however that would need rewriting the class definitions a bit since at present the same class name is used in both files.  It would work fine to have one class  EllipticCurveTorsionSubgroup whose constructor used different code depending on whether the base_ring was or was not QQ.


---

Attachment


---

Comment by wuthrich created at 2008-07-10 13:59:06

trac3377.extra2.patch has to be applied after trac3377-extra1.patch

It corrects .div to .quo_rem, since it seems that the .div no longer exists for these polynomials.


---

Attachment


---

Comment by cremona created at 2008-08-31 11:43:38

Another patch attached (trac3377.extra3.patch) -- sorry to do this so late in the release cycle, this can wait until the next one after 3.1.2 unless there's a quick review.

This patch adds quite a lot of new functionality as well as refactoring what was done already.  Apply all the patches in order (omit the one whose name ends .py) to 3.1.2.alpha2 or later.  (It will not apply to 3.1.1 unless the division-polynomials patches are applied first so best to use 3.1.2.alpha2).  I tested that this does work and all tests in sage.schemes.elliptic_curves pass.

In the new patch I deleted the new file ell_nf_torsion.py and also the old file rational_torsion.py, replacing them with a new file ell_torsion.py which unifies the code for Q and number fields.

There's a new class EllipticCurvePoint_number_field derived from EllipticCurvePoint_field, and functions specific to number fields have been moved down there;  this class also handles points on curves over Q, for which there is a bit more functionality -- but the gap is closing!

I moved Chris's p-primary-torsion into ell_generic.py, as it does work more generally.  I also moved the torsion_bound function into ell_number_field.py since it can be used to determine whether points have finite order or not, and find their order, even if the full torsion_subgroup() function is not used.  The bound is cached.

In going over the code for points over number fields I have made several things work which only used to work over Q, such as period_lattice and elliptic_logarithm -- provided that one supplies a real embedding of the number field.  Precision issues are dealt with intelligently (I hope).  That required a function refine_embedding() which I put in sage.rings.number_field.numer_field.py.  At some point someone will implement period lattices and elliptic logs for complex (non-real) embeddings -- I know how to do the former using complex AGM, but have never worked out the latter.

There you are -- I changed the ticket's title to reflect the fact that a lot more than torsion is covered.  I would certainly like Chris to review this as he started it, but we need an independent 3rd party too, such as Nick Alexander?


---

Comment by wuthrich created at 2008-09-02 12:06:31

Great work. This patch contains quite a lot of things and it should be reviewed carefully and independently, I agree.

I ran into the following problem, which is probably unrelated to this.


```
E = EllipticCurve('37a1')
K = Qp(7,10)
EK = E.base_extend(K)
```


Then 

```
EK._p_primary_torsion_basis(3)
```

fails with

```
AttributeError: 'Polynomial_padic_flat' object has no attribute '__coeffs'
```


because this fails already

```
g = EK.division_polynomial_0(3)
g.roots()
```


Chris


---

Comment by cremona created at 2008-09-02 13:01:39

Thanks.  Alex Ghitza has agreed to review this too.  I'll look into why g.roots() fails for a p-adic polynomial.

By the way, there's no need to add me to the CC, since anyone who contributes to a ticket is automatically CC'd.


---

Comment by wuthrich created at 2008-09-02 13:18:50

> By the way, there's no need to add me to the CC,
> since anyone who contributes to a ticket is automatically CC'd. 

Oh I didn't know. So you are saying I should get your posts cc'd ? i don't !??


---

Comment by mabshoff created at 2008-09-02 13:22:28

Replying to [comment:9 wuthrich]:
> > By the way, there's no need to add me to the CC,
> > since anyone who contributes to a ticket is automatically CC'd. 
> 
> Oh I didn't know. So you are saying I should get your posts cc'd ? i don't !??

Chris,

in "Settings" you can add an email address for your account that is used. In case you did that already you should get emails from all comments by anybody commenting on any ticket you are involved in. If it does not work let me know.

If you want to add people to the CC field it is sufficient to add their trac account name, i.e. "cremona" would work here.

Cheers,

Michael


---

Comment by wuthrich created at 2008-09-02 13:28:21

ok i got it, thanks.


---

Comment by cremona created at 2008-09-02 13:38:23

Replying to [comment:8 cremona]:
> Thanks.  Alex Ghitza has agreed to review this too.  I'll look into why g.roots() fails for a p-adic polynomial.
> 

This is now trac # 4038.


---

Attachment

apply only this patch


---

Comment by AlexGhitza created at 2008-09-03 03:11:53

Chris and John,

This is good stuff.  I was having trouble looking at the changes over all the different patches, so I folded all your patches into one.  While reading the code, I made a number of minor changes, described below:

1. file: number_field.py, function refine_embedding(): added a doctest

2. file: ell_number_field.py, function reduction(): added a type check to throw an exception if the parameter place is not a fractional ideal of K.  As an added bonus, one can now do E.reduction(2*i+3) and the function automatically makes 2*i+3 into the appropriate fractional ideal

3. file: ell_point.py, function _divide_out(): added doctests

4. various typos in various files (some of them predating these patches)

CONCLUSION: apply only the last patch (3377-torsion_nf.patch); credit goes to Chris Wuthrich and John Cremona


---

Comment by mabshoff created at 2008-09-03 07:20:20

I am seeing two doctest failures on 3.1.2.alpha4+three merged patches:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.rc0$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc0/tmp/ell_point.py", line 946:
    sage: e1 <= e(P[0]) <= e2 < e3
Expected:
    True
Got:
    False
**********************************************************************
```

And some numerical noise it seems:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.rc0$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc0/tmp/ell_number_field.py", line 1123:
    sage: L.basis()
Expected:
    (4.13107185270501681, -2.06553592635250840 + 0.988630424469107767*I)
Got:
    (4.13107185270501680, -2.06553592635250840 + 0.988630424469107767*I)
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.rc0/tmp/ell_number_field.py", line 1125:
    sage: L.basis(prec=75)
Expected:
    (4.131071852705016774309696920,
    -2.065535926352508387154848460 + 0.9886304244691077723690104516*I)
Got:
    (4.1310718527050167743096969215298790187, -2.0655359263525083871548484607649395093 + 0.98863042446910777236901045157674201375*I)
**********************************************************************
```



---

Comment by AlexGhitza created at 2008-09-03 07:52:46

I cannot reproduce any of these in my pristine 3.1.2.alpha4 (on 32bit ubuntu).

AFAIK (i.e. trac tells me) that the only patches merged in rc0 so far are #4043 (which has no way of interacting with this) and #3885.  I applied #3885 to my alpha4, then the patch here, and I'm still not getting any of these failures.

So I don't know what's going on.


---

Comment by cremona created at 2008-09-03 08:32:49

Many thanks to Alex for his review, his additions, and for rolling all our patches into one -- something I avoid doing since I always mess it up.

I'll try out his new single patch and see if I can sort out mabshoff's issues.


---

Attachment

Alex's patch applies fine to 3.1.2.alpha4.  I get the same doctest issues as Michael on a 64-bit machine.  Both are fixed in 3377-torsion_nf-1.patch.

In the first e1 <= e(P[0]) <= e2 < e3 is really true since e(P[0])==e2==-1 but rounding error caused e(P[0]) <= e2 to give false sometimes.  I fixed this by checking it differently.

In the second it's just numerical fuzz in the last decimal place, so I replces the last 3 digits by ... in the doctest.

The result passes all doctests in sage.schemes.elliptic_curves on both 32-bit and 64-bit machines.  I would not be that surprised if on some other machines we saw more of the same, though:  several bits of the patches are about computing some numbers to arbitrary precision, so I did want to include some decimal numbers in the output, and I have not (sorry) gone through each and every one replacing the final digits by dots.


---

Comment by AlexGhitza created at 2008-09-03 12:12:19

This looks good and passes all tests on my machine.

One should apply 3377-torsion_nf.patch followed by 3377-torsion_nf-1.patch.


---

Comment by mabshoff created at 2008-09-03 16:13:07

Merged 3377-torsion_nf.patch and 3377-torsion_nf-1.patch in Sage 3.1.2.rc0. Now everything works for me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-03 16:13:07

Resolution: fixed
