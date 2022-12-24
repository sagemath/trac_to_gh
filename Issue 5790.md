# Issue 5790: Updating some quirks in partition.py

archive/issues_005790.json:
```json
{
    "body": "Assignee: andrew.mathas\n\nCC:  sage-combinat jbandlow saliola\n\nKeywords: partitions, cores, quotients\n\nDear All,\n\nI have just pushed a patch to the combinat server which:\n* deprecates *r_core*, *r_quotient* (and *k_core*) in favour of *core* and *quotient*, respectively. I also made *core* return a partition rather than a list.\n* rewrite the Partition() calling function to use keywords rather than named arguments. In the process I deprecated the 'core_and_quotient' argument.\n* deprecated *partition_sign* in favour of *sign* and replaced the previous call to gap with plus or minus one as required.\n\nAlmost all of the changes are to partition.py, however, the  patch affects the following four files as they all called *r_core* or *r_quotient*::\n    sage/combinat/ktableau.py\n    sage/combinat/partition.py\n    sage/combinat/ribbon_tableau.py\n    sage/combinat/skew_partition.py\n\nNot all of the doc tests pass, however, the problems seem to be caused elsewhere.\n\nAndrew\n\nIssue created by migration from https://trac.sagemath.org/ticket/5790\n\n",
    "created_at": "2009-04-15T06:41:27Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "Updating some quirks in partition.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5790",
    "user": "andrew.mathas"
}
```
Assignee: andrew.mathas

CC:  sage-combinat jbandlow saliola

Keywords: partitions, cores, quotients

Dear All,

I have just pushed a patch to the combinat server which:
* deprecates *r_core*, *r_quotient* (and *k_core*) in favour of *core* and *quotient*, respectively. I also made *core* return a partition rather than a list.
* rewrite the Partition() calling function to use keywords rather than named arguments. In the process I deprecated the 'core_and_quotient' argument.
* deprecated *partition_sign* in favour of *sign* and replaced the previous call to gap with plus or minus one as required.

Almost all of the changes are to partition.py, however, the  patch affects the following four files as they all called *r_core* or *r_quotient*::
    sage/combinat/ktableau.py
    sage/combinat/partition.py
    sage/combinat/ribbon_tableau.py
    sage/combinat/skew_partition.py

Not all of the doc tests pass, however, the problems seem to be caused elsewhere.

Andrew

Issue created by migration from https://trac.sagemath.org/ticket/5790





---

