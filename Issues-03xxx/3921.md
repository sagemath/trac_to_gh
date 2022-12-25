# Issue 3921: [with patch, positive review] calculus -- solve(..., constant) should complain by default

archive/issues_003921.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n```\n> One thing I came across is, that symbolic expressions with predefined\n> variables (i.e. they are not variables) confuse someone when used in\n> functions.\n> for example\n> x = 5\n> solve([x^2==3], x)\n> then solve does nothing. I think, because there is an explicit x, it\n> would be nice to have at least a warning message telling the user that\n> x is not a symbolic variable, but already assigned.\n>\n\nThis is an extremely good idea and trivial to implement.  \n\nWilliam\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3921\n\n",
    "closed_at": "2008-09-01T13:02:23Z",
    "created_at": "2008-08-21T15:18:05Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, positive review] calculus -- solve(..., constant) should complain by default",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3921",
    "user": "https://github.com/williamstein"
}
```
Assignee: @garyfurnish

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

archive/issue_comments_027990.json:
```json
{
    "body": "Attachment [solve_error_handling.patch](tarball://root/attachments/some-uuid/ticket3921/solve_error_handling.patch) by @jicama created at 2008-08-31 21:23:56",
    "created_at": "2008-08-31T21:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-27990",
    "user": "https://github.com/jicama"
}
```

Attachment [solve_error_handling.patch](tarball://root/attachments/some-uuid/ticket3921/solve_error_handling.patch) by @jicama created at 2008-08-31 21:23:56



---

archive/issue_comments_027991.json:
```json
{
    "body": "This patch makes sage raise a TypeError in the case mentioned above, and adds relevant doctests.",
    "created_at": "2008-08-31T21:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-27991",
    "user": "https://github.com/jicama"
}
```

This patch makes sage raise a TypeError in the case mentioned above, and adds relevant doctests.



---

archive/issue_comments_027992.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-09-01T10:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-27992",
    "user": "https://github.com/aghitza"
}
```

Looks good to me.



---

archive/issue_comments_027993.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T13:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-27993",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha4



---

archive/issue_comments_027994.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T13:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3921#issuecomment-27994",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008987.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-01T13:02:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3921",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3921#event-8987"
}
```
