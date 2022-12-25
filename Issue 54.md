# Issue 54: guaranteed correct result for log(integer, integer)

archive/issues_000054.json:
```json
{
    "body": "Assignee: somebody\n\nIn a current project, I often want to know the largest power of a prime p that is less than or equal to a given integer n. I used int(log(n, p)) in these cases, but I'm concerned that there might be precision issues in this floating point calculation. It would be nice to have some function that was guaranteed to return the correct result for floor(log(n, p)), where n and p are integers. Perhaps call it floor_log or something.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/54\n\n",
    "created_at": "2006-09-13T20:40:38Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "title": "guaranteed correct result for log(integer, integer)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/54",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

In a current project, I often want to know the largest power of a prime p that is less than or equal to a given integer n. I used int(log(n, p)) in these cases, but I'm concerned that there might be precision issues in this floating point calculation. It would be nice to have some function that was guaranteed to return the correct result for floor(log(n, p)), where n and p are integers. Perhaps call it floor_log or something.


Issue created by migration from https://trac.sagemath.org/ticket/54





---

archive/issue_comments_000291.json:
```json
{
    "body": "fixed -- added Integer.exact_log()",
    "created_at": "2006-09-22T01:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/54",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/54#issuecomment-291",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

fixed -- added Integer.exact_log()



---

archive/issue_comments_000292.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-09-22T01:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/54",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/54#issuecomment-292",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Resolution: fixed



---

archive/issue_events_000053.json:
```json
{
    "actor": "dmharvey",
    "created_at": "2006-09-22T01:21:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/54",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/54#event-53"
}
```
