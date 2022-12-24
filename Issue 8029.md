# Issue 8029: Defect: Power series over a polynomial ring with real coefficients

archive/issues_008029.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  mjo mhansen\n\nKeywords: polynomial ring, power series\n\nSage 4.3 in a PowerPC Mac:\n\n```\nsage: A.<x> = RR['x']\nsage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]]\nsage: 1. + O(t)\n1.00000000000000 + O(t)\nsage: 1. + O(t^2)\n1.00000000000000 + O(t^2)\nsage: 1. + O(t^3)\n1.00000000000000 + O(t^3)\nsage: 1. + O(t^4)\n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_INVALID_ADDRESS at address: 0xffffffe4\n__pyx_f_4sage_5rings_10polynomial_26polynomial_real_mpfr_dense_19PolynomialRealDense__add_ (__pyx_v_left=0x14096f8, __pyx_v__right=0x10fc6260, __pyx_skip_dispatch=0) at sage/rings/polynomial/polynomial_real_mpfr_dense.c:5360\n5360    sage/rings/polynomial/polynomial_real_mpfr_dense.c: No such file or directory.\n        in sage/rings/polynomial/polynomial_real_mpfr_dense.c\n```\n\n\nNOTE: Bug was not present in Sage v2.9.1, but was already present in v3.4 (running on 64-bit Opteron). It is *not* triggered over QQ as basefield.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8029\n\n",
    "created_at": "2010-01-21T18:47:19Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "Defect: Power series over a polynomial ring with real coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8029",
    "user": "eduenez"
}
```
Assignee: AlexGhitza

CC:  mjo mhansen

Keywords: polynomial ring, power series

Sage 4.3 in a PowerPC Mac:

```
sage: A.<x> = RR['x']
sage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]]
sage: 1. + O(t)
1.00000000000000 + O(t)
sage: 1. + O(t^2)
1.00000000000000 + O(t^2)
sage: 1. + O(t^3)
1.00000000000000 + O(t^3)
sage: 1. + O(t^4)

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0xffffffe4
__pyx_f_4sage_5rings_10polynomial_26polynomial_real_mpfr_dense_19PolynomialRealDense__add_ (__pyx_v_left=0x14096f8, __pyx_v__right=0x10fc6260, __pyx_skip_dispatch=0) at sage/rings/polynomial/polynomial_real_mpfr_dense.c:5360
5360    sage/rings/polynomial/polynomial_real_mpfr_dense.c: No such file or directory.
        in sage/rings/polynomial/polynomial_real_mpfr_dense.c
```


NOTE: Bug was not present in Sage v2.9.1, but was already present in v3.4 (running on 64-bit Opteron). It is *not* triggered over QQ as basefield.

Issue created by migration from https://trac.sagemath.org/ticket/8029





---

archive/issue_comments_070129.json:
```json
{
    "body": "Attachment [sage-trac_8029.patch](tarball://root/attachments/some-uuid/ticket8029/sage-trac_8029.patch) by mjo created at 2011-12-16 06:15:48\n\nAdd a doctest from the description",
    "created_at": "2011-12-16T06:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70129",
    "user": "mjo"
}
```

Attachment [sage-trac_8029.patch](tarball://root/attachments/some-uuid/ticket8029/sage-trac_8029.patch) by mjo created at 2011-12-16 06:15:48

Add a doctest from the description



---

archive/issue_comments_070130.json:
```json
{
    "body": "I don't have a PowerPC Mac, but I do have 64-bit Linux. I believe this is fixed, so I've added a doctest for it.",
    "created_at": "2011-12-16T06:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70130",
    "user": "mjo"
}
```

I don't have a PowerPC Mac, but I do have 64-bit Linux. I believe this is fixed, so I've added a doctest for it.



---

archive/issue_comments_070131.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-16T06:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70131",
    "user": "mjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070132.json:
```json
{
    "body": "We should probably double-check on PowerPC.",
    "created_at": "2011-12-18T10:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70132",
    "user": "mhansen"
}
```

We should probably double-check on PowerPC.



---

archive/issue_comments_070133.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> We should probably double-check on PowerPC.\n\nMac OS X 105.8, Dual 2.5 GHz PowerPC G5\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: A.<x> = RR['x'] \nsage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]] \nsage: 1. + O(t) \n1.00000000000000 + O(t)\nsage: 1. + O(t^2) \n1.00000000000000 + O(t^2)\nsage: 1. + O(t^3) \n1.00000000000000 + O(t^3)\nsage: 1. + O(t^4) \n1.00000000000000 + O(t^4)\n```\n",
    "created_at": "2011-12-20T12:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70133",
    "user": "fwclarke"
}
```

Replying to [comment:4 mhansen]:
> We should probably double-check on PowerPC.

Mac OS X 105.8, Dual 2.5 GHz PowerPC G5

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A.<x> = RR['x'] 
sage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]] 
sage: 1. + O(t) 
1.00000000000000 + O(t)
sage: 1. + O(t^2) 
1.00000000000000 + O(t^2)
sage: 1. + O(t^3) 
1.00000000000000 + O(t^3)
sage: 1. + O(t^4) 
1.00000000000000 + O(t^4)
```




---

archive/issue_comments_070134.json:
```json
{
    "body": "Changing keywords from \"polynomial ring, power series\" to \"polynomial ring, power series, sd35\".",
    "created_at": "2011-12-20T12:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70134",
    "user": "mhansen"
}
```

Changing keywords from "polynomial ring, power series" to "polynomial ring, power series, sd35".



---

archive/issue_comments_070135.json:
```json
{
    "body": "Nice -- I'll give this a positive review then.",
    "created_at": "2011-12-20T12:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70135",
    "user": "mhansen"
}
```

Nice -- I'll give this a positive review then.



---

archive/issue_comments_070136.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-20T12:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70136",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070137.json:
```json
{
    "body": "In private communication last night, Robert Campbell wrote to me and mjo:\n\n```\nRunning Sage v 4.7.2 on a PowerMac G5 running OSX 10.5.8 it seems to work.  If desired I can take the time to compile and run one of the 4.8 alphas, but that may take a few days until I can find the time.\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: A.<x> = RR['x']\nsage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]]\nsage: 1. + O(t)\n1.00000000000000 + O(t)\nsage: 1. + O(t^2)\n1.00000000000000 + O(t^2)\nsage: 1. + O(t^3)\n1.00000000000000 + O(t^3)\nsage: 1. + O(t^4)\n1.00000000000000 + O(t^4)\nsage:\n```\n\nThat's a lot of confirmation.",
    "created_at": "2011-12-20T14:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70137",
    "user": "kcrisman"
}
```

In private communication last night, Robert Campbell wrote to me and mjo:

```
Running Sage v 4.7.2 on a PowerMac G5 running OSX 10.5.8 it seems to work.  If desired I can take the time to compile and run one of the 4.8 alphas, but that may take a few days until I can find the time.

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A.<x> = RR['x']
sage: B.<t> = PowerSeriesRing(A) # B = R[x][[t]]
sage: 1. + O(t)
1.00000000000000 + O(t)
sage: 1. + O(t^2)
1.00000000000000 + O(t^2)
sage: 1. + O(t^3)
1.00000000000000 + O(t^3)
sage: 1. + O(t^4)
1.00000000000000 + O(t^4)
sage:
```

That's a lot of confirmation.



---

archive/issue_comments_070138.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-24T01:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8029#issuecomment-70138",
    "user": "jdemeyer"
}
```

Resolution: fixed
