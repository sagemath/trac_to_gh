# Issue 2167: Echelon form of symbolic matrices does not work

archive/issues_002167.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nYou sage: M = Matrix([[1,0],[x,4]])\nsage: M\n\n[1 0]\n[x 4]\nsage: type(M)\n<type 'sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense'>\nsage: M.echelon_form()\n\n[1 0]\n[0 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2167\n\n",
    "created_at": "2008-02-15T00:28:45Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Echelon form of symbolic matrices does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2167",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @williamstein


```
You sage: M = Matrix([[1,0],[x,4]])
sage: M

[1 0]
[x 4]
sage: type(M)
<type 'sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense'>
sage: M.echelon_form()

[1 0]
[0 1]
```


Issue created by migration from https://trac.sagemath.org/ticket/2167





---

archive/issue_comments_014193.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-02-15T00:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2167#issuecomment-14193",
    "user": "https://github.com/bobmoretti"
}
```

Resolution: invalid



---

archive/issue_comments_014194.json:
```json
{
    "body": "Sorry, I realized I was giving the wrong input. It appears to be implemented.",
    "created_at": "2008-02-15T00:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2167#issuecomment-14194",
    "user": "https://github.com/bobmoretti"
}
```

Sorry, I realized I was giving the wrong input. It appears to be implemented.



---

archive/issue_events_005185.json:
```json
{
    "actor": "https://github.com/bobmoretti",
    "created_at": "2008-02-15T00:35:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2167",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2167#event-5185"
}
```
