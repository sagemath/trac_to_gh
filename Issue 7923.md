# Issue 7923: signed int overflow in givaro elements' __pow__ method

archive/issues_007923.json:
```json
{
    "body": "Assignee: @aghitza\n\nWhen 2^31 < q^2 < 2^32, one can get an overflow in exponentiation (because of the use of signed vs unsigned ints).  This occurs for q=3^10.\n\n```\nsage: K.<a> = GF(3^10)\nsage: b = a^9 + a^7 + 2*a^6 + a^4 + a^3 + 2*a^2 + a + 2\nsage: b^(71*7381) == (b^71)^7381\nFalse\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7923\n\n",
    "created_at": "2010-01-14T00:15:44Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "signed int overflow in givaro elements' __pow__ method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7923",
    "user": "https://github.com/roed314"
}
```
Assignee: @aghitza

When 2^31 < q^2 < 2^32, one can get an overflow in exponentiation (because of the use of signed vs unsigned ints).  This occurs for q=3^10.

```
sage: K.<a> = GF(3^10)
sage: b = a^9 + a^7 + 2*a^6 + a^4 + a^3 + 2*a^2 + a + 2
sage: b^(71*7381) == (b^71)^7381
False
```

Issue created by migration from https://trac.sagemath.org/ticket/7923





---

archive/issue_comments_068845.json:
```json
{
    "body": "Attachment [7923.patch](tarball://root/attachments/some-uuid/ticket7923/7923.patch) by @roed314 created at 2010-01-14 00:19:20",
    "created_at": "2010-01-14T00:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7923#issuecomment-68845",
    "user": "https://github.com/roed314"
}
```

Attachment [7923.patch](tarball://root/attachments/some-uuid/ticket7923/7923.patch) by @roed314 created at 2010-01-14 00:19:20



---

archive/issue_comments_068846.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-14T00:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7923#issuecomment-68846",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068847.json:
```json
{
    "body": "This is based against 4.3.rc0 and the patch 7585_ALL.patch, but that will only change relative positioning, so it should apply with just a shift.",
    "created_at": "2010-01-14T15:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7923#issuecomment-68847",
    "user": "https://github.com/roed314"
}
```

This is based against 4.3.rc0 and the patch 7585_ALL.patch, but that will only change relative positioning, so it should apply with just a shift.



---

archive/issue_comments_068848.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-16T10:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7923#issuecomment-68848",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068849.json:
```json
{
    "body": "The code looks good, it does apply to 4.3, and it corrects the bug.  Positive review.",
    "created_at": "2010-01-16T10:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7923#issuecomment-68849",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

The code looks good, it does apply to 4.3, and it corrects the bug.  Positive review.



---

archive/issue_comments_068850.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-18T23:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7923#issuecomment-68850",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_018983.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-18T23:45:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7923",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7923#event-18983"
}
```
