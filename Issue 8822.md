# Issue 8822: Bug in Family constructor

archive/issues_008822.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: combinat, family\n\n\n```\nsage: f = Family(Zmod(3), lambda i: 2*i, lazy=False)\nsage: f\nLazy family (<lambda>(i))_{i in Ring of integers modulo 3}\n```\n\n\nShould we really just silently ignore the intent here, or should\n\n`Family(S, f, lazy=False)` always return `Family([i for i in S], f)`\n\n(I guess the default for lazy should then be made 'None' so that 'True',\n'False' and 'None' could all have different behaviors.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8822\n\n",
    "created_at": "2010-04-29T12:25:31Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Bug in Family constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8822",
    "user": "@jbandlow"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: combinat, family


```
sage: f = Family(Zmod(3), lambda i: 2*i, lazy=False)
sage: f
Lazy family (<lambda>(i))_{i in Ring of integers modulo 3}
```


Should we really just silently ignore the intent here, or should

`Family(S, f, lazy=False)` always return `Family([i for i in S], f)`

(I guess the default for lazy should then be made 'None' so that 'True',
'False' and 'None' could all have different behaviors.)


Issue created by migration from https://trac.sagemath.org/ticket/8822





---

archive/issue_comments_081024.json:
```json
{
    "body": "Changing assignee from sage-combinat to @hivert.",
    "created_at": "2010-05-13T22:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8822#issuecomment-81024",
    "user": "@hivert"
}
```

Changing assignee from sage-combinat to @hivert.



---

archive/issue_comments_081025.json:
```json
{
    "body": "I'm working on this one\n\nFlorent",
    "created_at": "2010-05-13T22:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8822#issuecomment-81025",
    "user": "@hivert"
}
```

I'm working on this one

Florent



---

archive/issue_comments_081026.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8822#issuecomment-81026",
    "user": "@mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.
