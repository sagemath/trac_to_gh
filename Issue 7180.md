# Issue 7180: HP-UX cddlib-094f checks for gmp library, then igores the fact it can't find it.

archive/issues_007180.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @fchapoton\n\nKeywords: HP-UX gmp mpir\n\nMPIR would not build on my HP-UX box, so needless to say programs wanting gmp will not work. However, cddlib-094f  checks for gmp, then ignores the fact it can't find it. It should exit with a clear error message then, not carry on. \n\nA developer can have access to the HP-UX box, but this is not really necessay to fix this. Just email me with your preffered user name if you want to have an account \n\n```\n...\n-rw-r--r--   1 drkirkby   users       266542 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/cddlib-094f.spkg\nFinished extraction\n****************************************************\nHost system\nuname -a:\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: hppa1.1-hp-hpux11.11\nConfigured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11\nThread model: posix\ngcc version 4.4.0 (GCC)\n****************************************************\nchecking for a BSD-compatible install... ./install-sh -c\nchecking whether build environment is sane... yes\nchecking for gawk... no\nchecking for mawk... no\nchecking for nawk... no\nchecking for awk... awk\nchecking whether make sets $(MAKE)... yes\nchecking for gcc... gcc\nchecking for C compiler default output file name... a.out\nchecking whether the C compiler works... yes\nchecking whether we are cross compiling... no\nchecking for suffix of executables...\nchecking for suffix of object files... o\nchecking whether we are using the GNU C compiler... yes\nchecking whether gcc accepts -g... yes\nchecking for gcc option to accept ISO C89... none needed\nchecking for style of include used by make... GNU\nchecking dependency style of gcc... gcc3\nchecking for a BSD-compatible install... ./install-sh -c\nchecking for ranlib... ranlib\nchecking for main in -lgmp... no\nchecking how to run the C preprocessor... gcc -E\nchecking for grep that handles long lines and -e... /usr/bin/grep\nchecking for egrep... /usr/bin/grep -E\nchecking for ANSI C header files... yes\nchecking for an ANSI C-conforming const... yes\nconfigure: creating ./config.status\nconfig.status: creating lib-src/Makefile\nconfig.status: WARNING:  lib-src/Makefile.in seems to ignore the --datarootdir setting\nconfig.status: creating src/Makefile\nconfig.status: WARNING:  src/Makefile.in seems to ignore the --datarootdir setting\nconfig.status: creating lib-src-gmp/Makefile\nconfig.status: WARNING:  lib-src-gmp/Makefile.in seems to ignore the --datarootdir setting\nconfig.status: creating src-gmp/Makefile\nconfig.status: WARNING:  src-gmp/Makefile.in seems to ignore the --datarootdir setting\nconfig.status: creating Makefile\nconfig.status: WARNING:  Makefile.in seems to ignore the --datarootdir setting\nconfig.status: executing depfiles commands\nMake: line 409: syntax error.  Stop.\nError building cddlib\n\nreal    0m8.255s\nuser    0m4.260s\nsys     0m2.460s\nsage: An error occurred while installing cddlib-094f\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7180\n\n",
    "closed_at": "2020-06-24T06:28:42Z",
    "created_at": "2009-10-10T09:24:44Z",
    "labels": [
        "component: porting: aix or hp-ux",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "HP-UX cddlib-094f checks for gmp library, then igores the fact it can't find it.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7180",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @fchapoton

Keywords: HP-UX gmp mpir

MPIR would not build on my HP-UX box, so needless to say programs wanting gmp will not work. However, cddlib-094f  checks for gmp, then ignores the fact it can't find it. It should exit with a clear error message then, not carry on. 

A developer can have access to the HP-UX box, but this is not really necessay to fix this. Just email me with your preffered user name if you want to have an account 

```
...
-rw-r--r--   1 drkirkby   users       266542 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/cddlib-094f.spkg
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
checking for a BSD-compatible install... ./install-sh -c
checking whether build environment is sane... yes
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking for gcc... gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking for a BSD-compatible install... ./install-sh -c
checking for ranlib... ranlib
checking for main in -lgmp... no
checking how to run the C preprocessor... gcc -E
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for ANSI C header files... yes
checking for an ANSI C-conforming const... yes
configure: creating ./config.status
config.status: creating lib-src/Makefile
config.status: WARNING:  lib-src/Makefile.in seems to ignore the --datarootdir setting
config.status: creating src/Makefile
config.status: WARNING:  src/Makefile.in seems to ignore the --datarootdir setting
config.status: creating lib-src-gmp/Makefile
config.status: WARNING:  lib-src-gmp/Makefile.in seems to ignore the --datarootdir setting
config.status: creating src-gmp/Makefile
config.status: WARNING:  src-gmp/Makefile.in seems to ignore the --datarootdir setting
config.status: creating Makefile
config.status: WARNING:  Makefile.in seems to ignore the --datarootdir setting
config.status: executing depfiles commands
Make: line 409: syntax error.  Stop.
Error building cddlib

real    0m8.255s
user    0m4.260s
sys     0m2.460s
sage: An error occurred while installing cddlib-094f

```

Issue created by migration from https://trac.sagemath.org/ticket/7180





---

archive/issue_comments_059361.json:
```json
{
    "body": "I'm not sure who to report this too, but it does need reporting.",
    "created_at": "2009-11-27T13:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7180#issuecomment-59361",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm not sure who to report this too, but it does need reporting.



---

archive/issue_events_016990.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16990"
}
```



---

archive/issue_events_016991.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16991"
}
```



---

archive/issue_events_016992.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16992"
}
```



---

archive/issue_events_016993.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16993"
}
```



---

archive/issue_events_016994.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16994"
}
```



---

archive/issue_events_016995.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16995"
}
```



---

archive/issue_events_016996.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16996"
}
```



---

archive/issue_comments_059362.json:
```json
{
    "body": "Changing component from build to porting: AIX or HP-UX.",
    "created_at": "2015-09-08T12:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7180#issuecomment-59362",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to porting: AIX or HP-UX.



---

archive/issue_events_016997.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-01-15T18:39:07Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16997"
}
```



---

archive/issue_events_016998.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-01-15T18:39:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16998"
}
```



---

archive/issue_comments_059363.json:
```json
{
    "body": "I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).",
    "created_at": "2019-01-15T18:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7180#issuecomment-59363",
    "user": "https://github.com/embray"
}
```

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).



---

archive/issue_comments_059364.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7180#issuecomment-59364",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_events_016999.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-23T21:26:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-16999"
}
```



---

archive/issue_events_017000.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-06-23T21:26:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-17000"
}
```



---

archive/issue_comments_059365.json:
```json
{
    "body": "We should close this ticket as outdated.",
    "created_at": "2020-06-23T21:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7180#issuecomment-59365",
    "user": "https://github.com/mkoeppe"
}
```

We should close this ticket as outdated.



---

archive/issue_events_017001.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-06-24T06:28:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7180#event-17001"
}
```



---

archive/issue_comments_059366.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-24T06:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7180",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7180#issuecomment-59366",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
