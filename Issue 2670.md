# Issue 2670: matrix cmp expr should return a matrix with True/False entries from mapping the test to the entries

archive/issues_002670.json:
```json
{
    "body": "Assignee: mabshoff\n\nSee the numpy where() command or the matlab find() command:\n\nhttp://www.scipy.org/NumPy_for_Matlab_Users\n\nso:\n\n\n```\nsage: m=matrix([[1,2,],[3,4]])\nsage: m>2\n*returns matrix([[False,True],[True,True]])\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2670\n\n",
    "created_at": "2008-03-25T22:27:36Z",
    "labels": [
        "component: cygwin"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "matrix cmp expr should return a matrix with True/False entries from mapping the test to the entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2670",
    "user": "https://github.com/jasongrout"
}
```
Assignee: mabshoff

See the numpy where() command or the matlab find() command:

http://www.scipy.org/NumPy_for_Matlab_Users

so:


```
sage: m=matrix([[1,2,],[3,4]])
sage: m>2
*returns matrix([[False,True],[True,True]])
```



Issue created by migration from https://trac.sagemath.org/ticket/2670





---

archive/issue_comments_018336.json:
```json
{
    "body": "uh, the return above should be `matrix([[False, False], [True, True]])`, of course!",
    "created_at": "2008-03-25T22:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18336",
    "user": "https://github.com/jasongrout"
}
```

uh, the return above should be `matrix([[False, False], [True, True]])`, of course!



---

archive/issue_comments_018337.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2008-03-26T18:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18337",
    "user": "https://github.com/dfdeshom"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_comments_018338.json:
```json
{
    "body": "Do we want to mess with python's semantics for `__cmp__` here? I would rather not take that route and instead define a custom operator (like (`.>`)) to indicate element-wise comparison. \n\nActually, there has been a thread related to element-wise operations on matrices in sage whichc could be part of a larger ticket.",
    "created_at": "2008-03-26T18:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18338",
    "user": "https://github.com/dfdeshom"
}
```

Do we want to mess with python's semantics for `__cmp__` here? I would rather not take that route and instead define a custom operator (like (`.>`)) to indicate element-wise comparison. 

Actually, there has been a thread related to element-wise operations on matrices in sage whichc could be part of a larger ticket.



---

archive/issue_comments_018339.json:
```json
{
    "body": "Changing component from Cygwin to linear algebra.",
    "created_at": "2008-03-26T18:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18339",
    "user": "https://github.com/dfdeshom"
}
```

Changing component from Cygwin to linear algebra.



---

archive/issue_comments_018340.json:
```json
{
    "body": "Changing the original proposal, how about adding a find() method of a matrix that takes a boolean test and applies the boolean function to the entries of the matrix.\n\nSo in the above example,\n\n\n```\nsage: m=matrix([[1,2,],[3,4]])\nsage: m.find(lambda x:x>2)\n*returns matrix([[False,False],[True,True]])\n```\n",
    "created_at": "2008-03-31T19:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18340",
    "user": "https://github.com/jasongrout"
}
```

Changing the original proposal, how about adding a find() method of a matrix that takes a boolean test and applies the boolean function to the entries of the matrix.

So in the above example,


```
sage: m=matrix([[1,2,],[3,4]])
sage: m.find(lambda x:x>2)
*returns matrix([[False,False],[True,True]])
```




---

archive/issue_comments_018341.json:
```json
{
    "body": "Attachment [2670.patch](tarball://root/attachments/some-uuid/ticket2670/2670.patch) by @dfdeshom created at 2008-04-03 15:36:39\n\nA patch is up. Turns out you cannot create a matrix with True and False entries, so I returned one with entries in GF(2).",
    "created_at": "2008-04-03T15:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18341",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2670.patch](tarball://root/attachments/some-uuid/ticket2670/2670.patch) by @dfdeshom created at 2008-04-03 15:36:39

A patch is up. Turns out you cannot create a matrix with True and False entries, so I returned one with entries in GF(2).



---

archive/issue_comments_018342.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-04T21:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18342",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_002862.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T21:56:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2670#event-2862"
}
```



---

archive/issue_comments_018343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T21:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18343",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018344.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T21:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2670#issuecomment-18344",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1