archive/issue_comments_045332.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2009-04-15T06:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45332",
    "user": "andrew.mathas"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_045333.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2009-04-15T06:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45333",
    "user": "andrew.mathas"
}
```

Changing type from defect to task.



---

archive/issue_comments_045334.json:
```json
{
    "body": "The patch looks good. A couple of small comments.\n\n* The documentation for core still uses the terminology \"r-core\". Perhaps you can replace this with 'core' and add a note along the lines: 'sometimes called r-core and k-core in the literature'.\n\n* Same comment applies to the documentation for \"r-quotient\".",
    "created_at": "2009-04-15T15:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45334",
    "user": "saliola"
}
```

The patch looks good. A couple of small comments.

* The documentation for core still uses the terminology "r-core". Perhaps you can replace this with 'core' and add a note along the lines: 'sometimes called r-core and k-core in the literature'.

* Same comment applies to the documentation for "r-quotient".



---

archive/issue_comments_045335.json:
```json
{
    "body": "I've fixed the documentation problems...and also deprecated partition_associated, from_core_and_quotient and from_exp moving them all into Partition_class. All doc tests now pass.",
    "created_at": "2009-04-15T23:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45335",
    "user": "andrew.mathas"
}
```

I've fixed the documentation problems...and also deprecated partition_associated, from_core_and_quotient and from_exp moving them all into Partition_class. All doc tests now pass.



---

archive/issue_comments_045336.json:
```json
{
    "body": "Attachment [partition-update-AM.patch](tarball://root/attachments/some-uuid/ticket5790/partition-update-AM.patch) by andrew.mathas created at 2009-04-16 05:12:32",
    "created_at": "2009-04-16T05:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45336",
    "user": "andrew.mathas"
}
```

Attachment [partition-update-AM.patch](tarball://root/attachments/some-uuid/ticket5790/partition-update-AM.patch) by andrew.mathas created at 2009-04-16 05:12:32



---

archive/issue_comments_045337.json:
```json
{
    "body": "Attachment [partition-update-AM.2.2.patch](tarball://root/attachments/some-uuid/ticket5790/partition-update-AM.2.2.patch) by andrew.mathas created at 2009-04-16 05:15:00",
    "created_at": "2009-04-16T05:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45337",
    "user": "andrew.mathas"
}
```

Attachment [partition-update-AM.2.2.patch](tarball://root/attachments/some-uuid/ticket5790/partition-update-AM.2.2.patch) by andrew.mathas created at 2009-04-16 05:15:00



---

archive/issue_comments_045338.json:
```json
{
    "body": "Attachment [partition-update-AM.2.patch](tarball://root/attachments/some-uuid/ticket5790/partition-update-AM.2.patch) by andrew.mathas created at 2009-04-16 05:19:49\n\nI noticed that from_core_and_quotient returned a list rather than a partition, so changed this as well...",
    "created_at": "2009-04-16T05:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45338",
    "user": "andrew.mathas"
}
```

Attachment [partition-update-AM.2.patch](tarball://root/attachments/some-uuid/ticket5790/partition-update-AM.2.patch) by andrew.mathas created at 2009-04-16 05:19:49

I noticed that from_core_and_quotient returned a list rather than a partition, so changed this as well...



---

archive/issue_comments_045339.json:
```json
{
    "body": "Attachment [5790.2.patch](tarball://root/attachments/some-uuid/ticket5790/5790.2.patch) by jbandlow created at 2009-06-15 19:58:47\n\nI've rebased this to apply to 4.0.1; all doctests pass.  I give a positive review to all of Andrew's changes, but I've left the status as 'needs review' so someone has a chance approve my changes.  Let's get this in quickly before we need to rebase again!  :)",
    "created_at": "2009-06-15T19:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45339",
    "user": "jbandlow"
}
```

Attachment [5790.2.patch](tarball://root/attachments/some-uuid/ticket5790/5790.2.patch) by jbandlow created at 2009-06-15 19:58:47

I've rebased this to apply to 4.0.1; all doctests pass.  I give a positive review to all of Andrew's changes, but I've left the status as 'needs review' so someone has a chance approve my changes.  Let's get this in quickly before we need to rebase again!  :)



---

archive/issue_comments_045340.json:
```json
{
    "body": "I'm changing this from \"task\" to \"enhancement\" to make sure it shows up in the right queries and searches. Tasks somehow seem to get lost too easily.",
    "created_at": "2009-06-16T01:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45340",
    "user": "ddrake"
}
```

I'm changing this from "task" to "enhancement" to make sure it shows up in the right queries and searches. Tasks somehow seem to get lost too easily.



---

archive/issue_comments_045341.json:
```json
{
    "body": "Changing type from task to enhancement.",
    "created_at": "2009-06-16T01:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45341",
    "user": "ddrake"
}
```

Changing type from task to enhancement.



---

archive/issue_comments_045342.json:
```json
{
    "body": "Attachment [trac_5790-review.patch](tarball://root/attachments/some-uuid/ticket5790/trac_5790-review.patch) by saliola created at 2009-06-21 19:31:19\n\nApply only 5790.2.patch and this patch (in this order)",
    "created_at": "2009-06-21T19:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45342",
    "user": "saliola"
}
```

Attachment [trac_5790-review.patch](tarball://root/attachments/some-uuid/ticket5790/trac_5790-review.patch) by saliola created at 2009-06-21 19:31:19

Apply only 5790.2.patch and this patch (in this order)



---

archive/issue_comments_045343.json:
```json
{
    "body": "Andrew's changes made `from_exp` and `from_core_and_quotient`\nmethods of a partition, but they shouldn't be since they don't depend on\nthe partition at all. It's strange, to me, to have the constructor work\nthis way:\n\n\n```\nsage: p = Partition([])\nsage: p.from_exp([3,2,1])\n[3, 2, 2, 1, 1, 1]\n\nsage: q = Partition([3,2,2,1,1,1])\nsage: q.from_exp([3,2,1])\n[3, 2, 2, 1, 1, 1]\n```\n\n\nI've reverted those changes in my review patch, otherwise it looks good. \n\nTo be clear: I do not object to gathering all the code for constructing\npartitions into one class. Perhaps a new `PartitionConstructor` class\nwould be better? Either way, this is not the point of this ticket.\n\nSomeone needs to look over my changes, of course.\n\nApply only 5790.2.patch and trac_5790-review.patch.",
    "created_at": "2009-06-21T19:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45343",
    "user": "saliola"
}
```

Andrew's changes made `from_exp` and `from_core_and_quotient`
methods of a partition, but they shouldn't be since they don't depend on
the partition at all. It's strange, to me, to have the constructor work
this way:


```
sage: p = Partition([])
sage: p.from_exp([3,2,1])
[3, 2, 2, 1, 1, 1]

