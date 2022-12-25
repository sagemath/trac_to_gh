# Issue 5034: stupid output of sage -br:  "using n cpus"

archive/issues_005034.json:
```json
{
    "body": "Assignee: mabshoff\n\nI just noticed that when we do \"sage -br\" with \"export MAKE='make -j3'\" on a 2-core machine we get:\n\n```\nsteragon-2:sage-3.3.alpha0 wstein$ sage -br\n...\nExecute 4 commands (using 3 cpus)\n```\n\nNote the \"3 cpus\", which looks really dumb, since I have only 1 cpu in my laptop, and it has 2 cores.  To fix this bug change \"cpus\" to \"threads\".  That's it!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5034\n\n",
    "created_at": "2009-01-20T06:13:23Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "stupid output of sage -br:  \"using n cpus\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5034",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

I just noticed that when we do "sage -br" with "export MAKE='make -j3'" on a 2-core machine we get:

```
steragon-2:sage-3.3.alpha0 wstein$ sage -br
...
Execute 4 commands (using 3 cpus)
```

Note the "3 cpus", which looks really dumb, since I have only 1 cpu in my laptop, and it has 2 cores.  To fix this bug change "cpus" to "threads".  That's it!

Issue created by migration from https://trac.sagemath.org/ticket/5034





---

archive/issue_comments_038261.json:
```json
{
    "body": "this is against sage-3.3.alpha0",
    "created_at": "2009-01-20T06:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38261",
    "user": "https://github.com/williamstein"
}
```

this is against sage-3.3.alpha0



---

archive/issue_comments_038262.json:
```json
{
    "body": "Attachment [trac_5034.patch](tarball://root/attachments/some-uuid/ticket5034/trac_5034.patch) by @williamstein created at 2009-01-20 06:39:25\n\nThe attached patch is just a textual substitution of \"threads\" for \"cpus\".",
    "created_at": "2009-01-20T06:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38262",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5034.patch](tarball://root/attachments/some-uuid/ticket5034/trac_5034.patch) by @williamstein created at 2009-01-20 06:39:25

The attached patch is just a textual substitution of "threads" for "cpus".



---

archive/issue_comments_038263.json:
```json
{
    "body": "Of course, \"threads\" is also technically incorrect; \"processes\" would be more accurate.",
    "created_at": "2009-01-20T23:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38263",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Of course, "threads" is also technically incorrect; "processes" would be more accurate.



---

archive/issue_comments_038264.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T09:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38264",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_038265.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5034#issuecomment-38265",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011611.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T09:07:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5034",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5034#event-11611"
}
```
