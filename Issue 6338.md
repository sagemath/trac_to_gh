# Issue 6338: make sage -sdist and -bdist take an existing tag name and verify that the tag name is valid

archive/issues_006338.json:
```json
{
    "body": "Assignee: tbd\n\nIt's annoying that one has to hg tag --remove VERSION by hand in a bunch of repos if one wants to rebundle a release.\n\nAlso, sage -sdist sage-VERSION instead of sage -sdist VERSION causes problems.  Check for this and raise an error.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6338\n\n",
    "created_at": "2009-06-16T19:00:05Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "make sage -sdist and -bdist take an existing tag name and verify that the tag name is valid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6338",
    "user": "https://github.com/ncalexan"
}
```
Assignee: tbd

It's annoying that one has to hg tag --remove VERSION by hand in a bunch of repos if one wants to rebundle a release.

Also, sage -sdist sage-VERSION instead of sage -sdist VERSION causes problems.  Check for this and raise an error.

Issue created by migration from https://trac.sagemath.org/ticket/6338





---

archive/issue_comments_050496.json:
```json
{
    "body": "Changing component from distribution to scripts.",
    "created_at": "2012-05-18T13:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50496",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from distribution to scripts.



---

archive/issue_comments_050497.json:
```json
{
    "body": "Changing assignee from tbd to @nexttime.",
    "created_at": "2012-05-18T13:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50497",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from tbd to @nexttime.



---

archive/issue_comments_050498.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-05-18T13:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50498",
    "user": "https://github.com/jdemeyer"
}
```

Changing priority from major to minor.



---

archive/issue_comments_050499.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-18T13:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50499",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050500.json:
```json
{
    "body": "Attachment [6338_sagedist.patch](tarball://root/attachments/some-uuid/ticket6338/6338_sagedist.patch) by @jdemeyer created at 2012-05-19 08:30:37",
    "created_at": "2012-05-19T08:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50500",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [6338_sagedist.patch](tarball://root/attachments/some-uuid/ticket6338/6338_sagedist.patch) by @jdemeyer created at 2012-05-19 08:30:37



---

archive/issue_comments_050501.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-23T16:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50501",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050502.json:
```json
{
    "body": "Looks good. I tripped over this more than once, thanks for fixing!",
    "created_at": "2012-05-23T16:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50502",
    "user": "https://github.com/vbraun"
}
```

Looks good. I tripped over this more than once, thanks for fixing!



---

archive/issue_comments_050503.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-05-23T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50503",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
