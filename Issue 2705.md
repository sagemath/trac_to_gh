# Issue 2705: random_matrix with sparse=True is very slow

archive/issues_002705.json:
```json
{
    "body": "Assignee: was\n\nCreating a 2000x200 full matrix is much faster than creating a 500x500 sparse matrix:\n\n\n```\nsage: %time A = random_matrix(ZZ,2000)\nCPU times: user 0.97 s, sys: 0.28 s, total: 1.25 s\nWall time: 1.25\n\nsage: %time B = random_matrix(ZZ,500,sparse=True)\nCPU times: user 7.20 s, sys: 0.00 s, total: 7.20 s\nWall time: 7.20\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2705\n\n",
    "created_at": "2008-03-28T18:41:29Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "random_matrix with sparse=True is very slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2705",
    "user": "dfdeshom"
}
```
Assignee: was

Creating a 2000x200 full matrix is much faster than creating a 500x500 sparse matrix:


```
sage: %time A = random_matrix(ZZ,2000)
CPU times: user 0.97 s, sys: 0.28 s, total: 1.25 s
Wall time: 1.25

sage: %time B = random_matrix(ZZ,500,sparse=True)
CPU times: user 7.20 s, sys: 0.00 s, total: 7.20 s
Wall time: 7.20
```


Issue created by migration from https://trac.sagemath.org/ticket/2705





---

archive/issue_comments_018657.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T23:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2705#issuecomment-18657",
    "user": "malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_018658.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-06-15T06:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2705#issuecomment-18658",
    "user": "ryan"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_018659.json:
```json
{
    "body": "could it have anything to do with the fact that a random matrix is not sparse in nature?",
    "created_at": "2011-06-15T06:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2705#issuecomment-18659",
    "user": "ryan"
}
```

could it have anything to do with the fact that a random matrix is not sparse in nature?



---

archive/issue_comments_018660.json:
```json
{
    "body": "I noted that even when we specify the density of nonzero entries, a sparse matrix still takes a significant amount of time.\n\n\n```\nsage: time B = random_matrix(ZZ, 2000, density=.05, sparse=True)\nTime: CPU 7.02 s, Wall: 8.77 s\nsage: time A = random_matrix(ZZ 2000, density=.05, sparse=False)\nTime: CPU 1.20 s, Wall: 1.70 s\n```\n",
    "created_at": "2011-06-15T06:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2705#issuecomment-18660",
    "user": "ryan"
}
```

I noted that even when we specify the density of nonzero entries, a sparse matrix still takes a significant amount of time.


```
sage: time B = random_matrix(ZZ, 2000, density=.05, sparse=True)
Time: CPU 7.02 s, Wall: 8.77 s
sage: time A = random_matrix(ZZ 2000, density=.05, sparse=False)
Time: CPU 1.20 s, Wall: 1.70 s
```




---

archive/issue_comments_018661.json:
```json
{
    "body": "Well...apparently density=.05 is too dense for a 2000x2000 matrix\n\n\n```\nsage: time A = random_matrix(QQ, 2000, density=.01, sparse=True)\nTime: CPU 2.17 s, Wall: 2.82 s\nsage: time A = random_matrix(QQ, 2000, density=.01, sparse=False)\nTime: CPU 3.25 s, Wall: 3.57 s\n```\n\n\nHowever, sparse matrices in sage are in need of some tender loving care (according to some other sage devs)",
    "created_at": "2011-06-15T07:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2705#issuecomment-18661",
    "user": "ryan"
}
```

Well...apparently density=.05 is too dense for a 2000x2000 matrix


```
sage: time A = random_matrix(QQ, 2000, density=.01, sparse=True)
Time: CPU 2.17 s, Wall: 2.82 s
sage: time A = random_matrix(QQ, 2000, density=.01, sparse=False)
Time: CPU 3.25 s, Wall: 3.57 s
```


However, sparse matrices in sage are in need of some tender loving care (according to some other sage devs)



---

archive/issue_comments_018662.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd31\".",
    "created_at": "2011-06-15T07:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2705",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2705#issuecomment-18662",
    "user": "ryan"
}
```

Changing keywords from "" to "sd31".
