# Issue 2955: GFortran autodection on Linux/Itanium

archive/issues_002955.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe do not ship any Fortran compiler for Linux/Itanium. Since any reasonable distribution on Itanium ships GFortran automate detection for that special case. With this ticket, #2953 and 2954 Sage 3.0 should build out of the box on SageNet's RHEL 5 and SLES 10 Itanium test boxen.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2955\n\n",
    "created_at": "2008-04-19T04:03:42Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "GFortran autodection on Linux/Itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2955",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

We do not ship any Fortran compiler for Linux/Itanium. Since any reasonable distribution on Itanium ships GFortran automate detection for that special case. With this ticket, #2953 and 2954 Sage 3.0 should build out of the box on SageNet's RHEL 5 and SLES 10 Itanium test boxen.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2955





---

archive/issue_comments_020332.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-19T04:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020333.json:
```json
{
    "body": "#1642 does fix most of the problem already, but on some Itanium systems [RHEL 5 for example] there is no libgfortran.so, only a libgfortran.so.1.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T06:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

#1642 does fix most of the problem already, but on some Itanium systems [RHEL 5 for example] there is no libgfortran.so, only a libgfortran.so.1.

Cheers,

Michael



---

archive/issue_comments_020334.json:
```json
{
    "body": "I added some more verbose output, check the arch flag for also i[345]86 [which like could cause bugs on some other systems, check for libgfortran.so[.1] relative to gfortran and link that lib into SAGE_LOCAL/lib. This makes the fortran.spkg work out of the box on RHEL 5/Itanium.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T10:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20334",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I added some more verbose output, check the arch flag for also i[345]86 [which like could cause bugs on some other systems, check for libgfortran.so[.1] relative to gfortran and link that lib into SAGE_LOCAL/lib. This makes the fortran.spkg work out of the box on RHEL 5/Itanium.

Cheers,

Michael



---

archive/issue_comments_020335.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/rc0/fortran-20071120.p4.spkg\n\nSorry wjp ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T10:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/rc0/fortran-20071120.p4.spkg

Sorry wjp ;)

Cheers,

Michael



---

archive/issue_comments_020336.json:
```json
{
    "body": "Merged in Sage 3.0.rc0",
    "created_at": "2008-04-20T10:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20336",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.rc0



---

archive/issue_events_006753.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-20T10:51:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2955#event-6753"
}
```



---

archive/issue_comments_020337.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T10:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20337",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
