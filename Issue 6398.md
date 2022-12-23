# Issue 6398: shorten long doctests in sage/schemes/elliptic_curves/sha_tate.py

archive/issues_006398.json:
```json
{
    "body": "Assignee: tbd\n\nAfter this last round of merging:\n\n\n```\nsage -t -long sage/schemes/elliptic_curves/sha_tate.py\n         [891.9 s]\n```\n\n\nThis is 15 minutes, and the second longest doctest takes just over 4 minutes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6398\n\n",
    "created_at": "2009-06-24T19:31:44Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "shorten long doctests in sage/schemes/elliptic_curves/sha_tate.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6398",
    "user": "rlm"
}
```
Assignee: tbd

After this last round of merging:


```
sage -t -long sage/schemes/elliptic_curves/sha_tate.py
         [891.9 s]
```


This is 15 minutes, and the second longest doctest takes just over 4 minutes.

Issue created by migration from https://trac.sagemath.org/ticket/6398





---

archive/issue_comments_051397.json:
```json
{
    "body": "On sage.math this is:\n\n\n```\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/sha_tate.py\"\n         [161.1 s]\n```\n\n\nso this is no longer even a problem.",
    "created_at": "2009-07-09T05:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6398#issuecomment-51397",
    "user": "was"
}
```

On sage.math this is:


```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
         [161.1 s]
```


so this is no longer even a problem.



---

archive/issue_comments_051398.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-09T05:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6398#issuecomment-51398",
    "user": "was"
}
```

Resolution: fixed
