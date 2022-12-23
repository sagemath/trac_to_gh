# Issue 7761: Python 2.6.2.p4 faills to build on Open Solaris

Issue created by migration from https://trac.sagemath.org/ticket/7761

Original creator: drkirkby

Original creation time: 2009-12-24 16:45:17

Assignee: drkirkby

CC:  was david.kirkby@onetel.net mvngu

Keywords: python open solaris

I believe William is aware of this bug and said it can be fixed by installing OpenSSL or similar. But I am unable to find a trac ticket for it, so I thought I'd open one. It's interesting this issue does not arise on Solaris 10 (SPARC), despite OpenSSL libraries not being present there either. This bug seems to come up a lot on linux too, as a Google search shows. 

On a Sun Ultra 27 (Intel Xeon processor), running Open Solaris 06/2009, I get the following problem when python is being built. 


```
copying build/scripts-2.6/pydoc -> /export/home/drkirkby/sage-4.3.rc2/local/bin
changing mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/2to3 to 755
changing mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/smtpd.py to 755
changing mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/idle to 755
changing mode of /export/home/drkirkby/sage-4.3.rc2/local/bin/pydoc to 755
running install_egg_info
Removing /export/home/drkirkby/sage-4.3.rc2/local/lib/python2.6/lib-dynload/Python-2.6.2-py2.6.egg-info
Writing /export/home/drkirkby/sage-4.3.rc2/local/lib/python2.6/lib-dynload/Python-2.6.2-py2.6.egg-info
if test -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python -o -h /export/home/drkirkby/sage-4.3.rc2/local/bin/python; \
	then rm -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python; \
	else true; \
	fi
(cd /export/home/drkirkby/sage-4.3.rc2/local/bin; ln python2.6 python)
rm -f /export/home/drkirkby/sage-4.3.rc2/local/bin/python-config
(cd /export/home/drkirkby/sage-4.3.rc2/local/bin; ln -s python2.6-config python-config)
/usr/bin/ginstall -c -m 644 ./Misc/python.man \
		/export/home/drkirkby/sage-4.3.rc2/local/share/man/man1/python.1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.rc2/spkg/build/python-2.6.2.p4/src'
Sleeping for three seconds before testing python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/export/home/drkirkby/sage-4.3.rc2/local/lib/python/hashlib.py", line 136, in <module>
    md5 = __get_builtin_constructor('md5')
  File "/export/home/drkirkby/sage-4.3.rc2/local/lib/python/hashlib.py", line 63, in __get_builtin_constructor
    import _md5
ImportError: No module named _md5

real	1m38.244s
user	1m15.115s
sys	0m13.132s
sage: An error occurred while installing python-2.6.2.p4

```


I'm not sure if this should be reported upstream or not. Some feedback on that might be useful. If so, I will report it to a python bug tracker or similar. The issue seems to arrise often enough. 

Dave 

PS, to even get to this point, I had to delete the following list of files, to get around a gnutls issue in #7387.


```
    * SAGE_LOCAL/include/gcrypt-module.h
    * SAGE_LOCAL/include/gpg-error.h
    * SAGE_LOCAL/include/gcrypt.h
    * SAGE_LOCAL/lib/libgcrypt*
    * SAGE_LOCAL/lib/libgpg* 
```



---

Comment by drkirkby created at 2010-01-02 09:23:14

These problems go away if one builds in 64-bit mode, by exporting SAGE64 to yes. However, CFLAGS must be passed properly to Python, otherwise the -m64 does not get added as a CFLAG. That was only happening on OS X. 

This updated spkg file adds:


```
CC="$CC $CFLAGS"
```

on the end of the configure line. Then, as long as CFLAGS contains -m64, so the package will build with 64-bit support. 

http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/


---

Comment by drkirkby created at 2010-01-02 09:23:14

Changing status from new to needs_review.


---

Comment by jsp created at 2010-01-03 01:08:25

On my Open Solaris build still fails:

```
Sleeping for three seconds before testing python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/export/home/jaap/Downloads/sage-4.3/local/lib/python/hashlib.py", line 136, in <module>
    md5 = __get_builtin_constructor('md5')
  File "/export/home/jaap/Downloads/sage-4.3/local/lib/python/hashlib.py", line 63, in __get_builtin_constructor
    import _md5
ImportError: No module named _md5

real	3m11.679s
user	1m47.153s
sys	0m36.011s
sage: An error occurred while installing python-2.6.2.p5

```


