# Issue 2161: [with patch, with positive review] some speed improvements for mpolynomials over ZZ

archive/issues_002161.json:
```json
{
    "body": "Assignee: @malb\n\nHere's a patch improving some things associated with scalar multiplication over ZZ.\n\nPrior to patch:\n\n```\nsage: R.<x,y,z>=ZZ[]\nsage: f=x+y+z\nsage: timeit f*3\n1000 loops, best of 3: 322 \u00c2\u00b5s per loop\n```\n\nAfter patch:\n\n```\nsage: R.<x,y,z>=ZZ[]\nsage: f=x+y+z\nsage: timeit f*3\n10000 loops, best of 3: 68 \u00c2\u00b5s per loop\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2161\n\n",
    "closed_at": "2008-02-15T00:17:35Z",
    "created_at": "2008-02-14T19:18:02Z",
    "labels": [
        "component: commutative algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, with positive review] some speed improvements for mpolynomials over ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2161",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @malb

Here's a patch improving some things associated with scalar multiplication over ZZ.

Prior to patch:

```
sage: R.<x,y,z>=ZZ[]
sage: f=x+y+z
sage: timeit f*3
1000 loops, best of 3: 322 Âµs per loop
```

After patch:

```
sage: R.<x,y,z>=ZZ[]
sage: f=x+y+z
sage: timeit f*3
10000 loops, best of 3: 68 Âµs per loop
```

Issue created by migration from https://trac.sagemath.org/ticket/2161





---

archive/issue_comments_014160.json:
```json
{
    "body": "Attachment [mpoly-scalar.patch](tarball://root/attachments/some-uuid/ticket2161/mpoly-scalar.patch) by jbmohler created at 2008-02-14 19:19:35\n\nscalar mult optimizations",
    "created_at": "2008-02-14T19:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2161#issuecomment-14160",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [mpoly-scalar.patch](tarball://root/attachments/some-uuid/ticket2161/mpoly-scalar.patch) by jbmohler created at 2008-02-14 19:19:35

scalar mult optimizations



---

archive/issue_comments_014161.json:
```json
{
    "body": "I say apply, it looks good to me.  There are additional improvements, it seems: maybe caching one, and the TODO (typoed to TOOD) about addition and subtraction.",
    "created_at": "2008-02-14T23:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2161#issuecomment-14161",
    "user": "https://github.com/ncalexan"
}
```

I say apply, it looks good to me.  There are additional improvements, it seems: maybe caching one, and the TODO (typoed to TOOD) about addition and subtraction.



---

archive/issue_comments_014162.json:
```json
{
    "body": "Replying to [comment:1 ncalexan]:\n> I say apply, it looks good to me.  There are additional improvements, it seems: maybe caching one, and the TODO (typoed to TOOD) about addition and subtraction.\n\n\nEvery parent should have a one cache called `_one_element` where *should* means that a parent is already supposed to implement it.",
    "created_at": "2008-02-14T23:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2161#issuecomment-14162",
    "user": "https://github.com/malb"
}
```

Replying to [comment:1 ncalexan]:
> I say apply, it looks good to me.  There are additional improvements, it seems: maybe caching one, and the TODO (typoed to TOOD) about addition and subtraction.


Every parent should have a one cache called `_one_element` where *should* means that a parent is already supposed to implement it.



---

archive/issue_events_005170.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-15T00:17:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2161",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2161#event-5170"
}
```



---

archive/issue_comments_014163.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T00:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2161#issuecomment-14163",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014164.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T00:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2161#issuecomment-14164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
