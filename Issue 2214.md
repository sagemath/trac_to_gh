# Issue 2214: DSage and memory leaks

archive/issues_002214.json:
```json
{
    "body": "Assignee: yi\n\nIf a job has a memory leak, it is not reclaimed when the worker resets itself. If the memory after reset does not go down to \"normal\" (or, say, twice normal) then it should warn the user that the job leaked memory and actually restart the worker. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2214\n\n",
    "created_at": "2008-02-19T22:05:09Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "DSage and memory leaks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2214",
    "user": "robertwb"
}
```
Assignee: yi

If a job has a memory leak, it is not reclaimed when the worker resets itself. If the memory after reset does not go down to "normal" (or, say, twice normal) then it should warn the user that the job leaked memory and actually restart the worker. 



Issue created by migration from https://trac.sagemath.org/ticket/2214





---

archive/issue_comments_014625.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-29T06:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14625",
    "user": "yi"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014626.json:
```json
{
    "body": "This will be fixed once #2322 gets merged.",
    "created_at": "2008-02-29T06:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14626",
    "user": "yi"
}
```

This will be fixed once #2322 gets merged.



---

archive/issue_comments_014627.json:
```json
{
    "body": "This bug has been fixed in 2.10.4, please close it.",
    "created_at": "2008-03-24T16:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14627",
    "user": "yi"
}
```

This bug has been fixed in 2.10.4, please close it.



---

archive/issue_comments_014628.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-24T16:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14628",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014629.json:
```json
{
    "body": "Fixed in Sage 2.10.4 according to Yi, so close this.",
    "created_at": "2008-03-24T16:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2214#issuecomment-14629",
    "user": "mabshoff"
}
```

Fixed in Sage 2.10.4 according to Yi, so close this.