Where is openssl supposed to be be installed?

/usr/local/ssl did not work for me.

Jaap


---

Comment by drkirkby created at 2010-01-03 02:13:50

That is very odd. I just used OpenSSL's default location, which is /usr/local/ssl. Python knows to look there. I manged to get the following all built now in 64-bit mode.  

```
drkirkby@hawk:~/sage-4.3/spkg/installed$ ls
bzip2-1.0.5             libgcrypt-1.4.4.p1      python-2.6.2.p5
cliquer-1.2.p2          libgpg_error-1.6.p3     readline-6.0.p1
conway_polynomials-0.2  libpng-1.2.35.p0        sage_scripts-4.3
dir-0.1                 mercurial-1.3.1.p0      scons-1.2.0
eclib-20080310.p8       mpir-1.2.2              sqlite-3.6.19.p0
elliptic_curves-0.1     ntl-5.4.2.p9            termcap-1.3.1.p0
extcode-4.3             opencdk-0.6.6.p3        zlib-1.2.3.p5
gnutls-2.2.1.p5         pari-2.3.3.p5
graphs-20070722.p1      prereq-0.6
```

before Flint decided it did not want to play ball, and exited with an ELFCLASS problem (mixing of 32 and 64-bit objects). 

I did something like:

```
$ export SAGE64=yes
$ export CFLAGS=-m64
$ export CXFLAGS=-m64
$ export FCFLAGS=-m64
$ export SAGE_FORTRAN_LIB=/usr/local/lib/libgfortran.so
$ make
```


I've got several gcc's on here, but just noticed the one which got this far was *not* using the GNU asssembler as I advised, but all Sun tools. Note the configure option '--with-build-time-tools=/usr/ccs/bin' Perhaps the GCC bugs are sorted out in 4.4.2 which allow it to work with the Sun assembler. 

```
drkirkby@hawk:~$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ./configure --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.2 (GCC) 
```



---

Comment by jsp created at 2010-01-05 14:44:27

Replying to [comment:3 drkirkby]:
> That is very odd. I just used OpenSSL's default location, which is /usr/local/ssl. Python knows to look there. I manged to get the following all built now in 64-bit mode.  

You are right. The problem I have is again with ld


```
BN_mod_sqrt                         0x1159      /usr/local/lib/libcrypto.a(ecp_smpl.o)
BN_kronecker                        0x119e      /usr/local/lib/libcrypto.a(ecp_smpl.o)
BN_kronecker                        0x1f5       /usr/local/lib/libcrypto.a(bn_sqrt.o)
.rodata (section)                   0x198       /usr/local/lib/libcrypto.a(bn_kron.o)
.rodata (section)                   0x293       /usr/local/lib/libcrypto.a(bn_kron.o)
.rodata.str1.1 (merged string section) 0x56             /usr/local/lib/libcrypto.a(bn_sqrt.o)
.rodata.str1.1 (merged string section) 0x491            /usr/local/lib/libcrypto.a(bn_sqrt.o)
.rodata.str1.1 (merged string section) 0x529            /usr/local/lib/libcrypto.a(bn_sqrt.o)
.rodata.str1.1 (merged string section) 0x53e            /usr/local/lib/libcrypto.a(bn_sqrt.o)
ld: fatal: relocations remain against allocatable but non-writable sections
collect2: ld returned 1 exit status

```


I'll build a new gcc.

Jaap


---

Comment by drkirkby created at 2010-01-07 17:23:35

> .rodata.str1.1 (merged string section) 0x53e            /usr/local/lib/libcrypto.a(bn_sqrt.o)
> ld: fatal: relocations remain against allocatable but non-writable sections
> collect2: ld returned 1 exit status
> 
> }}}
> 
> I'll build a new gcc.
> 
> Jaap
> 
Yes, I think building a new gcc is probably your best course of action. Several people have said gcc 4.3.4 is one of the more stable gcc's. 

I think ATLAS might dictate the use of the Sun assembler, as some of the assembly looks like it will only work with the GNU assembler. 

The following has allowed me to build python with 'hashlib' support. Try building python with that. If it fails, try building OpenSSL with it. 

