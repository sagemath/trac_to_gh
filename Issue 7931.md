# Issue 7931: Improved nth root for finite fields and integer_mods

archive/issues_007931.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  robertwb\n\nKeywords: finite fields, nth root\n\nImplements an algorithm described in \n{{\nJohnston, Anna M. A generalized qth root algorithm. \nProceedings of the tenth annual ACM-SIAM symposium on Discrete algorithms. \nBaltimore, 1999: pp 929-930.\n}}}\n\nThis means we can take nth roots with large n, since we no longer need to create the polynomial x^n-a.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7931\n\n",
    "created_at": "2010-01-14T15:27:30Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Improved nth root for finite fields and integer_mods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7931",
    "user": "roed"
}
```
Assignee: AlexGhitza

CC:  robertwb

Keywords: finite fields, nth root

Implements an algorithm described in 
{{
Johnston, Anna M. A generalized qth root algorithm. 
Proceedings of the tenth annual ACM-SIAM symposium on Discrete algorithms. 
Baltimore, 1999: pp 929-930.
}}}

This means we can take nth roots with large n, since we no longer need to create the polynomial x^n-a.

Issue created by migration from https://trac.sagemath.org/ticket/7931





---

archive/issue_comments_069049.json:
```json
{
    "body": "Attachment [7931.patch](tarball://root/attachments/some-uuid/ticket7931/7931.patch) by roed created at 2010-01-14 15:30:02",
    "created_at": "2010-01-14T15:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69049",
    "user": "roed"
}
```

Attachment [7931.patch](tarball://root/attachments/some-uuid/ticket7931/7931.patch) by roed created at 2010-01-14 15:30:02



---

archive/issue_comments_069050.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-14T15:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69050",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069051.json:
```json
{
    "body": "Is there something I am missing?\n\n```\nsage: K = GF(31)\nsage: b=K(22)^200\nsage: b.nth_root(200)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/virtual/scratch/rishi/sage-4.3.1.alpha2-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()\n\n/virtual/scratch/rishi/sage-4.3.1.alpha2-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod_abstract.nth_root (sage/rings/integer_mod.c:11446)()\n\nValueError: no nth root\nsage:\n\n```\n",
    "created_at": "2010-01-21T17:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69051",
    "user": "rishi"
}
```

Is there something I am missing?

```
sage: K = GF(31)
sage: b=K(22)^200
sage: b.nth_root(200)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/virtual/scratch/rishi/sage-4.3.1.alpha2-sage.math.washington.edu-x86_64-Linux/<ipython console> in <module>()

/virtual/scratch/rishi/sage-4.3.1.alpha2-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod_abstract.nth_root (sage/rings/integer_mod.c:11446)()

ValueError: no nth root
sage:

```




---

archive/issue_comments_069052.json:
```json
{
    "body": "It looks to me as if the original code (now deleted) worked with finite field elements, while thie new code works with integer-mods.  That must surely mean that for non-prime finite fields there was something which worked, but now there isn't?  If I am right, it would be a good idea to allow the original code as a fall-back.",
    "created_at": "2010-01-24T18:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69052",
    "user": "cremona"
}
```

It looks to me as if the original code (now deleted) worked with finite field elements, while thie new code works with integer-mods.  That must surely mean that for non-prime finite fields there was something which worked, but now there isn't?  If I am right, it would be a good idea to allow the original code as a fall-back.



---

archive/issue_comments_069053.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-24T18:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69053",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069054.json:
```json
{
    "body": "Patch applies fine to 4.3.1 and tests pass, but I reproduced the example from rishi, so -- \"needs work\".",
    "created_at": "2010-01-24T18:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69054",
    "user": "cremona"
}
```

Patch applies fine to 4.3.1 and tests pass, but I reproduced the example from rishi, so -- "needs work".



---

archive/issue_comments_069055.json:
```json
{
    "body": "Attachment [7931_nth_root.patch](tarball://root/attachments/some-uuid/ticket7931/7931_nth_root.patch) by roed created at 2010-02-23 15:30:11\n\nShould fix the problem observed earlier",
    "created_at": "2010-02-23T15:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69055",
    "user": "roed"
}
```

Attachment [7931_nth_root.patch](tarball://root/attachments/some-uuid/ticket7931/7931_nth_root.patch) by roed created at 2010-02-23 15:30:11

Should fix the problem observed earlier



---

archive/issue_comments_069056.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-23T15:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69056",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069057.json:
```json
{
    "body": "David, should the 2nd patch be applied after the 1st one or alone?",
    "created_at": "2010-02-25T22:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69057",
    "user": "zimmerma"
}
```

David, should the 2nd patch be applied after the 1st one or alone?



---

archive/issue_comments_069058.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-25T22:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69058",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_069059.json:
```json
{
    "body": "Alone.  Sorry about that.",
    "created_at": "2010-02-25T23:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69059",
    "user": "roed"
}
```

Alone.  Sorry about that.



---

archive/issue_comments_069060.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-25T23:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69060",
    "user": "roed"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_069061.json:
```json
{
    "body": "Changing assignee from AlexGhitza to roed.",
    "created_at": "2010-02-25T23:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69061",
    "user": "roed"
}
```

Changing assignee from AlexGhitza to roed.



---

archive/issue_comments_069062.json:
```json
{
    "body": "Oops.  I made it depend on a bunch of other changes\n\n```\n8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> this patch\n```\n\n\nThe actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.",
    "created_at": "2010-02-25T23:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69062",
    "user": "roed"
}
```

Oops.  I made it depend on a bunch of other changes

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> this patch
```


The actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.



---

archive/issue_comments_069063.json:
```json
{
    "body": "> The actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.\n\nthat would be nice. Otherwise we can wait for the other patches to be reviewed.\nPaul",
    "created_at": "2010-02-26T08:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69063",
    "user": "zimmerma"
}
```

> The actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.

that would be nice. Otherwise we can wait for the other patches to be reviewed.
Paul



---

archive/issue_comments_069064.json:
```json
{
    "body": "Replying to [comment:8 roed]:\n> Oops.  I made it depend on a bunch of other changes\n> {{{\n> 8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> this patch\n> }}}\n> \n> The actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.\n\nJust so we have trac's help to see which of the dependencies have already been merged: this depends on #8218, #8332, #7880, #7883, #8333, #8334.",
    "created_at": "2010-06-05T00:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69064",
    "user": "AlexGhitza"
}
```

Replying to [comment:8 roed]:
> Oops.  I made it depend on a bunch of other changes
> {{{
> 8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> this patch
> }}}
> 
> The actual change is fairly small; I'll try to extract it out and get something based only on 4.3.3, but I won't be able to do that tonight.

Just so we have trac's help to see which of the dependencies have already been merged: this depends on #8218, #8332, #7880, #7883, #8333, #8334.



---

archive/issue_comments_069065.json:
```json
{
    "body": "Patch `7931_nth_root.patch` applies and builds fine and all doctests in `finite_rings` pass (with the dependencies installed); but I'm not terribly happy about the amount of code duplication that's going on -- the code added to `element_base` and `integer_mod` has about 30 lines that are virtually identical. Could it not be refactored to avoid this?",
    "created_at": "2010-09-27T10:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69065",
    "user": "davidloeffler"
}
```

Patch `7931_nth_root.patch` applies and builds fine and all doctests in `finite_rings` pass (with the dependencies installed); but I'm not terribly happy about the amount of code duplication that's going on -- the code added to `element_base` and `integer_mod` has about 30 lines that are virtually identical. Could it not be refactored to avoid this?



---

archive/issue_comments_069066.json:
```json
{
    "body": "I completely agree.  In the long run I want to change `FiniteFieldElement` to `FiniteRingElement` and make `IntegerMod_abstract` inherit from that.  The `nth_root` function on `FiniteRingElement` can then be modified to handle both cases.  An additional benefit of having such a common parent is that the finite field elements can then no longer require `p` prime (or `modulus` irreducible for that matter), which will be useful for p-adic extensions.  In fact, I want to modify the finite field element classes to use templates (a la `sage.rings.polynomial.polynomial_template`): then we can share common code between polynomials, finite fields and rings, and p-adic extension fields.  Coercions between them will be much easier and faster and it will make implementing extensions of extensions easier (which are necessary for p-adic extensions that are neither unramified nor totally ramified).\n\nThe first step though, of making `IntegerMod_abstract` inherit from `FiniteRingElement` caused compile-time bugs that I couldn't figure out and I gave up for the moment.\n\nSo currently their closest common superclass is `CommutativeRingElement`.  It didn't seem like a good idea to put the common `nth_root` code there, and there wasn't another obvious way to do it.  Any suggestions?",
    "created_at": "2010-09-27T17:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69066",
    "user": "roed"
}
```

I completely agree.  In the long run I want to change `FiniteFieldElement` to `FiniteRingElement` and make `IntegerMod_abstract` inherit from that.  The `nth_root` function on `FiniteRingElement` can then be modified to handle both cases.  An additional benefit of having such a common parent is that the finite field elements can then no longer require `p` prime (or `modulus` irreducible for that matter), which will be useful for p-adic extensions.  In fact, I want to modify the finite field element classes to use templates (a la `sage.rings.polynomial.polynomial_template`): then we can share common code between polynomials, finite fields and rings, and p-adic extension fields.  Coercions between them will be much easier and faster and it will make implementing extensions of extensions easier (which are necessary for p-adic extensions that are neither unramified nor totally ramified).

The first step though, of making `IntegerMod_abstract` inherit from `FiniteRingElement` caused compile-time bugs that I couldn't figure out and I gave up for the moment.

So currently their closest common superclass is `CommutativeRingElement`.  It didn't seem like a good idea to put the common `nth_root` code there, and there wasn't another obvious way to do it.  Any suggestions?



---

archive/issue_comments_069067.json:
```json
{
    "body": "Another problem with the current patch is that for large `n`, finding the factorization of the size of the unit group becomes a bottleneck.  There's a change in #8335 that  helps with this problem for finite fields of small characteristic by caching the factorization of p<sup>n</sup>-1 and using the Cunningham package at #7240 to speed up the computation in the first place.  Thematically it would make sense to backport it to this patch (which I've done already locally), but it makes this patch depend on #7240 (otherwise there are warnings printed when `_factor_cunningham` is used).  What do you think?",
    "created_at": "2010-09-27T17:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69067",
    "user": "roed"
}
```

