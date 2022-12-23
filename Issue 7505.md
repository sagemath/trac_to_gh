# Issue 7505: Add scripts which check C and C++ compilers, and report what they are.

Issue created by migration from https://trac.sagemath.org/ticket/7505

Original creator: drkirkby

Original creation time: 2009-11-20 18:09:29

Assignee: tbd

CC:  malb david.kirkby@onetel.net was pjeremy

In some parts of Sage, it is desirable to know what compiler is being used - in particular if its gcc or Sun, but there are other cases too. 

The two scripts check the variable CC and CXX, and try to determine what the compiler is. I've no idea where the scripts should go though - ultimately they should be copied to SAGE_LOCAL/bin, but if great if someone can put them in a sensible place to start with. I would be appreciate that. 

The scripts can report one of several answers.  

    * GNU (for GNU gcc, on any platform.)
    * Sun_on_Solaris (for the Sun Studio compiler on Solaris)
    * Intel_improved_GCC (An improved commercial version of gcc by Intel. Compatible with gcc, but supposedly faster)
    * Sun_improved_GCC (A compiler by Sun, that appears to code to be gcc, but uses Sun Studio as a back-end.)
    * HP_on_Alpha_Linux (HP compiler on Alpha hardware running Linux)
    * HP_on_HPUX (HP's commerical compiler on HP-UX)
    * IBM_on_AIX (IBM's commercial compiler on AIX)
    * HP_on_Tru64 (HP's commerical compiler on Tru64)
    * Unknown  (The scripts can't work out what the compiler is). 

These two scripts work by testing what pre-processor directives the compilers test. For example, gcc will define __GNUC__. 

But so will the Intel and Sun compilers which try to be GNU like. But the Intel one will define __INTEL_COMPILER 
Rhe Sun compilers defined __SUNPRO_C  so it's possible to differentiate the GNU, Intel and Sun compilers, even though they all aim to be GCC-like. 
 Compiler documentation was obtained from various sites, and is documented in the scripts. 
 == Testing ==
Obviously a reviewer can test these scripts on any platforms they have access to, but here are some tests I performed. I've not managed to check these scripts on every platform and compiler for which they are aimed to work on, due to lack of access to the hardware. 

 * On a Sun Blade 2000 SPARC box, with Sun Studio 12.1

```
drkirkby@swan:[~] $ uname -a
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
drkirkby@swan:[~] $ echo $CC
/opt/xxxsunstudio12.1/bin/cc
drkirkby@swan:[~] $ echo $CXX
/opt/xxxsunstudio12.1/bin/CC
drkirkby@swan:[~] $ ./testcc
Sun_on_Solaris
drkirkby@swan:[~] $ ./testcxx
Sun_on_Solaris
```


 *  On the same Sun Blade 2000, but with CC and CXX set to gcc and g++

```
drkirkby@swan:[~] $ export CC=gcc
drkirkby@swan:[~] $ export CXX=g++
drkirkby@swan:[~] $ ./testcc 
GNU
drkirkby@swan:[~] $ ./testcxx
GNU
```


 * On a Sun Ultra 27, but with CC defined to be a simple _hello world program_, to prove the code returns _Unknown_ when it can not determine the compiler. 

```
SunOS hawk 5.11 snv_111b i86pc i386 i86pc
bash-3.2$ gcc hello.c -o hello
bash-3.2$ export CC=./hello
bash-3.2$ ./testcc
Unknown
```


 * On an IBM machine running AIX 6.

```
$ uname -a
AIX client9 1 6 00C6B7C04C00
$ export CC=gcc
$ export CXX=g++
$ ./testcc
GNU
$ ./testcxx
GNU
```


 * On the same IBM machine running AIX 6, but with CC and CXX set to the IBM commercial compilers. 

```
$ uname -a
AIX client9 1 6 00C6B7C04C00
$ export CC=/usr/vacpp/bin/xlc
$ export CXX=/usr/vacpp/bin/xlc++
$ ./testcc
IBM_on_AIX
$ ./testcxx
IBM_on_AIX
```


 * On a HP C3600 running HP-UX 11.11, CC and CXX set to GNU compilers. 

```
$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
$ export CC=gcc
$ export CXX=g++
$ ./testcc
GNU
$ ./testcxx
GNU
```


 * On the same HP C3600, but this time using trial versions of HP's commercial C and C++ compilers. 

```
$ export CC=/opt/ansic/bin/cc
$ export CXX=/opt/aCC/bin/aCC
$ ./testcc
HP_on_HPUX
$ ./testcxx
HP_on_HPUX
```


 * On a linux machine (sage.math.washington.edu), with the variable CC and CXX not set. In this case, the exit code is 1, not 0. 

```
kirkby@sage:~$ unset CC
kirkby@sage:~$ unset CXX
kirkby@sage:~$ ./testcc
Sorry, you should define the environment variable CC
kirkby@sage:~$ ./testcxx
Sorry, you should define the environment variable CXX
```


 * On the same Linux machine, but with CC and CXX set to locations of GNU compilers. In one case an absolute path is given, in the other case it is not 

```
kirkby@sage:~$ uname -a
Linux sage.math.washington.edu 2.6.24-23-server #1 SMP Wed Apr 1 22:14:30 UTC 2009 x86_64 GNU/Linux
kirkby@sage:~$ export CC=/usr/bin/gcc
kirkby@sage:~$ export CXX=g++
kirkby@sage:~$ ./testcc
GNU
kirkby@sage:~$ ./testcxx
GNU
```


 * On an Apple (bsd.math.washington.edu) running OS X 

```
[kirkby@bsd ~]$ uname -a
Darwin bsd.local 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386 i386 MacPro1,1 Darwin
[kirkby@bsd ~]$ export CC=gcc
[kirkby@bsd ~]$ export CXX=g++
[kirkby@bsd ~]$ ./testcc
GNU
[kirkby@bsd ~]$ ./testcxx
GNU
```


The code was tested by someone else on Tru64, but I can not show the results of this. 

I have not verified it with the Sun or Intel compilers which are GCC compatible, nor on Alpha linux. In each case, I've used compiler documentation, and hope it is right. 

Dave


---

Comment by drkirkby created at 2009-11-20 18:10:11

Small shell script to check the type of C compiler


---

Attachment

Small shell script to check the type of C++ compiler


---

Attachment


---

Comment by drkirkby created at 2009-11-20 18:14:45

Changing status from new to needs_review.


---

Comment by malb created at 2009-11-21 12:15:00

I was worried that the sage_scripts repository would be installed too late for these scripts but I was wrong. I agree with Mike that this is where these scripts belong.

The only issue I can see is that `# of C++ code, and checking what are defined.` in testcc should be `C code`. There are a few of these copy'n'paste 'errors' in the docs, which are beautiful in general! 

Also, I'd call the scripts `testcc.sh` and `testcxx.sh` to emphasise that they are shell scripts.


---

Comment by drkirkby created at 2009-11-25 03:40:35

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2009-11-25 03:40:35

Thank you for your comments. I am now exactly sure what you mean by the "The only issue I can see is that # of C++ code, and checking what are defined. in testcc should be C code."


I did intend making a change to these scripts. I thought it would be better if they returned 'GNU' for *any* compiler which was like gcc (i.e. whether produced by Sun, Intel or HP), and only gave very specific information about whether it was Sun/Intel/HP if an option was passed to the scripts. This is because, in 99% of cases, the user will only want to know if the compiler acts like gcc, and will probably not care if it the GNU distribution, or an improved one from HP, Intel or Sun. 

Once I know exactly what you mean by your comment, I'll make the changes, rename the files with a .sh extension, and submit again for review. 
Dave


---

Comment by malb created at 2009-11-25 11:31:27

Oh, its just that you talk about C++ in the C script in the comments. That's all.


---

Comment by drkirkby created at 2009-11-27 11:03:10

I made a few changes. 
 * Renamed to testcc.sh and testcxx.sh as suggested
 * Corrected the comment which has C++ in it, when the script was for testing the C++ compiler. 
 * Added a usage message, if the scripts are called with any arguments at all, as they are not designed to be. 
 * Abandoned attempts to find the different variants of gcc. It was more difficult than I thought. 

I'm a bit concerned these need to be available very early on, before bzip2 is built, as that has options which depend on the compiler type, as it creates position independent code, the option for which is not standard. Wherever testcc.sh and testcxx.sh are added, then need execute permission. 

Dave 

Dave


---

Comment by drkirkby created at 2009-11-27 11:03:10

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2009-11-28 22:32:39

I'm uploading a slightly changed version, which changes the output from 'Sun_on_Solaris' to 'Sun_Studio' as I'd overlooked the fact that Sun Studio can be installed on Linux too. 

Dave


---

Comment by drkirkby created at 2009-12-08 11:13:17

I'm a bit worried about where these two files should go. Putting them in the 



```
sage_scripts-$version.spkg
```

 

will *not* be suitable, as this a bzip2 compressed file. Hence bzip2 needs to be built before that can extracted. But these two scripts which test the compiler needs to be available before bzip2 is compiled. They need to be available before bzip2 is compiled - particularly since bzip2 does have some compiler-specific flags, as it creates a shared library. 

Dave


---

Comment by malb created at 2009-12-08 12:03:38

Hi, sorry for letting it bitrot so long. The scripts are fine, so you get a positive review as soon as we figured out where to put them. How about adding them to the *prereq SPKG*?


---

Comment by drkirkby created at 2009-12-08 14:55:00

Hi,
the prereq spkg seems a good idea, as that is a tar file, so needed nothing to extract it. I'll add that later today - I am in the middle of decorating now, and being the winter, there are not many daylight hours here in the UK

Dave


---

Comment by drkirkby created at 2009-12-08 23:25:46

Having looked at prereq, it is not a collection of scripts, so I do not believe that is the appropriate place for them. 

I believe if the two scripts are put in the directory 


```
$SAGE_ROOT/spkg/base/
```


and the file 


```
$SAGE_ROOT/spkg/install
```


is updated to copy these two scripts to $SAGE_LOCAL/bin (as it does some other files), then that will solve the problem. That 'SAGE_ROOT/spkg/install' script is run very early (before even prereq), so an added bonus is that the script could be called from within prereq if needed. 

I'm not sure how to check these in properly though vi hg. I've never got to grips with that properly. I'll drop you an email about that. 

I'm attaching the revised install script, and the patch file. 

Dave


---

Attachment

Updated 'install' scipt which copies testcc.sh and testcxx.sh to $SAGE_LOCAL/bin


---

Attachment

Patch, showing changes between the old an new versions of the install script


---

Comment by drkirkby created at 2009-12-20 12:58:45

The review of this has got a bit complex, mainly since agreeing where the scripts should go has not been without some problem, but I also slightly changed the output shown, in view of difficulty of the fact Sun Studio can be run on Solaris, and difficulties finding some information I wanted. 

Hence I thought I'd clarify some things. 

The scripts output one of:

 * GCC
 * Sun_Studio
 * HP_on_Tru64
 * HP_on_Alpha_Linux
 * HP_on_HP-UX
 * IBM_on_AIX
 * Unknown

I believe the scripts (see attached) should be:

```
$SAGE_ROOT/spkg/base/testcc.sh
$SAGE_ROOT/spkg/base/testcxx.sh
```

The file

```
$SAGE_ROOT/spkg/install
```

needs to be modified (patch attached), so it copies the two scripts to 

```
$SAGE_LOCAL/bin
```


in addition to the files it already copies there. This allows the scripts to be called from anywhere, including the prereq script, which might be necessary. 

The scripts can't actually break anything in Sage, as they are not called at all. But calling them will simplify a lot of portability issues later one. 

Dave


---

Comment by drkirkby created at 2009-12-20 12:58:45

Changing priority from minor to major.


---

Comment by drkirkby created at 2009-12-20 13:01:40

Oops, I mean the fact Sun Studio could be run on *Linux* caused me to change the output - everyone known they can run on Solaris!


---

Comment by drkirkby created at 2009-12-30 02:07:36

Changing status from needs_review to needs_work.


---

Attachment

Peter Jeremy has found a cleaner way of testing the compiler, which I intend using. It makes use of the pre-processor in exactly the same way, but it is simpler to maintain, they way Peter wrote it. 

This needs a bit of further testing, so I've stuck it back to 'needs work' for now. Then hopefully it can be reviewed when I've uploaded a couple of revised versions of testcc.sh and testcxx.sh

Dave


---

Attachment

Simpler version of file to check the c-compiler


---

Attachment

Simpler version of file to check the C++ compiler


---

Comment by drkirkby created at 2009-12-30 16:00:17

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2009-12-30 16:02:28

Here are revised versions of the scripts, which report the compiler type. They use the same method as before (checking was macros are predefined), but avoid the use of some grep statments and generally look a lot cleaner. Thank you Peter for the revisions. 

Dave


---

Attachment

A patch to be used in place of Martin's earlier version.


---

Comment by was created at 2009-12-31 16:31:51

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-12-31 16:31:51

REFEREE REPORT:

Please read everything below before making any changes.

1. In the usage it says:
"Will return one of the following, to indicate the C compiler". 
However, shell scripts don't return anything.  It is more precise to say "Will print one of the following to stdout, to indicate the C compiler."

2. I would expect to also get the usage message when CC isn't defined. 

```
flat:Downloads wstein$ ./testcc.sh
Sorry, you must define the environment variable CC
```


Currently, the *only* way to get the usage is to call the command with an extra argument (in which case one doesn't get an error message, by the way):

```
flat:Downloads wstein$ ./testcc.sh foo
Usage: ./testcc.sh
  Will return one of the following, to indicate the C compiler
...
```




3. Perhaps change the message to say "You must export the CC environment variable", because of course defining the CC variable as instructed above doesn't work:

```
flat:Downloads wstein$ CC=gcc
flat:Downloads wstein$ ./testcc.sh 
Sorry, you must define the environment variable CC
flat:Downloads wstein$ CC=gcc; export CC
flat:Downloads wstein$ ./testcc.sh 
GCC
```


4. I wonder about the design. If I were writing this script I would make it take a single argument:

```
$  ./testcc.sh <path to compiler>
```

instead of using an environment variable.   Then the usage info would naturally be printed no matter what when one does 

```
$ ./testcc.sh
```

and one doesn't have to mess with (= muck up) the environment at all in order to use this command.     You could use it like you already plan to by just doing

```
testcc.sh "$CC"
```

To me, that would fit much, much better with standard conventions for command line tools. 

5. I think the script should immediately bail in case 

```
TESTFILE=/tmp/test.$$.c
```

already exists.  Its entirely possible somebody else makes a shell script that uses a similar "strategy" for making temp files and your script just clobbers them.  (The right way to make temp files is to use the tmpfile C library calls.  It would be reasonably easy to rewrite this script, say in Python, to do that, and then temp files would be properly handled and never clash.  This should be done later, since your script is nicely laying down the interface.   Yes, this would depend on some Python being installed system-wide, but that's OK.)

Maybe you could completely avoid using temp files by using - to get input from stdin, e.g. use `$CC -` and pipe the input in. 

```
$ echo "main(){}" | gcc - -E
# 1 "<stdin>"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "<stdin>"
main(){}
```



SUMMARY: I personally think that testcc and testcxx should take one command line argument instead of using the environment to pass arguments.  Their documentation could be slightly clarified.  The use of the temp file could also be very slightly made more robust.   In fact -- much better -- perhaps just rewrite the script to not use temp files at all. 

Sorry for being so picky.  It's just because I just spent a bunch of my limited time reading through this all very carefully and just want to contribute something of value.


---

Comment by drkirkby created at 2009-12-31 17:44:48

Thank you for the helpful comments. 

 * I agree about the documentation. That is easy to fix. 
 * I'll change them so they take a command line argument as the compiler, rather than use CC and CXX. 
 * These scripts are designed to improve portability and should therefore not rely on having python installed. Neither my HP-UX box or the AIX box I use at Metamodul.com has python. I expect the same would be true of many cut-down Linux installations on mobile phones and similar. That's a definite no-no as far as I am concerned. 
 * I did try an earlier version where no temp file was created, but it did not work as intended. I was involved in some discussion about this on comp.unix.shell, but creating the file inline was not working. I'd rather not revisit that. 
 * I would have thought it *extremely* unlikely for the temp file to clobber anything else.    
  * First, the Unix file permissions would prevent it unless someone was stupid enough to set their UMASK in such a way to allow anyone else to write over their files. If they do that, I suspect having a temp file clobbered would be the least of their worries. 
  * Secondly, the filename contains the unique PID of the process. It's a common technique to include the PID like this, as the PID is unique at any one time. It would not be acceptable for a security application where I would worry about race conditions, fake files etc. But that is not an issue. I know 'mktemp' exists on many platforms, but not all. It is not part of POSIX. So that is another no-no. In any case, the extension is important here otherwise the compilers will probably not understand it. Would it be acceptable to you if the file name was much more complex, say 
 {{{
/tmp/hkldfz-test-for-c-compiler-6sokljkhsdhfdf.$$.c 
 }}}
  Even if two people run the same program, at the same time, on the same system, this would not result in a file being clobbered. Since /tmp is not shared amount different computers, it could never be an issue across networks either. 

Dave


---

Comment by mvngu created at 2009-12-31 18:41:50

based on Sage 4.3


---

Attachment

version of kirkby's patch suitable for applying to spkg/base repository


---

Comment by mvngu created at 2009-12-31 19:23:06

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by mvngu created at 2009-12-31 19:25:27

The patch `trac_7505-test-scripts.patch` contains two shell scripts: one for testing the type of C compiler, and the other for testing the type of C++ compiler. Here are the results of my testing them on different combinations of platform and hardware:

 * AIX 6.1 (access provided by OpenAIX at http://www.metamodul.com/10.html), PowerPC_POWER5 `@` 2097 MHz, with GCC 4.2.4. Unfortunately, the license for the IBM commercial compilers on this machine has expired, so I wasn't able to use those IBM compilers to test the scripts.
 {{{
[mvngu`@`client9 ~]$ gcc -v
Using built-in specs.
Target: powerpc-ibm-aix5.3.0.0
Configured with: ../stage/gcc-4.2.4/configure --disable-shared 
--enable-threads=posix --prefix=/opt/pware --with-long-double-128 
--with-mpfr=/opt/pware --with-gmp=/opt/pware
Thread model: aix
gcc version 4.2.4
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`client9 ~]$ uname -a
AIX client1 1 6 00C6B7C04C00
[mvngu`@`client9 ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`client9 ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now set CC and CXX to gcc and g++:
 {{{
[mvngu`@`client9 ~]$ uname -a
AIX client1 1 6 00C6B7C04C00
[mvngu`@`client9 ~]$ export CC=gcc
[mvngu`@`client9 ~]$ export CXX=g++
[mvngu`@`client9 ~]$ ./testcc.sh 
GCC
[mvngu`@`client9 ~]$ ./testcxx.sh 
GCC
 }}}
 * Cygwin on Windows XP (winxp1 on boxen.math), Intel(R) Xeon(R) CPU X7460  `@` 2.66GHz, with GCC 3.4.4 and GCC 4.3.2:
 {{{
mvngu`@`winxp ~
$ gcc -v
Using built-in specs.
Target: i686-pc-cygwin
Configured with: /gnu/gcc/package/gcc4-4.3.2-2/src/gcc-4.3.2/configure 
--srcdir=/gnu/gcc/package/gcc4-4.3.2-2/src/gcc-4.3.2 --prefix=/usr 
--exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --libexecdir=/usr/sbin
--datadir=/usr/share --localstatedir=/var --sysconfdir=/etc 
--infodir=/usr/share/info --mandir=/usr/share/man --datadir=/usr/share 
--infodir=/usr/share/info --mandir=/usr/share/man -v --with-gmp=/usr 
--with-mpfr=/usr --enable-bootstrap --enable-version-specific-runtime-libs 
--with-slibdir=/usr/bin --libexecdir=/usr/lib --enable-static --enable-shared 
--enable-shared-libgcc --enable-__cxa_atexit --with-gnu-ld --with-gnu-as 
--with-dwarf2 --disable-sjlj-exceptions 
--enable-languages=ada,c,c++,fortran,java,objc,obj-c++ --disable-symvers 
--enable-libjava --program-suffix=-4 --enable-libgomp --enable-libssp 
--enable-libada --enable-threads=posix 
AS=/opt/gcc-tools/bin/as.exe 
AS_FOR_TARGET=/opt/gcc-tools/bin/as.exe LD=/opt/gcc-tools/bin/ld.exe
LD_FOR_TARGET=/opt/gcc-tools/bin/ld.exe
Thread model: posix
gcc version 4.3.2 20080827 (beta) 2 (GCC)
mvngu`@`winxp ~
$ cc -v
Reading specs from /usr/lib/gcc/i686-pc-cygwin/3.4.4/specs
Configured with: /managed/gcc-build/final-v3-bootstrap/gcc-3.4.4-999/configure 
--verbose --program-suffix=-3 --prefix=/usr --exec-prefix=/usr --sysconfdir=/etc
--libdir=/usr/lib --libexecdir=/usr/lib --mandir=/usr/share/man 
--infodir=/usr/share/info --enable-languages=c,ada,c++,d,f77,pascal,java,objc 
--enable-nls --without-included-gettext --enable-version-specific-runtime-libs 
--without-x --enable-libgcj --disable-java-awt --with-system-zlib 
--enable-interpreter --disable-libgcj-debug --enable-threads=posix 
--enable-java-gc=boehm --disable-win32-registry --enable-sjlj-exceptions 
--enable-hash-synchronization --enable-libstdcxx-debug
Thread model: posix
gcc version 3.4.4 (cygming special, gdc 0.12, using dmd 0.125)
 }}}
 Without setting CC and CXX:
 {{{
mvngu`@`winxp ~
$ uname -a
CYGWIN_NT-5.1 winxp 1.5.25(0.156/4/2) 2008-06-12 19:34 i686 Cygwin

mvngu`@`winxp ~
$ ./testcc.sh 
Sorry, you must define the environment variable CC

mvngu`@`winxp ~
$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now set CC and CXX to GCC 3.4.4:
 {{{
mvngu`@`winxp ~
$ uname -a
CYGWIN_NT-5.1 winxp 1.5.25(0.156/4/2) 2008-06-12 19:34 i686 Cygwin

mvngu`@`winxp ~
$ export CC=cc

mvngu`@`winxp ~
$ export CXX=c++

mvngu`@`winxp ~
$ ./testcc.sh 
GCC

mvngu`@`winxp ~
$ ./testcxx.sh 
GCC
 }}}
 Now set CC and CXX to use GCC 4.3.2 20080827 (beta) 2:
 {{{
mvngu`@`winxp ~
$ uname -a
CYGWIN_NT-5.1 winxp 1.5.25(0.156/4/2) 2008-06-12 19:34 i686 Cygwin

mvngu`@`winxp ~
$ export CC=gcc

mvngu`@`winxp ~
$ export CXX=g++

mvngu`@`winxp ~
$ ./testcc.sh 
GCC

mvngu`@`winxp ~
$ ./testcxx.sh 
GCC
 }}}
 * Fedora 12 (cicero on SkyNet), Intel(R) Pentium(R) 4 CPU 2.66GHz, GCC 4.4.2:
 {{{
[mvngu`@`cicero ~]$ gcc -v
Using built-in specs.
Target: i686-pc-linux-gnu
Configured with: /usr/local/gcc-4.4.2/src/gcc-4.4.2/configure 
--enable-languages=c,c++,fortran --with-gnu-as 
--with-as=/usr/local/binutils-2.20/x86-Linux-pentium4-gcc-4.4.2/bin/as 
--with-gnu-ld 
--with-ld=/usr/local/binutils-2.20/x86-Linux-pentium4-gcc-4.4.2/bin/ld 
--with-gmp=/usr/local/mpir-1.2.1/x86-Linux-pentium4-gcc-4.4.0 
--with-mpfr=/usr/local/mpfr-2.4.1/x86-Linux-pentium4-mpir-1.2.1-gcc-4.4.0 
--prefix=/usr/local/gcc-4.4.2/x86-Linux-pentium4-binutils-2.20
Thread model: posix
gcc version 4.4.2 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`cicero ~]$ uname -a
Linux cicero 2.6.31.6-145.fc12.i686 #1 SMP Sat Nov 21 16:28:23 EST 2009 i686 i686 i386 GNU/Linux
[mvngu`@`cicero ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`cicero ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`cicero ~]$ uname -a
Linux cicero 2.6.31.6-145.fc12.i686 #1 SMP Sat Nov 21 16:28:23 EST 2009 i686 i686 i386 GNU/Linux
[mvngu`@`cicero ~]$ export CC=gcc
[mvngu`@`cicero ~]$ export CXX=g++
[mvngu`@`cicero ~]$ ./testcc.sh 
GCC
[mvngu`@`cicero ~]$ ./testcxx.sh 
GCC
 }}}
 * Fedora 12 (eno on SkyNet), Intel(R) Core(TM)2 Quad CPU Q6600 `@` 2.40GHz, GCC 4.4.2:
 {{{
[mvngu`@`eno ~]$ gcc -v
Using built-in specs.
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.4.2/src/gcc-4.4.2/configure 
--enable-languages=c,c++,fortran --with-gnu-as 
--with-gnu-as=/usr/local/binutils-2.20/x86_64-Linux-core2-fc-gcc-4.4.2/bin/as 
--with-gnu-ld 
--with-ld=/usr/local/binutils-2.20/x86_64-Linux-core2-fc-gcc-4.4.2/bin/ld 
--with-gmp=/usr/local/mpir-1.2.1/x86_64-Linux-core2-gcc-4.4.0 
--with-mpfr=/usr/local/mpfr-2.4.1/x86_64-Linux-core2-mpir-1.2.1-gcc-4.4.0 
--prefix=/usr/local/gcc-4.4.2/x86_64-Linux-core2-fc-binutils-2.20
Thread model: posix
gcc version 4.4.2 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`eno ~]$ uname -a
Linux eno 2.6.31.6-166.fc12.x86_64 #1 SMP Wed Dec 9 10:46:22 EST 2009 x86_64 x86_64 x86_64 GNU/Linux
[mvngu`@`eno ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`eno ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`eno ~]$ uname -a
Linux eno 2.6.31.6-166.fc12.x86_64 #1 SMP Wed Dec 9 10:46:22 EST 2009 x86_64 x86_64 x86_64 GNU/Linux
[mvngu`@`eno ~]$ export CC=gcc
[mvngu`@`eno ~]$ export CXX=g++
[mvngu`@`eno ~]$ ./testcc.sh 
GCC
[mvngu`@`eno ~]$ ./testcxx.sh 
GCC
 }}}
 * Fedora 12 (lena on SkyNet), AMD Phenom(tm) II X4 940 Processor, GCC 4.4.2:
 {{{
[mvngu`@`lena ~]$ gcc -v
Using built-in specs.
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.4.2/src/gcc-4.4.2/configure 
--enable-languages=c,c++,fortran --with-gnu-as 
--with-gnu-as=/usr/local/binutils-2.20/x86_64-Linux-k10-gcc-4.4.2/bin/as 
--with-gnu-ld 
--with-ld=/usr/local/binutils-2.20/x86_64-Linux-k10-gcc-4.4.2/bin/ld 
--with-gmp=/usr/local/mpir-1.2.1/x86_64-Linux-k10-gcc-4.1.2-rh 
--with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-k10-mpir-1.2.1-gcc-4.4.2-rh 
--prefix=/usr/local/gcc-4.4.2/x86_64-Linux-k10-fc
Thread model: posix
gcc version 4.4.2 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`lena ~]$ uname -a
Linux lena 2.6.31.6-145.fc12.x86_64 #1 SMP Sat Nov 21 15:57:45 EST 2009 x86_64 x86_64 x86_64 GNU/Linux
[mvngu`@`lena ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`lena ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`lena ~]$ uname -a
Linux lena 2.6.31.6-145.fc12.x86_64 #1 SMP Sat Nov 21 15:57:45 EST 2009 x86_64 x86_64 x86_64 GNU/Linux
[mvngu`@`lena ~]$ export CC=gcc
[mvngu`@`lena ~]$ export CXX=g++
[mvngu`@`lena ~]$ ./testcc.sh 
GCC
[mvngu`@`lena ~]$ ./testcxx.sh 
GCC
 }}}
 * HP-UX 11i (David Kirkby's machine), PA-RISC processor `@` 552 MHz, GCC 4.3.3 and HP-UX C/C++ compilers:
 {{{
[mvngu`@`hpbox ~]$ /opt/hp-gcc-4.3.3/bin/gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.3.3.tar.gz/gcc-4.3.3/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.3.3 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.3.3 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`hpbox ~]$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
[mvngu`@`hpbox ~]$ ./testcc.sh                                                   
Sorry, you must define the environment variable CC
[mvngu`@`hpbox ~]$ ./testcxx.sh                                                  
Sorry, you should define the environment variable CXX
 }}}
 Now set CC and CXX to use GCC:
 {{{
[mvngu`@`hpbox ~]$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
[mvngu`@`hpbox ~]$ export CC=/opt/hp-gcc-4.3.3/bin/gcc                           
[mvngu`@`hpbox ~]$ export CXX=/opt/hp-gcc-4.3.3/bin/g++                          
[mvngu`@`hpbox ~]$ ./testcc.sh                                                   
GCC
[mvngu`@`hpbox ~]$ ./testcxx.sh                                                  
GCC
 }}}
 Now set CC and CXX to use HP-UX compilers:
 {{{
[mvngu`@`hpbox ~]$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
[mvngu`@`hpbox ~]$ export CC=/opt/ansic/bin/cc                                   
[mvngu`@`hpbox ~]$ export CXX=/opt/aCC/bin/aCC                                   
[mvngu`@`hpbox ~]$ ./testcc.sh                                                   
HP_on_HP-UX
[mvngu`@`hpbox ~]$ ./testcxx.sh                                                  
HP_on_HP-UX
 }}}
 * Mac OS X 10.4.11 (my own MacBook), Intel Core 2 Duo 2 GHz, GCC 4.0.1:
 {{{
[mvngu`@`darkstar mvngu]$ gcc -v
Using built-in specs.
Target: i686-apple-darwin8
Configured with: /private/var/tmp/gcc/gcc-5367.obj~1/src/configure 
--disable-checking -enable-werror --prefix=/usr --mandir=/share/man 
--enable-languages=c,objc,c++,obj-c++ 
--program-transform-name=/<sup>[cg][</sup>.-]*$/s/$/-4.0/ 
--with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib 
--build=powerpc-apple-darwin8 --with-arch=nocona --with-tune=generic 
--program-prefix= --host=i686-apple-darwin8 --target=i686-apple-darwin8
Thread model: posix
gcc version 4.0.1 (Apple Computer, Inc. build 5367)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`darkstar mvngu]$ uname -a
Darwin darkstar.local 8.11.1 Darwin Kernel Version 8.11.1: Wed Oct 10 18:23:28 PDT 2007; root:xnu-792.25.20~1/RELEASE_I386 i386 i386
[mvngu`@`darkstar mvngu]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`darkstar mvngu]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`darkstar mvngu]$ uname -a
Darwin darkstar.local 8.11.1 Darwin Kernel Version 8.11.1: Wed Oct 10 18:23:28 PDT 2007; root:xnu-792.25.20~1/RELEASE_I386 i386 i386
[mvngu`@`darkstar mvngu]$ export CC=gcc
[mvngu`@`darkstar mvngu]$ export CXX=g++
[mvngu`@`darkstar mvngu]$ ./testcc.sh 
GCC
[mvngu`@`darkstar mvngu]$ ./testcxx.sh 
GCC
 }}}
 * Mac OS X 10.6.2 (bsd.math), Dual-Core Intel Xeon 2.66 GHz, GCC 4.2.1:
 {{{
[mvngu`@`bsd mvngu]$ gcc -v
Using built-in specs.
Target: i686-apple-darwin10
Configured with: /var/tmp/gcc/gcc-5646.1~2/src/configure --disable-checking 
--enable-werror --prefix=/usr --mandir=/share/man 
--enable-languages=c,objc,c++,obj-c++ 
--program-transform-name=/<sup>[cg][</sup>.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib 
--build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 
--program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 
--target=i686-apple-darwin10
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5646) (dot 1)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`bsd mvngu]$ uname -a
Darwin bsd.local 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386
[mvngu`@`bsd mvngu]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`bsd mvngu]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`bsd mvngu]$ uname -a
Darwin bsd.local 10.2.0 Darwin Kernel Version 10.2.0: Tue Nov  3 10:37:10 PST 2009; root:xnu-1486.2.11~1/RELEASE_I386 i386
[mvngu`@`bsd mvngu]$ export CC=gcc
[mvngu`@`bsd mvngu]$ export CXX=g++
[mvngu`@`bsd mvngu]$ ./testcc.sh 
GCC
[mvngu`@`bsd mvngu]$ ./testcxx.sh 
GCC
 }}}
 * openSUSE 11.1 (menas on SkyNet), Intel(R) Core(TM)2 Quad CPU Q6600 `@` 2.40GHz, GCC 4.4.2:
 {{{
[mvngu`@`menas ~]$ gcc -v
Using built-in specs.
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.4.2/src/gcc-4.4.2/configure 
--enable-languages=c,c++,fortran --with-gnu-as 
--with-as=/usr/local/binutils-2.20/x86_64-Linux-core2-suse-gcc-4.4.2/bin/as 
--with-gnu-ld 
--with-ld=/usr/local/binutils-2.20/x86_64-Linux-core2-suse-gcc-4.4.2/bin/ld 
--with-gmp=/usr/local/mpir-1.2.1/x86_64-Linux-core2-gcc-4.4.0 
--with-mpfr=/usr/local/mpfr-2.4.1/x86_64-Linux-core2-mpir-1.2.1-gcc-4.4.0 
--prefix=/usr/local/gcc-4.4.2/x86_64-Linux-core2-suse-binutils-2.20
Thread model: posix
gcc version 4.4.2 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`menas ~]$ uname -a
Linux menas 2.6.27.39-0.2-default #1 SMP 2009-11-23 12:57:38 +0100 x86_64 x86_64 x86_64 GNU/Linux
[mvngu`@`menas ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`menas ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`menas ~]$ uname -a
Linux menas 2.6.27.39-0.2-default #1 SMP 2009-11-23 12:57:38 +0100 x86_64 x86_64 x86_64 GNU/Linux
[mvngu`@`menas ~]$ export CC=gcc
[mvngu`@`menas ~]$ export CXX=g++
[mvngu`@`menas ~]$ ./testcc.sh 
GCC
[mvngu`@`menas ~]$ ./testcxx.sh 
GCC
 }}}
 * Red Hat Enterprise Linux Server 5.3 (cleo on SkyNet), IA-64 Itanium 2, GCC 4.4.2:
 {{{
[mvngu`@`cleo ~]$ gcc -v
Using built-in specs.
Target: ia64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.4.2/src/gcc-4.4.2/configure 
--enable-languages=c,c++,fortran --with-gnu-as 
--with-as=/usr/local/binutils-2.20/ia64-Linux-rhel-gcc-4.4.2/bin/as 
--with-gnu-ld 
--with-ld=/usr/local/binutils-2.20/ia64-Linux-rhel-gcc-4.4.2/bin/ld 
--with-gmp=/usr/local/mpir-1.2.1/ia64-Linux-rhel-gcc-4.4.0 
--with-mpfr=/usr/local/mpfr-2.4.1/ia64-Linux-mpir-1.2.1-gcc-4.4.0 
--prefix=/usr/local/gcc-4.4.2/ia64-Linux-rhel-binutils-2.20
Thread model: posix
gcc version 4.4.2 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`cleo ~]$ uname -a
Linux cleo 2.6.18-128.1.1.el5 #1 SMP Mon Jan 26 13:57:09 EST 2009 ia64 ia64 ia64 GNU/Linux
[mvngu`@`cleo ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`cleo ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`cleo ~]$ uname -a
Linux cleo 2.6.18-128.1.1.el5 #1 SMP Mon Jan 26 13:57:09 EST 2009 ia64 ia64 ia64 GNU/Linux
[mvngu`@`cleo ~]$ export CC=gcc
[mvngu`@`cleo ~]$ export CXX=g++
[mvngu`@`cleo ~]$ ./testcc.sh 
GCC
[mvngu`@`cleo ~]$ ./testcxx.sh 
GCC
 }}}
 * Red Hat Enterprise Linux Server 5.4 (rosemary.math), Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz, GCC 4.1.2:
 {{{
[wstein`@`rosemary mvngu]$ gcc -v
Using built-in specs.
Target: x86_64-redhat-linux
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-libgcj-multifile --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk --disable-dssi --enable-plugin --with-java-home=/usr/lib/jvm/java-1.4.2-gcj-1.4.2.0/jre --with-cpu=generic --host=x86_64-redhat-linux
Thread model: posix
gcc version 4.1.2 20080704 (Red Hat 4.1.2-46)
 }}}
 Without setting CC and CXX:
 {{{
[wstein`@`rosemary mvngu]$ uname -a
Linux rosemary.math.uga.edu 2.6.18-164.2.1.el5 #1 SMP Mon Sep 21 04:37:42 EDT 2009 x86_64 x86_64 x86_64 GNU/Linux
[wstein`@`rosemary mvngu]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[wstein`@`rosemary mvngu]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set to use GCC:
 {{{
[wstein`@`rosemary mvngu]$ uname -a
Linux rosemary.math.uga.edu 2.6.18-164.2.1.el5 #1 SMP Mon Sep 21 04:37:42 EDT 2009 x86_64 x86_64 x86_64 GNU/Linux
[wstein`@`rosemary mvngu]$ export CC=gcc
[wstein`@`rosemary mvngu]$ export CXX=g++
[wstein`@`rosemary mvngu]$ ./testcc.sh 
GCC
[wstein`@`rosemary mvngu]$ ./testcxx.sh 
GCC
 }}}
 * Solaris 10 (fulvia on SkyNet), i386 CPU `@` 2400 MHz, Sun Studio 12 and GCC 4.4.2:
 {{{
[mvngu`@`fulvia ~]$ /usr/local/SunStudio12-200709/x86_64-SunOS/SUNWspro/bin/cc -V                                                                                                                                                   
cc: Sun C 5.9 SunOS_i386 Patch 124868-01 2007/07/12
[mvngu`@`fulvia ~]$ /usr/local/SunStudio12-200709/x86_64-SunOS/SUNWspro/bin/CC -V
CC: Sun C++ 5.9 SunOS_i386 Patch 124864-01 2007/07/25
[mvngu`@`fulvia ~]$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.10
Configured with: /usr/local/gcc-4.4.2/src/gcc-4.4.2/configure 
--enable-languages=c,c++,fortran --with-gnu-as 
--with-as=/usr/local/binutils-2.20/x86_64-SunOS-core2-gcc-4.4.2/bin/as 
--with-gnu-ld 
--with-ld=/usr/local/binutils-2.20/x86_64-SunOS-core2-gcc-4.4.2/bin/ld 
--with-gmp=/usr/local/mpir-1.2.1/x86_64-SunOS-core2-gcc-4.4.0-abi32 
--with-mpfr=/usr/local/mpfr-2.4.1/x86_64-SunOS-core2-mpir-1.2.1-gcc-4.4.0-abi32
--prefix=/usr/local/gcc-4.4.2/x86_64-SunOS-core2-binutils-2.20
Thread model: posix
gcc version 4.4.2 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`fulvia ~]$ uname -a
SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc
[mvngu`@`fulvia ~]$ ./testcc.sh                                                  
Sorry, you must define the environment variable CC
[mvngu`@`fulvia ~]$ ./testcxx.sh                                                 
Sorry, you should define the environment variable CXX
 }}}
 Now set CC and CXX to gcc and g++:
 {{{
[mvngu`@`fulvia ~]$ uname -a
SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc
[mvngu`@`fulvia ~]$ export CC=gcc                                                
[mvngu`@`fulvia ~]$ export CXX=g++                                               
[mvngu`@`fulvia ~]$ ./testcc.sh                                                  
GCC
[mvngu`@`fulvia ~]$ ./testcxx.sh                                                 
GCC
 }}}
 Now set CC and CXX to use Sun Studio 12:
 {{{
[mvngu`@`fulvia ~]$ uname -a
SunOS fulvia 5.10 Generic_127128-11 i86pc i386 i86pc
[mvngu`@`fulvia ~]$ export CC=/usr/local/SunStudio12-200709/x86_64-SunOS/SUNWspro/bin/cc                                                                                                                                            
[mvngu`@`fulvia ~]$ export CXX=/usr/local/SunStudio12-200709/x86_64-SunOS/SUNWspro/bin/CC                                                                                                                                           
[mvngu`@`fulvia ~]$ ./testcc.sh                                                                                                                                                                                                     
Sun_Studio
[mvngu`@`fulvia ~]$ ./testcxx.sh                                                                                                                                                                                                    
Sun_Studio
 }}}
 * Solaris 10 (t2.math), SPARC T5240, with Sun Studio 12 and GCC 4.4.1:
 {{{
[mvngu`@`t2 ~]$ /opt/SUNWspro/prod/bin/cc -V
cc: Sun C 5.9 SunOS_sparc Patch 124867-11 2009/04/30
usage: cc [ options] files.  Use 'cc -flags' for details
[mvngu`@`t2 ~]$ /opt/SUNWspro/prod/bin/CC -V
CC: Sun C++ 5.9 SunOS_sparc Patch 124863-17 2009/10/27
[mvngu`@`t2 ~]$ gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.1/configure 
--prefix=/usr/local/gcc-4.4.1-sun-linker/ --with-as=/usr/ccs/bin/as 
--without-gnu-as --with-ld=/usr/ccs/bin/ld --without-gnu-ld 
--enable-languages=c,c++,fortran --with-mpfr-include=/usr/local/include 
--with-mpfr-lib=/usr/local/lib --with-gmp-include=/usr/local/include 
--with-gmp-lib=/usr/local/lib CC=/usr/sfw/bin/gcc CXX=/usr/sfw/bin/g++
Thread model: posix
gcc version 4.4.1 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`t2 ~]$ uname -a
SunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240
[mvngu`@`t2 ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`t2 ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now set CC and CXX to gcc and g++:
 {{{
[mvngu`@`t2 ~]$ uname -a
SunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240
[mvngu`@`t2 ~]$ export CC=gcc
[mvngu`@`t2 ~]$ export CXX=g++
[mvngu`@`t2 ~]$ ./testcc.sh 
GCC
[mvngu`@`t2 ~]$ ./testcxx.sh 
GCC
 }}}
 Now set CC and CXX to use Sun Studio 12:
 {{{
[mvngu`@`t2 ~]$ uname -a
SunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240
[mvngu`@`t2 ~]$ export CC=/opt/SUNWspro/prod/bin/cc
[mvngu`@`t2 ~]$ export CXX=/opt/SUNWspro/prod/bin/CC
[mvngu`@`t2 ~]$ ./testcc.sh 
Sun_Studio
[mvngu`@`t2 ~]$ ./testcxx.sh 
Sun_Studio
 }}}
 * SUSE Linux Enterprise Server 10 SP1 (iras on SkyNet), IA-64, GCC 4.4.2:
 {{{
[mvngu`@`iras ~]$ gcc -v
Using built-in specs.
Target: ia64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.4.2/src/gcc-4.4.2/configure 
--enable-languages=c,c++,fortran --with-gnu-as 
--with-as=/usr/local/binutils-2.20/ia64-Linux-suse-gcc-4.4.2/bin/as 
--with-gnu-ld 
--with-ld=/usr/local/binutils-2.20/ia64-Linux-suse-gcc-4.4.2/bin/ld 
--with-gmp=/usr/local/mpir-1.2.1/ia64-Linux-rhel-gcc-4.4.0 
--with-mpfr=/usr/local/mpfr-2.4.1/ia64-Linux-mpir-1.2.1-gcc-4.4.0 
--prefix=/usr/local/gcc-4.4.2/ia64-Linux-suse-binutils-2.20
Thread model: posix
gcc version 4.4.2 (GCC)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`iras ~]$ uname -a
Linux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux
[mvngu`@`iras ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`iras ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`iras ~]$ uname -a
Linux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux
[mvngu`@`iras ~]$ export CC=gcc
[mvngu`@`iras ~]$ export CXX=g++
[mvngu`@`iras ~]$ ./testcc.sh 
GCC
[mvngu`@`iras ~]$ ./testcxx.sh 
GCC
 }}}
 * Ubuntu 8.04.3 LTS (boxen.math), Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz, GCC 4.2.4:
 {{{
[mvngu`@`boxen mvngu]$ gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v 
--enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr 
--enable-shared --with-system-zlib --libexecdir=/usr/lib 
--without-included-gettext --enable-threads=posix --enable-nls 
--with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 
--enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr 
--enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu 
--target=x86_64-linux-gnu
Thread model: posix
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`boxen mvngu]$ uname -a
Linux boxen 2.6.24-24-server #1 SMP Sat Aug 22 00:59:57 UTC 2009 x86_64 GNU/Linux
[mvngu`@`boxen mvngu]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`boxen mvngu]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`boxen mvngu]$ uname -a
Linux boxen 2.6.24-24-server #1 SMP Sat Aug 22 00:59:57 UTC 2009 x86_64 GNU/Linux
[mvngu`@`boxen mvngu]$ export CC=gcc
[mvngu`@`boxen mvngu]$ export CXX=g++
[mvngu`@`boxen mvngu]$ ./testcc.sh 
GCC
[mvngu`@`boxen mvngu]$ ./testcxx.sh 
GCC
 }}}
 * Ubuntu 9.10 (running on my MacBook), Intel(R) Core(TM)2 CPU T7200 `@` 2.00GHz, GCC 4.4.1:
 {{{
[mvngu`@`darkstar ~]$ gcc -v
Using built-in specs.
Target: i486-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 4.4.1-4ubuntu8' 
--with-bugurl=file:///usr/share/doc/gcc-4.4/README.Bugs 
--enable-languages=c,c++,fortran,objc,obj-c++ --prefix=/usr --enable-shared 
--enable-multiarch --enable-linker-build-id --with-system-zlib 
--libexecdir=/usr/lib --without-included-gettext --enable-threads=posix 
--with-gxx-include-dir=/usr/include/c++/4.4 --program-suffix=-4.4 --enable-nls 
--enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc 
--enable-targets=all --disable-werror --with-arch-32=i486 --with-tune=generic 
--enable-checking=release --build=i486-linux-gnu --host=i486-linux-gnu 
--target=i486-linux-gnu
Thread model: posix
gcc version 4.4.1 (Ubuntu 4.4.1-4ubuntu8)
 }}}
 Without setting CC and CXX:
 {{{
[mvngu`@`darkstar ~]$ uname -a
Linux darkstar 2.6.31-16-generic #53-Ubuntu SMP Tue Dec 8 04:01:29 UTC 2009 i686 GNU/Linux
[mvngu`@`darkstar ~]$ ./testcc.sh 
Sorry, you must define the environment variable CC
[mvngu`@`darkstar ~]$ ./testcxx.sh 
Sorry, you should define the environment variable CXX
 }}}
 Now with CC and CXX set:
 {{{
[mvngu`@`darkstar ~]$ uname -a
Linux darkstar 2.6.31-16-generic #53-Ubuntu SMP Tue Dec 8 04:01:29 UTC 2009 i686 GNU/Linux
[mvngu`@`darkstar ~]$ export CC=gcc
[mvngu`@`darkstar ~]$ export CXX=g++
[mvngu`@`darkstar ~]$ ./testcc.sh 
GCC
[mvngu`@`darkstar ~]$ ./testcxx.sh     
GCC
 }}}

In each case, the test scripts work as claimed. We can say that the scripts have been tested and work as claimed on various versions of the following platforms with GCC and the relevant commercial compilers: AIX, Cygwin on Windows XP, Fedora, HP-UX, Mac OS X, openSUSE, Red Hat Enterprise Linux, Solaris, SUSE Linux Enterprise Server, Ubuntu. So far, no one has been able to test the scripts on Tru64 or Alpha Linux because we don't have access to the relevant platform/hardware combinations. At this [sage-devel](http://groups.google.com/group/sage-devel/msg/8ea858e120eec662) thread, Peter Jeremy mentions that he has access to a Tru64 machine, but he won't be able to test the scripts on that machine within the next few weeks from now. But that should not prevent the scripts from being merged in Sage.




The patch `trac_7505-test-scripts.patch` needs to be applied to `SAGE_ROOT/spkg/base`. But note that with Sage 4.3 some files under `SAGE_ROOT/spkg/base` are not yet managed by revision control:

```
[mvngu@boxen base]$ pwd
/dev/shm/mvngu/sage-4.3/spkg/base
[mvngu@boxen base]$ hg st
M sage-env
M sage-spkg
! prereq-0.3-install
? prereq-0.5-install
? prereq-0.5.tar
```

The file `prereq-0.3-install` is now superseded by `prereq-0.5-install` so `prereq-0.3-install` can be removed as follows:

```
[mvngu@boxen base]$ hg remove prereq-0.3-install
[mvngu@boxen base]$ hg st
M sage-env
M sage-spkg
R prereq-0.3-install
? prereq-0.5-install
? prereq-0.5.tar
```

Also, the file `prereq-0.5-install` needs to be checked in with:

```
[mvngu@boxen base]$ hg add prereq-0.5-install
[mvngu@boxen base]$ hg st
M sage-env
M sage-spkg
A prereq-0.5-install
R prereq-0.3-install
? prereq-0.5.tar
```

But the file `prereq-0.5.tar` need not be under revision control. In that case, the release manager could edit the file `.hgignore` to ignore that particular tarball. Anyway, I have attached the patch `trac_7505-revision-control.patch` which should take care of editing `.hgignore`, adding `prereq-0.5-install` and removing `prereq-0.3-install`. I have attached a version of David Kirkby's patch that contains his name so that when his scripts are checked in, they are committed in his name. Finally, note that the files `sage-env` and `sage-spkg` must be first checked in before applying any of the above patches. That is, patches/changes should be applied/made to the directory `SAGE_ROOT/spkg/base` in the following order:

 1. Check in the changes to `sage-env` and `sage-spkg`.
 1. Apply `trac_7505-revision-control.patch` to properly put three existing files under revision control.
 1. Finally, apply `trac_7505-scripts.patch` which has the same changes as `trac_7505-test-scripts.patch`, but any check ins would be made in David's name.


---

Comment by mvngu created at 2009-12-31 19:25:27

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-12-31 19:30:38

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2009-12-31 19:31:49

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2009-12-31 19:33:51

I forgot to say that someone needs to make sure that my patch `trac_7505-revision-control.patch` works as claimed. Once that is done, I think the whole ticket would receive positive review.


---

Comment by drkirkby created at 2009-12-31 19:50:38

Tests C compiler reading from the command line, not environment variable CC


---

Attachment

Tests C++ compiler reading from the command line, not environment variable CXX


---

Attachment

I've attached the revised versions. I did not overwrite the file names, and note they now have a 2 appended to the names, which was done by the trac server, not me.


---

Comment by drkirkby created at 2009-12-31 19:55:48

Oops my comments seems to have been missed. 

Minh

did you not see William's comments? The revised scripts attach address them. 


I do not know if the trac server is in some way out of sync, but I thought I put this comment a few mins ago. The fact Minh seems to have missed something William wrote, makes me wonder if there is a problem with the trac server

dave


---

Comment by mvngu created at 2009-12-31 20:00:12

Replying to [comment:27 drkirkby]:
> did you not see William's comments? 

I missed those comments.




> The revised scripts attach address them. 

I'll have a look at them.




> I do not know if the trac server is in some way out of sync, but I thought I put this comment a few mins ago. The fact Minh seems to have missed something William wrote, makes me wonder if there is a problem with the trac server

I wasn't CC'd on the ticket. So when I was reviewing your previous attachments, I missed William's comments. There's no need to worry. I can review your newer attachments.


---

Comment by drkirkby created at 2009-12-31 20:07:50

PS, regarding your comment about checking in prereq 0.5, see #7781 

Dave


---

Comment by mvngu created at 2009-12-31 20:25:34

There is a mismatch in documentation in `testcc.2.sh`:

```
54  # Exit if the user supplies any command-line arguments.
55	if [ $# -ne 1 ] ; then
56	  usage
57	  exit 1
58	fi
59	CC_LOCAL=$1
```

Do you also want to change the above section to something like the following?

```
# Exit if the user does not supply one command line argument.
if [ $# -ne 1 ] ; then
  usage
  exit 1
fi

CC_LOCAL=$1 # Compiler name or path as argument to script. 
```

This would also be in line with the corresponding documentation in `testcxx.2.sh`.




PS: If you want to replace an earlier version of an attachment with the same name, you could do so. On the page for uploading files, there should be a check box to indicate that you want to replace files of the same name.


---

Attachment


---

Comment by drkirkby created at 2009-12-31 20:52:21

Hi Minh, 
yes, I did want the comment updated, as now the scripts take one argument, not zero as before. I'd purposely chosen to leave the older version on the server, but perhaps with hindsight that was not wise. 

Dave


---

Comment by was created at 2009-12-31 22:19:04

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-31 22:19:04

> Would it be acceptable to you if the file name was much more complex, say [...]

Yes.  "/tmp/test.$$.c" seems just a little too generic.  I like the change you made in your latest script. 

Minh -- thanks for all your testing!

Definite positive review.


---

Comment by drkirkby created at 2010-01-03 22:23:55

## Note to Mike (release manager)

This ticket might have got a bit confusing. Just to recap, these things need going in. 

 * install.patch  (308 bytes) 
 * testcc.3.sh  (but named as testcc.sh)
 * testcxx.2.sh (but named as testcxx.sh)


---

Comment by mhansen created at 2010-01-04 01:47:46

Resolution: fixed
