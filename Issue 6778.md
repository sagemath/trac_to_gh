# Issue 6778: [with patch, needs review] Fix nfacets for non-reflexive lattice polytopes

archive/issues_006778.json:
```json
{
    "body": "Assignee: mhampton\n\nThere is a silly bug in computing the number of facets of non-reflexive lattice polytopes:\n\n```\nsage: p = LatticePolytope(matrix([1, 2]))\nsage: p.nfacets()\nTraceback (most recent call last):\n...\nTypeError: object of type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense' has no len()\n```\nThe attached one-line patch fixes it:\n\n```\nsage: p = LatticePolytope(matrix([1, 2]))\nsage: p.nfacets()\n2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6778\n\n",
    "created_at": "2009-08-19T23:01:45Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Fix nfacets for non-reflexive lattice polytopes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6778",
    "user": "https://github.com/novoselt"
}
```
Assignee: mhampton

There is a silly bug in computing the number of facets of non-reflexive lattice polytopes:

```
sage: p = LatticePolytope(matrix([1, 2]))
sage: p.nfacets()
Traceback (most recent call last):
...
TypeError: object of type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense' has no len()
```
The attached one-line patch fixes it:

```
sage: p = LatticePolytope(matrix([1, 2]))
sage: p.nfacets()
2
```


Issue created by migration from https://trac.sagemath.org/ticket/6778





---

archive/issue_comments_055726.json:
```json
{
    "body": "Attachment [trac_6778_nfacets_bug_in_lattice_polytope.patch](tarball://root/attachments/some-uuid/ticket6778/trac_6778_nfacets_bug_in_lattice_polytope.patch) by mhampton created at 2009-09-22 20:53:19\n\nThis is a simple patch for a simple bug.  I filed a duplicate ticket for this at #6991 which should be closed as well.",
    "created_at": "2009-09-22T20:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6778#issuecomment-55726",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_6778_nfacets_bug_in_lattice_polytope.patch](tarball://root/attachments/some-uuid/ticket6778/trac_6778_nfacets_bug_in_lattice_polytope.patch) by mhampton created at 2009-09-22 20:53:19

This is a simple patch for a simple bug.  I filed a duplicate ticket for this at #6991 which should be closed as well.



---

archive/issue_events_015974.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-23T02:45:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6778",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6778#event-15974"
}
```



---

archive/issue_comments_055727.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T02:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6778#issuecomment-55727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055728.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:45:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6778#issuecomment-55728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
