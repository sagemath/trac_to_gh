# Issue 3788: [with patch, needs review] many matrix_dense_modn operations are unreasonably slow

archive/issues_003788.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is because they use the generic algorithms (extracting each element as a Python object). \n\nSee discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/dae70440d7fd41\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3788\n\n",
    "created_at": "2008-08-07T10:04:21Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] many matrix_dense_modn operations are unreasonably slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3788",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

This is because they use the generic algorithms (extracting each element as a Python object). 

See discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/dae70440d7fd41



Issue created by migration from https://trac.sagemath.org/ticket/3788





---

archive/issue_comments_026878.json:
```json
{
    "body": "Hi Robert,\n\nEverything looks good except I got one little doctest failure:\n\n\n```\nFile \"/opt/sage/tmp/matrix_modn_dense.py\", line 204:\n    sage: matrix(GF(7), 2, 2, [-1, int(-2), GF(7)(-3), 1/4])\nExpected:\n    [6 2]\n    [4 2]\nGot:\n    [6 0]\n    [4 2]\n```\n\n\nShouldn't int(-2) go to 5 instead of either 2 or 0?",
    "created_at": "2008-08-07T16:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26878",
    "user": "https://github.com/mwhansen"
}
```

Hi Robert,

Everything looks good except I got one little doctest failure:


```
File "/opt/sage/tmp/matrix_modn_dense.py", line 204:
    sage: matrix(GF(7), 2, 2, [-1, int(-2), GF(7)(-3), 1/4])
Expected:
    [6 2]
    [4 2]
Got:
    [6 0]
    [4 2]
```


Shouldn't int(-2) go to 5 instead of either 2 or 0?



---

archive/issue_comments_026879.json:
```json
{
    "body": "Attachment [3788-matrix-modn.patch](tarball://root/attachments/some-uuid/ticket3788/3788-matrix-modn.patch) by @robertwb created at 2008-08-07 17:01:40",
    "created_at": "2008-08-07T17:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26879",
    "user": "https://github.com/robertwb"
}
```

Attachment [3788-matrix-modn.patch](tarball://root/attachments/some-uuid/ticket3788/3788-matrix-modn.patch) by @robertwb created at 2008-08-07 17:01:40



---

archive/issue_comments_026880.json:
```json
{
    "body": "That change to `mod_int` being unsigned bites again, and when I changed the doctest to test a negative int, coincidentally the output was the same (should have caught that nonetheless)--glad it was different for you. \n\nThe patch has been updated.",
    "created_at": "2008-08-07T17:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26880",
    "user": "https://github.com/robertwb"
}
```

That change to `mod_int` being unsigned bites again, and when I changed the doctest to test a negative int, coincidentally the output was the same (should have caught that nonetheless)--glad it was different for you. 

The patch has been updated.



---

archive/issue_comments_026881.json:
```json
{
    "body": "With the new patch, I get these failures:\n\n\n```\nsage -t  devel/sage-work/sage/matrix/matrix_modn_dense.pyx  **********************************************************************\nFile \"/opt/sage/tmp/matrix_modn_dense.py\", line 26:\n    sage: a^2\nExpected:\n    [ 3 23 31]\n    [20 17 29]\n    [25 16  0]\nGot:\n    [ 0 23 31]\n    [ 0 17 29]\n    [ 0 16  0]\n**********************************************************************\nFile \"/opt/sage/tmp/matrix_modn_dense.py\", line 42:\n    sage: b*a\nExpected:\n    [15 18 21]\n    [20 17 29]\nGot:\n    [ 0 18 21]\n    [ 0 17 29]\n**********************************************************************\n```\n",
    "created_at": "2008-08-07T17:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26881",
    "user": "https://github.com/mwhansen"
}
```

With the new patch, I get these failures:


```
sage -t  devel/sage-work/sage/matrix/matrix_modn_dense.pyx  **********************************************************************
File "/opt/sage/tmp/matrix_modn_dense.py", line 26:
    sage: a^2
Expected:
    [ 3 23 31]
    [20 17 29]
    [25 16  0]
Got:
    [ 0 23 31]
    [ 0 17 29]
    [ 0 16  0]
**********************************************************************
File "/opt/sage/tmp/matrix_modn_dense.py", line 42:
    sage: b*a
Expected:
    [15 18 21]
    [20 17 29]
Got:
    [ 0 18 21]
    [ 0 17 29]
**********************************************************************
```




---

archive/issue_comments_026882.json:
```json
{
    "body": "???\n\nMe too--no idea why that just changed, it used to work and I thought I only touched a couple of lines. Now I wish I had made a new patch instead of qrefresh. I'll look at this.",
    "created_at": "2008-08-07T17:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26882",
    "user": "https://github.com/robertwb"
}
```

???

Me too--no idea why that just changed, it used to work and I thought I only touched a couple of lines. Now I wish I had made a new patch instead of qrefresh. I'll look at this.



---

archive/issue_comments_026883.json:
```json
{
    "body": "Attachment [3788-matrix-modn.2.patch](tarball://root/attachments/some-uuid/ticket3788/3788-matrix-modn.2.patch) by @robertwb created at 2008-08-08 02:44:40\n\nThere was certainly a bug, but not in the code I touched so I don't know why it suddenly showed up now. I've fixed it, it should be working find again.",
    "created_at": "2008-08-08T02:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26883",
    "user": "https://github.com/robertwb"
}
```

Attachment [3788-matrix-modn.2.patch](tarball://root/attachments/some-uuid/ticket3788/3788-matrix-modn.2.patch) by @robertwb created at 2008-08-08 02:44:40

There was certainly a bug, but not in the code I touched so I don't know why it suddenly showed up now. I've fixed it, it should be working find again.



---

archive/issue_comments_026884.json:
```json
{
    "body": "Attachment [3788.patch](tarball://root/attachments/some-uuid/ticket3788/3788.patch) by @mwhansen created at 2008-08-08 06:23:54",
    "created_at": "2008-08-08T06:23:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26884",
    "user": "https://github.com/mwhansen"
}
```

Attachment [3788.patch](tarball://root/attachments/some-uuid/ticket3788/3788.patch) by @mwhansen created at 2008-08-08 06:23:54



---

archive/issue_comments_026885.json:
```json
{
    "body": "Apply only 3788.patch",
    "created_at": "2008-08-08T06:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26885",
    "user": "https://github.com/mwhansen"
}
```

Apply only 3788.patch



---

archive/issue_comments_026886.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-08T23:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026887.json:
```json
{
    "body": "Merged 3788.patch in Sage 3.1.alpha1",
    "created_at": "2008-08-08T23:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3788#issuecomment-26887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3788.patch in Sage 3.1.alpha1
