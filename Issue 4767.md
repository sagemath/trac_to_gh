# Issue 4767: [with patch; needs review] magma/sage interface -- speed up conversion of integers and rationals to Magma

archive/issues_004767.json:
```json
{
    "body": "Assignee: @williamstein\n\nUse hex very carefully (magma has issues, let's say) to convert large integers and rationals to Magma much much more quickly than before.  E.g., in the example below the conversion is 22 times faster than it was before -- 3.2 seconds versus 71.47 seconds!\n\n```\nsage: n = ZZ.random_element(x=0,y=2^(10^8))\nsage: time k = magma(n)\nCPU time: 1.03 s,  Wall time: 3.20 s\nsage: time j = magma(str(n))\nCPU time: 54.71 s,  Wall time: 71.47 s\nsage: 71.47/3.20\n22.3343750000000\n```\n\n\nNOTE: The attached patch also speed up is_integral (by a factor of 500!!!) for rational numbers, since I needed that for the rational number conversion speedup.\n \nBEFORE:\n\n```\nsage: n = -485/82847\nsage: n.is_integral()\nFalse\nsage: timeit('n.is_integral()')\n625 loops, best of 3: 160 \u00b5s per loop\n```\n\nAFTER:\n\n```\nsage: n = -485/82847\nsage: n.is_integral()\nFalse\nsage: timeit('n.is_integral()')\n625 loops, best of 3: 294 ns per loop\n```\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4767\n\n",
    "created_at": "2008-12-12T06:17:24Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch; needs review] magma/sage interface -- speed up conversion of integers and rationals to Magma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4767",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Use hex very carefully (magma has issues, let's say) to convert large integers and rationals to Magma much much more quickly than before.  E.g., in the example below the conversion is 22 times faster than it was before -- 3.2 seconds versus 71.47 seconds!

```
sage: n = ZZ.random_element(x=0,y=2^(10^8))
sage: time k = magma(n)
CPU time: 1.03 s,  Wall time: 3.20 s
sage: time j = magma(str(n))
CPU time: 54.71 s,  Wall time: 71.47 s
sage: 71.47/3.20
22.3343750000000
```


NOTE: The attached patch also speed up is_integral (by a factor of 500!!!) for rational numbers, since I needed that for the rational number conversion speedup.
 
BEFORE:

```
sage: n = -485/82847
sage: n.is_integral()
False
sage: timeit('n.is_integral()')
625 loops, best of 3: 160 µs per loop
```

AFTER:

```
sage: n = -485/82847
sage: n.is_integral()
False
sage: timeit('n.is_integral()')
625 loops, best of 3: 294 ns per loop
```





Issue created by migration from https://trac.sagemath.org/ticket/4767





---

archive/issue_comments_036049.json:
```json
{
    "body": "Attachment [trac_4767.patch](tarball://root/attachments/some-uuid/ticket4767/trac_4767.patch) by @williamstein created at 2008-12-12 06:19:42",
    "created_at": "2008-12-12T06:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4767#issuecomment-36049",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4767.patch](tarball://root/attachments/some-uuid/ticket4767/trac_4767.patch) by @williamstein created at 2008-12-12 06:19:42



---

archive/issue_comments_036050.json:
```json
{
    "body": "patch applies cleanly, reads good, doctests pass.",
    "created_at": "2008-12-12T14:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4767#issuecomment-36050",
    "user": "https://github.com/malb"
}
```

patch applies cleanly, reads good, doctests pass.



---

archive/issue_comments_036051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-12T16:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4767#issuecomment-36051",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036052.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-12T16:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4767#issuecomment-36052",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha2
