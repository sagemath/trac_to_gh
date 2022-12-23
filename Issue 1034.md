# Issue 1034: clean up 'revlex' term ordering mess

archive/issues_001034.json:
```json
{
    "body": "Assignee: malb\n\nWhat we call 'revlex' and which translates to 'rp' in Singular is not what is called 'revlex' in literature. Also our generic implementation doesn't match the one of Singular. This needs to be cleaned up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1034\n\n",
    "created_at": "2007-10-30T15:03:33Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "clean up 'revlex' term ordering mess",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1034",
    "user": "malb"
}
```
Assignee: malb

What we call 'revlex' and which translates to 'rp' in Singular is not what is called 'revlex' in literature. Also our generic implementation doesn't match the one of Singular. This needs to be cleaned up.

Issue created by migration from https://trac.sagemath.org/ticket/1034





---

archive/issue_comments_006318.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-30T16:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6318",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_006319.json:
```json
{
    "body": "the attached patch removes revlex which Singular does not support and introduces invlex which Singular supports and which is only relevant for non-commutative rings.",
    "created_at": "2007-10-30T16:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6319",
    "user": "malb"
}
```

the attached patch removes revlex which Singular does not support and introduces invlex which Singular supports and which is only relevant for non-commutative rings.



---

archive/issue_comments_006320.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-30T16:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6320",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006321.json:
```json
{
    "body": "applied to 2.8.11.alpha0",
    "created_at": "2007-11-01T10:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6321",
    "user": "mabshoff"
}
```

applied to 2.8.11.alpha0



---

archive/issue_comments_006322.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T10:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1034#issuecomment-6322",
    "user": "mabshoff"
}
```

Resolution: fixed
