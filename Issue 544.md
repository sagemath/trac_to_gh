# Issue 544: doctesting const.tex should not pop up any windows

archive/issues_000544.json:
```json
{
    "body": "Assignee: wdjoyner\n\nIt is very annoying that doctesting const.tex causes a bunch of windows to pop up.\nThis should not happen.  Stop this by putting #optional after all doctests that\nwould pop up a window, so they aren't actually run, except in the rare cases when\nI'm running all optional doctests (and then popups are fine). \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/544\n\n",
    "created_at": "2007-08-31T20:12:03Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "doctesting const.tex should not pop up any windows",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/544",
    "user": "was"
}
```
Assignee: wdjoyner

It is very annoying that doctesting const.tex causes a bunch of windows to pop up.
This should not happen.  Stop this by putting #optional after all doctests that
would pop up a window, so they aren't actually run, except in the rare cases when
I'm running all optional doctests (and then popups are fine). 



Issue created by migration from https://trac.sagemath.org/ticket/544





---

archive/issue_comments_002755.json:
```json
{
    "body": "Changing assignee from wdjoyner to mhansen.",
    "created_at": "2007-09-06T23:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/544#issuecomment-2755",
    "user": "mhansen"
}
```

Changing assignee from wdjoyner to mhansen.



---

archive/issue_comments_002756.json:
```json
{
    "body": "Attachment [544.patch](tarball://root/attachments/some-uuid/ticket544/544.patch) by mhansen created at 2007-09-06 23:45:53\n\nPatch attached.",
    "created_at": "2007-09-06T23:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/544#issuecomment-2756",
    "user": "mhansen"
}
```

Attachment [544.patch](tarball://root/attachments/some-uuid/ticket544/544.patch) by mhansen created at 2007-09-06 23:45:53

Patch attached.



---

archive/issue_comments_002757.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T03:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/544#issuecomment-2757",
    "user": "was"
}
```

Resolution: fixed