If all else fails, I can make some tarbals of my gcc and binutils binaries, upload them, then you try those. Then we would have *exactly* the same build tools. But I don't believe such drastic measures should be necessary, but if they are helpful, I can do it. 

```
drkirkby@hawk:~/sage-4.3.1.alpha1$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.3.4 (GCC) 
```



---

Comment by drkirkby created at 2010-01-10 18:30:12

I'm sticking this to 'needs info' as I've noticed another problem in this package (incorrect usage of set -e), and might as well fix the other one at the same time.


---

Comment by drkirkby created at 2010-01-10 18:30:12

Changing status from needs_review to needs_info.


---

Comment by jsp created at 2010-01-10 18:40:01

I'm slowly making progress building p5 on my Open Solaris in VirtualBox :)

_ssl.o and ssl.so are now built. _hashlib.so failed on:



```
gcc -Wall -g -m64 -Wall -g -m64 -shared -L/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/lib -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I. -IInclude -I./Include -I/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/include build/temp.solaris-2.11-i86pc-2.6/export/home/jaap/Downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5/src/Modules/_hashopenssl.o -L/export/home/jaap/Downloads/sage-4.3.1.alpha1/local/lib -L/usr/local/lib -lssl -lcrypto -o build/lib.solaris-2.11-i86pc-2.6/_hashlib.so
*** WARNING: renaming "_hashlib" since importing it failed: ld.so.1: python: fatal: relocation error: file build/lib.solaris-2.11-i86pc-2.6/_hashlib.so: symbol EVP_MD_CTX_md: referenced symbol not found

```



Jaap


---

Comment by jsp created at 2010-01-10 21:09:45

I finally got this going on Open Solaris in VirtualBox!

The problem was related to different ssl libraries.

We have to be sure there is only one openssl in the process.

In the end I only used the system ssl and libcrypto

Installing OpenSLL is probably not the solution in Open Solaris.

In the standard setup the spkg installs fine.

So positive review! But leaving it to needs_info. Waiting for David.

Jaap


---

Comment by jsp created at 2010-01-10 21:27:47

OK, I see you updated the spkg in

[http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/](http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/)

Let me test this.

Jaap


---

Comment by drkirkby created at 2010-01-10 21:40:30

Updated package which 

 * Fixes the issue on Open Solaris, though it relies on having the new sage-env patch #7818 installed. 
 * Removes 'set -e' which was hiding an error message. 
 * Added a check that the Itanium fix was actually applied properly. (That was the only thing which was not checked in spkg-install. Almost everything else was properly checked). 

The updated version can be found at: 

http://boxen.math.washington.edu/home/kirkby/portability/python-2.6.2.p5/


---

Comment by drkirkby created at 2010-01-10 21:40:30

Changing status from needs_info to needs_review.


---

Attachment


---

Comment by jsp created at 2010-01-10 23:36:50

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-01-10 23:36:50

On Open Solaris:


```
Sleeping for three seconds before testing python
hashlib module imported

real	2m45.196s
user	1m48.948s
sys	0m32.524s
Successfully installed python-2.6.2.p5
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.2.p5.spkg
jaap@opensolaris:~/Downloads/sage-4.3.1.alpha1$ 


```


Fedora 12:


```
Sleeping for three seconds before testing python
hashlib module imported

real	2m2.042s
user	1m51.869s
sys	0m17.783s
Successfully installed python-2.6.2.p5
You can safely delete the temporary build directory
/home/jaap/downloads/sage-4.3.1.alpha1/spkg/build/python-2.6.2.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.2.p5.spkg
[jaap@vrede sage-4.3.1.alpha1]$ 

```


Overall this looks good! Hope this gets into sage-3.4.1.

Positive review.

Jaap


---

Comment by rlm created at 2010-01-13 06:10:58

Too late for sage-3.4.1, but we'll still merge it ;-)


---

Comment by rlm created at 2010-01-13 06:10:58

Resolution: fixed


---

Comment by robertwb created at 2010-01-29 23:59:54

Changing status from closed to needs_work.


---

Comment by robertwb created at 2010-01-29 23:59:54

Does this still rely on the (unresolved) #7818? Distutils pulls CFLAGS out of the makefile, so I'm not convince that 


```
CC="$CC $CFLAGS"
```


is the way to go if extension modules should pick them up as well (but maybe it picks up CC as well). Probably better to pass them into the autoconf script using the OPT variable.


