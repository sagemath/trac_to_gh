# Issue 3377: [with patch, needs review] torsion for elliptic curves over number fields

archive/issues_003377.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n \n It computes the torsion subgroup of an elliptic curve over a number field. The method is the usual idea: Find an upper bound for the order, by considering a few reductions of the elliptic curve at places of small residue fields. Then construct the points by finding roots of the division polynomials over the number field.\n\n This patch changes the file ell_number_field.py and adds a file ell_nf_torsion.py.\n\n\n (sorry, if I am doing something wrong here : I am a trac-newbie !)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3377\n\n",
    "created_at": "2008-06-06T17:16:06Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] torsion for elliptic curves over number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3377",
    "user": "@categorie"
}
```
Assignee: @williamstein


 
 It computes the torsion subgroup of an elliptic curve over a number field. The method is the usual idea: Find an upper bound for the order, by considering a few reductions of the elliptic curve at places of small residue fields. Then construct the points by finding roots of the division polynomials over the number field.

 This patch changes the file ell_number_field.py and adds a file ell_nf_torsion.py.


 (sorry, if I am doing something wrong here : I am a trac-newbie !)

Issue created by migration from https://trac.sagemath.org/ticket/3377





---

archive/issue_comments_023626.json:
```json
{
    "body": "Attachment [ell_nf_torsion.py](tarball://root/attachments/some-uuid/ticket3377/ell_nf_torsion.py) by @categorie created at 2008-06-06 17:17:18",
    "created_at": "2008-06-06T17:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23626",
    "user": "@categorie"
}
```

Attachment [ell_nf_torsion.py](tarball://root/attachments/some-uuid/ticket3377/ell_nf_torsion.py) by @categorie created at 2008-06-06 17:17:18



---

archive/issue_comments_023627.json:
```json
{
    "body": "I'll be very happy to review this over the weekend.  Thanks, Chris!",
    "created_at": "2008-06-06T18:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23627",
    "user": "@JohnCremona"
}
```

I'll be very happy to review this over the weekend.  Thanks, Chris!



---

archive/issue_comments_023628.json:
```json
{
    "body": "Replacement for previous .py file (as a proper hg patch)",
    "created_at": "2008-06-07T16:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23628",
    "user": "@JohnCremona"
}
```

Replacement for previous .py file (as a proper hg patch)



---

archive/issue_comments_023629.json:
```json
{
    "body": "Attachment [ell_nf_torsion.patch](tarball://root/attachments/some-uuid/ticket3377/ell_nf_torsion.patch) by @JohnCremona created at 2008-06-07 16:39:23\n\n1. I applied the first patch ok to 3.0.3.alpha1, then copied the second non-patch .py file into place, added it to the repository and re-exported it to make the second genuine patch attached (ell_nf_torsion.patch).\n\n2. Doctests passed except for one error caused by a missing blank line at line 165 of ell_number_field.py.\n\n3. The new file ell_nf_torsion.py and old file rational_torsion.py should probably be merged;  and certainly delete from the latter the lines\n\n```\nTODO:\n    -- Torsion subgroups over number fields!\n```\n\n\n4. The function reduce() to reduce an e.c. at a place is very useful.  But it doesn't work for e.c.s defined over Q.  Rather than hack this code to work over Q I suggest adding a reduction method (function) in ell_rational_field.py just like the new one.  I can do this.\n\nMore to follow.... I am planning to add a further patch with some minor changes.",
    "created_at": "2008-06-07T16:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23629",
    "user": "@JohnCremona"
}
```

Attachment [ell_nf_torsion.patch](tarball://root/attachments/some-uuid/ticket3377/ell_nf_torsion.patch) by @JohnCremona created at 2008-06-07 16:39:23

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

archive/issue_comments_023630.json:
```json
{
    "body": "Apply after previous",
    "created_at": "2008-06-09T08:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23630",
    "user": "@JohnCremona"
}
```

Apply after previous



---

archive/issue_comments_023631.json:
```json
{
    "body": "Attachment [trac3377-extra1.patch](tarball://root/attachments/some-uuid/ticket3377/trac3377-extra1.patch) by @JohnCremona created at 2008-06-09 08:29:35\n\nThe patch trac3377-extra1.patch adds some doctests (not yet complete) and a few minor changes to the code just for clarity.\n\n* I think that it might be cleaner to use the P.division_points() functionality recently added by William instead of using the division polynomials directly.  But when I tried this I hit a bug (#3383) so this idea will have to wait until that is fixed.  For example, where the p-torsion is cyclic (the usual case) one could just pick a p-torsion point and keep dividing it by p until that is no longer possible, to get the one generator.\n\n* The has_x() function would be useful as a member function of the generic elliptic curve class\n\n* The torsion_bound() function is perhaps more naturally a member of the ell_number_field  class?\n\n* Is the intention for this to replace the code in rational_torsion.py?  That is not clear.  I would say that there should be special code for the rational field, but that the two cases could be included in the same file;  however that would need rewriting the class definitions a bit since at present the same class name is used in both files.  It would work fine to have one class  EllipticCurveTorsionSubgroup whose constructor used different code depending on whether the base_ring was or was not QQ.",
    "created_at": "2008-06-09T08:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23631",
    "user": "@JohnCremona"
}
```

Attachment [trac3377-extra1.patch](tarball://root/attachments/some-uuid/ticket3377/trac3377-extra1.patch) by @JohnCremona created at 2008-06-09 08:29:35

The patch trac3377-extra1.patch adds some doctests (not yet complete) and a few minor changes to the code just for clarity.

* I think that it might be cleaner to use the P.division_points() functionality recently added by William instead of using the division polynomials directly.  But when I tried this I hit a bug (#3383) so this idea will have to wait until that is fixed.  For example, where the p-torsion is cyclic (the usual case) one could just pick a p-torsion point and keep dividing it by p until that is no longer possible, to get the one generator.

* The has_x() function would be useful as a member function of the generic elliptic curve class

* The torsion_bound() function is perhaps more naturally a member of the ell_number_field  class?

* Is the intention for this to replace the code in rational_torsion.py?  That is not clear.  I would say that there should be special code for the rational field, but that the two cases could be included in the same file;  however that would need rewriting the class definitions a bit since at present the same class name is used in both files.  It would work fine to have one class  EllipticCurveTorsionSubgroup whose constructor used different code depending on whether the base_ring was or was not QQ.



---

archive/issue_comments_023632.json:
```json
{
    "body": "Attachment [trac3377.extra2.patch](tarball://root/attachments/some-uuid/ticket3377/trac3377.extra2.patch) by @categorie created at 2008-07-10 13:55:35",
    "created_at": "2008-07-10T13:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23632",
    "user": "@categorie"
}
```

Attachment [trac3377.extra2.patch](tarball://root/attachments/some-uuid/ticket3377/trac3377.extra2.patch) by @categorie created at 2008-07-10 13:55:35



---

archive/issue_comments_023633.json:
```json
{
    "body": "trac3377.extra2.patch has to be applied after trac3377-extra1.patch\n\nIt corrects .div to .quo_rem, since it seems that the .div no longer exists for these polynomials.",
    "created_at": "2008-07-10T13:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23633",
    "user": "@categorie"
}
```

trac3377.extra2.patch has to be applied after trac3377-extra1.patch

It corrects .div to .quo_rem, since it seems that the .div no longer exists for these polynomials.



---

archive/issue_comments_023634.json:
```json
{
    "body": "Attachment [trac3377.extra3.patch](tarball://root/attachments/some-uuid/ticket3377/trac3377.extra3.patch) by @JohnCremona created at 2008-08-31 11:29:43",
    "created_at": "2008-08-31T11:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23634",
    "user": "@JohnCremona"
}
```

Attachment [trac3377.extra3.patch](tarball://root/attachments/some-uuid/ticket3377/trac3377.extra3.patch) by @JohnCremona created at 2008-08-31 11:29:43



---

archive/issue_comments_023635.json:
```json
{
    "body": "Another patch attached (trac3377.extra3.patch) -- sorry to do this so late in the release cycle, this can wait until the next one after 3.1.2 unless there's a quick review.\n\nThis patch adds quite a lot of new functionality as well as refactoring what was done already.  Apply all the patches in order (omit the one whose name ends .py) to 3.1.2.alpha2 or later.  (It will not apply to 3.1.1 unless the division-polynomials patches are applied first so best to use 3.1.2.alpha2).  I tested that this does work and all tests in sage.schemes.elliptic_curves pass.\n\nIn the new patch I deleted the new file ell_nf_torsion.py and also the old file rational_torsion.py, replacing them with a new file ell_torsion.py which unifies the code for Q and number fields.\n\nThere's a new class EllipticCurvePoint_number_field derived from EllipticCurvePoint_field, and functions specific to number fields have been moved down there;  this class also handles points on curves over Q, for which there is a bit more functionality -- but the gap is closing!\n\nI moved Chris's p-primary-torsion into ell_generic.py, as it does work more generally.  I also moved the torsion_bound function into ell_number_field.py since it can be used to determine whether points have finite order or not, and find their order, even if the full torsion_subgroup() function is not used.  The bound is cached.\n\nIn going over the code for points over number fields I have made several things work which only used to work over Q, such as period_lattice and elliptic_logarithm -- provided that one supplies a real embedding of the number field.  Precision issues are dealt with intelligently (I hope).  That required a function refine_embedding() which I put in sage.rings.number_field.numer_field.py.  At some point someone will implement period lattices and elliptic logs for complex (non-real) embeddings -- I know how to do the former using complex AGM, but have never worked out the latter.\n\nThere you are -- I changed the ticket's title to reflect the fact that a lot more than torsion is covered.  I would certainly like Chris to review this as he started it, but we need an independent 3rd party too, such as Nick Alexander?",
    "created_at": "2008-08-31T11:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23635",
    "user": "@JohnCremona"
}
```

Another patch attached (trac3377.extra3.patch) -- sorry to do this so late in the release cycle, this can wait until the next one after 3.1.2 unless there's a quick review.

This patch adds quite a lot of new functionality as well as refactoring what was done already.  Apply all the patches in order (omit the one whose name ends .py) to 3.1.2.alpha2 or later.  (It will not apply to 3.1.1 unless the division-polynomials patches are applied first so best to use 3.1.2.alpha2).  I tested that this does work and all tests in sage.schemes.elliptic_curves pass.

In the new patch I deleted the new file ell_nf_torsion.py and also the old file rational_torsion.py, replacing them with a new file ell_torsion.py which unifies the code for Q and number fields.

There's a new class EllipticCurvePoint_number_field derived from EllipticCurvePoint_field, and functions specific to number fields have been moved down there;  this class also handles points on curves over Q, for which there is a bit more functionality -- but the gap is closing!

I moved Chris's p-primary-torsion into ell_generic.py, as it does work more generally.  I also moved the torsion_bound function into ell_number_field.py since it can be used to determine whether points have finite order or not, and find their order, even if the full torsion_subgroup() function is not used.  The bound is cached.

In going over the code for points over number fields I have made several things work which only used to work over Q, such as period_lattice and elliptic_logarithm -- provided that one supplies a real embedding of the number field.  Precision issues are dealt with intelligently (I hope).  That required a function refine_embedding() which I put in sage.rings.number_field.numer_field.py.  At some point someone will implement period lattices and elliptic logs for complex (non-real) embeddings -- I know how to do the former using complex AGM, but have never worked out the latter.

There you are -- I changed the ticket's title to reflect the fact that a lot more than torsion is covered.  I would certainly like Chris to review this as he started it, but we need an independent 3rd party too, such as Nick Alexander?



---

archive/issue_comments_023636.json:
```json
{
    "body": "Great work. This patch contains quite a lot of things and it should be reviewed carefully and independently, I agree.\n\nI ran into the following problem, which is probably unrelated to this.\n\n\n```\nE = EllipticCurve('37a1')\nK = Qp(7,10)\nEK = E.base_extend(K)\n```\n\n\nThen \n\n```\nEK._p_primary_torsion_basis(3)\n```\n\nfails with\n\n```\nAttributeError: 'Polynomial_padic_flat' object has no attribute '__coeffs'\n```\n\n\nbecause this fails already\n\n```\ng = EK.division_polynomial_0(3)\ng.roots()\n```\n\n\nChris",
    "created_at": "2008-09-02T12:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23636",
    "user": "@categorie"
}
```

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

archive/issue_comments_023637.json:
```json
{
    "body": "Thanks.  Alex Ghitza has agreed to review this too.  I'll look into why g.roots() fails for a p-adic polynomial.\n\nBy the way, there's no need to add me to the CC, since anyone who contributes to a ticket is automatically CC'd.",
    "created_at": "2008-09-02T13:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23637",
    "user": "@JohnCremona"
}
```

Thanks.  Alex Ghitza has agreed to review this too.  I'll look into why g.roots() fails for a p-adic polynomial.

By the way, there's no need to add me to the CC, since anyone who contributes to a ticket is automatically CC'd.



---

archive/issue_comments_023638.json:
```json
{
    "body": "> By the way, there's no need to add me to the CC,\n> since anyone who contributes to a ticket is automatically CC'd. \n\nOh I didn't know. So you are saying I should get your posts cc'd ? i don't !??",
    "created_at": "2008-09-02T13:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23638",
    "user": "@categorie"
}
```

> By the way, there's no need to add me to the CC,
> since anyone who contributes to a ticket is automatically CC'd. 

Oh I didn't know. So you are saying I should get your posts cc'd ? i don't !??



---

archive/issue_comments_023639.json:
```json
{
    "body": "Replying to [comment:9 wuthrich]:\n> > By the way, there's no need to add me to the CC,\n> > since anyone who contributes to a ticket is automatically CC'd. \n> \n> Oh I didn't know. So you are saying I should get your posts cc'd ? i don't !??\n\nChris,\n\nin \"Settings\" you can add an email address for your account that is used. In case you did that already you should get emails from all comments by anybody commenting on any ticket you are involved in. If it does not work let me know.\n\nIf you want to add people to the CC field it is sufficient to add their trac account name, i.e. \"cremona\" would work here.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-02T13:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23639",
    "user": "mabshoff"
}
```

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

archive/issue_comments_023640.json:
```json
{
    "body": "ok i got it, thanks.",
    "created_at": "2008-09-02T13:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23640",
    "user": "@categorie"
}
```

ok i got it, thanks.



---

archive/issue_comments_023641.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> Thanks.  Alex Ghitza has agreed to review this too.  I'll look into why g.roots() fails for a p-adic polynomial.\n> \n\nThis is now trac # 4038.",
    "created_at": "2008-09-02T13:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23641",
    "user": "@JohnCremona"
}
```

