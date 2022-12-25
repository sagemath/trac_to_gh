# Issue 528: write new Integer_mod_dense class that wraps NTL directly

archive/issues_000528.json:
```json
{
    "body": "Assignee: dmharvey\n\nCurrently `Integer_mod_dense` wraps the `ZZX` class in `ntl.pyx`. This causes a lot of overhead for small polynomials.\n\nIssue created by migration from https://trac.sagemath.org/ticket/528\n\n",
    "created_at": "2007-08-30T13:20:50Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "write new Integer_mod_dense class that wraps NTL directly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/528",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: dmharvey

Currently `Integer_mod_dense` wraps the `ZZX` class in `ntl.pyx`. This causes a lot of overhead for small polynomials.

Issue created by migration from https://trac.sagemath.org/ticket/528





---

archive/issue_comments_002675.json:
```json
{
    "body": "related: #331",
    "created_at": "2007-09-11T00:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2675",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

related: #331



---

archive/issue_comments_002676.json:
```json
{
    "body": "Attachment [poly-int-dense1.hg](tarball://root/attachments/some-uuid/ticket528/poly-int-dense1.hg) by dmharvey created at 2007-09-11 15:01:23\n\nmoves Polynomial_integer_dense to cython",
    "created_at": "2007-09-11T15:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2676",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [poly-int-dense1.hg](tarball://root/attachments/some-uuid/ticket528/poly-int-dense1.hg) by dmharvey created at 2007-09-11 15:01:23

moves Polynomial_integer_dense to cython



---

archive/issue_comments_002677.json:
```json
{
    "body": "The patch `poly-int-dense1.hg` moves `Polynomial_integer_dense` to a new cython file `polynomial_integer_dense_ntl.pyx` and renames the class to `Polynomial_integer_dense_ntl`, and minimal changes needed to make this build and pass tests.\n\nThis is the first step in addressing this ticket. Next step will be to change the underlying implementation to work with the NTL ZZX object directly instead of via `ntl.pyx`.\n\nAlready there's an improvement in overheads for arithmetic on small objects:\n\n```\nsage: R.<x> = PolynomialRing(ZZ)\nsage: f = x^2 + x^3 - 5*x^4\nsage: g = 47*x^2 + 3\nsage: timeit h = f * g\n10000 loops, best of 3: 23.8 \u00b5s per loop\n```\n\nvs\n\n```\n100000 loops, best of 3: 17.7 \u00b5s per loop\n```\n",
    "created_at": "2007-09-11T15:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2677",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

The patch `poly-int-dense1.hg` moves `Polynomial_integer_dense` to a new cython file `polynomial_integer_dense_ntl.pyx` and renames the class to `Polynomial_integer_dense_ntl`, and minimal changes needed to make this build and pass tests.

This is the first step in addressing this ticket. Next step will be to change the underlying implementation to work with the NTL ZZX object directly instead of via `ntl.pyx`.

Already there's an improvement in overheads for arithmetic on small objects:

```
sage: R.<x> = PolynomialRing(ZZ)
sage: f = x^2 + x^3 - 5*x^4
sage: g = 47*x^2 + 3
sage: timeit h = f * g
10000 loops, best of 3: 23.8 µs per loop
```

vs

```
100000 loops, best of 3: 17.7 µs per loop
```




---

archive/issue_comments_002678.json:
```json
{
    "body": "Some thoughts to consider: \n\n* How far away is FLINT from doing the basic arithmetic at least? If it is close, how much effort should be spent on this? \n* Is there anything to learn from the re-wrapping of NTL by Craig Citro and Joel Mohler?",
    "created_at": "2007-09-11T21:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2678",
    "user": "https://github.com/robertwb"
}
```

Some thoughts to consider: 

* How far away is FLINT from doing the basic arithmetic at least? If it is close, how much effort should be spent on this? 
* Is there anything to learn from the re-wrapping of NTL by Craig Citro and Joel Mohler?



---

archive/issue_comments_002679.json:
```json
{
    "body": "> How far away is FLINT from doing the basic arithmetic at least? If it is close, how much effort should be spent on this?\n\nI don't know. I am not working on FLINT presently due to lack of time. The amount of effort required to get FLINT to production standard appears to be way more than the time required to get this ticket done.\n\n> Is there anything to learn from the re-wrapping of NTL by Craig Citro and Joel Mohler?\n\nYes most definitely. I've discussed with this Joel, and I'll be studying that code before moving onto the next phase.",
    "created_at": "2007-09-11T21:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2679",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

> How far away is FLINT from doing the basic arithmetic at least? If it is close, how much effort should be spent on this?

I don't know. I am not working on FLINT presently due to lack of time. The amount of effort required to get FLINT to production standard appears to be way more than the time required to get this ticket done.

> Is there anything to learn from the re-wrapping of NTL by Craig Citro and Joel Mohler?

Yes most definitely. I've discussed with this Joel, and I'll be studying that code before moving onto the next phase.



---

archive/issue_comments_002680.json:
```json
{
    "body": "I've applied the bundle poly-int-dense1.hg to the official repo for the next SAGE release.",
    "created_at": "2007-09-11T21:42:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2680",
    "user": "https://github.com/williamstein"
}
```

I've applied the bundle poly-int-dense1.hg to the official repo for the next SAGE release.



---

archive/issue_comments_002681.json:
```json
{
    "body": "I've added a patch `patch-528.hg`. This makes the `Polynomial_integer_dense_ntl` class talk directly to NTL, instead of wrapping an NTL object from ntl.pyx.\n\nAlso it adds many new doctests for polynomials over Z.\n\nIt's still pretty damn ugly though. Just the minimum to get the job done. A lot of work is still needed.\n\nI think it basically works, but I wasn't able to run doctests properly because there are currently lots of other doctest failures in the repository.",
    "created_at": "2007-09-21T02:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2681",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I've added a patch `patch-528.hg`. This makes the `Polynomial_integer_dense_ntl` class talk directly to NTL, instead of wrapping an NTL object from ntl.pyx.

Also it adds many new doctests for polynomials over Z.

It's still pretty damn ugly though. Just the minimum to get the job done. A lot of work is still needed.

I think it basically works, but I wasn't able to run doctests properly because there are currently lots of other doctest failures in the repository.



---

archive/issue_comments_002682.json:
```json
{
    "body": "Note: `patch-528.hg` replaces an old version of the same name; it should be applied directly to sage 2.8.5. It also includes the patch for #738.",
    "created_at": "2007-09-23T23:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2682",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Note: `patch-528.hg` replaces an old version of the same name; it should be applied directly to sage 2.8.5. It also includes the patch for #738.



---

archive/issue_comments_002683.json:
```json
{
    "body": "hmmm that last patch is currently in conflict. Please ignore it for now; I'm going to work on a new one at SD5 anyway.",
    "created_at": "2007-09-30T19:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2683",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

hmmm that last patch is currently in conflict. Please ignore it for now; I'm going to work on a new one at SD5 anyway.



---

archive/issue_comments_002684.json:
```json
{
    "body": "Attachment [patch-528.hg](tarball://root/attachments/some-uuid/ticket528/patch-528.hg) by dmharvey created at 2007-10-01 01:55:25\n\nhopefully better now",
    "created_at": "2007-10-01T01:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2684",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [patch-528.hg](tarball://root/attachments/some-uuid/ticket528/patch-528.hg) by dmharvey created at 2007-10-01 01:55:25

hopefully better now



---

archive/issue_comments_002685.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T18:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/528#issuecomment-2685",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
