# Issue 2316: dsage.start_all() can leave zombie workers around

archive/issues_002316.json:
```json
{
    "body": "Assignee: yi\n\nCC:  was\n\nKeywords: dsage\n\nIf you do dsage.start_all() and kill the server without killing the workers, the workers will be left hanging around so that the next time you do dsage.start_all(), you'll have twice as many workers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2316\n\n",
    "created_at": "2008-02-26T17:40:08Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "title": "dsage.start_all() can leave zombie workers around",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2316",
    "user": "yi"
}
```
Assignee: yi

CC:  was

Keywords: dsage

If you do dsage.start_all() and kill the server without killing the workers, the workers will be left hanging around so that the next time you do dsage.start_all(), you'll have twice as many workers.

Issue created by migration from https://trac.sagemath.org/ticket/2316





---

archive/issue_comments_015414.json:
```json
{
    "body": "patch which kills dsage server and workers when exiting sage",
    "created_at": "2008-04-01T22:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15414",
    "user": "yi"
}
```

patch which kills dsage server and workers when exiting sage



---

archive/issue_comments_015415.json:
```json
{
    "body": "Attachment\n\nAttached patch which kills the dsage server and worker on exit. This in conjunction with the sage cleaner should fix the zombie issues.",
    "created_at": "2008-04-01T22:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15415",
    "user": "yi"
}
```

Attachment

Attached patch which kills the dsage server and worker on exit. This in conjunction with the sage cleaner should fix the zombie issues.



---

archive/issue_comments_015416.json:
```json
{
    "body": "The patch applies to 3.0.alpha1 and fixes the issue for me.",
    "created_at": "2008-04-07T01:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15416",
    "user": "mhansen"
}
```

The patch applies to 3.0.alpha1 and fixes the issue for me.



---

archive/issue_comments_015417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T01:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15417",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015418.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T01:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2316",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2316#issuecomment-15418",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2
