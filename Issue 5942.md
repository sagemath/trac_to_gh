# Issue 5942: bug in RealIntervalField printing

archive/issues_005942.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  cwitty @mwhansen\n\nThis seems bad to me...\n\n```\nsage: p=RealIntervalField(4)(pi)\nsage: p.str(style='brackets')\n'[3.00 .. 3.25]'\nsage: p\n4.?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5942\n\n",
    "created_at": "2009-04-29T22:05:36Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in RealIntervalField printing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5942",
    "user": "ylchapuy"
}
```
Assignee: somebody

CC:  cwitty @mwhansen

This seems bad to me...

```
sage: p=RealIntervalField(4)(pi)
sage: p.str(style='brackets')
'[3.00 .. 3.25]'
sage: p
4.?
```


Issue created by migration from https://trac.sagemath.org/ticket/5942





---

archive/issue_comments_046967.json:
```json
{
    "body": "should be closed with won't fix. It's a design choice.",
    "created_at": "2009-11-26T02:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5942#issuecomment-46967",
    "user": "ylchapuy"
}
```

should be closed with won't fix. It's a design choice.



---

archive/issue_comments_046968.json:
```json
{
    "body": "Mike, I'm ccing you as this should apparently be closed.",
    "created_at": "2010-01-02T03:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5942#issuecomment-46968",
    "user": "@aghitza"
}
```

Mike, I'm ccing you as this should apparently be closed.



---

archive/issue_comments_046969.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-02T03:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5942#issuecomment-46969",
    "user": "@mwhansen"
}
```

Resolution: invalid
