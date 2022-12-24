# Issue 2956: generic multivariate polynomials are buggy on exponent overflow

archive/issues_002956.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  mjo\n\nLong exponents are silently truncated to word-size exponents:\n\n```\nsage: K.<x,y> = AA[]\nsage: x^(2^64 + 12345)\nx^12345\n```\n\n\nIn one test, I also saw a crash, but I can't reproduce it.\n\n```\nsage: K.<x,y> = ZZ[]\nsage: (x^12345)^54321\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\n...\n```\n\n(The crash was on 32-bit x86 Debian testing.  The first test fails with the same answer on both 32-bit and 64-bit x86.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2956\n\n",
    "created_at": "2008-04-19T15:26:41Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "generic multivariate polynomials are buggy on exponent overflow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2956",
    "user": "cwitty"
}
```
Assignee: somebody

CC:  mjo

Long exponents are silently truncated to word-size exponents:

```
sage: K.<x,y> = AA[]
sage: x^(2^64 + 12345)
x^12345
```


In one test, I also saw a crash, but I can't reproduce it.

```
sage: K.<x,y> = ZZ[]
sage: (x^12345)^54321


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
...
```

(The crash was on 32-bit x86 Debian testing.  The first test fails with the same answer on both 32-bit and 64-bit x86.)

Issue created by migration from https://trac.sagemath.org/ticket/2956





---

archive/issue_comments_020381.json:
```json
{
    "body": "For the 2nd example, I do not get a crash, but a funny result with 3.1.4 on a 32-bit computer:\n\n```\nsage: K.<x,y> = ZZ[]\nsage: (x^12345)^54321\nx^28393*y^10232\n```\n\nNote that y does not appear in the input!\n\nPossible explanation: 12345*54321 = 10232*2^16+28393.\nApparently the low 16 bits are used to store the exponent of x, and the upper 16 bits\nfor the exponent of y, but no check for overflow is done!!!",
    "created_at": "2008-10-19T13:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20381",
    "user": "zimmerma"
}
```

For the 2nd example, I do not get a crash, but a funny result with 3.1.4 on a 32-bit computer:

```
sage: K.<x,y> = ZZ[]
sage: (x^12345)^54321
x^28393*y^10232
```

Note that y does not appear in the input!

Possible explanation: 12345*54321 = 10232*2^16+28393.
Apparently the low 16 bits are used to store the exponent of x, and the upper 16 bits
for the exponent of y, but no check for overflow is done!!!



---

archive/issue_comments_020382.json:
```json
{
    "body": "Replying to [comment:2 zimmerma]:\n\nI realize this was already noticed by Carl in #2957.",
    "created_at": "2008-10-19T13:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20382",
    "user": "zimmerma"
}
```

Replying to [comment:2 zimmerma]:

I realize this was already noticed by Carl in #2957.



---

archive/issue_comments_020383.json:
```json
{
    "body": "Changing assignee from somebody to malb.",
    "created_at": "2009-01-25T19:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20383",
    "user": "malb"
}
```

Changing assignee from somebody to malb.



---

archive/issue_comments_020384.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T19:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20384",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020385.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-07T23:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20385",
    "user": "mjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_020386.json:
```json
{
    "body": "I think these are both fixed, so I've added doctests. I have only tested on x64: I think the first example should overflow on both, the second should work on both. But a reviewer should give it a try on x32.",
    "created_at": "2012-01-07T23:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20386",
    "user": "mjo"
}
```

I think these are both fixed, so I've added doctests. I have only tested on x64: I think the first example should overflow on both, the second should work on both. But a reviewer should give it a try on x32.



---

archive/issue_comments_020387.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-08T10:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20387",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_020388.json:
```json
{
    "body": "I tried on a 32-bit machine with vanilla 4.7.2. The first doctest is ok, for the second one I get:\n\n```\nsage: (x^12345)^54321\n...\nOverflowError: Exponent overflow (670592745).\n```\n\nthus the patch needs work.\n\nPaul Zimmermann",
    "created_at": "2012-01-08T10:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20388",
    "user": "zimmerma"
}
```

I tried on a 32-bit machine with vanilla 4.7.2. The first doctest is ok, for the second one I get:

```
sage: (x^12345)^54321
...
OverflowError: Exponent overflow (670592745).
```

thus the patch needs work.

Paul Zimmermann



---

archive/issue_comments_020389.json:
```json
{
    "body": "Hmm, I wonder how big we can make the exponent. I was guessing `(2^31 - 1)`, but `670592745` is way smaller than that.\n\nSince the crash was on a 32-bit machine, we can assume (i.e. hope) that it was due to the overflow. With that in mind, maybe we should just ignore the output with \"...\" and consider the test a success if it doesn't crash?",
    "created_at": "2012-01-08T17:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20389",
    "user": "mjo"
}
```

Hmm, I wonder how big we can make the exponent. I was guessing `(2^31 - 1)`, but `670592745` is way smaller than that.

Since the crash was on a 32-bit machine, we can assume (i.e. hope) that it was due to the overflow. With that in mind, maybe we should just ignore the output with "..." and consider the test a success if it doesn't crash?



---

archive/issue_comments_020390.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-09T00:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20390",
    "user": "mjo"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_020391.json:
```json
{
    "body": "Attachment [sage-trac_2956.patch](tarball://root/attachments/some-uuid/ticket2956/sage-trac_2956.patch) by mjo created at 2012-01-09 01:54:18\n\nUpdated patch, should also work on x32.",
    "created_at": "2012-01-09T01:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20391",
    "user": "mjo"
}
```

Attachment [sage-trac_2956.patch](tarball://root/attachments/some-uuid/ticket2956/sage-trac_2956.patch) by mjo created at 2012-01-09 01:54:18

Updated patch, should also work on x32.



---

archive/issue_comments_020392.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd35.5\".",
    "created_at": "2012-01-09T08:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20392",
    "user": "zimmerma"
}
```

