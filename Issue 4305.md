# Issue 4305: [with patch, needs review] move finite fields into their own directory

archive/issues_004305.json:
```json
{
    "body": "Assignee: tbd\n\nThis is in anticipation of much re-factoring and refinement. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4305\n\n",
    "created_at": "2008-10-15T20:50:56Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] move finite fields into their own directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4305",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

This is in anticipation of much re-factoring and refinement. 

Issue created by migration from https://trac.sagemath.org/ticket/4305





---

archive/issue_comments_031436.json:
```json
{
    "body": "Attachment [4305-move-finite-field.patch](tarball://root/attachments/some-uuid/ticket4305/4305-move-finite-field.patch) by @robertwb created at 2008-10-15 20:52:02",
    "created_at": "2008-10-15T20:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31436",
    "user": "https://github.com/robertwb"
}
```

Attachment [4305-move-finite-field.patch](tarball://root/attachments/some-uuid/ticket4305/4305-move-finite-field.patch) by @robertwb created at 2008-10-15 20:52:02



---

archive/issue_comments_031437.json:
```json
{
    "body": "apply to docs repo",
    "created_at": "2008-10-15T21:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31437",
    "user": "https://github.com/robertwb"
}
```

apply to docs repo



---

archive/issue_comments_031438.json:
```json
{
    "body": "Attachment [4305-ff-docs.patch](tarball://root/attachments/some-uuid/ticket4305/4305-ff-docs.patch) by mabshoff created at 2008-10-15 21:05:44\n\nLooks good to me - damn the torpedoes :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-15T21:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [4305-ff-docs.patch](tarball://root/attachments/some-uuid/ticket4305/4305-ff-docs.patch) by mabshoff created at 2008-10-15 21:05:44

Looks good to me - damn the torpedoes :)

Cheers,

Michael



---

archive/issue_events_009716.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-16T09:30:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4305#event-9716"
}
```



---

archive/issue_comments_031439.json:
```json
{
    "body": "Due to trouble when building the tree with the patch applied on sage.math, i.e. finite_field_givaro not being found, this patch unfortunately needs work :(\n\nI will attach a reviewer patch shortly once I have proper net again.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-16T09:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31439",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Due to trouble when building the tree with the patch applied on sage.math, i.e. finite_field_givaro not being found, this patch unfortunately needs work :(

I will attach a reviewer patch shortly once I have proper net again.

Cheers,

Michael



---

archive/issue_comments_031440.json:
```json
{
    "body": "Attachment [trac_4305_review.patch](tarball://root/attachments/some-uuid/ticket4305/trac_4305_review.patch) by mabshoff created at 2008-10-16 10:19:27",
    "created_at": "2008-10-16T10:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31440",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4305_review.patch](tarball://root/attachments/some-uuid/ticket4305/trac_4305_review.patch) by mabshoff created at 2008-10-16 10:19:27



---

archive/issue_comments_031441.json:
```json
{
    "body": "Robert,\n\nis anything going on here? I am not sure how much happened to the finite fields since SD 10, but that patch here certainly has gone stale. Should you plan to work on this in the short term please ping me so we can coordinate the big move. Otherwise we should delete the patches and wait until someone tackles this again.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T09:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31441",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Robert,

is anything going on here? I am not sure how much happened to the finite fields since SD 10, but that patch here certainly has gone stale. Should you plan to work on this in the short term please ping me so we can coordinate the big move. Otherwise we should delete the patches and wait until someone tackles this again.

Cheers,

Michael



---

archive/issue_comments_031442.json:
```json
{
    "body": "I'm hoping to have a little time to look into this over the break. Don't delete the patches just yet.",
    "created_at": "2008-12-07T09:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31442",
    "user": "https://github.com/robertwb"
}
```

I'm hoping to have a little time to look into this over the break. Don't delete the patches just yet.



---

archive/issue_events_009717.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2008-12-07T09:41:47Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4305#event-9717"
}
```



---

archive/issue_events_009718.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2008-12-07T09:41:47Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4305#event-9718"
}
```



---

archive/issue_comments_031443.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> I'm hoping to have a little time to look into this over the break. Don't delete the patches just yet. \n\n\nOk, I just think that a lot of this patch needs to be rebased, so it might be a good idea to start over, but we will see. One aspect that puzzles me to this day is that we never got it to work on any other system but your own.\n\nOne issue that likely will need addressing is pickling issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-07T09:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 robertwb]:
> I'm hoping to have a little time to look into this over the break. Don't delete the patches just yet. 


Ok, I just think that a lot of this patch needs to be rebased, so it might be a good idea to start over, but we will see. One aspect that puzzles me to this day is that we never got it to work on any other system but your own.

One issue that likely will need addressing is pickling issues.

Cheers,

Michael



---

archive/issue_comments_031444.json:
```json
{
    "body": "Should be closed because of #8218 I guess.",
    "created_at": "2010-02-09T14:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31444",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Should be closed because of #8218 I guess.



---

archive/issue_comments_031445.json:
```json
{
    "body": "I concur. I'm setting this to \"positive review\" to bring it to the attention of the release manager who has the authority to close it.\n\n*** Please close this ticket without applying any of the patches! ***",
    "created_at": "2010-06-29T08:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31445",
    "user": "https://github.com/loefflerd"
}
```

I concur. I'm setting this to "positive review" to bring it to the attention of the release manager who has the authority to close it.

*** Please close this ticket without applying any of the patches! ***



---

archive/issue_comments_031446.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-29T08:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31446",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_031447.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T08:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31447",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031448.json:
```json
{
    "body": "I'm resolving this ticket as a \"duplicate.\"",
    "created_at": "2010-07-20T09:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31448",
    "user": "https://github.com/qed777"
}
```

I'm resolving this ticket as a "duplicate."



---

archive/issue_events_009719.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T09:23:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4305#event-9719"
}
```



---

archive/issue_events_009720.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T09:23:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4305#event-9720"
}
```



---

archive/issue_comments_031449.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-07-20T09:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4305#issuecomment-31449",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate



---

archive/issue_events_009721.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T09:23:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4305",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4305#event-9721"
}
```
