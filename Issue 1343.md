# Issue 1343: singular factorize is randomly slow

archive/issues_001343.json:
```json
{
    "body": "Assignee: @malb\n\nSingular's factorize command is immensely slow at times, but other times it is decent.  I'd not report this as a bug except for the fact that it appears that some tuning of something might fix this.\n\nRun this in singular (binary 3-0-4 from upstream as well):\n\n```\nring R=0,(p10,g0,g1,g2,g3,g4,X1,X2),dp;\npoly t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1;\nfactorize(t);\n```\n\nRepeat the factorize command a couple of times.  You'll get extreme fluctation on the amount of time required to factor (nearly instantaneous all the way out to 5-10 minutes!).\n\nObviously, sage demonstrates the same bizarre timing statistics:\n\n```\nsage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=QQ[]\nsage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1\nsage: time _=t.factor()\nCPU times: user 25.63 s, sys: 0.02 s, total: 25.65 s\nWall time: 26.18\nsage: time _=t.factor()\nCPU times: user 5.95 s, sys: 0.00 s, total: 5.95 s\nWall time: 5.95\nsage: time _=t.factor()\nCPU times: user 310.76 s, sys: 0.21 s, total: 310.97 s\nWall time: 311.65\n```\n\n\nI've reported this to the upstream forum as well (with no response so far):\nhttp://singular.mathematik.uni-kl.de/forum/viewtopic.php?t=1652\nI also just now submitted the bug through the singular bug request form.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1343\n\n",
    "created_at": "2007-11-30T15:12:45Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "singular factorize is randomly slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1343",
    "user": "jbmohler"
}
```
Assignee: @malb

Singular's factorize command is immensely slow at times, but other times it is decent.  I'd not report this as a bug except for the fact that it appears that some tuning of something might fix this.

Run this in singular (binary 3-0-4 from upstream as well):

```
ring R=0,(p10,g0,g1,g2,g3,g4,X1,X2),dp;
poly t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1;
factorize(t);
```

Repeat the factorize command a couple of times.  You'll get extreme fluctation on the amount of time required to factor (nearly instantaneous all the way out to 5-10 minutes!).

Obviously, sage demonstrates the same bizarre timing statistics:

```
sage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=QQ[]
sage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1
sage: time _=t.factor()
CPU times: user 25.63 s, sys: 0.02 s, total: 25.65 s
Wall time: 26.18
sage: time _=t.factor()
CPU times: user 5.95 s, sys: 0.00 s, total: 5.95 s
Wall time: 5.95
sage: time _=t.factor()
CPU times: user 310.76 s, sys: 0.21 s, total: 310.97 s
Wall time: 311.65
```


I've reported this to the upstream forum as well (with no response so far):
http://singular.mathematik.uni-kl.de/forum/viewtopic.php?t=1652
I also just now submitted the bug through the singular bug request form.

Issue created by migration from https://trac.sagemath.org/ticket/1343





---

archive/issue_comments_008613.json:
```json
{
    "body": "It turns out Magma and Maple are very fast and everybody else is slow. \n\n\n```\n\nHere's a new 2007 paper I just found that has an algorithm for\nmultivariate polynomial factorization that the authors claims\nblows away Maple in many cases:\n\n          http://arxiv.org/abs/math/0701670v1\n\nThere are a lot of references in this paper.  So this might\nbe a very good paper to study so Sage can do something\nthat beats everybody. \n\nWilliam\n```\n",
    "created_at": "2007-12-03T17:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1343#issuecomment-8613",
    "user": "@williamstein"
}
```

It turns out Magma and Maple are very fast and everybody else is slow. 


```

Here's a new 2007 paper I just found that has an algorithm for
multivariate polynomial factorization that the authors claims
blows away Maple in many cases:

          http://arxiv.org/abs/math/0701670v1

There are a lot of references in this paper.  So this might
be a very good paper to study so Sage can do something
that beats everybody. 

William
```




---

archive/issue_comments_008614.json:
```json
{
    "body": "Please see also #2152, which has some additional easier-to-try examples, but is really a duplicate of this ticket (so I close it as a dupe).",
    "created_at": "2008-10-30T17:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1343#issuecomment-8614",
    "user": "@williamstein"
}
```

Please see also #2152, which has some additional easier-to-try examples, but is really a duplicate of this ticket (so I close it as a dupe).



---

archive/issue_comments_008615.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T20:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1343#issuecomment-8615",
    "user": "@malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_008616.json:
```json
{
    "body": "This certainly is an enhancement.",
    "created_at": "2009-01-22T20:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1343#issuecomment-8616",
    "user": "@malb"
}
```

This certainly is an enhancement.



---

archive/issue_comments_008617.json:
```json
{
    "body": "This can be closed since in sage-4.1.1 the problem is gone:\n\n```\nsage: time _=t.factor()CPU times: user 19.92 s, sys: 0.00 s, total: 19.92 s\nWall time: 19.92 s\nsage: time _=t.factor()\nCPU times: user 9.83 s, sys: 0.01 s, total: 9.84 s\nWall time: 9.84 s\nsage: time _=t.factor()\nCPU times: user 17.45 s, sys: 0.00 s, total: 17.45 s\nWall time: 17.45 s\nsage: time _=t.factor()\nCPU times: user 1.20 s, sys: 0.00 s, total: 1.20 s\nWall time: 1.21 s\nsage: time _=t.factor()\nCPU times: user 10.57 s, sys: 0.00 s, total: 10.57 s\nWall time: 10.56 s\n```\n",
    "created_at": "2009-08-17T11:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1343#issuecomment-8617",
    "user": "@williamstein"
}
```

This can be closed since in sage-4.1.1 the problem is gone:

```
sage: time _=t.factor()CPU times: user 19.92 s, sys: 0.00 s, total: 19.92 s
Wall time: 19.92 s
sage: time _=t.factor()
CPU times: user 9.83 s, sys: 0.01 s, total: 9.84 s
Wall time: 9.84 s
sage: time _=t.factor()
CPU times: user 17.45 s, sys: 0.00 s, total: 17.45 s
Wall time: 17.45 s
sage: time _=t.factor()
CPU times: user 1.20 s, sys: 0.00 s, total: 1.20 s
Wall time: 1.21 s
sage: time _=t.factor()
CPU times: user 10.57 s, sys: 0.00 s, total: 10.57 s
Wall time: 10.56 s
```




---

archive/issue_comments_008618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-17T11:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1343#issuecomment-8618",
    "user": "@williamstein"
}
```

Resolution: fixed
