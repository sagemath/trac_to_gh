# Issue 4824: speed up conversion of matrices from sage to pari

archive/issues_004824.json:
```json
{
    "body": "Assignee: was\n\nThis is kind of sad, given that pari(...) is done entirely in C-level Cython compiled code in memory, and the magma(...) conversion is done using pexpect and the file system!\n\n```\nsage: a = random_matrix(ZZ,1000,x=-10,y=10)\nsage: time m = magma(a)\nCPU times: user 0.14 s, sys: 0.02 s, total: 0.16 s\nWall time: 0.36 s\nsage: time b= pari(a)\nCPU times: user 21.51 s, sys: 0.72 s, total: 22.23 s\nWall time: 22.24 s\n```\n\n\nFixing this will help with some algorithms, such as Hermite form. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4824\n\n",
    "created_at": "2008-12-18T01:25:11Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "speed up conversion of matrices from sage to pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4824",
    "user": "was"
}
```
Assignee: was

This is kind of sad, given that pari(...) is done entirely in C-level Cython compiled code in memory, and the magma(...) conversion is done using pexpect and the file system!

```
sage: a = random_matrix(ZZ,1000,x=-10,y=10)
sage: time m = magma(a)
CPU times: user 0.14 s, sys: 0.02 s, total: 0.16 s
Wall time: 0.36 s
sage: time b= pari(a)
CPU times: user 21.51 s, sys: 0.72 s, total: 22.23 s
Wall time: 22.24 s
```


Fixing this will help with some algorithms, such as Hermite form. 

Issue created by migration from https://trac.sagemath.org/ticket/4824





---

archive/issue_comments_036578.json:
```json
{
    "body": "This was fixed at some point:\n\n```\nsage: a = random_matrix(ZZ, 1000, x=-10, y=10)\nsage: %time p = pari(a)\nCPU times: user 0.20 s, sys: 0.36 s, total: 0.56 s\nWall time: 1.07 s\nsage: a = random_matrix(ZZ, 1000, x=-10, y=10)\nsage: %time p = pari(a)\nCPU times: user 0.17 s, sys: 0.02 s, total: 0.19 s\nWall time: 0.24 s\n```\n",
    "created_at": "2013-04-02T15:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4824#issuecomment-36578",
    "user": "tscrim"
}
```

This was fixed at some point:

```
sage: a = random_matrix(ZZ, 1000, x=-10, y=10)
sage: %time p = pari(a)
CPU times: user 0.20 s, sys: 0.36 s, total: 0.56 s
Wall time: 1.07 s
sage: a = random_matrix(ZZ, 1000, x=-10, y=10)
sage: %time p = pari(a)
CPU times: user 0.17 s, sys: 0.02 s, total: 0.19 s
Wall time: 0.24 s
```




---

archive/issue_comments_036579.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-02T15:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4824#issuecomment-36579",
    "user": "tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036580.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-09T14:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4824#issuecomment-36580",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036581.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-04-10T08:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4824",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4824#issuecomment-36581",
    "user": "jdemeyer"
}
```

Resolution: worksforme
