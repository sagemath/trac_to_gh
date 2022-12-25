# Issue 4772: [with patch; positive review] make determinants of matrices over GF(2) way faster

archive/issues_004772.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is sad:\n\n```\nwas@sage:~/build/sage-3.2.2.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: w = random_matrix(GF(2),100)\nsage: time w.determinant()\nCPU times: user 0.18 s, sys: 0.00 s, total: 0.18 s\nWall time: 0.19 s\n0\nsage: w = random_matrix(GF(3),100)\nsage: time w.determinant()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\n0\n```\n| Sage Version 3.2.2.alpha1, Release Date: 2008-12-10                |\n| Type notebook() for the GUI, and license() for information.        |\nThe fix - just compute the rank of the matrix, and if it is less than the nrows, then det is 0.  Otherwise det is 1.  Easy.  Right now, stupid generic code is being used. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4772\n\n",
    "closed_at": "2008-12-13T09:07:36Z",
    "created_at": "2008-12-12T19:26:24Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch; positive review] make determinants of matrices over GF(2) way faster",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4772",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is sad:

```
was@sage:~/build/sage-3.2.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: w = random_matrix(GF(2),100)
sage: time w.determinant()
CPU times: user 0.18 s, sys: 0.00 s, total: 0.18 s
Wall time: 0.19 s
0
sage: w = random_matrix(GF(3),100)
sage: time w.determinant()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
0
```
| Sage Version 3.2.2.alpha1, Release Date: 2008-12-10                |
| Type notebook() for the GUI, and license() for information.        |
The fix - just compute the rank of the matrix, and if it is less than the nrows, then det is 0.  Otherwise det is 1.  Easy.  Right now, stupid generic code is being used. 

Issue created by migration from https://trac.sagemath.org/ticket/4772





---

archive/issue_comments_036073.json:
```json
{
    "body": "BEFORE:\n\n```\nsage: w = random_matrix(GF(2),1000)\nsage: time w.determinant()\nCPU times: user 174.27 s, sys: 0.01 s, total: 174.29 s\nWall time: 174.30 s\n0\n```\n\nAFTER:\n\n```\nsage: w = random_matrix(GF(2),1000)\nsage: timeit('w._clear_cache(); w.determinant()')\n125 loops, best of 3: 5.48 ms per loop\n```\n\nFor a speedup of a factor of a factor of over THIRTY THOUSAND (!):\n\n```\nsage: 174/(5.48*10^(-3))\n31751.8248175182\n```",
    "created_at": "2008-12-12T19:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4772#issuecomment-36073",
    "user": "https://github.com/williamstein"
}
```

BEFORE:

```
sage: w = random_matrix(GF(2),1000)
sage: time w.determinant()
CPU times: user 174.27 s, sys: 0.01 s, total: 174.29 s
Wall time: 174.30 s
0
```

AFTER:

```
sage: w = random_matrix(GF(2),1000)
sage: timeit('w._clear_cache(); w.determinant()')
125 loops, best of 3: 5.48 ms per loop
```

For a speedup of a factor of a factor of over THIRTY THOUSAND (!):

```
sage: 174/(5.48*10^(-3))
31751.8248175182
```



---

archive/issue_comments_036074.json:
```json
{
    "body": "Attachment [trac_4772.patch](tarball://root/attachments/some-uuid/ticket4772/trac_4772.patch) by @jasongrout created at 2008-12-12 21:20:57\n\nVery nice speedup!  Positive review.  Doctests pass in the file.",
    "created_at": "2008-12-12T21:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4772#issuecomment-36074",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_4772.patch](tarball://root/attachments/some-uuid/ticket4772/trac_4772.patch) by @jasongrout created at 2008-12-12 21:20:57

Very nice speedup!  Positive review.  Doctests pass in the file.



---

archive/issue_comments_036075.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-13T09:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4772#issuecomment-36075",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha2



---

archive/issue_comments_036076.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-13T09:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4772#issuecomment-36076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010902.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-13T09:07:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4772",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4772#event-10902"
}
```
