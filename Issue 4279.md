# Issue 4279: Sage 3.1.3.rc0: numerical noise in rings/real_lazy.pyx

archive/issues_004279.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage/sage/rings/real_lazy.pyx \n********************************************************************** \nFile \"/Users/mh/Desktop/sage-3.1.3.rc0/tmp/real_lazy.py\", line 549: \n    sage: complex(CLF(-1)^(1/4)) \nExpected: \n    (0.70710678118654757+0.70710678118654746j) \nGot: \n    (0.70710678118654746+0.70710678118654757j) \n*********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4279\n\n",
    "created_at": "2008-10-14T09:42:43Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Sage 3.1.3.rc0: numerical noise in rings/real_lazy.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4279",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t  devel/sage/sage/rings/real_lazy.pyx 
********************************************************************** 
File "/Users/mh/Desktop/sage-3.1.3.rc0/tmp/real_lazy.py", line 549: 
    sage: complex(CLF(-1)^(1/4)) 
Expected: 
    (0.70710678118654757+0.70710678118654746j) 
Got: 
    (0.70710678118654746+0.70710678118654757j) 
*********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4279





---

archive/issue_comments_031301.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-14T09:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4279#issuecomment-31301",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031302.json:
```json
{
    "body": "On a G5 with 10.4 I am seeing the following issue:\n\n```\nsage -t -long devel/sage/sage/rings/real_lazy.pyx           \n**********************************************************************\nFile \"/Users/mabshoff/sage-3.1.3.rc0/tmp/real_lazy.py\", line 549:\n    sage: complex(CLF(-1)^(1/4))\nExpected:\n    (0.70710678118654757+0.70710678118654746j)\nGot:\n    (0.70710678118654746+0.70710678118654757j)\n**********************************************************************\n```\n",
    "created_at": "2008-10-14T11:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4279#issuecomment-31302",
    "user": "mabshoff"
}
```

On a G5 with 10.4 I am seeing the following issue:

```
sage -t -long devel/sage/sage/rings/real_lazy.pyx           
**********************************************************************
File "/Users/mabshoff/sage-3.1.3.rc0/tmp/real_lazy.py", line 549:
    sage: complex(CLF(-1)^(1/4))
Expected:
    (0.70710678118654757+0.70710678118654746j)
Got:
    (0.70710678118654746+0.70710678118654757j)
**********************************************************************
```




---

archive/issue_comments_031303.json:
```json
{
    "body": "Attachment [trac_4279.patch](tarball://root/attachments/some-uuid/ticket4279/trac_4279.patch) by mabshoff created at 2008-10-14 11:57:19",
    "created_at": "2008-10-14T11:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4279#issuecomment-31303",
    "user": "mabshoff"
}
```

Attachment [trac_4279.patch](tarball://root/attachments/some-uuid/ticket4279/trac_4279.patch) by mabshoff created at 2008-10-14 11:57:19



---

archive/issue_comments_031304.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-10-14T11:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4279#issuecomment-31304",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_031305.json:
```json
{
    "body": "Merged in 3.1.3.final",
    "created_at": "2008-10-14T12:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4279#issuecomment-31305",
    "user": "mabshoff"
}
```

Merged in 3.1.3.final



---

archive/issue_comments_031306.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-14T12:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4279",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4279#issuecomment-31306",
    "user": "mabshoff"
}
```

Resolution: fixed
