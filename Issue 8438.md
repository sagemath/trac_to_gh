# Issue 8438: Construction of a skew partition from its row and column lengths

archive/issues_008438.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  nborie\n\nKeywords: skew partitions\n\n```\nsage: print from_row_and_column_length([3,1,2,2],[2,3,1,1,1]).diagram()\n         ###\n        #\n       ##\n       ##\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8438\n\n",
    "created_at": "2010-03-04T20:42:23Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Construction of a skew partition from its row and column lengths",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8438",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  nborie

Keywords: skew partitions

```
sage: print from_row_and_column_length([3,1,2,2],[2,3,1,1,1]).diagram()
         ###
        #
       ##
       ##
```

Issue created by migration from https://trac.sagemath.org/ticket/8438





---

archive/issue_comments_075623.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-04T20:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75623",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075624.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-05T18:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75624",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075625.json:
```json
{
    "body": "Can you improve that : \n\n```\nsage: S = SkewPartition(([6],[6])) \nsage: S.column_lengths()\n[0, 0, 0, 0, 0, 0]\nsage: S.row_lengths()\n[0]\nsage: from_row_and_column_length([0],[0,0,0,0,0,0]) \n[[6], [6]] #perfect\n\nsage: S = SkewPartition(([1,1,1,1,1,1],[1,1,1,1,1,1]))\nsage: S.column_lengths()\n[0]\nsage: S.row_lengths()\n[0, 0, 0, 0, 0, 0]\nsage: from_row_and_column_length([0,0,0,0,0,0],[0]) \n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n...\n...\nValueError: invalid skew partition\n```",
    "created_at": "2010-03-05T18:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75625",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Can you improve that : 

```
sage: S = SkewPartition(([6],[6])) 
sage: S.column_lengths()
[0, 0, 0, 0, 0, 0]
sage: S.row_lengths()
[0]
sage: from_row_and_column_length([0],[0,0,0,0,0,0]) 
[[6], [6]] #perfect

sage: S = SkewPartition(([1,1,1,1,1,1],[1,1,1,1,1,1]))
sage: S.column_lengths()
[0]
sage: S.row_lengths()
[0, 0, 0, 0, 0, 0]
sage: from_row_and_column_length([0,0,0,0,0,0],[0]) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
...
ValueError: invalid skew partition
```



---

archive/issue_comments_075626.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-05T18:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75626",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075627.json:
```json
{
    "body": "Sorry,\n\nI don't know which behaviour you want for the last example I gave...\n\nI ran : \n\n```\nsage: for i in range(10):\n....:     for S in SkewPartitions(i):\n....:         if S != from_row_and_column_length(S.row_lengths(),S.column_lengths()):\n....:             print S\n....:             \nsage:\n```\nThat works! For the example comming from my last comment... I don't know.\n\nOtherwise, the patch is correct (apply, test and doc.). I am not an expert with Skew Partitions...",
    "created_at": "2010-03-05T18:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75627",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Sorry,

I don't know which behaviour you want for the last example I gave...

I ran : 

```
sage: for i in range(10):
....:     for S in SkewPartitions(i):
....:         if S != from_row_and_column_length(S.row_lengths(),S.column_lengths()):
....:             print S
....:             
sage:
```
That works! For the example comming from my last comment... I don't know.

Otherwise, the patch is correct (apply, test and doc.). I am not an expert with Skew Partitions...



---

archive/issue_comments_075628.json:
```json
{
    "body": "Attachment [trac_8438-skew_partitions_from_rc_lenghts-fh.patch](tarball://root/attachments/some-uuid/ticket8438/trac_8438-skew_partitions_from_rc_lenghts-fh.patch) by @hivert created at 2010-03-10 08:33:41",
    "created_at": "2010-03-10T08:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75628",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8438-skew_partitions_from_rc_lenghts-fh.patch](tarball://root/attachments/some-uuid/ticket8438/trac_8438-skew_partitions_from_rc_lenghts-fh.patch) by @hivert created at 2010-03-10 08:33:41



---

archive/issue_comments_075629.json:
```json
{
    "body": "Replying to [comment:2 nborie]:\n> Can you improve that : \n> \n\n{{{\nsage: S = SkewPartition(([1,1,1,1,1,1],[1,1,1,1,1,1]))\nsage: S.column_lengths()\n[0]\nsage: S.row_lengths()\n[0, 0, 0, 0, 0, 0]\nsage: from_row_and_column_length([0,0,0,0,0,0],[0]) \n\n---\nValueError                                Traceback (most recent call last)\n...\n...\nValueError: invalid skew partition\n}}}\nThe cases with 0 row and columns length are ambiguous (see the example in the doc). I now raise a proper error:\n\n```\nsage: sage: from_row_and_column_length([0,0,0,0,0,0],[0]) \n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n...\nValueError: row and column length must be positive\n```\nI re-uploaded the new patch ! Please review.",
    "created_at": "2010-03-10T08:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75629",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:2 nborie]:
> Can you improve that : 
> 

{{{
sage: S = SkewPartition(([1,1,1,1,1,1],[1,1,1,1,1,1]))
sage: S.column_lengths()
[0]
sage: S.row_lengths()
[0, 0, 0, 0, 0, 0]
sage: from_row_and_column_length([0,0,0,0,0,0],[0]) 

---
ValueError                                Traceback (most recent call last)
...
...
ValueError: invalid skew partition
}}}
The cases with 0 row and columns length are ambiguous (see the example in the doc). I now raise a proper error:

```
sage: sage: from_row_and_column_length([0,0,0,0,0,0],[0]) 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: row and column length must be positive
```
I re-uploaded the new patch ! Please review.



---

archive/issue_comments_075630.json:
```json
{
    "body": "Ok, no more corner case from my point of view....\n\nThe patch apply, the doc is perfect, all test passed. The rst construction with ..warning:: produces a very very nice html output.\n\nPositive review from me.",
    "created_at": "2010-03-10T10:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75630",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Ok, no more corner case from my point of view....

The patch apply, the doc is perfect, all test passed. The rst construction with ..warning:: produces a very very nice html output.

Positive review from me.



---

archive/issue_comments_075631.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-10T10:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75631",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075632.json:
```json
{
    "body": "Merged \"trac_8438-skew_partitions_from_rc_lenghts-fh.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75632",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8438-skew_partitions_from_rc_lenghts-fh.patch" into 4.4.alpha0.



---

archive/issue_comments_075633.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8438#issuecomment-75633",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_020236.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T23:52:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8438",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8438#event-20236"
}
```
