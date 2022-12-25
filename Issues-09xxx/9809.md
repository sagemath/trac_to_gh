# Issue 9809: Heisenbug in RationalPolyhedralCone.facets

archive/issues_009809.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @novoselt\n\nThe `faces` method of a cone in a fan manages to screw up subsequent `facet` output:\n\n```\nsage: cone = toric_varieties.dP8().fan().generating_cone(0)\nsage: cone\n2-d cone of Rational polyhedral fan in 2-d lattice N\nsage: cone.facets()\n(1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N)\nsage: cone.faces()\n((0-d cone of Rational polyhedral fan in 2-d lattice N,), (1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N), (2-d cone of Rational polyhedral fan in 2-d lattice N,))\nsage: cone.facets()\n(2-d cone of Rational polyhedral fan in 2-d lattice N,)\n```\nThis is on vanilla Sage 4.5.2 without any patches applied. Andrey, I think its somewhere in your code so you'll probably find it faster than I can.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9810\n\n",
    "closed_at": "2010-09-15T09:57:07Z",
    "created_at": "2010-08-26T21:12:05Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Heisenbug in RationalPolyhedralCone.facets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9809",
    "user": "https://github.com/vbraun"
}
```
Assignee: mhampton

CC:  @novoselt

The `faces` method of a cone in a fan manages to screw up subsequent `facet` output:

```
sage: cone = toric_varieties.dP8().fan().generating_cone(0)
sage: cone
2-d cone of Rational polyhedral fan in 2-d lattice N
sage: cone.facets()
(1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N)
sage: cone.faces()
((0-d cone of Rational polyhedral fan in 2-d lattice N,), (1-d cone of Rational polyhedral fan in 2-d lattice N, 1-d cone of Rational polyhedral fan in 2-d lattice N), (2-d cone of Rational polyhedral fan in 2-d lattice N,))
sage: cone.facets()
(2-d cone of Rational polyhedral fan in 2-d lattice N,)
```
This is on vanilla Sage 4.5.2 without any patches applied. Andrey, I think its somewhere in your code so you'll probably find it faster than I can.

Issue created by migration from https://trac.sagemath.org/ticket/9810





---

archive/issue_comments_096577.json:
```json
{
    "body": "Attachment [trac_9810_cone_faces_invalidates_facets.patch](tarball://root/attachments/some-uuid/ticket9810/trac_9810_cone_faces_invalidates_facets.patch) by @novoselt created at 2010-08-26 21:31:44",
    "created_at": "2010-08-26T21:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96577",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9810_cone_faces_invalidates_facets.patch](tarball://root/attachments/some-uuid/ticket9810/trac_9810_cone_faces_invalidates_facets.patch) by @novoselt created at 2010-08-26 21:31:44



---

archive/issue_comments_096578.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T21:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96578",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096579.json:
```json
{
    "body": "Should be 2 instead of 1... Thanks for catching!",
    "created_at": "2010-08-26T21:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96579",
    "user": "https://github.com/novoselt"
}
```

Should be 2 instead of 1... Thanks for catching!



---

archive/issue_comments_096580.json:
```json
{
    "body": "Fixes it!",
    "created_at": "2010-08-26T21:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96580",
    "user": "https://github.com/vbraun"
}
```

Fixes it!



---

archive/issue_comments_096581.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-26T21:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96581",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024648.json:
```json
{
    "actor": "https://github.com/novoselt",
    "created_at": "2010-08-27T03:45:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9809#event-24648"
}
```



---

archive/issue_comments_096582.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9809#issuecomment-96582",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024649.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T09:57:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9809",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9809#event-24649"
}
```
