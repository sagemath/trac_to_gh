# Issue 6561: Trivial bug with cartesian product of an empty list of iterators

archive/issues_006561.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @williamstein\n\nThe function cartesian_product_iterator (which takes a list of iterators as input) gets the wrong answer when given an empty list. It returns an empty list; but the cartesian product of an empty list of iterators should be *the list containing the empty tuple*. \n\nThe current behaviour means as a consequence that listing the elements of the zero finitely-presented module returns an empty list, rather than [0] which is clearly the right answer.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6561\n\n",
    "created_at": "2009-07-19T18:11:06Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Trivial bug with cartesian product of an empty list of iterators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6561",
    "user": "@loefflerd"
}
```
Assignee: cwitty

CC:  @williamstein

The function cartesian_product_iterator (which takes a list of iterators as input) gets the wrong answer when given an empty list. It returns an empty list; but the cartesian product of an empty list of iterators should be *the list containing the empty tuple*. 

The current behaviour means as a consequence that listing the elements of the zero finitely-presented module returns an empty list, rather than [0] which is clearly the right answer.



Issue created by migration from https://trac.sagemath.org/ticket/6561





---

archive/issue_comments_053513.json:
```json
{
    "body": "Attachment [trac_6561-empty_cartesian_product.patch](tarball://root/attachments/some-uuid/ticket6561/trac_6561-empty_cartesian_product.patch) by @loefflerd created at 2009-07-20 11:46:54",
    "created_at": "2009-07-20T11:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6561#issuecomment-53513",
    "user": "@loefflerd"
}
```

Attachment [trac_6561-empty_cartesian_product.patch](tarball://root/attachments/some-uuid/ticket6561/trac_6561-empty_cartesian_product.patch) by @loefflerd created at 2009-07-20 11:46:54



---

archive/issue_comments_053514.json:
```json
{
    "body": "Here's a patch. This fixes the bug, and removes some special-case code in combinat/words and abelian_groups that was there to work around the previous wrong behaviour.\n\nWilliam: I think I mentioned this to you in Barcelona -- any chance you could review it, or suggest someone else who could?",
    "created_at": "2009-07-20T11:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6561#issuecomment-53514",
    "user": "@loefflerd"
}
```

Here's a patch. This fixes the bug, and removes some special-case code in combinat/words and abelian_groups that was there to work around the previous wrong behaviour.

William: I think I mentioned this to you in Barcelona -- any chance you could review it, or suggest someone else who could?



---

archive/issue_comments_053515.json:
```json
{
    "body": "David, I am getting errors when I try to apply your patch to sage-4.1.1.  Can you try to rebase it?",
    "created_at": "2009-08-19T07:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6561#issuecomment-53515",
    "user": "@aghitza"
}
```

David, I am getting errors when I try to apply your patch to sage-4.1.1.  Can you try to rebase it?



---

archive/issue_comments_053516.json:
```json
{
    "body": "rebased to 4.1.1",
    "created_at": "2009-08-19T10:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6561#issuecomment-53516",
    "user": "@loefflerd"
}
```

rebased to 4.1.1



---

archive/issue_comments_053517.json:
```json
{
    "body": "Attachment [trac_6561-empty_cartesian_product-rebased.patch](tarball://root/attachments/some-uuid/ticket6561/trac_6561-empty_cartesian_product-rebased.patch) by @loefflerd created at 2009-08-19 10:22:11\n\nHere is a new rebased patch; I have checked it passes doctests in 4.1.1.",
    "created_at": "2009-08-19T10:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6561#issuecomment-53517",
    "user": "@loefflerd"
}
```

Attachment [trac_6561-empty_cartesian_product-rebased.patch](tarball://root/attachments/some-uuid/ticket6561/trac_6561-empty_cartesian_product-rebased.patch) by @loefflerd created at 2009-08-19 10:22:11

Here is a new rebased patch; I have checked it passes doctests in 4.1.1.



---

archive/issue_comments_053518.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-08-19T11:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6561#issuecomment-53518",
    "user": "@aghitza"
}
```

Looks good.



---

archive/issue_comments_053519.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-24T05:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6561#issuecomment-53519",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053520.json:
```json
{
    "body": "Merged `trac_6561-empty_cartesian_product-rebased.patch`.",
    "created_at": "2009-08-24T05:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6561#issuecomment-53520",
    "user": "mvngu"
}
```

Merged `trac_6561-empty_cartesian_product-rebased.patch`.
