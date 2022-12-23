# Issue 1669: remove bogus recommendation to set SAGE_ATLAS when numpy fails

archive/issues_001669.json:
```json
{
    "body": "Assignee: jkantor\n\nWhen numpy fails to build it prints the following error message which is no longer valid:\n\n```\n Error building numpy.\nTry setting SAGE_ATLAS to the directory that contains lib/libatlas.a ?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1669\n\n",
    "created_at": "2008-01-03T15:51:27Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "remove bogus recommendation to set SAGE_ATLAS when numpy fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1669",
    "user": "mabshoff"
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

archive/issue_comments_010600.json:
```json
{
    "body": "This will be fixed via the new numpy.spkg linked from #1720.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-09T00:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1669#issuecomment-10600",
    "user": "mabshoff"
}
```

This will be fixed via the new numpy.spkg linked from #1720.

Cheers,

Michael



---

archive/issue_comments_010601.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-09T01:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1669#issuecomment-10601",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010602.json:
```json
{
    "body": "Fixed in Sage 2.10.alpah1.",
    "created_at": "2008-01-09T01:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1669#issuecomment-10602",
    "user": "mabshoff"
}
```

Fixed in Sage 2.10.alpah1.
