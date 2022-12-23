# Issue 7838: Remove script using ctypes from ATLAS

Issue created by migration from https://trac.sagemath.org/ticket/7838

Original creator: drkirkby

Original creation time: 2010-01-04 03:07:50

Assignee: GeorgSWeber

CC:  jsp vengoroso@gmail.com

#1497 added a few lines of code 


```/usr/bin/env
import ctypes
print str(8*ctypes.sizeof(ctypes.c_long))
```

into the ATLAS build process, which reports the number of bits Sage was compiled as. It makes use of the module 'ctypes' in Python, but 

http://docs.activestate.com/activepython/2.5/whatsincluded.html

shows that ctypes is seriouly on many platforms, including

 * Older linux-x86 - build failures
 * aix-powerpc	build failures
 * linux-ia64	build failures
 * solaris-sparc build failures
 * solaris-x86	build failures
 * hpux-parisc	libffi not ported to PA-RISC arch
 * hpux-ia64	build failures
 * win64	

Hence the code needs replacing with something less broken

Dave


---

Comment by drkirkby created at 2010-01-04 03:37:40

Changing keywords from "" to "ctypes atlas".


---

Comment by drkirkby created at 2010-01-05 00:53:53

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-01-05 00:53:53

See: 

http://boxen.math.washington.edu/home/kirkby/portability/atlas-3.8.3.p10/

for an updated version of ATLAS which fixes this issue. bitwidth.py has been changed. 

The 4/5 lines of code I used were posted on sage-devel by  vengoroso`@`gmail.com but I don't know his fully name, so can't give full credit. Please let us know your full name! 

Note however, for me at least, ATLAS does not build fully, but at least it gets further than it did on Open Solaris. 

Dave


---

Comment by jsp created at 2010-01-05 14:09:57

The fix looks good.

My setup is clearly not ok. The build failed at the end:


```
ATLAS install complete.  Examine 
ATLAS/bin/<arch>/INSTALL_LOG/SUMMARY.LOG for details.
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build'
make clean
make[1]: Entering directory `/export/home/jaap/Downloads/sage-4.3.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build'
rm -f *.o x* config?.out *core*
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build'
Finished building ATLAS core
The Makefile generated in ATLAS for building shared libraries
assumes the linker is the GNU linker, which it not true in
your setup. (It is generally considered better to use the
Sun linker in /usr/ccs/bin rather than the GNU linker from binutils)
The linker flags in /export/home/jaap/Downloads/sage-4.3.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build/lib/Makefile will be changed. 
'-shared' will be changed to '-G'
'-soname' will be changed to '-h'
'--whole-archive' will be changed to '-zallextract'
'--no-whole-archive' will be changed to '-zdefaultextract'
A copy of the original Makefile will be copied to Makefile.orig
rm -f libatlas.so liblapack.so
make libatlas.so liblapack.so libf77blas.so libcblas.so liblapack.so
make[1]: Entering directory `/export/home/jaap/Downloads/sage-4.3.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build/lib'
ld -melf_x86_64 -G -h libatlas.so -o libatlas.so \
        -z allextract libatlas.a -z defaultextract -lc -lm
ld: warning: file libatlas.a(ATL_flushcache.o): wrong ELF class: ELFCLASS64
ld: fatal: entry point symbol `lf_x86_64' is undefined
make[1]: *** [libatlas.so] Error 1
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build/lib'
make: *** [shared] Error 2
Building shared ATLAS libraries failed
Failed to build ATLAS.

real	155m22.653s
user	147m22.502s
sys	6m4.162s
sage: An error occurred while installing atlas-3.8.3.p10

```


Maybe I should use gcc gcc-4.4.2 with the gnu loader?

Jaap


---

Comment by was created at 2010-01-05 14:19:47


```
Javier Lopez
 to wstein
	
show details 4:39 AM (1 hour ago)
	
Hi William,

reply here since I've got no trac account. My full name is Javier
López Peña, but no credit is needed for such a small contribution.

Cheers
J
```



---

Comment by jsp created at 2010-01-12 14:45:34

The patch works ok. Positive review.

Removed cwitty from the cc list.

And Javier from the authors list (see comment above).

Jaap


---

Comment by jsp created at 2010-01-12 14:45:34

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-14 02:35:54

Resolution: fixed
