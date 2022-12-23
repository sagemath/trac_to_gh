# Issue 8089: ecl 9.10.2-20091105cvs.p1 faiils to build on Open Solaris x64

Issue created by migration from https://trac.sagemath.org/ticket/8089

Original creator: drkirkby

Original creation time: 2010-01-27 04:21:05

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




---

Comment by drkirkby created at 2010-05-31 00:34:54

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-05-31 00:34:54

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

Attachment

Mercurial patch to disable assembly code on OpenSolaris x64


---

Comment by drkirkby created at 2010-05-31 02:43:08

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-05-31 02:43:08

This needs to be closed, not reviewed. I realised I have already got positive review for a later version of ECL, which dod not need this fix  - see #8951.


---

Comment by drkirkby created at 2010-06-12 21:20:50

Resolution: fixed


---

Comment by drkirkby created at 2010-06-18 11:53:37

I was wrong to close this, as the issues are not incorporated in the 10.4.1 package. I'm reopening this.


---

Comment by drkirkby created at 2010-06-18 11:53:37

Changing status from closed to new.


---

Comment by drkirkby created at 2010-06-18 11:53:37

Resolution changed from fixed to 


---

Comment by drkirkby created at 2010-06-21 09:03:12

#9264 Solves this issue, and several others related to ECL, so when #9264 is merged (it already has positive review), this issue will be resolved anyway. 

Dave


---

Comment by rlm created at 2010-06-25 11:20:22

Resolution: duplicate
