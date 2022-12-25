# Issue 2937: defects in polyhedra, 3d-gfan rendering

archive/issues_002937.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: polyhedra, convex hull, polytope, gfan\n\nCurrently there are major issues in polyhedra.py (see #2844), which also affect 3d rendering of Groebner gfans - for example, the following doesn't work:\n\n```\nsage: R4.<x,y,z,w> = PolynomialRing(QQ,4)\nsage: idnp = R4.ideal([x*y*z+x^2*z-x*y,x*w^2-z,x*w^4+x*z])\nsage: gfnp = idnp.groebner_fan()\nsage: a = gfnp.render3d()\n```\nI (Marshall Hampton) am actively fixing these issues but I don't have a patch yet.  There are two main problems: 1) I didn't handle unbounded polyhedra well (which is what causes the above problem) and 2) properties such as facial_incidences can be wrong because of vertex reordering by cddlib.  I should have a patch that fixes those problems and adds some rendering enhancements by 5/1/2008 (or earlier).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2937\n\n",
    "closed_at": "2008-05-17T21:36:33Z",
    "created_at": "2008-04-15T23:01:07Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "defects in polyhedra, 3d-gfan rendering",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2937",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

Keywords: polyhedra, convex hull, polytope, gfan

Currently there are major issues in polyhedra.py (see #2844), which also affect 3d rendering of Groebner gfans - for example, the following doesn't work:

```
sage: R4.<x,y,z,w> = PolynomialRing(QQ,4)
sage: idnp = R4.ideal([x*y*z+x^2*z-x*y,x*w^2-z,x*w^4+x*z])
sage: gfnp = idnp.groebner_fan()
sage: a = gfnp.render3d()
```
I (Marshall Hampton) am actively fixing these issues but I don't have a patch yet.  There are two main problems: 1) I didn't handle unbounded polyhedra well (which is what causes the above problem) and 2) properties such as facial_incidences can be wrong because of vertex reordering by cddlib.  I should have a patch that fixes those problems and adds some rendering enhancements by 5/1/2008 (or earlier).

Issue created by migration from https://trac.sagemath.org/ticket/2937





---

archive/issue_comments_020191.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-15T23:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2937#issuecomment-20191",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020192.json:
```json
{
    "body": "Once again, this time with feeling!:\n\nCurrently there are major issues in polyhedra.py (see #2844), which also affect 3d rendering of Groebner gfans - for example, the following doesn't work:\n\n```\nsage: R4.<x,y,z,w> = PolynomialRing(QQ,4) \nsage: idnp = R4.ideal([x*y*z+x2*z-x*y,x*w2-z,x*w4+x*z]) \nsage: gfnp = idnp.groebner_fan() \nsage: a = gfnp.render3d()\n```\n\nI (Marshall Hampton) am actively fixing these issues but I don't have a patch yet. There are two main problems: 1) I didn't handle unbounded polyhedra well (which is what causes the above problem) and 2) properties such as facial_incidences can be wrong because of vertex reordering by cddlib. I should have a patch that fixes those problems and adds some rendering enhancements by 5/1/2008 (or earlier).",
    "created_at": "2008-04-15T23:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2937#issuecomment-20192",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Once again, this time with feeling!:

Currently there are major issues in polyhedra.py (see #2844), which also affect 3d rendering of Groebner gfans - for example, the following doesn't work:

```
sage: R4.<x,y,z,w> = PolynomialRing(QQ,4) 
sage: idnp = R4.ideal([x*y*z+x2*z-x*y,x*w2-z,x*w4+x*z]) 
sage: gfnp = idnp.groebner_fan() 
sage: a = gfnp.render3d()
```

I (Marshall Hampton) am actively fixing these issues but I don't have a patch yet. There are two main problems: 1) I didn't handle unbounded polyhedra well (which is what causes the above problem) and 2) properties such as facial_incidences can be wrong because of vertex reordering by cddlib. I should have a patch that fixes those problems and adds some rendering enhancements by 5/1/2008 (or earlier).



---

archive/issue_comments_020193.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T21:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2937#issuecomment-20193",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020194.json:
```json
{
    "body": "This issue has been fixed by merging #2716:\n\n```\n[22:34] <mhampton> mabshoff: I just figured out why I was confused.  #2716 took long \nenough to get in that you had me rebase it, and I put in stuff that I had meant for #2937\n[22:34] <-- roed has left this server (Read error: 110 (Connection timed out)).\n[22:34] <mhampton> So #2937 can be closed\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-05-17T21:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2937",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2937#issuecomment-20194",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This issue has been fixed by merging #2716:

```
[22:34] <mhampton> mabshoff: I just figured out why I was confused.  #2716 took long 
enough to get in that you had me rebase it, and I put in stuff that I had meant for #2937
[22:34] <-- roed has left this server (Read error: 110 (Connection timed out)).
[22:34] <mhampton> So #2937 can be closed
```

Cheers,

Michael



---

archive/issue_events_006715.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-17T21:36:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2937",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2937#event-6715"
}
```
