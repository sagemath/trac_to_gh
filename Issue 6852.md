# Issue 6852: cliquer-1.2 fails to build as it cant find Sun compiler (SCons issue)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-31 14:34:53

Assignee: tbd

Keywords: solaris SCons

Yet one more issue that arrises on Solaris with SCons. This is on an old Sun Ultra 80, 4 x 450 MHz, 4 GB RAM, running the very first release of Solaris 10 (03/2005).  

Sage 4.1.1

This is fresh install of Solaris 10. There is nothing added to this - no new gcc, no Sun Studio. It set the machine up specifically to help test Sage and ECL on Solaris 03/2005. 


```

x cliquer-1.2/.hg/00changelog.i, 57 bytes, 1 tape blocks
x cliquer-1.2/.hg/requires, 23 bytes, 1 tape blocks
x cliquer-1.2/.hg/undo.branch, 7 bytes, 1 tape blocks
x cliquer-1.2/.hg/dirstate, 147 bytes, 1 tape blocks
x cliquer-1.2/.hg/undo.dirstate, 147 bytes, 1 tape blocks
x cliquer-1.2/SConstruct, 301 bytes, 1 tape blocks
Finished extraction
****************************************************
Host system
uname -a:
SunOS goose 5.10 Generic sun4u sparc SUNW,Ultra-80
****************************************************
****************************************************
CC Version
/usr/sfw/bin/gcc -v
Reading specs from /usr/sfw/lib/gcc/sparc-sun-solaris2.10/3.4.3/specs
Configured with: /gates/sfw10/builds/sfw10-gate/usr/src/cmd/gcc/gcc-3.4.3/configure --prefix=/usr/sfw --with-as=/usr/sfw/bin/gas --with-gnu-as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++ --enable-shared
Thread model: posix
gcc version 3.4.3 (csl-sol210-3_4-branch+sol_rpath)
****************************************************
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
cc -o src/so_cl.o -c -KPIC src/cl.c
sh: cc: not found
scons: *** [src/so_cl.o] Error 1
scons: building terminated because of errors.

real    0m11.561s
user    0m9.580s
sys     0m1.532s
sage: An error occurred while installing cliquer-1.2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /export/home/drkirkby/sage-4.1.1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/export/home/drkirkby/sage-4.1.1/spkg/build/cliquer-1.2 and type 'make'.
Instead type "/export/home/drkirkby/sage-4.1.1/sage -sh"
in order to set all environment variables correctly, then cd to
/export/home/drkirkby/sage-4.1.1/spkg/build/cliquer-1.2
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/cliquer-1.2] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.1.1/spkg'

real    23m21.646s
user    18m45.421s
sys     4m33.002s
Error building Sage.
$ echo $CC
/usr/sfw/bin/gcc
$

```




---

Comment by mhansen created at 2009-10-20 13:54:46

Resolution: invalid
