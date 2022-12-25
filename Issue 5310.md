# Issue 5310: addition to Sage for Msieve factoring program

archive/issues_005310.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @zimmermann6 wstein boothby @nexttime jpflori\n\nKeywords: msieve, factorization\n\nThis addition of Msieve will hopefully enhance Sage's Integer Factorization ability for all integers of a reasonable size, and provide the opportunity for users to utilize the Number Field Sieve.\n\nspkg located:  \n\nhttp://309codesign.com/code/\n\nAn explanation of Msieve from its documentation:\n\"There are plenty of algorithms for performing integer factorization. \nThe Msieve library implements most of them from scratch, and relies on\noptional external libraries for the rest of them. Trial division and\nPollard Rho is used on all inputs; if the result is less than 25 digits \nin size, tiny custom routines do the factoring. For larger numbers, the code\nswitches to the GMP-ECM library and runs the P-1, P+1 and ECM algorithms,\nexpending a user-configurable amount of effort to do so. If these do not \ncompletely factor the input number, the library switches to the heavy  \nartillery. Unless told otherwise, Msieve runs the self-initializing quadratic\nsieve algorithm, and if this doesn't factor the input number then you've\nfound a library problem. If you know what you're doing, Msieve also contains\na complete implementation of the number field sieve, that has helped complete\nsome of the largest public factorization efforts known.\"\nand\n\"To be as fast as possible. I claim (without proof) that for\n          completely factoring general inputs between 40 and 100 digits\n          in size, Msieve is faster than any other code implementing any\n          other algorithm.\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/5310\n\n",
    "created_at": "2009-02-19T04:25:19Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "addition to Sage for Msieve factoring program",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5310",
    "user": "https://trac.sagemath.org/admin/accounts/users/jblakeslee"
}
```
Assignee: mabshoff

CC:  @zimmermann6 wstein boothby @nexttime jpflori

Keywords: msieve, factorization

This addition of Msieve will hopefully enhance Sage's Integer Factorization ability for all integers of a reasonable size, and provide the opportunity for users to utilize the Number Field Sieve.

spkg located:  

http://309codesign.com/code/

An explanation of Msieve from its documentation:
"There are plenty of algorithms for performing integer factorization. 
The Msieve library implements most of them from scratch, and relies on
optional external libraries for the rest of them. Trial division and
Pollard Rho is used on all inputs; if the result is less than 25 digits 
in size, tiny custom routines do the factoring. For larger numbers, the code
switches to the GMP-ECM library and runs the P-1, P+1 and ECM algorithms,
expending a user-configurable amount of effort to do so. If these do not 
completely factor the input number, the library switches to the heavy  
artillery. Unless told otherwise, Msieve runs the self-initializing quadratic
sieve algorithm, and if this doesn't factor the input number then you've
found a library problem. If you know what you're doing, Msieve also contains
a complete implementation of the number field sieve, that has helped complete
some of the largest public factorization efforts known."
and
"To be as fast as possible. I claim (without proof) that for
          completely factoring general inputs between 40 and 100 digits
          in size, Msieve is faster than any other code implementing any
          other algorithm."

Issue created by migration from https://trac.sagemath.org/ticket/5310





---

archive/issue_comments_040783.json:
```json
{
    "body": "Attachment [msieve.patch](tarball://root/attachments/some-uuid/ticket5310/msieve.patch) by jblakeslee created at 2009-02-19 04:26:15",
    "created_at": "2009-02-19T04:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40783",
    "user": "https://trac.sagemath.org/admin/accounts/users/jblakeslee"
}
```

Attachment [msieve.patch](tarball://root/attachments/some-uuid/ticket5310/msieve.patch) by jblakeslee created at 2009-02-19 04:26:15



---

archive/issue_comments_040784.json:
```json
{
    "body": "I tried to build this on OS X Intel and immediately got this error, which suggests a bug in the spkg-install script itself.\n\n\n```\ngcc version 4.0.1 (Apple Inc. build 5465)\n****************************************************\n./spkg-install: line 5: [: missing `]'\n./spkg-install: line 5: i386: command not found\npick a target:\nx86       32-bit Intel/AMD systems (required if gcc used)\nx86_64    64-bit Intel/AMD systems (required if gcc used)\ngeneric   portable code\nalso add 'ECM=1' if GMP-ECM is available\nError building MSieve -- no file msieve was produced.\n\nreal\t0m0.084s\nuser\t0m0.011s\nsys\t0m0.022s\nsage: An error occurred while installing msieve-1.39\n```\n",
    "created_at": "2009-02-19T23:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40784",
    "user": "https://github.com/williamstein"
}
```

I tried to build this on OS X Intel and immediately got this error, which suggests a bug in the spkg-install script itself.


```
gcc version 4.0.1 (Apple Inc. build 5465)
****************************************************
./spkg-install: line 5: [: missing `]'
./spkg-install: line 5: i386: command not found
pick a target:
x86       32-bit Intel/AMD systems (required if gcc used)
x86_64    64-bit Intel/AMD systems (required if gcc used)
generic   portable code
also add 'ECM=1' if GMP-ECM is available
Error building MSieve -- no file msieve was produced.

real	0m0.084s
user	0m0.011s
sys	0m0.022s
sage: An error occurred while installing msieve-1.39
```




---

archive/issue_comments_040785.json:
```json
{
    "body": "The above error also occurs on all linux systems too.",
    "created_at": "2009-02-19T23:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40785",
    "user": "https://github.com/williamstein"
}
```

The above error also occurs on all linux systems too.



---

archive/issue_comments_040786.json:
```json
{
    "body": "I apologize for that.  Please try once again.  I have place the updated spkg in the same location.\n\nhttp://309codesign.com/code/msieve-1.39.spkg",
    "created_at": "2009-02-20T05:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40786",
    "user": "https://trac.sagemath.org/admin/accounts/users/jblakeslee"
}
```

I apologize for that.  Please try once again.  I have place the updated spkg in the same location.

http://309codesign.com/code/msieve-1.39.spkg



---

archive/issue_comments_040787.json:
```json
{
    "body": "This is too late for Sage 3.3, so bumped to 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T08:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is too late for Sage 3.3, so bumped to 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040788.json:
```json
{
    "body": "For mpQS vs. msieve Bill Hart has some numbers: \n\n```\nAnything over about 75 digits will be much slower on mpQS than on \nmsieve, due to the fact that the latter implements the double large \nprime variant and I don't. But the time for the second factorization \nis 15min 35s in mpQS. \n\nHere are some other times: \n\nmsieve mpQS \n\n2891670903938774131753: \n0.010s 0.000s \n\n7223934149780053552120237: \n0.020s 0.020s \n\n10890325463531930685071186191: \n0.070s 0.020s \n\n22746696815551279204773065179537: \n0.100s 0.040s \n\n34714945933810757311137622885134169: \n0.110s 0.050s \n\n10173256651176584336392947473501127227: \n0.130s 0.080s \n\n13018279488865181129955874562185134688337: \n0.200s 0.090s \n\n22301677236991560444759885102875349454660651: \n0.230s 0.210s \n\n8941543217242472708029937221739551760158967009: \n0.340s 0.280s \n\n6399059753136044767573853384689913264328520902553: \n0.570s 1.740s \n\n25506563753254047681462924229892337031031187330409537: \n1.050s 1.250s \n\n37987772559424160043450717911696894399547208398069213931: \n1.930s 2.520s \n\nSo for smaller numbers, mpQS is faster than msieve. I just haven't \nworked on speeding it up for numbers of 75 digits and more. \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T09:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40788",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For mpQS vs. msieve Bill Hart has some numbers: 

```
Anything over about 75 digits will be much slower on mpQS than on 
msieve, due to the fact that the latter implements the double large 
prime variant and I don't. But the time for the second factorization 
is 15min 35s in mpQS. 

Here are some other times: 

msieve mpQS 

2891670903938774131753: 
0.010s 0.000s 

7223934149780053552120237: 
0.020s 0.020s 

10890325463531930685071186191: 
0.070s 0.020s 

22746696815551279204773065179537: 
0.100s 0.040s 

34714945933810757311137622885134169: 
0.110s 0.050s 

10173256651176584336392947473501127227: 
0.130s 0.080s 

13018279488865181129955874562185134688337: 
0.200s 0.090s 

22301677236991560444759885102875349454660651: 
0.230s 0.210s 

8941543217242472708029937221739551760158967009: 
0.340s 0.280s 

6399059753136044767573853384689913264328520902553: 
0.570s 1.740s 

25506563753254047681462924229892337031031187330409537: 
1.050s 1.250s 

37987772559424160043450717911696894399547208398069213931: 
1.930s 2.520s 

So for smaller numbers, mpQS is faster than msieve. I just haven't 
worked on speeding it up for numbers of 75 digits and more. 
```


Cheers,

Michael



---

archive/issue_comments_040789.json:
```json
{
    "body": "I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS):\n\n```\n****************************************************\nHost system\nuname -a:\nLinux sage.math.washington.edu 2.6.24-23-server #1 SMP Mon Jan 26 01:36:05 UTC 2009 x86_64 GNU/Linux\n****************************************************\n****************************************************\nGCC Version\ngcc -v\nUsing built-in specs.\nTarget: x86_64-linux-gnu\nConfigured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu\nThread model: posix\ngcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu3)\n****************************************************\ngcc -D_FILE_OFFSET_BITS=64 -O3 -fomit-frame-pointer -march=athlon-xp -DNDEBUG  -Wall -W -Wconversion -Iinclude -Ignfs/poly -c -o common/lanczos/lanczos.o common/lanczos/lanczos.c\ncommon/lanczos/lanczos.c:1: error: CPU you selected does not support x86-64 instruction set\ncommon/lanczos/lanczos.c:1: error: CPU you selected does not support x86-64 instruction set\nmake: *** [common/lanczos/lanczos.o] Error 1\nError building M-Sieve\n\nreal    0m0.040s\nuser    0m0.010s\nsys     0m0.010s\nsage: An error occurred while installing msieve-1.39\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /scratch/wstein/build/sage-3.4.1.rc2-ref2/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/scratch/wstein/build/sage-3.4.1.rc2-ref2/spkg/build/msieve-1.39 and type 'make'.\nInstead type \"/scratch/wstein/build/sage-3.4.1.rc2-ref2/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/scratch/wstein/build/sage-3.4.1.rc2-ref2/spkg/build/msieve-1.39\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\nwstein@sage:~/build/sage-3.4.1.rc2-ref2$ \n```\n\n\n\nI also tried building on 32-bit OS X 10.5 (my laptop):\n\n```\nWall -W -Wconversion -Iinclude -Ignfs/poly -c -o common/ap.o common/ap.c\ncommon/ap.c: In function \u2018ap_mul\u2019:\ncommon/ap.c:339: error: can't find a register in class \u2018GENERAL_REGS\u2019 while reloading \u2018asm\u2019\ncommon/ap.c:339: error: can't find a register in class \u2018GENERAL_REGS\u2019 while reloading \u2018asm\u2019\ncommon/ap.c:339: error: can't find a register in class \u2018GENERAL_REGS\u2019 while reloading \u2018asm\u2019\ncommon/ap.c:339: error: can't find a register in class \u2018GENERAL_REGS\u2019 while reloading \u2018asm\u2019\nmake: *** [common/ap.o] Error 1\nError building M-Sieve\n\nreal\t0m5.432s\nuser\t0m1.786s\nsys\t0m0.348s\nsage: An error occurred while installing msieve-1.39\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /Users/wstein/build/sage-3.4.1.rc2/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/Users/wstein/build/sage-3.4.1.rc2/spkg/build/msieve-1.39 and type 'make'.\nInstead type \"/Users/wstein/build/sage-3.4.1.rc2/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/Users/wstein/build/sage-3.4.1.rc2/spkg/build/msieve-1.39\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\nteragon:~ wstein$ \n```\n\n\nSo I can't build this on either of my main devel machines, so it's hard to go anywhere with.",
    "created_at": "2009-04-12T06:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40789",
    "user": "https://github.com/williamstein"
}
```

I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS):

```
****************************************************
Host system
uname -a:
Linux sage.math.washington.edu 2.6.24-23-server #1 SMP Mon Jan 26 01:36:05 UTC 2009 x86_64 GNU/Linux
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu3)
****************************************************
gcc -D_FILE_OFFSET_BITS=64 -O3 -fomit-frame-pointer -march=athlon-xp -DNDEBUG  -Wall -W -Wconversion -Iinclude -Ignfs/poly -c -o common/lanczos/lanczos.o common/lanczos/lanczos.c
common/lanczos/lanczos.c:1: error: CPU you selected does not support x86-64 instruction set
common/lanczos/lanczos.c:1: error: CPU you selected does not support x86-64 instruction set
make: *** [common/lanczos/lanczos.o] Error 1
Error building M-Sieve

