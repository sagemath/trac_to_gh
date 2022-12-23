# Issue 1591: cygwin -- immediately terminate the build

Issue created by migration from https://trac.sagemath.org/ticket/1591

Original creator: was

Original creation time: 2007-12-23 14:45:49

Assignee: mabshoff

I thought we already wrote code so building sage on cygwin would *immediately* terminate the build with a "it won't work" error.  Same with gcc <= 3.3.  But
we keep getting emails like this on sage-support:

```
I just downloaded sage 2.9 source code tar from http://www.sagemath.org/dist/src/index.html

did tar xvf on it, then did make.

I get this build error below.
I am using cygwin

$ uname -a
CYGWIN_NT-5.1 computer-h20djr 1.5.24(0.156/4/2) 2007-01-31 10:57 i686
Cygwin

$ gcc -v
gcc version 3.4.4 (cygming special, gdc 0.12, using dmd 0.125)

$ python -v
Python 2.5 (r25:51908, Mar 13 2007, 08:13:14)
[GCC 3.4.4 (cygming special, gdc 0.12, using dmd 0.125)] on cygwin

---- part of log file where error occured ---------

 gcc -c -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMP -I.. -
DOPERATION_dive_1
-m32 -O2 -fomit-frame-pointer -mtune=pentium3 -march=pentium3 tmp-
dive_1.s -DPIC
 -o .libs/dive_1.o
/usr/lib/gcc/i686-pc-cygwin/3.4.4/../../../../i686-pc-cygwin/bin/as:
BFD 2.17.50
 20060817 assertion fail /netrel/src/binutils-20060817-1/bfd/coff-
i386.c:576
tmp-dive_1.s: Assembler messages:
tmp-dive_1.s:110: Error: cannot represent relocation type
BFD_RELOC_386_GOTPC
make[4]: *** [dive_1.lo] Error 1
make[4]: Leaving directory `/cygdrive/e/nabbasi/data/CDROM/DVD11/SAGE/
sage-2.9/s
pkg/build/gmp-4.2.1.p12/src/mpn'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/cygdrive/e/nabbasi/data/CDROM/DVD11/SAGE/
sage-2.9/s
pkg/build/gmp-4.2.1.p12/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/cygdrive/e/nabbasi/data/CDROM/DVD11/SAGE/
sage-2.9/s
pkg/build/gmp-4.2.1.p12/src'
Error building GMP.

real    1m47.938s
user    4m16.002s
sys     1m1.670s
sage: An error occurred while installing gmp-4.2.1.p12
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /cygdrive/e/nabbasi/data/CDROM/DVD11/SAGE/sage-2.9/install.log.
Describe you
r computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/cygdrive/e/nabbasi/data/CDROM/DVD11/SAGE/sage-2.9/spkg/build/
gmp-4.2.1.p12 and
type 'make'.
Instead type "/cygdrive/e/nabbasi/data/CDROM/DVD11/SAGE/sage-2.9/sage -
sh"
in order to set all environment variables correctly, then cd to
/cygdrive/e/nabbasi/data/CDROM/DVD11/SAGE/sage-2.9/spkg/build/
gmp-4.2.1.p12
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/gmp-4.2.1.p12] Error 1
make[1]: Leaving directory `/cygdrive/e/nabbasi/data/CDROM/DVD11/SAGE/
sage-2.9/s
pkg'

real    2m4.192s
user    4m25.386s
sys     1m4.705s


Nasser

```



---

Comment by was created at 2007-12-27 06:52:25

From Mabshoff:

```
> I've created ticket #1591 to address this sort of thing happening:
>
>    http://trac.sagemath.org/sage_trac/ticket/1591
>
> I'm actually surprised, since I thought we already wrote code to prevent it.

I just tested and Sage prints a message informing the user that it
isn't supported, but then goes on happily :)
```



---

Comment by mabshoff created at 2007-12-30 19:45:04

Even if we terminate the build by default I would really like to bypass this by setting some magic env-variable to keep the port alive. The same should happen on Solaris.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-03 15:21:21

Resolution: fixed


---

Comment by mabshoff created at 2008-01-03 15:21:21

I added the following to `spkg/base/prereq-0.3-install`:

```
if [ "$SAGE_PORT" = "" ]; then
   if [ `uname | sed -e 's/WIN.\+/WIN/'` = "CYGWIN" ]; then
      echo "Building or using SAGE with Cygwin is absolutely definitely"
      echo "not supported, and will definitely not work.  The only way"
      echo "to run SAGE on Windows, is via VMware (or Virtual PC or "
      echo "some other virtualization system such as andLinux)."
      echo "NOTE: SAGE used to support Cygwin several months ago (around March"
      echo "2007), so you may have seen some old documentation about this."
      exit -1
   fi
   if [ `uname` = "SunOS" ]; then
      echo "Building or using Sage on Solaris is tricky and not supported"
      echo "at the moment. It is possible, but you should be well aware that"
      echo "some things do not work. To get past this message export the"
      echo "variable \$SAGE_PORT to something non-empty. Support for Solaris"
      echo "is actively being worked on."
      exit -1
   fi
fi
```

The first check, i.e. the Cygwin one was already there, but was missing the `exit -1`.

Cheers,

Michael
