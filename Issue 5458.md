# Issue 5458: Refactor set partitions with a single entry points in global name space for the various cartan types

archive/issues_005458.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nRefactor the set partitions code to have a single entry point in the global name space for the various types. I.e. from the user point of view, replace the various:\n\n> > SetPartitions     SetPartitionsIk   SetPartitionsRk\n> > SetPartitionsAk   SetPartitionsPRk  SetPartitionsSk\n> > SetPartitionsBk   SetPartitionsPk   SetPartitionsTk\n\nBy something like:\n \tSetPartitions(..., type=[\"A\",3])\n\nSee also: http://groups.google.com/group/sage-devel/msg/a49f3288fca1b75c\n\nIssue created by migration from https://trac.sagemath.org/ticket/5458\n\n",
    "created_at": "2009-03-08T21:03:46Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Refactor set partitions with a single entry points in global name space for the various cartan types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5458",
    "user": "nthiery"
}
```
Assignee: mhansen

CC:  sage-combinat

Refactor the set partitions code to have a single entry point in the global name space for the various types. I.e. from the user point of view, replace the various:

> > SetPartitions     SetPartitionsIk   SetPartitionsRk
> > SetPartitionsAk   SetPartitionsPRk  SetPartitionsSk
> > SetPartitionsBk   SetPartitionsPk   SetPartitionsTk

By something like:
 	SetPartitions(..., type=["A",3])

See also: http://groups.google.com/group/sage-devel/msg/a49f3288fca1b75c

Issue created by migration from https://trac.sagemath.org/ticket/5458





---

archive/issue_comments_042388.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-07-23T14:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5458#issuecomment-42388",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_042389.json:
```json
{
    "body": "I think we can close this as a duplicate of #14234 which actually has some work being done on it.",
    "created_at": "2013-07-23T14:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5458#issuecomment-42389",
    "user": "mhansen"
}
```

I think we can close this as a duplicate of #14234 which actually has some work being done on it.



---

archive/issue_comments_042390.json:
```json
{
    "body": "This is not a duplicate of #14234 since that does not remove these from the global namespace, deprecate them, nor correctly pass along the correct object. There is still work to be done here, so please reopen this ticket.",
    "created_at": "2013-07-26T08:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5458#issuecomment-42390",
    "user": "tscrim"
}
```

This is not a duplicate of #14234 since that does not remove these from the global namespace, deprecate them, nor correctly pass along the correct object. There is still work to be done here, so please reopen this ticket.
