# Issue 8007: Speed up generation of random number field elements

archive/issues_008007.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @williamstein boothby spancratz\n\nIn the process of looking at #3436, I noticed that generation of random number field elements was slow. I was hoping that speeding it up would make it fast enough that we could use a \"generic\" algorithm for generating matrices over cyclotomic fields. I did get a **100-150X** speedup for generating random elements of number fields, but amazingly, this **still** wasn't quite fast enough to beat the more \"quick and dirty\" approaches for cyclotomic matrices. However, I think this code is probably still worth merging.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8007\n\n",
    "created_at": "2010-01-20T04:50:23Z",
    "labels": [
        "component: number fields",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Speed up generation of random number field elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8007",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @loefflerd

CC:  @williamstein boothby spancratz

In the process of looking at #3436, I noticed that generation of random number field elements was slow. I was hoping that speeding it up would make it fast enough that we could use a "generic" algorithm for generating matrices over cyclotomic fields. I did get a **100-150X** speedup for generating random elements of number fields, but amazingly, this **still** wasn't quite fast enough to beat the more "quick and dirty" approaches for cyclotomic matrices. However, I think this code is probably still worth merging.

Issue created by migration from https://trac.sagemath.org/ticket/8007





---

archive/issue_comments_069845.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T04:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69845",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069846.json:
```json
{
    "body": "I should comment that it's actually not too hard to understand why this still isn't fast enough to beat the code on #3436. A large part of the problem is that we still represent elements of number fields by NTL polynomials -- the lion's share of the difference comes down to the fact that we end up doing several copies of data back and forth between NTL `ZZX` objects and GMP/MPIR `mpz_t` and `mpq_t` objects, which adds up fast.",
    "created_at": "2010-01-20T04:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69846",
    "user": "https://github.com/craigcitro"
}
```

I should comment that it's actually not too hard to understand why this still isn't fast enough to beat the code on #3436. A large part of the problem is that we still represent elements of number fields by NTL polynomials -- the lion's share of the difference comes down to the fact that we end up doing several copies of data back and forth between NTL `ZZX` objects and GMP/MPIR `mpz_t` and `mpq_t` objects, which adds up fast.



---

archive/issue_comments_069847.json:
```json
{
    "body": "Looks good, just needs some fixes due to random number generation changes:\n\n```\n\tsage -t  devel/sage-main/sage/rings/number_field/number_field.py # 1 doctests failed\n\tsage -t  devel/sage-main/sage/algebras/quatalg/quaternion_algebra.py # 4 doctests failed\n```",
    "created_at": "2010-01-20T09:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69847",
    "user": "https://github.com/robertwb"
}
```

Looks good, just needs some fixes due to random number generation changes:

```
	sage -t  devel/sage-main/sage/rings/number_field/number_field.py # 1 doctests failed
	sage -t  devel/sage-main/sage/algebras/quatalg/quaternion_algebra.py # 4 doctests failed
```



---

archive/issue_comments_069848.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T09:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69848",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069849.json:
```json
{
    "body": "Cool, fixed. New patch attached. \n\n(Amusingly, the `number_field.py` failure was a change I made on purpose: I was putting it there for myself as a reminder to doctest everything, because I was habitually only doctesting that directory ... oops.)",
    "created_at": "2010-01-20T19:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69849",
    "user": "https://github.com/craigcitro"
}
```

Cool, fixed. New patch attached. 

(Amusingly, the `number_field.py` failure was a change I made on purpose: I was putting it there for myself as a reminder to doctest everything, because I was habitually only doctesting that directory ... oops.)



---

archive/issue_comments_069850.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T19:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69850",
    "user": "https://github.com/craigcitro"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069851.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-11T20:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69851",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069852.json:
```json
{
    "body": "Attachment [trac_8007.patch](tarball://root/attachments/some-uuid/ticket8007/trac_8007.patch) by @roed314 created at 2010-02-11 20:45:13\n\nNeeds to be rebased against 4.3.2...",
    "created_at": "2010-02-11T20:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69852",
    "user": "https://github.com/roed314"
}
```

Attachment [trac_8007.patch](tarball://root/attachments/some-uuid/ticket8007/trac_8007.patch) by @roed314 created at 2010-02-11 20:45:13

Needs to be rebased against 4.3.2...



---

archive/issue_comments_069853.json:
```json
{
    "body": "Attachment [trac_8007_rebase.patch](tarball://root/attachments/some-uuid/ticket8007/trac_8007_rebase.patch) by @craigcitro created at 2010-02-12 20:15:21",
    "created_at": "2010-02-12T20:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69853",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_8007_rebase.patch](tarball://root/attachments/some-uuid/ticket8007/trac_8007_rebase.patch) by @craigcitro created at 2010-02-12 20:15:21



---

archive/issue_comments_069854.json:
```json
{
    "body": "Done.",
    "created_at": "2010-02-12T20:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69854",
    "user": "https://github.com/craigcitro"
}
```

Done.



---

archive/issue_comments_069855.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-12T20:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69855",
    "user": "https://github.com/craigcitro"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069856.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-15T19:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69856",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069857.json:
```json
{
    "body": "All tests pass, code looks good.",
    "created_at": "2010-02-15T19:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69857",
    "user": "https://github.com/roed314"
}
```

All tests pass, code looks good.



---

archive/issue_comments_069858.json:
```json
{
    "body": "Merged [trac_8007_rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8007/trac_8007_rebase.patch).",
    "created_at": "2010-02-17T20:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8007_rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8007/trac_8007_rebase.patch).



---

archive/issue_events_019186.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-17T20:43:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8007#event-19186"
}
```



---

archive/issue_comments_069859.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T20:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69859",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
