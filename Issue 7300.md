# Issue 7300: Display tight constraints

archive/issues_007300.json:
```json
{
    "body": "Assignee: jkantor\n\nIt is often useful when solving linear programs to see which constraints are tight.... And so there should be a way to do it in Sage !!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7300\n\n",
    "created_at": "2009-10-25T19:42:04Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Display tight constraints",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7300",
    "user": "ncohen"
}
```
Assignee: jkantor

It is often useful when solving linear programs to see which constraints are tight.... And so there should be a way to do it in Sage !!!

Issue created by migration from https://trac.sagemath.org/ticket/7300





---

archive/issue_comments_060845.json:
```json
{
    "body": "Changing component from numerical to linear programming.",
    "created_at": "2010-09-06T11:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7300#issuecomment-60845",
    "user": "ncohen"
}
```

Changing component from numerical to linear programming.



---

archive/issue_comments_060846.json:
```json
{
    "body": "Perhaps there should be a `MixedIntegerLinearProgram` method similar to `get_values` that retrieves the values of the constraint functions at the current solution; its input should be the same as the input to `constraints`.\n\nNote also that some backends already have support for getting this kind of information, for example GLPK has `get_row_prim`.",
    "created_at": "2016-04-03T19:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7300",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7300#issuecomment-60846",
    "user": "mkoeppe"
}
```

Perhaps there should be a `MixedIntegerLinearProgram` method similar to `get_values` that retrieves the values of the constraint functions at the current solution; its input should be the same as the input to `constraints`.

Note also that some backends already have support for getting this kind of information, for example GLPK has `get_row_prim`.
