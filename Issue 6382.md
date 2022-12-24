# Issue 6382: implement additive_order for points on an elliptic curve

archive/issues_006382.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mwhansen mvngu\n\nThis should work:\n\n\n```\nsage: E = EllipticCurve('11a'); P = E.torsion_subgroup().gens()[0]; P\n(5 : 5 : 1)\nsage: P.additive_order()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/resid_tg105.upc.es/5930/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.additive_order (sage/structure/element.c:8113)()\n\nNotImplementedError: \nsage: P.order()\n5\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6382\n\n",
    "created_at": "2009-06-21T23:39:34Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "implement additive_order for points on an elliptic curve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6382",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @mwhansen mvngu

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


Issue created by migration from https://trac.sagemath.org/ticket/6382





---

archive/issue_comments_051088.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6382#issuecomment-51088",
    "user": "@loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_051089.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6382#issuecomment-51089",
    "user": "@loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_051090.json:
```json
{
    "body": "This is a duplicate of #3108 whic hhas a patch waiting review.  This ticket can terefore be closed.",
    "created_at": "2009-07-25T17:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6382#issuecomment-51090",
    "user": "@JohnCremona"
}
```

This is a duplicate of #3108 whic hhas a patch waiting review.  This ticket can terefore be closed.



---

archive/issue_comments_051091.json:
```json
{
    "body": "Please note the request to close this.",
    "created_at": "2009-10-06T19:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6382#issuecomment-51091",
    "user": "@jasongrout"
}
```

Please note the request to close this.



---

archive/issue_comments_051092.json:
```json
{
    "body": "Duplicate of #3108.",
    "created_at": "2009-10-07T04:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6382#issuecomment-51092",
    "user": "@mwhansen"
}
```

Duplicate of #3108.



---

archive/issue_comments_051093.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-07T04:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6382#issuecomment-51093",
    "user": "@mwhansen"
}
```

Resolution: duplicate
