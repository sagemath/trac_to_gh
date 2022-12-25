# Issue 3591: notebook -- remove notebook.save()  from Logout

archive/issues_003591.json:
```json
{
    "body": "Assignee: TimothyClemans\n\nOn sagenb.org it takes several seconds to logout because in class Logout(resource.Resource) in twist.py notebook.save() is called. That is very bad.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3591\n\n",
    "created_at": "2008-07-07T21:16:19Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "notebook -- remove notebook.save()  from Logout",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3591",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: TimothyClemans

On sagenb.org it takes several seconds to logout because in class Logout(resource.Resource) in twist.py notebook.save() is called. That is very bad.

Issue created by migration from https://trac.sagemath.org/ticket/3591





---

archive/issue_comments_025325.json:
```json
{
    "body": "Attachment [sage-3591.patch](tarball://root/attachments/some-uuid/ticket3591/sage-3591.patch) by TimothyClemans created at 2008-07-07 22:01:41\n\nAlso removed \"child_logout = Logout()\" from Toplevel resource because it's already in UserToplevel and anonymous users can't logout anyways.",
    "created_at": "2008-07-07T22:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3591#issuecomment-25325",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-3591.patch](tarball://root/attachments/some-uuid/ticket3591/sage-3591.patch) by TimothyClemans created at 2008-07-07 22:01:41

Also removed "child_logout = Logout()" from Toplevel resource because it's already in UserToplevel and anonymous users can't logout anyways.



---

archive/issue_comments_025326.json:
```json
{
    "body": "After discussion with was, this sounds good.  Apply!",
    "created_at": "2008-08-10T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3591#issuecomment-25326",
    "user": "https://github.com/ncalexan"
}
```

After discussion with was, this sounds good.  Apply!



---

archive/issue_comments_025327.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-11T02:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3591#issuecomment-25327",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_025328.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T02:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3591#issuecomment-25328",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003810.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-11T02:40:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3591",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3591#event-3810"
}
```
