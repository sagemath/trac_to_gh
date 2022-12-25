# Issue 382: Unitialized variable in error message

archive/issues_000382.json:
```json
{
    "body": "Assignee: @williamstein\n\nIn \"databases/db_class_polynomials.py:_dbpath()\", the \"NYI\" error for level>1 refers\nto the variable 's'; it should be 'level'. \n\nBundle attached.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/382\n\n",
    "created_at": "2007-05-29T04:23:16Z",
    "labels": [
        "component: algebraic geometry",
        "trivial",
        "bug"
    ],
    "title": "Unitialized variable in error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/382",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

In "databases/db_class_polynomials.py:_dbpath()", the "NYI" error for level>1 refers
to the variable 's'; it should be 'level'. 

Bundle attached.


Issue created by migration from https://trac.sagemath.org/ticket/382





---

archive/issue_comments_001852.json:
```json
{
    "body": "OK, Trac blew chunks when I tried to attach the bundle.  I'm sending it out of band, to William.",
    "created_at": "2007-05-29T04:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/382#issuecomment-1852",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

OK, Trac blew chunks when I tried to attach the bundle.  I'm sending it out of band, to William.



---

archive/issue_comments_001853.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-31T13:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/382#issuecomment-1853",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000404.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-05-31T13:48:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/382",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/382#event-404"
}
```



---

archive/issue_comments_001854.json:
```json
{
    "body": "I applied the patch.",
    "created_at": "2007-05-31T13:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/382#issuecomment-1854",
    "user": "https://github.com/williamstein"
}
```

I applied the patch.
