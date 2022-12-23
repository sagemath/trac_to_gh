# Issue 7375: upgrade M4RI to newest upstream release

Issue created by migration from https://trac.sagemath.org/ticket/7375

Original creator: malb

Original creation time: 2009-11-02 11:17:39

Assignee: tbd

CC:  david.kirkby@onetel.net drkirkby

Keywords: M4RI, linear algebra

Improvements in the most recent versions:
  * switched to LQUP instead of PLUQ for better performance
  * because of this and other improvements much better handling of sparse-ish matrices
  * overall better performance for elimination
  * better performance for mzd_transpose
  * dropped the check for the numer of CPUs from configure which was unused and not cross platform
  * optional tuning code to calculate cache sizes (not enabled by default)
   + some refactoring
   + mzd_row_add_offset() fixed a segfault


---

Comment by malb created at 2009-11-02 11:18:15

Changing status from new to needs_review.


---

Comment by malb created at 2009-11-02 11:18:15

The SPKG is here

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20091101.spkg

Dave, can you take a look?


---

Comment by malb created at 2009-11-02 16:30:40

I replaced the same SPKG with a new version which fixes two `sizeof(word) != sizeof(size_t)` bugs that I found while testing on t2.


---

Comment by malb created at 2009-11-03 12:40:43

Again, I replaced the SPKG with an updated one which fixes compiler warnings and errors from Microsoft Visual Studio C++. I should have all platforms accounted for now (I might try the Sun compiler later though)


---

Comment by drkirkby created at 2009-11-18 15:49:54

For some reason I never got a message about this. I will check over this.


---

Comment by malb created at 2009-11-18 16:53:17

A new SPKG which is supposed to fix #7171 is available at

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20091118.spkg


---

Comment by drkirkby created at 2009-11-19 01:55:18

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2009-11-19 01:55:18

Hi, 
I have had a few beers tonight, which are a nice benefit of attending the London Open Solaris User Group (LOSUG), so I hope my comments are coherent! (FWIW, one of tonights talks at LOSUG was very interesting from the point of view of Sage). 

Anyway, back to the trac ticket...There are still some problems with this, which means the configure script believes the Sun compiler is broken. I've also made some other points. Some are _nit-picking_, but while you resolve one issue, you might as well resolve the others. 

The main problem is that spkg-install sets CFLAGS to include -fPIC and -Wall, both of which are GNU specific flags. So when called with the Sun compiler, the compiler fails to build an executable, as its given erroneous flags. That can be seen in the config.log attached. It's essential that flags like those are only added on compilers that accept them. 

I've attached a small script called _testcc_ that I was intending at some point including in a more general place in Sage, but you can use it if you wish. It tests the C compiler and will report one of:

   * GNU  (for any GCC compatible compiler)
   * Sun_on_Solaris (for the Sun compiler on Solaris)
   * Intel_improved_GCC 
   * Sun_improved_GCC
   * HP_on_Alpha_Linux
   * HP_on_HPUX
   * IBM_on_AIX
   * HP_on_Tru64
   * Unknown

The script works by checking what the C pre-processor defines, which is more reliable than looking for words like GNU or Sun in the output. You could use that script to decide what flag to add to the compiler - whether it is -fPIC for GNU compilers, or -Kpic for the Sun compiler. I would not worry about the others at the minute. 

Here is what the script gives as output on both Sun and GNU compilers on a Sun workstation. It's also been tested on AIX, tru64 and HP-UX too. 


```
drkirkby@swan:[~] $ export CC=/opt/xxxsunstudio12.1/bin/cc
drkirkby@swan:[~] $ ./testcc
Sun_on_Solaris
drkirkby@swan:[~] $ export CC=gcc
drkirkby@swan:[~] $ ./testcc
GNU
```


Out of completeness, I'll attach another for the C++ compiler (_testcxx_), but I do not think you will want the one for C++. 

Using that script, you could then add in spkg-install something like the following, which I have not tested. 


```
if [ x`testcc`  = "xGNU" ] ; then 
   CFLAGS="$CFLAGS -fPIC -Wall "
elif [ x`testcc` = "xSun_on_Solaris" ] ; then 
   CLFAGS="$CLFAGS -Kpic "
elif [ x`testcc` = "xHP_on_HPUX" ] ; then
   CFLAGS="$CFLAGS + z "
fi 

```