---

Comment by jsp created at 2010-01-30 01:29:22

Replying to [comment:15 robertwb]:
> Does this still rely on the (unresolved) #7818? Distutils pulls CFLAGS out of the makefile, so I'm not convince that 
> 
> {{{
> CC="$CC $CFLAGS"
> }}}
> 
> is the way to go if extension modules should pick them up as well (but maybe it picks up CC as well). Probably better to pass them into the autoconf script using the OPT variable. 

I don't like the way you handle this. Dave made a point. It works on Open Solaris when CFLAGS contains -m64.

It maybe not sufficient, but it works here and let me have a working python.

I think release managers are way due to resolve this issue: having two p5 patches.

Let's get on!

Jaap


---

Comment by robertwb created at 2010-01-30 03:27:56

I'm just saying that the problems we have later on using setup.py to build extensions may have to do with the fact that Python is built with "covert" command line options that Distutils doesn't pick up. I figured this ticket needed to be re-opened 'cause if it never got in it's clearly shouldn't be closed. (At this point, we should probably make a p6 spkg.) I agree with the general goal behind #7818, but it has issues that I don't know how to fix, so shouldn't be a dependancy (unless that gets worked out first).


---

Comment by drkirkby created at 2010-01-30 04:36:19

I can understand why this was not merged. I'm just in the process of updating #7818. I just need to double check everything. But the main change is that 

 * The user can supply SAGE_CFLAGS to set some CFLAGS they want. Since they are not setting CFLAGS, them doing so will not risk corrupting the Sage environment. 

 * CFLAGS will not be exported, but instead 'SAGE_COMMON_CFLAGS', which will contain what the user specific in SAGE_CFLAGS, plus those flags I deem sensible. 

 * Any spkg-install script that wants to use these flags, would have to do so by explicitly doing so via. 

CFLAGS="$SAGE_COMOON_CFLAGS"

That I believe will be safe. No package is forced to use my flags, but they can choose to. Hence I believe the changes to sage-env will be 100% safe, as they will not change any commonly used environment variables. 

So that's what I intend to do with sage-env. Now to the specific of this package. 

Prior to writing this new package, I looked at Python's spkg-install to see how the 64-bit build has been enabled on OS X, and you can see it added -m64 to gcc, so "gcc -m64" was used as a compiler. Hence I basically used a similar method. 

Having later looked more carefully at the python documentation, the way to pass flags is not the way it is done on the spkg-install for OS X, so whist it may work, it is not the right way to do it. 

I think the best solution is that I update sage-env, then update the python package, but in a way that is specific to Solaris, AIX and HP-UX. Then at a later date, we can try in an alpha0 to drop it in without it being specific to that platform. 

I think the ability to allow the user to pass their own flags is quite important, as they can use that to optimise gcc for thier processor. At the momemnt, 95% of Sage's code is being built for a generic processor, and not exploiting the features of anyones particular processor. 

So let me update sage-env in a safe way, then update this, to make use of sage-env's changes, but only on some rarer platforms. 

I think in the short term, Jaap should not worry about setting CFLAGS globally if it allows a package to build. Progress can then be made. He can always break the build process manually at some point, and unset it, just before cython gets to work. 

Leave it with me. I'll make what I believe are sensible decisions, then others can comment of course. In the mean time, I'm happy with this not being merged just now. I do agree it is sub-optimal. 

Dave


---

Comment by robertwb created at 2010-01-30 05:41:00

Replying to [comment:18 drkirkby]:
> I can understand why this was not merged. I'm just in the process of updating #7818. I just need to double check everything. But the main change is that 

Great. 

> Prior to writing this new package, I looked at Python's spkg-install to see how the 64-bit build has been enabled on OS X, and you can see it added -m64 to gcc, so "gcc -m64" was used as a compiler. Hence I basically used a similar method. 

Ah, OK. For easy reference: 


```
    if [ `uname` = "Darwin" ]; then
        if [ "$SAGE64" = "yes" ]; then
            echo "64 bit OSX build enabled"
            OPT="-g -O3 -m64 -Wall -Wstrict-prototypes"; export OPT
            ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL" --without-libpng \
	    --enable-unicode=ucs4 --with-gcc="gcc -m64" --disable-toolbox-glue
        else
            ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL" --without-libpng \
	    --enable-unicode=ucs4 --disable-toolbox-glue
        fi
    else
        ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL" --without-libpng --enable-unicode=ucs4 CC="$CC $CFLAGS" CXX="$CXX $CXXFLAGS"
    fi
```


