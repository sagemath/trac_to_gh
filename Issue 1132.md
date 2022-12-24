# Issue 1132: error inverting matrix over RQDF

archive/issues_001132.json:
```json
{
    "body": "Assignee: @williamstein\n\nI've attached b.sobj which you can load to reproduce the error.\n\n\n```\nsage: ~b\n---------------------------------------------------------------------------\n<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)\n\n/home/mike/<ipython console> in <module>()\n\n/home/mike/matrix0.pyx in sage.matrix.matrix0.Matrix.__invert__()\n\n<type 'exceptions.ZeroDivisionError'>: self is not invertible\nsage: c = b.change_ring(RDF)\nsage: ~c\n\n[ 0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778]\n[  0.111111111111  -0.111111111111  0.0555555555556 -0.0555555555556  0.0555555555556 -0.0555555555556]\n[             0.0              0.0  0.0962250448649  0.0962250448649 -0.0962250448649 -0.0962250448649]\n[            -0.0             -0.0  0.0962250448649 -0.0962250448649 -0.0962250448649  0.0962250448649]\n[  0.111111111111   0.111111111111 -0.0555555555556 -0.0555555555556 -0.0555555555556 -0.0555555555556]\n[ 0.0277777777778 -0.0277777777778 -0.0277777777778  0.0277777777778 -0.0277777777778  0.0277777777778]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1132\n\n",
    "created_at": "2007-11-09T03:51:57Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "error inverting matrix over RQDF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1132",
    "user": "@mwhansen"
}
```
Assignee: @williamstein

I've attached b.sobj which you can load to reproduce the error.


```
sage: ~b
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/home/mike/<ipython console> in <module>()

/home/mike/matrix0.pyx in sage.matrix.matrix0.Matrix.__invert__()

<type 'exceptions.ZeroDivisionError'>: self is not invertible
sage: c = b.change_ring(RDF)
sage: ~c

[ 0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778  0.0277777777778]
[  0.111111111111  -0.111111111111  0.0555555555556 -0.0555555555556  0.0555555555556 -0.0555555555556]
[             0.0              0.0  0.0962250448649  0.0962250448649 -0.0962250448649 -0.0962250448649]
[            -0.0             -0.0  0.0962250448649 -0.0962250448649 -0.0962250448649  0.0962250448649]
[  0.111111111111   0.111111111111 -0.0555555555556 -0.0555555555556 -0.0555555555556 -0.0555555555556]
[ 0.0277777777778 -0.0277777777778 -0.0277777777778  0.0277777777778 -0.0277777777778  0.0277777777778]

```


Issue created by migration from https://trac.sagemath.org/ticket/1132





---

archive/issue_comments_006862.json:
```json
{
    "body": "Attachment [b.sobj](tarball://root/attachments/some-uuid/ticket1132/b.sobj) by mabshoff created at 2007-12-18 09:12:28",
    "created_at": "2007-12-18T09:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1132#issuecomment-6862",
    "user": "mabshoff"
}
```

Attachment [b.sobj](tarball://root/attachments/some-uuid/ticket1132/b.sobj) by mabshoff created at 2007-12-18 09:12:28



---

archive/issue_comments_006863.json:
```json
{
    "body": "This is due to the following:\n\n\n```\nsage: b = load('/home/mike/Desktop/b.sobj')\nsage: A = b.augment(b.parent().identity_matrix())\nsage: B = A.echelon_form()\nsage: B[5,5]\n1.000000000000000000000000000000000000000000000000000000000000000\nsage: B[5,5] == 1\nFalse\n```\n",
    "created_at": "2007-12-22T17:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1132#issuecomment-6863",
    "user": "@mwhansen"
}
```

This is due to the following:


```
sage: b = load('/home/mike/Desktop/b.sobj')
sage: A = b.augment(b.parent().identity_matrix())
sage: B = A.echelon_form()
sage: B[5,5]
1.000000000000000000000000000000000000000000000000000000000000000
sage: B[5,5] == 1
False
```




---

archive/issue_comments_006864.json:
```json
{
    "body": "This ought to be solved. Maybe it is fodder fir Bug Day 8.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-29T17:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1132#issuecomment-6864",
    "user": "mabshoff"
}
```

This ought to be solved. Maybe it is fodder fir Bug Day 8.

Cheers,

Michael



---

archive/issue_comments_006865.json:
```json
{
    "body": "Wontfix since we will remove RQDF - see #3762.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T05:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1132#issuecomment-6865",
    "user": "mabshoff"
}
```

Wontfix since we will remove RQDF - see #3762.

Cheers,

Michael



---

archive/issue_comments_006866.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-11-14T05:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1132#issuecomment-6866",
    "user": "mabshoff"
}
```

Resolution: wontfix
