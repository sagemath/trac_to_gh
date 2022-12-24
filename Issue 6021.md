# Issue 6021: Implement period lattices for elliptic curves over CC

archive/issues_006021.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\nKeywords: elliptic curve periods\n\nFor elliptic curves over number fields we currently only support the period lattice for real embeddings.  here we will implement the same for complex embeddings too (using the complex AGM method to compute the basis).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6021\n\n",
    "created_at": "2009-05-11T14:10:05Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "Implement period lattices for elliptic curves over CC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6021",
    "user": "@JohnCremona"
}
```
Assignee: @williamstein

CC:  @robertwb

Keywords: elliptic curve periods

For elliptic curves over number fields we currently only support the period lattice for real embeddings.  here we will implement the same for complex embeddings too (using the complex AGM method to compute the basis).

Issue created by migration from https://trac.sagemath.org/ticket/6021





---

archive/issue_comments_047939.json:
```json
{
    "body": "The patch does what was proposed.\n\nI added an is_real() method to mpfr reals (returning True of course) also, for convenience.",
    "created_at": "2009-05-11T16:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47939",
    "user": "@JohnCremona"
}
```

The patch does what was proposed.

I added an is_real() method to mpfr reals (returning True of course) also, for convenience.



---

archive/issue_comments_047940.json:
```json
{
    "body": "It looks good so far. Is there any reason we're still using Pari to compute in the real embedding case rather than just doing it all ourself?",
    "created_at": "2009-05-11T19:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47940",
    "user": "@robertwb"
}
```

It looks good so far. Is there any reason we're still using Pari to compute in the real embedding case rather than just doing it all ourself?



---

archive/issue_comments_047941.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> It looks good so far. Is there any reason we're still using Pari to compute in the real embedding case rather than just doing it all ourself? \n\nWell,  in either case we are using pari for the agm (real and complex cases)!  In the real case one has to be a bit careful to get the real and im periods properly, but I certainly know how to do that.  So I could put that in if you thought it better (but I will not have time until Wednesday...)\n\nJohn",
    "created_at": "2009-05-11T20:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47941",
    "user": "@JohnCremona"
}
```

Replying to [comment:3 robertwb]:
> It looks good so far. Is there any reason we're still using Pari to compute in the real embedding case rather than just doing it all ourself? 

Well,  in either case we are using pari for the agm (real and complex cases)!  In the real case one has to be a bit careful to get the real and im periods properly, but I certainly know how to do that.  So I could put that in if you thought it better (but I will not have time until Wednesday...)

John



---

archive/issue_comments_047942.json:
```json
{
    "body": "There have been additional comments about this on sage-nt. As a result I am adding to the patch, providing also (1) normalization of periods, (2) local implementation in the real case as an option instead of calling pari.\n \nThere will be an additional patch, so I have downgraded this to \"not ready for review\".",
    "created_at": "2009-05-13T11:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47942",
    "user": "@JohnCremona"
}
```

There have been additional comments about this on sage-nt. As a result I am adding to the patch, providing also (1) normalization of periods, (2) local implementation in the real case as an option instead of calling pari.
 
There will be an additional patch, so I have downgraded this to "not ready for review".



---

archive/issue_comments_047943.json:
```json
{
    "body": "With the new patch we now have a native implementation for real embeddings, which is the default with 'pari' as an option.  The period computation itself is devolved to a couple of internal functions.  Also, a normalisation function is included and one can ask for either a basis or normalised basis (these being different only for real embeddings).  The documentation is complete.\n\nOne thing which could be done is to cache the computed periods (with care so that if the user asks again with higher precision they do get recomputed).\n\nThe second patch was slightly premature (I had forgotten doctests for the two internal functions) so should be replaced by the third one, to be applied after the first, based on 3.4.2.",
    "created_at": "2009-05-13T14:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47943",
    "user": "@JohnCremona"
}
```

With the new patch we now have a native implementation for real embeddings, which is the default with 'pari' as an option.  The period computation itself is devolved to a couple of internal functions.  Also, a normalisation function is included and one can ask for either a basis or normalised basis (these being different only for real embeddings).  The documentation is complete.

One thing which could be done is to cache the computed periods (with care so that if the user asks again with higher precision they do get recomputed).

