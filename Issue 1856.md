# Issue 1856: 3d graphics -- bug in setting options via the show command

archive/issues_001856.json:
```json
{
    "body": "Assignee: was\n\nTry this:\n\n```\nsage: sphere((0,0,0), figsize=2).show(viewer='tachyon', figsize=10)\n```\n\nA tiny picture of a sphere appears.  It should be that the second figsize overwrites the first.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1856\n\n",
    "created_at": "2008-01-19T23:45:50Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "3d graphics -- bug in setting options via the show command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1856",
    "user": "was"
}
```
Assignee: was

Try this:

```
sage: sphere((0,0,0), figsize=2).show(viewer='tachyon', figsize=10)
```

A tiny picture of a sphere appears.  It should be that the second figsize overwrites the first.

Issue created by migration from https://trac.sagemath.org/ticket/1856





---

archive/issue_comments_011741.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-19T23:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11741",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011742.json:
```json
{
    "body": "Attachment [trac-1856.patch](tarball://root/attachments/some-uuid/ticket1856/trac-1856.patch) by was created at 2008-01-20 00:07:59",
    "created_at": "2008-01-20T00:07:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11742",
    "user": "was"
}
```

Attachment [trac-1856.patch](tarball://root/attachments/some-uuid/ticket1856/trac-1856.patch) by was created at 2008-01-20 00:07:59



---

archive/issue_comments_011743.json:
```json
{
    "body": "This fixes the problem mentioned above in a simple clean way, adds the ability to globally override the defaults, and adds an unrelated doctest.",
    "created_at": "2008-01-20T00:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11743",
    "user": "was"
}
```

This fixes the problem mentioned above in a simple clean way, adds the ability to globally override the defaults, and adds an unrelated doctest.



---

archive/issue_comments_011744.json:
```json
{
    "body": "Attachment [1856.patch](tarball://root/attachments/some-uuid/ticket1856/1856.patch) by mhansen created at 2008-01-21 03:55:29",
    "created_at": "2008-01-21T03:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11744",
    "user": "mhansen"
}
```

Attachment [1856.patch](tarball://root/attachments/some-uuid/ticket1856/1856.patch) by mhansen created at 2008-01-21 03:55:29



---

archive/issue_comments_011745.json:
```json
{
    "body": "The patch I posted applies (after #1854) and passes tests.",
    "created_at": "2008-01-21T03:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11745",
    "user": "mhansen"
}
```

The patch I posted applies (after #1854) and passes tests.



---

archive/issue_comments_011746.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11746",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011747.json:
```json
{
    "body": "Merged trac-1856.patch in Sage 2.10.1.alpha. mhansen's patch gave rejects.",
    "created_at": "2008-01-21T04:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1856#issuecomment-11747",
    "user": "mabshoff"
}
```

Merged trac-1856.patch in Sage 2.10.1.alpha. mhansen's patch gave rejects.
