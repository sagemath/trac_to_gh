# Issue 7521: typo in optional doctest for R interface

archive/issues_007521.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jason mhansen\n\n\n```\nsage: r.install_package('Hmisc')       #optional \n```\n\nmakes no sense, because the command is install_packages().\n\nIssue created by migration from https://trac.sagemath.org/ticket/7521\n\n",
    "created_at": "2009-11-24T01:00:30Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "typo in optional doctest for R interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7521",
    "user": "kcrisman"
}
```
Assignee: tbd

CC:  jason mhansen


```
sage: r.install_package('Hmisc')       #optional 
```

makes no sense, because the command is install_packages().

Issue created by migration from https://trac.sagemath.org/ticket/7521





---

archive/issue_comments_063721.json:
```json
{
    "body": "Attachment [trac_7521-R-typo.patch](tarball://root/attachments/some-uuid/ticket7521/trac_7521-R-typo.patch) by kcrisman created at 2009-12-14 15:48:01\n\nBased on 4.2.1",
    "created_at": "2009-12-14T15:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63721",
    "user": "kcrisman"
}
```

Attachment [trac_7521-R-typo.patch](tarball://root/attachments/some-uuid/ticket7521/trac_7521-R-typo.patch) by kcrisman created at 2009-12-14 15:48:01

Based on 4.2.1



---

archive/issue_comments_063722.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-14T15:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63722",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063723.json:
```json
{
    "body": "This should apply ok to newer versions, though.  Please note that Hmisc has been replaced with a package which depends only on R itself, in addition to fixing the doctest. \n\nThis should be VERY easy to review.",
    "created_at": "2009-12-14T15:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63723",
    "user": "kcrisman"
}
```

This should apply ok to newer versions, though.  Please note that Hmisc has been replaced with a package which depends only on R itself, in addition to fixing the doctest. 

This should be VERY easy to review.



---

archive/issue_comments_063724.json:
```json
{
    "body": "Something looks weird with the character encoding in the patch.",
    "created_at": "2009-12-14T15:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63724",
    "user": "mhansen"
}
```

Something looks weird with the character encoding in the patch.



---

archive/issue_comments_063725.json:
```json
{
    "body": "You're right.  I'm not sure how to fix that; what the original looks like is in the attached file.  I don't know how to deal with that, since I can't actually create those kind of quotes on my computer.  Would it be enough to just replace the weird stuff in line 385 with `aaMI'?",
    "created_at": "2009-12-14T16:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63725",
    "user": "kcrisman"
}
```

You're right.  I'm not sure how to fix that; what the original looks like is in the attached file.  I don't know how to deal with that, since I can't actually create those kind of quotes on my computer.  Would it be enough to just replace the weird stuff in line 385 with `aaMI'?



---

archive/issue_comments_063726.json:
```json
{
    "body": "Attachment [pic.tiff](tarball://root/attachments/some-uuid/ticket7521/pic.tiff) by kcrisman created at 2009-12-14 16:28:51",
    "created_at": "2009-12-14T16:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63726",
    "user": "kcrisman"
}
```

Attachment [pic.tiff](tarball://root/attachments/some-uuid/ticket7521/pic.tiff) by kcrisman created at 2009-12-14 16:28:51



---

archive/issue_comments_063727.json:
```json
{
    "body": "As far as I can tell, we can also now remove the warnings for Mac in this function. New patch coming up - hopefully without weird character issues.",
    "created_at": "2010-01-25T19:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63727",
    "user": "kcrisman"
}
```

As far as I can tell, we can also now remove the warnings for Mac in this function. New patch coming up - hopefully without weird character issues.



---

archive/issue_comments_063728.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-25T19:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63728",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063729.json:
```json
{
    "body": "Attachment [trac_7521-R-typo-take2.patch](tarball://root/attachments/some-uuid/ticket7521/trac_7521-R-typo-take2.patch) by kcrisman created at 2010-01-25 19:37:00\n\nBased on 4.3.1, sort of depends on spkg in #6532",
    "created_at": "2010-01-25T19:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63729",
    "user": "kcrisman"
}
```

Attachment [trac_7521-R-typo-take2.patch](tarball://root/attachments/some-uuid/ticket7521/trac_7521-R-typo-take2.patch) by kcrisman created at 2010-01-25 19:37:00

Based on 4.3.1, sort of depends on spkg in #6532



---

archive/issue_comments_063730.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-25T19:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63730",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063731.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-25T23:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63731",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063732.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-01-25T23:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63732",
    "user": "mvngu"
}
```

Looks good to me.



---

archive/issue_comments_063733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T23:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63733",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_063734.json:
```json
{
    "body": "Merged [trac_7521-R-typo-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7521/trac_7521-R-typo-take2.patch).",
    "created_at": "2010-01-25T23:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7521#issuecomment-63734",
    "user": "mvngu"
}
```

Merged [trac_7521-R-typo-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7521/trac_7521-R-typo-take2.patch).
