# Issue 9355: 100% coverage for quadratic_forms

archive/issues_009355.json:
```json
{
    "body": "Assignee: mvngu\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9355\n\n",
    "created_at": "2010-06-27T21:48:38Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "100% coverage for quadratic_forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9355",
    "user": "@annahaensch"
}
```
Assignee: mvngu



Issue created by migration from https://trac.sagemath.org/ticket/9355





---

archive/issue_comments_088800.json:
```json
{
    "body": "Attachment [trac_9355.patch](tarball://root/attachments/some-uuid/ticket9355/trac_9355.patch) by @annahaensch created at 2010-06-27 21:51:58",
    "created_at": "2010-06-27T21:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88800",
    "user": "@annahaensch"
}
```

Attachment [trac_9355.patch](tarball://root/attachments/some-uuid/ticket9355/trac_9355.patch) by @annahaensch created at 2010-06-27 21:51:58



---

archive/issue_comments_088801.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-27T21:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88801",
    "user": "@annahaensch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088802.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-28T17:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88802",
    "user": "@loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088803.json:
```json
{
    "body": "I tried this, and it is fine as far as it goes but `sage -coverage` still grumbles about the lack of a `TestSuite.run()` doctest in genera/genus.py. In fact the two classes in that file don't derive from SageObject (although they probably should), so the TestSuite machinery doesn't work on them; but it would be good to have loads/dumps doctests for these classes. With those added I would be happy for this to go in.\n\n(A much bigger step forward would be adding the quadratic forms code to the reference manual, but that's a separate issue.)",
    "created_at": "2010-06-28T17:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88803",
    "user": "@loefflerd"
}
```

I tried this, and it is fine as far as it goes but `sage -coverage` still grumbles about the lack of a `TestSuite.run()` doctest in genera/genus.py. In fact the two classes in that file don't derive from SageObject (although they probably should), so the TestSuite machinery doesn't work on them; but it would be good to have loads/dumps doctests for these classes. With those added I would be happy for this to go in.

(A much bigger step forward would be adding the quadratic forms code to the reference manual, but that's a separate issue.)



---

archive/issue_comments_088804.json:
```json
{
    "body": "Attachment [trac_9355_loads_dumps.patch](tarball://root/attachments/some-uuid/ticket9355/trac_9355_loads_dumps.patch) by @annahaensch created at 2010-06-29 06:25:46\n\nApply on top of trac_9355.patch",
    "created_at": "2010-06-29T06:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88804",
    "user": "@annahaensch"
}
```

Attachment [trac_9355_loads_dumps.patch](tarball://root/attachments/some-uuid/ticket9355/trac_9355_loads_dumps.patch) by @annahaensch created at 2010-06-29 06:25:46

Apply on top of trac_9355.patch



---

archive/issue_comments_088805.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-29T06:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88805",
    "user": "@annahaensch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088806.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T07:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88806",
    "user": "@loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088807.json:
```json
{
    "body": "OK, that looks fine.",
    "created_at": "2010-06-29T07:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88807",
    "user": "@loefflerd"
}
```

OK, that looks fine.



---

archive/issue_comments_088808.json:
```json
{
    "body": "Changing keywords from \"\" to \"quadratic forms\".",
    "created_at": "2010-06-29T07:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88808",
    "user": "@loefflerd"
}
```

Changing keywords from "" to "quadratic forms".



---

archive/issue_comments_088809.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T10:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88809",
    "user": "@qed777"
}
```

Resolution: fixed
