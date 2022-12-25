# Issue 6779: [with patch, needs review] positive_integer_relations bug in lattice_polytope

archive/issues_006779.json:
```json
{
    "body": "Assignee: mhampton\n\nSince gcd(3/2, 9/5) used to be 3/10, it was used in lattice_polytope functions for rescaling to primitive integral vectors in the given rational direction. This is no longer true and leads to bugs:\n\n```\nsage: p = ReflexivePolytope(2, 1)\nsage: lattice_polytope.positive_integer_relations(p.vertices())\nTraceback (most recent call last):\n...\nTypeError: matrix has denominators so can't change to ZZ.\n```\nThe patch adds a function integral_length and uses it instead of gcd:\n\n```\nsage: p = ReflexivePolytope(2, 1)\nsage: lattice_polytope.positive_integer_relations(p.vertices())\n[2 1 1]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6779\n\n",
    "created_at": "2009-08-20T00:04:40Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "[with patch, needs review] positive_integer_relations bug in lattice_polytope",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6779",
    "user": "https://github.com/novoselt"
}
```
Assignee: mhampton

Since gcd(3/2, 9/5) used to be 3/10, it was used in lattice_polytope functions for rescaling to primitive integral vectors in the given rational direction. This is no longer true and leads to bugs:

```
sage: p = ReflexivePolytope(2, 1)
sage: lattice_polytope.positive_integer_relations(p.vertices())
Traceback (most recent call last):
...
TypeError: matrix has denominators so can't change to ZZ.
```
The patch adds a function integral_length and uses it instead of gcd:

```
sage: p = ReflexivePolytope(2, 1)
sage: lattice_polytope.positive_integer_relations(p.vertices())
[2 1 1]
```

Issue created by migration from https://trac.sagemath.org/ticket/6779





---

archive/issue_comments_055729.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-24T15:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6779#issuecomment-55729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_055730.json:
```json
{
    "body": "Attachment [trac_6779_positive_integer_relations_bug_in_lattice_polytope.patch](tarball://root/attachments/some-uuid/ticket6779/trac_6779_positive_integer_relations_bug_in_lattice_polytope.patch) by mhampton created at 2009-10-24 15:44:28\n\nLooks good, positive review.",
    "created_at": "2009-10-24T15:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6779#issuecomment-55730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_6779_positive_integer_relations_bug_in_lattice_polytope.patch](tarball://root/attachments/some-uuid/ticket6779/trac_6779_positive_integer_relations_bug_in_lattice_polytope.patch) by mhampton created at 2009-10-24 15:44:28

Looks good, positive review.



---

archive/issue_comments_055731.json:
```json
{
    "body": "This patch is included as a part of a rebased patch for #6831.",
    "created_at": "2009-10-30T05:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6779#issuecomment-55731",
    "user": "https://github.com/novoselt"
}
```

This patch is included as a part of a rebased patch for #6831.



---

archive/issue_comments_055732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-02T04:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6779#issuecomment-55732",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_015975.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-02T04:35:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6779",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6779#event-15975"
}
```



---

archive/issue_comments_055733.json:
```json
{
    "body": "Fixed as part of #6831",
    "created_at": "2009-11-02T04:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6779#issuecomment-55733",
    "user": "https://github.com/mwhansen"
}
```

Fixed as part of #6831