Replying to [comment:8 cremona]:
> Thanks.  Alex Ghitza has agreed to review this too.  I'll look into why g.roots() fails for a p-adic polynomial.
> 

This is now trac # 4038.



---

archive/issue_comments_023642.json:
```json
{
    "body": "Attachment [3377-torsion_nf.patch](tarball://root/attachments/some-uuid/ticket3377/3377-torsion_nf.patch) by @aghitza created at 2008-09-03 03:09:36\n\napply only this patch",
    "created_at": "2008-09-03T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23642",
    "user": "@aghitza"
}
```

Attachment [3377-torsion_nf.patch](tarball://root/attachments/some-uuid/ticket3377/3377-torsion_nf.patch) by @aghitza created at 2008-09-03 03:09:36

apply only this patch



---

archive/issue_comments_023643.json:
```json
{
    "body": "Chris and John,\n\nThis is good stuff.  I was having trouble looking at the changes over all the different patches, so I folded all your patches into one.  While reading the code, I made a number of minor changes, described below:\n\n1. file: number_field.py, function refine_embedding(): added a doctest\n\n2. file: ell_number_field.py, function reduction(): added a type check to throw an exception if the parameter place is not a fractional ideal of K.  As an added bonus, one can now do E.reduction(2*i+3) and the function automatically makes 2*i+3 into the appropriate fractional ideal\n\n3. file: ell_point.py, function _divide_out(): added doctests\n\n4. various typos in various files (some of them predating these patches)\n\nCONCLUSION: apply only the last patch (3377-torsion_nf.patch); credit goes to Chris Wuthrich and John Cremona",
    "created_at": "2008-09-03T03:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23643",
    "user": "@aghitza"
}
```

Chris and John,

This is good stuff.  I was having trouble looking at the changes over all the different patches, so I folded all your patches into one.  While reading the code, I made a number of minor changes, described below:

1. file: number_field.py, function refine_embedding(): added a doctest

2. file: ell_number_field.py, function reduction(): added a type check to throw an exception if the parameter place is not a fractional ideal of K.  As an added bonus, one can now do E.reduction(2*i+3) and the function automatically makes 2*i+3 into the appropriate fractional ideal

3. file: ell_point.py, function _divide_out(): added doctests

4. various typos in various files (some of them predating these patches)

CONCLUSION: apply only the last patch (3377-torsion_nf.patch); credit goes to Chris Wuthrich and John Cremona



---

archive/issue_comments_023644.json:
```json
{
    "body": "I am seeing two doctest failures on 3.1.2.alpha4+three merged patches:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.rc0$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc0/tmp/ell_point.py\", line 946:\n    sage: e1 <= e(P[0]) <= e2 < e3\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n\nAnd some numerical noise it seems:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.rc0$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc0/tmp/ell_number_field.py\", line 1123:\n    sage: L.basis()\nExpected:\n    (4.13107185270501681, -2.06553592635250840 + 0.988630424469107767*I)\nGot:\n    (4.13107185270501680, -2.06553592635250840 + 0.988630424469107767*I)\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.rc0/tmp/ell_number_field.py\", line 1125:\n    sage: L.basis(prec=75)\nExpected:\n    (4.131071852705016774309696920,\n    -2.065535926352508387154848460 + 0.9886304244691077723690104516*I)\nGot:\n    (4.1310718527050167743096969215298790187, -2.0655359263525083871548484607649395093 + 0.98863042446910777236901045157674201375*I)\n**********************************************************************\n```\n",
    "created_at": "2008-09-03T07:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23644",
    "user": "mabshoff"
}
```

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

archive/issue_comments_023645.json:
```json
{
    "body": "I cannot reproduce any of these in my pristine 3.1.2.alpha4 (on 32bit ubuntu).\n\nAFAIK (i.e. trac tells me) that the only patches merged in rc0 so far are #4043 (which has no way of interacting with this) and #3885.  I applied #3885 to my alpha4, then the patch here, and I'm still not getting any of these failures.\n\nSo I don't know what's going on.",
    "created_at": "2008-09-03T07:52:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23645",
    "user": "@aghitza"
}
```

I cannot reproduce any of these in my pristine 3.1.2.alpha4 (on 32bit ubuntu).

AFAIK (i.e. trac tells me) that the only patches merged in rc0 so far are #4043 (which has no way of interacting with this) and #3885.  I applied #3885 to my alpha4, then the patch here, and I'm still not getting any of these failures.

So I don't know what's going on.



---

archive/issue_comments_023646.json:
```json
{
    "body": "Many thanks to Alex for his review, his additions, and for rolling all our patches into one -- something I avoid doing since I always mess it up.\n\nI'll try out his new single patch and see if I can sort out mabshoff's issues.",
    "created_at": "2008-09-03T08:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23646",
    "user": "@JohnCremona"
}
```

Many thanks to Alex for his review, his additions, and for rolling all our patches into one -- something I avoid doing since I always mess it up.

I'll try out his new single patch and see if I can sort out mabshoff's issues.



---

archive/issue_comments_023647.json:
```json
{
    "body": "Attachment [3377-torsion_nf-1.patch](tarball://root/attachments/some-uuid/ticket3377/3377-torsion_nf-1.patch) by @JohnCremona created at 2008-09-03 09:47:21\n\nAlex's patch applies fine to 3.1.2.alpha4.  I get the same doctest issues as Michael on a 64-bit machine.  Both are fixed in 3377-torsion_nf-1.patch.\n\nIn the first e1 <= e(P[0]) <= e2 < e3 is really true since e(P[0])==e2==-1 but rounding error caused e(P[0]) <= e2 to give false sometimes.  I fixed this by checking it differently.\n\nIn the second it's just numerical fuzz in the last decimal place, so I replces the last 3 digits by ... in the doctest.\n\nThe result passes all doctests in sage.schemes.elliptic_curves on both 32-bit and 64-bit machines.  I would not be that surprised if on some other machines we saw more of the same, though:  several bits of the patches are about computing some numbers to arbitrary precision, so I did want to include some decimal numbers in the output, and I have not (sorry) gone through each and every one replacing the final digits by dots.",
    "created_at": "2008-09-03T09:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23647",
    "user": "@JohnCremona"
}
```

Attachment [3377-torsion_nf-1.patch](tarball://root/attachments/some-uuid/ticket3377/3377-torsion_nf-1.patch) by @JohnCremona created at 2008-09-03 09:47:21

Alex's patch applies fine to 3.1.2.alpha4.  I get the same doctest issues as Michael on a 64-bit machine.  Both are fixed in 3377-torsion_nf-1.patch.

In the first e1 <= e(P[0]) <= e2 < e3 is really true since e(P[0])==e2==-1 but rounding error caused e(P[0]) <= e2 to give false sometimes.  I fixed this by checking it differently.

In the second it's just numerical fuzz in the last decimal place, so I replces the last 3 digits by ... in the doctest.

The result passes all doctests in sage.schemes.elliptic_curves on both 32-bit and 64-bit machines.  I would not be that surprised if on some other machines we saw more of the same, though:  several bits of the patches are about computing some numbers to arbitrary precision, so I did want to include some decimal numbers in the output, and I have not (sorry) gone through each and every one replacing the final digits by dots.



---

archive/issue_comments_023648.json:
```json
{
    "body": "This looks good and passes all tests on my machine.\n\nOne should apply 3377-torsion_nf.patch followed by 3377-torsion_nf-1.patch.",
    "created_at": "2008-09-03T12:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23648",
    "user": "@aghitza"
}
```

This looks good and passes all tests on my machine.

One should apply 3377-torsion_nf.patch followed by 3377-torsion_nf-1.patch.



---

archive/issue_comments_023649.json:
```json
{
    "body": "Merged 3377-torsion_nf.patch and 3377-torsion_nf-1.patch in Sage 3.1.2.rc0. Now everything works for me.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-03T16:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23649",
    "user": "mabshoff"
}
```

Merged 3377-torsion_nf.patch and 3377-torsion_nf-1.patch in Sage 3.1.2.rc0. Now everything works for me.

Cheers,

Michael



---

archive/issue_comments_023650.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-03T16:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3377#issuecomment-23650",
    "user": "mabshoff"
}
```

Resolution: fixed
