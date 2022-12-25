# Issue 4093: [with patch, needs review] fix numerical fuzz in period_lattice for 3.1.2

archive/issues_004093.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: elliptic curve period lattice\n\n3.1.2.rc1 has this doctest failure:\n\n```\nFile \"/home/john/sage-3.1.2.rc1/tmp/period_lattice.py\", line 281:\n    sage: EllipticCurve('389a1').period_lattice().sigma(CC(2,1))\nExpected:\n    2.609121635701083769 - 0.20086508082458695134*I\nGot:\n    2.609121635701083769 - 0.20086508082458695200*I\n```\n\n\nThe patch fixes this by replacin the last 3 digits above by \"...\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4093\n\n",
    "created_at": "2008-09-09T19:28:19Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] fix numerical fuzz in period_lattice for 3.1.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4093",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

Keywords: elliptic curve period lattice

3.1.2.rc1 has this doctest failure:

```
File "/home/john/sage-3.1.2.rc1/tmp/period_lattice.py", line 281:
    sage: EllipticCurve('389a1').period_lattice().sigma(CC(2,1))
Expected:
    2.609121635701083769 - 0.20086508082458695134*I
Got:
    2.609121635701083769 - 0.20086508082458695200*I
```


The patch fixes this by replacin the last 3 digits above by "...".


Issue created by migration from https://trac.sagemath.org/ticket/4093





---

archive/issue_comments_029470.json:
```json
{
    "body": "Attachment [10515.patch](tarball://root/attachments/some-uuid/ticket4093/10515.patch) by @JohnCremona created at 2008-09-09 19:28:32",
    "created_at": "2008-09-09T19:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4093#issuecomment-29470",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [10515.patch](tarball://root/attachments/some-uuid/ticket4093/10515.patch) by @JohnCremona created at 2008-09-09 19:28:32



---

archive/issue_comments_029471.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T19:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4093#issuecomment-29471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_029472.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-10T01:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4093#issuecomment-29472",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009331.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-10T01:10:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4093#event-9331"
}
```



---

archive/issue_comments_029473.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc2",
    "created_at": "2008-09-10T01:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4093#issuecomment-29473",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc2
