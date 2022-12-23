# Issue 7057: cliquer-1.2 ignores CC and uses gcc instead of Sun compiler.

Issue created by migration from https://trac.sagemath.org/ticket/7057

Original creator: drkirkby

Original creation time: 2009-09-28 21:11:04

Assignee: tbd

cliquer seems one seriously messed up package! Under some circumstances (see #6852) it can fail to build as it can't find the Sun C compiler cc. On other occasions, it can build with gcc, even though CC is set to the Sun compiler. 

In the example below, CC was set to the Sun compiler, but cliquer uses gcc instead!


```
cliquer-1.2/.hg/undo.dirstate
cliquer-1.2/SConstruct
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
gcc -o src/cl.pic.o -c -fPIC src/cl.c
gcc -o src/cliquer.pic.o -c -fPIC src/cliquer.c
gcc -o src/graph.pic.o -c -fPIC src/graph.c
gcc -o src/reorder.pic.o -c -fPIC src/reorder.c
gcc -G -o libcliquer.so src/cl.pic.o src/cliquer.pic.o src/graph.pic.o src/reorder.pic.o
Install file: "libcliquer.so" as "Build/libcliquer.so"
scons: done building targets.

real    0m7.963s
user    0m5.668s
sys     0m1.410s
Successfully installed cliquer-1.2
```



---

Comment by mvngu created at 2009-09-29 17:00:14

That's because cliquer-1.2.spkg is using SCons. The package cliquer-1.2.p0.spkg at #6681 doesn't use SCons at all.


---

Comment by mhansen created at 2009-10-20 13:54:11

Resolution: invalid
