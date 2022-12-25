# Issue 5202: [with spkg, needs review] update MPFR to 2.4.0 (latest upstream)

archive/issues_005202.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @zimmermann6\n\nThe spkg at\n\n http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha6/mpfr-2.4.0.spkg\n\nupdates the mpfr.spkg to latest upstream. For now the test suite is invoked automatically. It passes on\n\nSkyNet:\n\n* eno (x86_64, FC9)\n* mark (Sparc, Solaris)\n* fulvia (x86, Solaris)\n* cicero (x86, FC9)\n* menas (x86_64, OpenSUSE 10.3)\n* iras (Itanium, SLES 10)\n* cleo (Itanium, RHEL 5.2)\n* varro (PPC, OSX 10.4)\n\nMisc machines:\n\n* bsd (x86, OSX 10.5)\n* sage.math (x86_64, Ubuntu LTS 8.04)\n* sprocketer (x86-64, OSX 10.5)\n\nwith MPIR-0.9.rc3, which will be updated via a separate ticket.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5202\n\n",
    "created_at": "2009-02-08T01:08:28Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with spkg, needs review] update MPFR to 2.4.0 (latest upstream)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @zimmermann6

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha6/mpfr-2.4.0.spkg

updates the mpfr.spkg to latest upstream. For now the test suite is invoked automatically. It passes on

SkyNet:

* eno (x86_64, FC9)
* mark (Sparc, Solaris)
* fulvia (x86, Solaris)
* cicero (x86, FC9)
* menas (x86_64, OpenSUSE 10.3)
* iras (Itanium, SLES 10)
* cleo (Itanium, RHEL 5.2)
* varro (PPC, OSX 10.4)

Misc machines:

* bsd (x86, OSX 10.5)
* sage.math (x86_64, Ubuntu LTS 8.04)
* sprocketer (x86-64, OSX 10.5)

with MPIR-0.9.rc3, which will be updated via a separate ticket.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5202





---

archive/issue_comments_039784.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-08T01:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5202#issuecomment-39784",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039785.json:
```json
{
    "body": "Paul,\n\nI can supply you with the config.guess output of all the machines above in case you want it for the MPFR website. I can also test on MIPS64/Linux.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T01:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5202#issuecomment-39785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Paul,

I can supply you with the config.guess output of all the machines above in case you want it for the MPFR website. I can also test on MIPS64/Linux.

Cheers,

Michael



---

archive/issue_comments_039786.json:
```json
{
    "body": "Looks good.  Passes all tests for me.",
    "created_at": "2009-02-08T01:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5202#issuecomment-39786",
    "user": "https://github.com/mwhansen"
}
```

Looks good.  Passes all tests for me.



---

archive/issue_comments_039787.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-08T01:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5202#issuecomment-39787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039788.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T01:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5202#issuecomment-39788",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_events_005457.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-08T01:58:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5202",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5202#event-5457"
}
```



---

archive/issue_comments_039789.json:
```json
{
    "body": "> I can supply you with the config.guess output of all the machines above in case you want it for the MPFR website. I can also test on MIPS64/Linux.\n\nyes please supply it for configurations not already listed for mpfr-2.4.0.\n\nPaul",
    "created_at": "2009-02-08T09:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5202#issuecomment-39789",
    "user": "https://github.com/zimmermann6"
}
```

> I can supply you with the config.guess output of all the machines above in case you want it for the MPFR website. I can also test on MIPS64/Linux.

yes please supply it for configurations not already listed for mpfr-2.4.0.

Paul
