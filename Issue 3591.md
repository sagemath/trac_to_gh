# Issue 3591: notebook -- remove notebook.save()  from Logout

archive/issues_003591.json:
```json
{
    "body": "Assignee: TimothyClemans\n\nOn sagenb.org it takes several seconds to logout because in class Logout(resource.Resource) in twist.py notebook.save() is called. That is very bad.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3591\n\n",
    "created_at": "2008-07-07T21:16:19Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "notebook -- remove notebook.save()  from Logout",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3591",
    "user": "TimothyClemans"
}
```
Assignee: TimothyClemans

On sagenb.org it takes several seconds to logout because in class Logout(resource.Resource) in twist.py notebook.save() is called. That is very bad.

Issue created by migration from https://trac.sagemath.org/ticket/3591





---

archive/issue_comments_025375.json:
```json
{
    "body": "Attachment [sage-3591.patch](tarball://root/attachments/some-uuid/ticket3591/sage-3591.patch) by TimothyClemans created at 2008-07-07 22:01:41\n\nAlso removed \"child_logout = Logout()\" from Toplevel resource because it's already in UserToplevel and anonymous users can't logout anyways.",
    "created_at": "2008-07-07T22:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3591#issuecomment-25375",
    "user": "TimothyClemans"
}
```

Attachment [sage-3591.patch](tarball://root/attachments/some-uuid/ticket3591/sage-3591.patch) by TimothyClemans created at 2008-07-07 22:01:41

Also removed "child_logout = Logout()" from Toplevel resource because it's already in UserToplevel and anonymous users can't logout anyways.



---

archive/issue_comments_025376.json:
```json
{
    "body": "After discussion with was, this sounds good.  Apply!",
    "created_at": "2008-08-10T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3591#issuecomment-25376",
    "user": "@ncalexan"
}
```

After discussion with was, this sounds good.  Apply!



---

archive/issue_comments_025377.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-11T02:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3591#issuecomment-25377",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_025378.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T02:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3591#issuecomment-25378",
    "user": "mabshoff"
}
```

Resolution: fixed
