# Issue 1421: [with patch] finer control in ECM interface

archive/issues_001421.json:
```json
{
    "body": "Assignee: was\n\nI have added a new method \"one_curve\" (maybe a better name can be found) to run exactly one\ncurve (either ECM or P-1 or P+1). Also added examples for find_factor() method.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1421\n\n",
    "created_at": "2007-12-07T19:34:29Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "title": "[with patch] finer control in ECM interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1421",
    "user": "zimmerma"
}
```
Assignee: was

I have added a new method "one_curve" (maybe a better name can be found) to run exactly one
curve (either ECM or P-1 or P+1). Also added examples for find_factor() method.

Issue created by migration from https://trac.sagemath.org/ticket/1421





---

archive/issue_comments_009166.json:
```json
{
    "body": "Attachment [7544.patch](tarball://root/attachments/some-uuid/ticket1421/7544.patch) by zimmerma created at 2007-12-07 19:34:50",
    "created_at": "2007-12-07T19:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1421#issuecomment-9166",
    "user": "zimmerma"
}
```

Attachment [7544.patch](tarball://root/attachments/some-uuid/ticket1421/7544.patch) by zimmerma created at 2007-12-07 19:34:50



---

archive/issue_comments_009167.json:
```json
{
    "body": "code looks good -- if it passes tests, put it in.",
    "created_at": "2007-12-15T10:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1421#issuecomment-9167",
    "user": "was"
}
```

code looks good -- if it passes tests, put it in.



---

archive/issue_comments_009168.json:
```json
{
    "body": "Fixed one line in the original patch -- it creates a string to return as the error message, and then accidentally returns something other than that string (which I'm assuming wasn't the intended behavior).",
    "created_at": "2007-12-18T01:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1421#issuecomment-9168",
    "user": "craigcitro"
}
```

Fixed one line in the original patch -- it creates a string to return as the error message, and then accidentally returns something other than that string (which I'm assuming wasn't the intended behavior).



---

archive/issue_comments_009169.json:
```json
{
    "body": "Attachment [1421-pt2.patch](tarball://root/attachments/some-uuid/ticket1421/1421-pt2.patch) by craigcitro created at 2007-12-18 01:45:38",
    "created_at": "2007-12-18T01:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1421#issuecomment-9169",
    "user": "craigcitro"
}
```

Attachment [1421-pt2.patch](tarball://root/attachments/some-uuid/ticket1421/1421-pt2.patch) by craigcitro created at 2007-12-18 01:45:38



---

archive/issue_comments_009170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-18T02:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1421#issuecomment-9170",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_009171.json:
```json
{
    "body": "Merged in 2.9.1.alpha1",
    "created_at": "2007-12-18T02:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1421#issuecomment-9171",
    "user": "rlm"
}
```

Merged in 2.9.1.alpha1
