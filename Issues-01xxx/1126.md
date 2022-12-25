# Issue 1126: [with spkg] building of fplll is broken

archive/issues_001126.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\n> \n> ***\n> x86_64-Linux\n> ***\n> While compiling libfplll-2.1-20071024, I get\n> \n> g++ -shared -nostdlib /usr/lib/../lib64/crti.o\n> /usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/crtbeginS.o\n>  .libs/fplll.o  -Wl,--rpath\n> -Wl,/usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64 -Wl,--rpath\n> -Wl,/usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64 -lmpfr -lgmp\n> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2\n> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/../../../../lib64\n> -L/lib/../lib64 -L/usr/lib/../lib64\n> -L/home/kate/sage/sage-2.8.12-x86_64-Linux/local/lib\n> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/../../..\n> /usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64/libstdc++.so -lm -lc\n> -lgcc_s /usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/crtendS.o\n> /usr/lib/../lib64/crtn.o  -Wl,-soname -Wl,libfplll.so.0 -o\n> .libs/libfplll.so.0.0.0\n> /usr/bin/ld: /usr/lib/../lib64/libmpfr.a(exceptions.o): relocation\n> R_X86_64_32 against `a local symbol' can not be used when making a\n> shared object; recompile with -fPIC\n> /usr/lib/../lib64/libmpfr.a: could not read symbols: Bad value\n> \n> Why is Sage trying to use libmpfr.a out of /usr/lib?  Should it not be\n> using the version\n> in [sage]/local/lib?\n\nI agree.  Note that libfpll is a brand new package in Sage (it does very fast LLL reduction,\nso is quite important), but it hasn't been as widely tested as other components of Sage. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1126\n\n",
    "closed_at": "2007-11-18T06:19:30Z",
    "created_at": "2007-11-07T19:07:40Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "[with spkg] building of fplll is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1126",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

```
> 
> ***
> x86_64-Linux
> ***
> While compiling libfplll-2.1-20071024, I get
> 
> g++ -shared -nostdlib /usr/lib/../lib64/crti.o
> /usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/crtbeginS.o
>  .libs/fplll.o  -Wl,--rpath
> -Wl,/usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64 -Wl,--rpath
> -Wl,/usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64 -lmpfr -lgmp
> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2
> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/../../../../lib64
> -L/lib/../lib64 -L/usr/lib/../lib64
> -L/home/kate/sage/sage-2.8.12-x86_64-Linux/local/lib
> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/../../..
> /usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64/libstdc++.so -lm -lc
> -lgcc_s /usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/crtendS.o
> /usr/lib/../lib64/crtn.o  -Wl,-soname -Wl,libfplll.so.0 -o
> .libs/libfplll.so.0.0.0
> /usr/bin/ld: /usr/lib/../lib64/libmpfr.a(exceptions.o): relocation
> R_X86_64_32 against `a local symbol' can not be used when making a
> shared object; recompile with -fPIC
> /usr/lib/../lib64/libmpfr.a: could not read symbols: Bad value
> 
> Why is Sage trying to use libmpfr.a out of /usr/lib?  Should it not be
> using the version
> in [sage]/local/lib?

I agree.  Note that libfpll is a brand new package in Sage (it does very fast LLL reduction,
so is quite important), but it hasn't been as widely tested as other components of Sage. 
```

Issue created by migration from https://trac.sagemath.org/ticket/1126





---

archive/issue_comments_006780.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-07T23:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1126#issuecomment-6780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006781.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-11-07T23:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1126#issuecomment-6781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_006782.json:
```json
{
    "body": "For a potential solutions to this problem please try\n\nhttp://sage.math.washington.edu/home/mabshoff/libfplll-2.1-20071024.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-11-07T23:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1126#issuecomment-6782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For a potential solutions to this problem please try

http://sage.math.washington.edu/home/mabshoff/libfplll-2.1-20071024.p0.spkg

Cheers,

Michael



---

archive/issue_comments_006783.json:
```json
{
    "body": "Ok, got feedback from Kate: It works on her x86-64 box and also builds fine for me on sage.math.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-08T20:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1126#issuecomment-6783",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, got feedback from Kate: It works on her x86-64 box and also builds fine for me on sage.math.

Cheers,

Michael



---

archive/issue_events_003008.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-10T23:13:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1126#event-3008"
}
```



---

archive/issue_comments_006784.json:
```json
{
    "body": "I've uploaded a new spkg to\n\nhttp://sage.math.washington.edu/home/malb/pkgs/libfplll-2.1.3-20071117.spkg\n\nwhich contains a cleaner fix than the package linked above by mabshoff. We shouldn't touch `Makefile.am` of the upstream package with SAGE specific fixes and thus I added that flag to `spkg-install`.",
    "created_at": "2007-11-17T13:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1126#issuecomment-6784",
    "user": "https://github.com/malb"
}
```

I've uploaded a new spkg to

http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.1.3-20071117.spkg

which contains a cleaner fix than the package linked above by mabshoff. We shouldn't touch `Makefile.am` of the upstream package with SAGE specific fixes and thus I added that flag to `spkg-install`.



---

archive/issue_comments_006785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-18T06:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1126#issuecomment-6785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006786.json:
```json
{
    "body": "Merged in 2.8.13.alpha0.",
    "created_at": "2007-11-18T06:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1126#issuecomment-6786",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.alpha0.



---

archive/issue_events_003009.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-18T06:19:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1126",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1126#event-3009"
}
```