The second patch was slightly premature (I had forgotten doctests for the two internal functions) so should be replaced by the third one, to be applied after the first, based on 3.4.2.



---

archive/issue_comments_047944.json:
```json
{
    "body": "Looks good to me. Works as advertised and well documented. Nice work.",
    "created_at": "2009-05-15T00:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47944",
    "user": "@robertwb"
}
```

Looks good to me. Works as advertised and well documented. Nice work.



---

archive/issue_comments_047945.json:
```json
{
    "body": "Unsurprisingly this causes a bunch of numerical noise problems:\n\n```\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_number_field.py # 1 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_point.py # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/rational_field.py # 1 doctests failed\n        sage -t -long devel/sage/sage/schemes/elliptic_curves/period_lattice.py # 11 doctests failed\n```\n\nSome of them are quite disturbing:\n\n```\nFile \"/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/schemes/elliptic_curves/period_lattice.py\", line 439:\n    sage: Ls[2]._compute_periods_complex(100)\nExpected:\n    (1.9072648860892726204877126889 - 1.3404778596244020430694806590*I,\n    -1.9072648860892726204877126889 - 1.3404778596244020430694806590*I)\nGot:\n    (-1.9072648860892727038846028695 - 1.3404778596244020695699736749*I,\n     -1.9072648860892727038846028695 + 1.3404778596244020695699736749*I)\n```\n\nI.e. notice that for the real part above **11** digits are different.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T06:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47945",
    "user": "mabshoff"
}
```

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

I.e. notice that for the real part above **11** digits are different.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_047946.json:
```json
{
    "body": "Maybe it's a 32/64 thing (I only tested on 32-bit, my fault).\n\nI will look into it.",
    "created_at": "2009-05-15T07:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47946",
    "user": "@JohnCremona"
}
```

Maybe it's a 32/64 thing (I only tested on 32-bit, my fault).

I will look into it.



---

archive/issue_comments_047947.json:
```json
{
    "body": "Attachment [trac_6021_new.patch](tarball://root/attachments/some-uuid/ticket6021/trac_6021_new.patch) by @JohnCremona created at 2009-05-17 16:56:03\n\nReplaces all previous; based on 4.0.alpha0",
    "created_at": "2009-05-17T16:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47947",
    "user": "@JohnCremona"
}
```

Attachment [trac_6021_new.patch](tarball://root/attachments/some-uuid/ticket6021/trac_6021_new.patch) by @JohnCremona created at 2009-05-17 16:56:03

Replaces all previous; based on 4.0.alpha0



---

archive/issue_comments_047948.json:
```json
{
    "body": "There was some 32/64 fuzz, which I have fixed, but there were also some bugs in the precision handling, which have also been fixed.\n\nThe new patch trac_6021_new.patch replaces all previous, and is based on 4.0.alpha0.  I tested the problem files on both 32- and 64-bit.",
    "created_at": "2009-05-17T16:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47948",
    "user": "@JohnCremona"
}
```

There was some 32/64 fuzz, which I have fixed, but there were also some bugs in the precision handling, which have also been fixed.

The new patch trac_6021_new.patch replaces all previous, and is based on 4.0.alpha0.  I tested the problem files on both 32- and 64-bit.



---

archive/issue_comments_047949.json:
```json
{
    "body": "Why are there so many ...'s? Since we're no longer using Pari (unless we explicitly ask for it) the result should be deterministic and platform independent. (We are using Pari for complex agm, but not for real agm, but it seems to return exactly the same thing both 64- and 32-bit systems).",
    "created_at": "2009-05-18T21:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47949",
    "user": "@robertwb"
}
```

Why are there so many ...'s? Since we're no longer using Pari (unless we explicitly ask for it) the result should be deterministic and platform independent. (We are using Pari for complex agm, but not for real agm, but it seems to return exactly the same thing both 64- and 32-bit systems).



---

archive/issue_comments_047950.json:
```json
{
    "body": "Good question.\n\nI knew we use pari for complex agm and had assumed we also did for real agm.  I suggest that first we implement complex agm in native Sage, to remove that variable.\n\nHere are the steps:  \n\n1. compute 2-division poly over the number field (exact)\n2. embed the coeffs into RR or CC (depends on the embedding precision)\n3. find its roots in RR or CC (depends on precision)\n4. compute some square roots (ditto)\n5. compute some AGMs\n6. take reciprocals and multiply by pi\n\nWhat should be done is to find out exactly at what point things differ.",
    "created_at": "2009-05-19T07:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47950",
    "user": "@JohnCremona"
}
```

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

archive/issue_comments_047951.json:
```json
{
    "body": "I'm headed to bed soon, but I think Pari is involved in the root finding.",
    "created_at": "2009-05-19T08:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47951",
    "user": "@robertwb"
}
```

I'm headed to bed soon, but I think Pari is involved in the root finding.



---

archive/issue_comments_047952.json:
```json
{
    "body": "Attachment [embed_qqbar.patch](tarball://root/attachments/some-uuid/ticket6021/embed_qqbar.patch) by @JohnCremona created at 2009-05-22 15:03:55\n\nApply after previous",
    "created_at": "2009-05-22T15:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47952",
    "user": "@JohnCremona"
}
```

Attachment [embed_qqbar.patch](tarball://root/attachments/some-uuid/ticket6021/embed_qqbar.patch) by @JohnCremona created at 2009-05-22 15:03:55

Apply after previous



---

archive/issue_comments_047953.json:
```json
{
    "body": "apply after previous two",
    "created_at": "2009-05-22T15:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47953",
    "user": "@JohnCremona"
}
```

apply after previous two



---

archive/issue_comments_047954.json:
```json
{
    "body": "Attachment [cperiods.patch](tarball://root/attachments/some-uuid/ticket6021/cperiods.patch) by @JohnCremona created at 2009-05-22 15:13:07\n\nOK, so I have added two new patches:  embed_qqbar.patch is independent of the others, and adds functionality to the refine_embedding() function for embeddings of number fields to allow extending any embedding into RR or CC to an embedding into AA or QQbar (choosing the correct root).  Then cperiods.patch uses that to rethink how precision is handled for period lattices (real and complex):  the embedding supplied by the user is only used to determine which embedding is wanted, not its precision (which is ignored).  the lattice converts this (on construction) into an embedding into AA or QQbar, which it keeps.  Then the period-finding functions do as much as they can exactly (i.e. in AA or QQbar), up as far as computing sqrt(ei-ej) where e1,e2,e3 are the roots of the 2-division polynomial (so these expressions may have degree 6* the degree of the field);  only then are they converted into RR or CC (with the correct precision) for the transcendental step of computing AGMs.\n\nTo test this I removed the \"...\" which worried robertwb and reran the doctests -- they now all pass and agree on both 32 and 64-bit machines.\n\nI think this is a good strategy to use for number field embeddings (a.k.a. infinite places): separate the information \"which place\" from the information \"what precision\".\n\nIf this is approved, I will use the same tactic to improve the precision of the elliptic log (since the next thing on this agenda is to implement complex elliptic logs).",
    "created_at": "2009-05-22T15:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47954",
    "user": "@JohnCremona"
}
```

Attachment [cperiods.patch](tarball://root/attachments/some-uuid/ticket6021/cperiods.patch) by @JohnCremona created at 2009-05-22 15:13:07

OK, so I have added two new patches:  embed_qqbar.patch is independent of the others, and adds functionality to the refine_embedding() function for embeddings of number fields to allow extending any embedding into RR or CC to an embedding into AA or QQbar (choosing the correct root).  Then cperiods.patch uses that to rethink how precision is handled for period lattices (real and complex):  the embedding supplied by the user is only used to determine which embedding is wanted, not its precision (which is ignored).  the lattice converts this (on construction) into an embedding into AA or QQbar, which it keeps.  Then the period-finding functions do as much as they can exactly (i.e. in AA or QQbar), up as far as computing sqrt(ei-ej) where e1,e2,e3 are the roots of the 2-division polynomial (so these expressions may have degree 6* the degree of the field);  only then are they converted into RR or CC (with the correct precision) for the transcendental step of computing AGMs.

To test this I removed the "..." which worried robertwb and reran the doctests -- they now all pass and agree on both 32 and 64-bit machines.

I think this is a good strategy to use for number field embeddings (a.k.a. infinite places): separate the information "which place" from the information "what precision".

If this is approved, I will use the same tactic to improve the precision of the elliptic log (since the next thing on this agenda is to implement complex elliptic logs).



---

archive/issue_comments_047955.json:
```json
{
    "body": "Looks good. I like the idea of using AA/QQbar for embeddings as well.",
    "created_at": "2009-05-26T18:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47955",
    "user": "@robertwb"
}
```

Looks good. I like the idea of using AA/QQbar for embeddings as well.



---

archive/issue_comments_047956.json:
```json
{
    "body": "Thanks Robert.  I'm now working on moving the elliptic log code into the Lattice class, which certainly depends on this but there's no reason to delay this.",
    "created_at": "2009-05-26T21:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47956",
    "user": "@JohnCremona"
}
```

Thanks Robert.  I'm now working on moving the elliptic log code into the Lattice class, which certainly depends on this but there's no reason to delay this.



---

archive/issue_comments_047957.json:
```json
{
    "body": "Yet another patch, to be applied after the previous ones.\n\n1. Better handling of precision.  The algebraic quantities needed for both periods and elliptic logs are now cached.  Then period and log computations just have to coerce into the appropriate Real/ComplexField, and do the transcendental part via agm.\n2. Elliptic log implementation now moved into period lattice class (except for the algorithm=\"pari\" case which is unchanged).  Also available via call i.e. as L.elliptic_logarithm(P) or just L(P).  Uses an extended agm function which has been separated off.\n3. Earlier precision issues with a difficult example are fixed;  we get all the same digits as pari, and faster.  To do this we compute the extended AGM in double the required precision and then revert to desired precision at the end.  (I tried adding 10 or 20 bits of precision, but that nasty example (18074g1) needs more).\n\nThe only remaining thing is to implement elliptic logs for non-real lattices.  This is not hard to do but harder to justify!  Before I do that, to test it  I need to implement the reverse of the elliptic log -- using Weierstrass P-functions and derivative to go from z mod L back to P(x,y) with complex coords in general.\n\nApologies for adding this after a positive review (which applies to the first three patches only).  So: the first 3 patches have a positive review, while the 4th does not (yet).",
    "created_at": "2009-05-27T21:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47957",
    "user": "@JohnCremona"
}
```

Yet another patch, to be applied after the previous ones.

1. Better handling of precision.  The algebraic quantities needed for both periods and elliptic logs are now cached.  Then period and log computations just have to coerce into the appropriate Real/ComplexField, and do the transcendental part via agm.
2. Elliptic log implementation now moved into period lattice class (except for the algorithm="pari" case which is unchanged).  Also available via call i.e. as L.elliptic_logarithm(P) or just L(P).  Uses an extended agm function which has been separated off.
3. Earlier precision issues with a difficult example are fixed;  we get all the same digits as pari, and faster.  To do this we compute the extended AGM in double the required precision and then revert to desired precision at the end.  (I tried adding 10 or 20 bits of precision, but that nasty example (18074g1) needs more).

The only remaining thing is to implement elliptic logs for non-real lattices.  This is not hard to do but harder to justify!  Before I do that, to test it  I need to implement the reverse of the elliptic log -- using Weierstrass P-functions and derivative to go from z mod L back to P(x,y) with complex coords in general.

Apologies for adding this after a positive review (which applies to the first three patches only).  So: the first 3 patches have a positive review, while the 4th does not (yet).



---

archive/issue_comments_047958.json:
```json
{
    "body": "I moved the last patch to #6193, as it's really starting to implement new functionality (though there is some good cleanup/precision handling of this code as well).",
    "created_at": "2009-06-03T07:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47958",
    "user": "@robertwb"
}
```

I moved the last patch to #6193, as it's really starting to implement new functionality (though there is some good cleanup/precision handling of this code as well).



---

archive/issue_comments_047959.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T20:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47959",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_047960.json:
```json
{
    "body": "Merged all three patches in 4.0.1.rc0.",
    "created_at": "2009-06-03T20:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47960",
    "user": "@mwhansen"
}
```

Merged all three patches in 4.0.1.rc0.



---

archive/issue_comments_047961.json:
```json
{
    "body": "See also #7719.",
    "created_at": "2009-12-17T10:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6021#issuecomment-47961",
    "user": "@JohnCremona"
}
```

See also #7719.
