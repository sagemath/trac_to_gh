# Issue 3134: binomial doesn't take big integers

archive/issues_003134.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nI'm running sage-3.0.1 on linux/amd64 (using the precompiled binary) and binomial throws an exception if its second argument is greater than 2^63.\n\n\n```\nsage: binomial(2^100, 2^100)\n---------------------------------------------------------------------------\n<type 'exceptions.OverflowError'>         Traceback (most recent call last)\n\n/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/<ipython console> in <module>()\n\n/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/arith.py in binomial(x, m)\n   2009             raise TypeError, 'Either m or x-m must be an integer'\n   2010     if isinstance(x, (int, long, integer.Integer)):\n-> 2011         return integer_ring.ZZ(pari(x).binomial(m))\n   2012     try:\n   2013         P = x.parent()\n\n/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/gen.pyx in sage.libs.pari.gen.gen.binomial (sage/libs/pari/gen.c:13841)()\n\n<type 'exceptions.OverflowError'>: long int too large to convert to int\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3134\n\n",
    "created_at": "2008-05-08T17:05:33Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "binomial doesn't take big integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3134",
    "user": "https://trac.sagemath.org/admin/accounts/users/gebner"
}
```
Assignee: @mwhansen

CC:  sage-combinat

I'm running sage-3.0.1 on linux/amd64 (using the precompiled binary) and binomial throws an exception if its second argument is greater than 2^63.


```
sage: binomial(2^100, 2^100)
---------------------------------------------------------------------------
<type 'exceptions.OverflowError'>         Traceback (most recent call last)

/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/<ipython console> in <module>()

/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/arith.py in binomial(x, m)
   2009             raise TypeError, 'Either m or x-m must be an integer'
   2010     if isinstance(x, (int, long, integer.Integer)):
-> 2011         return integer_ring.ZZ(pari(x).binomial(m))
   2012     try:
   2013         P = x.parent()

/home/gebner/build/sage-3.0.1-debian64-intel-sse2-x86_64-Linux/gen.pyx in sage.libs.pari.gen.gen.binomial (sage/libs/pari/gen.c:13841)()

<type 'exceptions.OverflowError'>: long int too large to convert to int
```


Issue created by migration from https://trac.sagemath.org/ticket/3134





---

archive/issue_comments_021724.json:
```json
{
    "body": "Attachment [trac_3134.patch](tarball://root/attachments/some-uuid/ticket3134/trac_3134.patch) by @mwhansen created at 2008-12-02 09:44:00",
    "created_at": "2008-12-02T09:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3134#issuecomment-21724",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3134.patch](tarball://root/attachments/some-uuid/ticket3134/trac_3134.patch) by @mwhansen created at 2008-12-02 09:44:00



---

archive/issue_comments_021725.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-02T09:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3134#issuecomment-21725",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021726.json:
```json
{
    "body": "Attachment [trac_3134-2.patch](tarball://root/attachments/some-uuid/ticket3134/trac_3134-2.patch) by @mwhansen created at 2008-12-02 09:45:30\n\nI've attached two patches each of which fixes the problem.  I couldn't decide which one is better so I've left it up to the reviewer.  In my tests, PARI seemed to be a bit faster than the GMP routine.",
    "created_at": "2008-12-02T09:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3134#issuecomment-21726",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3134-2.patch](tarball://root/attachments/some-uuid/ticket3134/trac_3134-2.patch) by @mwhansen created at 2008-12-02 09:45:30

I've attached two patches each of which fixes the problem.  I couldn't decide which one is better so I've left it up to the reviewer.  In my tests, PARI seemed to be a bit faster than the GMP routine.



---

archive/issue_comments_021727.json:
```json
{
    "body": "rlm, \n\nI know you are busy, but can you give this a review? :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T15:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3134#issuecomment-21727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

rlm, 

I know you are busy, but can you give this a review? :)

Cheers,

Michael



---

archive/issue_comments_021728.json:
```json
{
    "body": "Everything looks good here, but I haven't run tests or anything...",
    "created_at": "2008-12-02T22:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3134#issuecomment-21728",
    "user": "https://github.com/rlmill"
}
```

Everything looks good here, but I haven't run tests or anything...



---

archive/issue_comments_021729.json:
```json
{
    "body": "I guess we are going with the PARI version then for speed reasons. And I will run doctests shortly to check if there are any issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T22:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3134#issuecomment-21729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I guess we are going with the PARI version then for speed reasons. And I will run doctests shortly to check if there are any issues.

Cheers,

Michael



---

archive/issue_comments_021730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T15:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3134#issuecomment-21730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021731.json:
```json
{
    "body": "Merged trac_3134-2.patch in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T15:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3134#issuecomment-21731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_3134-2.patch in Sage 3.2.2.alpha0
