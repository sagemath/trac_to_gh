# Issue 3204: [with spkg, needs review] update M4RI to version 20080514

archive/issues_003204.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: linear algebra, gf(2), m4ri\n\nA new version of M4RI is available at:\n\n   http://sage.math.washington.edu/home/malb/m4ri/\n\nThe matching SPKG is at:\n\n  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080514.p0.spkg\n\nThis SPKG needs a patch which is attached to this ticket.\n\nThe new version has quite a new features:\n* Strassen-Winograd matrix multiplication (though not used by default yet),\n* Native support for Solaris and Windows,\n* SSE2 support,\n* Much improved documentation,\n* Nicer calling conventions.\n\nThe SSE2 support could cause trouble but I've successfully built the library on 32 and 64-bit Linux, OSX (Intel and PPC), OpenSolaris 2008.05 and Windows XP.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3204\n\n",
    "created_at": "2008-05-14T20:35:58Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "[with spkg, needs review] update M4RI to version 20080514",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3204",
    "user": "malb"
}
```
Assignee: malb

Keywords: linear algebra, gf(2), m4ri

A new version of M4RI is available at:

   http://sage.math.washington.edu/home/malb/m4ri/

The matching SPKG is at:

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080514.p0.spkg

This SPKG needs a patch which is attached to this ticket.

The new version has quite a new features:
* Strassen-Winograd matrix multiplication (though not used by default yet),
* Native support for Solaris and Windows,
* SSE2 support,
* Much improved documentation,
* Nicer calling conventions.

The SSE2 support could cause trouble but I've successfully built the library on 32 and 64-bit Linux, OSX (Intel and PPC), OpenSolaris 2008.05 and Windows XP.

Issue created by migration from https://trac.sagemath.org/ticket/3204





---

archive/issue_comments_022137.json:
```json
{
    "body": "I'm curious what the speed differences are with SSE2 support now.  Do you have any timings?",
    "created_at": "2008-05-14T22:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22137",
    "user": "jason"
}
```

I'm curious what the speed differences are with SSE2 support now.  Do you have any timings?



---

archive/issue_comments_022138.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> I'm curious what the speed differences are with SSE2 support now.  Do you have any timings?\n\nIt is not too overwhelming:\n* It only improves things up t L2 cache size for my code since then the cache miss is more expensive, however a more clever programmer might be able to prefetch around this problem.\n* On AMD CPUs it seems slower (see my mail to [sage-devel])\n\n**64-bit Debian/Linux Core2Duo 2.33Ghz without SSE2**\n\n\n```\nsage: A = random_matrix(GF(2),8*1024,8*1024)\nsage: B = random_matrix(GF(2),8*1024,8*1024)\nsage: time C = A._multiply_strassen(B,cutoff=1024)\nCPU times: user 2.25 s, sys: 0.01 s, total: 2.26 s\nWall time: 2.28\n\nsage: time C = A._multiply_strassen(B,cutoff=2*1024)\nCPU times: user 2.11 s, sys: 0.02 s, total: 2.13 s\nWall time: 2.13\n\nsage: time C = A._multiply_strassen(B,cutoff=4*1024)\nCPU times: user 4.27 s, sys: 0.01 s, total: 4.28 s\nWall time: 4.31\n\nsage: A = random_matrix(GF(2),16*1024,16*1024)\nsage: B = random_matrix(GF(2),16*1024,16*1024)\nsage: time C = A._multiply_strassen(B,cutoff=2*1024)\nCPU times: user 25.01 s, sys: 0.09 s, total: 25.09 s\nWall time: 25.23\n```\n\n\n**64-bit Debian/Linux Core2Duo 2.33Ghz with SSE2**\n\n\n```\nsage: A = random_matrix(GF(2),8*1024,8*1024)\nsage: B = random_matrix(GF(2),8*1024,8*1024)\nsage: time C = A._multiply_strassen(B,cutoff=1024)\nCPU times: user 2.29 s, sys: 0.01 s, total: 2.30 s\nWall time: 2.32\n\nsage: time C = A._multiply_strassen(B,cutoff=2*1024)\nCPU times: user 1.82 s, sys: 0.02 s, total: 1.84 s\nWall time: 1.86\n\nsage: time C = A._multiply_strassen(B,cutoff=4*1024)\nCPU times: user 3.73 s, sys: 0.16 s, total: 3.89 s\nWall time: 3.99\n\nsage: A = random_matrix(GF(2),16*1024,16*1024)\nsage: B = random_matrix(GF(2),16*1024,16*1024)\nsage: time C = A._multiply_strassen(B,cutoff=2*1024)\nCPU times: user 22.84 s, sys: 0.08 s, total: 22.93 s\nWall time: 23.06\n```\n\n\nI don't claim to have a close to optimal implementation, though. In fact, this experience taught me that there is much I don't yet understand about writing tight C code.",
    "created_at": "2008-05-14T23:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22138",
    "user": "malb"
}
```

