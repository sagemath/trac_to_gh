# Issue 7182: HP-UX failure of gfan-0.3.p4 but easier to ensure we have GNU make.

archive/issues_007182.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: HP-UX Solaris make\n\ngfan will not build on my HP-UX box, as the 'make' program does not like a 'makefile'. Perhaps the gfan developer would like to fix this, but from the point of view of Sage, it is easier we ensure that 'make' is GNU make (see #7181), since on Solaris we find Sun's 'make' has no chance at all of building Sage. \n\n\n```\nExtracting package /home/drkirkby/sage-4.1.2.rc0/spkg/standard/gfan-0.3.p4.spkg ...\n-rw-r--r--   1 drkirkby   users       129974 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/gfan-0.3.p4.spkg\nFinished extraction\n****************************************************\nHost system\nuname -a:\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: hppa1.1-hp-hpux11.11\nConfigured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11\nThread model: posix\ngcc version 4.4.0 (GCC)\n****************************************************\nMake: Must be a separator on rules line 14.  Stop.\nError building gfan\n\nreal    0m0.050s\nuser    0m0.030s\nsys     0m0.020s\nsage: An error occurred while installing gfan-0.3.p4\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7182\n\n",
    "created_at": "2009-10-10T09:35:18Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "HP-UX failure of gfan-0.3.p4 but easier to ensure we have GNU make.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7182",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Keywords: HP-UX Solaris make

gfan will not build on my HP-UX box, as the 'make' program does not like a 'makefile'. Perhaps the gfan developer would like to fix this, but from the point of view of Sage, it is easier we ensure that 'make' is GNU make (see #7181), since on Solaris we find Sun's 'make' has no chance at all of building Sage. 


```
Extracting package /home/drkirkby/sage-4.1.2.rc0/spkg/standard/gfan-0.3.p4.spkg ...
-rw-r--r--   1 drkirkby   users       129974 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/gfan-0.3.p4.spkg
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.4.0 (GCC)
****************************************************
Make: Must be a separator on rules line 14.  Stop.
Error building gfan

real    0m0.050s
user    0m0.030s
sys     0m0.020s
sage: An error occurred while installing gfan-0.3.p4

```


Issue created by migration from https://trac.sagemath.org/ticket/7182





---

archive/issue_comments_059369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-20T06:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7182#issuecomment-59369",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059370.json:
```json
{
    "body": "Fixed by #7352",
    "created_at": "2009-11-20T06:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7182#issuecomment-59370",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #7352



---

archive/issue_events_007401.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-20T06:22:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7182",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7182#event-7401"
}
```
