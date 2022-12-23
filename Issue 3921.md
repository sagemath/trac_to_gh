# Issue 3921: calculus -- solve(..., constant) should complain by default

archive/issues_003921.json:
```json
{
    "body": "Assignee: gfurnish\n\n\n```\n> One thing I came across is, that symbolic expressions with predefined\n> variables (i.e. they are not variables) confuse someone when used in\n> functions.\n> for example\n> x = 5\n> solve([x^2==3], x)\n> then solve does nothing. I think, because there is an explicit x, it\n> would be nice to have at least a warning message telling the user that\n> x is not a symbolic variable, but already assigned.\n>\n\nThis is an extremely good idea and trivial to implement.  \n\nWilliam\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3921\n\n",
    "created_at": "2008-08-21T15:18:05Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "calculus -- solve(..., constant) should complain by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3921",
    "user": "was"
}
```
Assignee: gfurnish


```
> One thing I came across is, that symbolic expressions with predefined
> variables (i.e. they are not variables) confuse someone when used in
> functions.
> for example
> x = 5
> solve([x^2==3], x)
> then solve does nothing. I think, because there is an explicit x, it
> would be nice to have at least a warning message telling the user that
> x is not a symbolic variable, but already assigned.
>

This is an extremely good idea and trivial to implement.  

William
```




Issue created by migration from https://trac.sagemath.org/ticket/3921





---

archive/issue_comments_028048.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-31T21:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-28048",
    "user": "jwmerrill"
}
```

Attachment



---

archive/issue_comments_028049.json:
```json
{
    "body": "This patch makes sage raise a TypeError in the case mentioned above, and adds relevant doctests.",
    "created_at": "2008-08-31T21:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-28049",
    "user": "jwmerrill"
}
```

This patch makes sage raise a TypeError in the case mentioned above, and adds relevant doctests.



---

archive/issue_comments_028050.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-01T10:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-28050",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_028051.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T13:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-28051",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha4



---

archive/issue_comments_028052.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T13:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-28052",
    "user": "mabshoff"
}
```

Resolution: fixed
