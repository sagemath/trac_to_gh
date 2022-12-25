# Issue 3367: rename CachedFunction to cached_function

archive/issues_003367.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @mwhansen\n\nI wrote over at #3254:\nIs CachedFunction the right name though? Shouldn't it be cached_function? I think there is a different style convention for the persistent and the cached functions which is a bummer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3367\n\n",
    "created_at": "2008-06-04T21:06:05Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "rename CachedFunction to cached_function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3367",
    "user": "https://github.com/malb"
}
```
Assignee: cwitty

CC:  @mwhansen

I wrote over at #3254:
Is CachedFunction the right name though? Shouldn't it be cached_function? I think there is a different style convention for the persistent and the cached functions which is a bummer.

Issue created by migration from https://trac.sagemath.org/ticket/3367





---

archive/issue_comments_023512.json:
```json
{
    "body": "Yep, I think it should be cached_function (in fact, I import it as cached_function in my code).  CachedFunction should be deprecated.",
    "created_at": "2008-06-04T22:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3367#issuecomment-23512",
    "user": "https://github.com/mwhansen"
}
```

Yep, I think it should be cached_function (in fact, I import it as cached_function in my code).  CachedFunction should be deprecated.



---

archive/issue_comments_023513.json:
```json
{
    "body": "This is fixed in 3.1.2 at least (`CachedFunction` and `cached_function` are available now). This ticket can be closed.",
    "created_at": "2008-09-20T15:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3367#issuecomment-23513",
    "user": "https://github.com/malb"
}
```

This is fixed in 3.1.2 at least (`CachedFunction` and `cached_function` are available now). This ticket can be closed.



---

archive/issue_comments_023514.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> This is fixed in 3.1.2 at least (`CachedFunction` and `cached_function` are available now). This ticket can be closed.\n\nI thought so, too, but cached_function is just an alias for CachedFunction in the code. To close this ticket the code should be moved to cached_function and CachedFunction should be officially deprecated.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-20T20:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3367#issuecomment-23514",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 malb]:
> This is fixed in 3.1.2 at least (`CachedFunction` and `cached_function` are available now). This ticket can be closed.

I thought so, too, but cached_function is just an alias for CachedFunction in the code. To close this ticket the code should be moved to cached_function and CachedFunction should be officially deprecated.

Cheers,

Michael



---

archive/issue_comments_023515.json:
```json
{
    "body": "CCing Mike as he wrote the code in question.",
    "created_at": "2008-09-28T14:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3367#issuecomment-23515",
    "user": "https://github.com/malb"
}
```

CCing Mike as he wrote the code in question.



---

archive/issue_comments_023516.json:
```json
{
    "body": "Does it actually hurt to have the alias? I vote for closing the ticket.",
    "created_at": "2009-01-21T02:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3367#issuecomment-23516",
    "user": "https://github.com/malb"
}
```

Does it actually hurt to have the alias? I vote for closing the ticket.



---

archive/issue_comments_023517.json:
```json
{
    "body": "I think the alias is fine too.  Since CachedFunction is a class, it conforms to the naming convention for classes.",
    "created_at": "2009-01-21T02:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3367#issuecomment-23517",
    "user": "https://github.com/mwhansen"
}
```

I think the alias is fine too.  Since CachedFunction is a class, it conforms to the naming convention for classes.



---

archive/issue_comments_023518.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-02-04T21:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3367#issuecomment-23518",
    "user": "https://github.com/malb"
}
```

Resolution: wontfix
