# Issue 554: the calculus roots command is totally stupid.

archive/issues_000554.json:
```json
{
    "body": "Assignee: was\n\nConsider this below -- the output doesn't make any sense at all:\n\n```\nsage: var('x')\nsage: f = x^(1/9) + (2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9)\nsage: f\n(2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9) + x^(1/9)\nsage: f.roots()\n[((x^(8/9) - x^(1/9) + 2^(8/9) - 2^(1/9))/(2^(8/9) - 2^(1/9)), 1)]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/554\n\n",
    "created_at": "2007-09-01T17:25:30Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "the calculus roots command is totally stupid.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/554",
    "user": "was"
}
```
Assignee: was

Consider this below -- the output doesn't make any sense at all:

```
sage: var('x')
sage: f = x^(1/9) + (2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9)
sage: f
(2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9) + x^(1/9)
sage: f.roots()
[((x^(8/9) - x^(1/9) + 2^(8/9) - 2^(1/9))/(2^(8/9) - 2^(1/9)), 1)]
```



Issue created by migration from https://trac.sagemath.org/ticket/554





---

archive/issue_comments_002865.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-11-03T19:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/554#issuecomment-2865",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_002866.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-03T19:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/554#issuecomment-2866",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002867.json:
```json
{
    "body": "Attachment [554.patch](tarball://root/attachments/some-uuid/ticket554/554.patch) by mhansen created at 2007-11-03 19:53:39",
    "created_at": "2007-11-03T19:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/554#issuecomment-2867",
    "user": "mhansen"
}
```

Attachment [554.patch](tarball://root/attachments/some-uuid/ticket554/554.patch) by mhansen created at 2007-11-03 19:53:39



---

archive/issue_comments_002868.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T20:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/554#issuecomment-2868",
    "user": "was"
}
```

Resolution: fixed
