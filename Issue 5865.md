# Issue 5865: Add SAGE_SIMD_FLAG="SSE2" README.txt

archive/issues_005865.json:
```json
{
    "body": "Assignee: tba\n\nAdd some documentation to README.txt that explains the \n\n\n```\nexport SAGE_SIMD_FLAG=\"SSE2\"\n```\n\n\nflag, which makes it so one can build SAGE with ATLAS without sse3 optimizations.  This is slower but works on way more machines.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5865\n\n",
    "created_at": "2009-04-23T06:38:41Z",
    "labels": [
        "documentation",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add SAGE_SIMD_FLAG=\"SSE2\" README.txt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5865",
    "user": "@williamstein"
}
```
Assignee: tba

Add some documentation to README.txt that explains the 


```
export SAGE_SIMD_FLAG="SSE2"
```


flag, which makes it so one can build SAGE with ATLAS without sse3 optimizations.  This is slower but works on way more machines.

Issue created by migration from https://trac.sagemath.org/ticket/5865





---

archive/issue_comments_046333.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2009-04-24T11:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5865#issuecomment-46333",
    "user": "mabshoff"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_046334.json:
```json
{
    "body": "Oops, it is **SAGE_SIMD_MODE** - not sure how this confusion arose.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T11:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5865#issuecomment-46334",
    "user": "mabshoff"
}
```

Oops, it is **SAGE_SIMD_MODE** - not sure how this confusion arose.

Cheers,

Michael



---

archive/issue_comments_046335.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-06-02T21:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5865#issuecomment-46335",
    "user": "@williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_046336.json:
```json
{
    "body": "SAGE_SIMD_MODE is deprecated.",
    "created_at": "2009-06-02T21:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5865#issuecomment-46336",
    "user": "@williamstein"
}
```

SAGE_SIMD_MODE is deprecated.
