# Issue 6804: Permutation.weak_excedences inconsistency

archive/issues_006804.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @orlitzky\n\nEither code or docstring is wrong in 4.1.1, \"=\" vs. \">=\":\n\n\n```\nReturns all the numbers self[i] such that self[i] = i+1\n```\n\n\n\n```\nif self[i] >= i + 1:\n    res.append(self[i])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6804\n\n",
    "created_at": "2009-08-22T17:16:29Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Permutation.weak_excedences inconsistency",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6804",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: @mwhansen

CC:  @orlitzky

Either code or docstring is wrong in 4.1.1, "=" vs. ">=":


```
Returns all the numbers self[i] such that self[i] = i+1
```



```
if self[i] >= i + 1:
    res.append(self[i])
```


Issue created by migration from https://trac.sagemath.org/ticket/6804





---

archive/issue_comments_055923.json:
```json
{
    "body": "Attachment [sage-trac_6804.patch](tarball://root/attachments/some-uuid/ticket6804/sage-trac_6804.patch) by @orlitzky created at 2012-01-09 05:24:49\n\nFix the docstring.",
    "created_at": "2012-01-09T05:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6804#issuecomment-55923",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_6804.patch](tarball://root/attachments/some-uuid/ticket6804/sage-trac_6804.patch) by @orlitzky created at 2012-01-09 05:24:49

Fix the docstring.



---

archive/issue_comments_055924.json:
```json
{
    "body": "I found a reference; the bug was in the docstring.",
    "created_at": "2012-01-09T05:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6804#issuecomment-55924",
    "user": "https://github.com/orlitzky"
}
```

I found a reference; the bug was in the docstring.



---

archive/issue_comments_055925.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-09T05:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6804#issuecomment-55925",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_055926.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-29T15:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6804#issuecomment-55926",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055927.json:
```json
{
    "body": "Well, then...`:-)`\n\nNathann",
    "created_at": "2012-01-29T15:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6804#issuecomment-55927",
    "user": "https://github.com/nathanncohen"
}
```

Well, then...`:-)`

Nathann



---

archive/issue_events_016034.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-02-02T12:51:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6804",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6804#event-16034"
}
```



---

archive/issue_comments_055928.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-02T12:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6804#issuecomment-55928",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
