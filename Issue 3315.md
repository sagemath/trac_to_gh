# Issue 3315: parametric plot should accept a function that returns a tuple

archive/issues_003315.json:
```json
{
    "body": "Assignee: was\n\nKeywords: parametric_plot\n\nSubject says it all.  I (Marshall Hampton) will work on this if I have time; should be pretty easy.  Currently parametric_plot wants a tuple of functions; I think it should do that OR accept a function that returns a tuple.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3315\n\n",
    "created_at": "2008-05-27T19:06:22Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "parametric plot should accept a function that returns a tuple",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3315",
    "user": "mhampton"
}
```
Assignee: was

Keywords: parametric_plot

Subject says it all.  I (Marshall Hampton) will work on this if I have time; should be pretty easy.  Currently parametric_plot wants a tuple of functions; I think it should do that OR accept a function that returns a tuple.

Issue created by migration from https://trac.sagemath.org/ticket/3315





---

archive/issue_comments_022964.json:
```json
{
    "body": "See also #3313 for another input format parametric_plot should take: vectors.",
    "created_at": "2009-03-06T21:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3315#issuecomment-22964",
    "user": "jason"
}
```

See also #3313 for another input format parametric_plot should take: vectors.



---

archive/issue_comments_022965.json:
```json
{
    "body": "Really, parametric_plot should take functions returning any of the allowed types (tuple, list, or with #3313, vectors).",
    "created_at": "2009-03-06T21:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3315#issuecomment-22965",
    "user": "jason"
}
```

Really, parametric_plot should take functions returning any of the allowed types (tuple, list, or with #3313, vectors).



---

archive/issue_comments_022966.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> See also #3313 for another input format parametric_plot should take: vectors.\n\n#3313 has nothing to do with vectors.  And now, parametric_plot takes vectors anyway:\n\n\n```\nsage: r(t)=[t,t+1]\nsage: parametric_plot(r, (t,0,1))\n\nsage: parametric_plot(r(t), (t,0,1))\n\n```\n",
    "created_at": "2010-05-11T20:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3315#issuecomment-22966",
    "user": "jason"
}
```

Replying to [comment:1 jason]:
> See also #3313 for another input format parametric_plot should take: vectors.

#3313 has nothing to do with vectors.  And now, parametric_plot takes vectors anyway:


```
sage: r(t)=[t,t+1]
sage: parametric_plot(r, (t,0,1))

sage: parametric_plot(r(t), (t,0,1))

```

