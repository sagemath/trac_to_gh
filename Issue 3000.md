# Issue 3000: Some packages don't respect the CXX environment variable

archive/issues_003000.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @orlitzky\n\nPackages which seem not to honor CXX environment variable (they use \"g++\")\n\n```\npolybori-0.3.1.p1\nrubiks-20070912.p5\nsage-3.0.rc1\ngfan-0.3.p3\nflintqs-20070817.p3\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3000\n\n",
    "created_at": "2008-04-22T16:43:16Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Some packages don't respect the CXX environment variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3000",
    "user": "@dfdeshom"
}
```
Assignee: mabshoff

CC:  @orlitzky

Packages which seem not to honor CXX environment variable (they use "g++")

```
polybori-0.3.1.p1
rubiks-20070912.p5
sage-3.0.rc1
gfan-0.3.p3
flintqs-20070817.p3
```


Issue created by migration from https://trac.sagemath.org/ticket/3000





---

archive/issue_comments_020641.json:
```json
{
    "body": "See #2999 for PolyBoRi,\n\nRegards,\n  Alexander",
    "created_at": "2008-04-22T21:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20641",
    "user": "PolyBoRi"
}
```

See #2999 for PolyBoRi,

Regards,
  Alexander



---

archive/issue_comments_020642.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-26T10:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20642",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020643.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-27T15:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20643",
    "user": "@orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_020644.json:
```json
{
    "body": "These are fixed or have their own tickets:\n\n* flintqs: #12428\n* gfan: #7820\n* rubiks: #7036\n* sage: #12443\n\nAs with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.",
    "created_at": "2012-02-27T15:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20644",
    "user": "@orlitzky"
}
```

These are fixed or have their own tickets:

* flintqs: #12428
* gfan: #7820
* rubiks: #7036
* sage: #12443

As with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.



---

archive/issue_comments_020645.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-27T18:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20645",
    "user": "@ohanar"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_020646.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-03-04T21:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20646",
    "user": "@jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_020647.json:
```json
{
    "body": "Replying to [comment:3 mjo]:\n> These are fixed or have their own tickets:\n> \n>  * flintqs: #12428\n>  * gfan: #7820\n>  * rubiks: #7036\n>  * sage: #12443\n> \n> As with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.\n\nI wouldn't have closed this ticket.  There's at least still Lcalc with its ugly `Makefile`, using `CC` and `CCFLAGS`[sic] for compiling C as well as C++, hardcoding `CC` to `g++`, and even Singular apparently has an instance of a hardcoded `g++`.",
    "created_at": "2012-03-17T02:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20647",
    "user": "@nexttime"
}
```

Replying to [comment:3 mjo]:
> These are fixed or have their own tickets:
> 
>  * flintqs: #12428
>  * gfan: #7820
>  * rubiks: #7036
>  * sage: #12443
> 
> As with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.

I wouldn't have closed this ticket.  There's at least still Lcalc with its ugly `Makefile`, using `CC` and `CCFLAGS`[sic] for compiling C as well as C++, hardcoding `CC` to `g++`, and even Singular apparently has an instance of a hardcoded `g++`.



---

archive/issue_comments_020648.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> Replying to [comment:3 mjo]:\n> > These are fixed or have their own tickets:\n> > \n> >  * flintqs: #12428\n> >  * gfan: #7820\n> >  * rubiks: #7036\n> >  * sage: #12443\n> > \n> > As with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.\n> \n> I wouldn't have closed this ticket.  There's at least still Lcalc with its ugly `Makefile`, using `CC` and `CCFLAGS`[sic] for compiling C as well as C++, hardcoding `CC` to `g++`, and even Singular apparently has an instance of a hardcoded `g++`.\n\nSingular (3-1-3-3) is now #12680 (**needs review**).\n\nI've also fixed the Lcalc spkg, but haven't yet opened a ticket for that.",
    "created_at": "2012-03-17T11:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20648",
    "user": "@nexttime"
}
```

Replying to [comment:7 leif]:
> Replying to [comment:3 mjo]:
> > These are fixed or have their own tickets:
> > 
> >  * flintqs: #12428
> >  * gfan: #7820
> >  * rubiks: #7036
> >  * sage: #12443
> > 
> > As with `$CC`, it looks like polybori is fixed, but I can't pin down the ticket where it happened.
> 
> I wouldn't have closed this ticket.  There's at least still Lcalc with its ugly `Makefile`, using `CC` and `CCFLAGS`[sic] for compiling C as well as C++, hardcoding `CC` to `g++`, and even Singular apparently has an instance of a hardcoded `g++`.

Singular (3-1-3-3) is now #12680 (**needs review**).

I've also fixed the Lcalc spkg, but haven't yet opened a ticket for that.



---

archive/issue_comments_020649.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> I've also fixed the Lcalc spkg, but haven't yet opened a ticket for that.\n\nThis is now #12681 (soon **needing review**).",
    "created_at": "2012-03-17T11:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3000#issuecomment-20649",
    "user": "@nexttime"
}
```

Replying to [comment:8 leif]:
> I've also fixed the Lcalc spkg, but haven't yet opened a ticket for that.

This is now #12681 (soon **needing review**).
