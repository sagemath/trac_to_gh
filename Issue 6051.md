# Issue 6051: [with patch, needs some work] Enable Singular's coefficient rings which are not fields

archive/issues_006051.json:
```json
{
    "body": "Assignee: @malb\n\nSingular 3-1-0 supports coefficient rings which are not fields. In particular, it supports ZZ and ZZ/nZZ now. We should support those natively too.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6051\n\n",
    "created_at": "2009-05-17T01:05:00Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, needs some work] Enable Singular's coefficient rings which are not fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6051",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Singular 3-1-0 supports coefficient rings which are not fields. In particular, it supports ZZ and ZZ/nZZ now. We should support those natively too.


Issue created by migration from https://trac.sagemath.org/ticket/6051





---

archive/issue_comments_048106.json:
```json
{
    "body": "almost works",
    "created_at": "2009-05-17T01:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48106",
    "user": "https://github.com/malb"
}
```

almost works



---

archive/issue_comments_048107.json:
```json
{
    "body": "Attachment [singular_3_1_0-rings.patch](tarball://root/attachments/some-uuid/ticket6051/singular_3_1_0-rings.patch) by @malb created at 2009-05-17 05:00:27\n\nThe attached patch enables the Singular coefficient rings natively. It passes doctests except: \n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/rings/polynomial/toy_d_basis.py # 1 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1049.8 seconds\n```\n\nwhich I reported upstream at \n\n  http://www.singular.uni-kl.de:8002/trac/ticket/137",
    "created_at": "2009-05-17T05:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48107",
    "user": "https://github.com/malb"
}
```

Attachment [singular_3_1_0-rings.patch](tarball://root/attachments/some-uuid/ticket6051/singular_3_1_0-rings.patch) by @malb created at 2009-05-17 05:00:27

The attached patch enables the Singular coefficient rings natively. It passes doctests except: 

```
The following tests failed:

        sage -t  devel/sage/sage/rings/polynomial/toy_d_basis.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1049.8 seconds
```

which I reported upstream at 

  http://www.singular.uni-kl.de:8002/trac/ticket/137



---

archive/issue_comments_048108.json:
```json
{
    "body": "I applied this against 4.0 patched by #6034, and it works great. I don't find any other doctest failures.",
    "created_at": "2009-06-02T16:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48108",
    "user": "https://github.com/kedlaya"
}
```

I applied this against 4.0 patched by #6034, and it works great. I don't find any other doctest failures.



---

archive/issue_comments_048109.json:
```json
{
    "body": "FYI I pinged upstream again about this blocker.",
    "created_at": "2009-06-03T22:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48109",
    "user": "https://github.com/malb"
}
```

FYI I pinged upstream again about this blocker.



---

archive/issue_comments_048110.json:
```json
{
    "body": "Against 4.0.1:\n\n\n```\nncalexan@sage:~/releases/sage-4.0.2.alpha0/devel/sage-main/sage$ sage -hg import ~/releases/trac_6051-singular-3_1_0-rings.patch \napplying /home/ncalexan/releases/trac_6051-singular-3_1_0-rings.patch\npatching file doc/en/reference/polynomial_rings.rst\nHunk #2 FAILED at 13\n1 out of 2 hunks FAILED -- saving rejects to file doc/en/reference/polynomial_rings.rst.rej\npatching file sage/rings/polynomial/multi_polynomial_ideal.py\nHunk #14 FAILED at 353\nHunk #52 FAILED at 2195\nHunk #53 FAILED at 2219\nHunk #54 FAILED at 2263\nHunk #55 FAILED at 2271\nHunk #57 FAILED at 2381\n6 out of 63 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\nHunk #16 succeeded at 529 with fuzz 1 (offset 0 lines).\nHunk #17 FAILED at 550\nHunk #87 succeeded at 2650 with fuzz 1 (offset 21 lines).\nHunk #90 succeeded at 2711 with fuzz 1 (offset 23 lines).\n1 out of 176 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2009-06-10T05:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48110",
    "user": "https://github.com/ncalexan"
}
```

Against 4.0.1:


```
ncalexan@sage:~/releases/sage-4.0.2.alpha0/devel/sage-main/sage$ sage -hg import ~/releases/trac_6051-singular-3_1_0-rings.patch 
applying /home/ncalexan/releases/trac_6051-singular-3_1_0-rings.patch
patching file doc/en/reference/polynomial_rings.rst
Hunk #2 FAILED at 13
1 out of 2 hunks FAILED -- saving rejects to file doc/en/reference/polynomial_rings.rst.rej
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #14 FAILED at 353
Hunk #52 FAILED at 2195
Hunk #53 FAILED at 2219
Hunk #54 FAILED at 2263
Hunk #55 FAILED at 2271
Hunk #57 FAILED at 2381
6 out of 63 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #16 succeeded at 529 with fuzz 1 (offset 0 lines).
Hunk #17 FAILED at 550
Hunk #87 succeeded at 2650 with fuzz 1 (offset 21 lines).
Hunk #90 succeeded at 2711 with fuzz 1 (offset 23 lines).
1 out of 176 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_048111.json:
```json
{
    "body": "Upstream fixed the issue in:\n\n   ftp://www.mathematik.uni-kl.de/pub/Math/Singular/src/3-1-0/Singular-3-1-0-4.tar.gz",
    "created_at": "2009-06-10T08:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48111",
    "user": "https://github.com/malb"
}
```

Upstream fixed the issue in:

   ftp://www.mathematik.uni-kl.de/pub/Math/Singular/src/3-1-0/Singular-3-1-0-4.tar.gz



---

