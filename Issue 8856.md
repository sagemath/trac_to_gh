# Issue 8856: Reinstate cached one in algebra_with_basis

archive/issues_008856.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: cached one_basis\n\nFrom `algebra_with_basis.py`:\n\n```\n#@cached_method   # todo: reinstate once #5843 is fixed\ndef one_from_one_basis(self):\n    \"\"\"\n    Returns the one of the algebra, as per\n            ``Monoids.ParentMethods.one``\n    [...]\n    \"\"\"\n    return self.monomial(self.one_basis()) #.\n```\n\nSo I'm removing the comment since #5843 is fixed.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8856\n\n",
    "created_at": "2010-05-03T14:39:53Z",
    "labels": [
        "component: categories"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Reinstate cached one in algebra_with_basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8856",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  sage-combinat

Keywords: cached one_basis

From `algebra_with_basis.py`:

```
#@cached_method   # todo: reinstate once #5843 is fixed
def one_from_one_basis(self):
    """
    Returns the one of the algebra, as per
            ``Monoids.ParentMethods.one``
    [...]
    """
    return self.monomial(self.one_basis()) #.
```

So I'm removing the comment since #5843 is fixed.


Issue created by migration from https://trac.sagemath.org/ticket/8856





---

archive/issue_comments_081251.json:
```json
{
    "body": "Attachment [trac_8856-cached_one_basis-fh.patch](tarball://root/attachments/some-uuid/ticket8856/trac_8856-cached_one_basis-fh.patch) by @hivert created at 2010-05-03 14:54:33",
    "created_at": "2010-05-03T14:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81251",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8856-cached_one_basis-fh.patch](tarball://root/attachments/some-uuid/ticket8856/trac_8856-cached_one_basis-fh.patch) by @hivert created at 2010-05-03 14:54:33



---

archive/issue_comments_081252.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-03T14:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81252",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081253.json:
```json
{
    "body": "Ready for review...",
    "created_at": "2010-05-03T14:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81253",
    "user": "https://github.com/hivert"
}
```

Ready for review...



---

archive/issue_comments_081254.json:
```json
{
    "body": "I had ask for this change, and the extra tests are good. Thanks for handling this!\n\nPlease double check that all test pass (they should), and then you can put a positive review on my behalf.",
    "created_at": "2010-05-03T15:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81254",
    "user": "https://github.com/nthiery"
}
```

I had ask for this change, and the extra tests are good. Thanks for handling this!

Please double check that all test pass (they should), and then you can put a positive review on my behalf.



---

archive/issue_comments_081255.json:
```json
{
    "body": "I got a all test on massena (upto usual synchro problem which I rechecked...)...",
    "created_at": "2010-05-03T15:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81255",
    "user": "https://github.com/hivert"
}
```

I got a all test on massena (upto usual synchro problem which I rechecked...)...



---

archive/issue_comments_081256.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-03T15:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81256",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081257.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81257",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