Replying to [comment:1 jason]:
> I'm curious what the speed differences are with SSE2 support now.  Do you have any timings?

It is not too overwhelming:
* It only improves things up t L2 cache size for my code since then the cache miss is more expensive, however a more clever programmer might be able to prefetch around this problem.
* On AMD CPUs it seems slower (see my mail to [sage-devel])

**64-bit Debian/Linux Core2Duo 2.33Ghz without SSE2**


```
sage: A = random_matrix(GF(2),8*1024,8*1024)
sage: B = random_matrix(GF(2),8*1024,8*1024)
sage: time C = A._multiply_strassen(B,cutoff=1024)
CPU times: user 2.25 s, sys: 0.01 s, total: 2.26 s
Wall time: 2.28

sage: time C = A._multiply_strassen(B,cutoff=2*1024)
CPU times: user 2.11 s, sys: 0.02 s, total: 2.13 s
Wall time: 2.13

sage: time C = A._multiply_strassen(B,cutoff=4*1024)
CPU times: user 4.27 s, sys: 0.01 s, total: 4.28 s
Wall time: 4.31

sage: A = random_matrix(GF(2),16*1024,16*1024)
sage: B = random_matrix(GF(2),16*1024,16*1024)
sage: time C = A._multiply_strassen(B,cutoff=2*1024)
CPU times: user 25.01 s, sys: 0.09 s, total: 25.09 s
Wall time: 25.23
```


**64-bit Debian/Linux Core2Duo 2.33Ghz with SSE2**


```
sage: A = random_matrix(GF(2),8*1024,8*1024)
sage: B = random_matrix(GF(2),8*1024,8*1024)
sage: time C = A._multiply_strassen(B,cutoff=1024)
CPU times: user 2.29 s, sys: 0.01 s, total: 2.30 s
Wall time: 2.32

sage: time C = A._multiply_strassen(B,cutoff=2*1024)
CPU times: user 1.82 s, sys: 0.02 s, total: 1.84 s
Wall time: 1.86

sage: time C = A._multiply_strassen(B,cutoff=4*1024)
CPU times: user 3.73 s, sys: 0.16 s, total: 3.89 s
Wall time: 3.99

sage: A = random_matrix(GF(2),16*1024,16*1024)
sage: B = random_matrix(GF(2),16*1024,16*1024)
sage: time C = A._multiply_strassen(B,cutoff=2*1024)
CPU times: user 22.84 s, sys: 0.08 s, total: 22.93 s
Wall time: 23.06
```


I don't claim to have a close to optimal implementation, though. In fact, this experience taught me that there is much I don't yet understand about writing tight C code.



---

archive/issue_comments_022139.json:
```json
{
    "body": "REVIEW:\n\n```\ntried your new code up at #3204 under OS X and get this:\n\nsage: A = random_matrix(GF(2),10^4,10^4)\nsage: B = random_matrix(GF(2),10^4,10^4)\nsage: time C = A._multiply_strassen(B,cutoff=3200)\nsage.bin(39971) malloc: *** error for object 0xb95c010: Non-aligned\npointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(39971) malloc: *** error for object 0x79c9c10: Non-aligned\npointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(39971) malloc: *** error for object 0x7465a00:\nnon-page-aligned, non-allocated pointer being freed\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(39971) malloc: *** error for object 0x79ca610: Non-aligned\npointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\n...\nCPU times: user 10.29 s, sys: 0.26 s, total: 10.55 s\nWall time: 16.31\n\nMaybe you're doing something wrong?\n```\n",
    "created_at": "2008-05-15T00:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22139",
    "user": "was"
}
```

REVIEW:

```
tried your new code up at #3204 under OS X and get this:

sage: A = random_matrix(GF(2),10^4,10^4)
sage: B = random_matrix(GF(2),10^4,10^4)
sage: time C = A._multiply_strassen(B,cutoff=3200)
sage.bin(39971) malloc: *** error for object 0xb95c010: Non-aligned
pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(39971) malloc: *** error for object 0x79c9c10: Non-aligned
pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(39971) malloc: *** error for object 0x7465a00:
non-page-aligned, non-allocated pointer being freed
*** set a breakpoint in malloc_error_break to debug
sage.bin(39971) malloc: *** error for object 0x79ca610: Non-aligned
pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
...
CPU times: user 10.29 s, sys: 0.26 s, total: 10.55 s
Wall time: 16.31

