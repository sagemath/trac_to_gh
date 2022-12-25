# Issue 6308: [with spkg, needs review] Fix scipy spkg to play nicely with gfortran and g95

archive/issues_006308.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jasongrout jkantor wstein\n\nKeywords: scipy\n\nThe new `scipy-0.7.spkg` from #3391 is great -- except that it accidentally forgets to include a fix to `scipy.optimize.optimize` if `gfortran` is used instead of `g95`. There's a new spkg up that fixes that here: \n\n  http://sage.math.washington.edu/scratch/craigcitro/patches/scipy-0.7.p1.spkg \n\nIndeed, I spoke with Jason Grout, and he confirmed that the new `optimize.py` should be patched in regardless of what fortran compiler we use.\n\nI'm adding a few potential reviewers to the cc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6308\n\n",
    "created_at": "2009-06-16T06:32:32Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with spkg, needs review] Fix scipy spkg to play nicely with gfortran and g95",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6308",
    "user": "https://github.com/craigcitro"
}
```
Assignee: mabshoff

CC:  @jasongrout jkantor wstein

Keywords: scipy

The new `scipy-0.7.spkg` from #3391 is great -- except that it accidentally forgets to include a fix to `scipy.optimize.optimize` if `gfortran` is used instead of `g95`. There's a new spkg up that fixes that here: 

  http://sage.math.washington.edu/scratch/craigcitro/patches/scipy-0.7.p1.spkg 

Indeed, I spoke with Jason Grout, and he confirmed that the new `optimize.py` should be patched in regardless of what fortran compiler we use.

I'm adding a few potential reviewers to the cc.

Issue created by migration from https://trac.sagemath.org/ticket/6308





---

archive/issue_comments_050252.json:
```json
{
    "body": "Oh, I should say: I've tested this on both `sage.math` and `cleo` on skynet, which uses `gfortran` -- it worked fine in both cases.",
    "created_at": "2009-06-16T06:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6308#issuecomment-50252",
    "user": "https://github.com/craigcitro"
}
```

Oh, I should say: I've tested this on both `sage.math` and `cleo` on skynet, which uses `gfortran` -- it worked fine in both cases.



---

archive/issue_comments_050253.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-18T02:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6308#issuecomment-50253",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed



---

archive/issue_events_014750.json:
```json
{
    "actor": "https://github.com/craigcitro",
    "created_at": "2009-06-18T02:06:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6308",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6308#event-14750"
}
```
