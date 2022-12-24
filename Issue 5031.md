# Issue 5031: get doctesting of matrix/misc.pyx up to 100%; also make A.lift() 20 times faster by moving a "gem"

archive/issues_005031.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5031\n\n",
    "created_at": "2009-01-20T05:46:23Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "get doctesting of matrix/misc.pyx up to 100%; also make A.lift() 20 times faster by moving a \"gem\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5031",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/5031





---

archive/issue_comments_038318.json:
```json
{
    "body": "Some timings\n\n```\nBEFORE:\nsage: a = random_matrix(GF(19),500)\nsage: time b = a.lift()\nCPU times: user 0.93 s, sys: 0.02 s, total: 0.95 s\nWall time: 0.96 s\nsage: a = random_matrix(GF(19),200,sparse=True)\nsage: time b = a.lift()\nCPU times: user 0.81 s, sys: 0.01 s, total: 0.82 s\nWall time: 0.82 s\n\nAFTER:\nsage: a = random_matrix(GF(19),500)\nsage: time b = a.lift()\nCPU times: user 0.02 s, sys: 0.01 s, total: 0.04 s\nWall time: 0.04 s\nsage: a = random_matrix(GF(19),200,sparse=True)\nsage: time b = a.lift()\nCPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s\nWall time: 0.04 s\nsage: 0.82/0.04\n20.5000000000000\n```\n",
    "created_at": "2009-01-20T05:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38318",
    "user": "was"
}
```

Some timings

```
BEFORE:
sage: a = random_matrix(GF(19),500)
sage: time b = a.lift()
CPU times: user 0.93 s, sys: 0.02 s, total: 0.95 s
Wall time: 0.96 s
sage: a = random_matrix(GF(19),200,sparse=True)
sage: time b = a.lift()
CPU times: user 0.81 s, sys: 0.01 s, total: 0.82 s
Wall time: 0.82 s

AFTER:
sage: a = random_matrix(GF(19),500)
sage: time b = a.lift()
CPU times: user 0.02 s, sys: 0.01 s, total: 0.04 s
Wall time: 0.04 s
sage: a = random_matrix(GF(19),200,sparse=True)
sage: time b = a.lift()
CPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s
Wall time: 0.04 s
sage: 0.82/0.04
20.5000000000000
```




---

archive/issue_comments_038319.json:
```json
{
    "body": "this is against sage-3.3.alpha0",
    "created_at": "2009-01-20T06:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38319",
    "user": "was"
}
```

this is against sage-3.3.alpha0



---

archive/issue_comments_038320.json:
```json
{
    "body": "Attachment [trac_5031.patch](tarball://root/attachments/some-uuid/ticket5031/trac_5031.patch) by ddrake created at 2009-01-20 09:11:45\n\nI get even larger speedups (factor of 21 to 23), the doctest coverage for all 5 touched files is increased, and the code is fine. Positive review.",
    "created_at": "2009-01-20T09:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38320",
    "user": "ddrake"
}
```

Attachment [trac_5031.patch](tarball://root/attachments/some-uuid/ticket5031/trac_5031.patch) by ddrake created at 2009-01-20 09:11:45

I get even larger speedups (factor of 21 to 23), the doctest coverage for all 5 touched files is increased, and the code is fine. Positive review.



---

archive/issue_comments_038321.json:
```json
{
    "body": "You got to it while I was sleeping... The code looks good to me too, and this cleans things up a lot. +1",
    "created_at": "2009-01-20T18:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38321",
    "user": "robertwb"
}
```

You got to it while I was sleeping... The code looks good to me too, and this cleans things up a lot. +1



---

archive/issue_comments_038322.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T09:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38322",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_038323.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38323",
    "user": "mabshoff"
}
```

Resolution: fixed