Changing keywords from "" to "sd35.5".



---

archive/issue_comments_020393.json:
```json
{
    "body": "note: for `K.<x,y> = AA[]` the maximum exponent seems to be 2147483647 both on 32- and 64-bit,\nwhile for `K.<x,y> = ZZ[]` on 32-bit the maximum is 32768, and on 64-bit it is 1073741824.\n\nPaul",
    "created_at": "2012-01-09T08:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20393",
    "user": "zimmerma"
}
```

note: for `K.<x,y> = AA[]` the maximum exponent seems to be 2147483647 both on 32- and 64-bit,
while for `K.<x,y> = ZZ[]` on 32-bit the maximum is 32768, and on 64-bit it is 1073741824.

Paul



---

archive/issue_comments_020394.json:
```json
{
    "body": "both doctests now pass on x32. I'm running the doctests on x32.\n\nPaul",
    "created_at": "2012-01-09T08:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20394",
    "user": "zimmerma"
}
```

both doctests now pass on x32. I'm running the doctests on x32.

Paul



---

archive/issue_comments_020395.json:
```json
{
    "body": "my installation of Sage on x32 was corrupted, I will try again with sage.4.8.alpha6.\n\nPaul",
    "created_at": "2012-01-10T08:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20395",
    "user": "zimmerma"
}
```

my installation of Sage on x32 was corrupted, I will try again with sage.4.8.alpha6.

Paul



---

archive/issue_comments_020396.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-11T07:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20396",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_020397.json:
```json
{
    "body": "I confirm all doctests pass on x32 (I got one failure in `rings/real_mpfi.pyx` but this was due\nto the spkg from #12171 I had installed). Thus positive review.\n\nPaul",
    "created_at": "2012-01-11T07:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20397",
    "user": "zimmerma"
}
```

I confirm all doctests pass on x32 (I got one failure in `rings/real_mpfi.pyx` but this was due
to the spkg from #12171 I had installed). Thus positive review.

Paul



---

archive/issue_comments_020398.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-18T08:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2956#issuecomment-20398",
    "user": "jdemeyer"
}
```

Resolution: fixed
