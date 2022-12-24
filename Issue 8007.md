# Issue 8007: Speed up generation of random number field elements

archive/issues_008007.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  was boothby spancratz\n\nIn the process of looking at #3436, I noticed that generation of random number field elements was slow. I was hoping that speeding it up would make it fast enough that we could use a \"generic\" algorithm for generating matrices over cyclotomic fields. I did get a **100-150X** speedup for generating random elements of number fields, but amazingly, this **still** wasn't quite fast enough to beat the more \"quick and dirty\" approaches for cyclotomic matrices. However, I think this code is probably still worth merging.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8007\n\n",
    "created_at": "2010-01-20T04:50:23Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "Speed up generation of random number field elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8007",
    "user": "craigcitro"
}
```
Assignee: davidloeffler

CC:  was boothby spancratz

In the process of looking at #3436, I noticed that generation of random number field elements was slow. I was hoping that speeding it up would make it fast enough that we could use a "generic" algorithm for generating matrices over cyclotomic fields. I did get a **100-150X** speedup for generating random elements of number fields, but amazingly, this **still** wasn't quite fast enough to beat the more "quick and dirty" approaches for cyclotomic matrices. However, I think this code is probably still worth merging.

Issue created by migration from https://trac.sagemath.org/ticket/8007





---

archive/issue_comments_069965.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T04:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69965",
    "user": "craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069966.json:
```json
{
    "body": "I should comment that it's actually not too hard to understand why this still isn't fast enough to beat the code on #3436. A large part of the problem is that we still represent elements of number fields by NTL polynomials -- the lion's share of the difference comes down to the fact that we end up doing several copies of data back and forth between NTL `ZZX` objects and GMP/MPIR `mpz_t` and `mpq_t` objects, which adds up fast.",
    "created_at": "2010-01-20T04:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69966",
    "user": "craigcitro"
}
```

I should comment that it's actually not too hard to understand why this still isn't fast enough to beat the code on #3436. A large part of the problem is that we still represent elements of number fields by NTL polynomials -- the lion's share of the difference comes down to the fact that we end up doing several copies of data back and forth between NTL `ZZX` objects and GMP/MPIR `mpz_t` and `mpq_t` objects, which adds up fast.



---

archive/issue_comments_069967.json:
```json
{
    "body": "Looks good, just needs some fixes due to random number generation changes:\n\n\n```\n\tsage -t  devel/sage-main/sage/rings/number_field/number_field.py # 1 doctests failed\n\tsage -t  devel/sage-main/sage/algebras/quatalg/quaternion_algebra.py # 4 doctests failed\n```\n",
    "created_at": "2010-01-20T09:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69967",
    "user": "robertwb"
}
```

Looks good, just needs some fixes due to random number generation changes:


```
	sage -t  devel/sage-main/sage/rings/number_field/number_field.py # 1 doctests failed
	sage -t  devel/sage-main/sage/algebras/quatalg/quaternion_algebra.py # 4 doctests failed
```




---

archive/issue_comments_069968.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-20T09:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69968",
    "user": "robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069969.json:
```json
{
    "body": "Cool, fixed. New patch attached. \n\n(Amusingly, the `number_field.py` failure was a change I made on purpose: I was putting it there for myself as a reminder to doctest everything, because I was habitually only doctesting that directory ... oops.)",
    "created_at": "2010-01-20T19:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69969",
    "user": "craigcitro"
}
```

Cool, fixed. New patch attached. 

(Amusingly, the `number_field.py` failure was a change I made on purpose: I was putting it there for myself as a reminder to doctest everything, because I was habitually only doctesting that directory ... oops.)



---

archive/issue_comments_069970.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T19:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69970",
    "user": "craigcitro"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069971.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-11T20:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69971",
    "user": "roed"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069972.json:
```json
{
    "body": "Attachment [trac_8007.patch](tarball://root/attachments/some-uuid/ticket8007/trac_8007.patch) by roed created at 2010-02-11 20:45:13\n\nNeeds to be rebased against 4.3.2...",
    "created_at": "2010-02-11T20:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69972",
    "user": "roed"
}
```

Attachment [trac_8007.patch](tarball://root/attachments/some-uuid/ticket8007/trac_8007.patch) by roed created at 2010-02-11 20:45:13

Needs to be rebased against 4.3.2...



---

archive/issue_comments_069973.json:
```json
{
    "body": "Attachment [trac_8007_rebase.patch](tarball://root/attachments/some-uuid/ticket8007/trac_8007_rebase.patch) by craigcitro created at 2010-02-12 20:15:21",
    "created_at": "2010-02-12T20:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69973",
    "user": "craigcitro"
}
```

Attachment [trac_8007_rebase.patch](tarball://root/attachments/some-uuid/ticket8007/trac_8007_rebase.patch) by craigcitro created at 2010-02-12 20:15:21



---

archive/issue_comments_069974.json:
```json
{
    "body": "Done.",
    "created_at": "2010-02-12T20:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69974",
    "user": "craigcitro"
}
```

Done.



---

archive/issue_comments_069975.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-12T20:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69975",
    "user": "craigcitro"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069976.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-15T19:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69976",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069977.json:
```json
{
    "body": "All tests pass, code looks good.",
    "created_at": "2010-02-15T19:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69977",
    "user": "roed"
}
```

All tests pass, code looks good.



---

archive/issue_comments_069978.json:
```json
{
    "body": "Merged [trac_8007_rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8007/trac_8007_rebase.patch).",
    "created_at": "2010-02-17T20:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69978",
    "user": "mvngu"
}
```

Merged [trac_8007_rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8007/trac_8007_rebase.patch).



---

archive/issue_comments_069979.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T20:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8007",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8007#issuecomment-69979",
    "user": "mvngu"
}
```

Resolution: fixed
