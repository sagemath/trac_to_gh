# Issue 8856: Reinstate cached one in algebra_with_basis

archive/issues_008856.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  sage-combinat\n\nKeywords: cached one_basis\n\nFrom `algebra_with_basis.py`:\n\n```\n#@cached_method   # todo: reinstate once #5843 is fixed\ndef one_from_one_basis(self):\n    \"\"\"\n    Returns the one of the algebra, as per\n            ``Monoids.ParentMethods.one``\n    [...]\n    \"\"\"\n    return self.monomial(self.one_basis()) #.\n```\n\nSo I'm removing the comment since #5843 is fixed.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8856\n\n",
    "created_at": "2010-05-03T14:39:53Z",
    "labels": [
        "categories",
        "major",
        "enhancement"
    ],
    "title": "Reinstate cached one in algebra_with_basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8856",
    "user": "hivert"
}
```
Assignee: hivert

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

archive/issue_comments_081384.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-03T14:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81384",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_081385.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-03T14:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81385",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081386.json:
```json
{
    "body": "Ready for review...",
    "created_at": "2010-05-03T14:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81386",
    "user": "hivert"
}
```

Ready for review...



---

archive/issue_comments_081387.json:
```json
{
    "body": "I had ask for this change, and the extra tests are good. Thanks for handling this!\n\nPlease double check that all test pass (they should), and then you can put a positive review on my behalf.",
    "created_at": "2010-05-03T15:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81387",
    "user": "nthiery"
}
```

I had ask for this change, and the extra tests are good. Thanks for handling this!

Please double check that all test pass (they should), and then you can put a positive review on my behalf.



---

archive/issue_comments_081388.json:
```json
{
    "body": "I got a all test on massena (upto usual synchro problem which I rechecked...)...",
    "created_at": "2010-05-03T15:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81388",
    "user": "hivert"
}
```

I got a all test on massena (upto usual synchro problem which I rechecked...)...



---

archive/issue_comments_081389.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-03T15:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81389",
    "user": "hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081390.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:37:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8856#issuecomment-81390",
    "user": "mvngu"
}
```

Resolution: fixed
