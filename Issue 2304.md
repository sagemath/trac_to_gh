# Issue 2304: sparse_poly should probably be removed

archive/issues_002304.json:
```json
{
    "body": "Assignee: somebody\n\nIt looks like the module `sage.rings.sparse_poly` is deprecated and should be removed. I can't find any other references to it in the Sage library. Awaiting confirmation from wstein.\n\nfrom IRC:\n\n```\ncwitty: according to  search_src('sparse_poly') it's never referred to (never imported, etc.)...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2304\n\n",
    "created_at": "2008-02-25T21:31:04Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "sparse_poly should probably be removed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2304",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

It looks like the module `sage.rings.sparse_poly` is deprecated and should be removed. I can't find any other references to it in the Sage library. Awaiting confirmation from wstein.

from IRC:

```
cwitty: according to  search_src('sparse_poly') it's never referred to (never imported, etc.)...
```


Issue created by migration from https://trac.sagemath.org/ticket/2304





---

archive/issue_events_005433.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-25T21:34:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2304#event-5433"
}
```



---

archive/issue_comments_015296.json:
```json
{
    "body": "But David, my code's so fast.  Could YOU square sum(n*x^n for n in range(1000))\nin less than 1.24 seconds!?  :-)\n\n\nSeriously though, I wrote that code before version 0.1 of Sage as an experiment.  It can safely be removed.  If one really did want sparse polys that are fast, the best thing for now would probably to use libsingular  with one variable, e.g., \n\n```\nsage: R.<x,y> = MPolynomialRing(QQ,2)\nsage: type(x)\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\nsage: f = sum(n*x^(n^2) for n in primes(100))\nsage: time g = f*f\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\nsage: timeit('z=f*f')\n625 loops, best of 3: 35.5 \u00b5s per loop\n\n```\n\nThat said Singular polys only allow degrees up to 65K:\n\n```\nsage: x^66000\n<type 'exceptions.TypeError'>: exponent is too large, max. is 65535\n```\n\nSo I say delete sparse_poly.* from Sage.  If we someday want sparse polys that code could be revisited, or maybe flint will already have something much better.",
    "created_at": "2008-02-25T21:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2304#issuecomment-15296",
    "user": "https://github.com/williamstein"
}
```

But David, my code's so fast.  Could YOU square sum(n*x^n for n in range(1000))
in less than 1.24 seconds!?  :-)


Seriously though, I wrote that code before version 0.1 of Sage as an experiment.  It can safely be removed.  If one really did want sparse polys that are fast, the best thing for now would probably to use libsingular  with one variable, e.g., 

```
sage: R.<x,y> = MPolynomialRing(QQ,2)
sage: type(x)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: f = sum(n*x^(n^2) for n in primes(100))
sage: time g = f*f
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: timeit('z=f*f')
625 loops, best of 3: 35.5 µs per loop

```

That said Singular polys only allow degrees up to 65K:

```
sage: x^66000
<type 'exceptions.TypeError'>: exponent is too large, max. is 65535
```

So I say delete sparse_poly.* from Sage.  If we someday want sparse polys that code could be revisited, or maybe flint will already have something much better.



---

archive/issue_comments_015297.json:
```json
{
    "body": "Still there in 3.2.1, but trivial to fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-22T23:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2304#issuecomment-15297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Still there in 3.2.1, but trivial to fix.

Cheers,

Michael



---

archive/issue_comments_015298.json:
```json
{
    "body": "Changing assignee from somebody to mabshoff.",
    "created_at": "2008-11-22T23:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2304#issuecomment-15298",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to mabshoff.



---

archive/issue_comments_015299.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-22T23:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2304#issuecomment-15299",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015300.json:
```json
{
    "body": "Attachment [trac_2304.patch](tarball://root/attachments/some-uuid/ticket2304/trac_2304.patch) by mabshoff created at 2008-11-22 23:52:35",
    "created_at": "2008-11-22T23:52:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2304#issuecomment-15300",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2304.patch](tarball://root/attachments/some-uuid/ticket2304/trac_2304.patch) by mabshoff created at 2008-11-22 23:52:35



---

archive/issue_comments_015301.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2008-11-22T23:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2304#issuecomment-15301",
    "user": "https://github.com/ncalexan"
}
```

Fine by me.



---

archive/issue_events_005434.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-23T00:04:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2304#event-5434"
}
```



---

archive/issue_comments_015302.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-23T00:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2304#issuecomment-15302",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_015303.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T00:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2304#issuecomment-15303",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
