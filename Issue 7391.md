# Issue 7391: Warn the user of incorrect results when an approximate ill-conditioned matrix is used

archive/issues_007391.json:
```json
{
    "body": "Assignee: was\n\nThis should probably give a warning to the user that the matrix is ill-conditioned and you may get wrong results (like you do in this case).\n\n\n```\nsage: n = matrix([ [-0.3, 0.2, 0.1],\n                    [0.2, -0.4, 0.4],\n                    [0.1, 0.2, -0.5] ])\n\nsage: n.echelon_form()\n\n[ 1.00000000000000 0.000000000000000 0.000000000000000]\n[0.000000000000000  1.00000000000000 0.000000000000000]\n[0.000000000000000 0.000000000000000  1.00000000000000]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7391\n\n",
    "created_at": "2009-11-04T21:36:06Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "Warn the user of incorrect results when an approximate ill-conditioned matrix is used",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7391",
    "user": "jason"
}
```
Assignee: was

This should probably give a warning to the user that the matrix is ill-conditioned and you may get wrong results (like you do in this case).


```
sage: n = matrix([ [-0.3, 0.2, 0.1],
                    [0.2, -0.4, 0.4],
                    [0.1, 0.2, -0.5] ])

sage: n.echelon_form()

[ 1.00000000000000 0.000000000000000 0.000000000000000]
[0.000000000000000  1.00000000000000 0.000000000000000]
[0.000000000000000 0.000000000000000  1.00000000000000]

```


Issue created by migration from https://trac.sagemath.org/ticket/7391





---

archive/issue_comments_062168.json:
```json
{
    "body": "FYI: \n\n\n```\nsage: m.change_ring(RDF).SVD()[1]\n\n[   0.772642968023               0.0               0.0]\n[              0.0    0.450580563234               0.0]\n[              0.0               0.0 3.13289758759e-17]\n```\n",
    "created_at": "2009-11-04T21:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7391#issuecomment-62168",
    "user": "jason"
}
```

FYI: 


```
sage: m.change_ring(RDF).SVD()[1]

[   0.772642968023               0.0               0.0]
[              0.0    0.450580563234               0.0]
[              0.0               0.0 3.13289758759e-17]
```




---

archive/issue_comments_062169.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7391",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7391#issuecomment-62169",
    "user": "jason"
}
```

Changing type from defect to enhancement.
