# Issue 986: sage-2.8.9.rc1: order of .variety() depends on architecture in multi_polynomial_ideal.py

archive/issues_000986.json:
```json
{
    "body": "Assignee: was\n\nThis doctest fails on 32-bit x86 Linux:\n\n```\nFile \"multi_polynomial_ideal.py\", line 1078:\n    sage: V = I.variety(); V\nExpected:\n    [{y: w^2 + 2, x: 2*w}, {y: w^2 + 2*w, x: 2*w + 2}, {y: w^2 + w, x: 2*w + 1}]\nGot:\n    [{y: w^2 + w, x: 2*w + 1}, {y: w^2 + 2*w, x: 2*w + 2}, {y: w^2 + 2, x: 2*w}]\n```\n\n\nHowever, the doctest succeeds on 64-bit x86 Linux.\n\nIssue created by migration from https://trac.sagemath.org/ticket/986\n\n",
    "created_at": "2007-10-25T00:57:33Z",
    "labels": [
        "algebraic geometry",
        "blocker",
        "bug"
    ],
    "title": "sage-2.8.9.rc1: order of .variety() depends on architecture in multi_polynomial_ideal.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/986",
    "user": "cwitty"
}
```
Assignee: was

This doctest fails on 32-bit x86 Linux:

```
File "multi_polynomial_ideal.py", line 1078:
    sage: V = I.variety(); V
Expected:
    [{y: w^2 + 2, x: 2*w}, {y: w^2 + 2*w, x: 2*w + 2}, {y: w^2 + w, x: 2*w + 1}]
Got:
    [{y: w^2 + w, x: 2*w + 1}, {y: w^2 + 2*w, x: 2*w + 2}, {y: w^2 + 2, x: 2*w}]
```


However, the doctest succeeds on 64-bit x86 Linux.

Issue created by migration from https://trac.sagemath.org/ticket/986





---

archive/issue_comments_006027.json:
```json
{
    "body": "Attachment\n\nI've attached a patch that just sorts the output of .variety().",
    "created_at": "2007-10-25T01:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/986#issuecomment-6027",
    "user": "cwitty"
}
```

Attachment

I've attached a patch that just sorts the output of .variety().



---

archive/issue_comments_006028.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-25T06:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/986",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/986#issuecomment-6028",
    "user": "was"
}
```

Resolution: fixed
