# Issue 7062: ECL snapshot of 13th Sept 2009 fails with Sun Studio 12.1

Issue created by migration from https://trac.sagemath.org/ticket/7062

Original creator: drkirkby

Original creation time: 2009-09-29 04:26:10

Assignee: tbd

I tried to build the file ecl-9.8.4-20090913cvs.p1 in Sage sage-4.1.2.alpha4, but it fails with a message that the compiler needs to be c99 compliant. I think the author of ECL has now fixed that, so there is no such requirement, but no stable release has been made since he made the fix. 

I added a few lines to spkg-install, to force the compiler option -xc99, but whilst the build of ECL got a lot further, it failed with:


```
if test -f ../CROSS-DPP ; then ../CROSS-DPP /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/reference.d tm p.c ; else ./dpp /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/reference.d tmp.c ; fi
dpp: /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/reference.d -> tmp.c
/opt/xxxsunstudio12.1/bin/cc -DECLDIR="\"/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib/ecl-9.8.4\"" -I. -I/export/home/drkirkby/sage/sage-4. 1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/build -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c  -I../ecl/gc -DECL_API -DECL_NO_LEGACY -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -O2 -m64 -g -xc99 -fPIC -O2 -m64 -g -xc99 -fPIC - Dsun4sol2 -c  -o reference.o tmp.c
rm -f tmp.c
if test -f ../CROSS-DPP ; then ../CROSS-DPP /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/character.d tm p.c ; else ./dpp /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/character.d tmp.c ; fi
dpp: /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/character.d -> tmp.c
/opt/xxxsunstudio12.1/bin/cc -DECLDIR="\"/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib/ecl-9.8.4\"" -I. -I/export/home/drkirkby/sage/sage-4. 1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/build -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c  -I../ecl/gc -DECL_API -DECL_NO_LEGACY -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -O2 -m64 -g -xc99 -fPIC -O2 -m64 -g -xc99 -fPIC - Dsun4sol2 -c  -o character.o tmp.c
rm -f tmp.c
if test -f ../CROSS-DPP ; then ../CROSS-DPP /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/file.d tmp.c ;  else ./dpp /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/file.d tmp.c ; fi
dpp: /export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/file.d -> tmp.c
/opt/xxxsunstudio12.1/bin/cc -DECLDIR="\"/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib/ecl-9.8.4\"" -I. -I/export/home/drkirkby/sage/sage-4. 1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/build -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c  -I../ecl/gc -DECL_API -DECL_NO_LEGACY -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -O2 -m64 -g -xc99 -fPIC -O2 -m64 -g -xc99 -fPIC - Dsun4sol2 -c  -o file.o tmp.c
"/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/file.d", line 4019: void function cannot return value
"/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/file.d", line 4402: warning: statement not reached
"/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/file.d", line 4722: warning: statement not reached
"/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/file.d", line 4738: warning: shift count negative or too big: >>= 64
"/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/src/c/file.d", line 4769: warning: shift count negative or too big: <<= 64
cc: acomp failed for tmp.c
make[4]: *** [file.o] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/build/c'
make[3]: *** [libeclmin.a] Error 2
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src/build'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/ecl-9.8.4-20090913cvs.p2/src'
Failed to build ECL ... exiting

```



---

Comment by drkirkby created at 2009-09-30 06:02:02

Juanjo, 
the main author of ECL, has advised me this has been fixed in the ECL CVS. However, I will not at this point attempt to make a new package for Sage until there is a new stable release or ECL. 

david Kirkby


---

Comment by drkirkby created at 2011-04-02 13:02:48

This can be closed as fixed by #7393 in sage-4.2.1.alpha0


---

Comment by jdemeyer created at 2011-04-05 15:54:54

Resolution: duplicate
