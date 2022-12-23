# Issue 9397: Resolve corrupted patches to permit Singular to build on Solaris x86/x64

Issue created by migration from https://trac.sagemath.org/ticket/9397

Original creator: drkirkby

Original creation time: 2010-06-30 18:02:47

Assignee: GeorgSWeber

Singular will not build on Solaris or OpenSolaris with x86/x64 processors, nor will it build 64-bit Solaris x64 with SPARC processors.

There are two different reasons for the two different problems, but they are both addressed by this patch. 

## Problem No. 1 Poor patching practice prevents Solaris or OpenSolaris x86/x64 builds

The first only affects x86/x64 hardware. The second affects 

One patch added the following few lines to a file 

```
ifeq ($(SINGUNAME),ix86-SunOS)
SO_SUFFIX  = so
LIBSINGULAR_FLAGS = -shared
LIBSINGULAR_LIBS = -lsingfac -lsingcf -lntl -lreadline -lgmp lomalloc
endif
}}} 

but those changes subsequently got overwritten by a latter patch. An inspection of spkg-install in Singular shows the file `src/Singular/Makefile.in` being overwritten twice. See below. 

{{{
patch()
{
    # work-around patches
    cp patches/mminit.cc src/kernel/
    cp patches/assert.h src/factory/
    cp patches/kernel.rmodulon.cc src/kernel/rmodulon.cc
    cp patches/src.Singular.Makefile.in src/Singular/Makefile.in # FIRST
    cp patches/Singular.libsingular.h src/Singular/libsingular.h
    cp patches/factory.GNUmakefile.in src/factory/GNUmakefile.in
    cp patches/libfac.charset.alg_factor.cc src/libfac/charset/alg_factor.cc
    cp patches/kernel.Makefile.in src/kernel/Makefile.in
    cp patches/Singular.Makefile.in src/Singular/Makefile.in # OVERWRITES FIRST
    cp patches/Singular.tesths.cc src/Singular/tesths.cc

    if [ "$UNAME" = "CYGWIN" ]; then
        # Fine to make this patch on any system, because it is code that is only compiled on Windows.
        cp patches/sing_win.cc src/Singular/
        cp patches/IntegerProgramming-Makefile.in src/IntegerProgramming/Makefile.in
    fi

    #cp patches/Singular.configure src/Singular/configure
    #cp patches/Singular.configure.in src/Singular/configure.in
}
}}}

Removing the target `ix86-SunOS` would stop any build on Solaris or !OpenSolaris with x86/x64 hardware, but would not affect SPARC builds at all. 

## Problem No. 2 Compiler flag -m64 not propagating properly throughout the Singular build process

dding the compiler flag -m64 was not sufficient to permit Singular to build fully 64-bit, as part of it failed with:
{{{
make[1]: Entering directory 
`/export/home/drkirkby/clean/sage-4.5.alpha0/spkg/build/singular-3.1.0.4.p8/src/Singular'
g++ -O2 -g -m64 -fPIC -pipe -I. -I../kernel 
-I/export/home/drkirkby/clean/sage-4.5.alpha0/local/include 
-I/export/home/drkirkby/clean/sage-4.5.alpha0/local/include 
-I/export/home/drkirkby/clean/sage-4.5.alpha0/local/include -O2 -g -m64 
-fno-implicit-templates -DNDEBUG -DOM_NDEBUG -Dix86_SunOS -DHAVE_CONFIG_H 
-DLIBSINGULAR \
	   -o libsingular-tesths.o \
           -c tesths.cc
g++   -o libsingular.so \
	libsingular-tesths.o iparith.o mpsr_Tok.o claptmpl.o \
	grammar.o scanner.o attrib.o eigenval_ip.o extra.o fehelp.o feOpt.o 
ipassign.o 
ipconv.o ipid.o iplib.o ipprint.o ipshell.o lists.o sdb.o fglm.o 
interpolation.o 
silink.o subexpr.o janet.o wrapper.o libparse.o sing_win.o gms.o pcv.o 
maps_ip.o 
walk.o walk_ip.o cntrlc.o misc.o calcSVD.o  slInit_Static.o mpsr_Put.o 
mpsr_PutPoly.o mpsr_GetPoly.o mpsr_sl.o mpsr_Get.o mpsr_GetMisc.o mpsr_Error.o 
ndbm.o sing_dbm.o -lkernel -L../kernel -L../factory -L../libfac 
-L/export/home/drkirkby/clean/sage-4.5.alpha0/local/lib -lsingfac -lsingcf -
lntl 
-lreadline -lgmp -lomalloc
ld: fatal: file libsingular-tesths.o: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to libsingular.so
}}}

