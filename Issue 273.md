# Issue 273: sage-location path extraction thrown off by extra "local"

archive/issues_000273.json:
```json
{
    "body": "Assignee: @williamstein\n\nline 35 in sage-location tries to split off SAGE-ROOT by looking for the first occurrence of\n\"local/\" in the string. This fails if, for instance, sage is installed in\n\"/usr/local/sage/latestversion/...\"\n\nA fix that seems to work at present if to search for the last occurrence of \"local/\" instead:\n\n```\n           i = z.rfind('local/')\n```\n\n\nOne would have to check that no further \"local/\" can occur inside\n$SAGE_ROOT/local/\nin order for this criterion to work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/273\n\n",
    "created_at": "2007-02-21T02:05:02Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.2",
    "title": "sage-location path extraction thrown off by extra \"local\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/273",
    "user": "https://github.com/nbruin"
}
```
Assignee: @williamstein

line 35 in sage-location tries to split off SAGE-ROOT by looking for the first occurrence of
"local/" in the string. This fails if, for instance, sage is installed in
"/usr/local/sage/latestversion/..."

A fix that seems to work at present if to search for the last occurrence of "local/" instead:

```
           i = z.rfind('local/')
```


One would have to check that no further "local/" can occur inside
$SAGE_ROOT/local/
in order for this criterion to work.

Issue created by migration from https://trac.sagemath.org/ticket/273





---

archive/issue_events_000290.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-02-24T03:06:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/273",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/273#event-290"
}
```



---

archive/issue_comments_001294.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-24T03:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/273#issuecomment-1294",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001295.json:
```json
{
    "body": "Fixed for sage-2.2.",
    "created_at": "2007-02-24T03:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/273#issuecomment-1295",
    "user": "https://github.com/williamstein"
}
```

Fixed for sage-2.2.
