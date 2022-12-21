# Issue 7440: optional valgrind spkg doesn't build with newer GCC's

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-12 05:40:01

Assignee: tbd

CC:  was david.kirkby@onetel.net

I tried to build the valgrind_3.3.1 spkg on ubuntu-9.10 and it quickly fails with 

```
configure: error: Valgrind requires glibc version 2.2 - 2.7
error configuring valgrind 3.3.1

real    0m10.843s
user    0m2.928s
sys     0m6.640s
sage: An error occurred while installing valgrind_3.3.1
```



---

Comment by was created at 2009-11-12 05:44:02

I sent this email to sage-devel:

```
Hello,

The valgrind-3.3.1 spkg no longer works with newer Linux installs.
E.g., with Ubuntu-9.10 we get the error:

    configure: error: Valgrind requires glibc version 2.2 - 2.7
    error configuring valgrind 3.3.1

See: http://trac.sagemath.org/sage_trac/ticket/7440

Unfortunately, Michael Abshoff is the official maintainer of this
spkg.  Can somebody else please volunteer to be the Valgrind spkg
maintainer?  If nobody does, then I'll remove valgrind as an optional
spkg (I'll put it in experimental), at least until I have more time
and maintain it myself.

 -- William
```



---

Comment by timdumol created at 2009-12-21 04:32:57

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-12-21 04:32:57

A new package with the latest version of valgrind is here: http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg.


---

Comment by jhpalmieri created at 2009-12-22 05:57:17

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2009-12-22 05:57:17

I tried installing this on Mac OS X 10.6 and got an error during the "configure" process:

```
checking build system type... i686-apple-darwin10.2.0
checking host system type... i686-apple-darwin10.2.0
checking for a supported CPU... ok (i686)
checking for a 64-bit only build... no
checking for a 32-bit only build... no
checking for a supported OS... ok (darwin10.2.0)
checking for the kernel version... unsupported (10.2.0)
configure: error: Valgrind works on Darwin 9.x (Mac OS X 10.5)
error configuring valgrind 3.5.0
```

Seems to build correctly on sage.math, for what that's worth.

Once the OS X issue is worked out, other people should definitely look at this; I don't think I'm qualified to review it properly.


---

Comment by was created at 2009-12-22 17:02:12

Despite the message "Valgrind works on Darwin 9.x", that Valgrind spkg has never built on OS X.  Valgrind was Linux only.   I recently heard that it was ported to OS X, but I'm not sure if that is really the case.   Mabshoff used to tell me that it would be ported any day now...


---

Comment by timdumol created at 2009-12-23 03:39:37

I believe OS X 10.6 is Darwin 10.x, which Valgrind indeed does not support. I have uploaded a new version of the package which checks for the release version here: http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg.


---

Comment by timdumol created at 2009-12-23 03:39:37

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2009-12-24 00:33:49

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2009-12-24 00:33:49

This has a portability bug. 'uname' will will called with the '-p' option on any non-Linux system. But '-p' is not a POSIX option for uname. 

http://www.opengroup.org/onlinepubs/9699919799/utilities/uname.html

so there is no reason any system should support the -p option. If you need to test the processor type, make sure the test is only done on platforms where you know the -p option is supported. HP-UX is one platform where this will fail, and I expect there are others too. 


```
$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
$ uname -p
uname: illegal option -- p
usage: uname [-amnrsvil] [-S nodename]
```


Dave


---

Comment by was created at 2009-12-24 20:30:09

FYI: Valgrind doesn't make any sense on any platforms that don't support 'uname -p'.  The only supported platforms for the latest Valgrind are:  X86/Linux, AMD64/Linux, PPC32/Linux, PPC64/Linux, and X86/Darwin (Mac OS X).  These all support uname -p.


---

Comment by timdumol created at 2009-12-25 04:03:50

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-12-25 04:03:50

Replying to [comment:7 drkirkby]:
> This has a portability bug. 'uname' will will called with the '-p' option on any non-Linux system. But '-p' is not a POSIX option for uname. 

I do not believe this is a problem, since `uname -p` will only be called on Linux and Darwin platforms because of boolean logic shortcircuiting, e.g.:


```
[timdumol`@`tim-pc sage]$ if [ -z "" ] && [ -z "`error`" ]; then echo "Success"; fi
bash: error: command not found
Success
[timdumol`@`tim-pc sage]$ if [ -n "" ] && [ -z "`error`" ]; then echo "Success"; fi
```



---

Comment by drkirkby created at 2009-12-25 14:51:47

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2009-12-25 14:51:47

