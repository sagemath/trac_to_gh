# Issue 65: Profiler prints incorrect lines

archive/issues_000065.json:
```json
{
    "body": "Assignee: dmharvey\n\nThe Profiler class prints incorrect source code lines when the relevant source is right near the end of the source file (or probably right at the beginning too). Seems to be because the \"inspect\" module returns a truncated list. Shouldn't be hard to fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/65\n\n",
    "created_at": "2006-09-16T15:11:08Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Profiler prints incorrect lines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/65",
    "user": "dmharvey"
}
```
Assignee: dmharvey

The Profiler class prints incorrect source code lines when the relevant source is right near the end of the source file (or probably right at the beginning too). Seems to be because the "inspect" module returns a truncated list. Shouldn't be hard to fix.

Issue created by migration from https://trac.sagemath.org/ticket/65





---

archive/issue_comments_000336.json:
```json
{
    "body": "It would be much easier if there were an example with this bug report.  As is, it will be difficult to replicate (?).",
    "created_at": "2007-01-13T02:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/65",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/65#issuecomment-336",
    "user": "@williamstein"
}
```

It would be much easier if there were an example with this bug report.  As is, it will be difficult to replicate (?).



---

archive/issue_comments_000337.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-21T01:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/65",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/65#issuecomment-337",
    "user": "@williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_000338.json:
```json
{
    "body": "David says: \"I'm unable to reproduce the thing that I remember going wrong. So I'm\nhappy for it to be closed.\"",
    "created_at": "2007-10-21T02:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/65",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/65#issuecomment-338",
    "user": "@williamstein"
}
```

David says: "I'm unable to reproduce the thing that I remember going wrong. So I'm
happy for it to be closed."
