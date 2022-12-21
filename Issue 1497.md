# Issue 1497: atlas-3.8.p4.spkg fails to build on Intel Core 2 Duo with 32-bit operating system

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-13 23:24:11

Assignee: was

I run 32-bit Debian on my Core 2 Duo box.  ATLAS detects the Core 2 Duo and attempts to do a 64-bit build, which fails with errors like this:

```
cd /home/cwitty/sage-2.9.alpha6/spkg/build/atlas-3.8.p4/ATLAS-build ; ./xprobe_comp -v 0 -o atlconf.txt -O 1 -A 15 -Si nof77 0  -Fa ic '-fPIC' -Fa sm '-fPIC' -Fa dm '-fPIC' -Fa sk '-fPIC' -Fa dk '-fPIC' -Fa xc '-fPIC' -C if '/home/cwitty/sage-2.9.alpha6/local/bin/sage_fortran' -Fa if '-fPIC'  -b 64 > config1.out
/usr/bin/ld: skipping incompatible /usr/lib/gcc/i486-linux-gnu/4.2.3/libgcc.a when searching for -lgcc
/usr/bin/ld: skipping incompatible /usr/lib/gcc/i486-linux-gnu/4.2.3/libgcc.a when searching for -lgcc
/usr/bin/ld: cannot find -lgcc
collect2: ld returned 1 exit status
make[4]: *** [IRunCComp] Error 1
/usr/bin/ld: skipping incompatible /usr/lib/gcc/i486-linux-gnu/4.2.3/libgcc.a when searching for -lgcc
/usr/bin/ld: skipping incompatible /usr/lib/gcc/i486-linux-gnu/4.2.3/libgcc.a when searching for -lgcc
/usr/bin/ld: cannot find -lgcc
collect2: ld returned 1 exit status
make[4]: *** [IRunCComp] Error 1


Unable to find usable compiler for ICC; abortingMake sure compilers are in your path, and specify good compilers to configure
(see INSTALL.txt or 'configure --help' for details)
```

(Note the "-b 64" at the beginning of the above, which means to do a 64-bit build.)

Adding "-b 32" to the configure line in spkg-install allows the build to proceed.


---

Comment by jkantor created at 2007-12-14 02:41:26

This spkg

http://sage.math.washington.edu/home/jkantor/spkgs/atlas-3.8.p5.spkg

checks sizeof(long) (using ctypes) and infers whether the system is 32 or 64 bit.


---

Comment by mabshoff created at 2007-12-14 04:09:28

Resolution: fixed


---

Comment by mabshoff created at 2007-12-14 04:09:28

Merged in 2.9.alpha7.
