# Issue 9833: LaTeX representation of fractions still broken

archive/issues_009833.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @burcin\n\nKeywords: latex, fraction, pynac\n\nSimilarly as in #9314\n\n\n```\nsage: latex(-(x+1)/(x+2))\n\\frac{-x + 1}{x + 2}\n```\n\n\nnote the minus sign :(\n\nIssue created by migration from https://trac.sagemath.org/ticket/9834\n\n",
    "created_at": "2010-08-28T20:21:05Z",
    "labels": [
        "component: symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "LaTeX representation of fractions still broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9833",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

CC:  @burcin

Keywords: latex, fraction, pynac

Similarly as in #9314


```
sage: latex(-(x+1)/(x+2))
\frac{-x + 1}{x + 2}
```


note the minus sign :(

Issue created by migration from https://trac.sagemath.org/ticket/9834





---

archive/issue_comments_096869.json:
```json
{
    "body": "I fixed this while working on #9394 a while ago. I should have posted a new version of pynac before going on vacation, but couldn't find the time. Hopefully in the next days I'll push my changes to trac for review.",
    "created_at": "2010-08-28T20:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-96869",
    "user": "https://github.com/burcin"
}
```

I fixed this while working on #9394 a while ago. I should have posted a new version of pynac before going on vacation, but couldn't find the time. Hopefully in the next days I'll push my changes to trac for review.



---

archive/issue_comments_096870.json:
```json
{
    "body": "There is a new pynac version that fixes this at #9901, corresponding doctest fixes are included in the patch at #9394.\n\nThis ticket should be closed when those are merged.",
    "created_at": "2010-09-12T12:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-96870",
    "user": "https://github.com/burcin"
}
```

There is a new pynac version that fixes this at #9901, corresponding doctest fixes are included in the patch at #9394.

This ticket should be closed when those are merged.



---

archive/issue_comments_096871.json:
```json
{
    "body": "With inclusion of #9901, positive review.  Do not merge until #9901 is merged.  Doctests are at #9394.",
    "created_at": "2010-09-22T17:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-96871",
    "user": "https://github.com/kcrisman"
}
```

With inclusion of #9901, positive review.  Do not merge until #9901 is merged.  Doctests are at #9394.



---

archive/issue_comments_096872.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-22T17:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-96872",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096873.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T17:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-96873",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009955.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-10-06T03:19:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9833#event-9955"
}
```



---

archive/issue_comments_096874.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-06T03:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9833#issuecomment-96874",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate
