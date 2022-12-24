# Issue 2988: notebook -- issues with the CSS for the print display

archive/issues_002988.json:
```json
{
    "body": "Assignee: boothby\n\nMabshoff -- sorry I have to put this in as a 3.0 block (and fix it now).  It won't affect anything doctested.  I've had several professors (including me!) complain about issues with the notebook css and printing.  And, I told them I would fix this for 3.0.  \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2988\n\n",
    "created_at": "2008-04-21T14:24:04Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "notebook -- issues with the CSS for the print display",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2988",
    "user": "was"
}
```
Assignee: boothby

Mabshoff -- sorry I have to put this in as a 3.0 block (and fix it now).  It won't affect anything doctested.  I've had several professors (including me!) complain about issues with the notebook css and printing.  And, I told them I would fix this for 3.0.  



Issue created by migration from https://trac.sagemath.org/ticket/2988





---

archive/issue_comments_020570.json:
```json
{
    "body": "Attachment [sage-2988.patch](tarball://root/attachments/some-uuid/ticket2988/sage-2988.patch) by boothby created at 2008-04-21 20:29:28\n\nExcellent!",
    "created_at": "2008-04-21T20:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2988#issuecomment-20570",
    "user": "boothby"
}
```

Attachment [sage-2988.patch](tarball://root/attachments/some-uuid/ticket2988/sage-2988.patch) by boothby created at 2008-04-21 20:29:28

Excellent!



---

archive/issue_comments_020571.json:
```json
{
    "body": "It doesn't apply cleanly against rc1:\n\n```\nsage@modular:~/build/sage-3.0.rc1/devel/sage$ hg import /home2/mabshoff/trac_2988.patch\napplying /home2/mabshoff/trac_2988.patch\npatching file sage/server/notebook/cell.py\nHunk #1 FAILED at 645\n1 out of 2 hunks FAILED -- saving rejects to file sage/server/notebook/cell.py.rej\nabort: patch failed to apply\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-22T03:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2988#issuecomment-20571",
    "user": "mabshoff"
}
```

It doesn't apply cleanly against rc1:

```
sage@modular:~/build/sage-3.0.rc1/devel/sage$ hg import /home2/mabshoff/trac_2988.patch
applying /home2/mabshoff/trac_2988.patch
patching file sage/server/notebook/cell.py
Hunk #1 FAILED at 645
1 out of 2 hunks FAILED -- saving rejects to file sage/server/notebook/cell.py.rej
abort: patch failed to apply
```


Cheers,

Michael



---

archive/issue_comments_020572.json:
```json
{
    "body": "Attachment [sage-2988_rebased.patch](tarball://root/attachments/some-uuid/ticket2988/sage-2988_rebased.patch) by was created at 2008-04-22 04:16:55",
    "created_at": "2008-04-22T04:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2988#issuecomment-20572",
    "user": "was"
}
```

Attachment [sage-2988_rebased.patch](tarball://root/attachments/some-uuid/ticket2988/sage-2988_rebased.patch) by was created at 2008-04-22 04:16:55



---

archive/issue_comments_020573.json:
```json
{
    "body": "Merged sage-2988_rebased.patch in Sage 3.0.final",
    "created_at": "2008-04-22T04:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2988#issuecomment-20573",
    "user": "mabshoff"
}
```

Merged sage-2988_rebased.patch in Sage 3.0.final



---

archive/issue_comments_020574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-22T04:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2988",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2988#issuecomment-20574",
    "user": "mabshoff"
}
```

Resolution: fixed
