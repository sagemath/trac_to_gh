# Issue 8089: ecl 9.10.2-20091105cvs.p1 faiils to build on Open Solaris x64

archive/issues_008089.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jas\n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.3.1 (with a few packages hacked to work on 64-bit)\n* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.\n* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. \n\n## The problem\nThis looks like an assembly code issue. \n\n\n```\n/ecl-9.10.2-20091105cvs.p1/src/src/c/arch/ffi_x86.d -> ffi_x86.c\ngcc -DECLDIR=\"\\\"/export/home/drkirkby/sage-4.3.1/local/lib/ecl-9.10.2\\\"\" -I. -I/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src/build -I/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src/src/c -I../ecl/gc -DECL_API -DECL_NO_LEGACY   -I/export/home/drkirkby/sage-4.3.1/local/include  -O2  -m64  -g  -Wall  -fPIC  -Dsun4sol2 -c -o ffi_x86.o ffi_x86.c\n/var/tmp//ccvhai7u.s: Assembler messages:\n/var/tmp//ccvhai7u.s:49: Error: suffix or operands invalid for `mov'\n/var/tmp//ccvhai7u.s:51: Error: suffix or operands invalid for `mov'\n/var/tmp//ccvhai7u.s:136: Error: suffix or operands invalid for `mov'\nmake[4]: *** [ffi_x86.o] Error 1\nmake[4]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src/build/c'\nmake[3]: *** [libeclmin.a] Error 2\nmake[3]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src/build'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src'\nFailed to build ECL ... exiting\n\nreal\t0m32.626s\nuser\t0m21.119s\nsys\t0m10.626s\nsage: An error occurred while installing ecl-9.10.2-20091105cvs.p1\n```\n\n\n == Possible solution ==\nI note from the ECL mailing list, that this option to configure might fix this, though it might need a later CVS snapshot. \n\n# --with-dffi=no is required to bypass inline assembly errors\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8089\n\n",
    "created_at": "2010-01-27T04:21:05Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ecl 9.10.2-20091105cvs.p1 faiils to build on Open Solaris x64",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8089",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  jas

## Build environment
* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
* OpenSolaris 2009.06 snv_111b X86
* Sage 4.3.1 (with a few packages hacked to work on 64-bit)
* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 

## The problem
This looks like an assembly code issue. 


```
/ecl-9.10.2-20091105cvs.p1/src/src/c/arch/ffi_x86.d -> ffi_x86.c
gcc -DECLDIR="\"/export/home/drkirkby/sage-4.3.1/local/lib/ecl-9.10.2\"" -I. -I/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src/build -I/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src/src/c -I../ecl/gc -DECL_API -DECL_NO_LEGACY   -I/export/home/drkirkby/sage-4.3.1/local/include  -O2  -m64  -g  -Wall  -fPIC  -Dsun4sol2 -c -o ffi_x86.o ffi_x86.c
/var/tmp//ccvhai7u.s: Assembler messages:
/var/tmp//ccvhai7u.s:49: Error: suffix or operands invalid for `mov'
/var/tmp//ccvhai7u.s:51: Error: suffix or operands invalid for `mov'
/var/tmp//ccvhai7u.s:136: Error: suffix or operands invalid for `mov'
make[4]: *** [ffi_x86.o] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src/build/c'
make[3]: *** [libeclmin.a] Error 2
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src/build'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/ecl-9.10.2-20091105cvs.p1/src'
Failed to build ECL ... exiting