real    0m0.040s
user    0m0.010s
sys     0m0.010s
sage: An error occurred while installing msieve-1.39
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /scratch/wstein/build/sage-3.4.1.rc2-ref2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/scratch/wstein/build/sage-3.4.1.rc2-ref2/spkg/build/msieve-1.39 and type 'make'.
Instead type "/scratch/wstein/build/sage-3.4.1.rc2-ref2/sage -sh"
in order to set all environment variables correctly, then cd to
/scratch/wstein/build/sage-3.4.1.rc2-ref2/spkg/build/msieve-1.39
(When you are done debugging, you can type "exit" to leave the
subshell.)
wstein@sage:~/build/sage-3.4.1.rc2-ref2$ 
```



I also tried building on 32-bit OS X 10.5 (my laptop):

```
Wall -W -Wconversion -Iinclude -Ignfs/poly -c -o common/ap.o common/ap.c
common/ap.c: In function ‘ap_mul’:
common/ap.c:339: error: can't find a register in class ‘GENERAL_REGS’ while reloading ‘asm’
common/ap.c:339: error: can't find a register in class ‘GENERAL_REGS’ while reloading ‘asm’
common/ap.c:339: error: can't find a register in class ‘GENERAL_REGS’ while reloading ‘asm’
common/ap.c:339: error: can't find a register in class ‘GENERAL_REGS’ while reloading ‘asm’
make: *** [common/ap.o] Error 1
Error building M-Sieve

