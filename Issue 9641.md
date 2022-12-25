# Issue 9641: Race condition with sage -tp

archive/issues_009641.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @craigcitro\n\nAll files are named .sage/tmp/filename. At high parallelism, there are often conflicts (e.g. all.py, proof.py, ...) that result in untested code and spurious errors. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9641\n\n",
    "created_at": "2010-07-29T21:34:32Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Race condition with sage -tp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9641",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza

CC:  @craigcitro

All files are named .sage/tmp/filename. At high parallelism, there are often conflicts (e.g. all.py, proof.py, ...) that result in untested code and spurious errors. 

Issue created by migration from https://trac.sagemath.org/ticket/9641





---

archive/issue_comments_093302.json:
```json
{
    "body": "Changing component from algebra to doctest.",
    "created_at": "2010-09-02T11:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9641#issuecomment-93302",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to doctest.



---

archive/issue_comments_093303.json:
```json
{
    "body": "Changing assignee from @aghitza to mvngu.",
    "created_at": "2010-09-02T11:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9641#issuecomment-93303",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @aghitza to mvngu.



---

archive/issue_comments_093304.json:
```json
{
    "body": "Is this a duplicate of #9739 ? (This one is older, but #9739 has work in progress.)",
    "created_at": "2011-01-11T01:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9641#issuecomment-93304",
    "user": "https://github.com/wjp"
}
```

Is this a duplicate of #9739 ? (This one is older, but #9739 has work in progress.)



---

archive/issue_comments_093305.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-01-11T06:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9641#issuecomment-93305",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
