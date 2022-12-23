# Issue 3132: [PATCH] Add computation of multinomial coefficients

archive/issues_003132.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  sage-combinat\n\nThe attached code computes multinomial coefficients using products of binomial coefficients, which is reasonably fast even for large inputs.\n\n(However, MMA is about 3-4x times faster on my machine.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/3132\n\n",
    "created_at": "2008-05-08T13:16:47Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[PATCH] Add computation of multinomial coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3132",
    "user": "gebner"
}
```
Assignee: somebody

CC:  sage-combinat

The attached code computes multinomial coefficients using products of binomial coefficients, which is reasonably fast even for large inputs.

(However, MMA is about 3-4x times faster on my machine.)

Issue created by migration from https://trac.sagemath.org/ticket/3132





---

archive/issue_comments_021752.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-08T13:30:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21752",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_021753.json:
```json
{
    "body": "Code looks good, but the doctest fails on a 32-bit platform (due to #3134).  Either the doctest needs to be changed to use smaller numbers, or #3134 needs to be fixed.",
    "created_at": "2008-05-10T20:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21753",
    "user": "cwitty"
}
```

Code looks good, but the doctest fails on a 32-bit platform (due to #3134).  Either the doctest needs to be changed to use smaller numbers, or #3134 needs to be fixed.



---

archive/issue_comments_021754.json:
```json
{
    "body": "Attachment\n\nfix doctest not to hit #3134",
    "created_at": "2008-05-12T08:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21754",
    "user": "gebner"
}
```

Attachment

fix doctest not to hit #3134



---

archive/issue_comments_021755.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_cwitty\".",
    "created_at": "2008-06-20T04:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21755",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_cwitty".



---

archive/issue_comments_021756.json:
```json
{
    "body": "Looks good.  Thanks for fixing the doctest, and sorry it took so long to re-review.\n\nApply only the second patch.",
    "created_at": "2008-06-20T07:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21756",
    "user": "cwitty"
}
```

Looks good.  Thanks for fixing the doctest, and sorry it took so long to re-review.

Apply only the second patch.



---

archive/issue_comments_021757.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T06:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21757",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021758.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0\n\nGabriel,\n\nplease post hg patches and not diffs in the future, i.e. hg export instead of hg diff. I committed the patch in your name in this case.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T06:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3132#issuecomment-21758",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha0

Gabriel,

please post hg patches and not diffs in the future, i.e. hg export instead of hg diff. I committed the patch in your name in this case.

Cheers,

Michael