Another problem with the current patch is that for large `n`, finding the factorization of the size of the unit group becomes a bottleneck.  There's a change in #8335 that  helps with this problem for finite fields of small characteristic by caching the factorization of p<sup>n</sup>-1 and using the Cunningham package at #7240 to speed up the computation in the first place.  Thematically it would make sense to backport it to this patch (which I've done already locally), but it makes this patch depend on #7240 (otherwise there are warnings printed when `_factor_cunningham` is used).  What do you think?



---

archive/issue_comments_069068.json:
```json
{
    "body": "Could one perhaps have an auxilliary helper function (not a class method) that both of the nth root methods call? This is not terribly elegant, but it solves the duplication issue.\n\nI'd argue for not making this patch depend on #7240, since that patch seems to be stalled at the moment.",
    "created_at": "2010-09-27T17:43:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69068",
    "user": "davidloeffler"
}
```

Could one perhaps have an auxilliary helper function (not a class method) that both of the nth root methods call? This is not terribly elegant, but it solves the duplication issue.

I'd argue for not making this patch depend on #7240, since that patch seems to be stalled at the moment.



---

archive/issue_comments_069069.json:
```json
{
    "body": "Attachment [7931_nth_root.2.patch](tarball://root/attachments/some-uuid/ticket7931/7931_nth_root.2.patch) by roed created at 2010-09-28 08:33:15\n\nApply just this patch",
    "created_at": "2010-09-28T08:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69069",
    "user": "roed"
}
```

