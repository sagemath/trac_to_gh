# Issue 6383: implement additive_order for points on an elliptic curve

archive/issues_006383.json:
```json
{
    "body": "Assignee: was\n\nThis should work:\n\n\n```\nsage: E = EllipticCurve('11a'); P = E.torsion_subgroup().gens()[0]; P\n(5 : 5 : 1)\nsage: P.additive_order()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/resid_tg105.upc.es/5930/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.additive_order (sage/structure/element.c:8113)()\n\nNotImplementedError: \nsage: P.order()\n5\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6383\n\n",
    "created_at": "2009-06-21T23:39:37Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "implement additive_order for points on an elliptic curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6383",
    "user": "was"
}
```
Assignee: was

This should work:


```
sage: E = EllipticCurve('11a'); P = E.torsion_subgroup().gens()[0]; P
(5 : 5 : 1)
sage: P.additive_order()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/Users/wstein/.sage/temp/resid_tg105.upc.es/5930/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.additive_order (sage/structure/element.c:8113)()

NotImplementedError: 
sage: P.order()
5
```


Issue created by migration from https://trac.sagemath.org/ticket/6383





---

archive/issue_comments_051094.json:
```json
{
    "body": "This seems to be a duplicate of #6382.",
    "created_at": "2009-06-27T07:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6383#issuecomment-51094",
    "user": "davidloeffler"
}
```

This seems to be a duplicate of #6382.



---

archive/issue_comments_051095.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-07-08T20:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6383#issuecomment-51095",
    "user": "rlm"
}
```

Resolution: duplicate
