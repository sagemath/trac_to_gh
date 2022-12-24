# Issue 6249: graph1.plot() + graph2.plot() doesn't zorder correctly

archive/issues_006249.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  ekirkman @rlmill @kcrisman\n\nKeywords: graph plot z order overlay\n\nLet G1 and G2 be arbitrary graphs.  G1.plot() + G2.plot() and G2.plot() + G1.plot() (notice the ordering) look the same for me, ie I cannot make one graph appear above the other.  What seems to happen is that the vertices are brought forward in the zorder, but it appears that this is done globally, not locally for the individual plot.  I claim this is a bug.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6249\n\n",
    "created_at": "2009-06-08T16:25:31Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "graph1.plot() + graph2.plot() doesn't zorder correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6249",
    "user": "@ncalexan"
}
```
Assignee: @rlmill

CC:  ekirkman @rlmill @kcrisman

Keywords: graph plot z order overlay

Let G1 and G2 be arbitrary graphs.  G1.plot() + G2.plot() and G2.plot() + G1.plot() (notice the ordering) look the same for me, ie I cannot make one graph appear above the other.  What seems to happen is that the vertices are brought forward in the zorder, but it appears that this is done globally, not locally for the individual plot.  I claim this is a bug.

Issue created by migration from https://trac.sagemath.org/ticket/6249





---

archive/issue_comments_049906.json:
```json
{
    "body": "I'd just like to add that this bothers me too.  I once tried to fix it and got confused and gave up.",
    "created_at": "2009-06-11T19:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6249#issuecomment-49906",
    "user": "mhampton"
}
```

I'd just like to add that this bothers me too.  I once tried to fix it and got confused and gave up.



---

archive/issue_comments_049907.json:
```json
{
    "body": "I disagree. If you do not specify the z-order then there is no good way of automatically figuring out what to do. Amongst the multitude of possible behaviours you could even argue that G1.plot() + G2.plot() and G2.plot() + G1.plot() should be the same as addition is commutative. \n\nJust do G1.plot(zorder=0) + G2.plot(zorder=1) or vice versa if you care about the z-ordering. \n\nI recommend to close this bug.",
    "created_at": "2009-10-08T19:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6249#issuecomment-49907",
    "user": "@vbraun"
}
```

I disagree. If you do not specify the z-order then there is no good way of automatically figuring out what to do. Amongst the multitude of possible behaviours you could even argue that G1.plot() + G2.plot() and G2.plot() + G1.plot() should be the same as addition is commutative. 

Just do G1.plot(zorder=0) + G2.plot(zorder=1) or vice versa if you care about the z-ordering. 

I recommend to close this bug.



---

archive/issue_comments_049908.json:
```json
{
    "body": "Changing component from graph theory to graphics.",
    "created_at": "2010-06-23T13:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6249#issuecomment-49908",
    "user": "@kcrisman"
}
```

Changing component from graph theory to graphics.



---

archive/issue_comments_049909.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-06-23T13:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6249#issuecomment-49909",
    "user": "@kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_049910.json:
```json
{
    "body": "#3251 seems to be related, though perhaps not a dup.",
    "created_at": "2011-06-02T03:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6249",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6249#issuecomment-49910",
    "user": "@kcrisman"
}
```

#3251 seems to be related, though perhaps not a dup.
