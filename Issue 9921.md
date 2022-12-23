# Issue 9921: Add release notes to SAGE_ROOT

archive/issues_009921.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  leif mvngu kcrisman\n\nleif suggested at #9433 that we add release notes to SAGE_ROOT.  Perhaps they could be produced using mvngu's [rnotes script](http://sage.math.washington.edu/home/mvngu/apps/rnotes/) (also available at [http://bitbucket.org/mvngu/rnotes/](http://bitbucket.org/mvngu/rnotes/).  We could in fact (with his permission) include that script with Sage, and then run it as part of the sage-sdist script.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9922\n\n",
    "created_at": "2010-09-16T19:57:55Z",
    "labels": [
        "distribution",
        "minor",
        "enhancement"
    ],
    "title": "Add release notes to SAGE_ROOT",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9921",
    "user": "jhpalmieri"
}
```
Assignee: tbd

CC:  leif mvngu kcrisman

leif suggested at #9433 that we add release notes to SAGE_ROOT.  Perhaps they could be produced using mvngu's [rnotes script](http://sage.math.washington.edu/home/mvngu/apps/rnotes/) (also available at [http://bitbucket.org/mvngu/rnotes/](http://bitbucket.org/mvngu/rnotes/).  We could in fact (with his permission) include that script with Sage, and then run it as part of the sage-sdist script.

Issue created by migration from https://trac.sagemath.org/ticket/9922





---

archive/issue_comments_098770.json:
```json
{
    "body": "W.r.t. `VERSION.txt`: I think a single line containing the current version (perhaps also including *\"[last] upgraded from ...\"*) in plain format should be sufficient; cf. also #9434 and `local/bin/sage-banner`.",
    "created_at": "2010-09-17T01:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9921#issuecomment-98770",
    "user": "leif"
}
```

W.r.t. `VERSION.txt`: I think a single line containing the current version (perhaps also including *"[last] upgraded from ..."*) in plain format should be sufficient; cf. also #9434 and `local/bin/sage-banner`.



---

archive/issue_comments_098771.json:
```json
{
    "body": "In sage-sdist, should we write VERSION.txt to `SAGE_ROOT`, or should we create a symlink to `spkg/standard/VERSION.txt`?",
    "created_at": "2011-09-08T19:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9921#issuecomment-98771",
    "user": "jhpalmieri"
}
```

In sage-sdist, should we write VERSION.txt to `SAGE_ROOT`, or should we create a symlink to `spkg/standard/VERSION.txt`?



---

archive/issue_comments_098772.json:
```json
{
    "body": "At the very least we could probably add the sum total changelog to `SAGE_ROOT`.  Which I notice is no longer on the website, only the individual changelogs...",
    "created_at": "2016-04-11T14:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9921#issuecomment-98772",
    "user": "kcrisman"
}
```

At the very least we could probably add the sum total changelog to `SAGE_ROOT`.  Which I notice is no longer on the website, only the individual changelogs...
