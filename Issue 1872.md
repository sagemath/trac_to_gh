# Issue 1872: serious bug in pickling elliptic curves

archive/issues_001872.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: E = EllipticCurve('185c1')\nsage: E.gens()\n[(-5/4 : 3/8 : 1)]\nsage: loads(dumps(E))\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/<ipython console> in <module>()\n\n/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/sage_object.pyx in sage.structure.sage_object.loads()\n\n/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/sage_object.pyx in sage.structure.sage_object.loads()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in make_point(X, v)\n    648     # It looks like there's generic code to do this, but it's been commented out. \n    649     #\n    650     # Here we create a new (equivalent) parent manually. \n--> 651     del X._Scheme__ring_point_homset\n    652     return EllipticCurvePoint_field(X, v)\n\n<type 'str'>: (<type 'exceptions.AttributeError'>, AttributeError(\"'EllipticCurve_rational_field' object has no attribute '_EllipticCurve_generic__ainvs'\",))\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1872\n\n",
    "created_at": "2008-01-20T22:22:44Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "serious bug in pickling elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1872",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: E = EllipticCurve('185c1')
sage: E.gens()
[(-5/4 : 3/8 : 1)]
sage: loads(dumps(E))
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/<ipython console> in <module>()

/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/sage_object.pyx in sage.structure.sage_object.loads()

/Users/was/papers/bsdalg/newdata/heegner_index_rank1/data/sage_object.pyx in sage.structure.sage_object.loads()

/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_point.py in make_point(X, v)
    648     # It looks like there's generic code to do this, but it's been commented out. 
    649     #
    650     # Here we create a new (equivalent) parent manually. 
--> 651     del X._Scheme__ring_point_homset
    652     return EllipticCurvePoint_field(X, v)

<type 'str'>: (<type 'exceptions.AttributeError'>, AttributeError("'EllipticCurve_rational_field' object has no attribute '_EllipticCurve_generic__ainvs'",))

```


Issue created by migration from https://trac.sagemath.org/ticket/1872





---

archive/issue_comments_011857.json:
```json
{
    "body": "Attachment [trac-1872.patch](tarball://root/attachments/some-uuid/ticket1872/trac-1872.patch) by @williamstein created at 2008-01-21 06:33:37\n\nthis fixes the problem",
    "created_at": "2008-01-21T06:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1872#issuecomment-11857",
    "user": "@williamstein"
}
```

Attachment [trac-1872.patch](tarball://root/attachments/some-uuid/ticket1872/trac-1872.patch) by @williamstein created at 2008-01-21 06:33:37

this fixes the problem



---

archive/issue_comments_011858.json:
```json
{
    "body": "The patch simply deletes some functions, deletes some commented out code, and names a variable something meaningful instead of meaningless.",
    "created_at": "2008-01-21T06:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1872#issuecomment-11858",
    "user": "@williamstein"
}
```

The patch simply deletes some functions, deletes some commented out code, and names a variable something meaningful instead of meaningless.



---

archive/issue_comments_011859.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T09:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1872#issuecomment-11859",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011860.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-21T09:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1872",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1872#issuecomment-11860",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0
