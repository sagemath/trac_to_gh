# Issue 9933: Toric divisor class -> divisor lift should be integral

archive/issues_009933.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @novoselt\n\nAn integral divisor class should lift to an integral divisor. But:\n\n```\nsage: rays = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (2, -1, -1)]\nsage: cones = [(0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4)]\nsage: X = ToricVariety(Fan(cones=cones, rays=rays))\nsage: X.rational_class_group().gen(1).lift()\n-1/2*V(z0) + 1/2*V(z1)\n```\n\nThe attached patch fixes this and any doctest fallout.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9934\n\n",
    "created_at": "2010-09-17T14:00:03Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Toric divisor class -> divisor lift should be integral",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9933",
    "user": "https://github.com/vbraun"
}
```
Assignee: @aghitza

CC:  @novoselt

An integral divisor class should lift to an integral divisor. But:

```
sage: rays = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (2, -1, -1)]
sage: cones = [(0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4)]
sage: X = ToricVariety(Fan(cones=cones, rays=rays))
sage: X.rational_class_group().gen(1).lift()
-1/2*V(z0) + 1/2*V(z1)
```

The attached patch fixes this and any doctest fallout.

Issue created by migration from https://trac.sagemath.org/ticket/9934





---

archive/issue_comments_098741.json:
```json
{
    "body": "Initial patch",
    "created_at": "2010-09-17T14:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98741",
    "user": "https://github.com/vbraun"
}
```

Initial patch



---

archive/issue_comments_098742.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T14:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98742",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098743.json:
```json
{
    "body": "Attachment [trac_9934_class_group_fixes.patch](tarball://root/attachments/some-uuid/ticket9934/trac_9934_class_group_fixes.patch) by @vbraun created at 2010-09-17 14:03:39",
    "created_at": "2010-09-17T14:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98743",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9934_class_group_fixes.patch](tarball://root/attachments/some-uuid/ticket9934/trac_9934_class_group_fixes.patch) by @vbraun created at 2010-09-17 14:03:39



---

archive/issue_comments_098744.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T19:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98744",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098745.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-17T19:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98745",
    "user": "https://github.com/novoselt"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_098746.json:
```json
{
    "body": "Nice improvement! (Not quite defect ;-))\n\nTested on 4.5.3 with all the toric patches that got merged to 4.6.alpha1.",
    "created_at": "2010-09-17T19:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98746",
    "user": "https://github.com/novoselt"
}
```

Nice improvement! (Not quite defect ;-))

Tested on 4.5.3 with all the toric patches that got merged to 4.6.alpha1.



---

archive/issue_comments_098747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9933#issuecomment-98747",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_010061.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-29T08:39:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9933",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9933#event-10061"
}
```
