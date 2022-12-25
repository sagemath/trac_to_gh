# Issue 1345: I is sometimes wrapped in SymbolicConstant, sometimes not

archive/issues_001345.json:
```json
{
    "body": "Assignee: @mwhansen\n\nThis behavior seems strange:\n\n```\n sage: foo = I+I\n sage: foo._operands\n [I, I]\n sage: [type(i) for i in foo._operands]\n [<class 'sage.calculus.calculus.SymbolicConstant'>,\n  <class 'sage.functions.constants.I_class'>]\n```\n\nAnd here's another strange thing (probably the same bug):\n\n```\n sage: is_SymbolicExpression(SR(I))\n False\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1345\n\n",
    "created_at": "2007-11-30T22:20:45Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "I is sometimes wrapped in SymbolicConstant, sometimes not",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1345",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @mwhansen

This behavior seems strange:

```
 sage: foo = I+I
 sage: foo._operands
 [I, I]
 sage: [type(i) for i in foo._operands]
 [<class 'sage.calculus.calculus.SymbolicConstant'>,
  <class 'sage.functions.constants.I_class'>]
```

And here's another strange thing (probably the same bug):

```
 sage: is_SymbolicExpression(SR(I))
 False
```


Issue created by migration from https://trac.sagemath.org/ticket/1345





---

archive/issue_comments_008598.json:
```json
{
    "body": "Attachment [1345.patch](tarball://root/attachments/some-uuid/ticket1345/1345.patch) by @mwhansen created at 2007-11-30 22:56:37",
    "created_at": "2007-11-30T22:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8598",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1345.patch](tarball://root/attachments/some-uuid/ticket1345/1345.patch) by @mwhansen created at 2007-11-30 22:56:37



---

archive/issue_comments_008599.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-30T22:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8599",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008600.json:
```json
{
    "body": "This should be applied after #847.",
    "created_at": "2007-11-30T23:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8600",
    "user": "https://github.com/mwhansen"
}
```

This should be applied after #847.



---

archive/issue_comments_008601.json:
```json
{
    "body": "The code looks good and the doctests in the affected files pass.  I approve.",
    "created_at": "2007-12-01T02:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8601",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The code looks good and the doctests in the affected files pass.  I approve.



---

archive/issue_comments_008602.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_008603.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001487.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-01T11:14:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1345#event-1487"
}
```