real	0m5.432s
user	0m1.786s
sys	0m0.348s
sage: An error occurred while installing msieve-1.39
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wstein/build/sage-3.4.1.rc2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/wstein/build/sage-3.4.1.rc2/spkg/build/msieve-1.39 and type 'make'.
Instead type "/Users/wstein/build/sage-3.4.1.rc2/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/wstein/build/sage-3.4.1.rc2/spkg/build/msieve-1.39
(When you are done debugging, you can type "exit" to leave the
subshell.)
teragon:~ wstein$ 
```


So I can't build this on either of my main devel machines, so it's hard to go anywhere with.



---

archive/issue_comments_040790.json:
```json
{
    "body": "> I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]\n\nWilliam, you need to disable manually the default -march=athlon-xp in Makefile.",
    "created_at": "2009-04-17T12:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40790",
    "user": "https://github.com/zimmermann6"
}
```

> I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]

William, you need to disable manually the default -march=athlon-xp in Makefile.



---

archive/issue_comments_040791.json:
```json
{
    "body": "Replying to [comment:9 zimmerma]:\n> > I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]\n> \n> William, you need to disable manually the default -march=athlon-xp in Makefile.\n\nThat change has been added to the .spkg and should now work on x86_64 without having to mess with the Makefile.  The new .spkg hopefully works for intel-based Macs, too, but I haven't had a chance to try it yet. \nThanks.",
    "created_at": "2009-04-17T16:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40791",
    "user": "https://trac.sagemath.org/admin/accounts/users/jblakeslee"
}
```

Replying to [comment:9 zimmerma]:
> > I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]
> 
> William, you need to disable manually the default -march=athlon-xp in Makefile.

That change has been added to the .spkg and should now work on x86_64 without having to mess with the Makefile.  The new .spkg hopefully works for intel-based Macs, too, but I haven't had a chance to try it yet. 
Thanks.



---

archive/issue_comments_040792.json:
```json
{
    "body": "Replying to [comment:10 jblakeslee]:\n> Replying to [comment:9 zimmerma]:\n> > > I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]\n> > \n> > William, you need to disable manually the default -march=athlon-xp in Makefile.\n> \n> That change has been added to the .spkg and should now work on x86_64 without having to mess with the Makefile.  The new .spkg hopefully works for intel-based Macs, too, but I haven't had a chance to try it yet. \n> Thanks.\n\nThat version didn't work on the Intel Mac I tested, so updated again, and now does compile for me.",
    "created_at": "2009-04-20T05:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40792",
    "user": "https://trac.sagemath.org/admin/accounts/users/jblakeslee"
}
```

Replying to [comment:10 jblakeslee]:
> Replying to [comment:9 zimmerma]:
> > > I tried on sage.math (our x86_64 server with ubuntu 8.04.LTS): [...]
> > 
> > William, you need to disable manually the default -march=athlon-xp in Makefile.
> 
> That change has been added to the .spkg and should now work on x86_64 without having to mess with the Makefile.  The new .spkg hopefully works for intel-based Macs, too, but I haven't had a chance to try it yet. 
> Thanks.

That version didn't work on the Intel Mac I tested, so updated again, and now does compile for me.



---

archive/issue_comments_040793.json:
```json
{
    "body": "jblakeslee, the url doesn't appear to be correct.  The file msieve-1.39.spkg appears to be missing, and msieve-1.38.spkg in that directory is broken.  Please upload again.",
    "created_at": "2009-10-01T05:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40793",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

jblakeslee, the url doesn't appear to be correct.  The file msieve-1.39.spkg appears to be missing, and msieve-1.38.spkg in that directory is broken.  Please upload again.



---

archive/issue_comments_040794.json:
```json
{
    "body": "Replying to [comment:12 boothby]:\n> jblakeslee, the url doesn't appear to be correct.  The file msieve-1.39.spkg appears to be missing, and msieve-1.38.spkg in that directory is broken.  Please upload again.\n\nPlease use this url:\nhttp://309codesign.com/code/msieve-1.38.spkg\n\nPlease try again.  It is working for me with the following command:\nsage -i msieve-1.38.spkg\n\nIf it fails again can you give os type and error info.  Thank you.",
    "created_at": "2009-10-03T04:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40794",
    "user": "https://trac.sagemath.org/admin/accounts/users/jblakeslee"
}
```

Replying to [comment:12 boothby]:
> jblakeslee, the url doesn't appear to be correct.  The file msieve-1.39.spkg appears to be missing, and msieve-1.38.spkg in that directory is broken.  Please upload again.

Please use this url:
http://309codesign.com/code/msieve-1.38.spkg

Please try again.  It is working for me with the following command:
sage -i msieve-1.38.spkg

If it fails again can you give os type and error info.  Thank you.



---

archive/issue_comments_040795.json:
```json
{
    "body": "Attachment [msieve-1.47.spkg](tarball://root/attachments/some-uuid/ticket5310/msieve-1.47.spkg) by @a-andre created at 2010-10-27 14:16:05\n\nI attached a patch for the msieve interface updated to version 1.47.\n\nSomeone has to check whether msieve can be compiled on every relevant system and if necessary update the spkg-file.\nIt works on x86_64.",
    "created_at": "2010-10-27T14:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40795",
    "user": "https://github.com/a-andre"
}
```

Attachment [msieve-1.47.spkg](tarball://root/attachments/some-uuid/ticket5310/msieve-1.47.spkg) by @a-andre created at 2010-10-27 14:16:05

I attached a patch for the msieve interface updated to version 1.47.

Someone has to check whether msieve can be compiled on every relevant system and if necessary update the spkg-file.
It works on x86_64.



---

archive/issue_comments_040796.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-28T14:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40796",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_040797.json:
```json
{
    "body": "Remove assignee mabshoff.",
    "created_at": "2010-10-28T21:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40797",
    "user": "https://github.com/nexttime"
}
```

Remove assignee mabshoff.



---

archive/issue_comments_040798.json:
```json
{
    "body": "Attachment [msieve1.47.patch](tarball://root/attachments/some-uuid/ticket5310/msieve1.47.patch) by @a-andre created at 2010-11-03 08:38:45",
    "created_at": "2010-11-03T08:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40798",
    "user": "https://github.com/a-andre"
}
```

Attachment [msieve1.47.patch](tarball://root/attachments/some-uuid/ticket5310/msieve1.47.patch) by @a-andre created at 2010-11-03 08:38:45



---

archive/issue_comments_040799.json:
```json
{
    "body": "Attachment [trac_5310_msieve_148.patch](tarball://root/attachments/some-uuid/ticket5310/trac_5310_msieve_148.patch) by @a-andre created at 2011-01-17 17:13:18",
    "created_at": "2011-01-17T17:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40799",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_5310_msieve_148.patch](tarball://root/attachments/some-uuid/ticket5310/trac_5310_msieve_148.patch) by @a-andre created at 2011-01-17 17:13:18



---

archive/issue_comments_040800.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-27T20:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40800",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_040801.json:
```json
{
    "body": "Replying to [comment:14 jblakeslee]:\n> Please use this url:\n> http://309codesign.com/code/msieve-1.38.spkg\n\nThat link, which you posted 19 months ago, is not valid\n\n\n```\ndrkirkby@hawk:~/sage-4.7.alpha5/spkg/standard$ wget http://309codesign.com/code/msieve-1.39.spkg\n--2011-04-27 21:55:45--  http://309codesign.com/code/msieve-1.39.spkg\nResolving 309codesign.com (309codesign.com)... 74.220.215.62\nConnecting to 309codesign.com (309codesign.com)|74.220.215.62|:80... connected.\nHTTP request sent, awaiting response... 404 Not Found\n2011-04-27 21:55:56 ERROR 404: Not Found.\n```\n",
    "created_at": "2011-04-27T20:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40801",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:14 jblakeslee]:
> Please use this url:
> http://309codesign.com/code/msieve-1.38.spkg

That link, which you posted 19 months ago, is not valid


```
drkirkby@hawk:~/sage-4.7.alpha5/spkg/standard$ wget http://309codesign.com/code/msieve-1.39.spkg
--2011-04-27 21:55:45--  http://309codesign.com/code/msieve-1.39.spkg
Resolving 309codesign.com (309codesign.com)... 74.220.215.62
Connecting to 309codesign.com (309codesign.com)|74.220.215.62|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2011-04-27 21:55:56 ERROR 404: Not Found.
```




---

archive/issue_comments_040802.json:
```json
{
    "body": "Replying to [comment:18 drkirkby]:\n> Replying to [comment:14 jblakeslee]:\n> > Please use this url:\n> > http://309codesign.com/code/msieve-1.38.spkg\n> \n> That link, which you posted 19 months ago, is not valid\n> \n\nPlease use the msieve-1.48.spkg and patch, that are added by aapitzsch, just before your post, since I have stopped updating my link.  I had good luck with his msieve-1.47.spkg.\nThank you.",
    "created_at": "2011-05-03T02:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40802",
    "user": "https://trac.sagemath.org/admin/accounts/users/jblakeslee"
}
```

Replying to [comment:18 drkirkby]:
> Replying to [comment:14 jblakeslee]:
> > Please use this url:
> > http://309codesign.com/code/msieve-1.38.spkg
> 
> That link, which you posted 19 months ago, is not valid
> 

Please use the msieve-1.48.spkg and patch, that are added by aapitzsch, just before your post, since I have stopped updating my link.  I had good luck with his msieve-1.47.spkg.
Thank you.



---

archive/issue_comments_040803.json:
```json
{
    "body": "Ping.",
    "created_at": "2011-10-31T18:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40803",
    "user": "https://github.com/nexttime"
}
```

Ping.



---

archive/issue_comments_040804.json:
```json
{
    "body": "see also #6232",
    "created_at": "2011-11-01T09:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40804",
    "user": "https://github.com/zimmermann6"
}
```

see also #6232



---

archive/issue_comments_040805.json:
```json
{
    "body": "Attachment [msieve-1.49.p0.spkg](tarball://root/attachments/some-uuid/ticket5310/msieve-1.49.p0.spkg) by @a-andre created at 2011-11-01 18:36:22",
    "created_at": "2011-11-01T18:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40805",
    "user": "https://github.com/a-andre"
}
```

Attachment [msieve-1.49.p0.spkg](tarball://root/attachments/some-uuid/ticket5310/msieve-1.49.p0.spkg) by @a-andre created at 2011-11-01 18:36:22



---

archive/issue_comments_040806.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-11-01T18:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40806",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_040807.json:
```json
{
    "body": "Here is an updated version of msieve.",
    "created_at": "2011-11-01T18:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40807",
    "user": "https://github.com/a-andre"
}
```

Here is an updated version of msieve.



---

archive/issue_comments_040808.json:
```json
{
    "body": "`EXAMPLE:` and `EXAMPLES:` should have a double-colon (`::`).\n\nThe indentation of the results in the first examples block looks strange; they should line up with the `sage:` prompt.\n\nHaven't tested, but one should make sure that all temporary files are created in or below `SAGE_TMP` (or `SAGE_TMPDIR`?) [at least] during doctesting, since they should also pass if the user doesn't have write access on the Sage installation tree.\n\n(An ordinary user should of course also be able to just *use* the code without permission issues.)",
    "created_at": "2011-11-01T19:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40808",
    "user": "https://github.com/nexttime"
}
```

`EXAMPLE:` and `EXAMPLES:` should have a double-colon (`::`).

The indentation of the results in the first examples block looks strange; they should line up with the `sage:` prompt.

Haven't tested, but one should make sure that all temporary files are created in or below `SAGE_TMP` (or `SAGE_TMPDIR`?) [at least] during doctesting, since they should also pass if the user doesn't have write access on the Sage installation tree.

(An ordinary user should of course also be able to just *use* the code without permission issues.)



---

archive/issue_comments_040809.json:
```json
{
    "body": "P.S.: For inclusion into Sage, an spkg usually has to get an optional one first; then there should be a poll on sage-devel to make it a standard spkg.  The code should perhaps take care of that, i.e., not assume that `msieve` is installed, and print a meaningful error message (instructing the user how to install the spkg) in case it isn't.",
    "created_at": "2011-11-01T19:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40809",
    "user": "https://github.com/nexttime"
}
```

P.S.: For inclusion into Sage, an spkg usually has to get an optional one first; then there should be a poll on sage-devel to make it a standard spkg.  The code should perhaps take care of that, i.e., not assume that `msieve` is installed, and print a meaningful error message (instructing the user how to install the spkg) in case it isn't.



---

archive/issue_comments_040810.json:
```json
{
    "body": "Replying to [comment:23 leif]:\n> `EXAMPLE:` and `EXAMPLES:` should have a double-colon (`::`).\n> \n> The indentation of the results in the first examples block looks strange; they should line up with the `sage:` prompt.\n> \nFixed this.\n\n> Haven't tested, but one should make sure that all temporary files are created in or below `SAGE_TMP` (or `SAGE_TMPDIR`?) [at least] during doctesting, since they should also pass if the user doesn't have write access on the Sage installation tree.\n> \n> (An ordinary user should of course also be able to just *use* the code without permission issues.)\n\nMore or less I copied the TMPDIR part from qsieve.py , so this shouldn't be a problem.\n\nExamples are marked as optional now and in case msieve isn't installed there is warning.\n\nThere was already a discussion about adding msieve in 2009.\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/91f1ecf4dca5511d/d68c74a19b741255",
    "created_at": "2011-11-01T21:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40810",
    "user": "https://github.com/a-andre"
}
```

Replying to [comment:23 leif]:
> `EXAMPLE:` and `EXAMPLES:` should have a double-colon (`::`).
> 
> The indentation of the results in the first examples block looks strange; they should line up with the `sage:` prompt.
> 
Fixed this.

> Haven't tested, but one should make sure that all temporary files are created in or below `SAGE_TMP` (or `SAGE_TMPDIR`?) [at least] during doctesting, since they should also pass if the user doesn't have write access on the Sage installation tree.
> 
> (An ordinary user should of course also be able to just *use* the code without permission issues.)

More or less I copied the TMPDIR part from qsieve.py , so this shouldn't be a problem.

Examples are marked as optional now and in case msieve isn't installed there is warning.

There was already a discussion about adding msieve in 2009.
See http://groups.google.com/group/sage-devel/browse_thread/thread/91f1ecf4dca5511d/d68c74a19b741255



---

archive/issue_comments_040811.json:
```json
{
    "body": "The spkg certainly needs some work, which I'll do later.\n\nThe patch to the Sage library could be tweaked w.r.t. markup (e.g. identifiers and program names should be typeset monospaced, i.e. ```parameter```, ```True```, ```msieve``` etc.).  I'll *perhaps* make a reviewer patch as well.",
    "created_at": "2011-11-02T00:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40811",
    "user": "https://github.com/nexttime"
}
```

The spkg certainly needs some work, which I'll do later.

The patch to the Sage library could be tweaked w.r.t. markup (e.g. identifiers and program names should be typeset monospaced, i.e. ```parameter```, ```True```, ```msieve``` etc.).  I'll *perhaps* make a reviewer patch as well.



---

archive/issue_comments_040812.json:
```json
{
    "body": "Replying to [comment:25 aapitzsch]:\n> [...] in case msieve isn't installed there is warning.\n\nHow about printing that message and raising `NotImplementedError` (or `RuntimeError`)?\n\nThat way other (higher-level) functions can call `msieve()` and catch these exceptions.\n\nWe could also put the \"warning\" into the message of the exception, such that the output isn't messed up by just trying to call `msieve()` (from other parts of Sage).\n\n\n\n\n*SAGE* should be *Sage* btw.\n\n\n\n\nThe `TMPDIR` environment variable must not be modified globally; if there's no other way to tell `msieve` where it should put temporary files, a modified environment has to be passed to `msieve`.",
    "created_at": "2011-11-02T00:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40812",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:25 aapitzsch]:
> [...] in case msieve isn't installed there is warning.

How about printing that message and raising `NotImplementedError` (or `RuntimeError`)?

That way other (higher-level) functions can call `msieve()` and catch these exceptions.

We could also put the "warning" into the message of the exception, such that the output isn't messed up by just trying to call `msieve()` (from other parts of Sage).




*SAGE* should be *Sage* btw.




The `TMPDIR` environment variable must not be modified globally; if there's no other way to tell `msieve` where it should put temporary files, a modified environment has to be passed to `msieve`.



---

archive/issue_comments_040813.json:
```json
{
    "body": "Attachment [trac_5310_msieve_149.patch](tarball://root/attachments/some-uuid/ticket5310/trac_5310_msieve_149.patch) by @a-andre created at 2011-11-12 15:40:36\n\nPatch updated.\n\nReplying to [comment:27 leif]:\n> Replying to [comment:25 aapitzsch]:\n> > [...] in case msieve isn't installed there is warning.\n> \n> How about printing that message and raising `NotImplementedError` (or `RuntimeError`)?\n> \nNow `NotImplementedError` is raised.\n> \n> *SAGE* should be *Sage* btw.\n> \nDone.\n> \n> The `TMPDIR` environment variable must not be modified globally; if there's no other way to tell `msieve` where it should put temporary files, a modified environment has to be passed to `msieve`.\n\nFixed.",
    "created_at": "2011-11-12T15:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40813",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_5310_msieve_149.patch](tarball://root/attachments/some-uuid/ticket5310/trac_5310_msieve_149.patch) by @a-andre created at 2011-11-12 15:40:36

Patch updated.

Replying to [comment:27 leif]:
> Replying to [comment:25 aapitzsch]:
> > [...] in case msieve isn't installed there is warning.
> 
> How about printing that message and raising `NotImplementedError` (or `RuntimeError`)?
> 
Now `NotImplementedError` is raised.
> 
> *SAGE* should be *Sage* btw.
> 
Done.
> 
> The `TMPDIR` environment variable must not be modified globally; if there's no other way to tell `msieve` where it should put temporary files, a modified environment has to be passed to `msieve`.

Fixed.



---

archive/issue_comments_040814.json:
```json
{
    "body": "I tried installing the spkg with Sage 4.7.2 on a 32-bit computer and it failed:\n\n```\nmacaron% ./sage -i msieve-1.49.p0.spkg\n...\n\nranlib libmsieve.a\ngcc -D_FILE_OFFSET_BITS=64 -O3 -fomit-frame-pointer -march=k8 -DNDEBUG -D_LARGEFILE64_SOURCE  -Wall -W -DMSIEVE_SVN_VERSION=\"\\\"exported\\\"\" -I. -Iinclude -Ignfs -Ignfs/poly -Ignfs/poly/stage1 -DHAVE_GMP_ECM \"-I/localdisk/tmp/sage-4.7.2/local/include\" demo.c -o msieve  \\\n                        libmsieve.a -lecm -lz -lgmp -lm -lpthread\nlibmsieve.a(sieve.qo): In function `do_sieving':\nsieve.c:(.text+0x1335): undefined reference to `qs_core_sieve_p3_64k'\nsieve.c:(.text+0x175b): undefined reference to `qs_core_sieve_p2_64k'\nsieve.c:(.text+0x2556): undefined reference to `qs_core_sieve_pm_32k'\nsieve.c:(.text+0x2603): undefined reference to `qs_core_sieve_k7_64k'\nsieve.c:(.text+0x266b): undefined reference to `qs_core_sieve_k7xp_64k'\ncollect2: ld returned 1 exit status\nmake: *** [x86_64] Error 1\nError building Msieve -- no file msieve was produced.\n\nreal    1m33.556s\nuser    0m29.657s\nsys     0m2.000s\nsage: An error occurred while installing msieve-1.49.p0\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /localdisk/tmp/sage-4.7.2/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem yourself, *don't* just cd to\n/localdisk/tmp/sage-4.7.2/spkg/build/msieve-1.49.p0 and type 'make check' or whatever is appropriate.\nInstead, the following commands setup all environment variables\ncorrectly and load a subshell for you to debug the error:\n(cd '/localdisk/tmp/sage-4.7.2/spkg/build/msieve-1.49.p0' && '/localdisk/tmp/sage-4.7.2/sage' -sh)\nWhen you are done debugging, you can type \"exit\" to leave the\nsubshell.\nError: Failed to install package 'msieve-1.49.p0'.\n```\n\nThe processor is a Pentium 4. The system is Fedora 10.\n\nPaul Zimmermann",
    "created_at": "2011-12-21T09:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40814",
    "user": "https://github.com/zimmermann6"
}
```

I tried installing the spkg with Sage 4.7.2 on a 32-bit computer and it failed:

```
macaron% ./sage -i msieve-1.49.p0.spkg
...

ranlib libmsieve.a
gcc -D_FILE_OFFSET_BITS=64 -O3 -fomit-frame-pointer -march=k8 -DNDEBUG -D_LARGEFILE64_SOURCE  -Wall -W -DMSIEVE_SVN_VERSION="\"exported\"" -I. -Iinclude -Ignfs -Ignfs/poly -Ignfs/poly/stage1 -DHAVE_GMP_ECM "-I/localdisk/tmp/sage-4.7.2/local/include" demo.c -o msieve  \
                        libmsieve.a -lecm -lz -lgmp -lm -lpthread
libmsieve.a(sieve.qo): In function `do_sieving':
sieve.c:(.text+0x1335): undefined reference to `qs_core_sieve_p3_64k'
sieve.c:(.text+0x175b): undefined reference to `qs_core_sieve_p2_64k'
sieve.c:(.text+0x2556): undefined reference to `qs_core_sieve_pm_32k'
sieve.c:(.text+0x2603): undefined reference to `qs_core_sieve_k7_64k'
sieve.c:(.text+0x266b): undefined reference to `qs_core_sieve_k7xp_64k'
collect2: ld returned 1 exit status
make: *** [x86_64] Error 1
Error building Msieve -- no file msieve was produced.

real    1m33.556s
user    0m29.657s
sys     0m2.000s
sage: An error occurred while installing msieve-1.49.p0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /localdisk/tmp/sage-4.7.2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/localdisk/tmp/sage-4.7.2/spkg/build/msieve-1.49.p0 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/localdisk/tmp/sage-4.7.2/spkg/build/msieve-1.49.p0' && '/localdisk/tmp/sage-4.7.2/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
Error: Failed to install package 'msieve-1.49.p0'.
```

The processor is a Pentium 4. The system is Fedora 10.

Paul Zimmermann



---

archive/issue_comments_040815.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-21T09:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40815",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_040816.json:
```json
{
    "body": "The fails on my OpenSolaris box, and I can see will fail on any sort of Solaris system. These lines:\n\n\n```\nif [ \"`uname -m`\" = \"SunOS\" ]; then\n    $MAKE generic ECM=1\nfi\n```\n\n\nmake no sense, as the -m option to 'uname' is defined by POSIX to return the hardware, not the operating system. See:\n\nhttp://pubs.opengroup.org/onlinepubs/009695399/utilities/uname.html\n\nSo it produces:\n\n\n```\ndrkirkby@hawk:~$ uname -m\ni86pc\n```\n\n\nand on a SPARC would produce something different, like sun4m, sun4u, sun4v and possibly something else for the newer processors. On my old SPARC\n\n\n```\n-bash-3.00$ uname -m\nsun4u\n```\n\n\n\nRather than invoke the external program 'uname', it is better to use the sage variable UNAME. The following is the most robust way of testing a variable, which will work for any shell, and pretty much any circumstances. \n\n\n```\nif [ \"x$UNAME\" = xSunOS ] ; then\n```\n\n\nThere's nothing to build a 64-bit version on Solaris - the SAGE64 variable is not used. \n\nI also got another failure:\n\n\n```\n****************************************************\npatching file Makefile\nError building Msieve -- no file msieve was produced.\n\nreal\t0m0.022s\nuser\t0m0.006s\nsys\t0m0.015s\nsage: An error occurred while installing msieve-1.49.p0\n```\n\n\nI suspect this is picking up the Solaris version of patch, not the GNU one which is part of Sage, though I've never seen this issue before. \n\nAlso, this seems a bit pointless\n\n\n```\n$CP msieve \"$SAGE_LOCAL\"/bin/\n```\n\n\nWe should just call 'cp' directly. Variables are useful for programs like \"make\", but not for a simple copy like this. \n\nThe whole of spkg-install is a bit of a mess. It basically needs a total re-write. \n\nAlso, there is no spkg-check file. \n\nDave",
    "created_at": "2012-01-03T23:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40816",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The fails on my OpenSolaris box, and I can see will fail on any sort of Solaris system. These lines:


```
if [ "`uname -m`" = "SunOS" ]; then
    $MAKE generic ECM=1
fi
```


make no sense, as the -m option to 'uname' is defined by POSIX to return the hardware, not the operating system. See:

http://pubs.opengroup.org/onlinepubs/009695399/utilities/uname.html

So it produces:


```
drkirkby@hawk:~$ uname -m
i86pc
```


and on a SPARC would produce something different, like sun4m, sun4u, sun4v and possibly something else for the newer processors. On my old SPARC


```
-bash-3.00$ uname -m
sun4u
```



Rather than invoke the external program 'uname', it is better to use the sage variable UNAME. The following is the most robust way of testing a variable, which will work for any shell, and pretty much any circumstances. 


```
if [ "x$UNAME" = xSunOS ] ; then
```


There's nothing to build a 64-bit version on Solaris - the SAGE64 variable is not used. 

I also got another failure:


```
****************************************************
patching file Makefile
Error building Msieve -- no file msieve was produced.

real	0m0.022s
user	0m0.006s
sys	0m0.015s
sage: An error occurred while installing msieve-1.49.p0
```


I suspect this is picking up the Solaris version of patch, not the GNU one which is part of Sage, though I've never seen this issue before. 

Also, this seems a bit pointless


```
$CP msieve "$SAGE_LOCAL"/bin/
```


We should just call 'cp' directly. Variables are useful for programs like "make", but not for a simple copy like this. 

The whole of spkg-install is a bit of a mess. It basically needs a total re-write. 

Also, there is no spkg-check file. 

Dave



---

archive/issue_comments_040817.json:
```json
{
    "body": "Ignore the comment about the wrong version of 'patch'. I somehow thought the error message was being generated during the patch, but its simply that the code does not build, which is hardly surprising, as the operating system is not tested properly. \n\nIt would make sense to default to \"generic\", which according to the makefile produces portable code. So it then has some hope of working on Android, AIX, HP-UX or any of the numerous other operating systems.",
    "created_at": "2012-01-03T23:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40817",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Ignore the comment about the wrong version of 'patch'. I somehow thought the error message was being generated during the patch, but its simply that the code does not build, which is hardly surprising, as the operating system is not tested properly. 

It would make sense to default to "generic", which according to the makefile produces portable code. So it then has some hope of working on Android, AIX, HP-UX or any of the numerous other operating systems.



---

archive/issue_comments_040818.json:
```json
{
    "body": "Changing component from interfaces to packages: optional.",
    "created_at": "2015-06-23T13:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40818",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from interfaces to packages: optional.



---

archive/issue_comments_040819.json:
```json
{
    "body": "in comment [comment:21] I forgot to put CADO-NFS so that we hit this ticket when searching\nfor CADO-NFS. This is the only purpose of this new comment.",
    "created_at": "2015-06-23T13:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40819",
    "user": "https://github.com/zimmermann6"
}
```

in comment [comment:21] I forgot to put CADO-NFS so that we hit this ticket when searching
for CADO-NFS. This is the only purpose of this new comment.



---

archive/issue_comments_040820.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-08-23T03:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40820",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_040821.json:
```json
{
    "body": "Changed to an experimental package in order to get into Sage for 64-bit systems, seems to work fine on those. Reasonably tested with good speed and documentation for main function provided, may be useful to include additional doctests.\n----\nNew commits:",
    "created_at": "2015-08-23T03:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40821",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Changed to an experimental package in order to get into Sage for 64-bit systems, seems to work fine on those. Reasonably tested with good speed and documentation for main function provided, may be useful to include additional doctests.
----
New commits:



---

archive/issue_comments_040822.json:
```json
{
    "body": "Changing component from packages: optional to packages: experimental.",
    "created_at": "2015-08-23T03:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40822",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Changing component from packages: optional to packages: experimental.



---

archive/issue_comments_040823.json:
```json
{
    "body": "I managed to build the git branch, but I failed to install the upstream package\n(renamed to msieve-1.49.tar.gz as mentioned in the description above):\n\n```\nzimmerma@barbecue:/localdisk/tmp/sage-6.7$ ./sage -i /tmp/msieve-1.49.tar.gz \nmsieve-1.49.tar.gz\n====================================================\nExtracting package /tmp/msieve-1.49.tar.gz\n-rw-r----- 1 zimmerma caramel 457682 Aug 24 14:06 /tmp/msieve-1.49.tar.gz\nFinished extraction\n/localdisk/tmp/sage-6.7/build/bin/sage-spkg: line 512: cd: msieve-1.49.tar.gz: No such file or directory\nError: after extracting, the directory msieve-1.49.tar.gz does not exist\n```\n\nWhat did I do wrong?",
    "created_at": "2015-08-24T14:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40823",
    "user": "https://github.com/zimmermann6"
}
```

I managed to build the git branch, but I failed to install the upstream package
(renamed to msieve-1.49.tar.gz as mentioned in the description above):

```
zimmerma@barbecue:/localdisk/tmp/sage-6.7$ ./sage -i /tmp/msieve-1.49.tar.gz 
msieve-1.49.tar.gz
====================================================
Extracting package /tmp/msieve-1.49.tar.gz
-rw-r----- 1 zimmerma caramel 457682 Aug 24 14:06 /tmp/msieve-1.49.tar.gz
Finished extraction
/localdisk/tmp/sage-6.7/build/bin/sage-spkg: line 512: cd: msieve-1.49.tar.gz: No such file or directory
Error: after extracting, the directory msieve-1.49.tar.gz does not exist
```

What did I do wrong?



---

archive/issue_comments_040824.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-08-24T14:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40824",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_040825.json:
```json
{
    "body": "Move msieve-1.49.tar.gz to SAGE_ROOT/upstream and then ./sage -i msieve should work.",
    "created_at": "2015-08-24T17:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40825",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Move msieve-1.49.tar.gz to SAGE_ROOT/upstream and then ./sage -i msieve should work.



---

archive/issue_comments_040826.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2015-08-24T17:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40826",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_040827.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-01-15T01:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40827",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_040828.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2020-06-19T18:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40828",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_040829.json:
```json
{
    "body": "Setting spkg proposals that have not seen recent activity to \"sage-wishlist\".",
    "created_at": "2020-06-19T18:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5310#issuecomment-40829",
    "user": "https://github.com/mkoeppe"
}
```

Setting spkg proposals that have not seen recent activity to "sage-wishlist".