The Sun compilers are a lot more fussy than the GNU ones, so enabling extra warnings will probably show too many. 

Whilst Sage does not aim to support HP-UX, it would be worth adding that +z flag, as compiling with other compilers tends to show problems in code. The library might build on HP-UX with those changes.) 


Others issues I see are: 

 * -m64 is added only on OS X. I suggest a better alternative would be to have:


```
 if [ "x$SAGE64" = "xyes" ] ; then 
    CFLAGS="$CFLAGS -m64 "
 fi
```


That's far from perfect, but will work with the Sun and GNU compilers, as both accept -m64. 

I do not believe you need to set CPPFLAGS to -m64, as that is not an option for the C pre-processor. But it would be worth double-checking that. 

 * The standard name for the file that creates the configure script was changed from configure.in to configure.ac. So the autoconf manual says to use that. See http://www.gnu.org/software/autocon/manual/autoconf.html#Writing-Autoconf-Input where it says _"Previous versions of Autoconf promoted the name configure.in, which is somewhat ambiguous (the tool needed to process this file is not described by its extension), and introduces a slight confusion with config.h.in and so on (for which ‘.in’ means “to be processed by configure”). Using configure.ac is now preferred."_

 * The autoconf manual says configure.ac should start with AC_INIT, but your configure.in does not. This might possibly be the reason the configure script thinks the compiler is broken, though I doubt it. 

 * Adding something like _AC_PREREQ([2.64])_ or whatever version of autoconf you use to create the configure script will ensure nobody else can recreate it with an older version. It is recommended practice to do that. See http://www.gnu.org/software/autoconf/manual/autoconf.html#Versioning 
 
 * I do not think it is a good idea to test for the Sun compiler in configure.in (or configure.ac), to find what flags the compiler needs for C99 support, for several reasons
   * First, not all Sun compilers need any flag at all. 
   * Other compilers from HP, IBM, Intel etc might need their own flags. 

 A better way to add a flag for c99 support (*if it is needed*), is to call the autoconf macro AC_PROG_CC_C99  http://www.gnu.org/software/autoconf/manual/autoconf.html#C-Compiler That macro was designed for exactly this purpose. As such, you can delete all the code that checks for the Sun compiler in configure.in and just use the built-in macro. It would also be wise to exit with an error if the compiler is not C99 compliant, if that is needed. Test if $ac_cv_prog_cc_c99 = no, and if so exit with an error that the code needs to be able to find a C99 compliant compiler. 


If you can make those changes, this has a reasonable chance of building on Solaris with the Sun compiler. I'll also try it on HP-UX for you. The machine is not running at the minute, but there is no point in even trying, as I know the GNU flags will break the build.


---

Attachment

Checks the type of C compiler, much more thorougly than using grep on output


---

Comment by drkirkby created at 2009-11-19 01:57:21

Teses the C++ compiler. Not really needed here, but done for completelness.


---

Attachment

config.log showing the -Wall and -fPIC flags are causing problems.


---

Comment by malb created at 2009-11-19 10:41:23

Replying to [comment:6 drkirkby]:
> I have had a few beers tonight, which are a nice benefit of attending the London Open Solaris 
> User Group (LOSUG), so I hope my comments are coherent! (FWIW, one of tonights talks at LOSUG 
> was very interesting from the point of view of Sage). 

I had a few beers in London yesterday too but only in the pub down the road :)

 
> I've attached a small script called _testcc_ that I was intending at some point including in 
> a more general place in Sage, but you can use it if you wish. It tests the C compiler and will > report one of:

I am using it in spkg-install now
 

> -m64 is added only on OS X. I suggest a better alternative would be to have:

Changed.

> I do not believe you need to set CPPFLAGS to -m64, as that is not an option for the C pre-
> processor. But it would be worth double-checking that. 

Changed.
 
> The standard name for the file that creates the configure script was changed from configure.in 
> to configure.ac.

Changed.

>  * The autoconf manual says configure.ac should start with AC_INIT, but your configure.in does > not.

It's now at the top.

>  * Adding something like _AC_PREREQ([2.64])_

Added.
  
>  A better way to add a flag for c99 support (*if it is needed*), is to call the autoconf macro AC_PROG_CC_C99

Great, using that now.
 
