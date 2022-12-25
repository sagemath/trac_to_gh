# Issue 3744: Coercion between isomorphic parents should result in an element of the left operand's parent

archive/issues_003744.json:
```json
{
    "body": "Assignee: @robertwb\n\nThis is in accordance with the programming guide. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3744\n\n",
    "created_at": "2008-07-30T05:00:58Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Coercion between isomorphic parents should result in an element of the left operand's parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3744",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

This is in accordance with the programming guide. 

Issue created by migration from https://trac.sagemath.org/ticket/3744





---

archive/issue_comments_026530.json:
```json
{
    "body": "Attachment [3744-coercion-left.patch](tarball://root/attachments/some-uuid/ticket3744/3744-coercion-left.patch) by @robertwb created at 2008-07-30 05:02:39",
    "created_at": "2008-07-30T05:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26530",
    "user": "https://github.com/robertwb"
}
```

Attachment [3744-coercion-left.patch](tarball://root/attachments/some-uuid/ticket3744/3744-coercion-left.patch) by @robertwb created at 2008-07-30 05:02:39



---

archive/issue_comments_026531.json:
```json
{
    "body": "This patch does not apply cleanly to 3.1.alpha0:\n\n```\nsage: hg_sage.apply (\"/home/john/3744-coercion-left.patch\")\ncd \"/home/john/tmp/sage-3.1.alpha0/devel/sage\" && hg status\ncd \"/home/john/tmp/sage-3.1.alpha0/devel/sage\" && hg status\ncd \"/home/john/tmp/sage-3.1.alpha0/devel/sage\" && hg import   \"/home/john/3744-coercion-left.patch\"\napplying /home/john/3744-coercion-left.patch\npatching file sage/structure/coerce.pyx\nHunk #1 FAILED at 737\nHunk #2 FAILED at 754\n2 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej\nabort: patch failed to apply\n```\n\n\nI'm not sure how it fits in with the main coercion model patches though.",
    "created_at": "2008-08-10T10:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26531",
    "user": "https://github.com/JohnCremona"
}
```

This patch does not apply cleanly to 3.1.alpha0:

```
sage: hg_sage.apply ("/home/john/3744-coercion-left.patch")
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/john/tmp/sage-3.1.alpha0/devel/sage" && hg import   "/home/john/3744-coercion-left.patch"
applying /home/john/3744-coercion-left.patch
patching file sage/structure/coerce.pyx
Hunk #1 FAILED at 737
Hunk #2 FAILED at 754
2 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej
abort: patch failed to apply
```


I'm not sure how it fits in with the main coercion model patches though.



---

archive/issue_comments_026532.json:
```json
{
    "body": "Let's wait until #3738 gets in.",
    "created_at": "2008-08-11T16:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26532",
    "user": "https://github.com/robertwb"
}
```

Let's wait until #3738 gets in.



---

archive/issue_comments_026533.json:
```json
{
    "body": "Still does not apply cleanly to 3.1.alpha2:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: 3744\nsage: hg_sage.apply(\"/home/john/3744-coercion-left.patch\")\ncd \"/home/john/sage-3.1.alpha2/devel/sage\" && hg status\ncd \"/home/john/sage-3.1.alpha2/devel/sage\" && hg status\ncd \"/home/john/sage-3.1.alpha2/devel/sage\" && hg import   \"/home/john/3744-coercion-left.patch\"\napplying /home/john/3744-coercion-left.patch\npatching file sage/structure/coerce.pyx\nHunk #1 succeeded at 845 with fuzz 2 (offset 105 lines).\nHunk #2 FAILED at 780\n1 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-08-14T20:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26533",
    "user": "https://github.com/JohnCremona"
}
```

Still does not apply cleanly to 3.1.alpha2:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: 3744
sage: hg_sage.apply("/home/john/3744-coercion-left.patch")
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg status
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg status
cd "/home/john/sage-3.1.alpha2/devel/sage" && hg import   "/home/john/3744-coercion-left.patch"
applying /home/john/3744-coercion-left.patch
patching file sage/structure/coerce.pyx
Hunk #1 succeeded at 845 with fuzz 2 (offset 105 lines).
Hunk #2 FAILED at 780
1 out of 2 hunks FAILED -- saving rejects to file sage/structure/coerce.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_026534.json:
```json
{
    "body": "This is actually in 3.1.alpha2 and has been reviewed via #3738, so I am giving this a positive reivew.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-14T23:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26534",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is actually in 3.1.alpha2 and has been reviewed via #3738, so I am giving this a positive reivew.

Cheers,

Michael



---

archive/issue_comments_026535.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-14T23:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26535",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003967.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-14T23:49:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3744#event-3967"
}
```



---

archive/issue_comments_026536.json:
```json
{
    "body": "Merged in Sage 3.1.alpha2",
    "created_at": "2008-08-14T23:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26536",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha2



---

archive/issue_comments_026537.json:
```json
{
    "body": "Well, I really ought to change the subject, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-14T23:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3744#issuecomment-26537",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, I really ought to change the subject, too.

Cheers,

Michael
