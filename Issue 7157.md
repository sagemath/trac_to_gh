# Issue 7157: [with patch, needs review] neighbors_out/in instead of predecessor/successor in DiGraph

archive/issues_007157.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @jasongrout @rlmill @nthiery\n\nAs the title says, and following the discussion on Sage-devel :\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/bfeb9b1828a04350/10681dbb1f189b2f\n\nIssue created by migration from https://trac.sagemath.org/ticket/7157\n\n",
    "created_at": "2009-10-08T16:31:05Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review] neighbors_out/in instead of predecessor/successor in DiGraph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7157",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  @jasongrout @rlmill @nthiery

As the title says, and following the discussion on Sage-devel :
http://groups.google.com/group/sage-devel/browse_thread/thread/bfeb9b1828a04350/10681dbb1f189b2f

Issue created by migration from https://trac.sagemath.org/ticket/7157





---

archive/issue_comments_059181.json:
```json
{
    "body": "On my side, it passes -testall without any (related) failure.",
    "created_at": "2009-10-08T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59181",
    "user": "https://github.com/nathanncohen"
}
```

On my side, it passes -testall without any (related) failure.



---

archive/issue_comments_059182.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-08T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59182",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059183.json:
```json
{
    "body": "You shouldn't just remove the successor/predecessor terminology. A lot of people (e.g. Chris Godsil) might have to do a lot of work to change all their personal scripts etc. to reflect this change. This patch breaks backwards compatibility.",
    "created_at": "2009-10-08T16:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59183",
    "user": "https://github.com/rlmill"
}
```

You shouldn't just remove the successor/predecessor terminology. A lot of people (e.g. Chris Godsil) might have to do a lot of work to change all their personal scripts etc. to reflect this change. This patch breaks backwards compatibility.



---

archive/issue_comments_059184.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-08T16:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59184",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059185.json:
```json
{
    "body": "Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?",
    "created_at": "2009-10-08T16:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59185",
    "user": "https://github.com/nathanncohen"
}
```

Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?



---

archive/issue_comments_059186.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?\n\nI think aliases would be okay, but people have mentioned before that aliases are bad. Please bring this up on the sage-devel thread, and do what the consensus is there.",
    "created_at": "2009-10-08T16:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59186",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:3 ncohen]:
> Should I just add aliases and let the old functions exist ? Should we keep two copies of the same functions ?

I think aliases would be okay, but people have mentioned before that aliases are bad. Please bring this up on the sage-devel thread, and do what the consensus is there.



---

archive/issue_comments_059187.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-09T12:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59187",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059188.json:
```json
{
    "body": "Should be better now :-)\n\nThe new functions are defined, old functions are marked \"Deprecated\".",
    "created_at": "2009-10-09T12:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59188",
    "user": "https://github.com/nathanncohen"
}
```

Should be better now :-)

The new functions are defined, old functions are marked "Deprecated".



---

archive/issue_comments_059189.json:
```json
{
    "body": "Hi there,\n\nJust a short remark: If you wan't to shorten the patch: see #7515.",
    "created_at": "2009-11-22T19:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59189",
    "user": "https://github.com/hivert"
}
```

Hi there,

Just a short remark: If you wan't to shorten the patch: see #7515.



---

archive/issue_comments_059190.json:
```json
{
    "body": "Thank you very much !!! :-)",
    "created_at": "2009-11-22T19:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59190",
    "user": "https://github.com/nathanncohen"
}
```

Thank you very much !!! :-)



---

archive/issue_comments_059191.json:
```json
{
    "body": "Updated !",
    "created_at": "2009-11-24T15:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59191",
    "user": "https://github.com/nathanncohen"
}
```

Updated !



---

archive/issue_comments_059192.json:
```json
{
    "body": "Attachment [trac_7157.patch](tarball://root/attachments/some-uuid/ticket7157/trac_7157.patch) by @hivert created at 2009-11-30 10:48:39\n\nReplying to [comment:8 ncohen]:\n> Updated !\n\nIt was decided on sage-devel only to put the version and not the date in the message of deprecation aliases. I just uploaded a patch witch does that. Please review. Aside from that\n\nYou have a Positive review on trac_7157.patch. You can change the status as soon as you had an eye on my trivial review patch. \n\nCheers,\n\nFlorent\n\nBy the way a review on #7515 is welcome ;-)",
    "created_at": "2009-11-30T10:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59192",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7157.patch](tarball://root/attachments/some-uuid/ticket7157/trac_7157.patch) by @hivert created at 2009-11-30 10:48:39

Replying to [comment:8 ncohen]:
> Updated !

It was decided on sage-devel only to put the version and not the date in the message of deprecation aliases. I just uploaded a patch witch does that. Please review. Aside from that

You have a Positive review on trac_7157.patch. You can change the status as soon as you had an eye on my trivial review patch. 

Cheers,

Florent

By the way a review on #7515 is welcome ;-)



---

archive/issue_comments_059193.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-30T11:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59193",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007377.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-01T04:37:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7157#event-7377"
}
```



---

archive/issue_comments_059194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T04:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59194",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059195.json:
```json
{
    "body": "Attachment [trac_7157_review.patch](tarball://root/attachments/some-uuid/ticket7157/trac_7157_review.patch) by @mwhansen created at 2009-12-01 04:37:12\n\nI've added a new trac_7157_review.patch patch with two function calls that were missed.",
    "created_at": "2009-12-01T04:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59195",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7157_review.patch](tarball://root/attachments/some-uuid/ticket7157/trac_7157_review.patch) by @mwhansen created at 2009-12-01 04:37:12

I've added a new trac_7157_review.patch patch with two function calls that were missed.



---

archive/issue_comments_059196.json:
```json
{
    "body": "Thank you ! :-)",
    "created_at": "2009-12-01T05:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7157#issuecomment-59196",
    "user": "https://github.com/nathanncohen"
}
```

Thank you ! :-)
