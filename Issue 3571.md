# Issue 3571: ivalue field in integer_mod.pyx shouldn't be public

archive/issues_003571.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThe `ivalue` field for `IntegerMod_int` is `public`, but it shouldn't be. The following is very frightening, for instance:\n\n\n```\nsage: R = Integers(10)\nsage: x = R(2)\nsage: x\n2\nsage: x.ivalue = 33\nsage: x\n33\nsage: R(2)\n33\n```\n\n\nIt's easy to make this field no longer be public, but lots of things are using the fact that it is, so one needs to go through and make everything work correctly again.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3571\n\n",
    "created_at": "2008-07-06T20:55:32Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "ivalue field in integer_mod.pyx shouldn't be public",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3571",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

The `ivalue` field for `IntegerMod_int` is `public`, but it shouldn't be. The following is very frightening, for instance:


```
sage: R = Integers(10)
sage: x = R(2)
sage: x
2
sage: x.ivalue = 33
sage: x
33
sage: R(2)
33
```


It's easy to make this field no longer be public, but lots of things are using the fact that it is, so one needs to go through and make everything work correctly again.

Issue created by migration from https://trac.sagemath.org/ticket/3571





---

archive/issue_comments_025224.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T08:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3571#issuecomment-25224",
    "user": "@craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025225.json:
```json
{
    "body": "The attached patch fixes this issue, and in fact, gives about a 1.5-2X speedup on multiplying `IntegerMod_int`s. The interesting part is that previous to this patch, the `ivalue` field was occasionally being accessed as a Python attribute instead of a Cython attribute! That's why it broke if we made the field not `public` in the first place. Oops.\n\nBEFORE:\n\n\n```\nsage: R = Integers(100) ; x = R(3) ; y = R(5)\nsage: timeit('x*y')\n625 loops, best of 3: 403 ns per loop\nsage: timeit('x*y')\n625 loops, best of 3: 370 ns per loop\nsage: timeit('x*y')\n625 loops, best of 3: 410 ns per loop\nsage: timeit('x*y')\n625 loops, best of 3: 405 ns per loop\n```\n\n\nAFTER:\n\n\n```\nsage: R = Integers(100) ; x = R(3) ; y = R(5)\nsage: timeit('x*y')\n625 loops, best of 3: 190 ns per loop\nsage: timeit('x*y')\n625 loops, best of 3: 213 ns per loop\nsage: timeit('x*y')\n625 loops, best of 3: 174 ns per loop\nsage: timeit('x*y')\n625 loops, best of 3: 191 ns per loop\n```\n",
    "created_at": "2009-01-23T08:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3571#issuecomment-25225",
    "user": "@craigcitro"
}
```

The attached patch fixes this issue, and in fact, gives about a 1.5-2X speedup on multiplying `IntegerMod_int`s. The interesting part is that previous to this patch, the `ivalue` field was occasionally being accessed as a Python attribute instead of a Cython attribute! That's why it broke if we made the field not `public` in the first place. Oops.

BEFORE:


```
sage: R = Integers(100) ; x = R(3) ; y = R(5)
sage: timeit('x*y')
625 loops, best of 3: 403 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 370 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 410 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 405 ns per loop
```


AFTER:


```
sage: R = Integers(100) ; x = R(3) ; y = R(5)
sage: timeit('x*y')
625 loops, best of 3: 190 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 213 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 174 ns per loop
sage: timeit('x*y')
625 loops, best of 3: 191 ns per loop
```




---

archive/issue_comments_025226.json:
```json
{
    "body": "Attachment [trac-3571.patch](tarball://root/attachments/some-uuid/ticket3571/trac-3571.patch) by @robertwb created at 2009-01-23 08:09:47",
    "created_at": "2009-01-23T08:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3571#issuecomment-25226",
    "user": "@robertwb"
}
```

Attachment [trac-3571.patch](tarball://root/attachments/some-uuid/ticket3571/trac-3571.patch) by @robertwb created at 2009-01-23 08:09:47



---

archive/issue_comments_025227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3571#issuecomment-25227",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025228.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T09:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3571#issuecomment-25228",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael
