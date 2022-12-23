# Issue 4503: numerical noise in matrix_double_dense on intel mac os X 10.5: SVD

archive/issues_004503.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  jason\n\nKeywords: numerical noise, matrix\n\n(This has only been reported on intel macs running 10.4 or 10.5.)\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/fae59a9a9a53b8c0):\n\n\n```\nsage: m = matrix(RDF,3,2,range(6)); m\n\n[0.0 1.0]\n[2.0 3.0]\n[4.0 5.0]\nsage: U,S,V = m.SVD()\nsage: U*S*V.transpose()   # random low order bits\n\n[0.0 1.0]\n[2.0 3.0]\n[4.0 5.0]\n\nmax((U*S*V.transpose()-m).list())\n1.7763568394e-15 \n```\n\n\nThis leads to a doctest failure for `matrix_double_dense.py`.\n\nJason Grout suggests:\n\n```\nOkay, apparently the doctest just needs a looser bound; what you get is\nstill within reason for numerical issues.  Currently we see if that\nmaximum is < 1e-15.  Changing it to 1e-14 should fix this.\n```\n\n \n\nIssue created by migration from https://trac.sagemath.org/ticket/4503\n\n",
    "created_at": "2008-11-12T17:59:39Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "numerical noise in matrix_double_dense on intel mac os X 10.5: SVD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4503",
    "user": "jhpalmieri"
}
```
Assignee: somebody

CC:  jason

Keywords: numerical noise, matrix

(This has only been reported on intel macs running 10.4 or 10.5.)

From [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/fae59a9a9a53b8c0):


```
sage: m = matrix(RDF,3,2,range(6)); m

[0.0 1.0]
[2.0 3.0]
[4.0 5.0]
sage: U,S,V = m.SVD()
sage: U*S*V.transpose()   # random low order bits

[0.0 1.0]
[2.0 3.0]
[4.0 5.0]

max((U*S*V.transpose()-m).list())
1.7763568394e-15 
```


This leads to a doctest failure for `matrix_double_dense.py`.

Jason Grout suggests:

```
Okay, apparently the doctest just needs a looser bound; what you get is
still within reason for numerical issues.  Currently we see if that
maximum is < 1e-15.  Changing it to 1e-14 should fix this.
```

 

Issue created by migration from https://trac.sagemath.org/ticket/4503





---

archive/issue_comments_033368.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-11-13T03:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4503#issuecomment-33368",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_033369.json:
```json
{
    "body": "Here's a patch changing the doctest.  This fixes the problem on my mac.",
    "created_at": "2008-11-13T03:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4503#issuecomment-33369",
    "user": "jhpalmieri"
}
```

Here's a patch changing the doctest.  This fixes the problem on my mac.



---

archive/issue_comments_033370.json:
```json
{
    "body": "Positive review. Hopefully this will fix the dreaded numerical noise issue once and for all.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T04:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4503#issuecomment-33370",
    "user": "mabshoff"
}
```

Positive review. Hopefully this will fix the dreaded numerical noise issue once and for all.

Cheers,

Michael



---

archive/issue_comments_033371.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-14T17:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4503#issuecomment-33371",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc1



---

archive/issue_comments_033372.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T17:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4503#issuecomment-33372",
    "user": "mabshoff"
}
```

Resolution: fixed
