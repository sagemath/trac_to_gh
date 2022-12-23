# Issue 5901: [with patch, needs review] Avoid permission denied error message when testing with non-writeable sage install

archive/issues_005901.json:
```json
{
    "body": "Assignee: tabbott\n\nThis is a patch to fix the fact that running sage tests prints a permission denied error writing to test.log when you don't have write access to the Sage installation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5901\n\n",
    "created_at": "2009-04-26T05:47:24Z",
    "labels": [
        "debian-package",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] Avoid permission denied error message when testing with non-writeable sage install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5901",
    "user": "tabbott"
}
```
Assignee: tabbott

This is a patch to fix the fact that running sage tests prints a permission denied error writing to test.log when you don't have write access to the Sage installation.


Issue created by migration from https://trac.sagemath.org/ticket/5901





---

archive/issue_comments_046647.json:
```json
{
    "body": "Attachment\n\nI don't think this is applicable anymore. As far as I know, the testing is done in the user's home folder. Making $SAGE_ROOT unwritable didn't give me any permission errors either.",
    "created_at": "2010-04-18T13:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5901#issuecomment-46647",
    "user": "timdumol"
}
```

Attachment

I don't think this is applicable anymore. As far as I know, the testing is done in the user's home folder. Making $SAGE_ROOT unwritable didn't give me any permission errors either.



---

archive/issue_comments_046648.json:
```json
{
    "body": "My bad, I thought this was for sage-test. Looks good to me.",
    "created_at": "2010-06-23T11:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5901#issuecomment-46648",
    "user": "timdumol"
}
```

My bad, I thought this was for sage-test. Looks good to me.



---

archive/issue_comments_046649.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T11:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5901#issuecomment-46649",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046650.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5901",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5901#issuecomment-46650",
    "user": "rlm"
}
```

Resolution: fixed
