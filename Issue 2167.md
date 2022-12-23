# Issue 2167: Echelon form of symbolic matrices does not work

archive/issues_002167.json:
```json
{
    "body": "Assignee: was\n\n\n```\nYou sage: M = Matrix([[1,0],[x,4]])\nsage: M\n\n[1 0]\n[x 4]\nsage: type(M)\n<type 'sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense'>\nsage: M.echelon_form()\n\n[1 0]\n[0 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2167\n\n",
    "created_at": "2008-02-15T00:28:45Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "Echelon form of symbolic matrices does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2167",
    "user": "moretti"
}
```
Assignee: was


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

archive/issue_comments_014224.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-02-15T00:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2167#issuecomment-14224",
    "user": "moretti"
}
```

Resolution: invalid



---

archive/issue_comments_014225.json:
```json
{
    "body": "Sorry, I realized I was giving the wrong input. It appears to be implemented.",
    "created_at": "2008-02-15T00:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2167#issuecomment-14225",
    "user": "moretti"
}
```

Sorry, I realized I was giving the wrong input. It appears to be implemented.
