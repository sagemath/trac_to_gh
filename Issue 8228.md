# Issue 8228: Segfault in libsingular

archive/issues_008228.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @jaapspies\n\nThis is bad:\n\n\n```python\nsage: P.<x,y> = Zmod(10)[]; P(0)\n0\nsage: P.<x,y> = Zmod(2^10)[]; P(0)\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8228\n\n",
    "created_at": "2010-02-10T13:24:13Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Segfault in libsingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8228",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @jaapspies

This is bad:


```python
sage: P.<x,y> = Zmod(10)[]; P(0)
0
sage: P.<x,y> = Zmod(2^10)[]; P(0)

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/8228





---

archive/issue_comments_072536.json:
```json
{
    "body": "This is an upstream bug, cf.\n\n  http://groups.google.com/group/libsingular-devel/browse_thread/thread/aa42455cb52257d\n\nI will provide an updated SPKG later.",
    "created_at": "2010-02-10T13:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72536",
    "user": "https://github.com/malb"
}
```

This is an upstream bug, cf.

  http://groups.google.com/group/libsingular-devel/browse_thread/thread/aa42455cb52257d

I will provide an updated SPKG later.



---

archive/issue_comments_072537.json:
```json
{
    "body": "http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-9-20100125.p1.spkg",
    "created_at": "2010-02-10T13:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72537",
    "user": "https://github.com/malb"
}
```

http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-9-20100125.p1.spkg



---

archive/issue_comments_072538.json:
```json
{
    "body": "You will need the patch from #8059 to compile the Sage library with the Singular SPKG.",
    "created_at": "2010-02-10T13:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72538",
    "user": "https://github.com/malb"
}
```

You will need the patch from #8059 to compile the Sage library with the Singular SPKG.



---

archive/issue_comments_072539.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-10T13:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72539",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072540.json:
```json
{
    "body": "Bumping this ticket because it is ridiculous that this bug is around.",
    "created_at": "2010-03-03T12:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72540",
    "user": "https://github.com/malb"
}
```

Bumping this ticket because it is ridiculous that this bug is around.



---

archive/issue_comments_072541.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-03-03T12:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72541",
    "user": "https://github.com/malb"
}
```

Changing priority from major to critical.



---

archive/issue_comments_072542.json:
```json
{
    "body": "Ticket depends on #8059",
    "created_at": "2010-03-11T10:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72542",
    "user": "https://github.com/malb"
}
```

Ticket depends on #8059



---

archive/issue_comments_072543.json:
```json
{
    "body": "Setting to needs work since it depends on #8059 (though not strictly)",
    "created_at": "2010-06-02T18:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72543",
    "user": "https://github.com/malb"
}
```

Setting to needs work since it depends on #8059 (though not strictly)



---

archive/issue_comments_072544.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-02T18:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72544",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072545.json:
```json
{
    "body": "Attachment [trac_8228-doctest.patch](tarball://root/attachments/some-uuid/ticket8228/trac_8228-doctest.patch) by @burcin created at 2010-09-19 14:48:48\n\nadd doctest",
    "created_at": "2010-09-19T14:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72545",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_8228-doctest.patch](tarball://root/attachments/some-uuid/ticket8228/trac_8228-doctest.patch) by @burcin created at 2010-09-19 14:48:48

add doctest



---

archive/issue_comments_072546.json:
```json
{
    "body": "Since #8059 is merged with the new Singular package, this works:\n\n\n```\nsage: P.<x,y> = Zmod(10)[]; P(0)\n0\nsage: P.<x,y> = Zmod(2^10)[]; P(0)\n0\n```\n\n\nattachment:trac_8228-doctest.patch adds a doctest. Trivial review anyone?",
    "created_at": "2010-09-19T14:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72546",
    "user": "https://github.com/burcin"
}
```

Since #8059 is merged with the new Singular package, this works:


```
sage: P.<x,y> = Zmod(10)[]; P(0)
0
sage: P.<x,y> = Zmod(2^10)[]; P(0)
0
```


attachment:trac_8228-doctest.patch adds a doctest. Trivial review anyone?



---

archive/issue_comments_072547.json:
```json
{
    "body": "Changing keywords from \"\" to \"singular\".",
    "created_at": "2010-09-19T14:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72547",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "singular".



---

archive/issue_comments_072548.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-19T14:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72548",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072549.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-19T16:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72549",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072550.json:
```json
{
    "body": "Patch looks good, doctests pass.",
    "created_at": "2010-09-19T16:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72550",
    "user": "https://github.com/malb"
}
```

Patch looks good, doctests pass.



---

archive/issue_events_008429.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-29T04:24:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8228#event-8429"
}
```



---

archive/issue_comments_072551.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72551",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
