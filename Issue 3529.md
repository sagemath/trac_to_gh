# Issue 3529: ATLAS.spkg: reapply the PowerPC detection fix

archive/issues_003529.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nMaybe I advanced a little in this problem. I found that your patch \nATLAS-3.8.1-ppc-g4-7447-detect-fix.patch is not applied in sage. After \napplying this patch, it can detect architecture PPCG4. Here are the \nresult with atlas-3.8.1.p2 in 3.0.4.alpha1:\n---------------------------------------\nOS configured as Linux (1)\n\nAssembly configured as GAS_PPC (4)\n\nBad VECFLAG value=0, ierr=0, ln2='VECFLAG=0\n'\n\nVector ISA Extension configured as   (0,0)\n\nArchitecture configured as  PPCG4 (4)\n\nBad CPU MHZ value=0, ierr=0, ln2='CPU MHZ=0\n'\n\nClock rate configured as 0Mhz\n-----------------------------------\n\nand\n\n-----------------------------\nreal    62m10.407s\nuser    47m47.740s\nsys     4m38.025s\nSuccessfully installed atlas-3.8.1.p2\n-------------------------------\n\nFor comparison (atlas-3.8.1p1 in sage-3.0.3) I need long time:\n-------------------------\nreal    450m35.791s\nuser    371m58.504s\nsys     16m33.417s\nSuccessfully installed atlas-3.8.1.p1\n-----------------------------------------\n\nThanks\nBin \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3529\n\n",
    "created_at": "2008-06-28T10:07:49Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "ATLAS.spkg: reapply the PowerPC detection fix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3529",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
Maybe I advanced a little in this problem. I found that your patch 
ATLAS-3.8.1-ppc-g4-7447-detect-fix.patch is not applied in sage. After 
applying this patch, it can detect architecture PPCG4. Here are the 
result with atlas-3.8.1.p2 in 3.0.4.alpha1:
---------------------------------------
OS configured as Linux (1)

Assembly configured as GAS_PPC (4)

Bad VECFLAG value=0, ierr=0, ln2='VECFLAG=0
'

Vector ISA Extension configured as   (0,0)

Architecture configured as  PPCG4 (4)

Bad CPU MHZ value=0, ierr=0, ln2='CPU MHZ=0
'

Clock rate configured as 0Mhz
-----------------------------------

and

-----------------------------
real    62m10.407s
user    47m47.740s
sys     4m38.025s
Successfully installed atlas-3.8.1.p2
-------------------------------

For comparison (atlas-3.8.1p1 in sage-3.0.3) I need long time:
-------------------------
real    450m35.791s
user    371m58.504s
sys     16m33.417s
Successfully installed atlas-3.8.1.p1
-----------------------------------------

Thanks
Bin 
```


Issue created by migration from https://trac.sagemath.org/ticket/3529





---

archive/issue_comments_024842.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-28T10:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3529#issuecomment-24842",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024843.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/atlas-3.8.1.p3.spkg\n\nhas a patched archinfo.c which now properly detects the G4 in question.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T05:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3529#issuecomment-24843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/atlas-3.8.1.p3.spkg

has a patched archinfo.c which now properly detects the G4 in question.

Cheers,

Michael



---

archive/issue_comments_024844.json:
```json
{
    "body": "positive review as explained in irc.",
    "created_at": "2008-07-07T05:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3529#issuecomment-24844",
    "user": "https://github.com/williamstein"
}
```

positive review as explained in irc.



---

archive/issue_events_003748.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-07T05:46:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3529",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3529#event-3748"
}
```



---

archive/issue_comments_024845.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-07T05:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3529#issuecomment-24845",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_024846.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T05:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3529#issuecomment-24846",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
