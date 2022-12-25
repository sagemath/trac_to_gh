# Issue 3058: coercing a vector to symbolic entries doesn't work when the vector's parent has a user-defined basis

archive/issues_003058.json:
```json
{
    "body": "Assignee: @robertwb\n\nThe title is what I think is the real issue here:\n\n```\nsage: a=(QQ3).subspace([[1,0,1]])\nsage: b=a.basis()[0]\nsage: b/b.norm()\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\n/home/grout/element.pyx in sage.structure.element.Vector.__div__ \n(sage/structure/element.c:10962)()\n\n/home/grout/element.pyx in sage.structure.element.Vector.__mul__ \n(sage/structure/element.c:10413)()\n\n/home/grout/coerce.pyx in \nsage.structure.coerce.CoercionModel_cache_maps.bin_op_c \n(sage/structure/coerce.c:5292)()\n\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': \n'Vector space of degree 3 and dimension 1 over Rational Field\nBasis matrix:\n[1 0 1]' and 'Symbolic Ring'\n```\n\n\nNote that the following does work:\n\n```\nsage: b=vector(QQ,[1,0,1])\nsage: b/b.norm()\n(1/sqrt(2), 0, 1/sqrt(2))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3058\n\n",
    "closed_at": "2009-06-04T23:05:06Z",
    "created_at": "2008-04-29T23:37:30Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "coercing a vector to symbolic entries doesn't work when the vector's parent has a user-defined basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3058",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @robertwb

The title is what I think is the real issue here:

```
sage: a=(QQ3).subspace([[1,0,1]])
sage: b=a.basis()[0]
sage: b/b.norm()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/element.pyx in sage.structure.element.Vector.__div__ 
(sage/structure/element.c:10962)()

/home/grout/element.pyx in sage.structure.element.Vector.__mul__ 
(sage/structure/element.c:10413)()

/home/grout/coerce.pyx in 
sage.structure.coerce.CoercionModel_cache_maps.bin_op_c 
(sage/structure/coerce.c:5292)()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 
'Vector space of degree 3 and dimension 1 over Rational Field
Basis matrix:
[1 0 1]' and 'Symbolic Ring'
```


Note that the following does work:

```
sage: b=vector(QQ,[1,0,1])
sage: b/b.norm()
(1/sqrt(2), 0, 1/sqrt(2))
```


Issue created by migration from https://trac.sagemath.org/ticket/3058





---

archive/issue_comments_021071.json:
```json
{
    "body": "This seems fixed now (in 3.2.1).  However there are other similar issues, like:\n\n```\nsage: a=(QQ^3).subspace([[1,0,1]])\nsage: b=a.basis()[0]\nsage: b/b.norm()\n(1/sqrt(2), 0, 1/sqrt(2))\nsage: b-b/b.norm()\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__sub__ (sage/structure/element.c:6073)()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5805)()\n\nTypeError: unsupported operand parent(s) for '-': 'Vector space of degree 3 and dimension 1 over Rational Field\nBasis matrix:\n[1 0 1]' and 'Vector space of degree 3 and dimension 1 over Symbolic Ring\nUser basis matrix:\n[1 0 1]'\n```",
    "created_at": "2008-12-19T18:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3058#issuecomment-21071",
    "user": "https://github.com/jasongrout"
}
```

This seems fixed now (in 3.2.1).  However there are other similar issues, like:

```
sage: a=(QQ^3).subspace([[1,0,1]])
sage: b=a.basis()[0]
sage: b/b.norm()
(1/sqrt(2), 0, 1/sqrt(2))
sage: b-b/b.norm()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__sub__ (sage/structure/element.c:6073)()

/home/grout/sage/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5805)()

TypeError: unsupported operand parent(s) for '-': 'Vector space of degree 3 and dimension 1 over Rational Field
Basis matrix:
[1 0 1]' and 'Vector space of degree 3 and dimension 1 over Symbolic Ring
User basis matrix:
[1 0 1]'
```



---

archive/issue_comments_021072.json:
```json
{
    "body": "It also seems like the operation above takes *way* too long:\n\n```\nsage: %time b/b.norm()  \nCPU times: user 0.48 s, sys: 0.14 s, total: 0.62 s\nWall time: 2.02 s\n(1/sqrt(2), 0, 1/sqrt(2))\nsage: %time b.norm()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsqrt(2)\n```",
    "created_at": "2008-12-19T18:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3058#issuecomment-21072",
    "user": "https://github.com/jasongrout"
}
```

It also seems like the operation above takes *way* too long:

```
sage: %time b/b.norm()  
CPU times: user 0.48 s, sys: 0.14 s, total: 0.62 s
Wall time: 2.02 s
(1/sqrt(2), 0, 1/sqrt(2))
sage: %time b.norm()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sqrt(2)
```



---

archive/issue_comments_021073.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-04T23:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3058#issuecomment-21073",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_006926.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T23:05:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3058",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3058#event-6926"
}
```



---

archive/issue_comments_021074.json:
```json
{
    "body": "This looks good with 4.0.1.rc1:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: a=(QQ^3).subspace([[1,0,1]])\nsage: sage: b=a.basis()[0]\nsage: %time b/b.norm()\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01 s\n(1/2*sqrt(2), 0, 1/2*sqrt(2))\nsage: b-b/b.norm()\n(-1/2*sqrt(2) + 1, 0, -1/2*sqrt(2) + 1)\n```",
    "created_at": "2009-06-04T23:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3058",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3058#issuecomment-21074",
    "user": "https://github.com/mwhansen"
}
```

This looks good with 4.0.1.rc1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: a=(QQ^3).subspace([[1,0,1]])
sage: sage: b=a.basis()[0]
sage: %time b/b.norm()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
(1/2*sqrt(2), 0, 1/2*sqrt(2))
sage: b-b/b.norm()
(-1/2*sqrt(2) + 1, 0, -1/2*sqrt(2) + 1)
```



---

archive/issue_events_006927.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T23:05:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3058",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3058#event-6927"
}
```
