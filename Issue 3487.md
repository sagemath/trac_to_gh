# Issue 3487: mercurial and sage

archive/issues_003487.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen sage comes up it announces:\n\nLoading SAGE library. Current Mercurial branch is: worldDomination\n\nturns out, this is the current \"clone\"... when you are using \"hg branches\" in your clone it would be nice for it to say something like:\n\nLoading SAGE library. Current Mercurial clone is: worldDomination on branch: riemannProof\n\nIssue created by migration from https://trac.sagemath.org/ticket/3487\n\n",
    "created_at": "2008-06-20T21:02:04Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "mercurial and sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3487",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```
Assignee: @williamstein

When sage comes up it announces:

Loading SAGE library. Current Mercurial branch is: worldDomination

turns out, this is the current "clone"... when you are using "hg branches" in your clone it would be nice for it to say something like:

Loading SAGE library. Current Mercurial clone is: worldDomination on branch: riemannProof

Issue created by migration from https://trac.sagemath.org/ticket/3487





---

archive/issue_comments_024525.json:
```json
{
    "body": "In thinking about it, I think this is more general.\n\nSo, one clones using sage -clone worldDomination\n\nand then one asks what branch one is on with sage -branch\n\nbut, we should be able to clone and branch with the right syntax.  given the current switches, we need to be careful, but we should be able to clone and branch with switches to sage and ask where we are.\n\nso, sage -branch could simply spit out clone and branch... but \"sage -b\" is an issue",
    "created_at": "2008-06-20T21:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24525",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```

In thinking about it, I think this is more general.

So, one clones using sage -clone worldDomination

and then one asks what branch one is on with sage -branch

but, we should be able to clone and branch with the right syntax.  given the current switches, we need to be careful, but we should be able to clone and branch with switches to sage and ask where we are.

so, sage -branch could simply spit out clone and branch... but "sage -b" is an issue



---

archive/issue_comments_024526.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24526",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_024527.json:
```json
{
    "body": "we have switched to git, this is obsolete",
    "created_at": "2014-03-14T19:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24527",
    "user": "https://github.com/fchapoton"
}
```

we have switched to git, this is obsolete



---

archive/issue_comments_024528.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-14T19:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24528",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024529.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-15T13:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24529",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024530.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-03-19T04:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3487#issuecomment-24530",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_003707.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-03-19T04:41:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3487",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3487#event-3707"
}
```
