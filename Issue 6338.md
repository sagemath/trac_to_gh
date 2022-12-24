# Issue 6338: make sage -sdist and -bdist take an existing tag name and verify that the tag name is valid

archive/issues_006338.json:
```json
{
    "body": "Assignee: tbd\n\nIt's annoying that one has to hg tag --remove VERSION by hand in a bunch of repos if one wants to rebundle a release.\n\nAlso, sage -sdist sage-VERSION instead of sage -sdist VERSION causes problems.  Check for this and raise an error.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6338\n\n",
    "created_at": "2009-06-16T19:00:05Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "make sage -sdist and -bdist take an existing tag name and verify that the tag name is valid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6338",
    "user": "ncalexan"
}
```
Assignee: tbd

It's annoying that one has to hg tag --remove VERSION by hand in a bunch of repos if one wants to rebundle a release.

Also, sage -sdist sage-VERSION instead of sage -sdist VERSION causes problems.  Check for this and raise an error.

Issue created by migration from https://trac.sagemath.org/ticket/6338





---

archive/issue_comments_050592.json:
```json
{
    "body": "Changing component from distribution to scripts.",
    "created_at": "2012-05-18T13:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50592",
    "user": "jdemeyer"
}
```

Changing component from distribution to scripts.



---

archive/issue_comments_050593.json:
```json
{
    "body": "Changing assignee from tbd to leif.",
    "created_at": "2012-05-18T13:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50593",
    "user": "jdemeyer"
}
```

Changing assignee from tbd to leif.



---

archive/issue_comments_050594.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-05-18T13:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50594",
    "user": "jdemeyer"
}
```

Changing priority from major to minor.



---

archive/issue_comments_050595.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-18T13:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50595",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050596.json:
```json
{
    "body": "Attachment [6338_sagedist.patch](tarball://root/attachments/some-uuid/ticket6338/6338_sagedist.patch) by jdemeyer created at 2012-05-19 08:30:37",
    "created_at": "2012-05-19T08:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50596",
    "user": "jdemeyer"
}
```

Attachment [6338_sagedist.patch](tarball://root/attachments/some-uuid/ticket6338/6338_sagedist.patch) by jdemeyer created at 2012-05-19 08:30:37



---

archive/issue_comments_050597.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-23T16:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50597",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050598.json:
```json
{
    "body": "Looks good. I tripped over this more than once, thanks for fixing!",
    "created_at": "2012-05-23T16:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50598",
    "user": "vbraun"
}
```

Looks good. I tripped over this more than once, thanks for fixing!



---

archive/issue_comments_050599.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-05-23T21:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6338#issuecomment-50599",
    "user": "jdemeyer"
}
```

Resolution: fixed
