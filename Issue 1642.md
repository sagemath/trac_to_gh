# Issue 1642: Fortran.spkg: search for common Fortran compiles if no binary is present

archive/issues_001642.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe do not have binaries on less common platforms. If SAGE_FORTRAN isn't set we just fail, but we should check for common Fortran compilers and set them then instead of failing. Preference should be:\n* gfotran\n* g95\n* g77\n* f77 - on BSD the g77 is commonly called f77\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1642\n\n",
    "created_at": "2007-12-30T18:50:22Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Fortran.spkg: search for common Fortran compiles if no binary is present",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1642",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

We do not have binaries on less common platforms. If SAGE_FORTRAN isn't set we just fail, but we should check for common Fortran compilers and set them then instead of failing. Preference should be:
* gfotran
* g95
* g77
* f77 - on BSD the g77 is commonly called f77

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1642





---

archive/issue_comments_010419.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-31T10:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1642#issuecomment-10419",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010420.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T06:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1642#issuecomment-10420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010421.json:
```json
{
    "body": "This has been fixed by William Stein a while ago.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T06:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1642#issuecomment-10421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed by William Stein a while ago.

Cheers,

Michael
