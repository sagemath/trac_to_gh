# Issue 3379: [with patch, positive review] error in plotting 3d polytopes

archive/issues_003379.json:
```json
{
    "body": "Assignee: @mwhansen\n\nKeywords: editor_mhansen\n\n```\nsage: p = LatticePolytope(m, compute_vertices=True)\nsage: m = matrix([[0,0,0],[0,1,1],[1,0,1],[1,1,0]]).transpose()\nsage: p = LatticePolytope(m, compute_vertices=True)\nsage: p.plot3d()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/mike/temp/natalie/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/geometry/lattice_polytope.py in plot3d(self, show_facets, facet_opacity, facet_color, show_edges, edge_thickness, edge_color, show_vertices, vertex_size, vertex_color, show_points, point_size, point_color, show_vindices, vindex_color, show_pindices, pindex_color, index_shift)\n   1447         if show_points:\n   1448             pplot += point3d(self.points().columns(copy=False)[self.nvertices():],\n-> 1449                         size=point_size, rgbcolor=point_color)\n   1450         if show_pindices == None:\n   1451             show_pindices = show_points\n\n/opt/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/shapes2.py in point3d(v, size, **kwds)\n    506     else:\n    507         A = sum([Point(z, size, **kwds) for z in v])\n--> 508         A._set_extra_kwds(kwds)\n    509         return A\n    510     \n\nAttributeError: 'int' object has no attribute '_set_extra_kwds'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3379\n\n",
    "closed_at": "2008-06-23T12:24:18Z",
    "created_at": "2008-06-06T23:00:02Z",
    "labels": [
        "component: geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, positive review] error in plotting 3d polytopes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3379",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

Keywords: editor_mhansen

```
sage: p = LatticePolytope(m, compute_vertices=True)
sage: m = matrix([[0,0,0],[0,1,1],[1,0,1],[1,1,0]]).transpose()
sage: p = LatticePolytope(m, compute_vertices=True)
sage: p.plot3d()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/mike/temp/natalie/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/geometry/lattice_polytope.py in plot3d(self, show_facets, facet_opacity, facet_color, show_edges, edge_thickness, edge_color, show_vertices, vertex_size, vertex_color, show_points, point_size, point_color, show_vindices, vindex_color, show_pindices, pindex_color, index_shift)
   1447         if show_points:
   1448             pplot += point3d(self.points().columns(copy=False)[self.nvertices():],
-> 1449                         size=point_size, rgbcolor=point_color)
   1450         if show_pindices == None:
   1451             show_pindices = show_points

/opt/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/shapes2.py in point3d(v, size, **kwds)
    506     else:
    507         A = sum([Point(z, size, **kwds) for z in v])
--> 508         A._set_extra_kwds(kwds)
    509         return A
    510     

AttributeError: 'int' object has no attribute '_set_extra_kwds'
```

Issue created by migration from https://trac.sagemath.org/ticket/3379





---

archive/issue_comments_023607.json:
```json
{
    "body": "This is occurs because it assumes that \"self.points().columns(copy=False)[self.nvertices():]\" does not return an empty list.\n\n```\n> /opt/sage/local/lib/python2.5/site-packages/sage/geometry/lattice_polytope.py(1449)plot3d()\n   1448             pplot += point3d(self.points().columns(copy=False)[self.nvertices():],\n-> 1449                         size=point_size, rgbcolor=point_color)\n```\nA workaround is to use p.plot3d(show_points=False) so that it doesn't hit that code.",
    "created_at": "2008-06-06T23:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23607",
    "user": "https://github.com/mwhansen"
}
```

This is occurs because it assumes that "self.points().columns(copy=False)[self.nvertices():]" does not return an empty list.

```
> /opt/sage/local/lib/python2.5/site-packages/sage/geometry/lattice_polytope.py(1449)plot3d()
   1448             pplot += point3d(self.points().columns(copy=False)[self.nvertices():],
-> 1449                         size=point_size, rgbcolor=point_color)
```
A workaround is to use p.plot3d(show_points=False) so that it doesn't hit that code.



---

archive/issue_comments_023608.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-08T12:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023609.json:
```json
{
    "body": "Attachment [trac_3379_simple_fix.patch](tarball://root/attachments/some-uuid/ticket3379/trac_3379_simple_fix.patch) by mhampton created at 2008-06-08 14:52:13\n\nAddresses problem found by Mike Hansen",
    "created_at": "2008-06-08T14:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_3379_simple_fix.patch](tarball://root/attachments/some-uuid/ticket3379/trac_3379_simple_fix.patch) by mhampton created at 2008-06-08 14:52:13

Addresses problem found by Mike Hansen



---

archive/issue_comments_023610.json:
```json
{
    "body": "I did the simplest possible workaround, as suggested by Mike.  Other graphics components in this code are handled somewhat differently, so it did not appear that similar fixes were needed elsewhere.  Patch is attached.",
    "created_at": "2008-06-08T14:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I did the simplest possible workaround, as suggested by Mike.  Other graphics components in this code are handled somewhat differently, so it did not appear that similar fixes were needed elsewhere.  Patch is attached.



---

archive/issue_comments_023611.json:
```json
{
    "body": "Changing assignee from mhampton to @mwhansen.",
    "created_at": "2008-06-08T14:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from mhampton to @mwhansen.



---

archive/issue_comments_023612.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-06-08T14:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from assigned to new.



---

archive/issue_comments_023613.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-06-15T22:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23613",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_023614.json:
```json
{
    "body": "Attachment [3379.patch](tarball://root/attachments/some-uuid/ticket3379/3379.patch) by @mwhansen created at 2008-06-19 20:18:58",
    "created_at": "2008-06-19T20:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23614",
    "user": "https://github.com/mwhansen"
}
```

Attachment [3379.patch](tarball://root/attachments/some-uuid/ticket3379/3379.patch) by @mwhansen created at 2008-06-19 20:18:58



---

archive/issue_comments_023615.json:
```json
{
    "body": "Nick Alexander went over this with me and gave it positive review.",
    "created_at": "2008-06-19T20:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23615",
    "user": "https://github.com/mwhansen"
}
```

Nick Alexander went over this with me and gave it positive review.



---

archive/issue_comments_023616.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T12:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023617.json:
```json
{
    "body": "Merged 3379.patch in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T12:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3379#issuecomment-23617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3379.patch in Sage 3.0.4.alpha0



---

archive/issue_events_007621.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T12:24:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3379#event-7621"
}
```



---

archive/issue_events_007622.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-23T12:24:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3379",
    "milestone": "sage-3.0.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3379#event-7622"
}
```
