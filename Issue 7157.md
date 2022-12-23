# Issue 7157: [with patch, needs review] neighbors_out/in instead of predecessor/successor in DiGraph

archive/issues_007157.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  jason rlm nthiery\n\nAs the title says, and following the discussion on Sage-devel :\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/bfeb9b1828a04350/10681dbb1f189b2f\n\nIssue created by migration from https://trac.sagemath.org/ticket/7157\n\n",
    "created_at": "2009-10-08T16:31:05Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] neighbors_out/in instead of predecessor/successor in DiGraph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7157",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  jason rlm nthiery

As the title says, and following the discussion on Sage-devel :
http://groups.google.com/group/sage-devel/browse_thread/thread/bfeb9b1828a04350/10681dbb1f189b2f

Issue created by migration from https://trac.sagemath.org/ticket/7157





---

archive/issue_comments_059293.json:
```json
{
    "body": "On my side, it passes -testall without any (related) failure.",
    "created_at": "2009-10-08T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59293",
    "user": "ncohen"
}
```

On my side, it passes -testall without any (related) failure.



---

archive/issue_comments_059294.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-08T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59294",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059295.json:
```json
{
    "body": "You shouldn't just remove the successor/predecessor terminology. A lot of people (e.g. Chris Godsil) might have to do a lot of work to change all their personal scripts etc. to reflect this change. This patch breaks backwards compatibility.",
    "created_at": "2009-10-08T16:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59295",
    "user": "rlm"
}
```

You shouldn't just remove the successor/predecessor terminology. A lot of people (e.g. Chris Godsil) might have to do a lot of work to change all their personal scripts etc. to reflect this change. This patch breaks backwards compatibility.



---

archive/issue_comments_059296.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-08T16:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59296",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059297.json:
```json
{
    "body": "Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?",
    "created_at": "2009-10-08T16:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59297",
    "user": "ncohen"
}
```

Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?



---

archive/issue_comments_059298.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?\n\nI think aliases would be okay, but people have mentioned before that aliases are bad. Please bring this up on the sage-devel thread, and do what the consensus is there.",
    "created_at": "2009-10-08T16:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59298",
    "user": "rlm"
}
```

Replying to [comment:3 ncohen]:
> Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?

I think aliases would be okay, but people have mentioned before that aliases are bad. Please bring this up on the sage-devel thread, and do what the consensus is there.



---

archive/issue_comments_059299.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-09T12:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59299",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059300.json:
```json
{
    "body": "Should be better now :-)\n\nThe new functions are defined, old functions are marked \"Deprecated\".",
    "created_at": "2009-10-09T12:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59300",
    "user": "ncohen"
}
```

Should be better now :-)

The new functions are defined, old functions are marked "Deprecated".



---

archive/issue_comments_059301.json:
```json
{
    "body": "Hi there,\n\nJust a short remark: If you wan't to shorten the patch: see #7515.",
    "created_at": "2009-11-22T19:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59301",
    "user": "hivert"
}
```

Hi there,

Just a short remark: If you wan't to shorten the patch: see #7515.



---

archive/issue_comments_059302.json:
```json
{
    "body": "Thank you very much !!! :-)",
    "created_at": "2009-11-22T19:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59302",
    "user": "ncohen"
}
```

Thank you very much !!! :-)



---

archive/issue_comments_059303.json:
```json
{
    "body": "Updated !",
    "created_at": "2009-11-24T15:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59303",
    "user": "ncohen"
}
```

Updated !



---

archive/issue_comments_059304.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:8 ncohen]:\n> Updated !\n\nIt was decided on sage-devel only to put the version and not the date in the message of deprecation aliases. I just uploaded a patch witch does that. Please review. Aside from that\n\nYou have a Positive review on trac_7157.patch. You can change the status as soon as you had an eye on my trivial review patch. \n\nCheers,\n\nFlorent\n\nBy the way a review on #7515 is welcome ;-)",
    "created_at": "2009-11-30T10:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59304",
    "user": "hivert"
}
```

Attachment

Replying to [comment:8 ncohen]:
> Updated !

It was decided on sage-devel only to put the version and not the date in the message of deprecation aliases. I just uploaded a patch witch does that. Please review. Aside from that

You have a Positive review on trac_7157.patch. You can change the status as soon as you had an eye on my trivial review patch. 

Cheers,

Florent

By the way a review on #7515 is welcome ;-)



---

archive/issue_comments_059305.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-30T11:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59305",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059306.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T04:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59306",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059307.json:
```json
{
    "body": "Attachment\n\nI've added a new trac_7157_review.patch patch with two function calls that were missed.",
    "created_at": "2009-12-01T04:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59307",
    "user": "mhansen"
}
```

Attachment

I've added a new trac_7157_review.patch patch with two function calls that were missed.



---

archive/issue_comments_059308.json:
```json
{
    "body": "Thank you ! :-)",
    "created_at": "2009-12-01T05:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59308",
    "user": "ncohen"
}
```

Thank you ! :-)
