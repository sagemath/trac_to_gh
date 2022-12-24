# Issue 6123: [with patch, needs review] expose partition refinement functions to Python

archive/issues_006123.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  sage-combinat\n\nThe idea is that it would be nice to use the partition refinement functions for experimentation without having to recompile a lot of times.\n\nIt would be very good to get this into Sage-4.0, since this will allow for patches on the sage-combinat server which don't require excessive compilation time when pushing/popping.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6123\n\n",
    "created_at": "2009-05-24T07:41:34Z",
    "labels": [
        "group theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, needs review] expose partition refinement functions to Python",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6123",
    "user": "@rlmill"
}
```
Assignee: joyner

CC:  sage-combinat

The idea is that it would be nice to use the partition refinement functions for experimentation without having to recompile a lot of times.

It would be very good to get this into Sage-4.0, since this will allow for patches on the sage-combinat server which don't require excessive compilation time when pushing/popping.

Issue created by migration from https://trac.sagemath.org/ticket/6123





---

archive/issue_comments_048926.json:
```json
{
    "body": "Attachment [trac_6123-python_partn_ref.patch](tarball://root/attachments/some-uuid/ticket6123/trac_6123-python_partn_ref.patch) by @rlmill created at 2009-05-24 07:42:14",
    "created_at": "2009-05-24T07:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48926",
    "user": "@rlmill"
}
```

Attachment [trac_6123-python_partn_ref.patch](tarball://root/attachments/some-uuid/ticket6123/trac_6123-python_partn_ref.patch) by @rlmill created at 2009-05-24 07:42:14



---

archive/issue_comments_048927.json:
```json
{
    "body": "better for 4.0.1.  Get this reviewed!",
    "created_at": "2009-05-28T07:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48927",
    "user": "@williamstein"
}
```

better for 4.0.1.  Get this reviewed!



---

archive/issue_comments_048928.json:
```json
{
    "body": "`nthiery` promised a review in time for 4.0. I guess he can move it back over when he is done, if there is still time.",
    "created_at": "2009-05-28T08:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48928",
    "user": "@rlmill"
}
```

`nthiery` promised a review in time for 4.0. I guess he can move it back over when he is done, if there is still time.



---

archive/issue_comments_048929.json:
```json
{
    "body": "craigcitro and ncalexan want this to go in 4.0.2.alpha0, so we're going to merge it.  The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?",
    "created_at": "2009-06-14T22:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48929",
    "user": "@ncalexan"
}
```

craigcitro and ncalexan want this to go in 4.0.2.alpha0, so we're going to merge it.  The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?



---

archive/issue_comments_048930.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T22:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48930",
    "user": "@ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_048931.json:
```json
{
    "body": "Replying to [comment:3 ncalexan]:\n> ...The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?\n\nCan you be a *lot* more specific?",
    "created_at": "2009-06-16T08:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6123#issuecomment-48931",
    "user": "@rlmill"
}
```

Replying to [comment:3 ncalexan]:
> ...The doctests look good but not great: can we get some more examples that verify the Cython implementations, and some explanations of the existing examples?

Can you be a *lot* more specific?
