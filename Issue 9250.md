# Issue 9250: Bug in crystal code

archive/issues_009250.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  combinat\n\nThis currently breaks:\n\nsage: B=KirillovReshetikhinCrystal(['D',5,1], 3,1)\nsage: B[0].e(0)\n\nThis has to do with the method intermediate_shape for plus/minus diagrams.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9250\n\n",
    "created_at": "2010-06-16T21:25:50Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Bug in crystal code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9250",
    "user": "aschilling"
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

archive/issue_comments_087057.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-16T21:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-87057",
    "user": "aschilling"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087058.json:
```json
{
    "body": "Changing keywords from \"\" to \"crystals\".",
    "created_at": "2010-06-16T21:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-87058",
    "user": "aschilling"
}
```

Changing keywords from "" to "crystals".



---

archive/issue_comments_087059.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-16T21:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-87059",
    "user": "aschilling"
}
```

Attachment



---

archive/issue_comments_087060.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-25T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-87060",
    "user": "bump"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087061.json:
```json
{
    "body": "After the patch, passes `sage -testall`.\n\nFixes the crash mentioned in the Description.\n\nIncludes doctest.\n\nApparently the intermediate_shape method of PMDiagram presumed\nthat self.n was 2.\n\nThis one-line fix is obviously correct.",
    "created_at": "2010-06-25T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-87061",
    "user": "bump"
}
```

After the patch, passes `sage -testall`.

Fixes the crash mentioned in the Description.

Includes doctest.

Apparently the intermediate_shape method of PMDiagram presumed
that self.n was 2.

This one-line fix is obviously correct.



---

archive/issue_comments_087062.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T01:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9250#issuecomment-87062",
    "user": "mpatel"
}
```

Resolution: fixed
