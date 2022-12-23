# Issue 4324: [with patch, needs review] fix storage of GBs for PolyBoRi

archive/issues_004324.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  polybori\n\nThe current code prevents certain GB calculations to finish because it throws a ValueError just before the GB is returned (quit annoying).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4324\n\n",
    "created_at": "2008-10-19T15:54:13Z",
    "labels": [
        "algebra",
        "critical",
        "bug"
    ],
    "title": "[with patch, needs review] fix storage of GBs for PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4324",
    "user": "malb"
}
```
Assignee: tbd

CC:  polybori

The current code prevents certain GB calculations to finish because it throws a ValueError just before the GB is returned (quit annoying).

Issue created by migration from https://trac.sagemath.org/ticket/4324





---

archive/issue_comments_031680.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-19T15:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4324#issuecomment-31680",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_031681.json:
```json
{
    "body": "the patch is okay.\nNote, that the bug can only occur, when a system is passed, which is not a minimal GB.\nHowever, that's possible.\n\nIn the future version PolyBoRi 0.6 pure reduction can be implemented more efficiently without handling sets.\nHowever, you will need a different workaround there\n\n```\nr=ReductionStrategy()\nif not p.lead() in r.leading_terms:\n  r.add_generator(p)\n```\n",
    "created_at": "2008-10-21T08:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4324#issuecomment-31681",
    "user": "PolyBoRi"
}
```

the patch is okay.
Note, that the bug can only occur, when a system is passed, which is not a minimal GB.
However, that's possible.

In the future version PolyBoRi 0.6 pure reduction can be implemented more efficiently without handling sets.
However, you will need a different workaround there

```
r=ReductionStrategy()
if not p.lead() in r.leading_terms:
  r.add_generator(p)
```




---

archive/issue_comments_031682.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-26T14:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4324#issuecomment-31682",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_comments_031683.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T14:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4324#issuecomment-31683",
    "user": "mabshoff"
}
```

Resolution: fixed