archive/issue_comments_048112.json:
```json
{
    "body": "Replying to [comment:5 malb]:\n> Upstream fixed the issue in:\n> \n>    ftp://www.mathematik.uni-kl.de/pub/Math/Singular/src/3-1-0/Singular-3-1-0-4.tar.gz\n\nI'm release manager for this.  I should update your spkg with this new tree?  Will you do that for me?",
    "created_at": "2009-06-10T21:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48112",
    "user": "https://github.com/ncalexan"
}
```

Replying to [comment:5 malb]:
> Upstream fixed the issue in:
> 
>    ftp://www.mathematik.uni-kl.de/pub/Math/Singular/src/3-1-0/Singular-3-1-0-4.tar.gz

I'm release manager for this.  I should update your spkg with this new tree?  Will you do that for me?



---

archive/issue_comments_048113.json:
```json
{
    "body": "> I'm release manager for this.  I should update your spkg with this new tree?  Will you do that for me?\n\nNick, you don't have to update the SPKG just because you are release manager. In any case, I'll see if I can update it soon-ish.",
    "created_at": "2009-06-10T22:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48113",
    "user": "https://github.com/malb"
}
```

> I'm release manager for this.  I should update your spkg with this new tree?  Will you do that for me?

Nick, you don't have to update the SPKG just because you are release manager. In any case, I'll see if I can update it soon-ish.



---

archive/issue_comments_048114.json:
```json
{
    "body": "Attachment [trac_6051-rings-against-4.0.1.patch](tarball://root/attachments/some-uuid/ticket6051/trac_6051-rings-against-4.0.1.patch) by @ncalexan created at 2009-06-11 04:51:40\n\nI rebased the patch against 4.0.1 (really what will be 4.0.2.alpha0) and it works up to that one failing doctest.  I'd really like to merge this and #6034 for 4.0.2 so if the spkg itself isn't updated to the even newer singular, let's remove the failing doctest.",
    "created_at": "2009-06-11T04:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48114",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6051-rings-against-4.0.1.patch](tarball://root/attachments/some-uuid/ticket6051/trac_6051-rings-against-4.0.1.patch) by @ncalexan created at 2009-06-11 04:51:40

I rebased the patch against 4.0.1 (really what will be 4.0.2.alpha0) and it works up to that one failing doctest.  I'd really like to merge this and #6034 for 4.0.2 so if the spkg itself isn't updated to the even newer singular, let's remove the failing doctest.



---

archive/issue_comments_048115.json:
```json
{
    "body": "There are some issue with the new upstream release (computations timing out), which I haven't tracked down yet. I am a bit short on time so I'd suggest not to include this patch in 4.0.2 or to follow the strategy Nick proposed above: just remove the doctest failure.",
    "created_at": "2009-06-11T13:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48115",
    "user": "https://github.com/malb"
}
```

There are some issue with the new upstream release (computations timing out), which I haven't tracked down yet. I am a bit short on time so I'd suggest not to include this patch in 4.0.2 or to follow the strategy Nick proposed above: just remove the doctest failure.



---

archive/issue_comments_048116.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T08:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48116",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_048117.json:
```json
{
    "body": "Docstring #random-ed, follow up ticket at #6265.",
    "created_at": "2009-06-12T08:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48117",
    "user": "https://github.com/ncalexan"
}
```

Docstring #random-ed, follow up ticket at #6265.



---

archive/issue_events_006306.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-12T08:02:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6051#event-6306"
}
```



---

archive/issue_comments_048118.json:
```json
{
    "body": "Is this really merged in 4.0.2.alpha1? Do you mean 4.0.2.alpha0?",
    "created_at": "2009-06-12T14:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48118",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Is this really merged in 4.0.2.alpha1? Do you mean 4.0.2.alpha0?



---

archive/issue_comments_048119.json:
```json
{
    "body": "This is confusing, and the first part (multivariate rings) behave differently on 32 and 64 bit machines.  Any thoughts, Martin?\n\n\n```\nsage: P.<x,y,z> = Integers(2^32)[]\nsage: P(2^32-1)\n-1\nsage: P.<x> = Integers(2^32)[]\nsage: P(2^32-1)\n4294967295\n```\n",
    "created_at": "2009-06-14T21:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48119",
    "user": "https://github.com/ncalexan"
}
```

This is confusing, and the first part (multivariate rings) behave differently on 32 and 64 bit machines.  Any thoughts, Martin?


```
sage: P.<x,y,z> = Integers(2^32)[]
sage: P(2^32-1)
-1
sage: P.<x> = Integers(2^32)[]
sage: P(2^32-1)
4294967295
```




---

archive/issue_comments_048120.json:
```json
{
    "body": "This looks like an upstream bug to me. I reported it at\n\n\n  http://www.singular.uni-kl.de:8002/trac/ticket/138\n\nI will provide a workaround and attach it to this ticket.",
    "created_at": "2009-06-15T10:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48120",
    "user": "https://github.com/malb"
}
```

This looks like an upstream bug to me. I reported it at


  http://www.singular.uni-kl.de:8002/trac/ticket/138

I will provide a workaround and attach it to this ticket.



---

archive/issue_comments_048121.json:
```json
{
    "body": "Attachment [singular_exp_overflow.patch](tarball://root/attachments/some-uuid/ticket6051/singular_exp_overflow.patch) by @malb created at 2009-06-15 10:49:30\n\nThe attached patch fixes the issue on sage.math for me.",
    "created_at": "2009-06-15T10:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6051#issuecomment-48121",
    "user": "https://github.com/malb"
}
```

Attachment [singular_exp_overflow.patch](tarball://root/attachments/some-uuid/ticket6051/singular_exp_overflow.patch) by @malb created at 2009-06-15 10:49:30

The attached patch fixes the issue on sage.math for me.
