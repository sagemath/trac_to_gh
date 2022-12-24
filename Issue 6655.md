# Issue 6655: Clean up and new feature in partition

archive/issues_006655.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nKeywords: Parition\n\nI add a following new feature in partition:\na method returns a list of boxes in the arm.\nand so more.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6655\n\n",
    "created_at": "2009-07-29T14:25:13Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "Clean up and new feature in partition",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6655",
    "user": "numata"
}
```
Assignee: mhansen

CC:  sage-combinat

Keywords: Parition

I add a following new feature in partition:
a method returns a list of boxes in the arm.
and so more.

Issue created by migration from https://trac.sagemath.org/ticket/6655





---

archive/issue_comments_054625.json:
```json
{
    "body": "Attachment [trac_6655_partition_newfeature-ny.patch](tarball://root/attachments/some-uuid/ticket6655/trac_6655_partition_newfeature-ny.patch) by numata created at 2009-07-29 15:54:35",
    "created_at": "2009-07-29T15:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54625",
    "user": "numata"
}
```

Attachment [trac_6655_partition_newfeature-ny.patch](tarball://root/attachments/some-uuid/ticket6655/trac_6655_partition_newfeature-ny.patch) by numata created at 2009-07-29 15:54:35



---

archive/issue_comments_054626.json:
```json
{
    "body": "Changing assignee from mhansen to numata.",
    "created_at": "2009-07-29T15:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54626",
    "user": "numata"
}
```

Changing assignee from mhansen to numata.



---

archive/issue_comments_054627.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-29T15:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54627",
    "user": "numata"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054628.json:
```json
{
    "body": "Changing keywords from \"Parition\" to \"Partition cells arm legs\".",
    "created_at": "2010-04-22T19:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54628",
    "user": "hivert"
}
```

Changing keywords from "Parition" to "Partition cells arm legs".



---

archive/issue_comments_054629.json:
```json
{
    "body": "Changing assignee from numata to hivert.",
    "created_at": "2010-04-22T19:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54629",
    "user": "hivert"
}
```

Changing assignee from numata to hivert.



---

archive/issue_comments_054630.json:
```json
{
    "body": "Should be ready for review ! Apply only [trac_6655_partition_corner_cells-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-fh.patch)",
    "created_at": "2010-04-22T19:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54630",
    "user": "hivert"
}
```

Should be ready for review ! Apply only [trac_6655_partition_corner_cells-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-fh.patch)



---

archive/issue_comments_054631.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-22T19:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54631",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054632.json:
```json
{
    "body": "I slightly improved the doc and re-uploaded the patch...",
    "created_at": "2010-04-27T17:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54632",
    "user": "hivert"
}
```

I slightly improved the doc and re-uploaded the patch...



---

archive/issue_comments_054633.json:
```json
{
    "body": "I just discovered some failing docttests. Everything should now be ok. Please review",
    "created_at": "2010-05-01T13:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54633",
    "user": "hivert"
}
```

I just discovered some failing docttests. Everything should now be ok. Please review



---

archive/issue_comments_054634.json:
```json
{
    "body": "Hi Florent,\n\nThank you for this patch. Here are a couple of comments:\n\n* Please use consistently \"in English convention\" instead of \"in english notations\",\nsee line 840, 963, 924.\n\n* Would it be possible to lift the methods arm_length, leg_length, hook_length, arm_cells, etc also to SkewPartitions? I recently needed those and it would be convenient to have them directly in Sage.\n\nCheers,\n\nAnne",
    "created_at": "2010-05-01T16:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54634",
    "user": "aschilling"
}
```

Hi Florent,

Thank you for this patch. Here are a couple of comments:

* Please use consistently "in English convention" instead of "in english notations",
see line 840, 963, 924.

* Would it be possible to lift the methods arm_length, leg_length, hook_length, arm_cells, etc also to SkewPartitions? I recently needed those and it would be convenient to have them directly in Sage.

Cheers,

Anne



---

archive/issue_comments_054635.json:
```json
{
    "body": "Attachment [trac_6655_partition_corner_cells-fh.patch](tarball://root/attachments/some-uuid/ticket6655/trac_6655_partition_corner_cells-fh.patch) by hivert created at 2010-05-04 23:20:32",
    "created_at": "2010-05-04T23:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54635",
    "user": "hivert"
}
```

Attachment [trac_6655_partition_corner_cells-fh.patch](tarball://root/attachments/some-uuid/ticket6655/trac_6655_partition_corner_cells-fh.patch) by hivert created at 2010-05-04 23:20:32



---

archive/issue_comments_054636.json:
```json
{
    "body": "> * Please use consistently \"in English convention\" instead of \"in english notations\",\n> see line 840, 963, 924.\n\nFixed...\n\n> * Would it be possible to lift the methods arm_length, leg_length, hook_length, arm_cells, etc also to SkewPartitions? I recently needed those and it would be convenient to have them directly in Sage.\n\nExcept for `cells` which I just added, they are all accessible through `l.outer().arm_length`... So I'm not sure we wan't to link all of those.",
    "created_at": "2010-05-04T23:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54636",
    "user": "hivert"
}
```

> * Please use consistently "in English convention" instead of "in english notations",
> see line 840, 963, 924.

Fixed...

> * Would it be possible to lift the methods arm_length, leg_length, hook_length, arm_cells, etc also to SkewPartitions? I recently needed those and it would be convenient to have them directly in Sage.

Except for `cells` which I just added, they are all accessible through `l.outer().arm_length`... So I'm not sure we wan't to link all of those.



---

archive/issue_comments_054637.json:
```json
{
    "body": "Attachment [trac_6655_partition_corner_cells-review-as.patch](tarball://root/attachments/some-uuid/ticket6655/trac_6655_partition_corner_cells-review-as.patch) by aschilling created at 2010-05-05 23:34:17\n\nI reviewed the patch. It cleans up several features in partitions. In addition it fixes the slide method in skew_tableaux and adds the cell method to skew_partitions as requested. All tests pass. Positive review!\n\nRelease manager, please apply only\ntrac_6655_partition_corner_cells-fh.patch and \ntrac_6655_partition_corner_cells-review-as.patch (in this order).",
    "created_at": "2010-05-05T23:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54637",
    "user": "aschilling"
}
```

Attachment [trac_6655_partition_corner_cells-review-as.patch](tarball://root/attachments/some-uuid/ticket6655/trac_6655_partition_corner_cells-review-as.patch) by aschilling created at 2010-05-05 23:34:17

I reviewed the patch. It cleans up several features in partitions. In addition it fixes the slide method in skew_tableaux and adds the cell method to skew_partitions as requested. All tests pass. Positive review!

Release manager, please apply only
trac_6655_partition_corner_cells-fh.patch and 
trac_6655_partition_corner_cells-review-as.patch (in this order).



---

archive/issue_comments_054638.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-05T23:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54638",
    "user": "aschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054639.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_6655_partition_corner_cells-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-fh.patch)\n2. [trac_6655_partition_corner_cells-review-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-review-as.patch)",
    "created_at": "2010-05-08T21:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54639",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_6655_partition_corner_cells-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-fh.patch)
2. [trac_6655_partition_corner_cells-review-as.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6655/trac_6655_partition_corner_cells-review-as.patch)



---

archive/issue_comments_054640.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6655#issuecomment-54640",
    "user": "mvngu"
}
```

Resolution: fixed
