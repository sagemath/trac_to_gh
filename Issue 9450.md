# Issue 9450: Implement a factor() function for NumberFieldElement

archive/issues_009450.json:
```json
{
    "body": "Assignee: davidloeffler\n\nThe attached patch implements a factor() function for number field elements.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9450\n\n",
    "created_at": "2010-07-07T21:06:36Z",
    "labels": [
        "number fields",
        "major",
        "enhancement"
    ],
    "title": "Implement a factor() function for NumberFieldElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9450",
    "user": "jdemeyer"
}
```
Assignee: davidloeffler

The attached patch implements a factor() function for number field elements.

Issue created by migration from https://trac.sagemath.org/ticket/9450





---

archive/issue_comments_090568.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-07T21:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90568",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_090569.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-07T21:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90569",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090570.json:
```json
{
    "body": "Attachment\n\nApply after previous patch",
    "created_at": "2010-07-08T12:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90570",
    "user": "cremona"
}
```

Attachment

Apply after previous patch



---

archive/issue_comments_090571.json:
```json
{
    "body": "The patch applies and works fine.  I have changed the docstring a little, added a test for factoring 0 and simplified the code in a couple of places.  I also added an example in sage/rings/arith.py since the generic factor() function now works on number field elements!\n\nSince I changed quite a lot, I have left this as \"needs review\".",
    "created_at": "2010-07-08T12:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90571",
    "user": "cremona"
}
```

The patch applies and works fine.  I have changed the docstring a little, added a test for factoring 0 and simplified the code in a couple of places.  I also added an example in sage/rings/arith.py since the generic factor() function now works on number field elements!

Since I changed quite a lot, I have left this as "needs review".



---

archive/issue_comments_090572.json:
```json
{
    "body": "John's changes look good to me.",
    "created_at": "2010-07-11T01:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90572",
    "user": "mhansen"
}
```

John's changes look good to me.



---

archive/issue_comments_090573.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-11T01:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90573",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90574",
    "user": "mpatel"
}
```

Resolution: fixed
