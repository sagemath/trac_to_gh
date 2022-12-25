# Issue 13: p-adic integers class

archive/issues_000013.json:
```json
{
    "body": "Assignee: somebody\n\nfrom David Harvey: \nI'm kind of on the run, but I just remembered it would be good to have a pAdicInteger class. Just like we have PowerSeries vs LaurentSeries, and Integer vs Rational, it would be good to have pAdicInteger and pAdicField. Basically the idea is that it doesn't have to keep track of ordp, which currently slows down certain operations a lot (like when I convert an integer to a padic, it has to compute ordp). Essentially it would be like Integers(p^n) but with a floating precision. A very natural application would be the padic sigma stuff I'm working on now.\n \nI can't implement it and send you a patch due to time constraints, but perhaps if you like the idea you can add it to the roadmap.\n\nIssue created by migration from https://trac.sagemath.org/ticket/13\n\n",
    "created_at": "2006-09-12T21:33:20Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "p-adic integers class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/13",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

from David Harvey: 
I'm kind of on the run, but I just remembered it would be good to have a pAdicInteger class. Just like we have PowerSeries vs LaurentSeries, and Integer vs Rational, it would be good to have pAdicInteger and pAdicField. Basically the idea is that it doesn't have to keep track of ordp, which currently slows down certain operations a lot (like when I convert an integer to a padic, it has to compute ordp). Essentially it would be like Integers(p^n) but with a floating precision. A very natural application would be the padic sigma stuff I'm working on now.
 
I can't implement it and send you a patch due to time constraints, but perhaps if you like the idea you can add it to the roadmap.

Issue created by migration from https://trac.sagemath.org/ticket/13





---

archive/issue_comments_000061.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2006-09-12T21:33:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/13",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/13#issuecomment-61",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_000013.json:
```json
{
    "actor": "@roed314",
    "created_at": "2007-05-20T04:08:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/13#event-13"
}
```



---

archive/issue_comments_000062.json:
```json
{
    "body": "Included in the new p-adics.",
    "created_at": "2007-05-20T04:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/13",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/13#issuecomment-62",
    "user": "https://github.com/roed314"
}
```

Included in the new p-adics.



---

archive/issue_comments_000063.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-20T04:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/13",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/13#issuecomment-63",
    "user": "https://github.com/roed314"
}
```

Resolution: fixed
