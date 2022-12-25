# Issue 6885: Excessive nesting in PDF reference manual, possibly from ring.pyx

archive/issues_006885.json:
```json
{
    "body": "Assignee: tba\n\nWhen building the PDF reference manual on 64-bit Fedora 10:\n\n```\n[1913] [1914] [1915] [1916]\nChapter 24.\n\n! LaTeX Error: Too deeply nested.\n\nSee the LaTeX manual or LaTeX Companion for explanation.\nType  H <return>  for immediate help.\n ...\n\nl.154726 \\begin{itemize}\n\n?\n```\n\nI think this is near the beginning of `sage/rings/ring.pyx`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6885\n\n",
    "created_at": "2009-09-04T08:02:16Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Excessive nesting in PDF reference manual, possibly from ring.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6885",
    "user": "https://github.com/qed777"
}
```
Assignee: tba

When building the PDF reference manual on 64-bit Fedora 10:

```
[1913] [1914] [1915] [1916]
Chapter 24.

! LaTeX Error: Too deeply nested.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...

l.154726 \begin{itemize}

?
```

I think this is near the beginning of `sage/rings/ring.pyx`.


Issue created by migration from https://trac.sagemath.org/ticket/6885





---

archive/issue_comments_056786.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-22T20:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6885#issuecomment-56786",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_056787.json:
```json
{
    "body": "Close this ticket as duplicate of #6988.",
    "created_at": "2009-09-22T20:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6885#issuecomment-56787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close this ticket as duplicate of #6988.



---

archive/issue_events_016190.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-22T20:14:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6885",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6885#event-16190"
}
```



---

archive/issue_events_016191.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-22T20:14:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6885",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6885#event-16191"
}
```
