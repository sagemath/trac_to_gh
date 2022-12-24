# Issue 9566: [with patch, needs review] Allow sage.libs.mpmath.call(..., parent=something)

archive/issues_009566.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @burcin\n\nThis can simplify code that needs to call mpmath in some places.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9566\n\n",
    "created_at": "2010-07-21T17:49:51Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "[with patch, needs review] Allow sage.libs.mpmath.call(..., parent=something)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9566",
    "user": "@fredrik-johansson"
}
```
Assignee: @aghitza

CC:  @burcin

This can simplify code that needs to call mpmath in some places.

Issue created by migration from https://trac.sagemath.org/ticket/9566





---

archive/issue_comments_092346.json:
```json
{
    "body": "Attachment [mpmath_call.patch](tarball://root/attachments/some-uuid/ticket9566/mpmath_call.patch) by @haraldschilly created at 2010-07-21 21:17:01\n\ndoes it make sense to also test for parent RDF ?",
    "created_at": "2010-07-21T21:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92346",
    "user": "@haraldschilly"
}
```

Attachment [mpmath_call.patch](tarball://root/attachments/some-uuid/ticket9566/mpmath_call.patch) by @haraldschilly created at 2010-07-21 21:17:01

does it make sense to also test for parent RDF ?



---

archive/issue_comments_092347.json:
```json
{
    "body": "Attachment [mpmath_call_reviewer.patch](tarball://root/attachments/some-uuid/ticket9566/mpmath_call_reviewer.patch) by @haraldschilly created at 2010-07-21 21:17:38\n\nworks for me",
    "created_at": "2010-07-21T21:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92347",
    "user": "@haraldschilly"
}
```

Attachment [mpmath_call_reviewer.patch](tarball://root/attachments/some-uuid/ticket9566/mpmath_call_reviewer.patch) by @haraldschilly created at 2010-07-21 21:17:38

works for me



---

archive/issue_comments_092348.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-07-21T21:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92348",
    "user": "@haraldschilly"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_092349.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-21T21:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92349",
    "user": "@haraldschilly"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092350.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T21:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92350",
    "user": "@haraldschilly"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092351.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-22T02:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92351",
    "user": "@dandrake"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_092352.json:
```json
{
    "body": "Please include ticket numbers in commit messages! Please change back to positive review when both patches are fixed up. Thanks.",
    "created_at": "2010-07-22T02:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92352",
    "user": "@dandrake"
}
```

Please include ticket numbers in commit messages! Please change back to positive review when both patches are fixed up. Thanks.



---

archive/issue_comments_092353.json:
```json
{
    "body": "Attachment [mpmath_call_FIXED.patch](tarball://root/attachments/some-uuid/ticket9566/mpmath_call_FIXED.patch) by @fredrik-johansson created at 2010-07-22 20:54:14\n\nfixed patch",
    "created_at": "2010-07-22T20:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92353",
    "user": "@fredrik-johansson"
}
```

Attachment [mpmath_call_FIXED.patch](tarball://root/attachments/some-uuid/ticket9566/mpmath_call_FIXED.patch) by @fredrik-johansson created at 2010-07-22 20:54:14

fixed patch



---

archive/issue_comments_092354.json:
```json
{
    "body": "Added mpmath_call_FIXED.patch\n\nI fixed an error in the first patch (there shouldn't be a new kwarg in mpmath_to_sage) and included Harald's change with an extra line to also print the type of the output.",
    "created_at": "2010-07-22T20:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92354",
    "user": "@fredrik-johansson"
}
```

Added mpmath_call_FIXED.patch

I fixed an error in the first patch (there shouldn't be a new kwarg in mpmath_to_sage) and included Harald's change with an extra line to also print the type of the output.



---

archive/issue_comments_092355.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-22T21:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92355",
    "user": "@fredrik-johansson"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092356.json:
```json
{
    "body": "dear release manager, just merge mpmath_call_FIXED.patch and ignore the others.",
    "created_at": "2010-07-22T23:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92356",
    "user": "@haraldschilly"
}
```

dear release manager, just merge mpmath_call_FIXED.patch and ignore the others.



---

archive/issue_comments_092357.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-22T23:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92357",
    "user": "@haraldschilly"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092358.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T23:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92358",
    "user": "@dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_092359.json:
```json
{
    "body": "Replying to [comment:6 schilly]:\n> dear release manager, just merge mpmath_call_FIXED.patch and ignore the others. \n\nDone. Thanks for fixing the commit messages!",
    "created_at": "2010-07-22T23:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9566#issuecomment-92359",
    "user": "@dandrake"
}
```

Replying to [comment:6 schilly]:
> dear release manager, just merge mpmath_call_FIXED.patch and ignore the others. 

Done. Thanks for fixing the commit messages!
