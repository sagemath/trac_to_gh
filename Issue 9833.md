# Issue 9833: LaTeX representation of fractions still broken

archive/issues_009833.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  burcin\n\nKeywords: latex, fraction, pynac\n\nSimilarly as in #9314\n\n\n```\nsage: latex(-(x+1)/(x+2))\n\\frac{-x + 1}{x + 2}\n```\n\n\nnote the minus sign :(\n\nIssue created by migration from https://trac.sagemath.org/ticket/9834\n\n",
    "created_at": "2010-08-28T20:21:05Z",
    "labels": [
        "symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "LaTeX representation of fractions still broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9833",
    "user": "robert.marik"
}
```
Assignee: burcin

CC:  burcin

Keywords: latex, fraction, pynac

Similarly as in #9314


```
sage: latex(-(x+1)/(x+2))
\frac{-x + 1}{x + 2}
```


note the minus sign :(

Issue created by migration from https://trac.sagemath.org/ticket/9834





---

archive/issue_comments_097028.json:
```json
{
    "body": "I fixed this while working on #9394 a while ago. I should have posted a new version of pynac before going on vacation, but couldn't find the time. Hopefully in the next days I'll push my changes to trac for review.",
    "created_at": "2010-08-28T20:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-97028",
    "user": "burcin"
}
```

I fixed this while working on #9394 a while ago. I should have posted a new version of pynac before going on vacation, but couldn't find the time. Hopefully in the next days I'll push my changes to trac for review.



---

archive/issue_comments_097029.json:
```json
{
    "body": "There is a new pynac version that fixes this at #9901, corresponding doctest fixes are included in the patch at #9394.\n\nThis ticket should be closed when those are merged.",
    "created_at": "2010-09-12T12:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-97029",
    "user": "burcin"
}
```

There is a new pynac version that fixes this at #9901, corresponding doctest fixes are included in the patch at #9394.

This ticket should be closed when those are merged.



---

archive/issue_comments_097030.json:
```json
{
    "body": "With inclusion of #9901, positive review.  Do not merge until #9901 is merged.  Doctests are at #9394.",
    "created_at": "2010-09-22T17:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-97030",
    "user": "kcrisman"
}
```

With inclusion of #9901, positive review.  Do not merge until #9901 is merged.  Doctests are at #9394.



---

archive/issue_comments_097031.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-22T17:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-97031",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097032.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T17:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-97032",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097033.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-06T03:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-97033",
    "user": "mpatel"
}
```

Resolution: duplicate
