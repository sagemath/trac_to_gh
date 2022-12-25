# Issue 5258: escape html strings with cgi.escape instead of custom (and lacking) regexp

archive/issues_005258.json:
```json
{
    "body": "Assignee: boothby\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/3fd6f52b4b04108d for the discussion.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5258\n\n",
    "created_at": "2009-02-13T19:06:54Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "escape html strings with cgi.escape instead of custom (and lacking) regexp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5258",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

See http://groups.google.com/group/sage-devel/browse_thread/thread/3fd6f52b4b04108d for the discussion.


Issue created by migration from https://trac.sagemath.org/ticket/5258





---

archive/issue_comments_040275.json:
```json
{
    "body": "Attachment [trac_5258-escape-with-cgi.patch](tarball://root/attachments/some-uuid/ticket5258/trac_5258-escape-with-cgi.patch) by @jasongrout created at 2009-02-13 19:11:03",
    "created_at": "2009-02-13T19:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5258#issuecomment-40275",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5258-escape-with-cgi.patch](tarball://root/attachments/some-uuid/ticket5258/trac_5258-escape-with-cgi.patch) by @jasongrout created at 2009-02-13 19:11:03



---

archive/issue_comments_040276.json:
```json
{
    "body": "+1 and positive review!",
    "created_at": "2009-02-13T19:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5258#issuecomment-40276",
    "user": "https://github.com/williamstein"
}
```

+1 and positive review!



---

archive/issue_comments_040277.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2009-02-13T23:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5258#issuecomment-40277",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_040278.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-13T23:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5258#issuecomment-40278",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_events_005514.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-14T02:13:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5258#event-5514"
}
```



---

archive/issue_comments_040279.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T02:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5258#issuecomment-40279",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_040280.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T02:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5258#issuecomment-40280",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040281.json:
```json
{
    "body": "I blew it on this review -- there is a major major bug in this patch in that it uses escape in twist.py but does *not* import it!!  See #5358.",
    "created_at": "2009-02-24T14:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5258#issuecomment-40281",
    "user": "https://github.com/williamstein"
}
```

I blew it on this review -- there is a major major bug in this patch in that it uses escape in twist.py but does *not* import it!!  See #5358.



---

archive/issue_comments_040282.json:
```json
{
    "body": "Well, I blew it even more by writing the error in the patch!",
    "created_at": "2009-02-24T15:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5258#issuecomment-40282",
    "user": "https://github.com/jasongrout"
}
```

Well, I blew it even more by writing the error in the patch!
