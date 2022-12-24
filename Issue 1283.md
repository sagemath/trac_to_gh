# Issue 1283: Update coercion model API

archive/issues_001283.json:
```json
{
    "body": "Assignee: somebody\n\nCurrently, coercions (and conversions) are defined in many different places in the SAGE codebase. We are going through each parent and consolidating/cleaning up the codebase to conform to the new coercion API, as described in the new programming guide. \n\nThis includes removing all Parent __call__ methods to use a generic __call__.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1283\n\n",
    "created_at": "2007-11-26T20:48:01Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Update coercion model API",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1283",
    "user": "robertwb"
}
```
Assignee: somebody

Currently, coercions (and conversions) are defined in many different places in the SAGE codebase. We are going through each parent and consolidating/cleaning up the codebase to conform to the new coercion API, as described in the new programming guide. 

This includes removing all Parent __call__ methods to use a generic __call__.

Issue created by migration from https://trac.sagemath.org/ticket/1283





---

archive/issue_comments_008043.json:
```json
{
    "body": "Attachment [coerce-migration.hg](tarball://root/attachments/some-uuid/ticket1283/coerce-migration.hg) by robertwb created at 2007-11-26 23:39:44",
    "created_at": "2007-11-26T23:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1283#issuecomment-8043",
    "user": "robertwb"
}
```

Attachment [coerce-migration.hg](tarball://root/attachments/some-uuid/ticket1283/coerce-migration.hg) by robertwb created at 2007-11-26 23:39:44



---

archive/issue_comments_008044.json:
```json
{
    "body": "See relevant section of http://wiki.sagemath.org/days6/sprint/prog_guide/prog_guide/outline",
    "created_at": "2007-11-26T23:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1283#issuecomment-8044",
    "user": "robertwb"
}
```

See relevant section of http://wiki.sagemath.org/days6/sprint/prog_guide/prog_guide/outline



---

archive/issue_comments_008045.json:
```json
{
    "body": "See also http://wiki.sagemath.org/days7/coercion/todo",
    "created_at": "2008-02-21T23:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1283#issuecomment-8045",
    "user": "robertwb"
}
```

See also http://wiki.sagemath.org/days7/coercion/todo



---

archive/issue_comments_008046.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-04T22:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1283#issuecomment-8046",
    "user": "robertwb"
}
```

Resolution: duplicate



---

archive/issue_comments_008047.json:
```json
{
    "body": "Dupe of #2314",
    "created_at": "2008-03-04T22:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1283#issuecomment-8047",
    "user": "robertwb"
}
```

Dupe of #2314
