# Issue 7236: Partitions cleanup (box => cell + indentation fix)

archive/issues_007236.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: partitions cell\n\nAfter a vote on `sage-combinat-devel`, see\n\n```\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/bd6dd9b316236f91\n```\n\nit was decided that in a partition diagramm a square should be called a cell. The following patch implement this choice.\n\nI also take the occasion to fix an indentation problem which prevents some doc to be correctly typeset.\n\nCheers,\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/7236\n\n",
    "created_at": "2009-10-17T20:38:04Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Partitions cleanup (box => cell + indentation fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7236",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: partitions cell

After a vote on `sage-combinat-devel`, see

```
http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/bd6dd9b316236f91
```

it was decided that in a partition diagramm a square should be called a cell. The following patch implement this choice.

I also take the occasion to fix an indentation problem which prevents some doc to be correctly typeset.

Cheers,

Florent

Issue created by migration from https://trac.sagemath.org/ticket/7236





---

archive/issue_comments_059911.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-17T20:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59911",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059912.json:
```json
{
    "body": "Changing keywords from \"partitions cell\" to \"partitions cell, leg, arm, hook\".",
    "created_at": "2009-10-18T07:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59912",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "partitions cell" to "partitions cell, leg, arm, hook".



---

archive/issue_comments_059913.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-18T07:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59913",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059914.json:
```json
{
    "body": "I just reviewed your patch. Positive review up to the following points:\n\n- Specify in the definition of leg that this is in English notation\n- Add deprecation hooks for all renamed methods",
    "created_at": "2009-10-18T07:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59914",
    "user": "https://github.com/nthiery"
}
```

I just reviewed your patch. Positive review up to the following points:

- Specify in the definition of leg that this is in English notation
- Add deprecation hooks for all renamed methods



---

archive/issue_comments_059915.json:
```json
{
    "body": "Attachment [trac_7236-partitions_tableaux_cells_cleanup-fh.patch](tarball://root/attachments/some-uuid/ticket7236/trac_7236-partitions_tableaux_cells_cleanup-fh.patch) by @hivert created at 2009-10-18 15:20:37",
    "created_at": "2009-10-18T15:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59915",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7236-partitions_tableaux_cells_cleanup-fh.patch](tarball://root/attachments/some-uuid/ticket7236/trac_7236-partitions_tableaux_cells_cleanup-fh.patch) by @hivert created at 2009-10-18 15:20:37



---

archive/issue_comments_059916.json:
```json
{
    "body": "I just uploaded a new patch with the required backward compatibility hooks and deprecation warnings. It is ready to review. \n\nCheers,\n\nFlorent",
    "created_at": "2009-10-18T15:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59916",
    "user": "https://github.com/hivert"
}
```

I just uploaded a new patch with the required backward compatibility hooks and deprecation warnings. It is ready to review. 

Cheers,

Florent



---

archive/issue_comments_059917.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-18T15:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59917",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059918.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-18T21:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59918",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059919.json:
```json
{
    "body": "Thanks Florent. The test pass with 4.1.1 and a couple other patches applied. Positive review, assuming they pass smoothly on the current 4.2 ???\n\nFlorent: making a quick grep, I noticed that in sf/ns_macdonald.py, the LatticeDiagram uses the same old conventions as Partitions (box, leg, arm, ...). I let you decide if you want to fix this now as part of this ticket, or postpone to a later ticket.",
    "created_at": "2009-10-18T21:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59919",
    "user": "https://github.com/nthiery"
}
```

Thanks Florent. The test pass with 4.1.1 and a couple other patches applied. Positive review, assuming they pass smoothly on the current 4.2 ???

Florent: making a quick grep, I noticed that in sf/ns_macdonald.py, the LatticeDiagram uses the same old conventions as Partitions (box, leg, arm, ...). I let you decide if you want to fix this now as part of this ticket, or postpone to a later ticket.



---

archive/issue_comments_059920.json:
```json
{
    "body": "I think it can be another ticket.  I'm going to write a \"decorator\" to make deprecated aliases easier.  So, we'd just do \"boxes = deprecated_method_alias(cells)\".",
    "created_at": "2009-10-19T05:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59920",
    "user": "https://github.com/mwhansen"
}
```

I think it can be another ticket.  I'm going to write a "decorator" to make deprecated aliases easier.  So, we'd just do "boxes = deprecated_method_alias(cells)".



---

archive/issue_comments_059921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T05:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59921",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017135.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-19T05:49:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7236#event-17135"
}
```



---

archive/issue_comments_059922.json:
```json
{
    "body": "Replying to [comment:6 mhansen]:\n> I think it can be another ticket.\n\nOk. Thanks for merging it!\n\n> I'm going to write a \"decorator\" to make deprecated aliases easier.  So, we'd just do \"boxes = deprecated_method_alias(cells)\".\n\n+1!!!",
    "created_at": "2009-10-19T09:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7236#issuecomment-59922",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:6 mhansen]:
> I think it can be another ticket.

Ok. Thanks for merging it!

> I'm going to write a "decorator" to make deprecated aliases easier.  So, we'd just do "boxes = deprecated_method_alias(cells)".

+1!!!
