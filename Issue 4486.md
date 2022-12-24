# Issue 4486: Clean up partitions_c.cc and partitions_c.h

archive/issues_004486.json:
```json
{
    "body": "Assignee: @tornaria\n\nThese files need audited. In particular, `partitions_c.cc` should depend on `partitions_c.h`, and shouldn't duplicate the code there. Someone familiar with C should go ahead and clean these files up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4486\n\n",
    "created_at": "2008-11-09T23:22:58Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Clean up partitions_c.cc and partitions_c.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4486",
    "user": "@craigcitro"
}
```
Assignee: @tornaria

These files need audited. In particular, `partitions_c.cc` should depend on `partitions_c.h`, and shouldn't duplicate the code there. Someone familiar with C should go ahead and clean these files up.

Issue created by migration from https://trac.sagemath.org/ticket/4486





---

archive/issue_comments_033131.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4486#issuecomment-33131",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_033132.json:
```json
{
    "body": "Perhaps they could just be replaced by the implementation in arb once arb becomes a standard part of Sage.",
    "created_at": "2015-04-14T07:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4486#issuecomment-33132",
    "user": "@mezzarobba"
}
```

Perhaps they could just be replaced by the implementation in arb once arb becomes a standard part of Sage.