> If you can make those changes, this has a reasonable chance of building on Solaris with the Sun compiler. I'll also try it on HP-UX for you. The machine is not running at the minute, but there is no point in even trying, as I know the GNU flags will break the build. 

Thanks a lot, this is really really helpful!


---

Comment by malb created at 2009-11-19 10:44:12

The updated SPKG is at

 http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20091119.spkg


---

Comment by drkirkby created at 2009-11-19 17:43:31

Hi, 
I checked libm4ri-20091119.spkg on two UNIX workstations. 

 * Sun Blade 2000, Solaris 10 update 7, 2 x 1200 MHz UltraSPARC IV+ processors, 8 GB RAM, Sun Studio 12.1 compiler. 
 * HP C3600, HP-UX 11.11, 1 x 552 MHz PA-RISC processor, 8 GB RAM, gcc 4.4.0. 

I hope the results of the tests are useful. Sorry if some of these existed in your earlier spkg-install, and I forgot to mention them, but I did admit I was under the influence of alcohol!


 == General points ==

 * In spkg-install, if the tests fail, there is a message generated to say to report this upstream. It would be useful if that message could say where to - i.e. a web site, email address etc. Things are more likely to be reported upstream if someone can easily find where to report it to. I actually like the idea of suggesting to report this upstream. Other packages should follow your example. 

 * Since the current environment script enforces SAGE_64 to be "yes" or "no", then I think for consistency we should do the same for "SAGE_DEBUG". So I would change the 


```
if [ "$SAGE_DEBUG" = "1" ]; 
```

to 

```
if [ "x$SAGE_DEBUG" = "xyes" ]; 
```


However, there was a consensus some time back that the default should be to build with debug information present (-g flag) and only if SAGE_DEBUG was set to "no" should -g not be there. 

However, adding your --enable-debug flag to the configure script might have a serious impact on performance, in which case  you should not enable that by default. You can best judge how to handle that. 

 * One bit of code has this:


```
CFLAGS="$CFLAGS $INCLUDES -L$SAGE_LOCAL/lib -pedantic -g"
```


So -pedantic and -g are CFLAGS. This has two problems. First, -pedantic is a GNU specific flag. Secondly, there is the issue of whether the -g flag should be there or not. The '-g' flag does appear to be a portable flag, so should not be a problem on any compiler I know of. 

Now to the results. 

 == Results on HP-UX 11.11 with gcc 4.4.0 ==

M4RI configured properly, without aborting when trying to find the cache size, as reported in #7171. 

The package went on to compile ok on HP-UX, and passed all tests. That is certainly better than many packages. 

There was however a few things that perhaps can be addressed. One is HP-UX specific, so I would not bother trying to fix that, but the other two I believe will happen on other platforms too.  

 * There were repeated messages about redefining CPU_L1_CACHE and CPU_L2_CACHE. 

```
In file included from src/brilliantrussian.c:22:
src/misc.h:359:1: warning: "CPU_L2_CACHE" redefined
In file included from src/misc.h:33,
                 from src/brilliantrussian.c:22:
src/config.h:8:1: warning: this is the location of the previous definition
In file included from src/brilliantrussian.c:22:
src/misc.h:367:1: warning: "CPU_L1_CACHE" redefined
```


this happened on numerous files. Since the cache size will not be determined on Solaris, I might assume the same would happen there. Is there a way you can work around that, so the warning is not generated? It does not look very impressive to see warnings, but your package is still a *lot* better than many others in this respect. 

 * libtool gave a warning, which is probably specific to HP-UX, so I would certainly not worry about this, but for completeness, the warning was:


