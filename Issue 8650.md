# Issue 8650: Extreme faces of Polyhedra are inconsistent

archive/issues_008650.json:
```json
{
    "body": "Assignee: mhampton\n\nLet's look at the first face of each dimension of a polyhedron:\n\n```\nfor lset in polytopes.cross_polytope(2).face_lattice().level_sets():\n    print lset[0]\n```\n\nThe result is \n\n```\n(None, None)\n((0,), (1, 2))\n((1, 2), (3,))\n((0, 1, 2, 3), (0, 1, 2, 3))\n```\n\nwhere the first tuple (None, None) corresponds to the empty face of the polytope. The first element gives generating vertices of this face (there are None). The second one should give all facets that contain this face. This should be the set of all facets of the polytope, not None. Similarly, for the last face, i.e. the whole polytope, we need to list all vertices belonging to this face (they are correctly listed), and all facets containing the polytope - there should be None.\n\nWhile it should be easy to fix, I don't quite understand the code of face_lattice, so maybe someone else can do this...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8650\n\n",
    "created_at": "2010-04-04T19:23:02Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Extreme faces of Polyhedra are inconsistent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8650",
    "user": "https://github.com/novoselt"
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

archive/issue_comments_078354.json:
```json
{
    "body": "Oops.  I wrote face_lattice, so this is my fault.  Thanks for pointing it out.  I think I can fix it pretty soon (hopefully today).",
    "created_at": "2010-04-04T21:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78354",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Oops.  I wrote face_lattice, so this is my fault.  Thanks for pointing it out.  I think I can fix it pretty soon (hopefully today).



---

archive/issue_comments_078355.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-04T22:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078356.json:
```json
{
    "body": "Attachment [trac_8650_patch0.patch](tarball://root/attachments/some-uuid/ticket8650/trac_8650_patch0.patch) by mhampton created at 2010-04-04 22:20:54\n\nOK, I think the attached patch corrects things.",
    "created_at": "2010-04-04T22:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_8650_patch0.patch](tarball://root/attachments/some-uuid/ticket8650/trac_8650_patch0.patch) by mhampton created at 2010-04-04 22:20:54

OK, I think the attached patch corrects things.



---

archive/issue_comments_078357.json:
```json
{
    "body": "Attachment [trac_8650_fix_face_lattice_in_polyhedra.patch](tarball://root/attachments/some-uuid/ticket8650/trac_8650_fix_face_lattice_in_polyhedra.patch) by @novoselt created at 2010-04-05 03:15:30\n\nApply this patch only",
    "created_at": "2010-04-05T03:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78357",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8650_fix_face_lattice_in_polyhedra.patch](tarball://root/attachments/some-uuid/ticket8650/trac_8650_fix_face_lattice_in_polyhedra.patch) by @novoselt created at 2010-04-05 03:15:30

Apply this patch only



---

archive/issue_comments_078358.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T03:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78358",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020934.json:
```json
{
    "actor": "https://github.com/novoselt",
    "created_at": "2010-04-05T03:18:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8650#event-20934"
}
```



---

archive/issue_comments_078359.json:
```json
{
    "body": "Thank you! I have added the code above to the TESTS section.",
    "created_at": "2010-04-05T03:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78359",
    "user": "https://github.com/novoselt"
}
```

Thank you! I have added the code above to the TESTS section.



---

archive/issue_comments_078360.json:
```json
{
    "body": "Merged \"trac_8650_fix_face_lattice_in_polyhedra.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78360",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8650_fix_face_lattice_in_polyhedra.patch" in 4.4.alpha0.



---

archive/issue_comments_078361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78361",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_020935.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:56:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8650#event-20935"
}
```



---

archive/issue_comments_078362.json:
```json
{
    "body": "See #8709 for a followup.",
    "created_at": "2010-04-18T03:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78362",
    "user": "https://github.com/jhpalmieri"
}
```

See #8709 for a followup.



---

archive/issue_comments_078363.json:
```json
{
    "body": "And #8656.",
    "created_at": "2010-04-18T04:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8650#issuecomment-78363",
    "user": "https://github.com/novoselt"
}
```

And #8656.