First, merry Christmas to you both. 

William asked me the other day to check what optional packages installed on Solaris. Valgind did not install, but did give a helpful error message, indicating why. That's much better than executing a command which will fail. So I believe the fact Valgind does not work on Solaris, AIX, HP-UX etc is a not an excuse for sloppy programming - there is enough of that in Sage anyway!

William's use of:

```
elif [ `uname` = "SunOS" -a "`uname -p`" != "sparc" ]; then
```


in an early version of 'prereq' did cause an issue on HP-UX, with the -p option creating problems - see #7156. 

Tim's version is written slighlty different, using the preffered '&&' instead of '-a'. The use of '-a' is deprecated and discouraged by POSIX

http://www.opengroup.org/onlinepubs/009695399/utilities/test.html

so perhaps Tim's arugument is valid. On reflection, I agree with Tim. 

However, as my grandmother used to say, the proof of the pudding is in the eating, so I tested this on HP-UX, where sage-4.2.1 is installed. 


```
valgrind-3.5.0.p0/patches/sage.supp
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
Configured with: /tmp/gcc-4.3.3.tar.gz/gcc-4.3.3/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.3.3 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.3.3 (GCC)
****************************************************
Sorry, Valgrind only works on X86/Linux, AMD64/Linux,
PPC32/Linux, PPC64/Linux and X86/Darwin 9.x
(Mac OS X 10.5.x)

real    0m0.020s
user    0m0.020s
sys     0m0.010s
sage: An error occurred while installing valgrind-3.5.0.p0
```


So I would have to agree, the spkg-install *does* work properly, even on HP-UX. The error message is helpful too. The spkg-install does not fail as I initially expected it would, so I'm changing this to positive review. 

Dave


---

Comment by drkirkby created at 2009-12-25 15:19:39

BTW, I just noticed that Michael Abshoff is the noted as the package maintainer in SPKG.txt. #7738 says he should be removed from all packages, and specificially lists Valgrind. Hence I believe this would be a good oppotunity to remove Michael's name. Does time want to take on the role? 

As such, I'm swapping this back to 'needs work'. It would seem silly to update a package, without addressing this minor issue. Otherwise, I'm happy with this, so will change it back to positive when its done. 

Dave


---

Comment by drkirkby created at 2009-12-25 15:19:39

Changing status from positive_review to needs_work.


---

Comment by drkirkby created at 2009-12-25 15:26:45

That was supposed to be 'does *Tim* want to take on the role?', not 'time' as I said.


---

Comment by timdumol created at 2009-12-28 18:40:35

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-12-28 18:40:35

Replying to [comment:13 drkirkby]:
> BTW, I just noticed that Michael Abshoff is the noted as the package maintainer in SPKG.txt. #7738 says he should be removed from all packages, and specificially lists Valgrind. Hence I believe this would be a good oppotunity to remove Michael's name. Does time want to take on the role? 
> 
> As such, I'm swapping this back to 'needs work'. It would seem silly to update a package, without addressing this minor issue. Otherwise, I'm happy with this, so will change it back to positive when its done. 
> 
> Dave 

Sure, I'll be glad to. New version of spkg up at http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg


---

Comment by drkirkby created at 2009-12-28 19:05:34

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2009-12-28 19:05:34

Due to the problems with Sage (disk related I believe), I unable to download this. But since the only issue was changing someone name in a text file, I'm sure there will be no problem, so I'm changing it to positive review.


---

Comment by rlm created at 2010-01-19 01:34:11

Resolution: fixed


---

Comment by maldun created at 2010-08-28 12:03:25

Changing status from closed to needs_work.


---

Comment by maldun created at 2010-08-28 12:03:25

Now this package has a problem with the new glibc version as well.

I get: 

```
checking for a supported CPU/OS combination... ok (amd64-linux)
checking for use as an inner Valgrind... no
checking for egrep... grep -E
checking the GLIBC_VERSION version... unsupported version
configure: error: Valgrind requires glibc version 2.2 - 2.10
error configuring valgrind 3.5.0
```


I use Ubuntu 10.04, and the glibc version is 2.11 ....
Valgrind 3.6.0 is already out


---

Comment by maldun created at 2010-08-28 12:10:25

Sorry I oversaw ticket #7766: http://trac.sagemath.org/sage_trac/ticket/7766


---

Comment by mvngu created at 2010-08-28 18:11:14

Replying to [comment:18 maldun]:
> Now this package has a problem with the new glibc version as well.

As a general rule, don't reopen a ticket once it is closed. Open a new ticket instead.
