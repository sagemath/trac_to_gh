# Issue 9962: non-nef divisors can have sections, too

archive/issues_009962.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @novoselt\n\n`ToricDivisor_generic.sections()` has an incorrect shortcut if the divisor is not nef. The cohomology of the divisor is computed correctly:\n\n```\nsage: rays = [(1,0,0),(0,1,0),(0,0,1),(-2,0,-1),(-2,-1,0),(-3,-1,-1),(1,1,1),(-1,0,0)]\nsage: cones = [[0,1,3],[0,1,6],[0,2,4],[0,2,6],[0,3,5],[0,4,5],[1,3,7],[1,6,7],[2,4,7],[2,6,7],[3,5,7],[4,5,7]]\nsage: X = ToricVariety(Fan(rays=rays,cones=cones))\nsage: D = X.divisor(2); D\nV(z2)\nsage: D.is_nef()\nFalse\nsage:  D.sections()\n()\nsage: D.cohomology(dim=True)\n(1, 0, 0, 0)\n```\nAttached one-line patch fixes this issue and adds doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9963\n\n",
    "created_at": "2010-09-21T20:51:14Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "non-nef divisors can have sections, too",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9962",
    "user": "https://github.com/vbraun"
}
```
Assignee: @aghitza

CC:  @novoselt

`ToricDivisor_generic.sections()` has an incorrect shortcut if the divisor is not nef. The cohomology of the divisor is computed correctly:

```
sage: rays = [(1,0,0),(0,1,0),(0,0,1),(-2,0,-1),(-2,-1,0),(-3,-1,-1),(1,1,1),(-1,0,0)]
sage: cones = [[0,1,3],[0,1,6],[0,2,4],[0,2,6],[0,3,5],[0,4,5],[1,3,7],[1,6,7],[2,4,7],[2,6,7],[3,5,7],[4,5,7]]
sage: X = ToricVariety(Fan(rays=rays,cones=cones))
sage: D = X.divisor(2); D
V(z2)
sage: D.is_nef()
False
sage:  D.sections()
()
sage: D.cohomology(dim=True)
(1, 0, 0, 0)
```
Attached one-line patch fixes this issue and adds doctest.

Issue created by migration from https://trac.sagemath.org/ticket/9963





---

archive/issue_comments_099633.json:
```json
{
    "body": "Attachment [trac_9963_nonnef_divisors_can_have_sections.patch](tarball://root/attachments/some-uuid/ticket9963/trac_9963_nonnef_divisors_can_have_sections.patch) by @vbraun created at 2010-09-21 20:57:04\n\nInitial patch",
    "created_at": "2010-09-21T20:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9962#issuecomment-99633",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9963_nonnef_divisors_can_have_sections.patch](tarball://root/attachments/some-uuid/ticket9963/trac_9963_nonnef_divisors_can_have_sections.patch) by @vbraun created at 2010-09-21 20:57:04

Initial patch



---

archive/issue_comments_099634.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-21T20:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9962#issuecomment-99634",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099635.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T00:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9962#issuecomment-99635",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099636.json:
```json
{
    "body": "Passes tests on 4.6.alpha1!",
    "created_at": "2010-09-22T00:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9962#issuecomment-99636",
    "user": "https://github.com/novoselt"
}
```

Passes tests on 4.6.alpha1!



---

archive/issue_events_025137.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-29T08:39:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9962",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9962#event-25137"
}
```



---

archive/issue_comments_099637.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9962#issuecomment-99637",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
