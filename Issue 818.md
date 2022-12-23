# Issue 818: Convert of prod to Cython

archive/issues_000818.json:
```json
{
    "body": "Assignee: somebody\n\nI rewrote the prod function in Cython.  Some timings illustrating the improvement:\n\nBEFORE:\nsage: l=[1]*15\nsage: time for i in xrange(10000): _=prod(l)\nCPU times: user 0.18 s, sys: 0.01 s, total: 0.19 s\nWall time: 0.19\n\nAFTER:\nsage: l=[1]*15\nsage: time for i in xrange(10000): _=prod(l)\nCPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s\nWall time: 0.06\n\nThose times make it look pretty good, but most real-world multiplications are very dominated by the actual arithmetic.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/818\n\n",
    "created_at": "2007-10-04T01:33:44Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "Convert of prod to Cython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/818",
    "user": "jbmohler"
}
```
Assignee: somebody

I rewrote the prod function in Cython.  Some timings illustrating the improvement:

BEFORE:
sage: l=[1]*15
sage: time for i in xrange(10000): _=prod(l)
CPU times: user 0.18 s, sys: 0.01 s, total: 0.19 s
Wall time: 0.19

AFTER:
sage: l=[1]*15
sage: time for i in xrange(10000): _=prod(l)
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06

Those times make it look pretty good, but most real-world multiplications are very dominated by the actual arithmetic.


Issue created by migration from https://trac.sagemath.org/ticket/818





---

archive/issue_comments_005080.json:
```json
{
    "body": "Attachment\n\nconvert to cython bundle",
    "created_at": "2007-10-04T01:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/818#issuecomment-5080",
    "user": "jbmohler"
}
```

Attachment

convert to cython bundle



---

archive/issue_comments_005081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T18:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/818#issuecomment-5081",
    "user": "was"
}
```

Resolution: fixed
