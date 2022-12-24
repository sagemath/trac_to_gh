# Issue 1345: I is sometimes wrapped in SymbolicConstant, sometimes not

archive/issues_001345.json:
```json
{
    "body": "Assignee: mhansen\n\nThis behavior seems strange:\n\n```\n sage: foo = I+I\n sage: foo._operands\n [I, I]\n sage: [type(i) for i in foo._operands]\n [<class 'sage.calculus.calculus.SymbolicConstant'>,\n  <class 'sage.functions.constants.I_class'>]\n```\n\nAnd here's another strange thing (probably the same bug):\n\n```\n sage: is_SymbolicExpression(SR(I))\n False\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1345\n\n",
    "created_at": "2007-11-30T22:20:45Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "I is sometimes wrapped in SymbolicConstant, sometimes not",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1345",
    "user": "cwitty"
}
```
Assignee: mhansen

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

archive/issue_comments_008622.json:
```json
{
    "body": "Attachment [1345.patch](tarball://root/attachments/some-uuid/ticket1345/1345.patch) by mhansen created at 2007-11-30 22:56:37",
    "created_at": "2007-11-30T22:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8622",
    "user": "mhansen"
}
```

Attachment [1345.patch](tarball://root/attachments/some-uuid/ticket1345/1345.patch) by mhansen created at 2007-11-30 22:56:37



---

archive/issue_comments_008623.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-30T22:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8623",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008624.json:
```json
{
    "body": "This should be applied after #847.",
    "created_at": "2007-11-30T23:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8624",
    "user": "mhansen"
}
```

This should be applied after #847.



---

archive/issue_comments_008625.json:
```json
{
    "body": "The code looks good and the doctests in the affected files pass.  I approve.",
    "created_at": "2007-12-01T02:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8625",
    "user": "cwitty"
}
```

The code looks good and the doctests in the affected files pass.  I approve.



---

archive/issue_comments_008626.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T11:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8626",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_008627.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T11:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1345#issuecomment-8627",
    "user": "mabshoff"
}
```

Resolution: fixed
