# Issue 6246: SAGE_FAT_BINARY still doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/6246

Original creator: was

Original creation time: 2009-06-08 12:23:03

Assignee: tbd

I built a Sage-4.0.1 on sage.math (a 32-bit vmware machine actually) using the SAGE_FAT_BINARY environment variable.  This set MPIR's --enable-fat option (or should have!).    I then dropped the binary on cicero (on skynet), and it does *NOT* work at all.   The problem is definitely still MPIR.  This will have to get fixed soon.
At least this nails down that MPIR is the problem, and gives me a straightforward testcase. 


```
[wstein@cicero sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
The SAGE install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH (please wait at
most a few minutes)...
Do not interrupt this.
/home/wstein/tmp/sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux/local/bin/sage-sage: line 198: 27278 Illegal instruction     sage-ipython "$@" -i
[wstein@cicero sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux]$ ./sage -gdb
----------------------------------------------------------------------
----------------------------------------------------------------------
/home/wstein/tmp/sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux/local/bin/sage-ipython
GNU gdb Fedora (6.8-23.fc9)
Copyright (C) 2008 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i386-redhat-linux-gnu"...
[Thread debugging using libthread_db enabled]
Python 2.5.4 (r254:67916, Jun  6 2009, 05:52:22) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
[New Thread 0xb80b66c0 (LWP 27306)]
| Sage Version 4.0.1, Release Date: 2009-06-06                       |
| Type notebook() for the GUI, and license() for information.        |
| Sage Version 4.0.1, Release Date: 2009-06-06                       |
| Type notebook() for the GUI, and license() for information.        |
Program received signal SIGILL, Illegal instruction.
0x0018f1c9 in __gmpz_set_str () from /home/wstein/tmp/sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux/local/lib/libgmp.so.3
Missing separate debuginfos, use: debuginfo-install glibc.i686
(gdb) bt
#0  0x0018f1c9 in __gmpz_set_str () from /home/wstein/tmp/sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux/local/lib/libgmp.so.3
#1  0x006095d3 in initinteger () at sage/rings/integer.c:30705
#2  0x080e020c in _PyImport_LoadDynamicModule (name=0xbfaabba7 "sage.rings.integer", 
    pathname=0xbfaaab33 "/home/wstein/tmp/sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux/local/lib/python2.5/site-packages/sage/rings/integer.so", fp=0x89ae5e8)
    at ./Python/importdl.c:53
#3  0x080de075 in load_module (name=0xbfaabba7 "sage.rings.integer", fp=0x32, 
    buf=0xbfaaab33 "/home/wstein/tmp/sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux/local/lib/python2.5/site-packages/sage/rings/integer.so", type=3, loader=0xe)
    at Python/import.c:1758
#4  0x080de2f9 in import_submodule (mod=0xb7b581f4, subname=0xbfaabbb2 "integer", fullname=0xbfaabba7 "sage.rings.integer") at Python/import.c:2400
#5  0x080de7d4 in load_next (mod=0xb7b581f4, altmod=0xb7b581f4, p_name=<value optimized out>, buf=0xbfaabba7 "sage.rings.integer", p_buflen=0xbfaacba8) at Python/import.c:2220
#6  0x080dea20 in import_module_level (name=0x0, globals=<value optimized out>, locals=<value optimized out>, fromlist=0xb8084c6c, level=-1) at Python/import.c:2008
```


I then rebuilt MPIR with "sage -f mpir-1.2.p2" and Sage starts up.  But then it *does* die on use of ATLAS:

```
Making script relocatable
Finished installing mpir-1.2.p2.spkg
[wstein@cicero sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 
sage: 
sage: 
sage: 
Exiting SAGE (CPU time 0m0.09s, Wall time 0m11.48s).
Exiting spawned Gap process.
[wstein@cicero sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux]$ 
[wstein@cicero sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = random_matrix(ZZ,150)
sage: time a.det()
/home/wstein/tmp/sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux/local/bin/sage-sage: line 198: 17808 Illegal instruction     sage-ipython "$@" -i
[wstein@cicero sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux]$ cat /proc/cpuinfo 
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 15
model           : 2
model name      : Intel(R) Pentium(R) 4 CPU 2.66GHz
stepping        : 7
cpu MHz         : 2666.188
cache size      : 512 KB
fdiv_bug        : no
hlt_bug         : no
f00f_bug        : no
coma_bug        : no
fpu             : yes
fpu_exception   : yes
cpuid level     : 2
wp              : yes
flags           : fpu vme de pse tsc msr pae mce cx8 apic mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe up pebs bts
bogomips        : 5332.37
clflush size    : 64
power management:
| Sage Version 4.0.1, Release Date: 2009-06-06                       |
| Type notebook() for the GUI, and license() for information.        |
| Sage Version 4.0.1, Release Date: 2009-06-06                       |
| Type notebook() for the GUI, and license() for information.        |
[wstein@cicero sage-4.0.1-linux-Debian_GNU_Linux_4.0_etch-sse2-i686-Linux]$ 
```


So I think all the "SAGE_FAT_BINARY" stuff -- the atlas only using sse2, the MPIR building FAT -- absolutely none of it works at all. 
But again, now that there is a good test system in place (build on sage.math, test on cicero), this will be fixable. 


