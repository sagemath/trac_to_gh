# Issue 8075: Enhance sage/eclib interface

archive/issues_008075.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona\n\nThe sage/eclib interface is rather old and could be simplified and made more efficient, probably after a major change to eclib to remove the NTL/LiDIA duality which has never been used by Sage and is essentially dead.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8075\n\n",
    "created_at": "2010-01-26T09:26:57Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "Enhance sage/eclib interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8075",
    "user": "cremona"
}
```
Assignee: was

CC:  cremona

The sage/eclib interface is rather old and could be simplified and made more efficient, probably after a major change to eclib to remove the NTL/LiDIA duality which has never been used by Sage and is essentially dead.

Issue created by migration from https://trac.sagemath.org/ticket/8075





---

archive/issue_comments_070751.json:
```json
{
    "body": "Changing keywords from \"\" to \"eclib\".",
    "created_at": "2013-10-24T08:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70751",
    "user": "chapoton"
}
```

Changing keywords from "" to "eclib".



---

archive/issue_comments_070752.json:
```json
{
    "body": "Is this still of any actual pertinence ?",
    "created_at": "2015-03-16T20:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70752",
    "user": "chapoton"
}
```

Is this still of any actual pertinence ?



---

archive/issue_comments_070753.json:
```json
{
    "body": "Yes.  It would be nice to expose more of the modular symbol functionality of eclib to Sage, more than the minimal `CremonaModularSymbols()` which was done a long time ago:\n\n```\nsage: %time M = ModularSymbols(10001)\nCPU times: user 6.42 s, sys: 196 ms, total: 6.62 s\nWall time: 6.61 s\nsage: %time M = CremonaModularSymbols(10001)\nCPU times: user 139 ms, sys: 3.87 ms, total: 143 ms\nWall time: 142 ms\n```\n\nThere is no reason in principle for Sage not to be able to access all the functionality which is used to produce all the modular elliptic curves of conductor `N` for reasonable `N`.",
    "created_at": "2015-03-16T21:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70753",
    "user": "cremona"
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

archive/issue_comments_070754.json:
```json
{
    "body": "I am going to close this since the specific things mentioned were done long ago, though certainly there is more eclib functionality which could be exposed to Sage but is not.",
    "created_at": "2021-02-02T15:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70754",
    "user": "cremona"
}
```

I am going to close this since the specific things mentioned were done long ago, though certainly there is more eclib functionality which could be exposed to Sage but is not.



---

archive/issue_comments_070755.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-02-02T15:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70755",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070756.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2021-02-05T14:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70756",
    "user": "cremona"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_070757.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-02-05T14:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70757",
    "user": "chapoton"
}
```

Resolution: invalid



---

archive/issue_comments_070758.json:
```json
{
    "body": "ok, John, as you wish",
    "created_at": "2021-02-05T14:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8075#issuecomment-70758",
    "user": "chapoton"
}
```

ok, John, as you wish
