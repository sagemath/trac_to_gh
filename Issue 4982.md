# Issue 4982: consolidate shifts in polynomial_template

archive/issues_004982.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @malb @burcin\n\nSee discussion at end of #4965. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4982\n\n",
    "created_at": "2009-01-15T19:57:37Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "consolidate shifts in polynomial_template",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4982",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

CC:  @malb @burcin

See discussion at end of #4965. 

Issue created by migration from https://trac.sagemath.org/ticket/4982





---

archive/issue_comments_037905.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37905",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_037906.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T22:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37906",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_037907.json:
```json
{
    "body": "The point was to consolidate the three shift methods `shift`, `__lshift__`, and `__rshift__` by having `shift` do all the work and the other two call it.  (Right now there's significant code triplication going on.)\n\nThe attached patch does this.",
    "created_at": "2009-11-16T05:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37907",
    "user": "https://github.com/aghitza"
}
```

The point was to consolidate the three shift methods `shift`, `__lshift__`, and `__rshift__` by having `shift` do all the work and the other two call it.  (Right now there's significant code triplication going on.)

The attached patch does this.



---

archive/issue_comments_037908.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-16T05:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37908",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037909.json:
```json
{
    "body": "Attachment [trac_4982.patch](tarball://root/attachments/some-uuid/ticket4982/trac_4982.patch) by @aghitza created at 2009-11-16 05:37:45\n\nI'm ccing the participants in the discussion at #4965 in case they had something else in mind.",
    "created_at": "2009-11-16T05:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37909",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4982.patch](tarball://root/attachments/some-uuid/ticket4982/trac_4982.patch) by @aghitza created at 2009-11-16 05:37:45

I'm ccing the participants in the discussion at #4965 in case they had something else in mind.



---

archive/issue_comments_037910.json:
```json
{
    "body": "The only issue I can see is the potential performance overhead.\n\nVanilla 4.2.1:\n\n\n```\nsage: P.<x> = GF(2)[]\nsage: f = P.random_element(50)\nsage: %timeit f<<50\n1000000 loops, best of 3: 792 ns per loop\n```\n\n\nThis patch:\n\n\n```\nsage: P.<x> = GF(2)[]\nsage: f = P.random_element(50)\nsage: %timeit f<<50\n1000000 loops, best of 3: 952 ns per loop\n```\n\n\nMaybe a cdef method could be added which everyone (`shift`, `__lshift__`, `__rshift__`) calls?",
    "created_at": "2009-11-16T12:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37910",
    "user": "https://github.com/malb"
}
```

The only issue I can see is the potential performance overhead.

Vanilla 4.2.1:


```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(50)
sage: %timeit f<<50
1000000 loops, best of 3: 792 ns per loop
```


This patch:


```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(50)
sage: %timeit f<<50
1000000 loops, best of 3: 952 ns per loop
```


Maybe a cdef method could be added which everyone (`shift`, `__lshift__`, `__rshift__`) calls?



---

archive/issue_comments_037911.json:
```json
{
    "body": "Doctests pass btw., applies cleanly etc.",
    "created_at": "2009-11-16T13:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37911",
    "user": "https://github.com/malb"
}
```

Doctests pass btw., applies cleanly etc.



---

archive/issue_comments_037912.json:
```json
{
    "body": "Attachment [trac_4982_speedup.patch](tarball://root/attachments/some-uuid/ticket4982/trac_4982_speedup.patch) by @malb created at 2009-11-20 10:49:37\n\nAlex and I were discussing this off-list. The speedup patch does the following:\n\n* added a new C function which all methods call now \n* I inlined it\n* and I changed the code to avoid some initialisation\n\nHere is what I got:\n\n**Vanilla:**\n\n```\nsage: P.<x> = GF(2)[]\nsage: f = P.random_element(50)\nsage: %timeit f<<50\n1000000 loops, best of 3: 730 ns per loop\n```\n\n\n**Patch:**\n\n```\nsage: P.<x> = GF(2)[]\nsage: f = P.random_element(50)\nsage: %timeit f<<50\n1000000 loops, best of 3: 1.06 \u00b5s per loop\n```\n\n\n**Patch + Speed-up:**\n\n```\nsage: P.<x> = GF(2)[]\nsage: %timeit f<<50\n1000000 loops, best of 3: 761 ns per loop\n```\n\n\nSo there is still some overhead, but I think its acceptable.",
    "created_at": "2009-11-20T10:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37912",
    "user": "https://github.com/malb"
}
```

Attachment [trac_4982_speedup.patch](tarball://root/attachments/some-uuid/ticket4982/trac_4982_speedup.patch) by @malb created at 2009-11-20 10:49:37

Alex and I were discussing this off-list. The speedup patch does the following:

* added a new C function which all methods call now 
* I inlined it
* and I changed the code to avoid some initialisation

Here is what I got:

**Vanilla:**

```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(50)
sage: %timeit f<<50
1000000 loops, best of 3: 730 ns per loop
```


**Patch:**

```
sage: P.<x> = GF(2)[]
sage: f = P.random_element(50)
sage: %timeit f<<50
1000000 loops, best of 3: 1.06 µs per loop
```


**Patch + Speed-up:**

```
sage: P.<x> = GF(2)[]
sage: %timeit f<<50
1000000 loops, best of 3: 761 ns per loop
```


So there is still some overhead, but I think its acceptable.



---

archive/issue_comments_037913.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-22T22:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37913",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037914.json:
```json
{
    "body": "So I believe that Martin gave a positive review to my patch, except for the performance issue.\n\nI have read and tested his patch, and I'm happy with it.",
    "created_at": "2009-11-22T22:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37914",
    "user": "https://github.com/aghitza"
}
```

So I believe that Martin gave a positive review to my patch, except for the performance issue.

I have read and tested his patch, and I'm happy with it.



---

archive/issue_events_005225.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-29T04:44:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4982#event-5225"
}
```



---

archive/issue_comments_037915.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T04:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37915",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
