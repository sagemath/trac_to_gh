# Issue 889: 2.8.7-alpha0: doctest failure in schemes/elliptic_curves/lseries_ell.py (tiny differences in answer)

archive/issues_000889.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nFile \"lseries_ell.py\", line 59:\n    sage: L.taylor_series(series_prec=3)\nExpected:\n    -1.28158145691931e-23 + (7.26268290635587e-24)*z + 0.759316500288427*z^2 + O(z^3)\nGot:\n    -2.69129566562797e-23 + (1.52514901968783e-23)*z + 0.759316500288427*z^2 + O(z^3)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/889\n\n",
    "created_at": "2007-10-13T20:39:16Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "2.8.7-alpha0: doctest failure in schemes/elliptic_curves/lseries_ell.py (tiny differences in answer)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/889",
    "user": "cwitty"
}
```
Assignee: failure


```
File "lseries_ell.py", line 59:
    sage: L.taylor_series(series_prec=3)
Expected:
    -1.28158145691931e-23 + (7.26268290635587e-24)*z + 0.759316500288427*z^2 + O(z^3)
Got:
    -2.69129566562797e-23 + (1.52514901968783e-23)*z + 0.759316500288427*z^2 + O(z^3)
```



Issue created by migration from https://trac.sagemath.org/ticket/889





---

archive/issue_comments_005489.json:
```json
{
    "body": "Attachment\n\nFixes the doctest",
    "created_at": "2007-10-14T03:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/889#issuecomment-5489",
    "user": "roed"
}
```

Attachment

Fixes the doctest



---

archive/issue_comments_005490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T22:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/889#issuecomment-5490",
    "user": "was"
}
```

Resolution: fixed
