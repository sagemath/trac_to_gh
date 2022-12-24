# Issue 1953: [with patch] fix problems found by Jason while reviewing #1945

archive/issues_001953.json:
```json
{
    "body": "Assignee: @williamstein\n\nJason found a couple of problems with calculus.py while reviewing #1945: a one-character typo and a duplicate method.  The attached patch fixes both problems.\n\nDoctests pass in sage/calculus/.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1953\n\n",
    "created_at": "2008-01-27T22:05:53Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch] fix problems found by Jason while reviewing #1945",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1953",
    "user": "cwitty"
}
```
Assignee: @williamstein

Jason found a couple of problems with calculus.py while reviewing #1945: a one-character typo and a duplicate method.  The attached patch fixes both problems.

Doctests pass in sage/calculus/.


Issue created by migration from https://trac.sagemath.org/ticket/1953





---

archive/issue_comments_012439.json:
```json
{
    "body": "Attachment [trac-1953.patch](tarball://root/attachments/some-uuid/ticket1953/trac-1953.patch) by @williamstein created at 2008-01-27 22:17:32\n\nI think this patch is OK.\n\nI want to make one comment though.  With the previous version of this patch, if you made a new class that derives from CallableSymbolicExpressionRing_class and overload args, then arguments would automatically call the overloaded method.  Now it won't -- argument will give you the old method before overloading.  This isn't a problem since that's not done in calculus.py.  \n\nSo I give this a positive review.",
    "created_at": "2008-01-27T22:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1953#issuecomment-12439",
    "user": "@williamstein"
}
```

Attachment [trac-1953.patch](tarball://root/attachments/some-uuid/ticket1953/trac-1953.patch) by @williamstein created at 2008-01-27 22:17:32

I think this patch is OK.

I want to make one comment though.  With the previous version of this patch, if you made a new class that derives from CallableSymbolicExpressionRing_class and overload args, then arguments would automatically call the overloaded method.  Now it won't -- argument will give you the old method before overloading.  This isn't a problem since that's not done in calculus.py.  

So I give this a positive review.



---

archive/issue_comments_012440.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T22:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1953#issuecomment-12440",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012441.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc2",
    "created_at": "2008-01-27T22:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1953#issuecomment-12441",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc2
