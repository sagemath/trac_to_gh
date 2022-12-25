# Issue 8166: Expose max_weight_matching from NetworkX

archive/issues_008166.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  ylchapuy @jasongrout mvngu\n\nSince the new version of NetworkX is being merged into Sage, we could use their max matching algorithm. We already have one, though it uses Linear Programming and is optional :\n\nThe efficiency of these two algorithms have to be compared !\n\nBased upon this, the default behaviour could be :\n* To always use NetworkX\n* Only use it if there is no LP available\n* Not to use it if not asked explicitely\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8166\n\n",
    "created_at": "2010-02-03T08:45:32Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Expose max_weight_matching from NetworkX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8166",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  ylchapuy @jasongrout mvngu

Since the new version of NetworkX is being merged into Sage, we could use their max matching algorithm. We already have one, though it uses Linear Programming and is optional :

The efficiency of these two algorithms have to be compared !

Based upon this, the default behaviour could be :
* To always use NetworkX
* Only use it if there is no LP available
* Not to use it if not asked explicitely

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8166





---

archive/issue_comments_071727.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71727",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_071728.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-15T19:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71728",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071729.json:
```json
{
    "body": "As max_weight_matching had been exposed while I wasn't looking, this ticket now merges the two function into only one, for the better I hope ! :-)\n\nFrom now on, maximum matching are not optional anymore, and are way faster !\n\n\n```\nsage: g = graphs.RandomGNP(50,.3)\nsage: %timeit g.matching(algorithm=\"LP\",solver=\"GLPK\")\n5 loops, best of 3: 248 ms per loop\nsage: %timeit g.matching()\n25 loops, best of 3: 16.9 ms per loop\n```\n\n\nThe two different ways to solve matchings are kept, just in case.... But network'x version is now the default one, obviously :-)\n\nRequires #8364\n\nNathann",
    "created_at": "2010-05-15T19:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71729",
    "user": "https://github.com/nathanncohen"
}
```

As max_weight_matching had been exposed while I wasn't looking, this ticket now merges the two function into only one, for the better I hope ! :-)

From now on, maximum matching are not optional anymore, and are way faster !


```
sage: g = graphs.RandomGNP(50,.3)
sage: %timeit g.matching(algorithm="LP",solver="GLPK")
5 loops, best of 3: 248 ms per loop
sage: %timeit g.matching()
25 loops, best of 3: 16.9 ms per loop
```


The two different ways to solve matchings are kept, just in case.... But network'x version is now the default one, obviously :-)

Requires #8364

Nathann



---

archive/issue_comments_071730.json:
```json
{
    "body": "Attachment [trac_8166.patch](tarball://root/attachments/some-uuid/ticket8166/trac_8166.patch) by mvngu created at 2010-05-21 15:45:14\n\nI have attached a rebase of ncohen's patch, rebased on top of #8364. Based upon that, I did some clean-ups of the changes proposed by ncohen. My changes are mainly cosmetic clean-ups along the lines of PEP 008. Both ncohen's patch and my changes are folded into one patch to make it easier for anyone to give a final review.",
    "created_at": "2010-05-21T15:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8166.patch](tarball://root/attachments/some-uuid/ticket8166/trac_8166.patch) by mvngu created at 2010-05-21 15:45:14

I have attached a rebase of ncohen's patch, rebased on top of #8364. Based upon that, I did some clean-ups of the changes proposed by ncohen. My changes are mainly cosmetic clean-ups along the lines of PEP 008. Both ncohen's patch and my changes are folded into one patch to make it easier for anyone to give a final review.



---

archive/issue_comments_071731.json:
```json
{
    "body": "Oh, but then it means I can not review it myself ? :-)\n\nNathann",
    "created_at": "2010-05-21T17:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71731",
    "user": "https://github.com/nathanncohen"
}
```

Oh, but then it means I can not review it myself ? :-)

Nathann



---

archive/issue_comments_071732.json:
```json
{
    "body": "[reviewer.diff](http://trac.sagemath.org/sage_trac/attachment/ticket/8166/reviewer.diff) contains the changes I folded into ncohen's patch. This should make it easier to review [trac_8166-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8166/trac_8166-rebase.patch).",
    "created_at": "2010-05-21T18:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

[reviewer.diff](http://trac.sagemath.org/sage_trac/attachment/ticket/8166/reviewer.diff) contains the changes I folded into ncohen's patch. This should make it easier to review [trac_8166-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8166/trac_8166-rebase.patch).



---

archive/issue_comments_071733.json:
```json
{
    "body": "Attachment [trac_8166-rebase.patch](tarball://root/attachments/some-uuid/ticket8166/trac_8166-rebase.patch) by mvngu created at 2010-05-21 18:40:49",
    "created_at": "2010-05-21T18:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8166-rebase.patch](tarball://root/attachments/some-uuid/ticket8166/trac_8166-rebase.patch) by mvngu created at 2010-05-21 18:40:49



---

archive/issue_comments_071734.json:
```json
{
    "body": "Attachment [reviewer.diff](tarball://root/attachments/some-uuid/ticket8166/reviewer.diff) by mvngu created at 2010-05-21 18:41:02\n\ndiff patch showing changes proposed by reviewer",
    "created_at": "2010-05-21T18:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71734",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [reviewer.diff](tarball://root/attachments/some-uuid/ticket8166/reviewer.diff) by mvngu created at 2010-05-21 18:41:02

diff patch showing changes proposed by reviewer



---

archive/issue_comments_071735.json:
```json
{
    "body": "Nice, perfect, no error anywhere and many spelling/syntax mistakes fixed... Thank you again Minh ! :-)\n\nNathann",
    "created_at": "2010-05-21T18:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71735",
    "user": "https://github.com/nathanncohen"
}
```

Nice, perfect, no error anywhere and many spelling/syntax mistakes fixed... Thank you again Minh ! :-)

Nathann



---

archive/issue_comments_071736.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-21T18:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71736",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071737.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T00:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8166#issuecomment-71737",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_019567.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T00:41:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8166",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8166#event-19567"
}
```