```
./m4ri/config.h:5:1: warning: this is the location of the previous definition
	mv -f .deps/test_kernel.Tpo .deps/test_kernel.Po
	/bin/sh ./libtool --tag=CC    --mode=link gcc -std=gnu99    -I/home/drkirkby/sage-4.2/local/include/ -L/home/drkirkby/sage-4.2/local/lib -pedantic -g -fPIC -Wall  -O2  -lm4ri -lm  -o test_kernel test_kernel.o  
libtool: link: warning: this platform does not like uninstalled shared libraries
libtool: link: warning: `test_kernel' will be relinked during installation
```


 * I'm not sure if the following is done by libtool, or whether you have done it, but some bits of code are compiling with gcc with the -Wall option to show all warnings, then sends all warnings to /dev/null. It seems a bit silly. If it in your code, I would suggest you remove it. If it's something done by libtool, and not easily within your control, then leave it. 

So overall, on HP-UX, this is pretty good, though perhaps you can sort out at least the first of these. 

 == Results on Solaris 10 update 7 (SPARC) with Sun Studio 12.1 compiler ==

Here things were not as successful as on HP-UX with gcc. 

4MRI will not build with Sun Studio. 


```
libm4ri-20091119/testcc.sh
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
make: *** No rule to make target `clean'.  Stop.
checking build system type... sparc-sun-solaris2.10
checking host system type... sparc-sun-solaris2.10
checking for a BSD-compatible install... /usr/local/bin/ginstall -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... ./install-sh -c -d
checking for gawk... no
checking for mawk... no
checking for nawk... nawk
checking whether make sets $(MAKE)... yes
checking for style of include used by make... GNU
checking for gcc... /opt/xxxsunstudio12.1/bin/cc
checking for C compiler default output file name... 
configure: error: in `/export/home/drkirkby/sage-4.2/spkg/build/libm4ri-20091119/src':
configure: error: C compiler cannot create executables
See `config.log' for more details.
Error configuring libm4ri

real    0m2.911s
user    0m0.712s
sys     0m1.285s
sage: An error occurred while installing libm4ri-20091119
```


Whilst the -Wall and -fPIC flags are no longer being sent to the compiler, the -pedantic flag is getting to the compiler from spkg-install. I think that is what is preventing the Sun compiler from building an executable. I'm attaching another config.log generated on Solaris with the Sun compiler. I think the reason for the failure is pretty simple to sort out. 

I'm not sure if you need both -Wall and -pedantic (I don't know exactly what they are each supposed to do), but removing the -pedantic flag near the top of spkg-install, and adding in like this:


```
if [ "x$COMPILER"  = "xGNU" ] ; then 
   CFLAGS="$CFLAGS -fPIC -Wall -pedantic"
elif [ "x$COMPILER" = "xSun_on_Solaris" ] ; then 
   CLFAGS="$CLFAGS -Kpic "
elif [ "x$COMPILER" = "xHP_on_HPUX" ] ; then
   CFLAGS="$CFLAGS + z "
fi

```


will probably do the trick. Then it will only get added on GNU compilers, so should not prevent it building on Solaris 10. 

Dave 


Dave


---

Comment by malb created at 2009-11-20 10:12:31

Replying to [comment:10 drkirkby]:
> I hope the results of the tests are useful. Sorry if some of these existed in your earlier spkg-install, and I forgot to mention them, but I did admit I was under the influence of alcohol!

Very helpful indeed! 

> In spkg-install, if the tests fail, there is a message generated to say to report this 
> upstream. It would be useful if that message could say where to

Done.

> Since the current environment script enforces SAGE_64 to be "yes" or "no", then I think for 
> consistency we should do the same for "SAGE_DEBUG". So I would change the 

Okay, why not.
 
> So -pedantic and -g are CFLAGS. This has two problems. First, -pedantic is a GNU specific 
> flag. 

Moved to the GNU specific part.


> M4RI configured properly, without aborting when trying to find the cache size, as reported in #7171. 

If you like you can run `./configure --enable-cachetune` which should get rid of these warnings/issues. It will be default if the static tests failed soon and eventually default as such.
 
>  There were repeated messages about redefining CPU_L1_CACHE and CPU_L2_CACHE. 

See above.

>  * libtool gave a warning, which is probably specific to HP-UX, so I would certainly not worry about this, but for completeness, the warning was:

Doesn't ring a bell, so I won't address this for now.

>  I'm not sure if the following is done by libtool, or whether you have done it, but some bits of code are compiling with gcc with the -Wall option to show all warnings, then sends all warnings to /dev/null

I don't do anything with /dev/null, so I gues it must be in the toolchain.

> 4MRI will not build with Sun Studio. 

This should be fixed now.

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20091120.spkg


---

Comment by drkirkby created at 2009-11-20 11:50:49

Hi,
it now builds fine, and passes all tests on Solaris with the Sun compiler. 

I did not recheck on HP-UX as I have powered the machine off, and it is the garage, but I suspect it will still be fine there. 

But I notice at the top of spkg-install you have 


```
SAGE_DEBUG=0
```


