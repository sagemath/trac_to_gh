# Issue 2260: Upgrade ATLAS to 3.8.1

archive/issues_002260.json:
```json
{
    "body": "Assignee: m abs\n\n\n```\nATLAS 3.8.1 has been released.  It fixes all the known bugs in 3.8.0.  There\nare also several other improvements, but probably the most important is that\nI have finally fixed the Level 1 timing, so that it doesn't die so much with\n\"unable to get timings within tolerance\" when you don't have architectural\ndefaults.\n\nThe ChangeLog entry is below.\n\nCheers,\nClint\nATLAS 3.8.1 released 02/21/08, Changes from 3.8.0:\n   * Fixed bug in slvtst that counted complex flops same as real\n   * Fixed bug causing wrong answer for row-major gemm C=A*A' or A'A \n   * Fixed bug in configure causing Pentium-M to be IDed as CoreDuo\n   * Fixed bug in tfc.c causing memory overwrite when too many samples taken\n   * Improved L1 BLAS timers so they work like the rest of the package, and\n     thus don't die all the time on tolerance failures\n   * Improved ATLAS/tune/blas/gemm/mmsearch.c:\n     - for x86, tried more registers, since smart compiler can reduce A & B\n       regs to 2 (and possibly even 1)\n     - Made it so search tries both load-C-at-top and load-C-at-bottom of\n       M loop.  Bottom is superior for error, and ATLAS originally defaulted\n       to load-C-at-top.\n   * Added configure support for new K10h platform from AMD, as well as\n     basic architectural defaults (no new kernels, just good search)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2260\n\n",
    "created_at": "2008-02-22T17:03:07Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Upgrade ATLAS to 3.8.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2260",
    "user": "mabshoff"
}
```
Assignee: m abs


```
ATLAS 3.8.1 has been released.  It fixes all the known bugs in 3.8.0.  There
are also several other improvements, but probably the most important is that
I have finally fixed the Level 1 timing, so that it doesn't die so much with
"unable to get timings within tolerance" when you don't have architectural
defaults.

The ChangeLog entry is below.

Cheers,
Clint
ATLAS 3.8.1 released 02/21/08, Changes from 3.8.0:
   * Fixed bug in slvtst that counted complex flops same as real
   * Fixed bug causing wrong answer for row-major gemm C=A*A' or A'A 
   * Fixed bug in configure causing Pentium-M to be IDed as CoreDuo
   * Fixed bug in tfc.c causing memory overwrite when too many samples taken
   * Improved L1 BLAS timers so they work like the rest of the package, and
     thus don't die all the time on tolerance failures
   * Improved ATLAS/tune/blas/gemm/mmsearch.c:
     - for x86, tried more registers, since smart compiler can reduce A & B
       regs to 2 (and possibly even 1)
     - Made it so search tries both load-C-at-top and load-C-at-bottom of
       M loop.  Bottom is superior for error, and ATLAS originally defaulted
       to load-C-at-top.
   * Added configure support for new K10h platform from AMD, as well as
     basic architectural defaults (no new kernels, just good search)
```


Issue created by migration from https://trac.sagemath.org/ticket/2260





---

archive/issue_comments_014960.json:
```json
{
    "body": "Changing assignee from m abs to mabshoff.",
    "created_at": "2008-02-22T17:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2260#issuecomment-14960",
    "user": "mabshoff"
}
```

Changing assignee from m abs to mabshoff.



---

archive/issue_comments_014961.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-22T18:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2260#issuecomment-14961",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014962.json:
```json
{
    "body": "While I am at it I should fix all open ATLAS tickets:\n\n* #1495\n* #1641\n* #1767\n* #2108\n\nCheers,\n\nMichael",
    "created_at": "2008-02-22T18:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2260#issuecomment-14962",
    "user": "mabshoff"
}
```

While I am at it I should fix all open ATLAS tickets:

* #1495
* #1641
* #1767
* #2108

Cheers,

Michael



---

archive/issue_comments_014963.json:
```json
{
    "body": "Power throttling checking was disabled as per irc discussion, and after testing from me, positive review.",
    "created_at": "2008-03-20T10:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2260#issuecomment-14963",
    "user": "gfurnish"
}
```

Power throttling checking was disabled as per irc discussion, and after testing from me, positive review.



---

archive/issue_comments_014964.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/SPKG/atlas-3.8.1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T10:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2260#issuecomment-14964",
    "user": "mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/SPKG/atlas-3.8.1.spkg

Cheers,

Michael



---

archive/issue_comments_014965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T10:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2260#issuecomment-14965",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014966.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-20T10:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2260#issuecomment-14966",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0
