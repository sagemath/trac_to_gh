# Issue 4732: TypeError in converting from SR matrix to RR, but *only* in doctesting

archive/issues_004732.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n[17:21] <jason->  matrix(SR,[e]).change_ring(RR) works fine from the Sage command line\n[17:21] <jason-> but gives a huge type error when it is a doctest\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4732\n\n",
    "created_at": "2008-12-06T23:26:49Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "TypeError in converting from SR matrix to RR, but *only* in doctesting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4732",
    "user": "jason"
}
```
Assignee: mabshoff


```
[17:21] <jason->  matrix(SR,[e]).change_ring(RR) works fine from the Sage command line
[17:21] <jason-> but gives a huge type error when it is a doctest
```



Issue created by migration from https://trac.sagemath.org/ticket/4732





---

archive/issue_comments_035718.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-22T08:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4732#issuecomment-35718",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_035719.json:
```json
{
    "body": "Neither of us can reproduce this.  I'm going to mark this as invalid.",
    "created_at": "2009-01-22T08:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4732#issuecomment-35719",
    "user": "mhansen"
}
```

Neither of us can reproduce this.  I'm going to mark this as invalid.



---

archive/issue_comments_035720.json:
```json
{
    "body": "I agree.  I should have put the version and pasted output.",
    "created_at": "2009-01-22T08:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4732#issuecomment-35720",
    "user": "jason"
}
```

I agree.  I should have put the version and pasted output.