which means you override the value of the environment variable, so it makes any tests pointless. That should be very easy to fix.  

 == Suspect source code found with Sun's lint ==

As you can probably see, I can be a bit picky, but I am keen the quality of software in Sage is improved as much as possible. Some, such as _lcalc_ leaves a lot to be desired in my opinion. The code in there is pretty awful, which means I'd be suspicious myself of trusting any results that make use of _lcalc_. 

Anyway, with that in mind, I decided to have a *quick* look at the M4RI source code. I'm not a mathematician, so I do not understand what is going on, but I did notice a few things, with the aid of 'lint' that I believe need addressing. I'm not an expert using lint, so just did:


```
$ lint *.c
```


in the 'src' directory. Here are a few examples of things I found. I've attached a log of the lint results, so perhaps you can have a look though them, to see if there are things that you should fix. 

In  grayflex.c

```
int m4ri_opt_k(int a,int b,int c) {
  int n = MIN(a,b);
  int res = MIN( MAXKAY, MAX(1, (int)(0.75*log2_floor(n))) );
  return res;
}
```


does not use the argument 'c' at all. 

In permutation.c, the following function


```
void mzp_set_ui(mzp_t *P, unsigned int value) {
  size_t i;
  for (i=0; i<P->length; i++) {
    P->values[i] = i;
  }
}
```

does not use the integer 'value' at any point. 

Line 1180 of strassen.c 

```
 mzd_t* _mzd_addmul_weird_weird (mzd_t* C, mzd_t* A, mzd_t *B, int cutoff){
```


takes a argument 'cutoff' but you never actually use 'cutoff' in that function. 

sqrt() is used in brilliantrussian.c, but the header file math.h is not included.


---

Attachment

Results of running Sun's lint command in the 'src' directory.


---

Comment by malb created at 2009-11-20 12:04:51

I have made your lint suggestions a new ticket at:

   http://bitbucket.org/malb/m4ri/issue/18/cleanup-solaris-lint-warnings

I will address them in due course.

I have replaced the SPKG with a new SPKG which doesn't overwrite SAGE_DEBUG in the spkg-install script.

Is that a positive review then?


---

Comment by drkirkby created at 2009-11-20 12:14:16

Changing status from needs_work to needs_review.


---

Comment by malb created at 2009-11-20 12:20:32

What's holding off the positive review?


---

Comment by was created at 2009-11-20 12:32:49

Looks good to me, based on the above and my own snooping around. 
Well I don't like that 


```
$ hg status
? testcc.sh
```


Positive review subject to checking in testcc.sh somewhere.


---

Comment by was created at 2009-11-20 12:33:01

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2009-11-20 12:41:56

Hi,
I was about to give it a positive!  After this is incorporated, the following two tickets can be closed. 

 * #7171 _HP-UX failure of libm4ri 20090617 as it attempts to find L1 cache size_
 * #7037 _libm4ri thinks the C compiler is broken_

I thought it wise to open a *Sage* ticket for the issues reported by lint to be resolved. (lint should exist on any platform, or if not the source can be found easily). As such, I have opened: 

#7503 _M4RI source code needs looking at, as lint finds some issues._

Thank you for resolving the issues. I wish others would take as much care over fixing issues as you did. 

Dave


---

Comment by drkirkby created at 2009-11-20 12:45:52

BTW, if _testcc.sh_ is checked in outside of the .spkg file, then _testcxx_ (or if you want to call it testcxx.sh), which is attached to this ticket, should be placed in the same place. 

Both have wider use outside of M4RI. But the testcxx is not needed in M4RI. 

Dave


---

Comment by malb created at 2009-11-20 12:52:28

New SPKG with testcc.sh checked in:

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20091120.p0.spkg

I only checked it into the local M4RI SPKG repository. Once it is available globally in Sage, it can be removed again.


---

Comment by drkirkby created at 2009-11-20 16:29:20

Fine. 

I'll try to get the testcc and testcxx reviewed at some point in the future and incorporated a bit more widely. 

When your updated M4RI package is added, the release manager should close these two tickets, as this upgrade fixes both these issues. 

    * #7171 HP-UX failure of libm4ri 20090617 as it attempts to find L1 cache size
    * #7037 libm4ri thinks the C compiler is broken 

Dave


---

Comment by mhansen created at 2009-11-29 05:26:55

Resolution: fixed