---

Comment by was created at 2009-07-07 03:25:25

Here's a plan:

```

Fixing this is on the todo list, and I hope it happens for sage-4.1.1.  Mostly atlas and mpir are the only two packages that "cause trouble", though I'm not convinced of that -- I tried building a binary on sage.math (on a 32-bit vmware machine), then putting it on an *old* Pentium withouts ssse3 pni, and it of course wouldn't start.  Then I rebuilt atlas and mpir, and it seemed to work fine.  I then ran the test suite, which did *not* come close to passing -- so other things evidently fail.  If anybody wants to help with this, the plan is the following.

1. Fix the atlas and mpir spkg's so they definitely support the SAGE_FAT_BINARY environment variable (this might be the case already).

2. Build sage binary using the SAGE_FAT_BINARY variable set on a modern 32-bit linux box.

3. Move that binary to an old 32-bit linux box.

4. Try it out -- if it fails to start then the SAGE_FAT_BINARY flag doesn't work.   Go to 1.

5. If Sage starts, try "random_matrix(ZZ,300).det()", which will test ATLAS.  If this fails, go to 1.

6. Run the full Sage test suite.  Inspect and see what is still built using ssse3/pni, etc.  Go to 1.

 -- William
```



---

Comment by was created at 2009-08-09 17:54:04


```

On Sun, Aug 9, 2009 at 9:18 AM, Dr. David Kirkby <david.kirkby@onetel.net> wrote:


    Jason Moxham wrote:
    >
    > I guess the problem is this:
    > when gcc is built you can specify the architecture that it defaults to , and
    > for this virtual machine the default arch is "higher" than cicero. When MPIR
    > builds a fat build it calls gcc with no march options so you get the
    > default , what we should do is call gcc with march=486 etc
    > This is as far as I can  get , without access to systems that are known to
    > have this problem.
    >


Unfortunately, I don't have easy access to a system to replicate the problem either.  The virtual machine where I was building the test binary that I could try on cicero is down, and the VMware server admin web page is also down.  I'll likely have to do a slow and painful reboot of a lot of stuff to get his fixed.   I can also try building on an old laptop that's in my office.

Thanks for the idea above, which I can try.
 
 -- William

```



---

Comment by was created at 2009-08-09 20:56:46

More from Jason Moxham:

```

gcc -v
Reading specs from /usr/lib/gcc/x86_64-pc-linux/4.2.4/specs
Target: x86_64-pc-linux
Configured
with: ../gcc-4.2.4/configure --prefix=/usr --enable-shared --enable-languages=ada,c,c++,fortran,java,objc --disable-multilib --enable-threads=posix --enable-__cxa_atexit --disable-checking --with-gnu-ld --verbose
--build=x86_64-pc-linux
--target=x86_64-pc-linux
--host=x86_64-pc-linux
Thread model: posix
gcc version 4.2.4

These three parts

--build=x86_64-pc-linux
--target=x86_64-pc-linux
--host=x86_64-pc-linux

specify the default system , so we want to find a system where these
are "higher" than another system and then try the fat build on them , it
should fail if this is the answer

This will be easier on x86 than x86_64 as I expect gcc doesn't use the slight
differences on the 64bit arch much.
```



---

Comment by was created at 2009-11-11 17:46:33

Jason Moxham remarks:

```
The reason --enable-fat doesn't work is that in the sage-mpir install script
we detect for i386 and x86_64 ONLY , whereas uname -m can give other arches eg
on fedora32 it gives i686.  I bet the same is true for ATLAS.
An easy option for mpir at least is just to always pass -enable-fat if
SAGE_FAT is yes , else you will need to list all cpu's in the script that
uname -m can return.
```



---

Comment by was created at 2009-11-13 05:33:21

mpir patched: http://wstein.org/home/wstein/patches/mpir-1.2.p9.spkg


---

Comment by was created at 2009-11-13 05:33:54

atlas patched: http://wstein.org/home/mhansen/atlas-3.8.3.p10.spkg


---

Comment by was created at 2009-11-13 05:34:00

Changing status from new to needs_review.


---

Comment by was created at 2009-11-13 06:07:56

The mpir spkg works.  The atlas one hangs during building:

```
gcc -DL2SIZE=4194304 -I/tmp/wstein/farm/sage-4.2.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build/include -I/tmp/wstein/farm/sage-4.2.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build/../src//include -I/tmp/wstein/farm/sage-4.2.1.alpha0/spkg/build/atlas-3.8.3.p10/ATLAS-build/../src//include/contrib -DAdd__ -DF77_INTEGER=int -DStringSunStyle -DATL_OS_Linux -DATL_ARCH_HAMMER -DATL_CP*** glibc detected *** /usr/libexec/gcc/i586-redhat-linux/4.4.1/cc1: malloc(): memory corruption (fast): 0x0a3cbce0 ***

... 
HANG!
```



---

Comment by timdumol created at 2010-01-20 06:55:49

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-04-28 21:55:03

Nothing to merge -- this just works, and has just worked for a while now.  Yeah!


---

Comment by was created at 2010-04-28 21:55:03

Resolution: fixed
