# Issue 3380: Fix large performance regression in ATLAS 3.8.0 and 3.8.1

archive/issues_003380.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nThere is a performance bug that causes a fairly large performance drop on\nall architectures.  This bug is present in both ATLAS 3.8.0 and 3.8.1.\nThe explanation and fix is available at:\n   http://math-atlas.sourceforge.net/errata.html#JITcpBug\n\nRegards,\nClint\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3380\n\n",
    "created_at": "2008-06-06T23:05:43Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "Fix large performance regression in ATLAS 3.8.0 and 3.8.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3380",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
There is a performance bug that causes a fairly large performance drop on
all architectures.  This bug is present in both ATLAS 3.8.0 and 3.8.1.
The explanation and fix is available at:
   http://math-atlas.sourceforge.net/errata.html#JITcpBug

Regards,
Clint
```


Issue created by migration from https://trac.sagemath.org/ticket/3380





---

archive/issue_comments_023666.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-06T23:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3380#issuecomment-23666",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023667.json:
```json
{
    "body": "The errata says specifically:\n\n```\nBad GEMM call causes performance drop for all architectures\nA piece of duplicated code causes a special-case code to be used \nfor all GEMM problems, which reduces performance on all architectures \nand almost all problems. To fix, comment out (or delete) lines 191-194 \nof ATLAS/src/blas/gemm/ATL_gemmXX.c, which read:\n\n         {\n            mm2 = mm1;\n            mm1 = Mjoin(PATL,mmJITcp);\n         }\n\n(notice these 4 lines are a duplicate of the for lines above. \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-06-06T23:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3380#issuecomment-23667",
    "user": "mabshoff"
}
```

The errata says specifically:

```
Bad GEMM call causes performance drop for all architectures
A piece of duplicated code causes a special-case code to be used 
for all GEMM problems, which reduces performance on all architectures 
and almost all problems. To fix, comment out (or delete) lines 191-194 
of ATLAS/src/blas/gemm/ATL_gemmXX.c, which read:

         {
            mm2 = mm1;
            mm1 = Mjoin(PATL,mmJITcp);
         }

(notice these 4 lines are a duplicate of the for lines above. 
```


Cheers,

Michael



---

archive/issue_comments_023668.json:
```json
{
    "body": "The new spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha1/atlas-3.8.1.p2.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-06-27T00:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3380#issuecomment-23668",
    "user": "mabshoff"
}
```

The new spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha1/atlas-3.8.1.p2.spkg

Cheers,

Michael



---

archive/issue_comments_023669.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-27T03:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3380#issuecomment-23669",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_023670.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-27T03:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3380#issuecomment-23670",
    "user": "mabshoff"
}
```

Resolution: fixed