Maybe you're doing something wrong?
```




---

archive/issue_comments_022140.json:
```json
{
    "body": "REPORT:\n\nI'm using OS X 10.5.1 with GCC gcc version 4.0.1 (Apple Inc. build 5465) on my os x core 2 duo laptop.   After using your updated spkg (libm4ri-20080514.p0) and latest posted patch\nI get even more memory errors!:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: m4ri\nsage: A = random_matrix(GF(2),10^4,10^4)\nsage: B = random_matrix(GF(2),10^4,10^4)\nsage: time C = A._multiply_strassen(B,cutoff=3200)\nsage: sage: A = random_matrix(GF(2),10^4,10^4)\nsage: sage: B = random_matrix(GF(2),10^4,10^4)\nsage: sage: time C = A._multiply_strassen(B,cutoff=3200)\nsage.bin(58961) malloc: *** error for object 0xbaba010: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(58961) malloc: *** error for object 0x78f3610: Non-aligned pointer being freed (2)\n*** set a breakpoint in malloc_error_break to debug\nthousands more\nCPU times: user 9.03 s, sys: 0.29 s, total: 9.32 s\nWall time: 13.70\n```\n",
    "created_at": "2008-05-16T04:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22140",
    "user": "was"
}
```

REPORT:

I'm using OS X 10.5.1 with GCC gcc version 4.0.1 (Apple Inc. build 5465) on my os x core 2 duo laptop.   After using your updated spkg (libm4ri-20080514.p0) and latest posted patch
I get even more memory errors!:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: m4ri
sage: A = random_matrix(GF(2),10^4,10^4)
sage: B = random_matrix(GF(2),10^4,10^4)
sage: time C = A._multiply_strassen(B,cutoff=3200)
sage: sage: A = random_matrix(GF(2),10^4,10^4)
sage: sage: B = random_matrix(GF(2),10^4,10^4)
sage: sage: time C = A._multiply_strassen(B,cutoff=3200)
sage.bin(58961) malloc: *** error for object 0xbaba010: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
sage.bin(58961) malloc: *** error for object 0x78f3610: Non-aligned pointer being freed (2)
*** set a breakpoint in malloc_error_break to debug
thousands more
CPU times: user 9.03 s, sys: 0.29 s, total: 9.32 s
Wall time: 13.70
```




---

archive/issue_comments_022141.json:
```json
{
    "body": "Replying to [comment:4 was]:\n> REPORT:\n> \n> I'm using OS X 10.5.1 with GCC gcc version 4.0.1 (Apple Inc. build 5465) on my os x core 2 duo laptop.   After using your updated spkg (libm4ri-20080514.p0) and latest posted patch\n> I get even more memory errors!:\n\nIf the above is not a typo then you are still using 200805**14** which was never fixed. The bug is supposed to be fixed in 200805**15**.",
    "created_at": "2008-05-16T08:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22141",
    "user": "malb"
}
```

Replying to [comment:4 was]:
> REPORT:
> 
> I'm using OS X 10.5.1 with GCC gcc version 4.0.1 (Apple Inc. build 5465) on my os x core 2 duo laptop.   After using your updated spkg (libm4ri-20080514.p0) and latest posted patch
> I get even more memory errors!:

If the above is not a typo then you are still using 200805**14** which was never fixed. The bug is supposed to be fixed in 200805**15**.



---

archive/issue_comments_022142.json:
```json
{
    "body": "Using \n\nhttp://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080515.p0.spkg\n\nworks fine!\n\n -- William",
    "created_at": "2008-05-16T13:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22142",
    "user": "was"
}
```

Using 

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080515.p0.spkg

works fine!

 -- William



---

archive/issue_comments_022143.json:
```json
{
    "body": "Upgraded the link to 200805**16** which fixes a bug discovered by the Gentoo QA:\n\n\n```\n * QA Notice: Package has poor programming practices which may compile\n *            fine but exhibit random runtime failures.\n * src/misc.c:121: warning: implicit declaration of function '_mm_free'\n```\n\n\nand was brought to my attention by Francois Bissey.",
    "created_at": "2008-05-16T14:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22143",
    "user": "malb"
}
```

Upgraded the link to 200805**16** which fixes a bug discovered by the Gentoo QA:


```
 * QA Notice: Package has poor programming practices which may compile
 *            fine but exhibit random runtime failures.
 * src/misc.c:121: warning: implicit declaration of function '_mm_free'
```


and was brought to my attention by Francois Bissey.



---

archive/issue_comments_022144.json:
```json
{
    "body": "this patch has been applied the current m4ri.spkg and should also be applied to this spkg before it is merged",
    "created_at": "2008-05-19T05:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22144",
    "user": "mabshoff"
}
```

this patch has been applied the current m4ri.spkg and should also be applied to this spkg before it is merged



---

archive/issue_comments_022145.json:
```json
{
    "body": "Attachment [trac_3197_libm4ri-20071224.p2-spkg-install-64bit-osx.patch](tarball://root/attachments/some-uuid/ticket3204/trac_3197_libm4ri-20071224.p2-spkg-install-64bit-osx.patch) by malb created at 2008-05-21 21:28:47",
    "created_at": "2008-05-21T21:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22145",
    "user": "malb"
}
```

Attachment [trac_3197_libm4ri-20071224.p2-spkg-install-64bit-osx.patch](tarball://root/attachments/some-uuid/ticket3204/trac_3197_libm4ri-20071224.p2-spkg-install-64bit-osx.patch) by malb created at 2008-05-21 21:28:47



---

archive/issue_comments_022146.json:
```json
{
    "body": "* `libm4ri-20080521.p0.spkg` has the OSX 64-bit patch applied.",
    "created_at": "2008-05-21T21:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22146",
    "user": "malb"
}
```

* `libm4ri-20080521.p0.spkg` has the OSX 64-bit patch applied.



---

archive/issue_comments_022147.json:
```json
{
    "body": "Use `new_m4ri_2.patch` instead of `new_m4ri.patch`.",
    "created_at": "2008-05-21T21:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22147",
    "user": "malb"
}
```

Use `new_m4ri_2.patch` instead of `new_m4ri.patch`.



---

archive/issue_comments_022148.json:
```json
{
    "body": "silly little script to check the results against Magma for a small range of matrices",
    "created_at": "2008-05-28T12:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22148",
    "user": "malb"
}
```

silly little script to check the results against Magma for a small range of matrices



---

archive/issue_comments_022149.json:
```json
{
    "body": "Attachment [m4ri_test.py](tarball://root/attachments/some-uuid/ticket3204/m4ri_test.py) by malb created at 2008-05-28 12:33:58\n\nThe SPKG + patch passes the test in `m4ri_test.py` in addition to the Sage doctests and the M4RI tests.",
    "created_at": "2008-05-28T12:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22149",
    "user": "malb"
}
```

Attachment [m4ri_test.py](tarball://root/attachments/some-uuid/ticket3204/m4ri_test.py) by malb created at 2008-05-28 12:33:58

The SPKG + patch passes the test in `m4ri_test.py` in addition to the Sage doctests and the M4RI tests.



---

archive/issue_comments_022150.json:
```json
{
    "body": "Attachment [new_m4ri_corner_cases.patch](tarball://root/attachments/some-uuid/ticket3204/new_m4ri_corner_cases.patch) by malb created at 2008-05-28 16:33:43",
    "created_at": "2008-05-28T16:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22150",
    "user": "malb"
}
```

Attachment [new_m4ri_corner_cases.patch](tarball://root/attachments/some-uuid/ticket3204/new_m4ri_corner_cases.patch) by malb created at 2008-05-28 16:33:43



---

archive/issue_comments_022151.json:
```json
{
    "body": "The attached patch `new_m4ri_corner_cases.patch` should fix all zero number of rows / zero number of columns problems.",
    "created_at": "2008-05-28T16:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22151",
    "user": "malb"
}
```

The attached patch `new_m4ri_corner_cases.patch` should fix all zero number of rows / zero number of columns problems.



---

archive/issue_comments_022152.json:
```json
{
    "body": "Positive review for new_m4ri.patch and new_m4ri_corner_cases.patch as well as the spkg. The patches looks good, all the issues uncovered regarding degenerated matrices were addressed and doctested in new_m4ri_corner_cases.patch. Positive review! Really nice work malb!\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T19:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22152",
    "user": "mabshoff"
}
```

Positive review for new_m4ri.patch and new_m4ri_corner_cases.patch as well as the spkg. The patches looks good, all the issues uncovered regarding degenerated matrices were addressed and doctested in new_m4ri_corner_cases.patch. Positive review! Really nice work malb!

Cheers,

Michael



---

archive/issue_comments_022153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-28T19:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22153",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022154.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-28T19:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3204#issuecomment-22154",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0
