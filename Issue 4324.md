# Issue 4324: [with patch, needs review] fix storage of GBs for PolyBoRi

archive/issues_004324.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  polybori\n\nThe current code prevents certain GB calculations to finish because it throws a ValueError just before the GB is returned (quit annoying).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4324\n\n",
    "created_at": "2008-10-19T15:54:13Z",
    "labels": [
        "component: algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] fix storage of GBs for PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4324",
    "user": "https://github.com/malb"
}
```
Assignee: tbd

CC:  polybori

The current code prevents certain GB calculations to finish because it throws a ValueError just before the GB is returned (quit annoying).

Issue created by migration from https://trac.sagemath.org/ticket/4324





---

archive/issue_comments_031618.json:
```json
{
    "body": "Attachment [pbori_bugfix.patch](tarball://root/attachments/some-uuid/ticket4324/pbori_bugfix.patch) by @malb created at 2008-10-19 15:54:40",
    "created_at": "2008-10-19T15:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4324#issuecomment-31618",
    "user": "https://github.com/malb"
}
```

Attachment [pbori_bugfix.patch](tarball://root/attachments/some-uuid/ticket4324/pbori_bugfix.patch) by @malb created at 2008-10-19 15:54:40



---

archive/issue_comments_031619.json:
```json
{
    "body": "the patch is okay.\nNote, that the bug can only occur, when a system is passed, which is not a minimal GB.\nHowever, that's possible.\n\nIn the future version PolyBoRi 0.6 pure reduction can be implemented more efficiently without handling sets.\nHowever, you will need a different workaround there\n\n```\nr=ReductionStrategy()\nif not p.lead() in r.leading_terms:\n  r.add_generator(p)\n```\n",
    "created_at": "2008-10-21T08:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4324#issuecomment-31619",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
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

archive/issue_comments_031620.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-26T14:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4324#issuecomment-31620",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_events_009784.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-26T14:13:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4324#event-9784"
}
```



---

archive/issue_comments_031621.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T14:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4324#issuecomment-31621",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
