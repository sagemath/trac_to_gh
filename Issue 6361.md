# Issue 6361: elliptic curves -- easy to fix mistake in docs

archive/issues_006361.json:
```json
{
    "body": "Assignee: was\n\n\n```\neval_modular_form(points, prec) \nEvaluate the L-series of this elliptic curve at points in CC \nINPUT: \n\u2022points - a list of points in the half-plane of convergence \n\u2022prec - precision \nOUTPUT: A list of values L(E,s) for s in points \nNote: Better examples are welcome. \nEXAMPLES: \nsage: E=EllipticCurve(\u201937a1\u2019) \nsage: E.eval_modular_form([1.5+I,2.0+I,2.5+I],0.000001) \n[0, 0, 0] \n```\n\n\nIt should *NOT* say L-series above.  It should say modular form.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6361\n\n",
    "created_at": "2009-06-19T18:02:44Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "elliptic curves -- easy to fix mistake in docs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6361",
    "user": "was"
}
```
Assignee: was


```
eval_modular_form(points, prec) 
Evaluate the L-series of this elliptic curve at points in CC 
INPUT: 
•points - a list of points in the half-plane of convergence 
•prec - precision 
OUTPUT: A list of values L(E,s) for s in points 
Note: Better examples are welcome. 
EXAMPLES: 
sage: E=EllipticCurve(’37a1’) 
sage: E.eval_modular_form([1.5+I,2.0+I,2.5+I],0.000001) 
[0, 0, 0] 
```


It should *NOT* say L-series above.  It should say modular form.

Issue created by migration from https://trac.sagemath.org/ticket/6361





---

archive/issue_comments_050874.json:
```json
{
    "body": "Attachment\n\nbased on Sage 4.0.2",
    "created_at": "2009-06-19T22:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6361#issuecomment-50874",
    "user": "mvngu"
}
```

Attachment

based on Sage 4.0.2



---

archive/issue_comments_050875.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-06-20T00:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6361#issuecomment-50875",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_050876.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6361#issuecomment-50876",
    "user": "rlm"
}
```

Resolution: fixed
