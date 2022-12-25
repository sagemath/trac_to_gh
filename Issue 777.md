# Issue 777: sign function

archive/issues_000777.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @mwhansen\n\nKeywords: sign\n\nShould the following function exist globally?\n\n```\ndef sign(x):\n    if x > 0:\n        return 1\n    if x < 0:\n        return -1\n    return 0\n```\n\nI'm not sure if this is identical to\n\n```\ndef sign(x):\n    return x.__cmp__(0)\n```\n\nI'm also ambivalent as to whether this function is called \"sign\", \"signum\", or \"sgn\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/777\n\n",
    "created_at": "2007-10-02T00:40:40Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sign function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/777",
    "user": "https://github.com/kedlaya"
}
```
Assignee: somebody

CC:  @mwhansen

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

archive/issue_events_002140.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-04T19:52:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/777#event-2140"
}
```



---

archive/issue_comments_004621.json:
```json
{
    "body": "To release manager: note that this should be closed - see comment in #6803.",
    "created_at": "2009-08-26T15:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/777#issuecomment-4621",
    "user": "https://github.com/kcrisman"
}
```

To release manager: note that this should be closed - see comment in #6803.



---

archive/issue_comments_004622.json:
```json
{
    "body": "To clarify: we already have:\n\n```\nsage: sgn(1)\n1\nsage: sgn(-4)\n-1\n```\n\nso this ticket should be closed, presumably as a duplicate.",
    "created_at": "2009-11-10T15:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/777#issuecomment-4622",
    "user": "https://github.com/kcrisman"
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

archive/issue_events_002141.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-10T16:17:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/777#event-2141"
}
```



---

archive/issue_events_002142.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-10T16:17:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/777#event-2142"
}
```



---

archive/issue_events_002143.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-10T16:17:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/777#event-2143"
}
```



---

archive/issue_comments_004623.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-10T16:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/777#issuecomment-4623",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
