# Issue 3215: optional lrs package

archive/issues_003215.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: polyhedra, convex hull, polytope, geometry, lrs\n\nlrs (linear reverse search) is an alternate algorithm to cddlib for changing from a vertex to facet/inequality description of a polyhedron.  For some polyhedra, lrs is much faster than cddlib, and for others cddlib is better.  It is difficult to determine in advance which will be better.  Since lrs is a small and easy to compile program, I think it should be included in sage.  Eventually there should be an option in polytope code to use lrs instead of cddlib.  This ticket is only concerned with making the functionality available, not in altering the polyhedral code.\nA candidate spkg is available at: \nhttp://www.d.umn.edu/~mhampton/lrs-4.2b.p0.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3215\n\n",
    "created_at": "2008-05-16T02:34:09Z",
    "labels": [
        "component: geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "optional lrs package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3215",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: somebody

Keywords: polyhedra, convex hull, polytope, geometry, lrs

lrs (linear reverse search) is an alternate algorithm to cddlib for changing from a vertex to facet/inequality description of a polyhedron.  For some polyhedra, lrs is much faster than cddlib, and for others cddlib is better.  It is difficult to determine in advance which will be better.  Since lrs is a small and easy to compile program, I think it should be included in sage.  Eventually there should be an option in polytope code to use lrs instead of cddlib.  This ticket is only concerned with making the functionality available, not in altering the polyhedral code.
A candidate spkg is available at: 
http://www.d.umn.edu/~mhampton/lrs-4.2b.p0.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3215





---

archive/issue_comments_022217.json:
```json
{
    "body": "Changing keywords from \"polyhedra, convex hull, polytope, geometry, lrs\" to \"polyhedra, convex hull, polytope, geometry, lrs, editor_mhansen\".",
    "created_at": "2008-06-15T22:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3215#issuecomment-22217",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "polyhedra, convex hull, polytope, geometry, lrs" to "polyhedra, convex hull, polytope, geometry, lrs, editor_mhansen".



---

archive/issue_comments_022218.json:
```json
{
    "body": "This builds fine for me in about a minute.",
    "created_at": "2008-06-19T20:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3215#issuecomment-22218",
    "user": "https://github.com/mwhansen"
}
```

This builds fine for me in about a minute.



---

archive/issue_comments_022219.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T09:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3215#issuecomment-22219",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022220.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T09:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3215",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3215#issuecomment-22220",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1
