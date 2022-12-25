# Issue 1880: Sage 2.10: qqbar numerical doctest failure

archive/issues_001880.json:
```json
{
    "body": "Assignee: mabshoff\n\nReported in http://groups.google.com/group/sage-devel/browse_thread/thread/ff3b035b8b42961f/f0dd2e8510b13853#f0dd2e8510b13853 by Francois: \n\n\n```\nFile \"qqbar.py\", line 3075:\n    sage: cp.complex_roots(30, 1)\nExpected:\n    [[1.1892071150027208 .. 1.1892071150027213],\n[-1.1892071150027213 .. -1.18920711500272...], [1.1892071150027208 ..\n1.1892071150027213]*I, [-1.1892071150027213 .. -1.1892071150027208]*I]\nGot:\n    [[1.1892071150027208 .. 1.1892071150027213],\n[-1.1892071150027213 .. -1.1892071150027210], [1.1892071150027210 ..\n1.1892071150027213]*I, [-1.1892071150027213 .. -1.1892071150027208]*I] \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1880\n\n",
    "created_at": "2008-01-21T21:40:19Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Sage 2.10: qqbar numerical doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Reported in http://groups.google.com/group/sage-devel/browse_thread/thread/ff3b035b8b42961f/f0dd2e8510b13853#f0dd2e8510b13853 by Francois: 


```
File "qqbar.py", line 3075:
    sage: cp.complex_roots(30, 1)
Expected:
    [[1.1892071150027208 .. 1.1892071150027213],
[-1.1892071150027213 .. -1.18920711500272...], [1.1892071150027208 ..
1.1892071150027213]*I, [-1.1892071150027213 .. -1.1892071150027208]*I]
Got:
    [[1.1892071150027208 .. 1.1892071150027213],
[-1.1892071150027213 .. -1.1892071150027210], [1.1892071150027210 ..
1.1892071150027213]*I, [-1.1892071150027213 .. -1.1892071150027208]*I] 
```


Issue created by migration from https://trac.sagemath.org/ticket/1880





---

archive/issue_comments_011867.json:
```json
{
    "body": "Attachment [Sage-2.10.1.alpha0-fix-doctest-1880.patch](tarball://root/attachments/some-uuid/ticket1880/Sage-2.10.1.alpha0-fix-doctest-1880.patch) by mabshoff created at 2008-01-21 22:44:41",
    "created_at": "2008-01-21T22:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1880#issuecomment-11867",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.1.alpha0-fix-doctest-1880.patch](tarball://root/attachments/some-uuid/ticket1880/Sage-2.10.1.alpha0-fix-doctest-1880.patch) by mabshoff created at 2008-01-21 22:44:41



---

archive/issue_comments_011868.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-22T01:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1880#issuecomment-11868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011869.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-22T01:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1880",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1880#issuecomment-11869",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1
