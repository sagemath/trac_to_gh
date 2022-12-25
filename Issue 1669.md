# Issue 1669: remove bogus recommendation to set SAGE_ATLAS when numpy fails

archive/issues_001669.json:
```json
{
    "body": "Assignee: jkantor\n\nWhen numpy fails to build it prints the following error message which is no longer valid:\n\n```\n Error building numpy.\nTry setting SAGE_ATLAS to the directory that contains lib/libatlas.a ?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1669\n\n",
    "created_at": "2008-01-03T15:51:27Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "remove bogus recommendation to set SAGE_ATLAS when numpy fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: jkantor

When numpy fails to build it prints the following error message which is no longer valid:

```
 Error building numpy.
Try setting SAGE_ATLAS to the directory that contains lib/libatlas.a ?
```


Issue created by migration from https://trac.sagemath.org/ticket/1669





---

archive/issue_comments_010573.json:
```json
{
    "body": "This will be fixed via the new numpy.spkg linked from #1720.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-09T00:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1669#issuecomment-10573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This will be fixed via the new numpy.spkg linked from #1720.

Cheers,

Michael



---

archive/issue_events_001828.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-09T01:56:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1669",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1669#event-1828"
}
```



---

archive/issue_comments_010574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-09T01:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1669#issuecomment-10574",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010575.json:
```json
{
    "body": "Fixed in Sage 2.10.alpah1.",
    "created_at": "2008-01-09T01:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1669#issuecomment-10575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 2.10.alpah1.
