# Issue 2955: GFortran autodection on Linux/Itanium

archive/issues_002955.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe do not ship any Fortran compiler for Linux/Itanium. Since any reasonable distribution on Itanium ships GFortran automate detection for that special case. With this ticket, #2953 and 2954 Sage 3.0 should build out of the box on SageNet's RHEL 5 and SLES 10 Itanium test boxen.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2955\n\n",
    "created_at": "2008-04-19T04:03:42Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "GFortran autodection on Linux/Itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2955",
    "user": "mabshoff"
}
```
Assignee: mabshoff

We do not ship any Fortran compiler for Linux/Itanium. Since any reasonable distribution on Itanium ships GFortran automate detection for that special case. With this ticket, #2953 and 2954 Sage 3.0 should build out of the box on SageNet's RHEL 5 and SLES 10 Itanium test boxen.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2955





---

archive/issue_comments_020375.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-19T04:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20375",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020376.json:
```json
{
    "body": "#1642 does fix most of the problem already, but on some Itanium systems [RHEL 5 for example] there is no libgfortran.so, only a libgfortran.so.1.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T06:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20376",
    "user": "mabshoff"
}
```

#1642 does fix most of the problem already, but on some Itanium systems [RHEL 5 for example] there is no libgfortran.so, only a libgfortran.so.1.

Cheers,

Michael



---

archive/issue_comments_020377.json:
```json
{
    "body": "I added some more verbose output, check the arch flag for also i[345]86 [which like could cause bugs on some other systems, check for libgfortran.so[.1] relative to gfortran and link that lib into SAGE_LOCAL/lib. This makes the fortran.spkg work out of the box on RHEL 5/Itanium.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T10:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20377",
    "user": "mabshoff"
}
```

I added some more verbose output, check the arch flag for also i[345]86 [which like could cause bugs on some other systems, check for libgfortran.so[.1] relative to gfortran and link that lib into SAGE_LOCAL/lib. This makes the fortran.spkg work out of the box on RHEL 5/Itanium.

Cheers,

Michael



---

archive/issue_comments_020378.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/rc0/fortran-20071120.p4.spkg\n\nSorry wjp ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T10:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20378",
    "user": "mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/rc0/fortran-20071120.p4.spkg

Sorry wjp ;)

Cheers,

Michael



---

archive/issue_comments_020379.json:
```json
{
    "body": "Merged in Sage 3.0.rc0",
    "created_at": "2008-04-20T10:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20379",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.rc0



---

archive/issue_comments_020380.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-20T10:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2955#issuecomment-20380",
    "user": "mabshoff"
}
```

Resolution: fixed
