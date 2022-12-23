# Issue 4431: [with patch, needs review] conversion of maxima matrices to sage matrices

archive/issues_004431.json:
```json
{
    "body": "Assignee: whuss\n\nThis patch implements conversion of Maxima matrices, to Sage matrices. The patch is based on\nsage-3.2alpha1.\n\nA sample session:\n\n```\nsage: var('x,y')\nsage: v = maxima('v: vandermonde_matrix([x, y, 1/2])')\nsage: v\nmatrix([1,x,x^2],[1,y,y^2],[1,1/2,1/4])\nsage: type(v)\n<class 'sage.interfaces.maxima.MaximaElement'>\nsage: v.sage()\n\n[  1   x x^2]\n[  1   y y^2]\n[  1 1/2 1/4]\nsage: mlist = maxima('[v, sin(x), 1, v.v]').sage()\nsage: mlist\n\n[[  1   x x^2]\n[  1   y y^2]\n[  1 1/2 1/4],\n    sin(x),\n    1,\n    [       x^2 + x + 1    x*y + x^2/2 + x    x*y^2 + 5*x^2/4]\n[       y^2 + y + 1        3*y^2/2 + x  y^3 + y^2/4 + x^2]\n[               7/4      y/2 + x + 1/8 y^2/2 + x^2 + 1/16]]\nsage: [parent(i) for i in mlist]\n\n[Full MatrixSpace of 3 by 3 dense matrices over Symbolic Ring,\n    Symbolic Ring,\n    Symbolic Ring,\n    Full MatrixSpace of 3 by 3 dense matrices over Symbolic Ring]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4431\n\n",
    "created_at": "2008-11-03T19:37:18Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] conversion of maxima matrices to sage matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4431",
    "user": "whuss"
}
```
Assignee: whuss

This patch implements conversion of Maxima matrices, to Sage matrices. The patch is based on
sage-3.2alpha1.

A sample session:

```
sage: var('x,y')
sage: v = maxima('v: vandermonde_matrix([x, y, 1/2])')
sage: v
matrix([1,x,x^2],[1,y,y^2],[1,1/2,1/4])
sage: type(v)
<class 'sage.interfaces.maxima.MaximaElement'>
sage: v.sage()

[  1   x x^2]
[  1   y y^2]
[  1 1/2 1/4]
sage: mlist = maxima('[v, sin(x), 1, v.v]').sage()
sage: mlist

[[  1   x x^2]
[  1   y y^2]
[  1 1/2 1/4],
    sin(x),
    1,
    [       x^2 + x + 1    x*y + x^2/2 + x    x*y^2 + 5*x^2/4]
[       y^2 + y + 1        3*y^2/2 + x  y^3 + y^2/4 + x^2]
[               7/4      y/2 + x + 1/8 y^2/2 + x^2 + 1/16]]
sage: [parent(i) for i in mlist]

[Full MatrixSpace of 3 by 3 dense matrices over Symbolic Ring,
    Symbolic Ring,
    Symbolic Ring,
    Full MatrixSpace of 3 by 3 dense matrices over Symbolic Ring]
```



Issue created by migration from https://trac.sagemath.org/ticket/4431





---

archive/issue_comments_032557.json:
```json
{
    "body": "This patch looks good, but you should add the Vandermonde matrix as a test / example in the appropriate spot.  Also, I think the following construction is a bit cleaner than the string one:\n\n\n```\nsage: v = maxima.vandermonde_matrix([x,y,1/2])\n```\n",
    "created_at": "2008-11-04T20:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4431#issuecomment-32557",
    "user": "mhansen"
}
```

This patch looks good, but you should add the Vandermonde matrix as a test / example in the appropriate spot.  Also, I think the following construction is a bit cleaner than the string one:


```
sage: v = maxima.vandermonde_matrix([x,y,1/2])
```




---

archive/issue_comments_032558.json:
```json
{
    "body": "Attachment\n\nI updated the patch with some doctests.",
    "created_at": "2008-11-05T15:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4431#issuecomment-32558",
    "user": "whuss"
}
```

Attachment

I updated the patch with some doctests.



---

archive/issue_comments_032559.json:
```json
{
    "body": "I pinged mhansen to look at this.  He should finish the review instead of this bitrotting.",
    "created_at": "2008-11-27T18:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4431#issuecomment-32559",
    "user": "was"
}
```

I pinged mhansen to look at this.  He should finish the review instead of this bitrotting.



---

archive/issue_comments_032560.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2008-11-27T18:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4431#issuecomment-32560",
    "user": "mhansen"
}
```

Looks fine to me.



---

archive/issue_comments_032561.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0\n\nSince this is a diff I checked in the changes in Wilfried's name.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T07:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4431#issuecomment-32561",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc0

Since this is a diff I checked in the changes in Wilfried's name.

Cheers,

Michael



---

archive/issue_comments_032562.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T07:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4431",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4431#issuecomment-32562",
    "user": "mabshoff"
}
```

Resolution: fixed
