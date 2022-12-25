# Issue 3842: [with patch; positive review] notebook -- major bug in how javascript <script> tags are interpreted by the notebook

archive/issues_003842.json:
```json
{
    "body": "Assignee: boothby\n\nTry the following:\n\n```\nprint \"hi\"\nsleep(2)\nhtml('<script>alert(\"boom!\")</script>')\nsleep(5)\nhtml('<script>alert(\"sage!\")</script>')\n```\n\nThis illustrates that the <script> tags get evaled AS THE OUTPUT gets received.  Instead the <script> parser should wait until the output is done before parsing anything.  This will likely fix a LOT of annoying weirdness with latency and interact over a slow connection. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3842\n\n",
    "closed_at": "2008-08-14T16:42:29Z",
    "created_at": "2008-08-13T19:15:24Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch; positive review] notebook -- major bug in how javascript <script> tags are interpreted by the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3842",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Try the following:

```
print "hi"
sleep(2)
html('<script>alert("boom!")</script>')
sleep(5)
html('<script>alert("sage!")</script>')
```

This illustrates that the <script> tags get evaled AS THE OUTPUT gets received.  Instead the <script> parser should wait until the output is done before parsing anything.  This will likely fix a LOT of annoying weirdness with latency and interact over a slow connection. 

Issue created by migration from https://trac.sagemath.org/ticket/3842





---

archive/issue_comments_027267.json:
```json
{
    "body": "Attachment [sage-3842.patch](tarball://root/attachments/some-uuid/ticket3842/sage-3842.patch) by @williamstein created at 2008-08-14 01:57:24",
    "created_at": "2008-08-14T01:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3842#issuecomment-27267",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3842.patch](tarball://root/attachments/some-uuid/ticket3842/sage-3842.patch) by @williamstein created at 2008-08-14 01:57:24



---

archive/issue_comments_027268.json:
```json
{
    "body": "Without this patch, \"Boom!\" popped up 5 times.",
    "created_at": "2008-08-14T04:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3842#issuecomment-27268",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Without this patch, "Boom!" popped up 5 times.



---

archive/issue_events_008795.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-14T16:42:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3842",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3842#event-8795"
}
```



---

archive/issue_comments_027269.json:
```json
{
    "body": "Merged in Sage 3.1.rc0",
    "created_at": "2008-08-14T16:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3842#issuecomment-27269",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.rc0



---

archive/issue_comments_027270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-14T16:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3842#issuecomment-27270",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
