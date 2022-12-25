# Issue 5031: get doctesting of matrix/misc.pyx up to 100%; also make A.lift() 20 times faster by moving a "gem"

archive/issues_005031.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5031\n\n",
    "created_at": "2009-01-20T05:46:23Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "get doctesting of matrix/misc.pyx up to 100%; also make A.lift() 20 times faster by moving a \"gem\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5031",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/5031





---

archive/issue_comments_038246.json:
```json
{
    "body": "Some timings\n\n```\nBEFORE:\nsage: a = random_matrix(GF(19),500)\nsage: time b = a.lift()\nCPU times: user 0.93 s, sys: 0.02 s, total: 0.95 s\nWall time: 0.96 s\nsage: a = random_matrix(GF(19),200,sparse=True)\nsage: time b = a.lift()\nCPU times: user 0.81 s, sys: 0.01 s, total: 0.82 s\nWall time: 0.82 s\n\nAFTER:\nsage: a = random_matrix(GF(19),500)\nsage: time b = a.lift()\nCPU times: user 0.02 s, sys: 0.01 s, total: 0.04 s\nWall time: 0.04 s\nsage: a = random_matrix(GF(19),200,sparse=True)\nsage: time b = a.lift()\nCPU times: user 0.04 s, sys: 0.00 s, total: 0.04 s\nWall time: 0.04 s\nsage: 0.82/0.04\n20.5000000000000\n```\n",
    "created_at": "2009-01-20T05:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38246",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_038247.json:
```json
{
    "body": "this is against sage-3.3.alpha0",
    "created_at": "2009-01-20T06:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38247",
    "user": "https://github.com/williamstein"
}
```

this is against sage-3.3.alpha0



---

archive/issue_comments_038248.json:
```json
{
    "body": "Attachment [trac_5031.patch](tarball://root/attachments/some-uuid/ticket5031/trac_5031.patch) by @dandrake created at 2009-01-20 09:11:45\n\nI get even larger speedups (factor of 21 to 23), the doctest coverage for all 5 touched files is increased, and the code is fine. Positive review.",
    "created_at": "2009-01-20T09:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38248",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_5031.patch](tarball://root/attachments/some-uuid/ticket5031/trac_5031.patch) by @dandrake created at 2009-01-20 09:11:45

I get even larger speedups (factor of 21 to 23), the doctest coverage for all 5 touched files is increased, and the code is fine. Positive review.



---

archive/issue_comments_038249.json:
```json
{
    "body": "You got to it while I was sleeping... The code looks good to me too, and this cleans things up a lot. +1",
    "created_at": "2009-01-20T18:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38249",
    "user": "https://github.com/robertwb"
}
```

You got to it while I was sleeping... The code looks good to me too, and this cleans things up a lot. +1



---

archive/issue_comments_038250.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T09:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_events_005275.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T09:06:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5031#event-5275"
}
```



---

archive/issue_comments_038251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5031",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5031#issuecomment-38251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
