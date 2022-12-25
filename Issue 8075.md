# Issue 8075: Enhance sage/eclib interface

archive/issues_008075.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona\n\nThe sage/eclib interface is rather old and could be simplified and made more efficient, probably after a major change to eclib to remove the NTL/LiDIA duality which has never been used by Sage and is essentially dead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8075\n\n",
    "created_at": "2010-01-26T09:26:57Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Enhance sage/eclib interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8075",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

CC:  @JohnCremona

The sage/eclib interface is rather old and could be simplified and made more efficient, probably after a major change to eclib to remove the NTL/LiDIA duality which has never been used by Sage and is essentially dead.

Issue created by migration from https://trac.sagemath.org/ticket/8075





---

archive/issue_comments_070630.json:
```json
{
    "body": "Changing keywords from \"\" to \"eclib\".",
    "created_at": "2013-10-24T08:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70630",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "eclib".



---

archive/issue_comments_070631.json:
```json
{
    "body": "Is this still of any actual pertinence ?",
    "created_at": "2015-03-16T20:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70631",
    "user": "https://github.com/fchapoton"
}
```

Is this still of any actual pertinence ?



---

archive/issue_comments_070632.json:
```json
{
    "body": "Yes.  It would be nice to expose more of the modular symbol functionality of eclib to Sage, more than the minimal `CremonaModularSymbols()` which was done a long time ago:\n\n```\nsage: %time M = ModularSymbols(10001)\nCPU times: user 6.42 s, sys: 196 ms, total: 6.62 s\nWall time: 6.61 s\nsage: %time M = CremonaModularSymbols(10001)\nCPU times: user 139 ms, sys: 3.87 ms, total: 143 ms\nWall time: 142 ms\n```\n\nThere is no reason in principle for Sage not to be able to access all the functionality which is used to produce all the modular elliptic curves of conductor `N` for reasonable `N`.",
    "created_at": "2015-03-16T21:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70632",
    "user": "https://github.com/JohnCremona"
}
```

Yes.  It would be nice to expose more of the modular symbol functionality of eclib to Sage, more than the minimal `CremonaModularSymbols()` which was done a long time ago:

```
sage: %time M = ModularSymbols(10001)
CPU times: user 6.42 s, sys: 196 ms, total: 6.62 s
Wall time: 6.61 s
sage: %time M = CremonaModularSymbols(10001)
CPU times: user 139 ms, sys: 3.87 ms, total: 143 ms
Wall time: 142 ms
```

There is no reason in principle for Sage not to be able to access all the functionality which is used to produce all the modular elliptic curves of conductor `N` for reasonable `N`.



---

archive/issue_comments_070633.json:
```json
{
    "body": "I am going to close this since the specific things mentioned were done long ago, though certainly there is more eclib functionality which could be exposed to Sage but is not.",
    "created_at": "2021-02-02T15:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70633",
    "user": "https://github.com/JohnCremona"
}
```

I am going to close this since the specific things mentioned were done long ago, though certainly there is more eclib functionality which could be exposed to Sage but is not.



---

archive/issue_comments_070634.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-02-02T15:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70634",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070635.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2021-02-05T14:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70635",
    "user": "https://github.com/JohnCremona"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_070636.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-02-05T14:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70636",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_comments_070637.json:
```json
{
    "body": "ok, John, as you wish",
    "created_at": "2021-02-05T14:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70637",
    "user": "https://github.com/fchapoton"
}
```

ok, John, as you wish



---

archive/issue_events_008281.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2021-02-05T14:58:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8075#event-8281"
}
```
