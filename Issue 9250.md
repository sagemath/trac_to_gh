# Issue 9250: Bug in crystal code

archive/issues_009250.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  combinat\n\nThis currently breaks:\n\nsage: B=KirillovReshetikhinCrystal(['D',5,1], 3,1)\nsage: B[0].e(0)\n\nThis has to do with the method intermediate_shape for plus/minus diagrams.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9250\n\n",
    "created_at": "2010-06-16T21:25:50Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Bug in crystal code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9250",
    "user": "https://github.com/anneschilling"
}
```
Assignee: sage-combinat

CC:  combinat

This currently breaks:

sage: B=KirillovReshetikhinCrystal(['D',5,1], 3,1)
sage: B[0].e(0)

This has to do with the method intermediate_shape for plus/minus diagrams.

Issue created by migration from https://trac.sagemath.org/ticket/9250





---

archive/issue_comments_086918.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-16T21:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-86918",
    "user": "https://github.com/anneschilling"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086919.json:
```json
{
    "body": "Changing keywords from \"\" to \"crystals\".",
    "created_at": "2010-06-16T21:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-86919",
    "user": "https://github.com/anneschilling"
}
```

Changing keywords from "" to "crystals".



---

archive/issue_comments_086920.json:
```json
{
    "body": "Attachment [trac_9250-crystalbug-as.patch](tarball://root/attachments/some-uuid/ticket9250/trac_9250-crystalbug-as.patch) by @anneschilling created at 2010-06-16 21:52:09",
    "created_at": "2010-06-16T21:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-86920",
    "user": "https://github.com/anneschilling"
}
```

Attachment [trac_9250-crystalbug-as.patch](tarball://root/attachments/some-uuid/ticket9250/trac_9250-crystalbug-as.patch) by @anneschilling created at 2010-06-16 21:52:09



---

archive/issue_comments_086921.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-25T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-86921",
    "user": "https://github.com/dwbump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086922.json:
```json
{
    "body": "After the patch, passes `sage -testall`.\n\nFixes the crash mentioned in the Description.\n\nIncludes doctest.\n\nApparently the intermediate_shape method of PMDiagram presumed\nthat self.n was 2.\n\nThis one-line fix is obviously correct.",
    "created_at": "2010-06-25T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-86922",
    "user": "https://github.com/dwbump"
}
```

After the patch, passes `sage -testall`.

Fixes the crash mentioned in the Description.

Includes doctest.

Apparently the intermediate_shape method of PMDiagram presumed
that self.n was 2.

This one-line fix is obviously correct.



---

archive/issue_comments_086923.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-86923",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009411.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-07-21T01:44:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9250#event-9411"
}
```
