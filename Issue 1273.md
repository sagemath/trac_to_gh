# Issue 1273: [with patch] implement complex root isolation

archive/issues_001273.json:
```json
{
    "body": "Assignee: somebody\n\nI'm attaching a patch that implements complex root isolation for exact polynomials.  It uses a fairly inefficient strategy (find the roots using numpy or Pari, then verify them using interval arithmetic), but it does work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1273\n\n",
    "created_at": "2007-11-25T21:33:03Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "[with patch] implement complex root isolation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1273",
    "user": "cwitty"
}
```
Assignee: somebody

I'm attaching a patch that implements complex root isolation for exact polynomials.  It uses a fairly inefficient strategy (find the roots using numpy or Pari, then verify them using interval arithmetic), but it does work.

Issue created by migration from https://trac.sagemath.org/ticket/1273





---

archive/issue_comments_007971.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-25T21:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7971",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_007972.json:
```json
{
    "body": "I forgot to mention... this patch depends on the patch from #1270, which must be applied first.",
    "created_at": "2007-11-25T21:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7972",
    "user": "cwitty"
}
```

I forgot to mention... this patch depends on the patch from #1270, which must be applied first.



---

archive/issue_comments_007973.json:
```json
{
    "body": "Fast!",
    "created_at": "2007-11-30T05:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7973",
    "user": "rlm"
}
```

Fast!



---

archive/issue_comments_007974.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T10:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7974",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_007975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T10:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7975",
    "user": "mabshoff"
}
```

Resolution: fixed
