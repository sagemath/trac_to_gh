# Issue 1034: clean up 'revlex' term ordering mess

archive/issues_001034.json:
```json
{
    "body": "Assignee: @malb\n\nWhat we call 'revlex' and which translates to 'rp' in Singular is not what is called 'revlex' in literature. Also our generic implementation doesn't match the one of Singular. This needs to be cleaned up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1034\n\n",
    "created_at": "2007-10-30T15:03:33Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "clean up 'revlex' term ordering mess",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1034",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

What we call 'revlex' and which translates to 'rp' in Singular is not what is called 'revlex' in literature. Also our generic implementation doesn't match the one of Singular. This needs to be cleaned up.

Issue created by migration from https://trac.sagemath.org/ticket/1034





---

archive/issue_comments_006298.json:
```json
{
    "body": "Attachment [revlex.patch](tarball://root/attachments/some-uuid/ticket1034/revlex.patch) by @malb created at 2007-10-30 16:06:11",
    "created_at": "2007-10-30T16:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6298",
    "user": "https://github.com/malb"
}
```

Attachment [revlex.patch](tarball://root/attachments/some-uuid/ticket1034/revlex.patch) by @malb created at 2007-10-30 16:06:11



---

archive/issue_comments_006299.json:
```json
{
    "body": "the attached patch removes revlex which Singular does not support and introduces invlex which Singular supports and which is only relevant for non-commutative rings.",
    "created_at": "2007-10-30T16:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6299",
    "user": "https://github.com/malb"
}
```

the attached patch removes revlex which Singular does not support and introduces invlex which Singular supports and which is only relevant for non-commutative rings.



---

archive/issue_comments_006300.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-30T16:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6300",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_events_001159.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-01T10:20:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1034#event-1159"
}
```



---

archive/issue_comments_006301.json:
```json
{
    "body": "applied to 2.8.11.alpha0",
    "created_at": "2007-11-01T10:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6301",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.alpha0



---

archive/issue_comments_006302.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T10:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6302",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
