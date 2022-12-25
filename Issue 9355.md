# Issue 9355: 100% coverage for quadratic_forms

archive/issues_009355.json:
```json
{
    "body": "Assignee: mvngu\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9355\n\n",
    "created_at": "2010-06-27T21:48:38Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "100% coverage for quadratic_forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9355",
    "user": "https://github.com/annahaensch"
}
```
Assignee: mvngu



Issue created by migration from https://trac.sagemath.org/ticket/9355





---

archive/issue_comments_088660.json:
```json
{
    "body": "Attachment [trac_9355.patch](tarball://root/attachments/some-uuid/ticket9355/trac_9355.patch) by @annahaensch created at 2010-06-27 21:51:58",
    "created_at": "2010-06-27T21:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88660",
    "user": "https://github.com/annahaensch"
}
```

Attachment [trac_9355.patch](tarball://root/attachments/some-uuid/ticket9355/trac_9355.patch) by @annahaensch created at 2010-06-27 21:51:58



---

archive/issue_comments_088661.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-27T21:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88661",
    "user": "https://github.com/annahaensch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088662.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-28T17:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88662",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088663.json:
```json
{
    "body": "I tried this, and it is fine as far as it goes but `sage -coverage` still grumbles about the lack of a `TestSuite.run()` doctest in genera/genus.py. In fact the two classes in that file don't derive from SageObject (although they probably should), so the TestSuite machinery doesn't work on them; but it would be good to have loads/dumps doctests for these classes. With those added I would be happy for this to go in.\n\n(A much bigger step forward would be adding the quadratic forms code to the reference manual, but that's a separate issue.)",
    "created_at": "2010-06-28T17:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88663",
    "user": "https://github.com/loefflerd"
}
```

I tried this, and it is fine as far as it goes but `sage -coverage` still grumbles about the lack of a `TestSuite.run()` doctest in genera/genus.py. In fact the two classes in that file don't derive from SageObject (although they probably should), so the TestSuite machinery doesn't work on them; but it would be good to have loads/dumps doctests for these classes. With those added I would be happy for this to go in.

(A much bigger step forward would be adding the quadratic forms code to the reference manual, but that's a separate issue.)



---

archive/issue_comments_088664.json:
```json
{
    "body": "Attachment [trac_9355_loads_dumps.patch](tarball://root/attachments/some-uuid/ticket9355/trac_9355_loads_dumps.patch) by @annahaensch created at 2010-06-29 06:25:46\n\nApply on top of trac_9355.patch",
    "created_at": "2010-06-29T06:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88664",
    "user": "https://github.com/annahaensch"
}
```

Attachment [trac_9355_loads_dumps.patch](tarball://root/attachments/some-uuid/ticket9355/trac_9355_loads_dumps.patch) by @annahaensch created at 2010-06-29 06:25:46

Apply on top of trac_9355.patch



---

archive/issue_comments_088665.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-29T06:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88665",
    "user": "https://github.com/annahaensch"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088666.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T07:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88666",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088667.json:
```json
{
    "body": "OK, that looks fine.",
    "created_at": "2010-06-29T07:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88667",
    "user": "https://github.com/loefflerd"
}
```

OK, that looks fine.



---

archive/issue_comments_088668.json:
```json
{
    "body": "Changing keywords from \"\" to \"quadratic forms\".",
    "created_at": "2010-06-29T07:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88668",
    "user": "https://github.com/loefflerd"
}
```

Changing keywords from "" to "quadratic forms".



---

archive/issue_events_023085.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-21T10:07:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9355#event-23085"
}
```



---

archive/issue_comments_088669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T10:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9355#issuecomment-88669",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
