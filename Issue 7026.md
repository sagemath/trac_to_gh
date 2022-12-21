# Issue 7026: linbox 1.1.6.p0 says GMP is not installed, even though MPIR is

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 11:33:31

Assignee: cpernet

When using the Sun compiler with sage-4.1.2.alpha2, linbox 1.1.6.p0 seems to think GMP is not installed, even though the substitute mpir is installed. See below.

This is very similar to #7025, which occurs with givaro. 

All these files actually exist


```
local/include/gmp.h
local/include/gmpxx.h
local/lib/libgmp.la
local/lib/libgmp.so
local/lib/libgmp.so.3
local/lib/libgmp.so.3.4.4
local/lib/libgmpxx.la
local/lib/libgmpxx.so
local/lib/libgmpxx.so.3
local/lib/libgmpxx.so.3.1.4
```


Here's the error:


```

checking size of long long... 8
checking for __int64... no
checking size of __int64... 0
checking whether byte ordering is bigendian... yes
Default path = /usr /usr/local
checking whether to compile the drivers... no
checking for GMP >= 3.1.1... *******************************************************************************
 ERROR: GMP not found!

 GMP version 3.1.1 or greater with --enable-cxx is required for this library to compile. Please
 make sure GMP is installed and specify its location with the option
 --with-gmp=<prefix> when running configure.
*******************************************************************************
Error configuring linbox

real    0m29.178s
user    0m7.691s
sys     0m12.302s
sage: An error occurred while installing linbox-1.1.6.p0
```






---

Comment by drkirkby created at 2010-01-14 09:19:29

Linbox is also indicating it can't find GMP using gcc 4.4.1 in 64-bit mode on a SPARC.


```
checking size of int... 4
checking for long... yes
checking size of long... 8
checking for long long... yes
checking size of long long... 8
checking for __int64... no
checking size of __int64... 0
checking whether byte ordering is bigendian... yes
Default path = /usr /usr/local
checking whether to compile the drivers... no
checking for GMP >= 3.1.1... problem
Sorry, your GMP version is too old. Disabling.
*******************************************************************************
 ERROR: GMP not found!
```


So Linbox has problems with GMP on 

 * Solaris 10 SPARC 32-bit mode with the Sun compiler. 
 * Solaris 10 SPARC 64-bit mode with gcc

Linbox at least reconsises GMP on:
 
 * 32-bit mode Solaris 10 SPARC with gcc
 * 64-bit model Open Solaris with gcc.


---

Attachment

config.log seen on a SPARC using gcc in 64-bit mode


---

Comment by drkirkby created at 2010-01-14 16:42:03

The attachment _config.log.64-bit.gcc.SPARC.txt_ was generated on a Sun Blade 2000 from sage-4.3.1.alpha2, but with the following environment variables set to force the use of a 64-bit build.


```
LD_LIBRARY_PATH=/usr/local/lib
LD_LIBRARY_PATH_64=/usr/local/lib/sparcv9
FPIC_FLAG=-fPIC
CFLAG64=-m64
SAGE64=yes
CFLAGS=-m64
CXXFLAG64=-m64
FCFLAGS=-m64
```


Some of those are used internally to Sage.


---

Comment by drkirkby created at 2010-01-14 19:09:36

Having looked at the error message, it would appear the library can't be found. But it does exist as the place expected. 


```
drkirkby`@`swan:[~] $ file  gcc64/sage-4.3.1.alpha2/local/lib/libgmpxx.so.3
gcc64/sage-4.3.1.alpha2/local/lib/libgmpxx.so.3:        ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped, no debugging information available
drkirkby`@`swan:[~] $ 
```


Appending /export/home/drkirkby/gcc64/sage-4.3.1.alpha2/local/lib/ to LD_LIBRARY_PATH_64 gets past the issue with GMP, though it does not allow Linbox to build fully. 


```
export LD_LIBRARY_PATH_64=/usr/local/lib/sparcv9:/export/home/drkirkby/gcc64/sage-4.3.1.alpha2/local/lib/

checking size of long... 8
checking for long long... yes
checking size of long long... 8
checking for __int64... no
checking size of __int64... 0
checking whether byte ordering is bigendian... yes
Default path = /usr /usr/local
checking whether to compile the drivers... no
checking for GMP >= 3.1.1... found
checking whether GMP is 4.0 or greater... yes
checking whether GMP was compiled with --enable-cxx... yes

So it is happy with gmp.

checking for NTL >= 5.0... found
checking for GIVARO >= 3.2.10... found
checking whether to compile the sage interface... yes
checking for C interface to BLAS... not found
checking for others BLAS... not found
```


So Linbox ultimately fails to build for another reason, but the GMP issue can be circumvented. 

I think with hindsight, it would have been better for 64-bit libraries in Sage on Solaris to have been put in $SAGE_LOCAL/lib/sparcv9 or $SAGE_LOCAL/lib/amd64 as appropriate. 

Probably adding a new variable inside sage-env called LD_LIBRARY_PATH_64 and making that point to $SAGE_LOCAL/lib/ will do the trick. That will cause the linker to look there for 64-bit libraries.


---

Comment by jdemeyer created at 2013-03-28 22:50:33

Closing since this refers to old versions.


---

Comment by jdemeyer created at 2013-03-28 22:50:33

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-03-28 22:50:42

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-29 19:00:33

Resolution: invalid
