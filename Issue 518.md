# Issue 518: fix the indentation in monsky_washnitzer.py to be *FOUR* spaces not two.

archive/issues_000518.json:
```json
{
    "body": "Assignee: dmharvey\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/518\n\n",
    "created_at": "2007-08-29T21:51:35Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "fix the indentation in monsky_washnitzer.py to be *FOUR* spaces not two.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/518",
    "user": "https://github.com/williamstein"
}
```
Assignee: dmharvey



Issue created by migration from https://trac.sagemath.org/ticket/518





---

archive/issue_comments_002606.json:
```json
{
    "body": "fix indentation",
    "created_at": "2007-08-30T04:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/518#issuecomment-2606",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

fix indentation



---

archive/issue_comments_002607.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-30T12:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/518#issuecomment-2607",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002608.json:
```json
{
    "body": "Attachment [mw-indentation.patch](tarball://root/attachments/some-uuid/ticket518/mw-indentation.patch) by dmharvey created at 2007-08-30 12:11:25",
    "created_at": "2007-08-30T12:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/518#issuecomment-2608",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [mw-indentation.patch](tarball://root/attachments/some-uuid/ticket518/mw-indentation.patch) by dmharvey created at 2007-08-30 12:11:25



---

archive/issue_comments_002609.json:
```json
{
    "body": "I am unable to apply this patch:\n\n```\nhg_sage.sage: hg_sage.apply('mw-indentation.patch')\ncd \"/home/was/s/devel/sage\" && hg status\ncd \"/home/was/s/devel/sage\" && hg status\ncd \"/home/was/s/devel/sage\" && hg import   \"/home/was/Desktop/mw-indentation.patch\"\napplying /home/was/Desktop/mw-indentation.patch\nsage/schemes/elliptic_curves/monsky_washnitzer.py\nHunk #1 FAILED at 60.\nHunk #7 FAILED at 1150.\nHunk #8 FAILED at 1215.\n3 out of 9 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/monsky_washnitzer.py.rej\nabort: patch command failed: exited with status 1\nsage:\n```\n\n\nAnd it really genuinely is mostly not applied.",
    "created_at": "2007-09-05T04:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/518#issuecomment-2609",
    "user": "https://github.com/williamstein"
}
```

I am unable to apply this patch:

```
hg_sage.sage: hg_sage.apply('mw-indentation.patch')
cd "/home/was/s/devel/sage" && hg status
cd "/home/was/s/devel/sage" && hg status
cd "/home/was/s/devel/sage" && hg import   "/home/was/Desktop/mw-indentation.patch"
applying /home/was/Desktop/mw-indentation.patch
sage/schemes/elliptic_curves/monsky_washnitzer.py
Hunk #1 FAILED at 60.
Hunk #7 FAILED at 1150.
Hunk #8 FAILED at 1215.
3 out of 9 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/monsky_washnitzer.py.rej
abort: patch command failed: exited with status 1
sage:
```


And it really genuinely is mostly not applied.



---

archive/issue_comments_002610.json:
```json
{
    "body": "\n```\n[11:18] <dmharvey> #518: okay, I guess I'll just go through and do it again at some point. I think the real problem here is to do with trac. I posted the patch a while back, but it didn't get rolled into the repository until now. But meanwhile you and robert had done a bunch of things.\n```\n",
    "created_at": "2007-09-06T18:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/518#issuecomment-2610",
    "user": "https://github.com/williamstein"
}
```


```
[11:18] <dmharvey> #518: okay, I guess I'll just go through and do it again at some point. I think the real problem here is to do with trac. I posted the patch a while back, but it didn't get rolled into the repository until now. But meanwhile you and robert had done a bunch of things.
```




---

archive/issue_comments_002611.json:
```json
{
    "body": "let's try that again",
    "created_at": "2007-09-07T01:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/518#issuecomment-2611",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

let's try that again



---

archive/issue_events_000557.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-09-07T04:31:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/518#event-557"
}
```



---

archive/issue_comments_002612.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/518#issuecomment-2612",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_002613.json:
```json
{
    "body": "Attachment [mw-indentation2.hg](tarball://root/attachments/some-uuid/ticket518/mw-indentation2.hg) by @williamstein created at 2007-09-07 04:31:08",
    "created_at": "2007-09-07T04:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/518",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/518#issuecomment-2613",
    "user": "https://github.com/williamstein"
}
```

Attachment [mw-indentation2.hg](tarball://root/attachments/some-uuid/ticket518/mw-indentation2.hg) by @williamstein created at 2007-09-07 04:31:08
