# Issue 6029: [with patch, needs review] bug in floor() for python types

archive/issues_006029.json:
```json
{
    "body": "Assignee: somebody\n\nsage: floor(int(10^50))\n100000000000000007629769841091887003294964970946560\n\nIssue created by migration from https://trac.sagemath.org/ticket/6029\n\n",
    "created_at": "2009-05-12T10:15:40Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] bug in floor() for python types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6029",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

sage: floor(int(10^50))
100000000000000007629769841091887003294964970946560

Issue created by migration from https://trac.sagemath.org/ticket/6029





---

archive/issue_comments_047914.json:
```json
{
    "body": "Attachment [6029-int-long-floor.patch](tarball://root/attachments/some-uuid/ticket6029/6029-int-long-floor.patch) by mvngu created at 2009-05-13 03:46:11\n\nSome hunk failures:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: 6029\nsage: hg_sage.apply(\"/home/mvngu/patch/6029/6029-int-long-floor.patch\")\ncd \"/scratch/mvngu/sage-3.4.2/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-3.4.2/devel/sage\" && hg status\ncd \"/scratch/mvngu/sage-3.4.2/devel/sage\" && hg import   \"/home/mvngu/patch/6029/6029-int-long-floor.patch\"\napplying /home/mvngu/patch/6029/6029-int-long-floor.patch\nunable to find 'sage/functions/other.py' for patching\n3 out of 3 hunks FAILED -- saving rejects to file sage/functions/other.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-05-13T03:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6029#issuecomment-47914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [6029-int-long-floor.patch](tarball://root/attachments/some-uuid/ticket6029/6029-int-long-floor.patch) by mvngu created at 2009-05-13 03:46:11

Some hunk failures:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 6029
sage: hg_sage.apply("/home/mvngu/patch/6029/6029-int-long-floor.patch")
cd "/scratch/mvngu/sage-3.4.2/devel/sage" && hg status
cd "/scratch/mvngu/sage-3.4.2/devel/sage" && hg status
cd "/scratch/mvngu/sage-3.4.2/devel/sage" && hg import   "/home/mvngu/patch/6029/6029-int-long-floor.patch"
applying /home/mvngu/patch/6029/6029-int-long-floor.patch
unable to find 'sage/functions/other.py' for patching
3 out of 3 hunks FAILED -- saving rejects to file sage/functions/other.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_047915.json:
```json
{
    "body": "This is to be applied on top of the pynac branch.",
    "created_at": "2009-05-13T03:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6029#issuecomment-47915",
    "user": "https://github.com/robertwb"
}
```

This is to be applied on top of the pynac branch.



---

archive/issue_comments_047916.json:
```json
{
    "body": "This is included in the patch at #5930.",
    "created_at": "2009-05-19T05:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6029#issuecomment-47916",
    "user": "https://github.com/mwhansen"
}
```

This is included in the patch at #5930.



---

archive/issue_comments_047917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-20T23:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6029#issuecomment-47917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006284.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-20T23:48:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6029",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6029#event-6284"
}
```



---

archive/issue_comments_047918.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T23:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6029#issuecomment-47918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael
