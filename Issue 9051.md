# Issue 9051: Fast function field arithmetic

archive/issues_009051.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  minz\n\nFollowup to #7585, which also did many, many other things. \n\nWrapping flint directly is much faster than the current implementation of Frac(GF(p)['t'])\n\nIssue created by migration from https://trac.sagemath.org/ticket/9051\n\n",
    "created_at": "2010-05-26T00:27:53Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Fast function field arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9051",
    "user": "robertwb"
}
```
Assignee: AlexGhitza

CC:  minz

Followup to #7585, which also did many, many other things. 

Wrapping flint directly is much faster than the current implementation of Frac(GF(p)['t'])

Issue created by migration from https://trac.sagemath.org/ticket/9051





---

archive/issue_comments_083800.json:
```json
{
    "body": "Attachment [9051-FpT_1.patch](tarball://root/attachments/some-uuid/ticket9051/9051-FpT_1.patch) by robertwb created at 2010-05-27 07:29:28",
    "created_at": "2010-05-27T07:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83800",
    "user": "robertwb"
}
```

Attachment [9051-FpT_1.patch](tarball://root/attachments/some-uuid/ticket9051/9051-FpT_1.patch) by robertwb created at 2010-05-27 07:29:28



---

archive/issue_comments_083801.json:
```json
{
    "body": "Attachment [9051-FpT_3.patch](tarball://root/attachments/some-uuid/ticket9051/9051-FpT_3.patch) by robertwb created at 2010-05-27 07:29:39",
    "created_at": "2010-05-27T07:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83801",
    "user": "robertwb"
}
```

Attachment [9051-FpT_3.patch](tarball://root/attachments/some-uuid/ticket9051/9051-FpT_3.patch) by robertwb created at 2010-05-27 07:29:39



---

archive/issue_comments_083802.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-27T07:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83802",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083803.json:
```json
{
    "body": "Apply all three patches in order. \n\nPositive review to `9051-FpT_2.patch` (the third was somewhat a rebasing, referee, and fixing some stuff).",
    "created_at": "2010-05-27T07:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83803",
    "user": "robertwb"
}
```

Apply all three patches in order. 

Positive review to `9051-FpT_2.patch` (the third was somewhat a rebasing, referee, and fixing some stuff).



---

archive/issue_comments_083804.json:
```json
{
    "body": "Note:   9051-FpT_2.patch  is by David Roe.",
    "created_at": "2010-05-28T22:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83804",
    "user": "was"
}
```

Note:   9051-FpT_2.patch  is by David Roe.



---

archive/issue_comments_083805.json:
```json
{
    "body": "Attachment [9051-FpT_4.patch](tarball://root/attachments/some-uuid/ticket9051/9051-FpT_4.patch) by robertwb created at 2010-05-30 09:35:16",
    "created_at": "2010-05-30T09:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83805",
    "user": "robertwb"
}
```

Attachment [9051-FpT_4.patch](tarball://root/attachments/some-uuid/ticket9051/9051-FpT_4.patch) by robertwb created at 2010-05-30 09:35:16



---

archive/issue_comments_083806.json:
```json
{
    "body": "flattened parts1-4 and rebased against sage-4.4.4",
    "created_at": "2010-07-08T11:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83806",
    "user": "was"
}
```

flattened parts1-4 and rebased against sage-4.4.4



---

archive/issue_comments_083807.json:
```json
{
    "body": "Attachment [trac_9051-flattened_and_rebased.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051-flattened_and_rebased.patch) by was created at 2010-07-08 12:05:56\n\nI took sage-4.4.4 and applied trac_9051-flattened_and_rebased.patch.  Doctesting just rings/ fails very seriously after applying this patch:\n\n\n```\n\nsage -t devel/sage/sage/rings/\n\nThe following tests failed:\n\n        sage -t  devel/sage-main/sage/rings/residue_field.pyx # 16 doctests failed\n        sage -t  devel/sage-main/sage/rings/number_field/order.py # 3 doctests failed\n        sage -t  devel/sage-main/sage/rings/number_field/number_field_element_quadratic.pyx # 2 doctests failed\n        sage -t  devel/sage-main/sage/rings/arith.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/rings/ring.pyx # 5 doctests failed\n        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed\n        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 7 doctests failed\n        sage -t  devel/sage-main/sage/rings/integer_ring.pyx # 5 doctests failed\n        sage -t  devel/sage-main/sage/rings/number_field/galois_group.py # 8 doctests failed\n        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx # 7 doctests failed\n        sage -t  devel/sage-main/sage/rings/misc.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/rings/number_field/number_field_base.pyx # 13 doctests failed\n        sage -t  devel/sage-main/sage/rings/qqbar.py # 4 doctests failed\n        sage -t  devel/sage-main/sage/rings/number_field/number_field_rel.py # 10 doctests failed\n        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py # 15 doctests failed\n        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_singular_interface.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/rings/number_field/number_field_element.pyx # 13 doctests failed\n----------------------------------------------------------------------\nTimings have been updated.\nTotal time for all tests: 64.0 seconds\n```\n",
    "created_at": "2010-07-08T12:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83807",
    "user": "was"
}
```

Attachment [trac_9051-flattened_and_rebased.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051-flattened_and_rebased.patch) by was created at 2010-07-08 12:05:56

I took sage-4.4.4 and applied trac_9051-flattened_and_rebased.patch.  Doctesting just rings/ fails very seriously after applying this patch:


```

