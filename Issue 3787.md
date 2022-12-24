# Issue 3787: make ATLAS use extended cpuid

archive/issues_003787.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  cwitty @JohnCremona\n\n\n```\n[7:14pm] cwitty: 1) My spiffy new Xeon-branded core 2 quad computer is\nvery slow at compiling ATLAS.\n[7:14pm] mabshoff: mhhh, how long?\n[7:15pm] cwitty: I think ATLAS doesn't support the extended cpuid.\n[7:15pm] cwitty: About 2 hours.\n[7:15pm] mabshoff: On an Itanium 2 with loads of memory it takes about\n3 hours with loads of cache.\n[7:15pm] mabshoff: Can you check the ARCH in the makefile?\n[7:16pm] cwitty: PIII64SSE3\n[7:17pm] mabshoff: Ok, then it is identified. We might not have tuning\ninfo.\n[7:18pm] mabshoff: Let me check in a little while, but the compile\ntime depends on the L2 size.\n[7:18pm] cwitty: Umm... Pentium 3?  I'm pretty sure it's not a pentium\n3.\n[7:18pm] mabshoff: Oops\n[7:18pm] mabshoff: Yeah, you are right.\n[7:18pm] mabshoff: ATLAS uses cpuid, not extended cpuid.\n[7:18pm] mabshoff: I am not sure if 3.8.2 fixes that, but I can patch\nit in case it does not.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3787\n\n",
    "created_at": "2008-08-07T03:02:05Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "make ATLAS use extended cpuid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3787",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  cwitty @JohnCremona


```
[7:14pm] cwitty: 1) My spiffy new Xeon-branded core 2 quad computer is
very slow at compiling ATLAS.
[7:14pm] mabshoff: mhhh, how long?
[7:15pm] cwitty: I think ATLAS doesn't support the extended cpuid.
[7:15pm] cwitty: About 2 hours.
[7:15pm] mabshoff: On an Itanium 2 with loads of memory it takes about
3 hours with loads of cache.
[7:15pm] mabshoff: Can you check the ARCH in the makefile?
[7:16pm] cwitty: PIII64SSE3
[7:17pm] mabshoff: Ok, then it is identified. We might not have tuning
info.
[7:18pm] mabshoff: Let me check in a little while, but the compile
time depends on the L2 size.
[7:18pm] cwitty: Umm... Pentium 3?  I'm pretty sure it's not a pentium
3.
[7:18pm] mabshoff: Oops
[7:18pm] mabshoff: Yeah, you are right.
[7:18pm] mabshoff: ATLAS uses cpuid, not extended cpuid.
[7:18pm] mabshoff: I am not sure if 3.8.2 fixes that, but I can patch
it in case it does not.
```


Issue created by migration from https://trac.sagemath.org/ticket/3787





---

archive/issue_comments_026927.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-07T03:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26927",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026928.json:
```json
{
    "body": "Clint just told me in an offlist email that he is tracking the problem at\n\n http://math-atlas.sourceforge.net/errata.html#cpuid\n\nThat and another issue will be fixed in ATLAS 3.9.2 out this weekend.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-08T19:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26928",
    "user": "mabshoff"
}
```

Clint just told me in an offlist email that he is tracking the problem at

 http://math-atlas.sourceforge.net/errata.html#cpuid

That and another issue will be fixed in ATLAS 3.9.2 out this weekend.

Cheers,

Michael



---

archive/issue_comments_026929.json:
```json
{
    "body": "And I figure it is better to quote the solution since the errata page tends to get updated quite a bit:\n\nATLAS configure mis-identifies your new system as an older system (eg., Core2-Xeon detected as PIII)\nIn the original x86 ISA, when using CPUID to detect family and model, we were advised to only add in the extended bits for certain base bits. Intel and AMD now say to always add them in, and have reused the base bits for newer architectures. This means that 3.8.x (which uses the original CPUID instructions) will sometimes detect a modern machine as some older machine (for instance my Xeon E5420 was detected as a Pentium III). To fix this, simply comment out lines 95 and 99 of ATLAS/src/backend/archinfo_x86.c. So, change line 95 from:\n\n   if (*family == 0xf || *family == 0) /* extended family is added in */\n\nto:\n\n/* if (*family == 0xf || *family == 0)*/ /* extended family is added in */\n\nand change line 99 from\n\n   if (*model == 0xf)                  /* extended model is concatenated */\n\nto:\n\n/* if (*model == 0xf)*/                /* extended model is concatenated */\n\nEssentially, all the Core2-based systems are treated the same by ATLAS. So, to get to use the architectural defaults on Core2-based XEONs, change line 297 from:\n\n      case 15:\n\nto:\n\n      case 15: ; case 23:\n[end quote]",
    "created_at": "2008-08-08T20:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26929",
    "user": "mabshoff"
}
```

And I figure it is better to quote the solution since the errata page tends to get updated quite a bit:

ATLAS configure mis-identifies your new system as an older system (eg., Core2-Xeon detected as PIII)
In the original x86 ISA, when using CPUID to detect family and model, we were advised to only add in the extended bits for certain base bits. Intel and AMD now say to always add them in, and have reused the base bits for newer architectures. This means that 3.8.x (which uses the original CPUID instructions) will sometimes detect a modern machine as some older machine (for instance my Xeon E5420 was detected as a Pentium III). To fix this, simply comment out lines 95 and 99 of ATLAS/src/backend/archinfo_x86.c. So, change line 95 from:

   if (*family == 0xf || *family == 0) /* extended family is added in */

to:

/* if (*family == 0xf || *family == 0)*/ /* extended family is added in */

and change line 99 from

   if (*model == 0xf)                  /* extended model is concatenated */

to:

/* if (*model == 0xf)*/                /* extended model is concatenated */

Essentially, all the Core2-based systems are treated the same by ATLAS. So, to get to use the architectural defaults on Core2-based XEONs, change line 297 from:

      case 15:

to:

      case 15: ; case 23:
[end quote]



---

archive/issue_comments_026930.json:
```json
{
    "body": "The latest errata is the following:\n\n```\nTo fix this, simply comment out lines 95 and 99 of ATLAS/CONFIG/src/backend\n/archinfo_x86.c. So, change line 95 from:\n\n   if (*family == 0xf || *family == 0) /* extended family is added in */\n\nto:\n\n/* if (*family == 0xf || *family == 0)*/ /* extended family is added in */\n\nand change line 99 from\n\n   if (*model == 0xf)                  /* extended model is concatenated */\n\nto:\n\n/* if (*model == 0xf)*/                /* extended model is concatenated */\n\nEssentially, all the Core2-based systems are treated the same by ATLAS. So, \nto get to use the architectural defaults on Core2-based XEONs, change line \n297 from:\n\n      case 15:\n\nto:\n\n      case 15: ; case 23:\n\nFinally, to enable better P4E identification, change line 313 from:\n\n      case 4:\n\nto:\n\n      case 4: ; case 6:\n```\n",
    "created_at": "2008-12-17T13:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26930",
    "user": "mabshoff"
}
```

The latest errata is the following:

```
To fix this, simply comment out lines 95 and 99 of ATLAS/CONFIG/src/backend
/archinfo_x86.c. So, change line 95 from:

   if (*family == 0xf || *family == 0) /* extended family is added in */

