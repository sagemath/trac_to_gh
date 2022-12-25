# Issue 454: VERY SEVERE memory leaks, probably in linear algebra -- exposed by modular symbols functionality

archive/issues_000454.json:
```json
{
    "body": "Assignee: @williamstein\n\nTo see some VERY SEVERE memory leaks, probably in linear algebra -- exposed by modular symbols functionality do the following. \n\n1. comment out the line \"_cache[key] = weakref.ref(M)\" in sage/modular/modsym/modsym.py\n2. build and observe:\nsage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()\n174.125\n191.1796875\nsage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()\n191.1796875\n197.6875\nsage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()\n197.6875\n203.5546875\nsage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; get_memory_usage()\n203.546875\n208.12890625\nsage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; get_memory_usage()\n208.12890625\n210.41796875\n\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/454\n\n",
    "created_at": "2007-08-19T08:42:08Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "VERY SEVERE memory leaks, probably in linear algebra -- exposed by modular symbols functionality",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/454",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

To see some VERY SEVERE memory leaks, probably in linear algebra -- exposed by modular symbols functionality do the following. 

1. comment out the line "_cache[key] = weakref.ref(M)" in sage/modular/modsym/modsym.py
2. build and observe:
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()
174.125
191.1796875
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()
191.1796875
197.6875
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()
197.6875
203.5546875
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; get_memory_usage()
203.546875
208.12890625
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; get_memory_usage()
208.12890625
210.41796875

}}}

Issue created by migration from https://trac.sagemath.org/ticket/454





---

archive/issue_comments_002251.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2007-08-19T08:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2251",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to critical.



---

archive/issue_comments_002252.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2007-08-19T08:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2252",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_events_001141.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-19T23:53:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1141"
}
```



---

archive/issue_comments_002253.json:
```json
{
    "body": "Hello William,\n\nI did valgrind that exact example three times in a row in the same sage session and I got:\n\n==14358== LEAK SUMMARY:\n==14358==    definitely lost: 3,297,622 bytes in 194,267 blocks.\n==14358==    indirectly lost: 703,345 bytes in 4,603 blocks.\n==14358==      possibly lost: 387,022 bytes in 984 blocks.\n==14358==    still reachable: 153,105,982 bytes in 1,028,503 blocks.\n==14358==         suppressed: 0 bytes in 0 blocks.\n\nThe complete log is at http://sage.math.washington.edu/home/mabshoff/sage-2.8.1-ticket-454.valgrind\n\nJust search for \"indirectly\" and \"definitely\" to see the most interesting bits. Problems are all over the map: sparse & dense matricies, gmp allocations, LinBox Wrapper and so.\n\nLet me know if you need any help.\n\nI changed the Milestone to 2.8.2 - feel free to assign it to 3.0 if you feel that the 2.8.2 release cuts it too close.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-19T23:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello William,

I did valgrind that exact example three times in a row in the same sage session and I got:

==14358== LEAK SUMMARY:
==14358==    definitely lost: 3,297,622 bytes in 194,267 blocks.
==14358==    indirectly lost: 703,345 bytes in 4,603 blocks.
==14358==      possibly lost: 387,022 bytes in 984 blocks.
==14358==    still reachable: 153,105,982 bytes in 1,028,503 blocks.
==14358==         suppressed: 0 bytes in 0 blocks.

The complete log is at http://sage.math.washington.edu/home/mabshoff/sage-2.8.1-ticket-454.valgrind

Just search for "indirectly" and "definitely" to see the most interesting bits. Problems are all over the map: sparse & dense matricies, gmp allocations, LinBox Wrapper and so.

Let me know if you need any help.

I changed the Milestone to 2.8.2 - feel free to assign it to 3.0 if you feel that the 2.8.2 release cuts it too close.

Cheers,

Michael



---

archive/issue_events_001142.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-20T01:11:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1142"
}
```



---

archive/issue_events_001143.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-20T01:11:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.8.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1143"
}
```



---

archive/issue_events_001144.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T01:57:39Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.8.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1144"
}
```



---

