# Issue 6260: sage -startuptime is totally broken in sage-4.0.1

archive/issues_006260.json:
```json
{
    "body": "Assignee: cwitty\n\nsubject says it all.  This has something to do with hitting new code because of factoring out dsage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6260\n\n",
    "created_at": "2009-06-11T15:31:33Z",
    "labels": [
        "component: misc",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "sage -startuptime is totally broken in sage-4.0.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6260",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

subject says it all.  This has something to do with hitting new code because of factoring out dsage.

Issue created by migration from https://trac.sagemath.org/ticket/6260





---

archive/issue_comments_049894.json:
```json
{
    "body": "Attachment [trac_6260-apply_to_scripts_repo.patch](tarball://root/attachments/some-uuid/ticket6260/trac_6260-apply_to_scripts_repo.patch) by @williamstein created at 2009-06-11 15:38:26",
    "created_at": "2009-06-11T15:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6260#issuecomment-49894",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6260-apply_to_scripts_repo.patch](tarball://root/attachments/some-uuid/ticket6260/trac_6260-apply_to_scripts_repo.patch) by @williamstein created at 2009-06-11 15:38:26



---

archive/issue_comments_049895.json:
```json
{
    "body": "Looks good to me.  The old version wouldn't work when importing any module that used absolute imports (whose import signature is different than the old import signature.",
    "created_at": "2009-06-11T18:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6260#issuecomment-49895",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  The old version wouldn't work when importing any module that used absolute imports (whose import signature is different than the old import signature.



---

archive/issue_comments_049896.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T22:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6260#issuecomment-49896",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_006504.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-13T22:54:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6260",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6260#event-6504"
}
```
