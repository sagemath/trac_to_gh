# Issue 9257: remove misc/darcs.py in Sage 5.0

archive/issues_009257.json:
```json
{
    "body": "Assignee: mvngu\n\nFrom [sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/971ea3ce256eed20):\n\n```\nThe file misc/darcs.py was meant to serve as an interface to the Darcs\nsource code version control system, back in the old days before Sage\nswitched to using Mercurial. With the upcoming Sage 5.0 milestone, I\nthink that module can be removed from the Sage library. I believe its\nremoval would result in very minimal (next to zero?) hassle regarding\nissues of backward compatibility. If I understand the Mercurial log of\nthe Sage library correctly, Sage hasn't been using Darcs for over 2\nyears now, or even since February 2006. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9257\n\n",
    "created_at": "2010-06-18T05:58:15Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "remove misc/darcs.py in Sage 5.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9257",
    "user": "mvngu"
}
```
Assignee: mvngu

From [sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/971ea3ce256eed20):

```
The file misc/darcs.py was meant to serve as an interface to the Darcs
source code version control system, back in the old days before Sage
switched to using Mercurial. With the upcoming Sage 5.0 milestone, I
think that module can be removed from the Sage library. I believe its
removal would result in very minimal (next to zero?) hassle regarding
issues of backward compatibility. If I understand the Mercurial log of
the Sage library correctly, Sage hasn't been using Darcs for over 2
years now, or even since February 2006. 
```


Issue created by migration from https://trac.sagemath.org/ticket/9257





---

archive/issue_comments_087112.json:
```json
{
    "body": "Attachment [9257-remove-darcs.patch](tarball://root/attachments/some-uuid/ticket9257/9257-remove-darcs.patch) by robertwb created at 2010-06-21 21:36:15",
    "created_at": "2010-06-21T21:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-87112",
    "user": "robertwb"
}
```

Attachment [9257-remove-darcs.patch](tarball://root/attachments/some-uuid/ticket9257/9257-remove-darcs.patch) by robertwb created at 2010-06-21 21:36:15



---

archive/issue_comments_087113.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-21T21:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-87113",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087114.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-22T17:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-87114",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087115.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-06-22T17:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-87115",
    "user": "rlm"
}
```

Looks good to me.



---

archive/issue_comments_087116.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T10:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-87116",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_087117.json:
```json
{
    "body": "Followup; apparently we *still* have remnants of darcs.  See #13122.",
    "created_at": "2012-06-16T03:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-87117",
    "user": "kcrisman"
}
```

Followup; apparently we *still* have remnants of darcs.  See #13122.



---

archive/issue_comments_087118.json:
```json
{
    "body": "As a historical note, the original thread referenced here was off by about a year and a half on when Sage 5.0 would be released... ah, expectations.",
    "created_at": "2012-06-16T03:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9257#issuecomment-87118",
    "user": "kcrisman"
}
```

As a historical note, the original thread referenced here was off by about a year and a half on when Sage 5.0 would be released... ah, expectations.
