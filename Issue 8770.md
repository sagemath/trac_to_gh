# Issue 8770: gfan fails to build on Fedora Core 12 wtih GCC-4.5.0 (lena)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-26 20:08:26

Assignee: GeorgSWeber


```
g++  -O2 -DGMPRATIONAL -g -I /home/wstein/screen/lena/sage-4.4/local/include    -c halfopencone.cpp
g++  -O2 -DGMPRATIONAL -g -I /home/wstein/screen/lena/sage-4.4/local/include    -c lll.cpp
/tmp/ccngbXYk.s: Assembler messages:
/tmp/ccngbXYk.s:16711: Error: symbol `_ZZN6MatrixIiEixEPiPP6VektorIiEiE19__PRETTY_FUNCTION__' is already defined
make[2]: *** [lll.o] Error 1
make[2]: Leaving directory `/home/wstein/screen/lena/sage-4.4/spkg/build/gfan-0.4plus/src'
Error building gfan

real    0m54.211s
user    0m50.094s
sys     0m3.030s
sage: An error occurred while installing gfan-0.4plus
```


About the machine:

```
[wstein`@`lena sage-4.4]$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-k10-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-gnu-as=/usr/local/binutils-2.20.1/x86_64-Linux-k10-fc-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-k10-fc-gcc-4.4.3/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-k10-gcc-4.2.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-k10-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-k10-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3 --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-k10-fc
Thread model: posix
gcc version 4.5.0 (GCC)
[wstein`@`lena sage-4.4]$ uname -a
Linux lena 2.6.31.12-174.2.19.fc12.x86_64 #1 SMP Thu Feb 11 07:07:16 UTC 2010 x86_64 x86_64 x86_64 GNU/Linux
[wstein`@`lena sage-4.4]$ cat /etc/issue
Fedora release 12 (Constantine)
Kernel \r on an \m (\l)
                          
```



---

Comment by was created at 2010-04-26 20:29:27

Changing assignee from GeorgSWeber to was.


---

Comment by was created at 2010-04-26 20:29:27

Discoveries:

In gfan with GCC-4.5.0 on "lena (a k10)" linux box:

```
g++  -DGMPRATIONAL    -c lll.cpp
```

works fine, but

```
sage subshell$ g++ -O2 -DGMPRATIONAL    -c lll.cpp
/tmp/cchu2txF.s: Assembler messages:
/tmp/cchu2txF.s:5145: Error: symbol `_ZZN6MatrixIiEixEPiPP6VektorIiEiE19__PRETTY_FUNCTION__' is already defined
```


Doing make after compiling without -O2 gives:

```
...
g++  -O2 -DGMPRATIONAL -g     -c linalg.cpp
linalg.cpp:528:1: error: ‘FieldMatrix::FieldMatrix’ names the constructor, not the type
make: *** [linalg.o] Error 1
/home/wstein/screen/lena/sage-4.4
```



---

Comment by was created at 2010-04-26 20:33:54

The fix for linalg.cpp:528 is to replace that line of linalg.cpp with:

```
FieldMatrix FieldMatrix::solver()const
```



---

Comment by was created at 2010-04-26 20:36:01

With the above two fixes:

  (1) build with optimization off

  (2) Make one change in linalg.cpp

gfan builds and installs.


---

Comment by wjp created at 2010-04-26 23:30:54

Some observations on the duplicate symbol:

g++ 4.5 seems to mangle the `__PRETTY_FUNCTION__` symbol of two different `operator[]`'s (differing in their const-ness) to the same symbol, which is most likely a compiler bug, I think.

These `__PRETTY_FUNCTION__` symbols are only generated because of the asserts in `Matrix::operator[]` in `matrix.h`, so disabling those two asserts would be a workaround.


---

Comment by was created at 2010-04-27 00:14:40

and from wjp:

```
17:01 < wjp> something like "check for gcc 4.5, and pass -fno-ipa-rsa if found" should do the trick, I think
```



---

Comment by wjp created at 2010-04-27 01:10:46

I submitted the duplicate symbol issue to gcc's bug tracker:

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=43905


---

Comment by was created at 2010-04-28 03:06:15

From Upstream:

```
Anders Nedergaard Jensen to me, Willem
show details 2:23 AM (17 hours ago)
Hi William,
Thanks for reporting these "bugs".

"FieldMatrix::FieldMatrix" should clearly be "FieldMatrix".

For the assert problem, an acceptable solution for you is to remove one of the assert statements.

I will code my way around the gcc4.5 bug for the next gfan release.
-Anders
```



---

Comment by wjp created at 2010-04-28 16:35:28

Changing status from new to needs_review.


---

Comment by wjp created at 2010-04-28 16:35:28

I created a p1 that applies the changes Anders confirmed.

http://www.math.leidenuniv.nl/~wpalenst/sage/gfan-0.4plus.p1.spkg


---

Comment by was created at 2010-04-28 19:13:56

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-28 19:13:56

Looks good.


---

Comment by was created at 2010-04-28 19:26:45

Resolution: fixed


---

Comment by wjp created at 2010-06-24 13:18:54

The gcc bug involved is now fixed in gcc trunk according to

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=43905
