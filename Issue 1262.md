# Issue 1262: "make check" needs to depend on all

archive/issues_001262.json:
```json
{
    "body": "Assignee: was\n\nIf you run \"make check\" on a sage installation that hasn't been compiled all the doctests fail one by one. Make check depend on all to fix this.\n\nCheers,\n\nMichaek\n\nIssue created by migration from https://trac.sagemath.org/ticket/1262\n\n",
    "created_at": "2007-11-25T05:44:16Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.14",
    "title": "\"make check\" needs to depend on all",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1262",
    "user": "mabshoff"
}
```
Assignee: was

If you run "make check" on a sage installation that hasn't been compiled all the doctests fail one by one. Make check depend on all to fix this.

Cheers,

Michaek

Issue created by migration from https://trac.sagemath.org/ticket/1262





---

archive/issue_comments_007920.json:
```json
{
    "body": "OK, I fixed this by modifying SAGE_ROOT/makefile slightly.",
    "created_at": "2007-11-25T05:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1262#issuecomment-7920",
    "user": "was"
}
```

OK, I fixed this by modifying SAGE_ROOT/makefile slightly.



---

archive/issue_comments_007921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-25T05:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1262#issuecomment-7921",
    "user": "was"
}
```

Resolution: fixed
