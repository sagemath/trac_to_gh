# Issue 7180: HP-UX cddlib-094f checks for gmp.h, then igores the fact it can't find it.

Issue created by migration from https://trac.sagemath.org/ticket/7180

Original creator: drkirkby

Original creation time: 2009-10-10 09:24:44

Assignee: tbd

CC:  chapoton

Keywords: HP-UX gmp mpir

MPIR would not build on my HP-UX box, so needless to say programs wanting gmp will not work. However, cddlib-094f  checks for gmp, then ignores the fact it can't find it. It should exit with a clear error message then, not carry on. 

A developer can have access to the HP-UX box, but this is not really necessay to fix this. Just email me with your preffered user name if you want to have an account 

```
...
-rw-r--r--   1 drkirkby   users       266542 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/cddlib-094f.spkg
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
checking for a BSD-compatible install... ./install-sh -c
checking whether build environment is sane... yes
checking for gawk... no
checking for mawk... no
checking for nawk... no
checking for awk... awk
checking whether make sets $(MAKE)... yes
checking for gcc... gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking for a BSD-compatible install... ./install-sh -c
checking for ranlib... ranlib
checking for main in -lgmp... no
checking how to run the C preprocessor... gcc -E
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for ANSI C header files... yes
checking for an ANSI C-conforming const... yes
configure: creating ./config.status
config.status: creating lib-src/Makefile
config.status: WARNING:  lib-src/Makefile.in seems to ignore the --datarootdir setting
config.status: creating src/Makefile
config.status: WARNING:  src/Makefile.in seems to ignore the --datarootdir setting
config.status: creating lib-src-gmp/Makefile
config.status: WARNING:  lib-src-gmp/Makefile.in seems to ignore the --datarootdir setting
config.status: creating src-gmp/Makefile
config.status: WARNING:  src-gmp/Makefile.in seems to ignore the --datarootdir setting
config.status: creating Makefile
config.status: WARNING:  Makefile.in seems to ignore the --datarootdir setting
config.status: executing depfiles commands
Make: line 409: syntax error.  Stop.
Error building cddlib

real    0m8.255s
user    0m4.260s
sys     0m2.460s
sage: An error occurred while installing cddlib-094f

```



---

Comment by drkirkby created at 2009-11-27 13:29:44

I'm not sure who to report this too, but it does need reporting.


---

Comment by jdemeyer created at 2015-09-08 12:45:40

Changing component from build to porting: AIX or HP-UX.


---

Comment by embray created at 2019-01-15 18:39:07

I don't believe anyone's been maintaining support for AIX or HP-UX for some time.  Putting in sage-wishlist for now in case there is still a desire for it out there, otherwise these tickets should be closed (most of them are probably no longer relevant in any case but I have no obvious way to check this).


---

Comment by mkoeppe created at 2020-06-23 21:26:55

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-23 21:26:55

We should close this ticket as outdated.


---

Comment by chapoton created at 2020-06-24 06:28:42

Resolution: invalid