sage: q = Partition([3,2,2,1,1,1])
sage: q.from_exp([3,2,1])
[3, 2, 2, 1, 1, 1]
```


I've reverted those changes in my review patch, otherwise it looks good. 

To be clear: I do not object to gathering all the code for constructing
partitions into one class. Perhaps a new `PartitionConstructor` class
would be better? Either way, this is not the point of this ticket.

Someone needs to look over my changes, of course.

Apply only 5790.2.patch and trac_5790-review.patch.



---

archive/issue_comments_045344.json:
```json
{
    "body": "I am looking at it. Should be done tonight.",
    "created_at": "2009-07-17T17:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45344",
    "user": "nthiery"
}
```

I am looking at it. Should be done tonight.



---

archive/issue_comments_045345.json:
```json
{
    "body": "I rechecked the patches, merged them all together, did a couple minor doc fixes, renamed key_word into keyowrd, and merged in my patch on sage-combinat adding a doctest to the deprecation things for r_core and r_quotient (and fixed them, since they actually were broken) + updating of the llt code. The patch applies cleanly on 4.1. All tests pass. I consider it as good to go.\n\nFor the record. I am also about to attach a diff of my changes, should someone want to double checks.",
    "created_at": "2009-07-17T21:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45345",
    "user": "nthiery"
}
```

I rechecked the patches, merged them all together, did a couple minor doc fixes, renamed key_word into keyowrd, and merged in my patch on sage-combinat adding a doctest to the deprecation things for r_core and r_quotient (and fixed them, since they actually were broken) + updating of the llt code. The patch applies cleanly on 4.1. All tests pass. I consider it as good to go.

For the record. I am also about to attach a diff of my changes, should someone want to double checks.



---

archive/issue_comments_045346.json:
```json
{
    "body": "Apply only this one",
    "created_at": "2009-07-17T21:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45346",
    "user": "nthiery"
}
```

Apply only this one



---

archive/issue_comments_045347.json:
```json
{
    "body": "Attachment [trac_5790-partition.patch](tarball://root/attachments/some-uuid/ticket5790/trac_5790-partition.patch) by nthiery created at 2009-07-17 21:40:29\n\nFor the record. Don't apply.",
    "created_at": "2009-07-17T21:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45347",
    "user": "nthiery"
}
```

Attachment [trac_5790-partition.patch](tarball://root/attachments/some-uuid/ticket5790/trac_5790-partition.patch) by nthiery created at 2009-07-17 21:40:29

For the record. Don't apply.



---

archive/issue_comments_045348.json:
```json
{
    "body": "Attachment [trac_5790_review_nt.patch](tarball://root/attachments/some-uuid/ticket5790/trac_5790_review_nt.patch) by saliola created at 2009-07-17 22:24:45\n\nI give a positive review to Nicolas's changes.",
    "created_at": "2009-07-17T22:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45348",
    "user": "saliola"
}
```

Attachment [trac_5790_review_nt.patch](tarball://root/attachments/some-uuid/ticket5790/trac_5790_review_nt.patch) by saliola created at 2009-07-17 22:24:45

I give a positive review to Nicolas's changes.



---

archive/issue_comments_045349.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T15:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45349",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_045350.json:
```json
{
    "body": "Merged `trac_5790-partition.patch`.",
    "created_at": "2009-07-18T15:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5790#issuecomment-45350",
    "user": "mvngu"
}
```

Merged `trac_5790-partition.patch`.
