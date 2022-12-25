# Issue 6123: [with patch, positive review] expose partition refinement functions to Python

archive/issues_006123.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  sage-combinat\n\nThe idea is that it would be nice to use the partition refinement functions for experimentation without having to recompile a lot of times.\n\nIt would be very good to get this into Sage-4.0, since this will allow for patches on the sage-combinat server which don't require excessive compilation time when pushing/popping.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6123\n\n",
    "closed_at": "2009-06-14T22:45:19Z",
    "created_at": "2009-05-24T07:41:34Z",
    "labels": [
        "component: group theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, positive review] expose partition refinement functions to Python",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6123",
    "user": "https://github.com/rlmill"
}
```
Assignee: joyner

CC:  sage-combinat

The idea is that it would be nice to use the partition refinement functions for experimentation without having to recompile a lot of times.

It would be very good to get this into Sage-4.0, since this will allow for patches on the sage-combinat server which don't require excessive compilation time when pushing/popping.

Issue created by migration from https://trac.sagemath.org/ticket/6123





---

archive/issue_comments_048831.json:
```json
{
    "body": "Attachment [trac_6123-python_partn_ref.patch](tarball://root/attachments/some-uuid/ticket6123/trac_6123-python_partn_ref.patch) by @rlmill created at 2009-05-24 07:42:14",
    "created_at": "2009-05-24T07:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48831",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_6123-python_partn_ref.patch](tarball://root/attachments/some-uuid/ticket6123/trac_6123-python_partn_ref.patch) by @rlmill created at 2009-05-24 07:42:14



---

archive/issue_comments_048832.json:
```json
{
    "body": "better for 4.0.1.  Get this reviewed!",
    "created_at": "2009-05-28T07:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48832",
    "user": "https://github.com/williamstein"
}
```

better for 4.0.1.  Get this reviewed!



---

archive/issue_events_014418.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-05-28T07:17:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "milestone": "sage-4.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6123#event-14418"
}
```



---

archive/issue_comments_048833.json:
```json
{
    "body": "`nthiery` promised a review in time for 4.0. I guess he can move it back over when he is done, if there is still time.",
    "created_at": "2009-05-28T08:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48833",
    "user": "https://github.com/rlmill"
}
```

`nthiery` promised a review in time for 4.0. I guess he can move it back over when he is done, if there is still time.



---

archive/issue_comments_048834.json:
```json
{
    "body": "craigcitro and ncalexan want this to go in 4.0.2.alpha0, so we're going to merge it.  The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?",
    "created_at": "2009-06-14T22:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48834",
    "user": "https://github.com/ncalexan"
}
```

craigcitro and ncalexan want this to go in 4.0.2.alpha0, so we're going to merge it.  The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?



---

archive/issue_comments_048835.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T22:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48835",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_014419.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-14T22:45:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6123#event-14419"
}
```



---

archive/issue_comments_048836.json:
```json
{
    "body": "Replying to [comment:3 ncalexan]:\n> ...The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?\n\n\nCan you be a *lot* more specific?",
    "created_at": "2009-06-16T08:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48836",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:3 ncalexan]:
> ...The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?


Can you be a *lot* more specific?
