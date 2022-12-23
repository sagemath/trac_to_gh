# Issue 5899: [with patch, needs review] Update Debian build support for Sage spkg

archive/issues_005899.json:
```json
{
    "body": "Assignee: tabbott\n\nI've been working on getting the Debian build of Sage updated for the current version.  Because of some refactoring in setup.py for the sage spkg, the SAGE_DEBIAN definition no longer works as intended.  The three patches that are attached should fix this, without having any effect on other systems.  It'd be good to get these merged just to bring down the number of patches I have against Sage (future work for this code is to rename SAGE_DEBIAN to something more appropriate).\n\nThey need to be applied in order.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5899\n\n",
    "created_at": "2009-04-26T05:39:48Z",
    "labels": [
        "debian-package",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Update Debian build support for Sage spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5899",
    "user": "tabbott"
}
```
Assignee: tabbott

I've been working on getting the Debian build of Sage updated for the current version.  Because of some refactoring in setup.py for the sage spkg, the SAGE_DEBIAN definition no longer works as intended.  The three patches that are attached should fix this, without having any effect on other systems.  It'd be good to get these merged just to bring down the number of patches I have against Sage (future work for this code is to rename SAGE_DEBIAN to something more appropriate).

They need to be applied in order.

Issue created by migration from https://trac.sagemath.org/ticket/5899





---

archive/issue_comments_046637.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-26T05:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5899#issuecomment-46637",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_046638.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-26T05:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5899#issuecomment-46638",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_046639.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-16T08:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5899#issuecomment-46639",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046640.json:
```json
{
    "body": "Attachment\n\nLooks good to me.",
    "created_at": "2009-10-16T08:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5899#issuecomment-46640",
    "user": "mhansen"
}
```

Attachment

Looks good to me.



---

archive/issue_comments_046641.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T08:46:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5899#issuecomment-46641",
    "user": "mhansen"
}
```

Resolution: fixed
