# Issue 7286: After installing sphinx-0.6.3.p1.spkg, error occurs during docbuild

archive/issues_007286.json:
```json
{
    "body": "Assignee: mabshoff\n\n> 11:24 < williamstein> I tried \"sage -upgrade\" on a clean install (the systemwide one) on geom.math.\n\n> 11:24 < williamstein> It fails with:\n\n> 11:24 < williamstein>   File \"/usr/local/sage/local/lib/python2.6/site-packages/Sphinx-0.6.3-py2.6.egg/sphinx/environment.py\", line 204, in frompickle\n\n> 11:24 < williamstein>     env = pickle.load(picklefile)\n\n> 11:24 < williamstein> AttributeError: 'module' object has no attribute 'RedirStream'\n\nIssue created by migration from https://trac.sagemath.org/ticket/7286\n\n",
    "created_at": "2009-10-25T03:53:47Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "After installing sphinx-0.6.3.p1.spkg, error occurs during docbuild",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7286",
    "user": "https://github.com/TimDumol"
}
```
Assignee: mabshoff

> 11:24 < williamstein> I tried "sage -upgrade" on a clean install (the systemwide one) on geom.math.

> 11:24 < williamstein> It fails with:

> 11:24 < williamstein>   File "/usr/local/sage/local/lib/python2.6/site-packages/Sphinx-0.6.3-py2.6.egg/sphinx/environment.py", line 204, in frompickle

> 11:24 < williamstein>     env = pickle.load(picklefile)

> 11:24 < williamstein> AttributeError: 'module' object has no attribute 'RedirStream'

Issue created by migration from https://trac.sagemath.org/ticket/7286





---

archive/issue_comments_060519.json:
```json
{
    "body": "Has the updated package: http://sage.math.washington.edu/home/timdumol/sphinx-0.6.3.p2.spkg",
    "created_at": "2009-10-25T03:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7286#issuecomment-60519",
    "user": "https://github.com/TimDumol"
}
```

Has the updated package: http://sage.math.washington.edu/home/timdumol/sphinx-0.6.3.p2.spkg



---

archive/issue_comments_060520.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-25T03:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7286#issuecomment-60520",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060521.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-25T04:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7286#issuecomment-60521",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007509.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-25T04:21:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7286",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7286#event-7509"
}
```



---

archive/issue_comments_060522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-25T04:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7286#issuecomment-60522",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
