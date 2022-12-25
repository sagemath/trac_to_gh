# Issue 6915: Getting rays from a polytope fails.

archive/issues_006915.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: polyhedra\n\nSee this example:\n\n\n```\nsage: p=Polyhedron([[0,0],[0,1],[1,0]])\nsage: p.rays()                         \n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/home/seb/.sage/temp/thinbox/5080/_home_seb__sage_init_sage_0.py in <module>()\n\n/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in rays(self)\n    607                 return self._rays\n    608         except AttributeError:\n--> 609             dummy_verts = self.vertices(force_from_ieqs = True)\n    610             self._checked_rays = True\n    611             return self._rays\n\n/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in vertices(self, force_from_ieqs)\n    397         \"\"\"\n    398         if (self._vertices == [] and self._ieqs != []) or force_from_ieqs:\n--> 399             temp_poly_object = ieq_to_vert(self._ieqs, linearities = self._linearities, verbose = self._verbose)\n    400             self._vertices = temp_poly_object._vertices\n    401             self._vertex_incidences = temp_poly_object._vertex_incidences\n\n/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in ieq_to_vert(in_list, linearities, cdd_type, verbose)\n   1426     \"\"\"\n   1427     # first we create the input for cddlib:\n-> 1428     in_length = len(in_list[0])\n   1429     in_str = 'H-representation\\n'\n   1430     if linearities != []:\n\nIndexError: list index out of range\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6915\n\n",
    "created_at": "2009-09-10T11:47:55Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "title": "Getting rays from a polytope fails.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6915",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```
Assignee: mhampton

Keywords: polyhedra

See this example:


```
sage: p=Polyhedron([[0,0],[0,1],[1,0]])
sage: p.rays()                         
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/seb/.sage/temp/thinbox/5080/_home_seb__sage_init_sage_0.py in <module>()

/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in rays(self)
    607                 return self._rays
    608         except AttributeError:
--> 609             dummy_verts = self.vertices(force_from_ieqs = True)
    610             self._checked_rays = True
    611             return self._rays

/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in vertices(self, force_from_ieqs)
    397         """
    398         if (self._vertices == [] and self._ieqs != []) or force_from_ieqs:
--> 399             temp_poly_object = ieq_to_vert(self._ieqs, linearities = self._linearities, verbose = self._verbose)
    400             self._vertices = temp_poly_object._vertices
    401             self._vertex_incidences = temp_poly_object._vertex_incidences

/home/seb/.local/sage-4.1/local/lib/python2.6/site-packages/sage/geometry/polyhedra.pyc in ieq_to_vert(in_list, linearities, cdd_type, verbose)
   1426     """
   1427     # first we create the input for cddlib:
-> 1428     in_length = len(in_list[0])
   1429     in_str = 'H-representation\n'
   1430     if linearities != []:

IndexError: list index out of range

```


Issue created by migration from https://trac.sagemath.org/ticket/6915





---

archive/issue_comments_056996.json:
```json
{
    "body": "This will be fixed by #7109.",
    "created_at": "2009-11-13T03:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6915#issuecomment-56996",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This will be fixed by #7109.



---

archive/issue_events_007142.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2010-01-27T17:16:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6915",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6915#event-7142"
}
```



---

archive/issue_comments_056997.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-27T17:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6915#issuecomment-56997",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_056998.json:
```json
{
    "body": "fixed in 4.3.2.alpha0",
    "created_at": "2010-01-27T17:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6915#issuecomment-56998",
    "user": "https://github.com/vbraun"
}
```

fixed in 4.3.2.alpha0



---

archive/issue_comments_056999.json:
```json
{
    "body": "Replying to [comment:2 vbraun]:\n> fixed in 4.3.2.alpha0\n\nMake sure you understand the procedure for closing tickets. See http://www.sagemath.org/doc/developer/trac.html#closing-tickets",
    "created_at": "2010-01-28T04:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6915#issuecomment-56999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 vbraun]:
> fixed in 4.3.2.alpha0

Make sure you understand the procedure for closing tickets. See http://www.sagemath.org/doc/developer/trac.html#closing-tickets
