# Issue 680: Solaris 9: fix partition import problem

archive/issues_000680.json:
```json
{
    "body": "Assignee: mabshoff\n\nAs a workaround on Solaris 9 we define:\n\n```\n#if defined(__sun)\nextern long double fabsl (long double);\nextern long double sinl (long double);\nextern long double cosl (long double);\nextern long double sqrtl (long double);\nextern long double coshl (long double);\nextern long double sinhl (long double);\n#endif\n```\n\nProblem is that this file is C++, so those externs need to be defined as extern \"C\". Otherwise the linker mangles the function names and consequently Sage doesn't start complaining about missing symbols.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/680\n\n",
    "created_at": "2007-09-17T09:09:12Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "Solaris 9: fix partition import problem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/680",
    "user": "mabshoff"
}
```
Assignee: mabshoff

As a workaround on Solaris 9 we define:

```
#if defined(__sun)
extern long double fabsl (long double);
extern long double sinl (long double);
extern long double cosl (long double);
extern long double sqrtl (long double);
extern long double coshl (long double);
extern long double sinhl (long double);
#endif
```

Problem is that this file is C++, so those externs need to be defined as extern "C". Otherwise the linker mangles the function names and consequently Sage doesn't start complaining about missing symbols.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/680





---

archive/issue_comments_003530.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-17T09:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/680#issuecomment-3530",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003531.json:
```json
{
    "body": "A patch for this problem can be found at \n\nhttp://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4-fix-partition.so-load-problem-on-Solaris9.patch\n\nCheers,\n\nMichael",
    "created_at": "2007-09-18T20:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/680#issuecomment-3531",
    "user": "mabshoff"
}
```

A patch for this problem can be found at 

http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/Sage-2.8.4-fix-partition.so-load-problem-on-Solaris9.patch

Cheers,

Michael



---

archive/issue_comments_003532.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T00:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/680#issuecomment-3532",
    "user": "@williamstein"
}
```

Resolution: fixed
