# Issue 7474: [with patch, needs review]Expose some more functionality of fmz_poly

archive/issues_007474.json:
```json
{
    "body": "Assignee: mraum\n\nKeywords: flint, fmpz_poly, integers\n\nThis makes the FLINT wrapper in sage.libs.flint.fmpz_poly handle big integers correctly and exposes shifts and derivatives.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7474\n\n",
    "created_at": "2009-11-16T17:15:41Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review]Expose some more functionality of fmz_poly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7474",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```
Assignee: mraum

Keywords: flint, fmpz_poly, integers

This makes the FLINT wrapper in sage.libs.flint.fmpz_poly handle big integers correctly and exposes shifts and derivatives.

Issue created by migration from https://trac.sagemath.org/ticket/7474





---

archive/issue_comments_062875.json:
```json
{
    "body": "Attachment [trac-7474-flint.patch](tarball://root/attachments/some-uuid/ticket7474/trac-7474-flint.patch) by mraum created at 2009-11-16 17:16:39",
    "created_at": "2009-11-16T17:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Attachment [trac-7474-flint.patch](tarball://root/attachments/some-uuid/ticket7474/trac-7474-flint.patch) by mraum created at 2009-11-16 17:16:39



---

archive/issue_comments_062876.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-17T07:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62876",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_062877.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-17T07:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62877",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062878.json:
```json
{
    "body": "Actually, the derivative of 1 + 2*x + 6*x^2 should be [2, 12] and not [4, 18].  With this change the tests pass.",
    "created_at": "2009-11-17T07:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62878",
    "user": "https://github.com/mwhansen"
}
```

Actually, the derivative of 1 + 2*x + 6*x^2 should be [2, 12] and not [4, 18].  With this change the tests pass.



---

archive/issue_comments_062879.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T07:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62879",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062880.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T07:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62880",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007702.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-17T07:41:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7474#event-7702"
}
```



---

archive/issue_comments_062881.json:
```json
{
    "body": "Attachment [trac_7474-review.patch](tarball://root/attachments/some-uuid/ticket7474/trac_7474-review.patch) by @mwhansen created at 2009-11-17 07:41:26",
    "created_at": "2009-11-17T07:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7474#issuecomment-62881",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7474-review.patch](tarball://root/attachments/some-uuid/ticket7474/trac_7474-review.patch) by @mwhansen created at 2009-11-17 07:41:26
