# Issue 4023: Sage 3.1.2.alpha3: 32 vs. 64 b bit doctesting issuess for gp

archive/issues_004023.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @malb\n\nJohn Cremona reported:\n\n```\nsage -t  devel/sage/sage/interfaces/gp.py \n********************************************************************** \nFile \"/home/john/sage-3.1.2.alpha3/tmp/gp.py\", line 266: \n    sage: gp.get_precision() \nExpected: \n    38 \nGot: \n    28 \n********************************************************************** \nFile \"/home/john/sage-3.1.2.alpha3/tmp/gp.py\", line 520: \n    sage: gp.new_with_bits_prec(pi, 100) \nExpected: \n    3.1415926535897932384626433832795028842 \nGot: \n    3.141592653589793238462643383 \n********************************************************************** \nFile \"/home/john/sage-3.1.2.alpha3/tmp/gp.py\", line 244: \n    sage: gp.get_precision() \nExpected: \n    38 \nGot: \n    28 \n********************************************************************** \n3 items had failures: \n   1 of   6 in __main__.example_10 \n   1 of   3 in __main__.example_27 \n   1 of   3 in __main__.example_9 \n***Test Failed*** 3 failures. \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4023\n\n",
    "created_at": "2008-08-31T18:58:50Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Sage 3.1.2.alpha3: 32 vs. 64 b bit doctesting issuess for gp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4023",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @malb

John Cremona reported:

```
sage -t  devel/sage/sage/interfaces/gp.py 
********************************************************************** 
File "/home/john/sage-3.1.2.alpha3/tmp/gp.py", line 266: 
    sage: gp.get_precision() 
Expected: 
    38 
Got: 
    28 
********************************************************************** 
File "/home/john/sage-3.1.2.alpha3/tmp/gp.py", line 520: 
    sage: gp.new_with_bits_prec(pi, 100) 
Expected: 
    3.1415926535897932384626433832795028842 
Got: 
    3.141592653589793238462643383 
********************************************************************** 
File "/home/john/sage-3.1.2.alpha3/tmp/gp.py", line 244: 
    sage: gp.get_precision() 
Expected: 
    38 
Got: 
    28 
********************************************************************** 
3 items had failures: 
   1 of   6 in __main__.example_10 
   1 of   3 in __main__.example_27 
   1 of   3 in __main__.example_9 
***Test Failed*** 3 failures. 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4023





---

archive/issue_comments_028954.json:
```json
{
    "body": "Standard fix (gp has a default precision of 38 on 64-bit architectures, and 28 on 32-bit).\n\nThere are more serious pari precision issues tracked at #4064.",
    "created_at": "2008-09-05T01:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28954",
    "user": "https://github.com/aghitza"
}
```

Standard fix (gp has a default precision of 38 on 64-bit architectures, and 28 on 32-bit).

There are more serious pari precision issues tracked at #4064.



---

archive/issue_comments_028955.json:
```json
{
    "body": "Yeah, I had similar changes to submit. But I would like to add a remark to the gp.new_with_bits_prec(pi, 100) that the result is wrong and the issue tracked at #4064.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-05T01:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28955",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yeah, I had similar changes to submit. But I would like to add a remark to the gp.new_with_bits_prec(pi, 100) that the result is wrong and the issue tracked at #4064.

Cheers,

Michael



---

archive/issue_comments_028956.json:
```json
{
    "body": "Attachment [4023-gp_32_bit.patch](tarball://root/attachments/some-uuid/ticket4023/4023-gp_32_bit.patch) by @aghitza created at 2008-09-05 04:00:02",
    "created_at": "2008-09-05T04:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28956",
    "user": "https://github.com/aghitza"
}
```

Attachment [4023-gp_32_bit.patch](tarball://root/attachments/some-uuid/ticket4023/4023-gp_32_bit.patch) by @aghitza created at 2008-09-05 04:00:02



---

archive/issue_comments_028957.json:
```json
{
    "body": "I have looked into the matter of the second doctest failure more carefully and figured out that there were two problems with the function gp.new_with_bits_prec():\n\n1. the code was doing the wrong thing\n\n2. the doctest was testing the wrong thing (but the result was correct)\n\nBasically, asking gp to print out pi was pointless because gp's precision had been reset to its default (so of course it would only print the first 28 or 38 digits).  The new patch fixes the code and the doctests.  I don't have access to a 64-bit machine so I had to produce the 64-bit doctest results by pure thought, so it would be great if someone could actually doctest this.",
    "created_at": "2008-09-05T04:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28957",
    "user": "https://github.com/aghitza"
}
```

I have looked into the matter of the second doctest failure more carefully and figured out that there were two problems with the function gp.new_with_bits_prec():

1. the code was doing the wrong thing

2. the doctest was testing the wrong thing (but the result was correct)

Basically, asking gp to print out pi was pointless because gp's precision had been reset to its default (so of course it would only print the first 28 or 38 digits).  The new patch fixes the code and the doctests.  I don't have access to a 64-bit machine so I had to produce the 64-bit doctest results by pure thought, so it would be great if someone could actually doctest this.



---

archive/issue_comments_028958.json:
```json
{
    "body": "Patch looks good to me, but we have one doctest failure:\n\n```\nsage -t -long devel/sage/sage/crypto/mq/sr.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha5/tmp/sr.py\", line 1407:\n    sage: s\nExpected:\n    {k000: 1, k001: 0, k003: 1, k002: 0}\nGot:\n    {k000: 1, k001: 0, k002: 0, k003: 1}\n**********************************************************************\n```\n\nThe output is identical except that the order has slightly changed. Malb? \n\nCheers,\n\nMichael",
    "created_at": "2008-09-05T06:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me, but we have one doctest failure:

```
sage -t -long devel/sage/sage/crypto/mq/sr.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha5/tmp/sr.py", line 1407:
    sage: s
Expected:
    {k000: 1, k001: 0, k003: 1, k002: 0}
Got:
    {k000: 1, k001: 0, k002: 0, k003: 1}
**********************************************************************
```

The output is identical except that the order has slightly changed. Malb? 

Cheers,

Michael



---

archive/issue_comments_028959.json:
```json
{
    "body": "That's alright, it is a set and thus the order depends on the hash.",
    "created_at": "2008-09-05T09:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28959",
    "user": "https://github.com/malb"
}
```

That's alright, it is a set and thus the order depends on the hash.



---

archive/issue_comments_028960.json:
```json
{
    "body": "Replying to [comment:5 malb]:\n> That's alright, it is a set and thus the order depends on the hash.\n\nOk, with Martin's approval of the sr.py doctest fix this is a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-05T10:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28960",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 malb]:
> That's alright, it is a set and thus the order depends on the hash.

Ok, with Martin's approval of the sr.py doctest fix this is a positive review.

Cheers,

Michael



---

archive/issue_comments_028961.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0. I also fixed the doctest failure.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-05T11:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0. I also fixed the doctest failure.

Cheers,

Michael



---

archive/issue_events_004253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-05T11:12:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4023#event-4253"
}
```



---

archive/issue_comments_028962.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-05T11:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4023#issuecomment-28962",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