archive/issue_events_001145.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-29T01:57:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1145"
}
```



---

archive/issue_comments_002254.json:
```json
{
    "body": "Ok,\n\nvarious bits and pieces have been broken out into different tickets and fixed. We should revisit this ticket during Bug Day 2 and see what is left.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-29T22:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2254",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok,

various bits and pieces have been broken out into different tickets and fixed. We should revisit this ticket during Bug Day 2 and see what is left.

Cheers,

Michael



---

archive/issue_comments_002255.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-29T22:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2255",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002256.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-08-29T22:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2256",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_002257.json:
```json
{
    "body": "A status update for Sage 2.8.7.rc1:\n\ncode run:\n\n```\nfor n in range(10,100):\n  a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()\n```\n\nBefore:\n\n```\n==29058== LEAK SUMMARY:\n==29058==    definitely lost: 1,210,265 bytes in 113,436 blocks.\n==29058==    indirectly lost: 420,632 bytes in 7,210 blocks.\n==29058==      possibly lost: 375,630 bytes in 1,188 blocks.\n==29058==    still reachable: 92,961,383 bytes in 1,342,309 blocks.\n```\n\nAfter Patch 1 (fix for #619):\n\n```\n==13453== LEAK SUMMARY:\n==13453==    definitely lost: 1,075,235 bytes in 96,549 blocks.\n==13453==    indirectly lost: 419,640 bytes in 7,212 blocks.\n==13453==      possibly lost: 376,270 bytes in 1,195 blocks.\n==13453==    still reachable: 92,923,804 bytes in 1,342,166 blocks.\n==13453==         suppressed: 0 bytes in 0 blocks.\n```\n\nAfter Patch 2 (burcin's fix for #561):\n\n```\n==15147== LEAK SUMMARY:\n==15147==    definitely lost: 1,072,216 bytes in 96,412 blocks.\n==15147==    indirectly lost: 419,120 bytes in 7,205 blocks.\n==15147==      possibly lost: 376,558 bytes in 1,194 blocks.\n==15147==    still reachable: 92,977,412 bytes in 1,342,343 blocks.\n==15147==         suppressed: 0 bytes in 0 blocks.\n```\n\nRemaining leak: mix of LinBox and\n\n```\n==15147== 94,288 bytes in 11,786 blocks are definitely lost in loss record 2,401 of 2,546\n==15147==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==15147==    by 0x610A9A6: __gmpq_init (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)\n==15147==    by 0x12EC8E22: __pyx_f_22matrix_rational_sparse_allocate_mpq_vector (matrix_rational_sparse.c:5519)\n==15147==    by 0x12ECC464: __pyx_f_22matrix_rational_sparse_mpq_vector_set_entry (matrix_rational_sparse.c:6560)\n==15147==    by 0x12ECC5F5: __pyx_f_22matrix_rational_sparse_22Matrix_rational_sparse_set_unsafe (matrix_rational_sparse.c:8\n668)\n==15147==    by 0x114ED321: __pyx_mp_ass_subscript_7matrix0_Matrix (matrix0.c:2339)\n==15147==    by 0x47F046: PyEval_EvalFrameEx (ceval.c:1497)\n==15147==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==15147==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n```\n",
    "created_at": "2007-10-16T03:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2257",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A status update for Sage 2.8.7.rc1:

code run:

```
for n in range(10,100):
  a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

Before:

```
==29058== LEAK SUMMARY:
==29058==    definitely lost: 1,210,265 bytes in 113,436 blocks.
==29058==    indirectly lost: 420,632 bytes in 7,210 blocks.
==29058==      possibly lost: 375,630 bytes in 1,188 blocks.
==29058==    still reachable: 92,961,383 bytes in 1,342,309 blocks.
```

After Patch 1 (fix for #619):

```
==13453== LEAK SUMMARY:
==13453==    definitely lost: 1,075,235 bytes in 96,549 blocks.
==13453==    indirectly lost: 419,640 bytes in 7,212 blocks.
==13453==      possibly lost: 376,270 bytes in 1,195 blocks.
==13453==    still reachable: 92,923,804 bytes in 1,342,166 blocks.
==13453==         suppressed: 0 bytes in 0 blocks.
```

After Patch 2 (burcin's fix for #561):

```
==15147== LEAK SUMMARY:
==15147==    definitely lost: 1,072,216 bytes in 96,412 blocks.
==15147==    indirectly lost: 419,120 bytes in 7,205 blocks.
==15147==      possibly lost: 376,558 bytes in 1,194 blocks.
==15147==    still reachable: 92,977,412 bytes in 1,342,343 blocks.
==15147==         suppressed: 0 bytes in 0 blocks.
```

Remaining leak: mix of LinBox and

```
==15147== 94,288 bytes in 11,786 blocks are definitely lost in loss record 2,401 of 2,546
==15147==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==15147==    by 0x610A9A6: __gmpq_init (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)
==15147==    by 0x12EC8E22: __pyx_f_22matrix_rational_sparse_allocate_mpq_vector (matrix_rational_sparse.c:5519)
==15147==    by 0x12ECC464: __pyx_f_22matrix_rational_sparse_mpq_vector_set_entry (matrix_rational_sparse.c:6560)
==15147==    by 0x12ECC5F5: __pyx_f_22matrix_rational_sparse_22Matrix_rational_sparse_set_unsafe (matrix_rational_sparse.c:8
668)
==15147==    by 0x114ED321: __pyx_mp_ass_subscript_7matrix0_Matrix (matrix0.c:2339)
==15147==    by 0x47F046: PyEval_EvalFrameEx (ceval.c:1497)
==15147==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==15147==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
```




---

archive/issue_comments_002258.json:
```json
{
    "body": "With 2.8.10.rc1 (which applied #1024) we get:\n\n```\n==15811== LEAK SUMMARY:\n==15811==    definitely lost: 406,088 bytes in 5,792 blocks.\n==15811==    indirectly lost: 415,504 bytes in 7,199 blocks.\n==15811==      possibly lost: 382,110 bytes in 1,198 blocks.\n==15811==    still reachable: 93,391,247 bytes in 1,343,745 blocks.\n==15811==         suppressed: 0 bytes in 0 blocks.\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-10-28T22:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2258",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With 2.8.10.rc1 (which applied #1024) we get:

```
==15811== LEAK SUMMARY:
==15811==    definitely lost: 406,088 bytes in 5,792 blocks.
==15811==    indirectly lost: 415,504 bytes in 7,199 blocks.
==15811==      possibly lost: 382,110 bytes in 1,198 blocks.
==15811==    still reachable: 93,391,247 bytes in 1,343,745 blocks.
==15811==         suppressed: 0 bytes in 0 blocks.
```

Cheers,

Michael



---

archive/issue_comments_002259.json:
```json
{
    "body": "Once #1026 is merged we will have:\n\n```\n==19741== LEAK SUMMARY:\n==19741==    definitely lost: 11,608 bytes in 352 blocks.\n==19741==    indirectly lost: 286,560 bytes in 390 blocks.\n==19741==      possibly lost: 463,342 bytes in 879 blocks.\n==19741==    still reachable: 71,109,048 bytes in 1,285,713 blocks.\n==19741==         suppressed: 0 bytes in 0 blocks.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-10-29T04:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2259",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Once #1026 is merged we will have:

```
==19741== LEAK SUMMARY:
==19741==    definitely lost: 11,608 bytes in 352 blocks.
==19741==    indirectly lost: 286,560 bytes in 390 blocks.
==19741==      possibly lost: 463,342 bytes in 879 blocks.
==19741==    still reachable: 71,109,048 bytes in 1,285,713 blocks.
==19741==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael



---

archive/issue_comments_002260.json:
```json
{
    "body": "With Sage 2.9.1.1 we get:\n\n```\n==29169==    definitely lost: 1,237 bytes in 54 blocks.\n==29169==    indirectly lost: 7,704 bytes in 345 blocks.\n==29169==      possibly lost: 407,801 bytes in 991 blocks.\n==29169==    still reachable: 74,012,699 bytes in 1,287,766 blocks.\n==29169==         suppressed: 0 bytes in 0 blocks.\n```\n\nThe remaining definitely & indirectly lost are all due to known problems in LinBox when using Givaro.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-26T15:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2260",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With Sage 2.9.1.1 we get:

```
==29169==    definitely lost: 1,237 bytes in 54 blocks.
==29169==    indirectly lost: 7,704 bytes in 345 blocks.
==29169==      possibly lost: 407,801 bytes in 991 blocks.
==29169==    still reachable: 74,012,699 bytes in 1,287,766 blocks.
==29169==         suppressed: 0 bytes in 0 blocks.
```

The remaining definitely & indirectly lost are all due to known problems in LinBox when using Givaro.

Cheers,

Michael



---

archive/issue_events_001146.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-26T15:56:38Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1146"
}
```



---

archive/issue_events_001147.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-26T15:56:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1147"
}
```



---

archive/issue_comments_002261.json:
```json
{
    "body": "With the updated givaro.spkg from #2525 the leak in LinBox that was caused by Givaro is gone. Hence once that ticket is merged we cam close this old, long overdue ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T05:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2261",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the updated givaro.spkg from #2525 the leak in LinBox that was caused by Givaro is gone. Hence once that ticket is merged we cam close this old, long overdue ticket.

Cheers,

Michael



---

archive/issue_events_001148.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T05:06:22Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1148"
}
```



---

archive/issue_events_001149.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T05:06:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1149"
}
```



---

archive/issue_comments_002262.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-15T06:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2262",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002263.json:
```json
{
    "body": "Closed in Sage 2.10.4.alpha0\n\nSince #2524 has been merged this is in effect fixed. #2525 does fix some other issues, but not the memory leak that is the last one left.\n\nMany people have contributed to fixing this ticket over a seven month period:\n\n* Michael Abshoff\n* Martin Albrecht\n* Burcin Erocal\n* Willem Jan Palenstijn\n* Clement Pernet\n* William Stein \n\nIt is good to have reached the end of this journey.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-15T06:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/454#issuecomment-2263",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Closed in Sage 2.10.4.alpha0

Since #2524 has been merged this is in effect fixed. #2525 does fix some other issues, but not the memory leak that is the last one left.

Many people have contributed to fixing this ticket over a seven month period:

* Michael Abshoff
* Martin Albrecht
* Burcin Erocal
* Willem Jan Palenstijn
* Clement Pernet
* William Stein 

It is good to have reached the end of this journey.

Cheers,

Michael



---

archive/issue_events_001150.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-15T06:44:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/454",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/454#event-1150"
}
```