sage -t devel/sage/sage/rings/

The following tests failed:

        sage -t  devel/sage-main/sage/rings/residue_field.pyx # 16 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/order.py # 3 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/number_field_element_quadratic.pyx # 2 doctests failed
        sage -t  devel/sage-main/sage/rings/arith.py # 1 doctests failed
        sage -t  devel/sage-main/sage/rings/ring.pyx # 5 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 7 doctests failed
        sage -t  devel/sage-main/sage/rings/integer_ring.pyx # 5 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/galois_group.py # 8 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx # 7 doctests failed
        sage -t  devel/sage-main/sage/rings/misc.py # 1 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/number_field_base.pyx # 13 doctests failed
        sage -t  devel/sage-main/sage/rings/qqbar.py # 4 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/number_field_rel.py # 10 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py # 15 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_singular_interface.py # 1 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/number_field_element.pyx # 13 doctests failed
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 64.0 seconds
```




---

archive/issue_comments_083808.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-08T12:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83808",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083809.json:
```json
{
    "body": "Fixes the broken doctests",
    "created_at": "2010-07-09T11:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83809",
    "user": "roed"
}
```

Fixes the broken doctests



---

archive/issue_comments_083810.json:
```json
{
    "body": "Attachment [trac_9051_polycall_fixes.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051_polycall_fixes.patch) by roed created at 2010-07-09 11:59:46",
    "created_at": "2010-07-09T11:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83810",
    "user": "roed"
}
```

Attachment [trac_9051_polycall_fixes.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051_polycall_fixes.patch) by roed created at 2010-07-09 11:59:46



---

archive/issue_comments_083811.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-09T11:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83811",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083812.json:
```json
{
    "body": "The most recent patch should be applied on top of the flattened and rebased patche.",
    "created_at": "2010-07-09T12:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83812",
    "user": "roed"
}
```

The most recent patch should be applied on top of the flattened and rebased patche.



---

archive/issue_comments_083813.json:
```json
{
    "body": "I'm running tests with both patches:\n\n  http://sage.math.washington.edu/home/wstein/build/sage-4.4.4/devel/sage/9051.out",
    "created_at": "2010-07-09T12:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83813",
    "user": "was"
}
```

I'm running tests with both patches:

  http://sage.math.washington.edu/home/wstein/build/sage-4.4.4/devel/sage/9051.out



---

archive/issue_comments_083814.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-09T12:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83814",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083815.json:
```json
{
    "body": "Stuff fails.  See above link.",
    "created_at": "2010-07-09T12:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83815",
    "user": "was"
}
```

Stuff fails.  See above link.



---

archive/issue_comments_083816.json:
```json
{
    "body": "\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t  devel/sage-main/sage/modular/abvar/homspace.py # 20 doctests failed\n        sage -t  devel/sage-main/sage/modular/abvar/abvar.py # 32 doctests failed\n        sage -t  devel/sage-main/sage/modular/modsym/space.py # 6 doctests failed\n        sage -t  devel/sage-main/sage/modular/modsym/ambient.py # 2 doctests failed\n        sage -t  devel/sage-main/sage/modular/modform/element.py # 2 doctests failed\n        sage -t  devel/sage-main/sage/functions/piecewise.py # 6 doctests failed\n        sage -t  devel/sage-main/sage/graphs/graph.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed\n        sage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed\n        sage -t  devel/sage-main/sage/modular/abvar/homology.py # 19 doctests failed\n        sage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 12 doctests failed\n        sage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/numerical/optimize.py # 2 doctests failed\n        sage -t  devel/sage-main/sage/modular/abvar/constructor.py # 2 doctests failed\n        sage -t  devel/sage-main/sage/schemes/hyperelliptic_curves/hypellfrob.pyx # 1 doctests failed\n----------------------------------------------------------------------\nTimings have been updated.\nTotal time for all tests: 355.5 seconds\n                                                            \n```\n",
    "created_at": "2010-07-09T12:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83816",
    "user": "was"
}
```


```
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage-main/sage/modular/abvar/homspace.py # 20 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/abvar.py # 32 doctests failed
        sage -t  devel/sage-main/sage/modular/modsym/space.py # 6 doctests failed
        sage -t  devel/sage-main/sage/modular/modsym/ambient.py # 2 doctests failed
        sage -t  devel/sage-main/sage/modular/modform/element.py # 2 doctests failed
        sage -t  devel/sage-main/sage/functions/piecewise.py # 6 doctests failed
        sage -t  devel/sage-main/sage/graphs/graph.py # 1 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/homology.py # 19 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 12 doctests failed
        sage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed
        sage -t  devel/sage-main/sage/numerical/optimize.py # 2 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/constructor.py # 2 doctests failed
        sage -t  devel/sage-main/sage/schemes/hyperelliptic_curves/hypellfrob.pyx # 1 doctests failed
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 355.5 seconds
                                                            