to:

/* if (*family == 0xf || *family == 0)*/ /* extended family is added in */

and change line 99 from

   if (*model == 0xf)                  /* extended model is concatenated */

to:

/* if (*model == 0xf)*/                /* extended model is concatenated */

Essentially, all the Core2-based systems are treated the same by ATLAS. So, 
to get to use the architectural defaults on Core2-based XEONs, change line 
297 from:

      case 15:

to:

      case 15: ; case 23:

Finally, to enable better P4E identification, change line 313 from:

      case 4:

to:

      case 4: ; case 6:
```




---

archive/issue_comments_026931.json:
```json
{
    "body": "This will be resolved via #3785.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T14:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26931",
    "user": "mabshoff"
}
```

This will be resolved via #3785.

Cheers,

Michael



---

archive/issue_comments_026932.json:
```json
{
    "body": "This will be fixed via #3785. The spkg is also there.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T07:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26932",
    "user": "mabshoff"
}
```

This will be fixed via #3785. The spkg is also there.

Cheers,

Michael



---

archive/issue_comments_026933.json:
```json
{
    "body": "Positive review via #3785.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T21:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26933",
    "user": "mabshoff"
}
```

Positive review via #3785.

Cheers,

Michael



---

archive/issue_comments_026934.json:
```json
{
    "body": "Merged in Sage 3.2.3.final",
    "created_at": "2009-01-02T21:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26934",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.final



---

archive/issue_comments_026935.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-02T21:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26935",
    "user": "mabshoff"
}
```

Resolution: fixed
