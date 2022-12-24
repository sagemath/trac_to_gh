# Issue 5835: deleting a file from the DATA directory gives an error page

archive/issues_005835.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was\n\nSteps to reproduce:\n\n* Upload a file to a worksheet using the Data... menu\n* Click on the filename in the Data... menu\n* Click the link to delete the file.\n\nMy guess is that it deletes the file, but then tries to display it.  Instead, it should either go back to the worksheet view or to some list of all files in the DATA directory.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5835\n\n",
    "created_at": "2009-04-20T17:09:44Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "deleting a file from the DATA directory gives an error page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5835",
    "user": "jason"
}
```
Assignee: boothby

CC:  was

Steps to reproduce:

* Upload a file to a worksheet using the Data... menu
* Click on the filename in the Data... menu
* Click the link to delete the file.

My guess is that it deletes the file, but then tries to display it.  Instead, it should either go back to the worksheet view or to some list of all files in the DATA directory.

Issue created by migration from https://trac.sagemath.org/ticket/5835





---

archive/issue_comments_045857.json:
```json
{
    "body": "This has been fixed. Confirm and chekc please?",
    "created_at": "2010-01-18T04:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5835#issuecomment-45857",
    "user": "timdumol"
}
```

This has been fixed. Confirm and chekc please?



---

archive/issue_comments_045858.json:
```json
{
    "body": "Works with sagenb-0.6",
    "created_at": "2010-01-19T03:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5835#issuecomment-45858",
    "user": "timdumol"
}
```

Works with sagenb-0.6



---

archive/issue_comments_045859.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5835#issuecomment-45859",
    "user": "timdumol"
}
```

Resolution: duplicate



---

archive/issue_comments_045860.json:
```json
{
    "body": "Resolution changed from duplicate to fixed",
    "created_at": "2010-01-19T03:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5835#issuecomment-45860",
    "user": "timdumol"
}
```

Resolution changed from duplicate to fixed
