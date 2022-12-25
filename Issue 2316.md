# Issue 2316: [with patch, positive review] dsage.start_all() can leave zombie workers around

archive/issues_002316.json:
```json
{
    "body": "Assignee: @yqiang\n\nCC:  @williamstein\n\nKeywords: dsage\n\nIf you do dsage.start_all() and kill the server without killing the workers, the workers will be left hanging around so that the next time you do dsage.start_all(), you'll have twice as many workers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2316\n\n",
    "closed_at": "2008-04-07T01:18:59Z",
    "created_at": "2008-02-26T17:40:08Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, positive review] dsage.start_all() can leave zombie workers around",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2316",
    "user": "https://github.com/yqiang"
}
```
Assignee: @yqiang

CC:  @williamstein

Keywords: dsage

If you do dsage.start_all() and kill the server without killing the workers, the workers will be left hanging around so that the next time you do dsage.start_all(), you'll have twice as many workers.

Issue created by migration from https://trac.sagemath.org/ticket/2316





---

archive/issue_comments_015381.json:
```json
{
    "body": "patch which kills dsage server and workers when exiting sage",
    "created_at": "2008-04-01T22:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15381",
    "user": "https://github.com/yqiang"
}
```

patch which kills dsage server and workers when exiting sage



---

archive/issue_comments_015382.json:
```json
{
    "body": "Attachment [kill_zombies.patch](tarball://root/attachments/some-uuid/ticket2316/kill_zombies.patch) by @yqiang created at 2008-04-01 22:47:28\n\nAttached patch which kills the dsage server and worker on exit. This in conjunction with the sage cleaner should fix the zombie issues.",
    "created_at": "2008-04-01T22:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15382",
    "user": "https://github.com/yqiang"
}
```

Attachment [kill_zombies.patch](tarball://root/attachments/some-uuid/ticket2316/kill_zombies.patch) by @yqiang created at 2008-04-01 22:47:28

Attached patch which kills the dsage server and worker on exit. This in conjunction with the sage cleaner should fix the zombie issues.



---

archive/issue_comments_015383.json:
```json
{
    "body": "The patch applies to 3.0.alpha1 and fixes the issue for me.",
    "created_at": "2008-04-07T01:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15383",
    "user": "https://github.com/mwhansen"
}
```

The patch applies to 3.0.alpha1 and fixes the issue for me.



---

archive/issue_comments_015384.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T01:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015385.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T01:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15385",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_events_005459.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T01:18:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2316#event-5459"
}
```
