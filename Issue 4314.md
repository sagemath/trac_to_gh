# Issue 4314: [with patch] Add some functionality to matrices in eclib

archive/issues_004314.json:
```json
{
    "body": "Assignee: was\n\nKeywords: eclib CremonaModularSymbols\n\nThe attached patch (based on 3.1.4) makes two changes in libs/cremona/mat*:\n1. Adds getitem methods to the matric class so i,j entries may be extracted;\n2. Changes the conversion to sage of matrices so that matrices over ZZ are constructed instead of ZZ.\n\nThese were done as part of a hands-on tutorial William gave to John in Bordeaux.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4314\n\n",
    "created_at": "2008-10-17T17:12:39Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch] Add some functionality to matrices in eclib",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4314",
    "user": "cremona"
}
```
Assignee: was

Keywords: eclib CremonaModularSymbols

The attached patch (based on 3.1.4) makes two changes in libs/cremona/mat*:
1. Adds getitem methods to the matric class so i,j entries may be extracted;
2. Changes the conversion to sage of matrices so that matrices over ZZ are constructed instead of ZZ.

These were done as part of a hands-on tutorial William gave to John in Bordeaux.

Issue created by migration from https://trac.sagemath.org/ticket/4314





---

archive/issue_comments_031583.json:
```json
{
    "body": "This is a dupe of #4313",
    "created_at": "2008-10-18T10:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4314#issuecomment-31583",
    "user": "mhansen"
}
```

This is a dupe of #4313



---

archive/issue_comments_031584.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-10-18T10:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4314#issuecomment-31584",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_031585.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> This is a dupe of #4313\n\nThanks.  One day I'll succeed in creating a new ticket with a pre-existing patch without causing a duplication!",
    "created_at": "2008-10-18T14:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4314#issuecomment-31585",
    "user": "cremona"
}
```

Replying to [comment:1 mhansen]:
> This is a dupe of #4313

Thanks.  One day I'll succeed in creating a new ticket with a pre-existing patch without causing a duplication!
