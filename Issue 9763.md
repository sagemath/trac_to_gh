# Issue 9763: Change hashing and printing for NumberFieldIdeals

archive/issues_009763.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  was\n\nThis ticket is a fork from #9400.\n\n* implement hashing for number field ideals that isn't a stupid string repr, hence vastly faster \n\n* make number field ideals *not* print in reduced form; this will look uglier, but is massively faster and more sensible for any real applications, as people learned constantly at sage days 22.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9764\n\n",
    "created_at": "2010-08-18T21:57:52Z",
    "labels": [
        "number fields",
        "major",
        "enhancement"
    ],
    "title": "Change hashing and printing for NumberFieldIdeals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9763",
    "user": "jdemeyer"
}
```
Assignee: davidloeffler

CC:  was

This ticket is a fork from #9400.

* implement hashing for number field ideals that isn't a stupid string repr, hence vastly faster 

* make number field ideals *not* print in reduced form; this will look uglier, but is massively faster and more sensible for any real applications, as people learned constantly at sage days 22.

Issue created by migration from https://trac.sagemath.org/ticket/9764





---

archive/issue_comments_095652.json:
```json
{
    "body": "Needs to be rebased to #9343.",
    "created_at": "2010-08-18T22:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95652",
    "user": "jdemeyer"
}
```

Needs to be rebased to #9343.



---

archive/issue_comments_095653.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-18T22:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95653",
    "user": "jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_095654.json:
```json
{
    "body": "Patch against sage-4.5.3.alpha0",
    "created_at": "2010-08-18T22:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95654",
    "user": "jdemeyer"
}
```

Patch against sage-4.5.3.alpha0



---

archive/issue_comments_095655.json:
```json
{
    "body": "Attachment [9764_ideal_repr.patch](tarball://root/attachments/some-uuid/ticket9764/9764_ideal_repr.patch) by jdemeyer created at 2010-09-16 09:14:28",
    "created_at": "2010-09-16T09:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95655",
    "user": "jdemeyer"
}
```

Attachment [9764_ideal_repr.patch](tarball://root/attachments/some-uuid/ticket9764/9764_ideal_repr.patch) by jdemeyer created at 2010-09-16 09:14:28



---

archive/issue_comments_095656.json:
```json
{
    "body": "Changing keywords from \"\" to \"number field ideal hash\".",
    "created_at": "2010-09-16T16:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95656",
    "user": "jdemeyer"
}
```

Changing keywords from "" to "number field ideal hash".



---

archive/issue_comments_095657.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-16T16:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95657",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095658.json:
```json
{
    "body": "Patch against sage-4.6.alpha0 + #9400 + #9898 + #9753",
    "created_at": "2010-09-16T16:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95658",
    "user": "jdemeyer"
}
```

Patch against sage-4.6.alpha0 + #9400 + #9898 + #9753



---

archive/issue_comments_095659.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T11:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95659",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095660.json:
```json
{
    "body": "Attachment [9764_ideal_repr_new.patch](tarball://root/attachments/some-uuid/ticket9764/9764_ideal_repr_new.patch) by davidloeffler created at 2010-09-23 11:18:15\n\nI applied this to sage-4.6.alpha1 with #9898 and #9753 installed. Changes look sensible, patch applies fine, and all doctests pass. Positive review.",
    "created_at": "2010-09-23T11:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95660",
    "user": "davidloeffler"
}
```

Attachment [9764_ideal_repr_new.patch](tarball://root/attachments/some-uuid/ticket9764/9764_ideal_repr_new.patch) by davidloeffler created at 2010-09-23 11:18:15

I applied this to sage-4.6.alpha1 with #9898 and #9753 installed. Changes look sensible, patch applies fine, and all doctests pass. Positive review.



---

archive/issue_comments_095661.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9763",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9763#issuecomment-95661",
    "user": "mpatel"
}
```

Resolution: fixed
