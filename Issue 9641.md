# Issue 9641: Race condition with sage -tp

archive/issues_009641.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  craigcitro\n\nAll files are named .sage/tmp/filename. At high parallelism, there are often conflicts (e.g. all.py, proof.py, ...) that result in untested code and spurious errors. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9641\n\n",
    "created_at": "2010-07-29T21:34:32Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Race condition with sage -tp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9641",
    "user": "robertwb"
}
```
Assignee: AlexGhitza

CC:  craigcitro

All files are named .sage/tmp/filename. At high parallelism, there are often conflicts (e.g. all.py, proof.py, ...) that result in untested code and spurious errors. 

Issue created by migration from https://trac.sagemath.org/ticket/9641





---

archive/issue_comments_093458.json:
```json
{
    "body": "Changing component from algebra to doctest.",
    "created_at": "2010-09-02T11:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9641#issuecomment-93458",
    "user": "AlexGhitza"
}
```

Changing component from algebra to doctest.



---

archive/issue_comments_093459.json:
```json
{
    "body": "Changing assignee from AlexGhitza to mvngu.",
    "created_at": "2010-09-02T11:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9641#issuecomment-93459",
    "user": "AlexGhitza"
}
```

Changing assignee from AlexGhitza to mvngu.



---

archive/issue_comments_093460.json:
```json
{
    "body": "Is this a duplicate of #9739 ? (This one is older, but #9739 has work in progress.)",
    "created_at": "2011-01-11T01:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9641#issuecomment-93460",
    "user": "wjp"
}
```

Is this a duplicate of #9739 ? (This one is older, but #9739 has work in progress.)



---

archive/issue_comments_093461.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-01-11T06:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9641#issuecomment-93461",
    "user": "jdemeyer"
}
```

Resolution: duplicate
