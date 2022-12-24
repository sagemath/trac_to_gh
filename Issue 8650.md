# Issue 8650: Extreme faces of Polyhedra are inconsistent

archive/issues_008650.json:
```json
{
    "body": "Assignee: mhampton\n\nLet's look at the first face of each dimension of a polyhedron:\n\n```\nfor lset in polytopes.cross_polytope(2).face_lattice().level_sets():\n    print lset[0]\n```\n\nThe result is \n\n```\n(None, None)\n((0,), (1, 2))\n((1, 2), (3,))\n((0, 1, 2, 3), (0, 1, 2, 3))\n```\n\nwhere the first tuple (None, None) corresponds to the empty face of the polytope. The first element gives generating vertices of this face (there are None). The second one should give all facets that contain this face. This should be the set of all facets of the polytope, not None. Similarly, for the last face, i.e. the whole polytope, we need to list all vertices belonging to this face (they are correctly listed), and all facets containing the polytope - there should be None.\n\nWhile it should be easy to fix, I don't quite understand the code of face_lattice, so maybe someone else can do this...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8650\n\n",
    "created_at": "2010-04-04T19:23:02Z",
    "labels": [
        "geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Extreme faces of Polyhedra are inconsistent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8650",
    "user": "novoselt"
}
```
Assignee: mhampton

Let's look at the first face of each dimension of a polyhedron:

```
for lset in polytopes.cross_polytope(2).face_lattice().level_sets():
    print lset[0]
```

The result is 

```
(None, None)
((0,), (1, 2))
((1, 2), (3,))
((0, 1, 2, 3), (0, 1, 2, 3))
```

where the first tuple (None, None) corresponds to the empty face of the polytope. The first element gives generating vertices of this face (there are None). The second one should give all facets that contain this face. This should be the set of all facets of the polytope, not None. Similarly, for the last face, i.e. the whole polytope, we need to list all vertices belonging to this face (they are correctly listed), and all facets containing the polytope - there should be None.

While it should be easy to fix, I don't quite understand the code of face_lattice, so maybe someone else can do this...

Issue created by migration from https://trac.sagemath.org/ticket/8650





---

archive/issue_comments_078484.json:
```json
{
    "body": "Oops.  I wrote face_lattice, so this is my fault.  Thanks for pointing it out.  I think I can fix it pretty soon (hopefully today).",
    "created_at": "2010-04-04T21:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78484",
    "user": "mhampton"
}
```

Oops.  I wrote face_lattice, so this is my fault.  Thanks for pointing it out.  I think I can fix it pretty soon (hopefully today).



---

archive/issue_comments_078485.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-04T22:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78485",
    "user": "mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078486.json:
```json
{
    "body": "Attachment [trac_8650_patch0.patch](tarball://root/attachments/some-uuid/ticket8650/trac_8650_patch0.patch) by mhampton created at 2010-04-04 22:20:54\n\nOK, I think the attached patch corrects things.",
    "created_at": "2010-04-04T22:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78486",
    "user": "mhampton"
}
```

Attachment [trac_8650_patch0.patch](tarball://root/attachments/some-uuid/ticket8650/trac_8650_patch0.patch) by mhampton created at 2010-04-04 22:20:54

OK, I think the attached patch corrects things.



---

archive/issue_comments_078487.json:
```json
{
    "body": "Attachment [trac_8650_fix_face_lattice_in_polyhedra.patch](tarball://root/attachments/some-uuid/ticket8650/trac_8650_fix_face_lattice_in_polyhedra.patch) by novoselt created at 2010-04-05 03:15:30\n\nApply this patch only",
    "created_at": "2010-04-05T03:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78487",
    "user": "novoselt"
}
```

Attachment [trac_8650_fix_face_lattice_in_polyhedra.patch](tarball://root/attachments/some-uuid/ticket8650/trac_8650_fix_face_lattice_in_polyhedra.patch) by novoselt created at 2010-04-05 03:15:30

Apply this patch only



---

archive/issue_comments_078488.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T03:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78488",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078489.json:
```json
{
    "body": "Thank you! I have added the code above to the TESTS section.",
    "created_at": "2010-04-05T03:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78489",
    "user": "novoselt"
}
```

Thank you! I have added the code above to the TESTS section.



---

archive/issue_comments_078490.json:
```json
{
    "body": "Merged \"trac_8650_fix_face_lattice_in_polyhedra.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78490",
    "user": "jhpalmieri"
}
```

Merged "trac_8650_fix_face_lattice_in_polyhedra.patch" in 4.4.alpha0.



---

archive/issue_comments_078491.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78491",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_078492.json:
```json
{
    "body": "See #8709 for a followup.",
    "created_at": "2010-04-18T03:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78492",
    "user": "jhpalmieri"
}
```

See #8709 for a followup.



---

archive/issue_comments_078493.json:
```json
{
    "body": "And #8656.",
    "created_at": "2010-04-18T04:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78493",
    "user": "novoselt"
}
```

And #8656.
