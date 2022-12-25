# Issue 5892: Do not give workaround instructions when SIMD instructions aren't compatible

archive/issues_005892.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen Sage gives a warning about SIMD instructions way too many *experts* just delete the file as indicated and then complain about Sage blowing up. Don't give them the chance to do something stupid any more by removing the work around instructions. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5892\n\n",
    "created_at": "2009-04-25T09:11:58Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Do not give workaround instructions when SIMD instructions aren't compatible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5892",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

When Sage gives a warning about SIMD instructions way too many *experts* just delete the file as indicated and then complain about Sage blowing up. Don't give them the chance to do something stupid any more by removing the work around instructions. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5892





---

archive/issue_events_006147.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-06-15T23:27:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5892#event-6147"
}
```



---

archive/issue_comments_046513.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-15T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5892#issuecomment-46513",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_046514.json:
```json
{
    "body": "The right fix is to (1) remove this SIMD stuff (already done), and (2) make a SAGE_FAT_BINARY option that actually *works*.  So far, absolutely nothing at all that has been done toward this problem has worked in the list bit.  I'm closing this ticket as invalid.",
    "created_at": "2009-06-15T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5892#issuecomment-46514",
    "user": "https://github.com/williamstein"
}
```

The right fix is to (1) remove this SIMD stuff (already done), and (2) make a SAGE_FAT_BINARY option that actually *works*.  So far, absolutely nothing at all that has been done toward this problem has worked in the list bit.  I'm closing this ticket as invalid.