real	0m32.626s
user	0m21.119s
sys	0m10.626s
sage: An error occurred while installing ecl-9.10.2-20091105cvs.p1
```


 == Possible solution ==
I note from the ECL mailing list, that this option to configure might fix this, though it might need a later CVS snapshot. 

# --with-dffi=no is required to bypass inline assembly errors



Issue created by migration from https://trac.sagemath.org/ticket/8089





---

archive/issue_comments_070767.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-31T00:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70767",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070768.json:
```json
{
    "body": "The latest version of Sage has ECL 10.2.1. Whilst the problem observed above still exists, the configure option \n\n```\n--with-dffi=no\n```\n\nis implemented in this version of ECL. \n\nA new spkg which resolves this problem by adding that option can be found at:\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p0.spkg\n\nAll I needed to do was add this bit of code:\n\n\n```\nif [ \"x`uname -rsm`\" = \"xSunOS 5.11 i86pc\" ] && [ \"x$SAGE64\" = xyes ]  ; then\n   # Need to add --with-dffi=no to disable assembly code on OpenSolaris x64. \n   # This may be needed for other variants of Solaris, but for now at least\n   # the option is only given if all the following are true\n   # 1) OpenSolaris (SunOS 5.11)\n   # 2) Intel or AMD CPU \n   # 3) 64-bit build\n   ./configure --prefix=$SAGE_LOCAL --with-dffi=no\nelse\n   ./configure --prefix=$SAGE_LOCAL \nfi\n```\n\n\nto ensure the option is only given on OpenSolaris (SunOS 5.11) with an Intel/AMD CPU if built in 64-bit mode. Whether the option would be needed on Solaris 10, or with SPARC processors I don't know. So for now it is applied in very specific circumstances. \n\nWith that configure option added, ECL then builds properly. \n\n\n```\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/ecl-10.2.1.p0/src/build'\n\nreal\t1m41.880s\nuser\t1m26.518s\nsys\t0m14.183s\nSuccessfully installed ecl-10.2.1.p0\n```\n",
    "created_at": "2010-05-31T00:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70768",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The latest version of Sage has ECL 10.2.1. Whilst the problem observed above still exists, the configure option 

```
--with-dffi=no
```

is implemented in this version of ECL. 

A new spkg which resolves this problem by adding that option can be found at:

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p0.spkg

All I needed to do was add this bit of code:


```
if [ "x`uname -rsm`" = "xSunOS 5.11 i86pc" ] && [ "x$SAGE64" = xyes ]  ; then
   # Need to add --with-dffi=no to disable assembly code on OpenSolaris x64. 
   # This may be needed for other variants of Solaris, but for now at least
   # the option is only given if all the following are true
   # 1) OpenSolaris (SunOS 5.11)
   # 2) Intel or AMD CPU 
   # 3) 64-bit build
   ./configure --prefix=$SAGE_LOCAL --with-dffi=no
else
   ./configure --prefix=$SAGE_LOCAL 
fi
```


to ensure the option is only given on OpenSolaris (SunOS 5.11) with an Intel/AMD CPU if built in 64-bit mode. Whether the option would be needed on Solaris 10, or with SPARC processors I don't know. So for now it is applied in very specific circumstances. 

With that configure option added, ECL then builds properly. 


```
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/ecl-10.2.1.p0/src/build'

real	1m41.880s
user	1m26.518s
sys	0m14.183s
Successfully installed ecl-10.2.1.p0
```




---

archive/issue_comments_070769.json:
```json
{
    "body": "Attachment [disable-assembly-code-on-OpenSolaris.patch](tarball://root/attachments/some-uuid/ticket8089/disable-assembly-code-on-OpenSolaris.patch) by drkirkby created at 2010-05-31 00:35:57\n\nMercurial patch to disable assembly code on OpenSolaris x64",
    "created_at": "2010-05-31T00:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70769",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [disable-assembly-code-on-OpenSolaris.patch](tarball://root/attachments/some-uuid/ticket8089/disable-assembly-code-on-OpenSolaris.patch) by drkirkby created at 2010-05-31 00:35:57

Mercurial patch to disable assembly code on OpenSolaris x64



---

archive/issue_comments_070770.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-31T02:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70770",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070771.json:
```json
{
    "body": "This needs to be closed, not reviewed. I realised I have already got positive review for a later version of ECL, which dod not need this fix  - see #8951.",
    "created_at": "2010-05-31T02:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70771",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This needs to be closed, not reviewed. I realised I have already got positive review for a later version of ECL, which dod not need this fix  - see #8951.



---

archive/issue_comments_070772.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-12T21:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70772",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Resolution: fixed



---

archive/issue_events_008295.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-06-12T21:20:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8089#event-8295"
}
```



---

archive/issue_comments_070773.json:
```json
{
    "body": "I was wrong to close this, as the issues are not incorporated in the 10.4.1 package. I'm reopening this.",
    "created_at": "2010-06-18T11:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70773",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I was wrong to close this, as the issues are not incorporated in the 10.4.1 package. I'm reopening this.



---

archive/issue_comments_070774.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-06-18T11:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70774",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from closed to new.



---

archive/issue_events_008296.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-06-18T11:53:37Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8089#event-8296"
}
```



---

archive/issue_comments_070775.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-06-18T11:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70775",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_070776.json:
```json
{
    "body": "#9264 Solves this issue, and several others related to ECL, so when #9264 is merged (it already has positive review), this issue will be resolved anyway. \n\nDave",
    "created_at": "2010-06-21T09:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70776",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

#9264 Solves this issue, and several others related to ECL, so when #9264 is merged (it already has positive review), this issue will be resolved anyway. 

Dave



---

archive/issue_comments_070777.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-06-25T11:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8089#issuecomment-70777",
    "user": "https://github.com/rlmill"
}
```

Resolution: duplicate



---

archive/issue_events_008297.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-25T11:20:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8089",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8089#event-8297"
}
```
