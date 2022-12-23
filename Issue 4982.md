# Issue 4982: consolidate shifts in polynomial_template

archive/issues_004982.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  malb burcin\n\nSee discussion at end of #4965. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4982\n\n",
    "created_at": "2009-01-15T19:57:37Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "consolidate shifts in polynomial_template",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4982",
    "user": "robertwb"
}
```
Assignee: tbd

CC:  malb burcin

See discussion at end of #4965. 

Issue created by migration from https://trac.sagemath.org/ticket/4982





---

archive/issue_comments_037977.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37977",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_037978.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T22:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37978",
    "user": "mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_037979.json:
```json
{
    "body": "The point was to consolidate the three shift methods `shift`, `__lshift__`, and `__rshift__` by having `shift` do all the work and the other two call it.  (Right now there's significant code triplication going on.)\n\nThe attached patch does this.",
    "created_at": "2009-11-16T05:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37979",
    "user": "AlexGhitza"
}
```

The point was to consolidate the three shift methods `shift`, `__lshift__`, and `__rshift__` by having `shift` do all the work and the other two call it.  (Right now there's significant code triplication going on.)

The attached patch does this.



---

archive/issue_comments_037980.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-16T05:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37980",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037981.json:
```json
{
    "body": "Attachment\n\nI'm ccing the participants in the discussion at #4965 in case they had something else in mind.",
    "created_at": "2009-11-16T05:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37981",
    "user": "AlexGhitza"
}
```

Attachment

I'm ccing the participants in the discussion at #4965 in case they had something else in mind.



---

archive/issue_comments_037982.json:
```json
{
    "body": "The only issue I can see is the potential performance overhead.\n\nVanilla 4.2.1:\n\n\n```\nsage: P.<x> = GF(2)[]\nsage: f = P.random_element(50)\nsage: %timeit f<<50\n1000000 loops, best of 3: 792 ns per loop\n```\n\n\nThis patch:\n\n\n```\nsage: P.<x> = GF(2)[]\nsage: f = P.random_element(50)\nsage: %timeit f<<50\n1000000 loops, best of 3: 952 ns per loop\n```\n\n\nMaybe a cdef method could be added which everyone (`shift`, `__lshift__`, `__rshift__`) calls?",
    "created_at": "2009-11-16T12:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37982",
    "user": "malb"
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

archive/issue_comments_037983.json:
```json
{
    "body": "Doctests pass btw., applies cleanly etc.",
    "created_at": "2009-11-16T13:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37983",
    "user": "malb"
}
```

Doctests pass btw., applies cleanly etc.



---

archive/issue_comments_037984.json:
```json
{
    "body": "Attachment\n\nAlex and I were discussing this off-list. The speedup patch does the following:\n\n* added a new C function which all methods call now \n* I inlined it\n* and I changed the code to avoid some initialisation\n\nHere is what I got:\n\n**Vanilla:**\n\n```\nsage: P.<x> = GF(2)[]\nsage: f = P.random_element(50)\nsage: %timeit f<<50\n1000000 loops, best of 3: 730 ns per loop\n```\n\n\n**Patch:**\n\n```\nsage: P.<x> = GF(2)[]\nsage: f = P.random_element(50)\nsage: %timeit f<<50\n1000000 loops, best of 3: 1.06 \u00b5s per loop\n```\n\n\n**Patch + Speed-up:**\n\n```\nsage: P.<x> = GF(2)[]\nsage: %timeit f<<50\n1000000 loops, best of 3: 761 ns per loop\n```\n\n\nSo there is still some overhead, but I think its acceptable.",
    "created_at": "2009-11-20T10:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37984",
    "user": "malb"
}
```

Attachment

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

archive/issue_comments_037985.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-22T22:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37985",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037986.json:
```json
{
    "body": "So I believe that Martin gave a positive review to my patch, except for the performance issue.\n\nI have read and tested his patch, and I'm happy with it.",
    "created_at": "2009-11-22T22:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37986",
    "user": "AlexGhitza"
}
```

So I believe that Martin gave a positive review to my patch, except for the performance issue.

I have read and tested his patch, and I'm happy with it.



---

archive/issue_comments_037987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T04:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4982#issuecomment-37987",
    "user": "mhansen"
}
```

Resolution: fixed