Interestingly, -m64 gets added to both OPT (used by Python and distutils in making CFLAGS) and gcc. I wonder if both are necessary, or if this is redundant (yielding two -m65s in the final command, which shouldn't hurt). In any case, hopefully we can do this in such a way that all the spkg-installs that are just "python setup.py install" won't have to have extra stuff added in there as well.


---

Comment by jsp created at 2010-01-30 12:57:47

As a work around I changed Darwin to SunOS. This give a working cython!

Checking other packages with python setup.py install.

Jaap


---

Comment by drkirkby created at 2010-01-30 13:44:36

That seems fine. Whatever allows you to make progress. Specific issues can be sorted later. There are some quite interesting, and more complex tasks, such as #6028 to be solved. You might want to take a look at something more interesting, if you get fed up with adding -m64!

Dave


---

Attachment

Made a new spkg work on Open nSolaris, leaving the OSX solution as is.

[http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg)

See also the patch:
[http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.patch](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.patch)

On 'hawk':


```
(cd /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin; ln python2.6 python)
rm -f /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin/python-config
(cd /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/bin; ln -s python2.6-config python-config)
/usr/bin/ginstall -c -m 644 ./Misc/python.man \
                /export/home/jaap/sage_port/sage-4.3.2.alpha1/local/share/man/man1/python.1
Sleeping for three seconds before testing python
hashlib module imported
/export/home/jaap/sage_port/sage-4.3.2.alpha1

```


Big question: does this work for Solaris 10?

Jaap


---

Comment by jsp created at 2010-02-23 14:33:49

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-02-23 17:00:51

I see no reason this should not work on Linux, but have you checked it? I know  you have a linux build of Sage. Assuming you have checked it on Linux, then I'm happy to give it a positive review. It looks fine to me. 

It does build on Solaris 10 in 32-bit mode on SPARC. I've not tested 64-bit mode, but there is currently no effort being put into a 64-bit port on SPARC, so there is no need for it to work there. 

Positive review, subject to confirmation from you that  you have tested this on Linux. 

Dave


---

Comment by jsp created at 2010-02-23 17:49:24

Replying to [comment:23 drkirkby]:
> I see no reason this should not work on Linux, but have you checked it? I know  you have a linux build of Sage. Assuming you have checked it on Linux, then I'm happy to give it a positive review. It looks fine to me. 
> 
> It does build on Solaris 10 in 32-bit mode on SPARC. I've not tested 64-bit mode, but there is currently no effort being put into a 64-bit port on SPARC, so there is no need for it to work there. 
> 
> Positive review, subject to confirmation from you that  you have tested this on Linux. 
> 
> Dave 


Sure, I tested this on linux. But the change in spkg-install only affected SunOS. So
I was not afraid it would break a linux build.

Jaap


---

Comment by drkirkby created at 2010-02-23 18:36:49

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-02-23 18:36:49

No problem. I think it would be ok, but there is no harm in checking. 

Positive review.


---

Comment by drkirkby created at 2010-02-23 18:41:01

I'm taking myself off this as author, and adding myself as reviewer, as these changes by Jaap are his, and my earlier version was not working completely, so I feel justified in reviewing this. 

I'm going to delete the version I have on boxen, so not to cause any confusion. 

Dave


---

Comment by jsp created at 2010-02-23 18:58:33

I see this ticket is marked as: Ticket #7761 (positive_review defect: fixed)

Fixed? At some time it was merged, but reopened.

Jaap


---

Comment by drkirkby created at 2010-02-23 20:02:10

Remove assignee drkirkby.


---

Comment by drkirkby created at 2010-02-23 20:02:10

Yes, it got merged, but was changed by robertwb  from fixed to needs work. It relied on another patch (#7818) which itself caused problems by setting CFLAGS globally. So whilst my python version worked, the patch it relied on caused other problems. 

Dave


---

Comment by mvngu created at 2010-03-02 23:31:03

Merged [python-2.6.4.p6.spkg](http://boxen.math.washington.edu/home/jsp/ports/python-2.6.4.p6.spkg) in the standard spkg repository.
