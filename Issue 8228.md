# Issue 8228: Segfault in libsingular

archive/issues_008228.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @jaapspies\n\nThis is bad:\n\n\n```python\nsage: P.<x,y> = Zmod(10)[]; P(0)\n0\nsage: P.<x,y> = Zmod(2^10)[]; P(0)\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8228\n\n",
    "created_at": "2010-02-10T13:24:13Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Segfault in libsingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8228",
    "user": "@malb"
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

archive/issue_comments_072658.json:
```json
{
    "body": "This is an upstream bug, cf.\n\n  http://groups.google.com/group/libsingular-devel/browse_thread/thread/aa42455cb52257d\n\nI will provide an updated SPKG later.",
    "created_at": "2010-02-10T13:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72658",
    "user": "@malb"
}
```

This is an upstream bug, cf.

  http://groups.google.com/group/libsingular-devel/browse_thread/thread/aa42455cb52257d

I will provide an updated SPKG later.



---

archive/issue_comments_072659.json:
```json
{
    "body": "http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-9-20100125.p1.spkg",
    "created_at": "2010-02-10T13:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72659",
    "user": "@malb"
}
```

http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-9-20100125.p1.spkg



---

archive/issue_comments_072660.json:
```json
{
    "body": "You will need the patch from #8059 to compile the Sage library with the Singular SPKG.",
    "created_at": "2010-02-10T13:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72660",
    "user": "@malb"
}
```

You will need the patch from #8059 to compile the Sage library with the Singular SPKG.



---

archive/issue_comments_072661.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-10T13:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72661",
    "user": "@malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072662.json:
```json
{
    "body": "Bumping this ticket because it is ridiculous that this bug is around.",
    "created_at": "2010-03-03T12:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72662",
    "user": "@malb"
}
```

Bumping this ticket because it is ridiculous that this bug is around.



---

archive/issue_comments_072663.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-03-03T12:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72663",
    "user": "@malb"
}
```

Changing priority from major to critical.



---

archive/issue_comments_072664.json:
```json
{
    "body": "Ticket depends on #8059",
    "created_at": "2010-03-11T10:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72664",
    "user": "@malb"
}
```

Ticket depends on #8059



---

archive/issue_comments_072665.json:
```json
{
    "body": "Setting to needs work since it depends on #8059 (though not strictly)",
    "created_at": "2010-06-02T18:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72665",
    "user": "@malb"
}
```

Setting to needs work since it depends on #8059 (though not strictly)



---

archive/issue_comments_072666.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-02T18:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72666",
    "user": "@malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072667.json:
```json
{
    "body": "Attachment [trac_8228-doctest.patch](tarball://root/attachments/some-uuid/ticket8228/trac_8228-doctest.patch) by @burcin created at 2010-09-19 14:48:48\n\nadd doctest",
    "created_at": "2010-09-19T14:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72667",
    "user": "@burcin"
}
```

Attachment [trac_8228-doctest.patch](tarball://root/attachments/some-uuid/ticket8228/trac_8228-doctest.patch) by @burcin created at 2010-09-19 14:48:48

add doctest



---

archive/issue_comments_072668.json:
```json
{
    "body": "Since #8059 is merged with the new Singular package, this works:\n\n\n```\nsage: P.<x,y> = Zmod(10)[]; P(0)\n0\nsage: P.<x,y> = Zmod(2^10)[]; P(0)\n0\n```\n\n\nattachment:trac_8228-doctest.patch adds a doctest. Trivial review anyone?",
    "created_at": "2010-09-19T14:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72668",
    "user": "@burcin"
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

archive/issue_comments_072669.json:
```json
{
    "body": "Changing keywords from \"\" to \"singular\".",
    "created_at": "2010-09-19T14:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72669",
    "user": "@burcin"
}
```

Changing keywords from "" to "singular".



---

archive/issue_comments_072670.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-19T14:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72670",
    "user": "@burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072671.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-19T16:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72671",
    "user": "@malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072672.json:
```json
{
    "body": "Patch looks good, doctests pass.",
    "created_at": "2010-09-19T16:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72672",
    "user": "@malb"
}
```

Patch looks good, doctests pass.



---

archive/issue_comments_072673.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8228#issuecomment-72673",
    "user": "@qed777"
}
```

Resolution: fixed
