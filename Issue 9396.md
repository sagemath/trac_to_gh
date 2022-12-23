# Issue 9396: statistical package r fails to run, missing libicuuc

Issue created by migration from https://trac.sagemath.org/ticket/9396

Original creator: mariah

Original creation time: 2010-06-30 15:34:57

Assignee: Mariah Lenox

CC:  david.kirkby@onetel.net

The statistical package r fails to run if the 
libicuuc library (frequently in /usr/lib) is not
present.

libicuuc is from the International Components for Unicode
project (http://site.icu-project.org/).


---

Attachment


---

Comment by mariah created at 2010-06-30 17:58:21

Further investigation revealed that the problem only
occurs when SAGE_FAT_BINARY is used, libicuuc exists
on the build computer, but not on the computer where
sage executes.

A solution is to add "--with-ICU=no" to the configure
line in spkg-INSTALL.  A mercurial patch is attached
which does this.

The same solution _may_ work for Solaris (I have not
tested) which currently uses "--without-ICU".


---

Comment by mariah created at 2010-06-30 17:58:40

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-07-02 20:50:18

In addition to providing a patch as you have done, it's normal Sage practice to put on the trac tickets a link to complete .spkg file. That allows a reviewer to quickly test the revised .spkg file without making it. It also allows the reviewer to check that the repository in the package is correct (i.e. 'hg status' shows no output). However, do not attach the .spkg file - only provide a link. 

According to the GNU autoconf manual:

http://www.gnu.org/software/autoconf/manual/autoconf.html#External-Software

"--without-package is equivalent to --with-package=no" 

I don't know anything about the SAGE_FAT_BINARY, but when I asked William if it was important, he said very so. 


I don't know whether just disabling this library is best or not. Your patch could disable it for some people that might make use of it. With Solaris, it was clear R would never build without this library, but either the library is supplied with almost all Linux distributions, or R builds without it on some systems. 

I'll raise this on sage-devel. 

Dave


---

Comment by drkirkby created at 2010-07-02 20:50:18

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-07-03 14:56:51

Replying to [comment:1 mariah]:
> Further investigation revealed that the problem only
> occurs when SAGE_FAT_BINARY is used, libicuuc exists
> on the build computer, but not on the computer where
> sage executes.

Given $SAGE_ROOT/README.txt says


```
3. Fat Binaries: To make a binary that will run on the widest range of
   target machines, set the SAGE_FAT_BINARY environment variable to
   "yes" before building Sage:

       export SAGE_FAT_BINARY="yes"
       make
       ./sage -bdist x.y.z-fat
```


then it seems perfectly reasonable that if one wants Sage to run on the widest range of platforms, that this library is disabled. 

If you can provide a link to a .spkg which has all the changes, then I will no doubt give this positive review. 

Dave


---

Comment by rlm created at 2010-07-09 09:43:34

Replying to [comment:5 drkirkby]:
> If you can provide a link to a .spkg which has all the changes, then I will no doubt give this positive review. 

http://sage.math.washington.edu/home/rlmill/r-2.10.1.p3.spkg


---

Comment by rlm created at 2010-07-09 09:43:34

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-07-09 11:40:02

SPKG.txt is wrong, due undoubtably due to the fact #9186 was recently merged, and took the patch level 2 number. 


```
### r-2.10.1.p2 (Mitesh Patel, June 8th 2010)
 * #9186: Set an empty MAKEFLAGS variable before "make install".  On
   OS X, at least, this fixes building multiple spkgs in parallel (cf.
   #8306).

### r-2.10.1.p2 (Mariah Lenox, 30 Jun 2010)
 * added "--with-ICU=no" to configure line of spkg-install (#9396)

### r-2.10.1.p1 (Karl-Dieter Crisman, April 12th 2010)
 * Re-enable Aqua support on OSX
```


The entry for Mariah's code should now be r-2.10.1.p3, not r-2.10.1.p2. 

I've just started a build on sage.math with this package and SAGE_FAT_BINARY=yes and will look over it. I can't see any reason this should fail, but I am going to check it. I should be back in an hour or two with a definitive decision. 

BTW, I know William has offered Mariah an account, which she has accepted, so soon she should have an account and be able to put packages on sage.math herself. 

Dave


---

Comment by drkirkby created at 2010-07-09 11:40:02

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-07-09 12:10:05

Changing status from needs_work to needs_review.


---

Attachment

spkg updated


---

Comment by drkirkby created at 2010-07-09 12:43:11

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-07-09 12:43:11

Em, I thought this one was a formality, but glad I checked, since R fails to build on sage.math with SAGE_FAT_BINARY=yes (I've not tried with that unset). 


```
r-2.10.1.p3/.hg/branch.cache
r-2.10.1.p3/SPKG.txt
Finished extraction
****************************************************
Host system
uname -a:
Linux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)
****************************************************
./spkg-install: line 114: syntax error near unexpected token `else'
./spkg-install: line 114: `     else'

real	0m0.028s
user	0m0.000s
sys	0m0.000s
sage: An error occurred while installing r-2.10.1.p3
```



Dave


---

Comment by drkirkby created at 2010-07-09 12:54:02

I think the problem is:


```
     if [ "$SAGE_FAT_BINARY" = "yes" ];
```


should be:


```
     if [ "$SAGE_FAT_BINARY" = "yes" ]; then
```


I've just made that change, and it at least starts to compile now. However, I don't have time to do any more on this for a few hours, since I have a chess game scheduled in a few minutes. 

There is another ticket I've just created for R (#9464), since R has Fortran code, but a Fortran dependency is not listed. I'll test these later today. 

Dave


---

Comment by drkirkby created at 2010-07-09 15:14:17

OK, here's a patch which corrects the syntax error. With this addition, R builds without the library. config.log shows R building with the option --with-icu=no. 


```
This file contains any messages produced by compilers while
running configure, to aid debugging if configure makes a mistake.

It was created by R configure 2.10.1, which was
generated by GNU Autoconf 2.61.  Invocation command line was

  $ ./configure --prefix=/home/kirkby/sage-4.5.alpha4/local --enable-R-shlib --with-x=yes --with-readline=/home/kirkby/sage-4.5.alpha4/local --with-blas=-L/home/kirkby/sage-4.5.alpha4/local/lib -lf77blas -latlas --with-lapack=-L/home/kirkby/sage-4.5.alpha4/local/lib -llapack -lcblas --with-ICU=no

## --------- ##
## Platform. ##
## --------- ##

hostname = sage.math.washington.edu
```


A revised .spkg may be found at 

http://boxen.math.washington.edu/home/kirkby/patches/r-2.10.1.p3.spkg

Dave


---

Comment by drkirkby created at 2010-07-09 15:14:17

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-07-09 15:15:07

Corrects syntax error in spkg-install


---

Comment by rlm created at 2010-07-18 10:37:50

Changing status from needs_review to positive_review.


---

Attachment

I'm setting this to positive review, since it builds on Solaris and off.

I'm also removing myself from the author block, since I did virtually nothing.


---

Comment by rlm created at 2010-07-18 20:02:44

With a fresh sage build, sage can't even start:

```
Traceback (most recent call last):
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/bin/sage-eval",
line 4, in <module>
   from sage.all import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/all.py",
line 73, in <module>
   from sage.matrix.all     import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/all.py",
line 1, in <module>
   from matrix_space import MatrixSpace, is_MatrixSpace
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py",
line 40, in <module>
   import matrix_mod2_dense
ImportError: /mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so:
undefined symbol: mzd_lqup
Sage failed to startup.
```



---

Comment by rlm created at 2010-07-18 20:02:44

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-07-18 20:05:28

Changing status from needs_work to positive_review.


---

Comment by rlm created at 2010-07-18 20:05:28

Sorry, totally wrong ticket.


---

Comment by drkirkby created at 2010-07-18 20:16:52

Replying to [comment:14 rlm]:
> Sorry, totally wrong ticket.

I was just about to ask what the connection was! When I Gooogled the error you showed, it looked more like an M4RI issue. Anyway, I'm glad it's not this ticket. 

Dave


---

Comment by kcrisman created at 2010-08-05 15:36:46

Hopefully this gets in the next release - it could be related to some other support requests we've had.    As expected, works fine on Mac.

One question: is it okay that SUN_FLAGS is not determined for non-Sun systems?  Is it possible that the shell would still have SUN_FLAGS set to something else (bad) from earlier in the Sage build process that could cause problems?  I assume not, since I'm a shell ignoramus, but just wanted to make sure this is the case.


---

Comment by mpatel created at 2010-08-09 09:38:26

Resolution: fixed
