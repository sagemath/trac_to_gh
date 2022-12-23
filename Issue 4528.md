# Issue 4528: [with patch, needs review] Implement Krull dimension for orders in number fields

archive/issues_004528.json:
```json
{
    "body": "Assignee: was\n\nKeywords: number fields, orders\n\nThis is a triviality, but I noticed it while doing something else. All order in number fields have Krull dimension 1, but this was not implemented -- not even for the maximal order.  Now it is.\n\nPatch based on 3.2.rc1, touches rings/ring.pyx and rings/number_field/order.py\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4528\n\n",
    "created_at": "2008-11-15T16:56:35Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] Implement Krull dimension for orders in number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4528",
    "user": "cremona"
}
```
Assignee: was

Keywords: number fields, orders

This is a triviality, but I noticed it while doing something else. All order in number fields have Krull dimension 1, but this was not implemented -- not even for the maximal order.  Now it is.

Patch based on 3.2.rc1, touches rings/ring.pyx and rings/number_field/order.py


Issue created by migration from https://trac.sagemath.org/ticket/4528





---

archive/issue_comments_033624.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-15T16:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4528#issuecomment-33624",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_033625.json:
```json
{
    "body": "This looks good.\n\nAs a really trivial issue, someone should add a `.` at the end of line 754 of `ring.pyx`. It didn't seem worth another patch.",
    "created_at": "2008-11-21T10:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4528#issuecomment-33625",
    "user": "craigcitro"
}
```

This looks good.

As a really trivial issue, someone should add a `.` at the end of line 754 of `ring.pyx`. It didn't seem worth another patch.



---

archive/issue_comments_033626.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T11:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4528#issuecomment-33626",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033627.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T11:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4528#issuecomment-33627",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0
