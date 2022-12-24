# Issue 1596: preparser hangs if line starts with ...

archive/issues_001596.json:
```json
{
    "body": "Assignee: @williamstein\n\nAs reported by 'Octoploid' on IRC: The preparser crashes if a line starts with '...'.\n\nThis is caused by a string index in preparse_ellipsis() becoming negative and wrapping to the end of the string.\n\nPatch attached. This makes preparse('...') return 'Ellipsis'. Not sure if that's the desired behaviour. Maybe a syntax error would be better?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1596\n\n",
    "created_at": "2007-12-24T19:59:37Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "preparser hangs if line starts with ...",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1596",
    "user": "@wjp"
}
```
Assignee: @williamstein

As reported by 'Octoploid' on IRC: The preparser crashes if a line starts with '...'.

This is caused by a string index in preparse_ellipsis() becoming negative and wrapping to the end of the string.

Patch attached. This makes preparse('...') return 'Ellipsis'. Not sure if that's the desired behaviour. Maybe a syntax error would be better?

Issue created by migration from https://trac.sagemath.org/ticket/1596





---

archive/issue_comments_010157.json:
```json
{
    "body": "Attachment [preparse_ellipsis.patch](tarball://root/attachments/some-uuid/ticket1596/preparse_ellipsis.patch) by @wjp created at 2007-12-24 19:59:57",
    "created_at": "2007-12-24T19:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1596#issuecomment-10157",
    "user": "@wjp"
}
```

Attachment [preparse_ellipsis.patch](tarball://root/attachments/some-uuid/ticket1596/preparse_ellipsis.patch) by @wjp created at 2007-12-24 19:59:57



---

archive/issue_comments_010158.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-12-24T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1596#issuecomment-10158",
    "user": "@wjp"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_010159.json:
```json
{
    "body": "Changing component from algebraic geometry to user interface.",
    "created_at": "2007-12-24T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1596#issuecomment-10159",
    "user": "@wjp"
}
```

Changing component from algebraic geometry to user interface.



---

archive/issue_comments_010160.json:
```json
{
    "body": "Attachment [1596-ellipsis-bug.diff](tarball://root/attachments/some-uuid/ticket1596/1596-ellipsis-bug.diff) by @robertwb created at 2008-01-04 20:30:13\n\nThis patch fixes the problem. \n\nI agree that a syntax error would be preferable, see second patch (to replace the first). I also made the error on [1..] more explicit.",
    "created_at": "2008-01-04T20:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1596#issuecomment-10160",
    "user": "@robertwb"
}
```

Attachment [1596-ellipsis-bug.diff](tarball://root/attachments/some-uuid/ticket1596/1596-ellipsis-bug.diff) by @robertwb created at 2008-01-04 20:30:13

This patch fixes the problem. 

I agree that a syntax error would be preferable, see second patch (to replace the first). I also made the error on [1..] more explicit.



---

archive/issue_comments_010161.json:
```json
{
    "body": "Looks good to me. Merged in Sage 2.9.2.rc1.",
    "created_at": "2008-01-04T21:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1596#issuecomment-10161",
    "user": "mabshoff"
}
```

Looks good to me. Merged in Sage 2.9.2.rc1.



---

archive/issue_comments_010162.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-04T21:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1596",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1596#issuecomment-10162",
    "user": "mabshoff"
}
```

Resolution: fixed
