# Issue 635: [with patch] p-adic height gives incorrect precision

archive/issues_000635.json:
```json
{
    "body": "Assignee: dmharvey\n\nIf I ask for precision 10, I get precision 9:\n\n```\nsage: E = EllipticCurve(\"37a\")\nsage: P = E.gens()[0]\nsage: h = E.padic_height(5, 10)\nsage: h(P)\n4*5 + 3*5^2 + 3*5^3 + 4*5^4 + 4*5^5 + 5^6 + 4*5^8 + O(5^9)\n```\n\nIt didn't use to behave this way; it probably happened accidentally as a consequence of some changes chris wuthrich made, and it appears that the doctests were modified to make this behaviour the \"correct\" one. This should be fixed, because in the large prime case it ends up wasting a lot of time computing extra digits in intermediate steps.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/635\n\n",
    "closed_at": "2007-10-13T07:19:07Z",
    "created_at": "2007-09-10T19:28:56Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "[with patch] p-adic height gives incorrect precision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/635",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: dmharvey

If I ask for precision 10, I get precision 9:

```
sage: E = EllipticCurve("37a")
sage: P = E.gens()[0]
sage: h = E.padic_height(5, 10)
sage: h(P)
4*5 + 3*5^2 + 3*5^3 + 4*5^4 + 4*5^5 + 5^6 + 4*5^8 + O(5^9)
```

It didn't use to behave this way; it probably happened accidentally as a consequence of some changes chris wuthrich made, and it appears that the doctests were modified to make this behaviour the "correct" one. This should be fixed, because in the large prime case it ends up wasting a lot of time computing extra digits in intermediate steps.


Issue created by migration from https://trac.sagemath.org/ticket/635





---

archive/issue_events_001690.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-11T00:41:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/635#event-1690"
}
```



---

archive/issue_comments_003260.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-11T14:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/635#issuecomment-3260",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003261.json:
```json
{
    "body": "Changing assignee from @williamstein to dmharvey.",
    "created_at": "2007-09-11T14:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/635#issuecomment-3261",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing assignee from @williamstein to dmharvey.



---

archive/issue_comments_003262.json:
```json
{
    "body": "Attachment [patch-635.hg](tarball://root/attachments/some-uuid/ticket635/patch-635.hg) by dmharvey created at 2007-09-20 20:54:30\n\nAttached patch fixes the precision problem, but seems to introduce some weird segfault-like issues when running long doctests. I have no idea why this is happening because I'm only touching high-level python code. My guess is that those issues are independent of this one.",
    "created_at": "2007-09-20T20:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/635#issuecomment-3262",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [patch-635.hg](tarball://root/attachments/some-uuid/ticket635/patch-635.hg) by dmharvey created at 2007-09-20 20:54:30

Attached patch fixes the precision problem, but seems to introduce some weird segfault-like issues when running long doctests. I have no idea why this is happening because I'm only touching high-level python code. My guess is that those issues are independent of this one.



---

archive/issue_comments_003263.json:
```json
{
    "body": "I've tried the same patch against 2.8.5. Pretty much the same thing happens: the ordinary doctests (on `ell_rational_field.py`) are all fine, but long doctests produce *intermittent* segfaults... on some invocations everything is fine, and sometimes it segfaults. I have tried debugging with gdb, but either (a) the problem doesn't occur, or (b) I get an empty stack trace.\n\nI'm marking this as [with patch], because I think this patch is okay, and it's just exposing some other low-level bug somewhere else. If someone can track down the crasher that would be great.",
    "created_at": "2007-09-26T00:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/635#issuecomment-3263",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I've tried the same patch against 2.8.5. Pretty much the same thing happens: the ordinary doctests (on `ell_rational_field.py`) are all fine, but long doctests produce *intermittent* segfaults... on some invocations everything is fine, and sometimes it segfaults. I have tried debugging with gdb, but either (a) the problem doesn't occur, or (b) I get an empty stack trace.

I'm marking this as [with patch], because I think this patch is okay, and it's just exposing some other low-level bug somewhere else. If someone can track down the crasher that would be great.



---

archive/issue_events_001691.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/dmharvey",
    "created_at": "2007-09-26T00:24:22Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/635#event-1691"
}
```



---

archive/issue_events_001692.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/dmharvey",
    "created_at": "2007-09-26T00:24:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "milestone": "sage-2.8.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/635#event-1692"
}
```



---

archive/issue_events_001693.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T15:02:11Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "milestone": "sage-2.8.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/635#event-1693"
}
```



---

archive/issue_events_001694.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T15:02:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/635#event-1694"
}
```



---

archive/issue_comments_003264.json:
```json
{
    "body": "Changed to 2.8.7, since it will hopefully be in David Roe's patch already.",
    "created_at": "2007-10-04T15:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/635#issuecomment-3264",
    "user": "https://github.com/williamstein"
}
```

Changed to 2.8.7, since it will hopefully be in David Roe's patch already.



---

archive/issue_comments_003265.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/635#issuecomment-3265",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001695.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-13T07:19:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/635",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/635#event-1695"
}
```
