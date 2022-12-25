# Issue 6644: [with patch, positive review] fix doctest error for lazy_attribute and abstract_method

archive/issues_006644.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nAs reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/e1d0c61c235c4554), there are doctest failures for the files lazy_attribute.py and abstract_method.py.  These are caused by ticket #6505, it seems: the patch there changed banner.py, and those changes caused the failures.  Here's a patch.\n\n(In the old version of banner.py, the function banner started on line 72, and now it starts on line 79.  Hence this patch.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6644\n\n",
    "closed_at": "2009-07-29T10:56:54Z",
    "created_at": "2009-07-27T20:15:38Z",
    "labels": [
        "component: misc",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] fix doctest error for lazy_attribute and abstract_method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6644",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

As reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/e1d0c61c235c4554), there are doctest failures for the files lazy_attribute.py and abstract_method.py.  These are caused by ticket #6505, it seems: the patch there changed banner.py, and those changes caused the failures.  Here's a patch.

(In the old version of banner.py, the function banner started on line 72, and now it starts on line 79.  Hence this patch.)


Issue created by migration from https://trac.sagemath.org/ticket/6644





---

archive/issue_comments_054387.json:
```json
{
    "body": "Attachment [trac_6644-72-to-79.patch](tarball://root/attachments/some-uuid/ticket6644/trac_6644-72-to-79.patch) by @jhpalmieri created at 2009-07-27 20:16:32",
    "created_at": "2009-07-27T20:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6644#issuecomment-54387",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6644-72-to-79.patch](tarball://root/attachments/some-uuid/ticket6644/trac_6644-72-to-79.patch) by @jhpalmieri created at 2009-07-27 20:16:32



---

archive/issue_comments_054388.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-29T10:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6644#issuecomment-54388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015696.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-29T10:56:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6644",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6644#event-15696"
}
```
