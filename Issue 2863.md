# Issue 2863: Integer() does not specify that numbers beginning with 0 and 0x are treated specially

archive/issues_002863.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: integer octal hexadecimal\n\nThe Integer() function interprets numbers and strings beginning with 0 (respectively, 0x) as octal (respectively hexadecimal) numbers. The docstring does not reflect this. Attached patch fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2863\n\n",
    "created_at": "2008-04-09T08:45:49Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Integer() does not specify that numbers beginning with 0 and 0x are treated specially",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2863",
    "user": "https://github.com/dandrake"
}
```
Assignee: somebody

Keywords: integer octal hexadecimal

The Integer() function interprets numbers and strings beginning with 0 (respectively, 0x) as octal (respectively hexadecimal) numbers. The docstring does not reflect this. Attached patch fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/2863





---

archive/issue_comments_019599.json:
```json
{
    "body": "Attachment [integer-doc.patch](tarball://root/attachments/some-uuid/ticket2863/integer-doc.patch) by @dandrake created at 2008-04-09 08:46:12",
    "created_at": "2008-04-09T08:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2863#issuecomment-19599",
    "user": "https://github.com/dandrake"
}
```

Attachment [integer-doc.patch](tarball://root/attachments/some-uuid/ticket2863/integer-doc.patch) by @dandrake created at 2008-04-09 08:46:12



---

archive/issue_comments_019600.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-09T08:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2863#issuecomment-19600",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_comments_019601.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-09T08:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2863",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2863#issuecomment-19601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003057.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-09T08:52:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2863",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2863#event-3057"
}
```
