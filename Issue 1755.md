# Issue 1755: Hook block matrices into matrix(...) command

archive/issues_001755.json:
```json
{
    "body": "Assignee: was\n\nAdd the ability to access the functionality of #1732 to the default matrix(...) constructor.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1755\n\n",
    "created_at": "2008-01-11T03:17:59Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Hook block matrices into matrix(...) command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1755",
    "user": "robertwb"
}
```
Assignee: was

Add the ability to access the functionality of #1732 to the default matrix(...) constructor.

Issue created by migration from https://trac.sagemath.org/ticket/1755





---

archive/issue_comments_011077.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T22:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1755#issuecomment-11077",
    "user": "malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_011078.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-05-13T15:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1755#issuecomment-11078",
    "user": "@black-stones"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011079.json:
```json
{
    "body": "This is already implemented as block_matrix()\n\n\n```\nsage: A = random_matrix(ZZ, 2)\nsage: B = random_matrix(ZZ, 2)\nsage: C = random_matrix(ZZ, 2)\nsage: D = random_matrix(ZZ, 2)\nsage: block_matrix( [[A, B], [C, D]] )\n[  1  -3| -1  -1]\n[  0   0|  1   1]\n[-------+-------]\n[  0   0| -5   1]\n[ -1   0|-10  31]\n```\n\n\nI don't think matrix() should create block matrices. It's possible that one would want a matrix of matrices rather than to merge the matrices together.",
    "created_at": "2018-05-13T15:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1755#issuecomment-11079",
    "user": "@black-stones"
}
```

This is already implemented as block_matrix()


```
sage: A = random_matrix(ZZ, 2)
sage: B = random_matrix(ZZ, 2)
sage: C = random_matrix(ZZ, 2)
sage: D = random_matrix(ZZ, 2)
sage: block_matrix( [[A, B], [C, D]] )
[  1  -3| -1  -1]
[  0   0|  1   1]
[-------+-------]
[  0   0| -5   1]
[ -1   0|-10  31]
```


I don't think matrix() should create block matrices. It's possible that one would want a matrix of matrices rather than to merge the matrices together.



---

archive/issue_comments_011080.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-05-31T07:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1755#issuecomment-11080",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011081.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1755#issuecomment-11081",
    "user": "embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.



---

archive/issue_comments_011082.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1755",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1755#issuecomment-11082",
    "user": "embray"
}
```

Resolution: invalid
