# Issue 8487: Use use_grobner in to_poly_solve

archive/issues_008487.json:
```json
{
    "body": "Assignee: @burcin\n\nSage returns no solution \n\n```\nx,y=var('x y')\nc1(x,y)=(x-5)^2+y^2-16; c2(x,y)=(y-3)^2+x^2-9\nsolve([c1(x,y),c2(x,y)],[x,y])\n```\n\nreported on [sage-support](http://groups.google.cz/group/sage-support/browse_thread/thread/40eda7084856aa3e)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8487\n\n",
    "created_at": "2010-03-10T10:05:03Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Use use_grobner in to_poly_solve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8487",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

Sage returns no solution 

```
x,y=var('x y')
c1(x,y)=(x-5)^2+y^2-16; c2(x,y)=(y-3)^2+x^2-9
solve([c1(x,y),c2(x,y)],[x,y])
```

reported on [sage-support](http://groups.google.cz/group/sage-support/browse_thread/thread/40eda7084856aa3e)

Issue created by migration from https://trac.sagemath.org/ticket/8487





---

archive/issue_comments_076372.json:
```json
{
    "body": "Attachment [trac-8487.patch](tarball://root/attachments/some-uuid/ticket8487/trac-8487.patch) by @robert-marik created at 2010-03-10 10:11:06",
    "created_at": "2010-03-10T10:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8487#issuecomment-76372",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac-8487.patch](tarball://root/attachments/some-uuid/ticket8487/trac-8487.patch) by @robert-marik created at 2010-03-10 10:11:06



---

archive/issue_comments_076373.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T10:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8487#issuecomment-76373",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076374.json:
```json
{
    "body": "The patch applies cleanly to sage-4.3.5 and passes long doctests.",
    "created_at": "2010-04-02T05:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8487#issuecomment-76374",
    "user": "https://github.com/aghitza"
}
```

The patch applies cleanly to sage-4.3.5 and passes long doctests.



---

archive/issue_comments_076375.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-02T05:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8487#issuecomment-76375",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020387.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2010-04-02T05:48:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8487",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8487#event-20387"
}
```



---

archive/issue_events_020388.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T17:28:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8487",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8487#event-20388"
}
```



---

archive/issue_comments_076376.json:
```json
{
    "body": "Merged into 4.4.alpha0.",
    "created_at": "2010-04-16T17:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8487#issuecomment-76376",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha0.



---

archive/issue_comments_076377.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T17:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8487#issuecomment-76377",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
