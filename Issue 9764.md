# Issue 9764: matrix2.pyx: replace "x < 1e-15" by "abs(x) < 1e-15"

archive/issues_009764.json:
```json
{
    "body": "Assignee: @aghitza\n\nIn matrix2.pyx, there is a doctest (line 6406):\n\n```\n            sage: all(imag(e) < 1.1e-15 for e in eigs)\n```\n\nWe should replace \"imag(e)\" by \"abs(imag(e))\".\n\nThe attached patch depends on #9760.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9765\n\n",
    "created_at": "2010-08-18T22:14:49Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "matrix2.pyx: replace \"x < 1e-15\" by \"abs(x) < 1e-15\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9764",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @aghitza

In matrix2.pyx, there is a doctest (line 6406):

```
            sage: all(imag(e) < 1.1e-15 for e in eigs)
```

We should replace "imag(e)" by "abs(imag(e))".

The attached patch depends on #9760.


Issue created by migration from https://trac.sagemath.org/ticket/9765





---

archive/issue_comments_095503.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-18T22:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95503",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095504.json:
```json
{
    "body": "Attachment [trac_9765-matrix2-abs.patch](tarball://root/attachments/some-uuid/ticket9765/trac_9765-matrix2-abs.patch) by @jhpalmieri created at 2010-08-18 22:16:48",
    "created_at": "2010-08-18T22:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95504",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9765-matrix2-abs.patch](tarball://root/attachments/some-uuid/ticket9765/trac_9765-matrix2-abs.patch) by @jhpalmieri created at 2010-08-18 22:16:48



---

archive/issue_comments_095505.json:
```json
{
    "body": "The test still passes on bsd, redhawk, sage, and t2.math.",
    "created_at": "2010-08-23T01:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95505",
    "user": "https://github.com/qed777"
}
```

The test still passes on bsd, redhawk, sage, and t2.math.



---

archive/issue_comments_095506.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-23T01:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95506",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095507.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-08-23T22:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95507",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_events_024470.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-23T22:17:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9764#event-24470"
}
```



---

archive/issue_comments_095508.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-24T02:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95508",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024471.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-24T02:48:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9764#event-24471"
}
```