Attachment [7931_nth_root.2.patch](tarball://root/attachments/some-uuid/ticket7931/7931_nth_root.2.patch) by roed created at 2010-09-28 08:33:15

Apply just this patch



---

archive/issue_comments_069070.json:
```json
{
    "body": "I factored out most of the common code, and backported a few changes from #8335.  It still doesn't depend on #7240.",
    "created_at": "2010-09-28T08:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69070",
    "user": "roed"
}
```

I factored out most of the common code, and backported a few changes from #8335.  It still doesn't depend on #7240.



---

archive/issue_comments_069071.json:
```json
{
    "body": "Apply on top of 7931_nth_root.2.patch; moves _nth_root_common to FiniteRingElement, a new superclass of IntegerMod_abstract and the finite field elements",
    "created_at": "2010-09-29T01:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69071",
    "user": "roed"
}
```

Apply on top of 7931_nth_root.2.patch; moves _nth_root_common to FiniteRingElement, a new superclass of IntegerMod_abstract and the finite field elements



---

archive/issue_comments_069072.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-09-29T08:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69072",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_069073.json:
```json
{
    "body": "Attachment [7931_common_superclass.patch](tarball://root/attachments/some-uuid/ticket7931/7931_common_superclass.patch) by zimmerma created at 2010-09-29 08:57:33\n\nI tried applying both patches in sage-4.6.alpha1, but got a failure when running sage -br:\n\n```\npython `which cython` --embed-positions --directive cdivision=True -I/tmp/sage-4.6.alpha1/devel/sage-7931 -o sage/rings/finite_rings/element_ntl_gf2e.cpp sage/rings/finite_rings/element_ntl_gf2e.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n        if PY_TYPE_CHECK(e, int) \\\n               or PY_TYPE_CHECK(e, long) or PY_TYPE_CHECK(e, Integer):\n            GF2E_conv_long(res.x,int(e))\n            return res\n\n        if PY_TYPE_CHECK(e, FiniteFieldElement) or \\\n                                             ^\n------------------------------------------------------------\n\n/tmp/sage-4.6.alpha1/devel/sage-7931/sage/rings/finite_rings/element_ntl_gf2e.pyx:515:46: undeclared name not builtin: FiniteFieldElement\nError running command, failed with status 256.\nsage: There was an error installing modified sage library code.\n```\n\nWhich version was used to produce the patches?\n\nPaul",
    "created_at": "2010-09-29T08:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69073",
    "user": "zimmerma"
}
```

Attachment [7931_common_superclass.patch](tarball://root/attachments/some-uuid/ticket7931/7931_common_superclass.patch) by zimmerma created at 2010-09-29 08:57:33

I tried applying both patches in sage-4.6.alpha1, but got a failure when running sage -br:

```
python `which cython` --embed-positions --directive cdivision=True -I/tmp/sage-4.6.alpha1/devel/sage-7931 -o sage/rings/finite_rings/element_ntl_gf2e.cpp sage/rings/finite_rings/element_ntl_gf2e.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...
        if PY_TYPE_CHECK(e, int) \
               or PY_TYPE_CHECK(e, long) or PY_TYPE_CHECK(e, Integer):
            GF2E_conv_long(res.x,int(e))
            return res

        if PY_TYPE_CHECK(e, FiniteFieldElement) or \
                                             ^
------------------------------------------------------------

/tmp/sage-4.6.alpha1/devel/sage-7931/sage/rings/finite_rings/element_ntl_gf2e.pyx:515:46: undeclared name not builtin: FiniteFieldElement
Error running command, failed with status 256.
sage: There was an error installing modified sage library code.
```

Which version was used to produce the patches?

Paul



---

archive/issue_comments_069074.json:
```json
{
    "body": "I realized that I should also apply the patches #7883 and #8334, which were included in\nsage-4.6.alpha2, but were not yet in sage-4.6.alpha1. However after importing #7883\nsuccessfully in sage-4.6.alpha1, importing #8334 gives:\n\n```\nsage: hg_sage.import_patch(\"/tmp/8333_8334_ALL-better_commit_string.patch\")\ncd \"/tmp/sage-4.6.alpha1/devel/sage\" && hg status\ncd \"/tmp/sage-4.6.alpha1/devel/sage\" && hg status\ncd \"/tmp/sage-4.6.alpha1/devel/sage\" && hg import   \"/tmp/8333_8334_ALL-better_commit_string.patch\"\napplying /tmp/8333_8334_ALL-better_commit_string.patch\npatching file sage/rings/ideal_monoid.py\nHunk #1 succeeded at 90 with fuzz 2 (offset 0 lines).\npatching file sage/rings/residue_field.pyx\nHunk #3 succeeded at 74 with fuzz 2 (offset 0 lines).\nHunk #15 FAILED at 624\n1 out of 36 hunks FAILED -- saving rejects to file sage/rings/residue_field.pyx.rej\nabort: patch failed to apply\n```\n\nand I'm stuck there. Maybe I should wait that sage-4.6.alpha2 is out.\n\nPaul",
    "created_at": "2010-09-29T09:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69074",
    "user": "zimmerma"
}
```

I realized that I should also apply the patches #7883 and #8334, which were included in
sage-4.6.alpha2, but were not yet in sage-4.6.alpha1. However after importing #7883
successfully in sage-4.6.alpha1, importing #8334 gives:

```
sage: hg_sage.import_patch("/tmp/8333_8334_ALL-better_commit_string.patch")
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg status
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg status
cd "/tmp/sage-4.6.alpha1/devel/sage" && hg import   "/tmp/8333_8334_ALL-better_commit_string.patch"
applying /tmp/8333_8334_ALL-better_commit_string.patch
patching file sage/rings/ideal_monoid.py
Hunk #1 succeeded at 90 with fuzz 2 (offset 0 lines).
patching file sage/rings/residue_field.pyx
Hunk #3 succeeded at 74 with fuzz 2 (offset 0 lines).
Hunk #15 FAILED at 624
1 out of 36 hunks FAILED -- saving rejects to file sage/rings/residue_field.pyx.rej
abort: patch failed to apply
```

and I'm stuck there. Maybe I should wait that sage-4.6.alpha2 is out.

Paul



---

archive/issue_comments_069075.json:
```json
{
    "body": "Ticket #8334 has some other dependencies -- they are listed on that ticket (Jeroen's comment 24). With those installed the patch applies fine, and all doctests in sage/rings pass (I'm running a full ptestlong cycle now), so I'm putting this back to \"needs_review\".\n\nBy the way, Mitesh has a lovely script [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2), which you can run on a clean 4.6.alpha1 build and it will download and apply all of the patches and spkgs so far merged.",
    "created_at": "2010-09-29T10:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69075",
    "user": "davidloeffler"
}
```

Ticket #8334 has some other dependencies -- they are listed on that ticket (Jeroen's comment 24). With those installed the patch applies fine, and all doctests in sage/rings pass (I'm running a full ptestlong cycle now), so I'm putting this back to "needs_review".

By the way, Mitesh has a lovely script [merger-4.6.alpha2](http://sage.math.washington.edu/home/release/sage-4.6.alpha2/merger-4.6.alpha2), which you can run on a clean 4.6.alpha1 build and it will download and apply all of the patches and spkgs so far merged.



---

archive/issue_comments_069076.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-29T10:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69076",
    "user": "davidloeffler"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_069077.json:
```json
{
    "body": "I tried Mitesh's script on my sage-4.6.alpha1 build (after sage -b main), then I applied the two\npatches from that ticket, but I still get the same error as in comment 16.\n\nPaul",
    "created_at": "2010-09-29T11:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69077",
    "user": "zimmerma"
}
```

I tried Mitesh's script on my sage-4.6.alpha1 build (after sage -b main), then I applied the two
patches from that ticket, but I still get the same error as in comment 16.

Paul



---

archive/issue_comments_069078.json:
```json
{
    "body": "That's bizarre, because the patches apply and build fine for me.",
    "created_at": "2010-09-29T11:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69078",
    "user": "davidloeffler"
}
```

That's bizarre, because the patches apply and build fine for me.



---

archive/issue_comments_069079.json:
```json
{
    "body": "Actually I hadn't myself tried Mitesh's script when I posted above; I just did, and I couldn't get it to work either. But it should work if you install:\n\n```\n9898_pari_decl.patch\n9753.patch\n9764_ideal_repr_new.patch\ntrac_7883-ideals-folded.patch\n8333_8334_ALL-rebased_for_9764.patch\n7931_nth_root.2.patch\n7931_common_superclass.patch\n```\n",
    "created_at": "2010-09-29T12:48:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69079",
    "user": "davidloeffler"
}
```

Actually I hadn't myself tried Mitesh's script when I posted above; I just did, and I couldn't get it to work either. But it should work if you install:

```
9898_pari_decl.patch
9753.patch
9764_ideal_repr_new.patch
trac_7883-ideals-folded.patch
8333_8334_ALL-rebased_for_9764.patch
7931_nth_root.2.patch
7931_common_superclass.patch
```




---

archive/issue_comments_069080.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-29T14:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69080",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069081.json:
```json
{
    "body": "I managed to apply the patches following comment 21, however the following seems incorrect to me:\n\n```\nsage: b=Integers(3)(2)\nsage: b.nth_root(2)\n1\n```\n\nwhereas in say Sage 4.4.4 we got `ValueError: no nth root`.\n\nPS: I used the following reviewer program. Feel free to add it to the doctests.\n\n```\nfor n in range(2,100):\n   K=Integers(n)\n   for e in range(1,100):\n      for a in range(1,n):\n         b = K(a)\n         r = b.nth_root(e)\n         if r^e <> b:\n            print n, e, a\n            raise ValueError\n```\n",
    "created_at": "2010-09-29T14:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69081",
    "user": "zimmerma"
}
```

I managed to apply the patches following comment 21, however the following seems incorrect to me:

```
sage: b=Integers(3)(2)
sage: b.nth_root(2)
1
```

whereas in say Sage 4.4.4 we got `ValueError: no nth root`.

PS: I used the following reviewer program. Feel free to add it to the doctests.

```
for n in range(2,100):
   K=Integers(n)
   for e in range(1,100):
      for a in range(1,n):
         b = K(a)
         r = b.nth_root(e)
         if r^e <> b:
            print n, e, a
            raise ValueError
```




---

archive/issue_comments_069082.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-30T00:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69082",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069083.json:
```json
{
    "body": "Thanks for catching that.  I've fixed the problem and added a `_nth_root_naive` and check that the output of `b.nth_root(e, all=True)` matches `b._nth_root_naive(e)` for all `b` in `Zmod(n)` for `2 <= n < 100` and `1 <= e < 100`.  A shortened version of this test is left in as a doctest for `_nth_root_naive`.",
    "created_at": "2010-09-30T00:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69083",
    "user": "roed"
}
```

Thanks for catching that.  I've fixed the problem and added a `_nth_root_naive` and check that the output of `b.nth_root(e, all=True)` matches `b._nth_root_naive(e)` for all `b` in `Zmod(n)` for `2 <= n < 100` and `1 <= e < 100`.  A shortened version of this test is left in as a doctest for `_nth_root_naive`.



---

archive/issue_comments_069084.json:
```json
{
    "body": "Apply on top of 7931_nth_root.2.patch and 7931_common_superclass.patch",
    "created_at": "2010-09-30T03:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69084",
    "user": "roed"
}
```

Apply on top of 7931_nth_root.2.patch and 7931_common_superclass.patch



---

archive/issue_comments_069085.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-30T08:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69085",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069086.json:
```json
{
    "body": "Attachment [7931_fixes.patch](tarball://root/attachments/some-uuid/ticket7931/7931_fixes.patch) by zimmerma created at 2010-09-30 08:19:44\n\nwith the new patch, I still get unexpected results:\n\n```\nsage: K=Integers(6)\nsage: b=K(3)\nsage: b.nth_root(0,all=True)\n[3]\n```\n\nPaul",
    "created_at": "2010-09-30T08:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69086",
    "user": "zimmerma"
}
```

Attachment [7931_fixes.patch](tarball://root/attachments/some-uuid/ticket7931/7931_fixes.patch) by zimmerma created at 2010-09-30 08:19:44

with the new patch, I still get unexpected results:

```
sage: K=Integers(6)
sage: b=K(3)
sage: b.nth_root(0,all=True)
[3]
```

Paul



---

archive/issue_comments_069087.json:
```json
{
    "body": "Attachment [7931_fix2.patch](tarball://root/attachments/some-uuid/ticket7931/7931_fix2.patch) by roed created at 2010-09-30 09:19:26\n\nApply on top of previous patches",
    "created_at": "2010-09-30T09:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69087",
    "user": "roed"
}
```

Attachment [7931_fix2.patch](tarball://root/attachments/some-uuid/ticket7931/7931_fix2.patch) by roed created at 2010-09-30 09:19:26

Apply on top of previous patches



---

archive/issue_comments_069088.json:
```json
{
    "body": "Unexpected indeed.  Thanks for checking all these corner cases that I neglected (though some of the earlier ones were bugs I should have found if I'd tested sufficiently).\n\nIn this case I'm not quite sure what the right output is: an empty list or a ZeroDivisionError?  I've gone for the empty list, on the theory that `b.nth_root(e)` should return a list of all elements `a` with a<sup>e</sup>=b, and this makes sense even if `e=0`.",
    "created_at": "2010-09-30T09:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69088",
    "user": "roed"
}
```

Unexpected indeed.  Thanks for checking all these corner cases that I neglected (though some of the earlier ones were bugs I should have found if I'd tested sufficiently).

In this case I'm not quite sure what the right output is: an empty list or a ZeroDivisionError?  I've gone for the empty list, on the theory that `b.nth_root(e)` should return a list of all elements `a` with a<sup>e</sup>=b, and this makes sense even if `e=0`.



---

archive/issue_comments_069089.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-30T09:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69089",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069090.json:
```json
{
    "body": "e=0 is a hard case since there are too many solutions -- do we want to return all a in the ring? or all invertible a?\n\nSimilarly, do we allow negative e, where b must be invertible and b.nth_root(e) == (1/b).nth_root(-e), with an error if b is not invertible?\n\nOr do we want to specify in the documentation that e must be positive, and raise an error if not?",
    "created_at": "2010-09-30T10:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69090",
    "user": "cremona"
}
```

e=0 is a hard case since there are too many solutions -- do we want to return all a in the ring? or all invertible a?

Similarly, do we allow negative e, where b must be invertible and b.nth_root(e) == (1/b).nth_root(-e), with an error if b is not invertible?

Or do we want to specify in the documentation that e must be positive, and raise an error if not?



---

archive/issue_comments_069091.json:
```json
{
    "body": "My 2 cents:\n\n* for e=0 and b<>1, b.nth_root(e) should return the empty list\n\n* for e=0 and b=1, b.nth_root(e) should return only one solution, for example 1\n  (with all=True, return all a in the ring)\n\nPaul",
    "created_at": "2010-09-30T11:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69091",
    "user": "zimmerma"
}
```

My 2 cents:

* for e=0 and b<>1, b.nth_root(e) should return the empty list

* for e=0 and b=1, b.nth_root(e) should return only one solution, for example 1
  (with all=True, return all a in the ring)

Paul



---

archive/issue_comments_069092.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-30T12:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69092",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069093.json:
```json
{
    "body": "sorry, another problem:\n\n```\nsage: n=13777831336991389951\nsage: b=3798677550250515336\nsage: e=10608321776141318019\nsage: K = Integers(n)\nsage: b=K(b)\nsage: b.nth_root(e)\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n```\n\nThe documentation does not say when `ZeroDivisionError` can be obtained.\nThis was found with the following program:\n\n```\nwhile True:\n   n = randint(0,2^64)\n   K = Integers(n)\n   b = K.random_element()\n   e = randint(0,2^64)\n   print n, b, e, a\n   sys.stdout.flush()\n   try:\n      a = b.nth_root(e)\n      if a^e <> b:\n         print n, b, e, a\n         raise NotImplementedError\n   except ValueError:\n      n = 0\n```\n",
    "created_at": "2010-09-30T12:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69093",
    "user": "zimmerma"
}
```

sorry, another problem:

```
sage: n=13777831336991389951
sage: b=3798677550250515336
sage: e=10608321776141318019
sage: K = Integers(n)
sage: b=K(b)
sage: b.nth_root(e)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
```

The documentation does not say when `ZeroDivisionError` can be obtained.
This was found with the following program:

```
while True:
   n = randint(0,2^64)
   K = Integers(n)
   b = K.random_element()
   e = randint(0,2^64)
   print n, b, e, a
   sys.stdout.flush()
   try:
      a = b.nth_root(e)
      if a^e <> b:
         print n, b, e, a
         raise NotImplementedError
   except ValueError:
      n = 0
```




---

archive/issue_comments_069094.json:
```json
{
    "body": "You've found a bug in crt: it claims to work as long as the moduli are relatively prime, but in fact would often fail if one of them was 1.  I fixed that and clarified the behavior of `nth_root` when `n<=0` (it either returns the empty list or raises a `ValueError`, depending on the value of `all`; `mod(1,n).nth_root(0)` returns the list of all nonzero elements modulo n).",
    "created_at": "2010-10-01T06:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69094",
    "user": "roed"
}
```

You've found a bug in crt: it claims to work as long as the moduli are relatively prime, but in fact would often fail if one of them was 1.  I fixed that and clarified the behavior of `nth_root` when `n<=0` (it either returns the empty list or raises a `ValueError`, depending on the value of `all`; `mod(1,n).nth_root(0)` returns the list of all nonzero elements modulo n).



---

archive/issue_comments_069095.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-01T06:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69095",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069096.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-10-01T12:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69096",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069097.json:
```json
{
    "body": "Replying to [comment:29 roed]:\n> You've found a bug in crt: it claims to work as long as the moduli are relatively prime, but in fact would often fail if one of them was 1.  I fixed that and clarified the behavior of `nth_root` when `n<=0` (it either returns the empty list or raises a `ValueError`, depending on the value of `all`; `mod(1,n).nth_root(0)` returns the list of all nonzero elements modulo n).\n\nHi David,\n\nI'm not very happy with that answer. If a bug in crt was found, I would expect you to show a\nconcrete example, to report it as a new ticket, and to mention in your 3rd patch that it depends\non the new ticket, and can be removed once the new ticket is fixed.\n\nPaul",
    "created_at": "2010-10-01T12:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69097",
    "user": "zimmerma"
}
```

Replying to [comment:29 roed]:
> You've found a bug in crt: it claims to work as long as the moduli are relatively prime, but in fact would often fail if one of them was 1.  I fixed that and clarified the behavior of `nth_root` when `n<=0` (it either returns the empty list or raises a `ValueError`, depending on the value of `all`; `mod(1,n).nth_root(0)` returns the list of all nonzero elements modulo n).

Hi David,

I'm not very happy with that answer. If a bug in crt was found, I would expect you to show a
concrete example, to report it as a new ticket, and to mention in your 3rd patch that it depends
on the new ticket, and can be removed once the new ticket is fixed.

Paul



---

archive/issue_comments_069098.json:
```json
{
    "body": "Attachment [7931_fix3.patch](tarball://root/attachments/some-uuid/ticket7931/7931_fix3.patch) by roed created at 2010-10-01 14:28:50\n\nApply on top of previous patches",
    "created_at": "2010-10-01T14:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69098",
    "user": "roed"
}
```

Attachment [7931_fix3.patch](tarball://root/attachments/some-uuid/ticket7931/7931_fix3.patch) by roed created at 2010-10-01 14:28:50

Apply on top of previous patches



---

archive/issue_comments_069099.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-01T14:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69099",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069100.json:
```json
{
    "body": "You're right that it needs doctests; I've added some.  I also changed `7931_fix3.patch` by updating the `nth_root` function in `element_base` to match the behavior of the one in `integer_mod` for non-positive inputs.\n\nPersonally, I don't think that the crt bug is a major enough problem to need it's own ticket.  It only applies if one of the arguments is mod(0,1).  But I've separated the fix into its own patch; if you think it needs it's own ticket would you be willing to make the ticket and move the patch over there?",
    "created_at": "2010-10-01T14:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69100",
    "user": "roed"
}
```

You're right that it needs doctests; I've added some.  I also changed `7931_fix3.patch` by updating the `nth_root` function in `element_base` to match the behavior of the one in `integer_mod` for non-positive inputs.

Personally, I don't think that the crt bug is a major enough problem to need it's own ticket.  It only applies if one of the arguments is mod(0,1).  But I've separated the fix into its own patch; if you think it needs it's own ticket would you be willing to make the ticket and move the patch over there?



---

archive/issue_comments_069101.json:
```json
{
    "body": "I don't understand the crt patch: the examples given already worked in 4.6.alpha1 (and\nsimilarly in 4.4.4):\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: mod(0,1).crt(mod(4,17)) \n4\nsage: mod(0,1).crt(mod(0,1)) \n0\nsage: mod(21,22).crt(mod(0,1))\n21\n```\n\nWhat is exactly the crt bug (if any)?\n| Sage Version 4.6.alpha1, Release Date: 2010-09-18                  |\n| Type notebook() for the GUI, and license() for information.        |\nPaul",
    "created_at": "2010-10-01T15:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69101",
    "user": "zimmerma"
}
```

I don't understand the crt patch: the examples given already worked in 4.6.alpha1 (and
similarly in 4.4.4):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: mod(0,1).crt(mod(4,17)) 
4
sage: mod(0,1).crt(mod(0,1)) 
0
sage: mod(21,22).crt(mod(0,1))
21
```

What is exactly the crt bug (if any)?
| Sage Version 4.6.alpha1, Release Date: 2010-09-18                  |
| Type notebook() for the GUI, and license() for information.        |
Paul



---

archive/issue_comments_069102.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-10-01T15:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69102",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_069103.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-10-01T15:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69103",
    "user": "roed"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_069104.json:
```json
{
    "body": "Ah.  Now I understand why this problem only appeared with your latest test program that used large moduli.  The issue only occurs for `mod(0,1).crt(a)` when `a` has type `IntegerMod_gmp`.  So we didn't see it for smaller moduli.\n\nI've updated `7931_crt.patch`, and the doctest there does fail on my unpatched `4.6.alpha1`.",
    "created_at": "2010-10-01T15:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69104",
    "user": "roed"
}
```

Ah.  Now I understand why this problem only appeared with your latest test program that used large moduli.  The issue only occurs for `mod(0,1).crt(a)` when `a` has type `IntegerMod_gmp`.  So we didn't see it for smaller moduli.

I've updated `7931_crt.patch`, and the doctest there does fail on my unpatched `4.6.alpha1`.



---

archive/issue_comments_069105.json:
```json
{
    "body": "I understand now, this is really a bug, and I think it should be considered in a separate ticket:\n\n```\nsage: mod(0,1).crt(mod(4,2^31-2)) \n4\nsage: mod(0,1).crt(mod(4,2^31-1)) \n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n```\n",
    "created_at": "2010-10-01T15:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69105",
    "user": "zimmerma"
}
```

I understand now, this is really a bug, and I think it should be considered in a separate ticket:

```
sage: mod(0,1).crt(mod(4,2^31-2)) 
4
sage: mod(0,1).crt(mod(4,2^31-1)) 
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
```




---

archive/issue_comments_069106.json:
```json
{
    "body": "This is now #10047.",
    "created_at": "2010-10-01T16:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69106",
    "user": "roed"
}
```

This is now #10047.



---

archive/issue_comments_069107.json:
```json
{
    "body": "Attachment [7931_crt.patch](tarball://root/attachments/some-uuid/ticket7931/7931_crt.patch) by roed created at 2010-10-01 16:06:49\n\nThis is now #10047.",
    "created_at": "2010-10-01T16:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69107",
    "user": "roed"
}
```

Attachment [7931_crt.patch](tarball://root/attachments/some-uuid/ticket7931/7931_crt.patch) by roed created at 2010-10-01 16:06:49

This is now #10047.



---

archive/issue_comments_069108.json:
```json
{
    "body": "Attachment [7931_nth_root-folded.patch](tarball://root/attachments/some-uuid/ticket7931/7931_nth_root-folded.patch) by davidloeffler created at 2011-01-19 16:31:29\n\nQfolded patch. Apply only this patch.",
    "created_at": "2011-01-19T16:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69108",
    "user": "davidloeffler"
}
```

Attachment [7931_nth_root-folded.patch](tarball://root/attachments/some-uuid/ticket7931/7931_nth_root-folded.patch) by davidloeffler created at 2011-01-19 16:31:29

Qfolded patch. Apply only this patch.



---

archive/issue_comments_069109.json:
```json
{
    "body": "It took me some while to understand what patches to apply in what order, so having done so I thought it might be helpful to qfold everything into one patch. (I'm pleasantly surprised that patchbot understood immediately.)\n\nNow I'll have a look at the code.",
    "created_at": "2011-01-19T16:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69109",
    "user": "davidloeffler"
}
```

It took me some while to understand what patches to apply in what order, so having done so I thought it might be helpful to qfold everything into one patch. (I'm pleasantly surprised that patchbot understood immediately.)

Now I'll have a look at the code.



---

archive/issue_comments_069110.json:
```json
{
    "body": "The code looks plausible, and I'm pleased to report that we aren't going to have the same problem as #9304 -- old pickled objects seem to unpickle just fine. I'm not qualified to comment on the details of the algorithm though. Paul?",
    "created_at": "2011-01-19T17:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69110",
    "user": "davidloeffler"
}
```

The code looks plausible, and I'm pleased to report that we aren't going to have the same problem as #9304 -- old pickled objects seem to unpickle just fine. I'm not qualified to comment on the details of the algorithm though. Paul?



---

archive/issue_comments_069111.json:
```json
{
    "body": "Replying to [comment:37 davidloeffler]:\n> The code looks plausible, and I'm pleased to report that we aren't going to have the same problem as #9304 -- old pickled objects seem to unpickle just fine. I'm not qualified to comment on the details of the algorithm though. Paul?\n\nI won't have much time in the near future to look closely at the algorithm. Unless someone else\nhas time before me (John?) I'll look at this later. Don't hesitate to ping me.\n\nPaul",
    "created_at": "2011-01-20T07:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69111",
    "user": "zimmerma"
}
```

Replying to [comment:37 davidloeffler]:
> The code looks plausible, and I'm pleased to report that we aren't going to have the same problem as #9304 -- old pickled objects seem to unpickle just fine. I'm not qualified to comment on the details of the algorithm though. Paul?

I won't have much time in the near future to look closely at the algorithm. Unless someone else
has time before me (John?) I'll look at this later. Don't hesitate to ping me.

Paul



---

archive/issue_comments_069112.json:
```json
{
    "body": "Fixed ReST formatting",
    "created_at": "2011-01-25T13:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69112",
    "user": "davidloeffler"
}
```

Fixed ReST formatting



---

archive/issue_comments_069113.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-25T14:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69113",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069114.json:
```json
{
    "body": "Attachment [7931_nth_root-folded.2.patch](tarball://root/attachments/some-uuid/ticket7931/7931_nth_root-folded.2.patch) by davidloeffler created at 2011-01-25 14:04:36\n\nI checked this one with Bill Hart, who knows much more about these things than I, and he reckons that the implementation looks correct; I've run the tests and it seems to be fine. My only contribution has been to qfold everything and adjust some of the reference manual formatting, so I guess that doesn't need a separate review. \n\nApply only the last patch.",
    "created_at": "2011-01-25T14:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69114",
    "user": "davidloeffler"
}
```

Attachment [7931_nth_root-folded.2.patch](tarball://root/attachments/some-uuid/ticket7931/7931_nth_root-folded.2.patch) by davidloeffler created at 2011-01-25 14:04:36

I checked this one with Bill Hart, who knows much more about these things than I, and he reckons that the implementation looks correct; I've run the tests and it seems to be fine. My only contribution has been to qfold everything and adjust some of the reference manual formatting, so I guess that doesn't need a separate review. 

Apply only the last patch.



---

archive/issue_comments_069115.json:
```json
{
    "body": "Great!  Thanks to all of the reviewers for looking at this.",
    "created_at": "2011-01-25T17:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69115",
    "user": "roed"
}
```

Great!  Thanks to all of the reviewers for looking at this.



---

archive/issue_comments_069116.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-07T08:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7931",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7931#issuecomment-69116",
    "user": "jdemeyer"
}
```

Resolution: fixed
