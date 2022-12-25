# Issue 7865: R  - WARNING: cannot run mixed C/Fortran code (then exits)

archive/issues_007865.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @dimpase\n\n## Build environment\n* Sun Ultra 27 3.333 GHz Intel Xeon. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)\n* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.\n* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. \n \n## The problem\n\n```\nchecking for inline... inline\nchecking for int... yes\nchecking size of int... 4\nchecking for long... yes\nchecking size of long... 8\nchecking for long long... yes\nchecking size of long long... 8\nchecking for double... yes\nchecking size of double... 8\nchecking for long double... yes\nchecking size of long double... 16\nchecking for size_t... (cached) yes\nchecking size of size_t... 8\nchecking whether we can compute C Make dependencies... yes, using gcc -std=gnu99 -MM\nchecking whether gcc -std=gnu99 supports -c -o FILE.lo... yes\nchecking how to get verbose linking output from sage_fortran... -v\nchecking for Fortran 77 libraries of sage_fortran...  -L/lib/64 -L/usr/lib/64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib/ -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/amd64 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../amd64 -L/lib/amd64 -L/usr/lib/amd64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../.. -lgfortranbegin -lgfortran -lm\nchecking how to get verbose linking output from gcc -std=gnu99... -v\nchecking for C libraries of gcc -std=gnu99...  -L/lib/64 -L/usr/lib/64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib/ -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/amd64 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../amd64 -L/lib/amd64 -L/usr/lib/amd64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../.. -lgcc_eh\nchecking for dummy main to link with Fortran 77 libraries... none\nchecking for Fortran 77 name-mangling scheme... lower case, underscore, no extra underscore\nchecking whether sage_fortran appends underscores to external names... yes\nchecking whether sage_fortran appends extra underscores to external names... no\nchecking whether mixed C/Fortran code can be run... configure: WARNING: cannot run mixed C/Fortran code\nconfigure: error: Maybe check LDFLAGS for paths to Fortran libraries?\nError configuring R.\n\nreal\t0m11.582s\nuser\t0m3.994s\nsys\t0m4.392s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7865\n\n",
    "created_at": "2010-01-07T05:47:58Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "R  - WARNING: cannot run mixed C/Fortran code (then exits)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7865",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @dimpase

## Build environment
* Sun Ultra 27 3.333 GHz Intel Xeon. 12 GB RAM
* OpenSolaris 2009.06 snv_111b X86
* Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 
 
## The problem

```
checking for inline... inline
checking for int... yes
checking size of int... 4
checking for long... yes
checking size of long... 8
checking for long long... yes
checking size of long long... 8
checking for double... yes
checking size of double... 8
checking for long double... yes
checking size of long double... 16
checking for size_t... (cached) yes
checking size of size_t... 8
checking whether we can compute C Make dependencies... yes, using gcc -std=gnu99 -MM
checking whether gcc -std=gnu99 supports -c -o FILE.lo... yes
checking how to get verbose linking output from sage_fortran... -v
checking for Fortran 77 libraries of sage_fortran...  -L/lib/64 -L/usr/lib/64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib/ -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/amd64 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../amd64 -L/lib/amd64 -L/usr/lib/amd64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../.. -lgfortranbegin -lgfortran -lm
checking how to get verbose linking output from gcc -std=gnu99... -v
checking for C libraries of gcc -std=gnu99...  -L/lib/64 -L/usr/lib/64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib/ -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/amd64 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../../amd64 -L/lib/amd64 -L/usr/lib/amd64 -L/export/home/drkirkby/sage-4.3.1.alpha1/local/lib -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4 -L/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/gcc/i386-pc-solaris2.11/4.3.4/../../.. -lgcc_eh
checking for dummy main to link with Fortran 77 libraries... none
checking for Fortran 77 name-mangling scheme... lower case, underscore, no extra underscore
checking whether sage_fortran appends underscores to external names... yes
checking whether sage_fortran appends extra underscores to external names... no
checking whether mixed C/Fortran code can be run... configure: WARNING: cannot run mixed C/Fortran code
configure: error: Maybe check LDFLAGS for paths to Fortran libraries?
Error configuring R.

real	0m11.582s
user	0m3.994s
sys	0m4.392s
```


Issue created by migration from https://trac.sagemath.org/ticket/7865





---

archive/issue_comments_068088.json:
```json
{
    "body": "I'm not sure whether this is still valid.  Could be.",
    "created_at": "2011-11-20T01:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7865#issuecomment-68088",
    "user": "https://github.com/kcrisman"
}
```

I'm not sure whether this is still valid.  Could be.



---

archive/issue_comments_068089.json:
```json
{
    "body": "Changing keywords from \"\" to \"r-project\".",
    "created_at": "2011-11-20T01:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7865#issuecomment-68089",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "r-project".



---

archive/issue_events_018806.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18806"
}
```



---

archive/issue_events_018807.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18807"
}
```



---

archive/issue_events_018808.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18808"
}
```



---

archive/issue_events_018809.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18809"
}
```



---

archive/issue_events_018810.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18810"
}
```



---

archive/issue_events_018811.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18811"
}
```



---

archive/issue_events_018812.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18812"
}
```



---

archive/issue_comments_068090.json:
```json
{
    "body": "This is outdated and should be closed.",
    "created_at": "2020-03-24T22:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7865#issuecomment-68090",
    "user": "https://github.com/mkoeppe"
}
```

This is outdated and should be closed.



---

archive/issue_events_018813.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-03-24T22:13:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18813"
}
```



---

archive/issue_events_018814.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-03-24T22:13:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18814"
}
```



---

archive/issue_comments_068091.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-03-24T22:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7865#issuecomment-68091",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068092.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-03-25T01:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7865#issuecomment-68092",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018815.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-03-29T06:50:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7865#event-18815"
}
```



---

archive/issue_comments_068093.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-29T06:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7865#issuecomment-68093",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
