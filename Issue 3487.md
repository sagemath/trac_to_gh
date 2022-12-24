# Issue 3487: mercurial and sage

archive/issues_003487.json:
```json
{
    "body": "Assignee: was\n\nWhen sage comes up it announces:\n\nLoading SAGE library. Current Mercurial branch is: worldDomination\n\nturns out, this is the current \"clone\"... when you are using \"hg branches\" in your clone it would be nice for it to say something like:\n\nLoading SAGE library. Current Mercurial clone is: worldDomination on branch: riemannProof\n\nIssue created by migration from https://trac.sagemath.org/ticket/3487\n\n",
    "created_at": "2008-06-20T21:02:04Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "mercurial and sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3487",
    "user": "ghtdak"
}
```
Assignee: was

When sage comes up it announces:

Loading SAGE library. Current Mercurial branch is: worldDomination

turns out, this is the current "clone"... when you are using "hg branches" in your clone it would be nice for it to say something like:

Loading SAGE library. Current Mercurial clone is: worldDomination on branch: riemannProof

Issue created by migration from https://trac.sagemath.org/ticket/3487





---

archive/issue_comments_024574.json:
```json
{
    "body": "In thinking about it, I think this is more general.\n\nSo, one clones using sage -clone worldDomination\n\nand then one asks what branch one is on with sage -branch\n\nbut, we should be able to clone and branch with the right syntax.  given the current switches, we need to be careful, but we should be able to clone and branch with switches to sage and ask where we are.\n\nso, sage -branch could simply spit out clone and branch... but \"sage -b\" is an issue",
    "created_at": "2008-06-20T21:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24574",
    "user": "ghtdak"
}
```

In thinking about it, I think this is more general.

So, one clones using sage -clone worldDomination

and then one asks what branch one is on with sage -branch

but, we should be able to clone and branch with the right syntax.  given the current switches, we need to be careful, but we should be able to clone and branch with switches to sage and ask where we are.

so, sage -branch could simply spit out clone and branch... but "sage -b" is an issue



---

archive/issue_comments_024575.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24575",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_024576.json:
```json
{
    "body": "we have switched to git, this is obsolete",
    "created_at": "2014-03-14T19:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24576",
    "user": "chapoton"
}
```

we have switched to git, this is obsolete



---

archive/issue_comments_024577.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-14T19:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24577",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024578.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-15T13:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24578",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024579.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-03-19T04:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24579",
    "user": "vbraun"
}
```

Resolution: wontfix
