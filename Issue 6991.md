# Issue 6991: lattice polytope nfacets method broken for non-reflexive polytopes

archive/issues_006991.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @novoselt\n\nIn the nfacets method, for non-reflexive lattice polytopes this is computed from:\n\n```\nself._nfacets = len(self._facet_normals)\n```\n\nbut self._facet_normals is a matrix, which does not have a len method.  So I think this should instead be\n\n```\nself._nfacets = self._facet_normals.nrows()\n```\n\n\nA doctest should also be added for this case.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6991\n\n",
    "created_at": "2009-09-22T18:45:43Z",
    "labels": [
        "component: geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "lattice polytope nfacets method broken for non-reflexive polytopes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

CC:  @novoselt

In the nfacets method, for non-reflexive lattice polytopes this is computed from:

```
self._nfacets = len(self._facet_normals)
```

but self._facet_normals is a matrix, which does not have a len method.  So I think this should instead be

```
self._nfacets = self._facet_normals.nrows()
```


A doctest should also be added for this case.

Issue created by migration from https://trac.sagemath.org/ticket/6991





---

archive/issue_comments_057718.json:
```json
{
    "body": "This is actually fixed by this patch (which needs a review):\n\nhttp://trac.sagemath.org/sage_trac/ticket/6778",
    "created_at": "2009-09-22T19:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6991#issuecomment-57718",
    "user": "https://github.com/novoselt"
}
```

This is actually fixed by this patch (which needs a review):

http://trac.sagemath.org/sage_trac/ticket/6778



---

archive/issue_comments_057719.json:
```json
{
    "body": "OK, sorry about that.  I am working through your tickets and I should have looked more closely.  This ticket can be closed as a duplicate of 6778.\n\n-Marshall",
    "created_at": "2009-09-22T20:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6991#issuecomment-57719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, sorry about that.  I am working through your tickets and I should have looked more closely.  This ticket can be closed as a duplicate of 6778.

-Marshall



---

archive/issue_comments_057720.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2009-09-22T20:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6991#issuecomment-57720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_057721.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-12-19T00:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6991#issuecomment-57721",
    "user": "https://github.com/novoselt"
}
```

Resolution: duplicate
