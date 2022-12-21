# Issue 2575: GAP doesn't compile with CC='ccache gcc'

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2008-03-17 18:26:01

Assignee: mabshoff

i'm using ccache to speed up compilation. this works very well for other packages, but the configure script of GAP seems to be have an error.

environment variables:

```
CC=ccache gcc
CXX=ccache g++
```


GAP message:

```
Host system
uname -a:
Linux edoras 2.6.15-51-686 #1 SMP PREEMPT Tue Feb 12 16:59:15 UTC 2008 i686 GNU/Linux
****************************************************
****************************************************
GCC Version
gcc -v
Es werden eingebaute Spezifikationen verwendet.
Ziel: i486-linux-gnu
Konfiguriert mit: ../src/configure -v --enable-languages=c,c++,java,f95,objc,ada,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --program-suffix=-4.0 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-java-awt=gtk-default --enable-gtk-cairo --with-java-home=/usr/lib/jvm/java-1.4.2-gcj-4.0-1.4.2.0/jre --enable-mpfr --disable-werror --with-tune=pentium4 --enable-checking=release i486-linux-gnu
Thread-Modell: posix
gcc-Version 4.0.3 (Ubuntu 4.0.3-1ubuntu5)
****************************************************
checking build system type... i686-pc-linux-gnu
checking host system type... i686-pc-linux-gnu
checking target system type... i686-pc-linux-gnu
checking for gcc... ccache gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache gcc accepts -g... yes
checking for ccache gcc option to accept ANSI C... none needed
checking whether make sets $(MAKE)... yes
configure: creating ./config.status
config.status: creating Makefile
config.status: creating sysinfo.gap
config.status: creating bin/gap.sh
Building and installing gap-4.4.10
make[1]: Betrete Verzeichnis '/local/scratch/schilly/sage/spkg/build/gap-4.4.10.p2/src'
if test ! -d bin;  then mkdir bin;  fi
if test ! -d bin/i686-pc-linux-gnu-ccache;  then mkdir bin/i686-pc-linux-gnu-ccache;  fi
cp cnf/configure.out bin/i686-pc-linux-gnu-ccache/configure
( cd bin/i686-pc-linux-gnu-ccache ; CC='ccache gcc' ./configure --target=i686-pc-linux-gnu --prefix=/local/scratch/schilly/sage/local PREFIX=/local/scratch/schilly/sage/local CC=ccache gcc CXX=ccache g++ )
configure: WARNING: you should use --build, --host, --target
configure: WARNING: you should use --build, --host, --target
configure: WARNING: invalid host type: g++  
checking for gcc-gcc... ccache
checking for C compiler default output file name... configure: error: C compiler cannot create executables
See `config.log' for more details.
make[1]: *** [bin/i686-pc-linux-gnu-ccache/Makefile] Fehler 77
Error building gap.
```


my guess:

configure script, line 2293: `BASECC=`basename ${CC}``



---

Attachment

config.log produced by the configure process, for debugging, see BASECC variable


---

Comment by schilly created at 2008-04-22 14:08:33

just fo the record, problem still exists in 3.0 - this time the build process doesn't halt but continues (no info about failed gap).

after ./sage startup it raises a runtime exception complaining about broken gap.


---

Comment by mabshoff created at 2008-06-15 19:03:27

This has now popped up in other places. For now the short term solution is to unset CC in spkg-install. More long term we need to fix the autoconf issue and/or report this bug upstream.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-15 19:03:27

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-16 18:32:41

There is an updated spkg which should fix the issue at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/rc0/gap-4.4.10.p8.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-16 18:42:04

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-16 18:42:04

Resolution: fixed


---

Comment by schilly created at 2008-09-20 19:38:39

it doesn't work with 4.4.10 in sage 3.1.2/src


```
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking whether byte ordering is bigendian... no
checking for void *... yes
checking size of void *... 4
checking for nm... nm
checking whether symbols begin with an underscore... no
checking build system type... Invalid configuration `g++': machine `g++' not recognized
configure: error: /bin/bash ../../src/../cnf/config.sub g++ failed
make[1]: *** [bin/i686-pc-linux-gnu-gcc/Makefile] Error 1
make[1]: Leaving directory `/opt/sage/sage-src/spkg/build/gap-4.4.10.p9/src'
Error building gap.
```



```
CXX=ccache g++
CC=ccache gcc
```


unsetting those variables and the configure script works.


---

Comment by schilly created at 2008-09-20 19:38:39

Resolution changed from fixed to 


---

Comment by schilly created at 2008-09-20 19:38:39

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-09-20 20:28:48

Resolution: fixed


---

Comment by mabshoff created at 2008-09-20 20:28:48

We do not reopen tickets that have been fixed. This is not a regression, but the problem is that you set CXX in addition to CC. Unsetting CXX in the spkg-install will fix your problem, but for that open another ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-20 20:58:47

Harald, 

I now see that your original bug report also raises the issue with CXX, but since we hit this bug on another machine with CC and not CXX set we ended up fixing only the CXX case. You should still open a new ticket and not open old tickets for issues like that since it will muddy HISTORY.txt, i.e. fixing #2575 twice will only confuse people looking for specific tickets. Also resolving those tickets is messy since the comments on this ticket are already long. So a clean new ticket will solve all those problems.

Cheers,

Michael


---

Comment by drkirkby created at 2010-01-08 19:12:04

Perhaps striping 'ccache' out with 'sed' might have been a better solution.


---

Comment by schilly created at 2010-01-08 19:15:25

this ticket is already closed & fixed since it works. Is there a new compile problem? (If yes -> new ticket)

for me ccache works!

And stripping stuff out is probably not so cool, since it disables ccache ;)


---

Comment by leif created at 2012-03-22 14:24:27

Replying to [comment:11 schilly]:
> And stripping stuff out is probably not so cool, since it disables ccache ;)

Unsetting `CC` and `CXX` (as is currently done) also disables it. ;-)

If GAP still fails to configure / build when `CC` or `CXX` contain multiple words, we should probably unset `CC` and `CXX` *just in that case*, since currently even `CC=gcc-4.6.3` etc. are broken, and if the "default" gcc doesn't understand the flags intended for `$CC`, the build fails for no real reason.


---

Comment by leif created at 2012-03-22 17:47:13

Replying to [comment:12 leif]:
> If GAP still fails to configure / build when `CC` or `CXX` contain multiple words, we should probably unset `CC` and `CXX` *just in that case* [...]

For the record: My GAP 4.4.12.p7 spkg for #7041 will just do that.
