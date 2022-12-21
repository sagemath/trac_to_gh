# Issue 7182: HP-UX failure of gfan-0.3.p4 but easier to ensure we have GNU make.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-10-10 09:35:18

Assignee: tbd

Keywords: HP-UX Solaris make

gfan will not build on my HP-UX box, as the 'make' program does not like a 'makefile'. Perhaps the gfan developer would like to fix this, but from the point of view of Sage, it is easier we ensure that 'make' is GNU make (see #7181), since on Solaris we find Sun's 'make' has no chance at all of building Sage. 


```
Extracting package /home/drkirkby/sage-4.1.2.rc0/spkg/standard/gfan-0.3.p4.spkg ...
-rw-r--r--   1 drkirkby   users       129974 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/gfan-0.3.p4.spkg
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.4.0 (GCC)
****************************************************
Make: Must be a separator on rules line 14.  Stop.
Error building gfan

real    0m0.050s
user    0m0.030s
sys     0m0.020s
sage: An error occurred while installing gfan-0.3.p4

```



---

Comment by mhansen created at 2009-11-20 06:22:35

Resolution: fixed


---

Comment by mhansen created at 2009-11-20 06:22:35

Fixed by #7352
