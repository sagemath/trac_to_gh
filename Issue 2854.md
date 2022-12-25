# Issue 2854: A correction to the weight of crystal elements for type A and a speedup for all types

archive/issues_002854.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nFor Cartan Types 'A' a problem with the weight function of crystals was described here:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7cdfe075257ba963?hl=en\n\nThe method of correcting this problem was to hard-code the weight in the crystals of letters, \nand to have the crystals of tensors get the weight of a tensor element by summing the weights \nof its constituents. This alters the weight for Type A (correcting the defect) and returns the\nsame weight as the old algorithm for other Cartan types.\n\nWhen the patch was implemented it was found to be 2-3 times faster than the old algorithm.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2854\n\n",
    "created_at": "2008-04-08T06:00:48Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "A correction to the weight of crystal elements for type A and a speedup for all types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2854",
    "user": "https://github.com/dwbump"
}
```
Assignee: @mwhansen

CC:  sage-combinat

For Cartan Types 'A' a problem with the weight function of crystals was described here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/7cdfe075257ba963?hl=en

The method of correcting this problem was to hard-code the weight in the crystals of letters, 
and to have the crystals of tensors get the weight of a tensor element by summing the weights 
of its constituents. This alters the weight for Type A (correcting the defect) and returns the
same weight as the old algorithm for other Cartan types.

When the patch was implemented it was found to be 2-3 times faster than the old algorithm.

Issue created by migration from https://trac.sagemath.org/ticket/2854





---

archive/issue_comments_019548.json:
```json
{
    "body": "Attachment [crystal_weights.patch](tarball://root/attachments/some-uuid/ticket2854/crystal_weights.patch) by @mwhansen created at 2008-04-08 06:10:44",
    "created_at": "2008-04-08T06:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2854#issuecomment-19548",
    "user": "https://github.com/mwhansen"
}
```

Attachment [crystal_weights.patch](tarball://root/attachments/some-uuid/ticket2854/crystal_weights.patch) by @mwhansen created at 2008-04-08 06:10:44



---

archive/issue_comments_019549.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-04-08T06:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2854#issuecomment-19549",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_006536.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-04-08T06:10:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2854",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2854#event-6536"
}
```
