# Issue 710: bad segfault when hitting control-c

archive/issues_000710.json:
```json
{
    "body": "Assignee: somebody\n\nTry this:\n\n\n```\nsage: n=factor(2^997-1)\n[hit control c]\n---------------------------------------------------------------------------\n<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)\n\nsage: gp.eval('factor(2^997-1)')\n[hit control c]\nSegmentation fault (core dumped)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/710\n\n",
    "created_at": "2007-09-20T18:13:04Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "bad segfault when hitting control-c",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/710",
    "user": "@williamstein"
}
```
Assignee: somebody

Try this:


```
sage: n=factor(2^997-1)
[hit control c]
---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)

sage: gp.eval('factor(2^997-1)')
[hit control c]
Segmentation fault (core dumped)
```


Issue created by migration from https://trac.sagemath.org/ticket/710





---

archive/issue_comments_003729.json:
```json
{
    "body": "This is now fixed for the next SAGE release by Stein and Tornaria.  The fixes involved fixing some\nmistakes in gen.pyx a rewriting interrupt.c/h somewhat.",
    "created_at": "2007-09-21T05:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/710#issuecomment-3729",
    "user": "@williamstein"
}
```

This is now fixed for the next SAGE release by Stein and Tornaria.  The fixes involved fixing some
mistakes in gen.pyx a rewriting interrupt.c/h somewhat.



---

archive/issue_comments_003730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T05:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/710#issuecomment-3730",
    "user": "@williamstein"
}
```

Resolution: fixed
