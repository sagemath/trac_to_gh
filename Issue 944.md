# Issue 944: "sage -t ." does not run doctests in the current directory

archive/issues_000944.json:
```json
{
    "body": "Assignee: failure\n\n\"sage -t .\" should run the doctests in the current directory, but it doesn't.  It looks like maybe it fails when the directory name starts with a period:\n\n\n```\ncwitty@magnetar:~/sage/devel/sage/sage/rings/polynomial$ ~/sage/sage -t .\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 0.0 seconds\ncwitty@magnetar:~/sage/devel/sage/sage/rings/polynomial$ ~/sage/sage -t ../polynomial/\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 0.0 seconds\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/944\n\n",
    "created_at": "2007-10-20T17:05:01Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "title": "\"sage -t .\" does not run doctests in the current directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/944",
    "user": "cwitty"
}
```
Assignee: failure

"sage -t ." should run the doctests in the current directory, but it doesn't.  It looks like maybe it fails when the directory name starts with a period:


```
cwitty@magnetar:~/sage/devel/sage/sage/rings/polynomial$ ~/sage/sage -t .
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds
cwitty@magnetar:~/sage/devel/sage/sage/rings/polynomial$ ~/sage/sage -t ../polynomial/
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds
```



Issue created by migration from https://trac.sagemath.org/ticket/944





---

archive/issue_comments_005772.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T14:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/944#issuecomment-5772",
    "user": "gfurnish"
}
```

Resolution: fixed



---

archive/issue_comments_005773.json:
```json
{
    "body": "Fixed in sage-ptest",
    "created_at": "2008-03-21T14:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/944#issuecomment-5773",
    "user": "gfurnish"
}
```

Fixed in sage-ptest