```




---

archive/issue_comments_083817.json:
```json
{
    "body": "Attachment [trac_9051_fixes2.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051_fixes2.patch) by roed created at 2010-07-09 12:29:27\n\nFixes more doctests",
    "created_at": "2010-07-09T12:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83817",
    "user": "roed"
}
```

Attachment [trac_9051_fixes2.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051_fixes2.patch) by roed created at 2010-07-09 12:29:27

Fixes more doctests



---

archive/issue_comments_083818.json:
```json
{
    "body": "Thanks; I was going to run tests while sleeping, but this worked better.  I think I have them all now, but I haven't run tests after the fix: I'm doing it on my laptop, so it'll take a while.",
    "created_at": "2010-07-09T12:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83818",
    "user": "roed"
}
```

Thanks; I was going to run tests while sleeping, but this worked better.  I think I have them all now, but I haven't run tests after the fix: I'm doing it on my laptop, so it'll take a while.



---

archive/issue_comments_083819.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-09T12:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83819",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083820.json:
```json
{
    "body": "Here it goes again:\n\n   http://sage.math.washington.edu/home/wstein/build/sage-4.4.4/devel/sage/9051-try2.out",
    "created_at": "2010-07-09T14:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83820",
    "user": "was"
}
```

Here it goes again:

   http://sage.math.washington.edu/home/wstein/build/sage-4.4.4/devel/sage/9051-try2.out



---

archive/issue_comments_083821.json:
```json
{
    "body": "Looks like all tests pass; do you want to review it?",
    "created_at": "2010-07-09T22:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83821",
    "user": "roed"
}
```

Looks like all tests pass; do you want to review it?



---

archive/issue_comments_083822.json:
```json
{
    "body": "Wow, that's excellent that everything finally passes.  Yes, I hope to have time to review it soon.",
    "created_at": "2010-07-10T05:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83822",
    "user": "was"
}
```

Wow, that's excellent that everything finally passes.  Yes, I hope to have time to review it soon.



---

archive/issue_comments_083823.json:
```json
{
    "body": "Attachment [trac_9051-everything_flattened.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051-everything_flattened.patch) by was created at 2010-07-15 15:46:47\n\nI did a benchmark on sage.math, comparing this code to Magma:\n\nSAGE with your patch:\n\n```\nsage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)\nsage: timeit('a/b+b/a')\n625 loops, best of 3: 26.3 \u00b5s per loop\nsage: time v=[a/b+b/a for i in range(10^5)]\nCPU times: user 2.94 s, sys: 0.02 s, total: 2.96 s\nWall time: 2.96 s\nsage: time v=[a*b for i in range(10^5)]\nCPU times: user 0.54 s, sys: 0.02 s, total: 0.56 s\nWall time: 0.56 s\nsage: time v=[(1/a)*(1/b) for i in range(10^5)]\nCPU times: user 1.80 s, sys: 0.00 s, total: 1.80 s\nWall time: 1.80 s\n```\n\n\nBefore the patch, the same benchmark is massively slower, so this patch is a very big improvement:\n\n```\nsage: sage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)\nsage: sage: timeit('a/b+b/a')\n625 loops, best of 3: 776 \u00b5s per loop\n```\n\n\n\nIn Magma:\n\n```\nsage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)\nsage: aa=magma(a); bb=magma(b)\nsage: magma.eval('a:=%s;b:=%s;'%(aa.name(),bb.name()))\nsage: magma.eval('time v := [a/b+b/a : i in [1..10^5]];')\n'Time: 0.800'\nsage: magma.eval('time v := [a*b : i in [1..10^5]];')\n'Time: 0.320'\nsage: magma.eval('time v := [(1/a) * (1/b) : i in [1..10^5]];')\n'Time: 0.830'\n```\n\n\nSomething surprising is that working in your rational function field is much faster than working with polynomials!\n\n```\nsage: R.<T> = GF(71)[];  a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)\nsage: time v=[a*b for i in range(10^5)]\nCPU times: user 2.02 s, sys: 0.00 s, total: 2.02 s\nWall time: 2.02 s\n```\n",
    "created_at": "2010-07-15T15:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83823",
    "user": "was"
}
```

Attachment [trac_9051-everything_flattened.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051-everything_flattened.patch) by was created at 2010-07-15 15:46:47

I did a benchmark on sage.math, comparing this code to Magma:

SAGE with your patch:

```
sage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)
sage: timeit('a/b+b/a')
625 loops, best of 3: 26.3 µs per loop
sage: time v=[a/b+b/a for i in range(10^5)]
CPU times: user 2.94 s, sys: 0.02 s, total: 2.96 s
Wall time: 2.96 s
sage: time v=[a*b for i in range(10^5)]
CPU times: user 0.54 s, sys: 0.02 s, total: 0.56 s
Wall time: 0.56 s
sage: time v=[(1/a)*(1/b) for i in range(10^5)]
CPU times: user 1.80 s, sys: 0.00 s, total: 1.80 s
Wall time: 1.80 s
```


Before the patch, the same benchmark is massively slower, so this patch is a very big improvement:

```
sage: sage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)
sage: sage: timeit('a/b+b/a')
625 loops, best of 3: 776 µs per loop
```



In Magma:

```
sage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)
sage: aa=magma(a); bb=magma(b)
sage: magma.eval('a:=%s;b:=%s;'%(aa.name(),bb.name()))
sage: magma.eval('time v := [a/b+b/a : i in [1..10^5]];')
'Time: 0.800'
sage: magma.eval('time v := [a*b : i in [1..10^5]];')
'Time: 0.320'
sage: magma.eval('time v := [(1/a) * (1/b) : i in [1..10^5]];')
'Time: 0.830'
```


Something surprising is that working in your rational function field is much faster than working with polynomials!

```
sage: R.<T> = GF(71)[];  a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)
sage: time v=[a*b for i in range(10^5)]
CPU times: user 2.02 s, sys: 0.00 s, total: 2.02 s
Wall time: 2.02 s
```




---

archive/issue_comments_083824.json:
```json
{
    "body": "Before the patch... 79 seconds instead of the new 2.9 seconds:\n\n```\n\nsage: sage: time v=[a/b+b/a for i in range(10^5)]\nCPU times: user 78.91 s, sys: 0.15 s, total: 79.06 s\nWall time: 79.05 s\n```\n",
    "created_at": "2010-07-15T15:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83824",
    "user": "was"
}
```

Before the patch... 79 seconds instead of the new 2.9 seconds:

```

