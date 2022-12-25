# Issue 9952: int(symbolic expr) off by 1

archive/issues_009952.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @fredrik-johansson @kcrisman @zafeirakopoulos @orlitzky\n\nProblem, last digit is either 6 or 7. In short:\n\n\n```\nfermat(n) = 2**2**n + 1\nfermat(9) gives ....4097 but:\nint(fermat(9)) gives ...4096L.\nSame with: long(fermat(9)).\nint(2**2**9 +1) gives ...4097L\n```\n\n\nBurcin says: int(x) for a symbolic expression x just calls int(x.n(prec=100)). We lose that 1 in the approximation.\n\nfull example in 4.5.2:\n\n\n```\nsage: fermat(n) = 2**2**n + 1\nsage: fermat(9)\n134078079299425970995740249982058461274793658205923933777\\\n235614437217640300735469768018742981669034276900318581864\\\n86050853753882811946569946433649006084097\nsage: int(fermat(9))\n134078079299425970995740249982058461274793658205923933777\\\n235614437217640300735469768018742981669034276900318581864\\\n86050853753882811946569946433649006084096L\nsage: long(fermat(9))\n134078079299425970995740249982058461274793658205923933777\\\n235614437217640300735469768018742981669034276900318581864\\\n86050853753882811946569946433649006084096L\nsage: int(2**2**9 +1)\n134078079299425970995740249982058461274793658205923933777\\\n235614437217640300735469768018742981669034276900318581864\\\n86050853753882811946569946433649006084097L\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9953\n\n",
    "created_at": "2010-09-20T10:16:21Z",
    "labels": [
        "component: symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "int(symbolic expr) off by 1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9952",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: @burcin

CC:  @fredrik-johansson @kcrisman @zafeirakopoulos @orlitzky

Problem, last digit is either 6 or 7. In short:


```
fermat(n) = 2**2**n + 1
fermat(9) gives ....4097 but:
int(fermat(9)) gives ...4096L.
Same with: long(fermat(9)).
int(2**2**9 +1) gives ...4097L
```


Burcin says: int(x) for a symbolic expression x just calls int(x.n(prec=100)). We lose that 1 in the approximation.

full example in 4.5.2:


```
sage: fermat(n) = 2**2**n + 1
sage: fermat(9)
134078079299425970995740249982058461274793658205923933777\
235614437217640300735469768018742981669034276900318581864\
86050853753882811946569946433649006084097
sage: int(fermat(9))
134078079299425970995740249982058461274793658205923933777\
235614437217640300735469768018742981669034276900318581864\
86050853753882811946569946433649006084096L
sage: long(fermat(9))
134078079299425970995740249982058461274793658205923933777\
235614437217640300735469768018742981669034276900318581864\
86050853753882811946569946433649006084096L
sage: int(2**2**9 +1)
134078079299425970995740249982058461274793658205923933777\
235614437217640300735469768018742981669034276900318581864\
86050853753882811946569946433649006084097L
```



Issue created by migration from https://trac.sagemath.org/ticket/9953





---

archive/issue_comments_099105.json:
```json
{
    "body": "Attachment [9953.patch](tarball://root/attachments/some-uuid/ticket9953/9953.patch) by @roed314 created at 2010-10-25 21:27:01",
    "created_at": "2010-10-25T21:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9952#issuecomment-99105",
    "user": "https://github.com/roed314"
}
```

Attachment [9953.patch](tarball://root/attachments/some-uuid/ticket9953/9953.patch) by @roed314 created at 2010-10-25 21:27:01



---

archive/issue_comments_099106.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-10-25T21:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9952#issuecomment-99106",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_099107.json:
```json
{
    "body": "I don't want to work on this much, but I believe that this patch should fix the problem.  If someone wants to add some doctests and polish it a bit, go for it.",
    "created_at": "2010-10-25T21:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9952#issuecomment-99107",
    "user": "https://github.com/roed314"
}
```

I don't want to work on this much, but I believe that this patch should fix the problem.  If someone wants to add some doctests and polish it a bit, go for it.



---

archive/issue_comments_099108.json:
```json
{
    "body": "The current patch won't work for 0 or negative numbers (the log2 breaks).  This can be easily fixed, but dealing with cases like \n\n\n```\nsage: f = 1-1/10**100\nsage: int(f)\n0\nsage: int(SR(f))\n1\n```\n\n\nwhere the precision needed to get the right result isn't a function of the size is a little trickier.  Maybe fast-path the common cases and then fall back on the existing floor/ceil logic?",
    "created_at": "2011-02-18T19:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9952#issuecomment-99108",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

The current patch won't work for 0 or negative numbers (the log2 breaks).  This can be easily fixed, but dealing with cases like 


```
sage: f = 1-1/10**100
sage: int(f)
0
sage: int(SR(f))
1
```


where the precision needed to get the right result isn't a function of the size is a little trickier.  Maybe fast-path the common cases and then fall back on the existing floor/ceil logic?



---

archive/issue_comments_099109.json:
```json
{
    "body": "This appears to be a duplicate of #9627.",
    "created_at": "2011-02-19T09:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9952#issuecomment-99109",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

This appears to be a duplicate of #9627.



---

archive/issue_comments_099110.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-22T22:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9952#issuecomment-99110",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_099111.json:
```json
{
    "body": "#12968 has a patch with a positive review which fixes this. We should close this as a duplicate.",
    "created_at": "2012-05-22T22:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9952#issuecomment-99111",
    "user": "https://github.com/burcin"
}
```

#12968 has a patch with a positive review which fixes this. We should close this as a duplicate.



---

archive/issue_events_010081.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-19T13:25:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9952#event-10081"
}
```



---

archive/issue_comments_099112.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-06-19T13:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9952",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9952#issuecomment-99112",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
