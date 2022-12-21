# Issue 1246: mpfi-1.3.4-rc3.p9 fails to build on x86_64 SuSE 10.1

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-23 12:38:25

Assignee: mabshoff

Alexander Dreyer reported:

```
****************************************************
GCC Version
gcc -v
Es werden eingebaute Spezifikationen verwendet.
Ziel: x86_64-suse-linux
Konfiguriert mit: ../configure --enable-threads=posix --prefix=/usr --
with-local-prefix=/usr/local --infodir=/usr/share/info --mandir=/usr/
share/man --libdir=/usr/lib64 --libexecdir=/usr/lib64 --enable-
languages=c,c++,objc,fortran,obj-c++,java,ada --enable-
checking=release --with-gxx-include-dir=/usr/include/c++/4.1.2 --
enable-ssp --disable-libssp --disable-libgcj --with-slibdir=/lib64 --
with-system-zlib --enable-shared --enable-__cxa_atexit --enable-
libstdcxx-allocator=new --program-suffix= --enable-version-specific-
runtime-libs --without-system-libunwind --with-cpu=generic --
host=x86_64-suse-linux
Thread-Modell: posix
gcc-Version 4.1.2 20070115 (prerelease) (SUSE Linux)
****************************************************
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
/u/herc/dreyer/tmp/sage-2.8.13/spkg/build/mpfi-1.3.4-rc3.p9/src/
missing: Unknown `--run' option
Try `/u/herc/dreyer/tmp/sage-2.8.13/spkg/build/mpfi-1.3.4-rc3.p9/src/
missing --help' for more information
configure: WARNING: `missing' script is too old or missing
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for gawk... gawk
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
checking for ranlib... ranlib
checking how to run the C preprocessor... gcc -E
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for string.h... (cached) yes
checking for gmp.h... yes
checking for valid GMP... yes
checking for mpfr.h... yes
checking for main in -lmpfr... yes
checking for main in -lgmp... no
configure: error: Library GMP not found
Error configuring mpfi 
```


See also http://groups.google.com/group/sage-support/t/8e446357a1d15a8a

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-23 12:51:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-24 16:16:28

Alexander Dreyer reports:

```
Meanwhile, I got sage compiled by changing the configure line in spkg-
install of mpfi-1.3.4-rc3.p9 to
./configure --prefix="$SAGE_LOCAL" --with-mpfr-dir="$SAGE_LOCAL"
CFLAGS="-fPIC"
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 17:53:24

Ok, at 

http://sage.math.washington.edu/home/mabshoff/mpfi-1.3.4-rc3.p10.spkg

you can find an spkg that includes this fix.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-25 07:53:06

Merged in 2.8.14.rc2.


---

Comment by mabshoff created at 2007-11-25 07:53:06

Resolution: fixed
