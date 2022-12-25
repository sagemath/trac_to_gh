# Issue 5134: Polyhedron: conversion from V-form to H-form fails if no extreme point is given

archive/issues_005134.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  mhampton\n\nLet's consider the first diagonal in `R^2` as a polyhedron. It has one extreme point (the origin) and one ray.\nIt can be defined in sage in V-form and converted to H-form as shown\n\n```\nsage: p1v1r = Polyhedron([[0,0]],[[1,1]])\nsage: p1v1r\nA Polyhedron with 1 vertex with 1 rays.\nsage: p1v1r.ieqs()\n[[1, 0, 0], [0, 1, 0]]\nsage: p1v1r.linearities()\n[[0, -1, 1]]\n```\n\nthe H-form can be read as\n\n```\np1v1r = { (x,y) such that\n1 + 0*x + 0*y >= 0 and \n1 + 1*x + 0*y >= 0 and\n1 - 1*x + 1*y >= 0\n```\n\nSage also allows us to define the polyhedron without the vertex\n\n```\nsage: p0v1r = Polyhedron([], [[1,1]])        \nsage: p0v1r\nA Polyhedron with 1 vertex.\nsage: p0v1r.ieqs()                      \n[]\nsage: p0v1r.linearities()               \n[]\n```\n\nHowever, then\n1. the _repr_() text is different\n2. the conversion to H-form failed\n\nproblem 2 comes from cdd which requires to be given the extreme point. We could fix it by adding the point before calling cdd.\n\nHowever, from a theorical point of view, I think that it would also make sense to always require at least one vertex:\n\nOne can consider the polyhedron as a region of an euclidean space. In such a case, vertices are *points* and rays are * free vectors*. Then one would always require at least one point.\n\nWhat do you think?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5134\n\n",
    "created_at": "2009-01-30T01:37:00Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Polyhedron: conversion from V-form to H-form fails if no extreme point is given",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5134",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```
Assignee: mhampton

CC:  mhampton

Let's consider the first diagonal in `R^2` as a polyhedron. It has one extreme point (the origin) and one ray.
It can be defined in sage in V-form and converted to H-form as shown

```
sage: p1v1r = Polyhedron([[0,0]],[[1,1]])
sage: p1v1r
A Polyhedron with 1 vertex with 1 rays.
sage: p1v1r.ieqs()
[[1, 0, 0], [0, 1, 0]]
sage: p1v1r.linearities()
[[0, -1, 1]]
```

the H-form can be read as

```
p1v1r = { (x,y) such that
1 + 0*x + 0*y >= 0 and 
1 + 1*x + 0*y >= 0 and
1 - 1*x + 1*y >= 0
```

Sage also allows us to define the polyhedron without the vertex

```
sage: p0v1r = Polyhedron([], [[1,1]])        
sage: p0v1r
A Polyhedron with 1 vertex.
sage: p0v1r.ieqs()                      
[]
sage: p0v1r.linearities()               
[]
```

However, then
1. the _repr_() text is different
2. the conversion to H-form failed

problem 2 comes from cdd which requires to be given the extreme point. We could fix it by adding the point before calling cdd.

However, from a theorical point of view, I think that it would also make sense to always require at least one vertex:

One can consider the polyhedron as a region of an euclidean space. In such a case, vertices are *points* and rays are * free vectors*. Then one would always require at least one point.

What do you think?

Issue created by migration from https://trac.sagemath.org/ticket/5134





---

archive/issue_comments_039188.json:
```json
{
    "body": "Please remember to assign a milestone for each ticket opened.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-30T01:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5134#issuecomment-39188",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Please remember to assign a milestone for each ticket opened.

Cheers,

Michael



---

archive/issue_events_011901.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-30T01:50:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5134",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5134#event-11901"
}
```



---

archive/issue_comments_039189.json:
```json
{
    "body": "I think this will be addressed by #7109 once it is done.  If a ray is entered without a vertex, the current behavior is to assume that the ray starts at the origin.  I think this is reasonable.",
    "created_at": "2009-11-13T03:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5134#issuecomment-39189",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I think this will be addressed by #7109 once it is done.  If a ray is entered without a vertex, the current behavior is to assume that the ray starts at the origin.  I think this is reasonable.



---

archive/issue_comments_039190.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-04-03T14:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5134#issuecomment-39190",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_039191.json:
```json
{
    "body": "Should this ticket be closed now that #7109 is merged? Current outputs are different from the ones described here and as I understand now both representations are computed during construction and are always correct.",
    "created_at": "2010-04-03T14:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5134#issuecomment-39191",
    "user": "https://github.com/novoselt"
}
```

Should this ticket be closed now that #7109 is merged? Current outputs are different from the ones described here and as I understand now both representations are computed during construction and are always correct.



---

archive/issue_comments_039192.json:
```json
{
    "body": "Yes, I think it can be closed.",
    "created_at": "2010-04-03T19:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5134#issuecomment-39192",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Yes, I think it can be closed.



---

archive/issue_comments_039193.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-03T19:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5134#issuecomment-39193",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Resolution: fixed



---

archive/issue_events_011902.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mhampton",
    "created_at": "2010-04-03T19:12:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5134",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5134#event-11902"
}
```
