# Issue 7295: typo in ecm spkg-install

archive/issues_007295.json:
```json
{
    "body": "Assignee: tbd\n\nThe removal of the old version of ecm in ecm-6.2.1_p0.spkg\nis broken because of typo:\n\n\nrm -f \"$SAGE_LCOAL\"/lib/libecm.*\n\n\nshould be:\n\n\nrm -f \"$SAGE_LOCAL\"/lib/libecm.*\n\nNotice LOCAL\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7295\n\n",
    "created_at": "2009-10-25T09:35:57Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "typo in ecm spkg-install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7295",
    "user": "@kiwifb"
}
```
Assignee: tbd

The removal of the old version of ecm in ecm-6.2.1_p0.spkg
is broken because of typo:


rm -f "$SAGE_LCOAL"/lib/libecm.*


should be:


rm -f "$SAGE_LOCAL"/lib/libecm.*

Notice LOCAL


Issue created by migration from https://trac.sagemath.org/ticket/7295





---

archive/issue_comments_060734.json:
```json
{
    "body": "patch to spkg-install",
    "created_at": "2009-10-26T01:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7295#issuecomment-60734",
    "user": "@kiwifb"
}
```

patch to spkg-install



---

archive/issue_comments_060735.json:
```json
{
    "body": "Attachment [ecm-6.2.1_p0-spkg-install.patch](tarball://root/attachments/some-uuid/ticket7295/ecm-6.2.1_p0-spkg-install.patch) by @kiwifb created at 2009-10-26 01:02:32",
    "created_at": "2009-10-26T01:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7295#issuecomment-60735",
    "user": "@kiwifb"
}
```

Attachment [ecm-6.2.1_p0-spkg-install.patch](tarball://root/attachments/some-uuid/ticket7295/ecm-6.2.1_p0-spkg-install.patch) by @kiwifb created at 2009-10-26 01:02:32



---

archive/issue_comments_060736.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T01:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7295#issuecomment-60736",
    "user": "@kiwifb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060737.json:
```json
{
    "body": "The updated spkg can be found at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/ecm/ecm-6.2.1.p1.spkg\n\nAll changes have been committed in fbissey's name.",
    "created_at": "2009-10-28T14:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7295#issuecomment-60737",
    "user": "mvngu"
}
```

The updated spkg can be found at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/ecm/ecm-6.2.1.p1.spkg

All changes have been committed in fbissey's name.



---

archive/issue_comments_060738.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-28T14:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7295#issuecomment-60738",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T16:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7295",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7295#issuecomment-60739",
    "user": "@mwhansen"
}
```

Resolution: fixed
