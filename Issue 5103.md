# Issue 5103: setup.py: dependency checking does not ignore comments

archive/issues_005103.json:
```json
{
    "body": "Assignee: mabshoff\n\n    *\n\nHello,\n\nreading the code, I see another problem if ones has the following line in its .pyx:\n\n\n```\ncimport mod#mycomment\n```\n\n\nI such a case, we'll look for a dependency mod#mycomment.pxd instead of mod.pxd.\n\nOtherwise, the patch solves the aforementioned problems.\n\nCheers\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5103\n\n",
    "created_at": "2009-01-26T16:44:25Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "setup.py: dependency checking does not ignore comments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5103",
    "user": "mhansen"
}
```
Assignee: mabshoff

    *

Hello,

reading the code, I see another problem if ones has the following line in its .pyx:


```
cimport mod#mycomment
```


I such a case, we'll look for a dependency mod#mycomment.pxd instead of mod.pxd.

Otherwise, the patch solves the aforementioned problems.

Cheers


Issue created by migration from https://trac.sagemath.org/ticket/5103





---

archive/issue_comments_038970.json:
```json
{
    "body": "This is a dupe of #5104.",
    "created_at": "2009-01-26T16:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5103#issuecomment-38970",
    "user": "craigcitro"
}
```

This is a dupe of #5104.



---

archive/issue_comments_038971.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-26T16:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5103#issuecomment-38971",
    "user": "craigcitro"
}
```

Resolution: duplicate
