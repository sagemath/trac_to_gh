# Issue 6347: use faster 2^m^ implementation up to 2^62^ on 64-bit systems

archive/issues_006347.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: singular\n\nIt turns out the bug discussed at #6051 and\n\n  http://www.singular.uni-kl.de:8002/trac/ticket/138\n\nis not an upstream bug but a problem in our conversion. Fix it!\n\nIssue created by migration from https://trac.sagemath.org/ticket/6347\n\n",
    "created_at": "2009-06-17T15:32:55Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "use faster 2^m^ implementation up to 2^62^ on 64-bit systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6347",
    "user": "malb"
}
```
Assignee: malb

Keywords: singular

It turns out the bug discussed at #6051 and

  http://www.singular.uni-kl.de:8002/trac/ticket/138

is not an upstream bug but a problem in our conversion. Fix it!

Issue created by migration from https://trac.sagemath.org/ticket/6347





---

archive/issue_comments_050737.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-09-09T19:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6347#issuecomment-50737",
    "user": "malb"
}
```

Resolution: wontfix



---

archive/issue_comments_050738.json:
```json
{
    "body": "I turns out  that the assumption above is wrong. There are a couple of places in the Singular code where int is assumed so this ticket cannot be implemented unless Singular changes.",
    "created_at": "2009-09-09T19:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6347#issuecomment-50738",
    "user": "malb"
}
```

I turns out  that the assumption above is wrong. There are a couple of places in the Singular code where int is assumed so this ticket cannot be implemented unless Singular changes.
