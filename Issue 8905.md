# Issue 8905: Memory leak in echelon over QQ

archive/issues_008905.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mderickx\n\nKeywords: memleak echelonize\n\nApparently there is a memory leak in Sage-4.4 when one echelonizes a matrix over ``QQ``:\n\n```\nsage: MS = MatrixSpace(QQ,8)\nsage: M = MS.random_element()\nsage: N = copy(M)\nsage: N.echelonize()\nsage: N==M\nFalse\nsage: mem = get_memory_usage()\nsage: n = 0\nsage: while(1):\n....:     n+=1\n....:     if get_memory_usage()>mem:\n....:         mem = get_memory_usage()\n....:         print mem,n\n....:     N = copy(M)\n....:     N.echelonize()\n....:\n797.95703125 1\n798.0859375 32\n798.21484375 71\n798.34375 110\n798.47265625 155\n798.6015625 199\n798.8515625 202\n798.98046875 243\n799.109375 292\n799.23828125 329\n799.37109375 371\n799.5 406\n799.79296875 426\n799.921875 471\n800.05078125 530\n800.1796875 582\n800.30859375 634\n800.61328125 666\n...\n```\n\n\nHere I show that the critical step really is the echelon form:\n\n```\nsage: MS = MatrixSpace(QQ,8)\nsage: M = MS.random_element()\nsage: N = copy(M)\nsage: mem = get_memory_usage()\nsage: n = 0\nsage: while(1):\n....:     n+=1\n....:     if get_memory_usage()>mem:\n....:         mem = get_memory_usage()\n....:         print mem,n\n....:     N = copy(M)\n....:\n797.92578125 1\n```\n\nThe memory consumption is stable at that point. So, copying ``M`` is no problem, but computing the echelon form is!\n\nIssue created by migration from https://trac.sagemath.org/ticket/8905\n\n",
    "created_at": "2010-05-06T12:19:17Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Memory leak in echelon over QQ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8905",
    "user": "SimonKing"
}
```
Assignee: tbd

CC:  mderickx

Keywords: memleak echelonize

Apparently there is a memory leak in Sage-4.4 when one echelonizes a matrix over ``QQ``:

```
sage: MS = MatrixSpace(QQ,8)
sage: M = MS.random_element()
sage: N = copy(M)
sage: N.echelonize()
sage: N==M
False
sage: mem = get_memory_usage()
sage: n = 0
sage: while(1):
....:     n+=1
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:     N = copy(M)
....:     N.echelonize()
....:
797.95703125 1
798.0859375 32
798.21484375 71
798.34375 110
798.47265625 155
798.6015625 199
798.8515625 202
798.98046875 243
799.109375 292
799.23828125 329
799.37109375 371
799.5 406
799.79296875 426
799.921875 471
800.05078125 530
800.1796875 582
800.30859375 634
800.61328125 666
...
```


Here I show that the critical step really is the echelon form:

```
sage: MS = MatrixSpace(QQ,8)
sage: M = MS.random_element()
sage: N = copy(M)
sage: mem = get_memory_usage()
sage: n = 0
sage: while(1):
....:     n+=1
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:     N = copy(M)
....:
797.92578125 1
```

The memory consumption is stable at that point. So, copying ``M`` is no problem, but computing the echelon form is!

Issue created by migration from https://trac.sagemath.org/ticket/8905





---

archive/issue_comments_081971.json:
```json
{
    "body": "Similarly, one gets\n\n```\nsage: MS = MatrixSpace(QQ,8)\nsage: M = MS.random_element()\nsage: M = M.stack(M)\nsage: v = copy(M).left_kernel()\nsage: n = 0\nsage: mem = get_memory_usage()\nsage: while(1):\n....:     n+=1\n....:     if get_memory_usage()>mem:\n....:         mem = get_memory_usage()\n....:         print mem,n\n....:     v = copy(M).left_kernel()\n....:\n800.3828125 27\n800.51171875 62\n800.640625 94\n800.76953125 151\n801.05078125 168\n801.1796875 187\n801.30859375 221\n801.4375 256\n801.56640625 278\n801.71484375 314\n802.08984375 375\n802.21875 423\n802.34765625 460\n802.4765625 497\n802.60546875 521\n802.8984375 610\n803.02734375 635\n803.15625 690\n```\n\nI guess the two are related.",
    "created_at": "2010-05-06T14:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81971",
    "user": "SimonKing"
}
```

Similarly, one gets

```
sage: MS = MatrixSpace(QQ,8)
sage: M = MS.random_element()
sage: M = M.stack(M)
sage: v = copy(M).left_kernel()
sage: n = 0
sage: mem = get_memory_usage()
sage: while(1):
....:     n+=1
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:     v = copy(M).left_kernel()
....:
800.3828125 27
800.51171875 62
800.640625 94
800.76953125 151
801.05078125 168
801.1796875 187
801.30859375 221
801.4375 256
801.56640625 278
801.71484375 314
802.08984375 375
802.21875 423
802.34765625 460
802.4765625 497
802.60546875 521
802.8984375 610
803.02734375 635
803.15625 690
```

I guess the two are related.



---

archive/issue_comments_081972.json:
```json
{
    "body": "I guess #10262 might explain both of these leaks. I wouldn't find it strange that somewhere in both algorithms scalar*vector multiplication happens.",
    "created_at": "2011-01-08T01:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81972",
    "user": "mderickx"
}
```

I guess #10262 might explain both of these leaks. I wouldn't find it strange that somewhere in both algorithms scalar*vector multiplication happens.



---

archive/issue_comments_081973.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-11T17:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81973",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081974.json:
```json
{
    "body": "Seems to be fixed indeed.\n\n\n```\n\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\n\u2502 SageMath Version 6.6.rc2, Release Date: 2015-04-02                 \u2502\n[...]\nsage: MS = MatrixSpace(QQ,8)\nsage: M = MS.random_element()\nsage: N = copy(M)\nsage: N.echelonize()\nsage: N==M\nFalse\nsage: mem = get_memory_usage()\nsage: n = 0\nsage: while(1):\n....:     n+=1\n....:     if get_memory_usage()>mem:\n....:         mem = get_memory_usage()\n....:         print mem,n\n....:     N = copy(M)\n....:     N.echelonize()\n....:\n1006.625 2302\n1006.875 19154\n1007.0078125 27590\n1007.2578125 36321\n```\n",
    "created_at": "2015-04-11T17:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81974",
    "user": "mmezzarobba"
}
```

Seems to be fixed indeed.


```
┌────────────────────────────────────────────────────────────────────┐
│ SageMath Version 6.6.rc2, Release Date: 2015-04-02                 │
[...]
sage: MS = MatrixSpace(QQ,8)
sage: M = MS.random_element()
sage: N = copy(M)
sage: N.echelonize()
sage: N==M
False
sage: mem = get_memory_usage()
sage: n = 0
sage: while(1):
....:     n+=1
....:     if get_memory_usage()>mem:
....:         mem = get_memory_usage()
....:         print mem,n
....:     N = copy(M)
....:     N.echelonize()
....:
1006.625 2302
1006.875 19154
1007.0078125 27590
1007.2578125 36321
```




---

archive/issue_comments_081975.json:
```json
{
    "body": "Marco, the numbers you are giving indicate that the memory leak is smaller than before. But why do you think it is fixed?",
    "created_at": "2015-04-11T18:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81975",
    "user": "SimonKing"
}
```

Marco, the numbers you are giving indicate that the memory leak is smaller than before. But why do you think it is fixed?



---

archive/issue_comments_081976.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-04-11T18:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81976",
    "user": "SimonKing"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_081977.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2015-04-11T19:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81977",
    "user": "mmezzarobba"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_081978.json:
```json
{
    "body": "Replying to [comment:10 SimonKing]:\n> Marco, the numbers you are giving indicate that the memory leak is smaller than before. But why do you think it is fixed?\n\nNo, you are right, I misread the results. It looks like we are still leaking about 16 bytes per call.",
    "created_at": "2015-04-11T19:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81978",
    "user": "mmezzarobba"
}
```

Replying to [comment:10 SimonKing]:
> Marco, the numbers you are giving indicate that the memory leak is smaller than before. But why do you think it is fixed?

No, you are right, I misread the results. It looks like we are still leaking about 16 bytes per call.



---

archive/issue_comments_081979.json:
```json
{
    "body": "Replying to [comment:11 mmezzarobba]:\n> No, you are right, I misread the results. It looks like we are still leaking about 16 bytes per call.\n\nI wouldn't be so quick to conclude linear behaviour from so few data points. I'm getting:\n\n```\n1130.9375 1\n1131.1875 5107\n1131.4375 22580\n1131.6875 39743\n```\n\nand no further increase up to `n=738068` (after which I gave up). Echelonization over QQ likely leads to very complicated memory use (lots of allocation/deallocation), so together with non-deterministic gc (because parents only clear on triggered GC) you expect that the memory layout shows a lot of short-term fluctuations: fragmentation will lead to slowly increasing memory footprint; hopefully stabilizing over long periods. The numbers above are quite consistent with that. Certainly gc.objects() is not showing any significant object accumulation, so any leak would have to be outside python.\n\nI see no indication of a memory leak here anymore, but I guess you could valgrind it to be certain.",
    "created_at": "2015-04-11T19:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81979",
    "user": "nbruin"
}
```

Replying to [comment:11 mmezzarobba]:
> No, you are right, I misread the results. It looks like we are still leaking about 16 bytes per call.

I wouldn't be so quick to conclude linear behaviour from so few data points. I'm getting:

```
1130.9375 1
1131.1875 5107
1131.4375 22580
1131.6875 39743
```

and no further increase up to `n=738068` (after which I gave up). Echelonization over QQ likely leads to very complicated memory use (lots of allocation/deallocation), so together with non-deterministic gc (because parents only clear on triggered GC) you expect that the memory layout shows a lot of short-term fluctuations: fragmentation will lead to slowly increasing memory footprint; hopefully stabilizing over long periods. The numbers above are quite consistent with that. Certainly gc.objects() is not showing any significant object accumulation, so any leak would have to be outside python.

I see no indication of a memory leak here anymore, but I guess you could valgrind it to be certain.



---

archive/issue_comments_081980.json:
```json
{
    "body": "Yes, I came to the same conclusion after letting it run for a bit longer:\n\n```\n1005.9921875 376\n1006.2421875 2015\n1006.4921875 19150\n1006.4921875 20000\n1006.640625 30356\n1006.890625 36624\n1006.890625 40000\n1006.890625 60000\n1006.890625 80000\n1007.140625 95959\n1007.140625 100000\n1007.140625 6000000\n```\n",
    "created_at": "2015-04-11T20:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81980",
    "user": "mmezzarobba"
}
```

Yes, I came to the same conclusion after letting it run for a bit longer:

```
1005.9921875 376
1006.2421875 2015
1006.4921875 19150
1006.4921875 20000
1006.640625 30356
1006.890625 36624
1006.890625 40000
1006.890625 60000
1006.890625 80000
1007.140625 95959
1007.140625 100000
1007.140625 6000000
```




---

archive/issue_comments_081981.json:
```json
{
    "body": "Setting the ticket to duplicate/positive_review as we agree that the problem is fixed and there is no obvious regression test to add.",
    "created_at": "2015-04-13T12:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81981",
    "user": "mmezzarobba"
}
```

Setting the ticket to duplicate/positive_review as we agree that the problem is fixed and there is no obvious regression test to add.



---

archive/issue_comments_081982.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-04-13T12:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81982",
    "user": "mmezzarobba"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_081983.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-13T17:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8905#issuecomment-81983",
    "user": "vbraun"
}
```

Resolution: fixed
