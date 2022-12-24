# Issue 2855: A correction to the weight of crystal elements for type A and a speedup for all types

archive/issues_002855.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nFor Cartan Types 'A' a problem with the weight function of crystals was described here:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7cdfe075257ba963?hl=en\n\nThe method of correcting this problem was to hard-code the weight in the crystals of letters, \nand to have the crystals of tensors get the weight of a tensor element by summing the weights \nof its constituents. This alters the weight for Type A (correcting the defect) and returns the\nsame weight as the old algorithm for other Cartan types.\n\nWhen the patch was implemented it was found to be 2-3 times faster than the old algorithm.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2855\n\n",
    "created_at": "2008-04-08T06:03:01Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "A correction to the weight of crystal elements for type A and a speedup for all types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2855",
    "user": "bump"
}
```
Assignee: mhansen

CC:  sage-combinat

For Cartan Types 'A' a problem with the weight function of crystals was described here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7cdfe075257ba963?hl=en

The method of correcting this problem was to hard-code the weight in the crystals of letters, 
and to have the crystals of tensors get the weight of a tensor element by summing the weights 
of its constituents. This alters the weight for Type A (correcting the defect) and returns the
same weight as the old algorithm for other Cartan types.

When the patch was implemented it was found to be 2-3 times faster than the old algorithm.

Issue created by migration from https://trac.sagemath.org/ticket/2855





---

archive/issue_comments_019591.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-04-08T06:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2855#issuecomment-19591",
    "user": "bump"
}
```

Resolution: duplicate
