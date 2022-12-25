# Issue 3787: [with spkg, positive review] make ATLAS use extended cpuid

archive/issues_003787.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  cwitty @JohnCremona\n\n```\n[7:14pm] cwitty: 1) My spiffy new Xeon-branded core 2 quad computer is\nvery slow at compiling ATLAS.\n[7:14pm] mabshoff: mhhh, how long?\n[7:15pm] cwitty: I think ATLAS doesn't support the extended cpuid.\n[7:15pm] cwitty: About 2 hours.\n[7:15pm] mabshoff: On an Itanium 2 with loads of memory it takes about\n3 hours with loads of cache.\n[7:15pm] mabshoff: Can you check the ARCH in the makefile?\n[7:16pm] cwitty: PIII64SSE3\n[7:17pm] mabshoff: Ok, then it is identified. We might not have tuning\ninfo.\n[7:18pm] mabshoff: Let me check in a little while, but the compile\ntime depends on the L2 size.\n[7:18pm] cwitty: Umm... Pentium 3?  I'm pretty sure it's not a pentium\n3.\n[7:18pm] mabshoff: Oops\n[7:18pm] mabshoff: Yeah, you are right.\n[7:18pm] mabshoff: ATLAS uses cpuid, not extended cpuid.\n[7:18pm] mabshoff: I am not sure if 3.8.2 fixes that, but I can patch\nit in case it does not.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3787\n\n",
    "closed_at": "2009-01-02T21:54:17Z",
    "created_at": "2008-08-07T03:02:05Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "[with spkg, positive review] make ATLAS use extended cpuid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_026869.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-07T03:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26869",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026870.json:
```json
{
    "body": "Clint just told me in an offlist email that he is tracking the problem at\n\n http://math-atlas.sourceforge.net/errata.html#cpuid\n\nThat and another issue will be fixed in ATLAS 3.9.2 out this weekend.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-08T19:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26870",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Clint just told me in an offlist email that he is tracking the problem at

 http://math-atlas.sourceforge.net/errata.html#cpuid

That and another issue will be fixed in ATLAS 3.9.2 out this weekend.

Cheers,

Michael



---

archive/issue_comments_026871.json:
```json
{
    "body": "And I figure it is better to quote the solution since the errata page tends to get updated quite a bit:\n\nATLAS configure mis-identifies your new system as an older system (eg., Core2-Xeon detected as PIII)\nIn the original x86 ISA, when using CPUID to detect family and model, we were advised to only add in the extended bits for certain base bits. Intel and AMD now say to always add them in, and have reused the base bits for newer architectures. This means that 3.8.x (which uses the original CPUID instructions) will sometimes detect a modern machine as some older machine (for instance my Xeon E5420 was detected as a Pentium III). To fix this, simply comment out lines 95 and 99 of ATLAS/src/backend/archinfo_x86.c. So, change line 95 from:\n\n   if (*family == 0xf || *family == 0) /* extended family is added in */\n\nto:\n\n/* if (*family == 0xf || *family == 0)*/ /* extended family is added in */\n\nand change line 99 from\n\n   if (*model == 0xf)                  /* extended model is concatenated */\n\nto:\n\n/* if (*model == 0xf)*/                /* extended model is concatenated */\n\nEssentially, all the Core2-based systems are treated the same by ATLAS. So, to get to use the architectural defaults on Core2-based XEONs, change line 297 from:\n\n      case 15:\n\nto:\n\n      case 15: ; case 23:\n[end quote]",
    "created_at": "2008-08-08T20:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_events_008691.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-30T17:29:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "milestone": "sage-3.1.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3787#event-8691"
}
```



---

archive/issue_comments_026872.json:
```json
{
    "body": "The latest errata is the following:\n\n```\nTo fix this, simply comment out lines 95 and 99 of ATLAS/CONFIG/src/backend\n/archinfo_x86.c. So, change line 95 from:\n\n   if (*family == 0xf || *family == 0) /* extended family is added in */\n\nto:\n\n/* if (*family == 0xf || *family == 0)*/ /* extended family is added in */\n\nand change line 99 from\n\n   if (*model == 0xf)                  /* extended model is concatenated */\n\nto:\n\n/* if (*model == 0xf)*/                /* extended model is concatenated */\n\nEssentially, all the Core2-based systems are treated the same by ATLAS. So, \nto get to use the architectural defaults on Core2-based XEONs, change line \n297 from:\n\n      case 15:\n\nto:\n\n      case 15: ; case 23:\n\nFinally, to enable better P4E identification, change line 313 from:\n\n      case 4:\n\nto:\n\n      case 4: ; case 6:\n```",
    "created_at": "2008-12-17T13:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_026873.json:
```json
{
    "body": "This will be resolved via #3785.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-17T14:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26873",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This will be resolved via #3785.

Cheers,

Michael



---

archive/issue_events_008692.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-17T14:16:13Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "milestone": "sage-3.1.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3787#event-8692"
}
```



---

archive/issue_events_008693.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-17T14:16:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3787#event-8693"
}
```



---

archive/issue_events_008694.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-02T05:56:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3787#event-8694"
}
```



---

archive/issue_events_008695.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-02T05:56:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "milestone": "sage-3.2.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3787#event-8695"
}
```



---

archive/issue_comments_026874.json:
```json
{
    "body": "This will be fixed via #3785. The spkg is also there.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T07:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26874",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This will be fixed via #3785. The spkg is also there.

Cheers,

Michael



---

archive/issue_comments_026875.json:
```json
{
    "body": "Positive review via #3785.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T21:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review via #3785.

Cheers,

Michael



---

archive/issue_events_008696.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-02T21:54:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3787#event-8696"
}
```



---

archive/issue_comments_026876.json:
```json
{
    "body": "Merged in Sage 3.2.3.final",
    "created_at": "2009-01-02T21:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.final



---

archive/issue_comments_026877.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-02T21:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3787#issuecomment-26877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
