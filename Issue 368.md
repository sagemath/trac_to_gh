# Issue 368: {{{ }}} for worksheet text mode won't cut it.

archive/issues_000368.json:
```json
{
    "body": "Assignee: boothby\n\nTry this\n\n\n```\nvar('x a b')\nshow(solve(x^3 + c*x + b ==0, x)[0])\n```\n\n\nThen eval, click edit and save.\nIt doesn't work since the output of show\nhas }}} in it -- it's part of valid latex.\n\nWhat are we to do?\n\nIssue created by migration from https://trac.sagemath.org/ticket/368\n\n",
    "created_at": "2007-05-18T16:12:13Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "title": "{{{ }}} for worksheet text mode won't cut it.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/368",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Try this


```
var('x a b')
show(solve(x^3 + c*x + b ==0, x)[0])
```


Then eval, click edit and save.
It doesn't work since the output of show
has }}} in it -- it's part of valid latex.

What are we to do?

Issue created by migration from https://trac.sagemath.org/ticket/368





---

archive/issue_events_000390.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-05-31T14:55:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/368",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/368#event-390"
}
```



---

archive/issue_comments_001766.json:
```json
{
    "body": "Fixed by requiring }}} to have a newline before it.  That's hackish, but better than\nnothing.",
    "created_at": "2007-05-31T14:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/368#issuecomment-1766",
    "user": "https://github.com/williamstein"
}
```

Fixed by requiring }}} to have a newline before it.  That's hackish, but better than
nothing.



---

archive/issue_comments_001767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-31T14:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/368#issuecomment-1767",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