Note how the first line has the -m64 flag, but the second line does not - this is despite -m64 being in both CFLAGS and CXXFLAGS. I discovered that using 

 {{{
CC="gcc -m64"
CXX="g++ -m64"
export CC
export CXX
 }}}

solved the problem. After sending this to the Singular mailing list, I got a response from Hans Schoenemann, one of the developers saying "That's the right way."



Hence the patch which will be attached later does two things. 
 * Resolves the mess created by two patches patching the same file. 
 * Ensure the compilers really are called with the -m64 flag.


---

Attachment

Compressed build log on a 64-bit SPARC running Solaris 10, with Sage built 64-bit


---

Comment by drkirkby created at 2010-06-30 21:45:16

Compressed build log on a 64-bit SPARC running Solaris 10, with Sage built 32-bit


---

Attachment

Compressed build log on a MacPro 1 running OS X 10.6.4. Default 64-bit build


---

Attachment

Compressed build log on a Sun Fire X4450 server running Ubuntu 8.04.4 Linux


---

Attachment

Compressed build log on a Sun Ultra 27 (Xeon processor) running Solaris 10 06/2009. SAGE64=yes, so a 64-bit build


---

Attachment

Mercurial patch to sort out the mess of the Singular patches overwriting patches


---

Comment by drkirkby created at 2010-06-30 21:58:26

I've made the changes and tested this on a number of systems. On the Sun Blade 1000 running Solaris 10, it has been tested as both the default 32-bit build, but also as a 64-bit build. 

The build logs attached show this working on
 * Linux (sage.math) Default 64-bit build
 * OS X (bsd.math) Default 64-bit build
 * OpenSolaris 06/2009 on an Intel Xeon processors. Forced a 64-bit build 
 * Solaris 10. SPARC processor. Default 32-bit build
 * Solaris 10. SPARC processor. Forced a 64-bit build with SAGE64=yes

The package may be found at 

http://boxen.math.washington.edu/home/kirkby/patches/singular-3.1.0.4.p8.spkg

Dave


---

Comment by drkirkby created at 2010-06-30 21:58:26

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-07-24 23:15:53

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-07-24 23:15:53

This should now be fixed when a later Singular is committed, which already has positive review at #8059. So I'm setting this back to 'needs info' to save someone a wasted effort in reviewing this. 

## Note to the release manager
This ticket can be closed when the updated Singular at #8059 is merged. 

Dave


---

Comment by jhpalmieri created at 2010-08-03 03:23:11

For what it's worth, this has worked successfully on every Solaris machine I've tried it on, and it's worked where the previous version of singular didn't.  (I haven't used the spkg from #8059 because this also requires a change to the Sage library.)  I haven't tested this one very systematically, and I haven't tested it at all on non-Solaris machines.  But if there isn't movement on #8059, this one might be ready to go instead.


---

Comment by drkirkby created at 2010-08-03 04:15:52

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-08-03 04:15:52

I'm going to put this back to needs review. 

I think this is only going to have an effect when SAGE64 is yes. The big patch I removed, which added Solaris x86 support, was not doing anything since a later patch had overwritten it. 

So I think this is pretty safe. I tested it on OS X and Unbunta, and have attached the logs of it building on there.


---

Comment by drkirkby created at 2010-08-03 04:19:08

I should have perhaps clarified something here. Although I wrote 9 days ago that #8059 had positive review, that has now been removed, as it was causing problems. 

So this is now up for review. 

Dave


---

Comment by jhpalmieri created at 2010-08-16 21:49:27

Since #8059 has been merged, I think this can be closed now.  Or do you want to wait until 4.5.3 is officially released, not just in alpha versions?


---

Comment by drkirkby created at 2010-08-16 22:14:22

I think we should wait, just in case there are big problems and Singular gets backed out. I doubt it will happen, but because it used a lot, it's difficult to predict what problems it might cause. 

Dave


---

Comment by drkirkby created at 2010-09-13 08:58:38

Resolution: fixed


---

Comment by drkirkby created at 2010-09-13 08:58:38

This problem was fixed by #8059  which was merged in sage 4.5.3.alpha1.
