# Issue 1075: [with patch] sync'ing hashes for fraction fields and rings

archive/issues_001075.json:
```json
{
    "body": "Assignee: somebody\n\nThe attached patch provides a custom __hash__ function for fraction field elements so that fractions with a denominator of 1 hash the same as the hash of the numerator as an element in the ring.  A charming side effect is that __hash__ is *much* faster now for fraction field elements of MPoly's over QQ.\n\nThis fixes some bugs (IMO) in the subs method of ParentWithGens when passing a dictionary.\n\nI don't think there is any problems with hash's changing from one version to the next -- I guess there might be something I'm missing here.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1075\n\n",
    "created_at": "2007-11-03T12:42:09Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch] sync'ing hashes for fraction fields and rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1075",
    "user": "jbmohler"
}
```
Assignee: somebody

The attached patch provides a custom __hash__ function for fraction field elements so that fractions with a denominator of 1 hash the same as the hash of the numerator as an element in the ring.  A charming side effect is that __hash__ is *much* faster now for fraction field elements of MPoly's over QQ.

This fixes some bugs (IMO) in the subs method of ParentWithGens when passing a dictionary.

I don't think there is any problems with hash's changing from one version to the next -- I guess there might be something I'm missing here.

Issue created by migration from https://trac.sagemath.org/ticket/1075





---

archive/issue_comments_006506.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-05T01:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1075#issuecomment-6506",
    "user": "jbmohler"
}
```

Attachment



---

archive/issue_comments_006507.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-11-15T22:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1075#issuecomment-6507",
    "user": "jbmohler"
}
```

Resolution: invalid



---

archive/issue_comments_006508.json:
```json
{
    "body": "I'm closing this because the patch I'm going to attached to #1181 is much better and much broader.",
    "created_at": "2007-11-15T22:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1075#issuecomment-6508",
    "user": "jbmohler"
}
```

I'm closing this because the patch I'm going to attached to #1181 is much better and much broader.
