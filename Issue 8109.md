# Issue 8109: wrap NTL's lzz_pE and lzz_pEX and use them

archive/issues_008109.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis should fasten polynomial arithmetic over finite fields of small characteristic.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8109\n\n",
    "created_at": "2010-01-28T08:02:42Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "wrap NTL's lzz_pE and lzz_pEX and use them",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8109",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: @aghitza

This should fasten polynomial arithmetic over finite fields of small characteristic.

Issue created by migration from https://trac.sagemath.org/ticket/8109





---

archive/issue_comments_071054.json:
```json
{
    "body": "Attachment [trac_8109-lzz_pEX.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX.patch) by ylchapuy created at 2010-01-29 23:27:32\n\nneeds #7841 (I guess)",
    "created_at": "2010-01-29T23:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71054",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_8109-lzz_pEX.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX.patch) by ylchapuy created at 2010-01-29 23:27:32

needs #7841 (I guess)



---

archive/issue_comments_071055.json:
```json
{
    "body": "Changing keywords from \"\" to \"ntl\".",
    "created_at": "2010-01-29T23:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71055",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing keywords from "" to "ntl".



---

archive/issue_comments_071056.json:
```json
{
    "body": "Preliminary version.\n\nnote: this is mostly a copy of existing files for wrapping ZZ_pE and ZZ_pEX with\n'sed s/ZZ/zz/g' applied.\n\nwarning: there is no test (yet) for checking that the modulus is < NTL_SP_BOUND\n\nstill, doctests pass and here are some results:\n\n```\nsage: c=ntl.zz_pEContext(ntl.zz_pX([1,1,1,1,1], 19800713)) \nsage: a = ntl.zz_pE([3,2], c); b = ntl.zz_pE([1,2], c)\nsage: f = ntl.zz_pEX([a, b, b])\nsage: p = f**123\nsage: q = p+f**77+f\nsage: \nsage: C=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1,1,1], 19800713)) \nsage: A = ntl.ZZ_pE([3,2], C); B = ntl.ZZ_pE([1,2], C)\nsage: F = ntl.ZZ_pEX([A, B, B])\nsage: P = F**123\nsage: Q = P+F**77+F\nsage: \nsage: %timeit p+q\n625 loops, best of 3: 59.6 \u00b5s per loop\nsage: %timeit P+Q\n625 loops, best of 3: 180 \u00b5s per loop\nsage: \nsage: %timeit p*q\n125 loops, best of 3: 2.62 ms per loop\nsage: %timeit P*Q\n125 loops, best of 3: 5.65 ms per loop\nsage: \nsage: %timeit p.gcd(q)\n125 loops, best of 3: 7.28 ms per loop\nsage: %timeit P.gcd(Q)\n5 loops, best of 3: 62.5 ms per loop\nsage: \nsage: %timeit p**17\n5 loops, best of 3: 58 ms per loop\nsage: %timeit P**17\n5 loops, best of 3: 129 ms per loop\n```\n",
    "created_at": "2010-01-29T23:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71056",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Preliminary version.

note: this is mostly a copy of existing files for wrapping ZZ_pE and ZZ_pEX with
'sed s/ZZ/zz/g' applied.

warning: there is no test (yet) for checking that the modulus is < NTL_SP_BOUND

still, doctests pass and here are some results:

```
sage: c=ntl.zz_pEContext(ntl.zz_pX([1,1,1,1,1], 19800713)) 
sage: a = ntl.zz_pE([3,2], c); b = ntl.zz_pE([1,2], c)
sage: f = ntl.zz_pEX([a, b, b])
sage: p = f**123
sage: q = p+f**77+f
sage: 
sage: C=ntl.ZZ_pEContext(ntl.ZZ_pX([1,1,1,1,1], 19800713)) 
sage: A = ntl.ZZ_pE([3,2], C); B = ntl.ZZ_pE([1,2], C)
sage: F = ntl.ZZ_pEX([A, B, B])
sage: P = F**123
sage: Q = P+F**77+F
sage: 
sage: %timeit p+q
625 loops, best of 3: 59.6 µs per loop
sage: %timeit P+Q
625 loops, best of 3: 180 µs per loop
sage: 
sage: %timeit p*q
125 loops, best of 3: 2.62 ms per loop
sage: %timeit P*Q
125 loops, best of 3: 5.65 ms per loop
sage: 
sage: %timeit p.gcd(q)
125 loops, best of 3: 7.28 ms per loop
sage: %timeit P.gcd(Q)
5 loops, best of 3: 62.5 ms per loop
sage: 
sage: %timeit p**17
5 loops, best of 3: 58 ms per loop
sage: %timeit P**17
5 loops, best of 3: 129 ms per loop
```




---

archive/issue_comments_071057.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-29T23:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71057",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071058.json:
```json
{
    "body": "Replying to [comment:1 ylchapuy]:\n\n> warning: there is no test (yet) for checking that the modulus is < NTL_SP_BOUND\n\nI must be tired... there is a check, it's done in the lzz_p class.\n\nI guess this one is ready for review then. I will open another ticket to do the same as #7841 latter.",
    "created_at": "2010-01-29T23:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71058",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Replying to [comment:1 ylchapuy]:

> warning: there is no test (yet) for checking that the modulus is < NTL_SP_BOUND

I must be tired... there is a check, it's done in the lzz_p class.

I guess this one is ready for review then. I will open another ticket to do the same as #7841 latter.



---

archive/issue_comments_071059.json:
```json
{
    "body": "use both patches",
    "created_at": "2010-02-01T19:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71059",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

use both patches



---

archive/issue_comments_071060.json:
```json
{
    "body": "Attachment [trac_8109-lzz_pEX-part2.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX-part2.patch) by ylchapuy created at 2010-02-01 20:01:39\n\nFinally, this is such a small patch that I add it here.\nWith both patches applied, the default implementation for polynomial ring is now based on NTL, and uses type ZZ or lzz depending on the characteristic (tested against NTL_SP_BOUND).",
    "created_at": "2010-02-01T20:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71060",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_8109-lzz_pEX-part2.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX-part2.patch) by ylchapuy created at 2010-02-01 20:01:39

Finally, this is such a small patch that I add it here.
With both patches applied, the default implementation for polynomial ring is now based on NTL, and uses type ZZ or lzz depending on the characteristic (tested against NTL_SP_BOUND).



---

archive/issue_comments_071061.json:
```json
{
    "body": "I'll review this.  I'm working on multiple related things actually: improving finite fields (which I'm thinking of doing with a new templating class) and p-adic polynomials.",
    "created_at": "2010-02-08T22:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71061",
    "user": "https://github.com/roed314"
}
```

I'll review this.  I'm working on multiple related things actually: improving finite fields (which I'm thinking of doing with a new templating class) and p-adic polynomials.



---

archive/issue_comments_071062.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-09T17:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71062",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071063.json:
```json
{
    "body": "I see that you changed it to \"needs work.\"  One thing I noticed looking at the patch was that sage/libs/ntl/ntl_lzz_decl.pxd seems generally broken: shouldn't those be zz_p and lzz_p, not zz and lzz?",
    "created_at": "2010-02-09T22:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71063",
    "user": "https://github.com/roed314"
}
```

I see that you changed it to "needs work."  One thing I noticed looking at the patch was that sage/libs/ntl/ntl_lzz_decl.pxd seems generally broken: shouldn't those be zz_p and lzz_p, not zz and lzz?



---

archive/issue_comments_071064.json:
```json
{
    "body": "Attachment [trac_8109-lzz_pEX-part3.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX-part3.patch) by ylchapuy created at 2010-02-10 14:23:22",
    "created_at": "2010-02-10T14:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71064",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_8109-lzz_pEX-part3.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX-part3.patch) by ylchapuy created at 2010-02-10 14:23:22



---

archive/issue_comments_071065.json:
```json
{
    "body": "replacing all previous ones",
    "created_at": "2010-02-10T18:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71065",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

replacing all previous ones



---

archive/issue_comments_071066.json:
```json
{
    "body": "Attachment [trac_8109-lzz_pEX-all_in_one.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX-all_in_one.patch) by ylchapuy created at 2010-02-10 18:41:53\n\nReplying to [comment:6 roed]:\n> I see that you changed it to \"needs work.\"  One thing I noticed looking at the patch was that sage/libs/ntl/ntl_lzz_decl.pxd seems generally broken: shouldn't those be zz_p and lzz_p, not zz and lzz?\n\nIt's even worse than that, this file just shouldn't exist :)\nThe last patch replaces all previous ones and should be almost ready for review. I will just check and address the comments made on #7841 before.",
    "created_at": "2010-02-10T18:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71066",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_8109-lzz_pEX-all_in_one.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX-all_in_one.patch) by ylchapuy created at 2010-02-10 18:41:53

Replying to [comment:6 roed]:
> I see that you changed it to "needs work."  One thing I noticed looking at the patch was that sage/libs/ntl/ntl_lzz_decl.pxd seems generally broken: shouldn't those be zz_p and lzz_p, not zz and lzz?

It's even worse than that, this file just shouldn't exist :)
The last patch replaces all previous ones and should be almost ready for review. I will just check and address the comments made on #7841 before.



---

archive/issue_comments_071067.json:
```json
{
    "body": "Attachment [trac_8109-lzz_pEX-copyrights.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX-copyrights.patch) by ylchapuy created at 2010-03-10 11:33:00",
    "created_at": "2010-03-10T11:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71067",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_8109-lzz_pEX-copyrights.patch](tarball://root/attachments/some-uuid/ticket8109/trac_8109-lzz_pEX-copyrights.patch) by ylchapuy created at 2010-03-10 11:33:00



---

archive/issue_comments_071068.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-10T11:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71068",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071069.json:
```json
{
    "body": "Apply only:\n\n* trac_8109-lzz_pEX-all_in_one.patch\n* trac_8109-lzz_pEX-copyrights.patch\n\nin this order.",
    "created_at": "2010-03-10T11:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71069",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Apply only:

* trac_8109-lzz_pEX-all_in_one.patch
* trac_8109-lzz_pEX-copyrights.patch

in this order.



---

archive/issue_comments_071070.json:
```json
{
    "body": "I get doctest failures on sage.math:\n\n\n```\nsage -t  devel/sage/sage/graphs/graph_list.py # 0 doctests failed\nsage -t  devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py # Killed/crashed\nsage -t  devel/sage/sage/libs/ntl/ntl_lzz_pX.pyx # 5 doctests failed\nsage -t  devel/sage/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi # 3 doctests failed\n```\n\n\nLooks like a 64-bit thing?\n\n\n```\nsage -t  devel/sage/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi\n**********************************************************************\nFile \"/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi\", line 178:\n    sage: (1+a+a^2)*x - (1+x+x^2)\nExpected:\n    1152921504606847008*x^2 + (a^2 + a)*x + 1152921504606847008\nGot:\n    1030*x^2 + (a^2 + a)*x + 1030\n**********************************************************************\nFile \"/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi\", line 189:\n    sage: -x\nExpected:\n    1152921504606847008*x\nGot:\n    1030*x\n**********************************************************************\nFile \"/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi\", line 308:\n    sage: (a+1+x).xgcd(a+x)\nExpected:\n    (1, 1, 1152921504606847008)\nGot:\n    (1, 1, 1030)\n**********************************************************************\n```\n",
    "created_at": "2010-04-14T10:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71070",
    "user": "https://github.com/malb"
}
```

I get doctest failures on sage.math:


```
sage -t  devel/sage/sage/graphs/graph_list.py # 0 doctests failed
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py # Killed/crashed
sage -t  devel/sage/sage/libs/ntl/ntl_lzz_pX.pyx # 5 doctests failed
sage -t  devel/sage/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi # 3 doctests failed
```


Looks like a 64-bit thing?


```
sage -t  devel/sage/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi", line 178:
    sage: (1+a+a^2)*x - (1+x+x^2)
Expected:
    1152921504606847008*x^2 + (a^2 + a)*x + 1152921504606847008
Got:
    1030*x^2 + (a^2 + a)*x + 1030
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi", line 189:
    sage: -x
Expected:
    1152921504606847008*x
Got:
    1030*x
**********************************************************************
File "/mnt/usb1/scratch/malb/sage-4.3.3/devel/sage-main/sage/libs/ntl/ntl_lzz_pEX_linkage.pxi", line 308:
    sage: (a+1+x).xgcd(a+x)
Expected:
    (1, 1, 1152921504606847008)
Got:
    (1, 1, 1030)
**********************************************************************
```




---

archive/issue_comments_071071.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-14T10:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71071",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071072.json:
```json
{
    "body": "The patch needs to be rebased as well.",
    "created_at": "2011-08-19T12:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8109#issuecomment-71072",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

The patch needs to be rebased as well.
