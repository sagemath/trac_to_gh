# Issue 4651: re-enable caching of cython dependencies during build

archive/issues_004651.json:
```json
{
    "body": "Assignee: craigcitro\n\nWe decided to temporarily disable the caching of the cython dependencies during the build, simply because it was causing so much grief. However, this should be re-enabled once someone takes the time to sit down and work out the last kinks. In particular, **removing** files from the sage tree and rebuilding tends to cause exceptions.\n\nSee `$SAGE_ROOT/devel/sage/setup.py` for some comments, and to play with this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4651\n\n",
    "created_at": "2008-11-29T07:05:55Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "re-enable caching of cython dependencies during build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4651",
    "user": "craigcitro"
}
```
Assignee: craigcitro

We decided to temporarily disable the caching of the cython dependencies during the build, simply because it was causing so much grief. However, this should be re-enabled once someone takes the time to sit down and work out the last kinks. In particular, **removing** files from the sage tree and rebuilding tends to cause exceptions.

See `$SAGE_ROOT/devel/sage/setup.py` for some comments, and to play with this.

Issue created by migration from https://trac.sagemath.org/ticket/4651





---

archive/issue_comments_035004.json:
```json
{
    "body": "Dependency checking is in upstream Cython now.",
    "created_at": "2013-05-19T13:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4651#issuecomment-35004",
    "user": "jdemeyer"
}
```

Dependency checking is in upstream Cython now.



---

archive/issue_comments_035005.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4651#issuecomment-35005",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_035006.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4651#issuecomment-35006",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_035007.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-21T07:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4651",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4651#issuecomment-35007",
    "user": "jdemeyer"
}
```

Resolution: invalid
