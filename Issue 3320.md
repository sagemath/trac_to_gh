# Issue 3320: Gap <-> Sage interface for Dense Matrices over GF(2)

archive/issues_003320.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: gap, linear algebra\n\nThis should be much faster:\n\n```\nsage: A = random_matrix(GF(2),200,200)\nsage: time Am = magma(A)\nCPU times: user 0.03 s, sys: 0.01 s, total: 0.04 s\nWall time: 0.50\nsage: time Ag = gap(A) #<-------------\nCPU times: user 10.35 s, sys: 0.63 s, total: 10.98 s\nWall time: 11.76\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3320\n\n",
    "created_at": "2008-05-28T13:26:33Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Gap <-> Sage interface for Dense Matrices over GF(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3320",
    "user": "@malb"
}
```
Assignee: @williamstein

Keywords: gap, linear algebra

This should be much faster:

```
sage: A = random_matrix(GF(2),200,200)
sage: time Am = magma(A)
CPU times: user 0.03 s, sys: 0.01 s, total: 0.04 s
Wall time: 0.50
sage: time Ag = gap(A) #<-------------
CPU times: user 10.35 s, sys: 0.63 s, total: 10.98 s
Wall time: 11.76
```


Issue created by migration from https://trac.sagemath.org/ticket/3320





---

archive/issue_comments_023018.json:
```json
{
    "body": "This seems to have been fixed at some point:\n\n```\nsage: A = random_matrix(GF(2), 200, 200)\nsage: %time Ag = gap(A)\nCPU times: user 0.38 s, sys: 0.12 s, total: 0.50 s\nWall time: 1.26 s\nsage: %time Ag = gap(A)\nCPU times: user 0.37 s, sys: 0.02 s, total: 0.40 s\nWall time: 0.58 s\nsage: %time Ag = gap(A)\nCPU times: user 0.39 s, sys: 0.02 s, total: 0.41 s\nWall time: 0.62 s\n```\n\nI can't do a comparison on my system with magma since it refuses to start for me (I'm running `5.7.beta3`).",
    "created_at": "2013-02-22T23:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3320#issuecomment-23018",
    "user": "@tscrim"
}
```

This seems to have been fixed at some point:

```
sage: A = random_matrix(GF(2), 200, 200)
sage: %time Ag = gap(A)
CPU times: user 0.38 s, sys: 0.12 s, total: 0.50 s
Wall time: 1.26 s
sage: %time Ag = gap(A)
CPU times: user 0.37 s, sys: 0.02 s, total: 0.40 s
Wall time: 0.58 s
sage: %time Ag = gap(A)
CPU times: user 0.39 s, sys: 0.02 s, total: 0.41 s
Wall time: 0.62 s
```

I can't do a comparison on my system with magma since it refuses to start for me (I'm running `5.7.beta3`).



---

archive/issue_comments_023019.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-22T23:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3320#issuecomment-23019",
    "user": "@tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023020.json:
```json
{
    "body": "Same here !\n\nNathann",
    "created_at": "2013-03-24T20:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3320#issuecomment-23020",
    "user": "@nathanncohen"
}
```

Same here !

Nathann



---

archive/issue_comments_023021.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-24T20:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3320#issuecomment-23021",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023022.json:
```json
{
    "body": "This should be duplicate/wontfix not postive_review, there's no patch.",
    "created_at": "2013-03-24T23:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3320#issuecomment-23022",
    "user": "@malb"
}
```

This should be duplicate/wontfix not postive_review, there's no patch.



---

archive/issue_comments_023023.json:
```json
{
    "body": "> This should be duplicate/wontfix not postive_review, there's no patch.\n\nOh ? But I thought we had to set the to positive_review so that Jeroen seens them and closes them ?... `O_o`\n\nNathann",
    "created_at": "2013-03-25T09:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3320#issuecomment-23023",
    "user": "@nathanncohen"
}
```

> This should be duplicate/wontfix not postive_review, there's no patch.

Oh ? But I thought we had to set the to positive_review so that Jeroen seens them and closes them ?... `O_o`

Nathann



---

archive/issue_comments_023024.json:
```json
{
    "body": "From my understanding, we need to do both since we have to verify that it is a duplicate (or wontfix/etc.).",
    "created_at": "2013-03-25T13:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3320#issuecomment-23024",
    "user": "@tscrim"
}
```

From my understanding, we need to do both since we have to verify that it is a duplicate (or wontfix/etc.).



---

archive/issue_comments_023025.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-29T18:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3320#issuecomment-23025",
    "user": "@jdemeyer"
}
```

Resolution: worksforme
