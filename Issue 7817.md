# Issue 7817: opencdk ignoring SAGE64 except on OS X

Issue created by migration from https://trac.sagemath.org/ticket/7817

Original creator: drkirkby

Original creation time: 2010-01-02 08:49:26

Assignee: drkirkby

Like many packages, opencdk has code which adds -m64 on OS X if SAGE64 is set to yes. It is being ignored on other platforms, with the result the build fails - see below. 


```
/home/drkirkby/sage-4.3/local/lib/libgcrypt.so /export/home/drkirkby/sage-4.3/local/lib/libgpg-error.so -lz -lc 
ld: fatal: file /export/home/drkirkby/sage-4.3/local/lib/libgcrypt.so: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to .libs/libopencdk.so.10.0.6
collect2: ld returned 1 exit status
make[4]: *** [libopencdk.la] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/opencdk-0.6.6.p2/src'
Failed to build OpenCDK
```





---

Comment by drkirkby created at 2010-01-02 09:13:07

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-02 09:13:07

I've updated spkg-install so SAGE64 is used on any platform. 

Changes have been checked in. 

http://boxen.math.washington.edu/home/kirkby/portability/opencdk-0.6.6.p3/


---

Comment by jsp created at 2010-01-02 18:19:37

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-02 18:19:37

Looks good to me. Tested it on Open Solaris and Fedora 11 and 12.

So positive review.

Jaap


---

Comment by mhansen created at 2010-01-04 03:42:29

Resolution: fixed
