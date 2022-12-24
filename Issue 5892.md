# Issue 5892: Do not give workaround instructions when SIMD instructions aren't compatible

archive/issues_005892.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen Sage gives a warning about SIMD instructions way too many *experts* just delete the file as indicated and then complain about Sage blowing up. Don't give them the chance to do something stupid any more by removing the work around instructions. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5892\n\n",
    "created_at": "2009-04-25T09:11:58Z",
    "labels": [
        "distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Do not give workaround instructions when SIMD instructions aren't compatible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5892",
    "user": "mabshoff"
}
```
Assignee: mabshoff

When Sage gives a warning about SIMD instructions way too many *experts* just delete the file as indicated and then complain about Sage blowing up. Don't give them the chance to do something stupid any more by removing the work around instructions. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5892





---

archive/issue_comments_046602.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-15T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5892#issuecomment-46602",
    "user": "was"
}
```

Resolution: invalid



---

archive/issue_comments_046603.json:
```json
{
    "body": "The right fix is to (1) remove this SIMD stuff (already done), and (2) make a SAGE_FAT_BINARY option that actually *works*.  So far, absolutely nothing at all that has been done toward this problem has worked in the list bit.  I'm closing this ticket as invalid.",
    "created_at": "2009-06-15T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5892#issuecomment-46603",
    "user": "was"
}
```

The right fix is to (1) remove this SIMD stuff (already done), and (2) make a SAGE_FAT_BINARY option that actually *works*.  So far, absolutely nothing at all that has been done toward this problem has worked in the list bit.  I'm closing this ticket as invalid.
