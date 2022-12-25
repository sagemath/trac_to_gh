# Issue 475: check for SAGE_DEBUG flag on build to include symbols

archive/issues_000475.json:
```json
{
    "body": "Assignee: @williamstein\n\nPackages should check for a flag (i.e. SAGE_DEBUG) on build. If this is set, options suitable for debugging should be used. i.e. CFLAGS=\"-g\", no optimizations,  --without-pymalloc in Python (for valgrind)\n\nIssue created by migration from https://trac.sagemath.org/ticket/475\n\n",
    "created_at": "2007-08-21T14:10:23Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "check for SAGE_DEBUG flag on build to include symbols",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/475",
    "user": "https://github.com/burcin"
}
```
Assignee: @williamstein

Packages should check for a flag (i.e. SAGE_DEBUG) on build. If this is set, options suitable for debugging should be used. i.e. CFLAGS="-g", no optimizations,  --without-pymalloc in Python (for valgrind)

Issue created by migration from https://trac.sagemath.org/ticket/475





---

archive/issue_comments_002363.json:
```json
{
    "body": "Changing keywords from \"\" to \"package audit\".",
    "created_at": "2007-11-20T14:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/475#issuecomment-2363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing keywords from "" to "package audit".



---

archive/issue_comments_002364.json:
```json
{
    "body": "-g in CFLAGS is, IMHO, a different level than turning off all optimization and Python memory management (the latter actually have a significant speed impact, the former none).",
    "created_at": "2009-07-28T12:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/475#issuecomment-2364",
    "user": "https://github.com/robertwb"
}
```

-g in CFLAGS is, IMHO, a different level than turning off all optimization and Python memory management (the latter actually have a significant speed impact, the former none).
