# Issue 9981: Allow plotting more complex points

archive/issues_009981.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @jasongrout @videlec\n\nSee #4838 and #8082 for the first addition of this.  Unfortunately, it only supports things like `CC`:\n\n\n```\nsage: point([CC(1.00000000000000 + 0.500000000000000*I)]) # works\nsage: point([1.00000000000000 + 0.500000000000000*I]) # nope\n```\n\n\nA little experimentation suggests that Python complexes also aren't supported.  Fixing this should also allow plotting `line`s in the complex plane pretty easily.\n\nI'm labeling this a defect rather than enhancement because it would be confusing not to have both.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9982\n\n",
    "created_at": "2010-09-23T18:21:33Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Allow plotting more complex points",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9981",
    "user": "https://github.com/kcrisman"
}
```
Assignee: jason, was

CC:  @jasongrout @videlec

See #4838 and #8082 for the first addition of this.  Unfortunately, it only supports things like `CC`:


```
sage: point([CC(1.00000000000000 + 0.500000000000000*I)]) # works
sage: point([1.00000000000000 + 0.500000000000000*I]) # nope
```


A little experimentation suggests that Python complexes also aren't supported.  Fixing this should also allow plotting `line`s in the complex plane pretty easily.

I'm labeling this a defect rather than enhancement because it would be confusing not to have both.

Issue created by migration from https://trac.sagemath.org/ticket/9982





---

archive/issue_comments_100145.json:
```json
{
    "body": "Notice that \n\n```\nsage: list_plot([1.00000000000000 + 0.500000000000000*I])\n```\n\ndoes work.",
    "created_at": "2012-07-07T03:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9981#issuecomment-100145",
    "user": "https://github.com/kcrisman"
}
```

Notice that 

```
sage: list_plot([1.00000000000000 + 0.500000000000000*I])
```

does work.



---

archive/issue_comments_100146.json:
```json
{
    "body": "That's great that you cced me ! I would like to mention that the result of the two following commands are different (and should not be)\n\n```\nsage: point2d([CC(0),CC(1)])      # two points at coordinates (0,0) and (1,0)\nsage: point2d([CDF(0),CDF(1)])    # one point at coordinate (0,1)\n```\n\nPerhaps that will be resolved with this ticket.",
    "created_at": "2013-05-24T20:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9981#issuecomment-100146",
    "user": "https://github.com/videlec"
}
```

That's great that you cced me ! I would like to mention that the result of the two following commands are different (and should not be)

```
sage: point2d([CC(0),CC(1)])      # two points at coordinates (0,0) and (1,0)
sage: point2d([CDF(0),CDF(1)])    # one point at coordinate (0,1)
```

Perhaps that will be resolved with this ticket.
