# Issue 777: sign function

archive/issues_000777.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  mhansen\n\nKeywords: sign\n\nShould the following function exist globally?\n\n```\ndef sign(x):\n    if x > 0:\n        return 1\n    if x < 0:\n        return -1\n    return 0\n```\n\nI'm not sure if this is identical to\n\n```\ndef sign(x):\n    return x.__cmp__(0)\n```\n\nI'm also ambivalent as to whether this function is called \"sign\", \"signum\", or \"sgn\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/777\n\n",
    "created_at": "2007-10-02T00:40:40Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sign function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/777",
    "user": "kedlaya"
}
```
Assignee: somebody

CC:  mhansen

Keywords: sign

Should the following function exist globally?

```
def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0
```

I'm not sure if this is identical to

```
def sign(x):
    return x.__cmp__(0)
```

I'm also ambivalent as to whether this function is called "sign", "signum", or "sgn".

Issue created by migration from https://trac.sagemath.org/ticket/777





---

archive/issue_comments_004637.json:
```json
{
    "body": "To release manager: note that this should be closed - see comment in #6803.",
    "created_at": "2009-08-26T15:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/777#issuecomment-4637",
    "user": "kcrisman"
}
```

To release manager: note that this should be closed - see comment in #6803.



---

archive/issue_comments_004638.json:
```json
{
    "body": "To clarify: we already have:\n\n```\nsage: sgn(1)\n1\nsage: sgn(-4)\n-1\n```\n\nso this ticket should be closed, presumably as a duplicate.",
    "created_at": "2009-11-10T15:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/777#issuecomment-4638",
    "user": "kcrisman"
}
```

To clarify: we already have:

```
sage: sgn(1)
1
sage: sgn(-4)
-1
```

so this ticket should be closed, presumably as a duplicate.



---

archive/issue_comments_004639.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-10T16:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/777#issuecomment-4639",
    "user": "mhansen"
}
```

Resolution: invalid