sage: sage: time v=[a/b+b/a for i in range(10^5)]
CPU times: user 78.91 s, sys: 0.15 s, total: 79.06 s
Wall time: 79.05 s
```




---

archive/issue_comments_083825.json:
```json
{
    "body": "Attachment [trac_9051-referee-1.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051-referee-1.patch) by was created at 2010-07-15 17:34:56\n\napply this after the \"everything flattened\" patch directly above.",
    "created_at": "2010-07-15T17:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83825",
    "user": "was"
}
```

Attachment [trac_9051-referee-1.patch](tarball://root/attachments/some-uuid/ticket9051/trac_9051-referee-1.patch) by was created at 2010-07-15 17:34:56

apply this after the "everything flattened" patch directly above.



---

archive/issue_comments_083826.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-15T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83826",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083827.json:
```json
{
    "body": "Reviewer patch looks good to me. My only comment is that it would be nice to have a faster not-equals comparison, but that's not worth holding this up.",
    "created_at": "2010-07-16T02:10:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83827",
    "user": "robertwb"
}
```

Reviewer patch looks good to me. My only comment is that it would be nice to have a faster not-equals comparison, but that's not worth holding this up.



---

archive/issue_comments_083828.json:
```json
{
    "body": "I've merged only\n\n* [attachment:trac_9051-everything_flattened.patch]\n* [attachment:trac_9051-referee-1.patch]\n\nin 4.5.2.alpha0.  Please correct the Author(s) and Reviewer(s) fields, if I'm wrong.",
    "created_at": "2010-07-20T09:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83828",
    "user": "mpatel"
}
```

I've merged only

* [attachment:trac_9051-everything_flattened.patch]
* [attachment:trac_9051-referee-1.patch]

in 4.5.2.alpha0.  Please correct the Author(s) and Reviewer(s) fields, if I'm wrong.



---

archive/issue_comments_083829.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83829",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_083830.json:
```json
{
    "body": "I assume that it's a mistake that the function\n\n```\ndef fraction_field(self):\n```\n\nwas added *twice* in `sage/rings/polynomial/polynomial_ring.py`",
    "created_at": "2013-01-18T08:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83830",
    "user": "jdemeyer"
}
```

I assume that it's a mistake that the function

```
def fraction_field(self):
```

was added *twice* in `sage/rings/polynomial/polynomial_ring.py`



---

archive/issue_comments_083831.json:
```json
{
    "body": "Please review #13971 to correct this duplicate method.",
    "created_at": "2013-01-19T11:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9051#issuecomment-83831",
    "user": "jdemeyer"
}
```

Please review #13971 to correct this duplicate method.
