# Issue 9450: Implement a factor() function for NumberFieldElement

archive/issues_009450.json:
```json
{
    "body": "Assignee: @loefflerd\n\nThe attached patch implements a factor() function for number field elements.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9450\n\n",
    "created_at": "2010-07-07T21:06:36Z",
    "labels": [
        "component: number fields"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Implement a factor() function for NumberFieldElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9450",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @loefflerd

The attached patch implements a factor() function for number field elements.

Issue created by migration from https://trac.sagemath.org/ticket/9450





---

archive/issue_events_023363.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-07-07T21:17:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9450#event-23363"
}
```



---

archive/issue_comments_090419.json:
```json
{
    "body": "Attachment [9450.patch](tarball://root/attachments/some-uuid/ticket9450/9450.patch) by @jdemeyer created at 2010-07-07 21:17:52",
    "created_at": "2010-07-07T21:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90419",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9450.patch](tarball://root/attachments/some-uuid/ticket9450/9450.patch) by @jdemeyer created at 2010-07-07 21:17:52



---

archive/issue_comments_090420.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-07T21:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90420",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090421.json:
```json
{
    "body": "Attachment [trac_9450-reviewer.patch](tarball://root/attachments/some-uuid/ticket9450/trac_9450-reviewer.patch) by @JohnCremona created at 2010-07-08 12:26:37\n\nApply after previous patch",
    "created_at": "2010-07-08T12:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90421",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_9450-reviewer.patch](tarball://root/attachments/some-uuid/ticket9450/trac_9450-reviewer.patch) by @JohnCremona created at 2010-07-08 12:26:37

Apply after previous patch



---

archive/issue_comments_090422.json:
```json
{
    "body": "The patch applies and works fine.  I have changed the docstring a little, added a test for factoring 0 and simplified the code in a couple of places.  I also added an example in sage/rings/arith.py since the generic factor() function now works on number field elements!\n\nSince I changed quite a lot, I have left this as \"needs review\".",
    "created_at": "2010-07-08T12:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90422",
    "user": "https://github.com/JohnCremona"
}
```

The patch applies and works fine.  I have changed the docstring a little, added a test for factoring 0 and simplified the code in a couple of places.  I also added an example in sage/rings/arith.py since the generic factor() function now works on number field elements!

Since I changed quite a lot, I have left this as "needs review".



---

archive/issue_comments_090423.json:
```json
{
    "body": "John's changes look good to me.",
    "created_at": "2010-07-11T01:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90423",
    "user": "https://github.com/mwhansen"
}
```

John's changes look good to me.



---

archive/issue_comments_090424.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-11T01:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90424",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023364.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-20T07:53:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9450#event-23364"
}
```



---

archive/issue_comments_090425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T07:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9450#issuecomment-90425",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
