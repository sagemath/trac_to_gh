# Issue 6531: Add generic ring classes to reference manual

archive/issues_006531.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: rings documentation doctest\n\nModule `sage.rings.ring` contains 11 base classes for various types of ring. This should be added to the reference manual. The file also needs a few more doctests to get to 100% coverage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6531\n\n",
    "created_at": "2009-07-14T09:59:29Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Add generic ring classes to reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6531",
    "user": "@loefflerd"
}
```
Assignee: tba

Keywords: rings documentation doctest

Module `sage.rings.ring` contains 11 base classes for various types of ring. This should be added to the reference manual. The file also needs a few more doctests to get to 100% coverage.

Issue created by migration from https://trac.sagemath.org/ticket/6531





---

archive/issue_comments_053238.json:
```json
{
    "body": "patch against 4.1",
    "created_at": "2009-07-14T10:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6531#issuecomment-53238",
    "user": "@loefflerd"
}
```

patch against 4.1



---

archive/issue_comments_053239.json:
```json
{
    "body": "Attachment [trac_6531-restify_generic_ring.patch](tarball://root/attachments/some-uuid/ticket6531/trac_6531-restify_generic_ring.patch) by @loefflerd created at 2009-07-14 10:16:33\n\nThis patch does the ReSTifying, adds all missing doctests (although I cheated by flagging some old unpickling functions with \"not tested\"), and comments out a few methods that achieve nothing at all.",
    "created_at": "2009-07-14T10:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6531#issuecomment-53239",
    "user": "@loefflerd"
}
```

Attachment [trac_6531-restify_generic_ring.patch](tarball://root/attachments/some-uuid/ticket6531/trac_6531-restify_generic_ring.patch) by @loefflerd created at 2009-07-14 10:16:33

This patch does the ReSTifying, adds all missing doctests (although I cheated by flagging some old unpickling functions with "not tested"), and comments out a few methods that achieve nothing at all.



---

archive/issue_comments_053240.json:
```json
{
    "body": "Attachment [trac_6531-restify_generic_ring-rebase.patch](tarball://root/attachments/some-uuid/ticket6531/trac_6531-restify_generic_ring-rebase.patch) by @JohnCremona created at 2009-08-30 14:42:54\n\nReplaces previous; rebased to 4.1.1",
    "created_at": "2009-08-30T14:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6531#issuecomment-53240",
    "user": "@JohnCremona"
}
```

Attachment [trac_6531-restify_generic_ring-rebase.patch](tarball://root/attachments/some-uuid/ticket6531/trac_6531-restify_generic_ring-rebase.patch) by @JohnCremona created at 2009-08-30 14:42:54

Replaces previous; rebased to 4.1.1



---

archive/issue_comments_053241.json:
```json
{
    "body": "On applying this to 4.1.1 there were some merge problems, which I fixed.  The second patch replaces the first and applies to 4.1.1.   I kept the author's name to David!",
    "created_at": "2009-08-30T14:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6531#issuecomment-53241",
    "user": "@JohnCremona"
}
```

On applying this to 4.1.1 there were some merge problems, which I fixed.  The second patch replaces the first and applies to 4.1.1.   I kept the author's name to David!



---

archive/issue_comments_053242.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-31T06:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6531#issuecomment-53242",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053243.json:
```json
{
    "body": "Merged `trac_6531-restify_generic_ring-rebase.patch`. See #6850 for a follow-up to this ticket.",
    "created_at": "2009-08-31T06:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6531#issuecomment-53243",
    "user": "mvngu"
}
```

Merged `trac_6531-restify_generic_ring-rebase.patch`. See #6850 for a follow-up to this ticket.
