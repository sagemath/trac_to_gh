# Issue 9029: sympow is buiding 32-bit on OpenSolaris x64 even when SAGE64 is set to "yes"

archive/issues_009029.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @williamstein\n\nWhen building 'sympow' on OpenSolaris, with SAGE64 set to yes, I see: \n\n\n\n```\n**ATTENTION** If you wish build SYMPOW, please ensure beforehand\nthat the various licenses of your C compiler, linker, assembler, etc.\nallow you to create a derived work based on SYMPOW and your C libraries\ngcc -O3   -c -o analrank.o analrank.c\ngcc -O3   -c -o analytic.o analytic.c\ngcc -O3   -c -o compute.o compute.c\ngcc -O3   -c -o compute2.o compute2.c\ngcc -O3   -c -o fpu.o fpu.c\ngcc -O3   -c -o help.o help.c\ngcc -O3   -c -o conductors.o conductors.c\ngcc -O3   -c -o disk.o disk.c\ngcc -O3   -c -o ec_ap.o ec_ap.c\ngcc -O3   -c -o ec_ap_bsgs.o ec_ap_bsgs.c\ngcc -O3   -c -o ec_ap_large.o ec_ap_large.c\ngcc -O3   -c -o eulerfactors.o eulerfactors.c\ngcc -O3   -c -o factor.o factor.c\ngcc -O3   -c -o generate.o generate.c\ngcc -O3   -c -o init_curve.o init_curve.c\ngcc -O3   -c -o main.o main.c\ngcc -O3   -c -o moddeg.o moddeg.c\ngcc -O3   -c -o periods.o periods.c\ngcc -O3   -c -o prepare.o prepare.c\ngcc -O3   -c -o QD.o QD.c\ngcc -O3   -c -o rootno.o rootno.c\ngcc -O3   -c -o util.o util.c\nmkdir -p datafiles\ntouch datafiles/param_data\ngcc -O3  -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o \n```\n\n\nThen checking one of the generated files, \n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow\n./local/lib/sympow/sympow:\tELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped\n```\n\n\nwe see it is indeed a 32-bit file. \n\nLooking at sympow-1.018.1.p6 source code, I can't see anything that would attempt to build 64-bit on any platform, so I doubt sympow ever built 64-bit on OS X versions where 32-bit was the default. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9029\n\n",
    "created_at": "2010-05-24T07:34:13Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "sympow is buiding 32-bit on OpenSolaris x64 even when SAGE64 is set to \"yes\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9029",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @williamstein

When building 'sympow' on OpenSolaris, with SAGE64 set to yes, I see: 



```
**ATTENTION** If you wish build SYMPOW, please ensure beforehand
that the various licenses of your C compiler, linker, assembler, etc.
allow you to create a derived work based on SYMPOW and your C libraries
gcc -O3   -c -o analrank.o analrank.c
gcc -O3   -c -o analytic.o analytic.c
gcc -O3   -c -o compute.o compute.c
gcc -O3   -c -o compute2.o compute2.c
gcc -O3   -c -o fpu.o fpu.c
gcc -O3   -c -o help.o help.c
gcc -O3   -c -o conductors.o conductors.c
gcc -O3   -c -o disk.o disk.c
gcc -O3   -c -o ec_ap.o ec_ap.c
gcc -O3   -c -o ec_ap_bsgs.o ec_ap_bsgs.c
gcc -O3   -c -o ec_ap_large.o ec_ap_large.c
gcc -O3   -c -o eulerfactors.o eulerfactors.c
gcc -O3   -c -o factor.o factor.c
gcc -O3   -c -o generate.o generate.c
gcc -O3   -c -o init_curve.o init_curve.c
gcc -O3   -c -o main.o main.c
gcc -O3   -c -o moddeg.o moddeg.c
gcc -O3   -c -o periods.o periods.c
gcc -O3   -c -o prepare.o prepare.c
gcc -O3   -c -o QD.o QD.c
gcc -O3   -c -o rootno.o rootno.c
gcc -O3   -c -o util.o util.c
mkdir -p datafiles
touch datafiles/param_data
gcc -O3  -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o 
```


Then checking one of the generated files, 


```
drkirkby@hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow
./local/lib/sympow/sympow:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
```


we see it is indeed a 32-bit file. 

Looking at sympow-1.018.1.p6 source code, I can't see anything that would attempt to build 64-bit on any platform, so I doubt sympow ever built 64-bit on OS X versions where 32-bit was the default. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9029





---

archive/issue_comments_083427.json:
```json
{
    "body": "For other OpenSolaris issues, see #9026",
    "created_at": "2010-05-24T18:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9029#issuecomment-83427",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

For other OpenSolaris issues, see #9026



---

archive/issue_comments_083428.json:
```json
{
    "body": "Mercurial patch to build 64-bit if SAGE64 is set to \"yes\"",
    "created_at": "2010-05-25T02:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9029#issuecomment-83428",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Mercurial patch to build 64-bit if SAGE64 is set to "yes"



---

archive/issue_comments_083429.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-25T03:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9029#issuecomment-83429",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083430.json:
```json
{
    "body": "Attachment [sympow-64-bit.patch](tarball://root/attachments/some-uuid/ticket9029/sympow-64-bit.patch) by drkirkby created at 2010-05-25 03:03:10\n\nWith the attached patch and\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p7.spkg\n\nthis now builds 64-bit. \n\n\n```\ngcc -O3  -m64  -c -o rootno.o rootno.c\ngcc -O3  -m64  -c -o util.o util.c\nmkdir -p datafiles\ntouch datafiles/param_data\ngcc -O3  -m64 -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o \n\nreal\t0m4.465s\nuser\t0m4.101s\nsys\t0m0.301s\nSuccessfully installed sympow-1.018.1.p7\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.2/spkg/build/sympow-1.018.1.p7\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing sympow-1.018.1.p7.spkg\ndrkirkby@hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow\n./local/lib/sympow/sympow:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available\n```\n\n\nThe binary is now 64-bit, not 32-bit as before. \n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow\n./local/lib/sympow/sympow:\tELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available\n```\n",
    "created_at": "2010-05-25T03:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9029#issuecomment-83430",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sympow-64-bit.patch](tarball://root/attachments/some-uuid/ticket9029/sympow-64-bit.patch) by drkirkby created at 2010-05-25 03:03:10

With the attached patch and

http://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p7.spkg

this now builds 64-bit. 


```
gcc -O3  -m64  -c -o rootno.o rootno.c
gcc -O3  -m64  -c -o util.o util.c
mkdir -p datafiles
touch datafiles/param_data
gcc -O3  -m64 -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o 

real	0m4.465s
user	0m4.101s
sys	0m0.301s
Successfully installed sympow-1.018.1.p7
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.2/spkg/build/sympow-1.018.1.p7
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing sympow-1.018.1.p7.spkg
drkirkby@hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow
./local/lib/sympow/sympow:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
```


The binary is now 64-bit, not 32-bit as before. 


```
drkirkby@hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow
./local/lib/sympow/sympow:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
```




---

archive/issue_comments_083431.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-10T16:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9029#issuecomment-83431",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083432.json:
```json
{
    "body": "Looks ok for me on Open Solaris:\n\n\n\n```\n-bash-4.0$ file local/lib/sympow/sympow \nlocal/lib/sympow/sympow:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available\n-bash-4.0$ \n\n```\n\n\nPositive review.\n\nJaap",
    "created_at": "2010-06-10T16:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9029#issuecomment-83432",
    "user": "https://github.com/jaapspies"
}
```

Looks ok for me on Open Solaris:



```
-bash-4.0$ file local/lib/sympow/sympow 
local/lib/sympow/sympow:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
-bash-4.0$ 

```


Positive review.

Jaap



---

archive/issue_events_009181.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-11T21:05:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9029",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9029#event-9181"
}
```



---

archive/issue_comments_083433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-11T21:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9029",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9029#issuecomment-83433",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
