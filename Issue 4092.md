# Issue 4092: libm4ri-20080904 fails to build on OSX 10.4

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-09 18:52:10

Assignee: malb

CC:  anakha

I thought we fixed that:

```
checking for a BSD-compatible install... /usr/bin/install -c 
checking mm_malloc.h usability... no 
checking mm_malloc.h presence... no 
checking for mm_malloc.h... no 
checking for a sed that does not truncate output... /usr/bin/sed 
checking the number of available CPUs... 1 
checking the number of available CPUs... 1 
checking for x86 cpuid 0x0 output... unknown 
checking for the processor vendor... Unknown 
262144 
32768 
second level name l1cachesize in hw.l1cachesize is invalid 
second level name l1cachesize in hw.l1cachesize is invalid 
./configure: line 21633: / 1024: syntax error: operand expected (error 
token is "/ 1024") 
Error configuring libm4ri 
```


Malb: any chance we missed a patch that did not make it in?


---

Comment by malb created at 2008-09-09 18:59:40

I thought so too and it was confirmed over at #4059. Adding anakha (the author of the fixes of #4059) as CC.


---

Comment by malb created at 2008-09-09 19:02:35

a autoconf call was missing


---

Comment by malb created at 2008-09-09 19:06:44

New spkg at

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20080909.spkg


---

Comment by anakha created at 2008-09-09 19:29:55

You did miss the v4 patch over at #4059 if this shows up now.  The posted package does integrate it so everything should be alright.  

I can't test it myself, since I don't have any machines with 10.4 though.


---

Comment by mabshoff created at 2008-09-09 19:32:24

It works for me now on a Dual G5 OSX 10.4 box:

```
checking for a sed that does not truncate output... /usr/bin/sed
checking the number of available CPUs... 2 
checking the number of available CPUs... 2 
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
checking the L1 cache size... 32768 Bytes
checking the L2 cache size... 524288 Bytes
checking whether make sets $(MAKE)... (cached) yes
configure: creating ./config.status
```


I will do some build testing on other machines before giving this a positive review :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-10 02:43:26

Builds fine on 

 * Linux x86, x86-64, Itanium
 * Solaris 
 * OSX 10.5 Intel and OSX 10.4 PPC

So: positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-10 02:47:28

Resolution: fixed


---

Comment by mabshoff created at 2008-09-10 02:47:28

Merged in Sage 3.1.2.rc2
