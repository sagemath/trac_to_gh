# Issue 8783: frobby optional spkg doesn't build with newer GCC's

Issue created by migration from https://trac.sagemath.org/ticket/8783

Original creator: was

Original creation time: 2010-04-27 20:14:41

Assignee: tbd


```
frobby-0.7.6/src/test/transform/t3.gen.m2
frobby-0.7.6/src/test/transform/t3.gen.nm
Finished extraction
****************************************************
Host system
uname -a:
Linux eno 2.6.32.10-90.fc12.x86_64 #1 SMP Tue Mar 23 09:47:08 UTC 2010 x86_64 x86_64 x86_64 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-core2-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-gnu-as=/usr/local/binutils-2.20.1/x86_64-Linux-core2-fc-gcc-4.4.3-rh/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-core2-fc-gcc-4.4.3-rh/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-core2-fc-gcc-4.4.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-core2-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-core2-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3-rh --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-core2-fc
Thread model: posix
gcc version 4.5.0 (GCC)
****************************************************
mkdir -p bin/release/
g++ -Wall -ansi -pedantic -Wextra -Wno-uninitialized -Wno-unused-parameter -Werror -isystem /home/wstein/screen/eno/sage-4.3/local/include -O3 -c src/main.cpp -o bin/release/main.o
src/main.cpp: In function ‘int main(int, const char**)’:
src/main.cpp:30:16: error: ‘srand’ was not declared in this scope
make: *** [bin/release/main.o] Error 1
Error building Frobby.

real    0m0.614s
user    0m0.283s
sys     0m0.052s
sage: An error occurred while installing frobby-0.7.6
Please email sage-devel http://groups.google.com/group/sag
```



---

Comment by was created at 2010-04-27 20:17:26

Note that this still builds on sage.math with GCC-4.2.4...  But it doesn't build on Skynet with newer GCC's.


---

Comment by was created at 2010-04-27 21:52:11


```
Hi William,

Yes, it is just a question of a few extra includes. I haven't fixed it
since I was making a new release of Frobby anyway. That new release
has become rather large since that has been convenient for my
research, and so it is taking longer than expected. I'll submit a fix
once I get back from this conference next week.

Cheers
Bjarke
```



---

Comment by was created at 2010-04-27 22:04:47


```
The error in the ticket mentions srand. What I do is google srand and I get e.g.

 http://www.cplusplus.com/reference/clibrary/cstdlib/srand/

it says it is in cstdlib, so add

 #include <cstdlib>

to the cpp file that is having a problem. Then likely another file
will have the same problem due to the same or another missing header,
and after a few iterations of this the problem should be solved. Most
likely all the missing includes are in cpp files, though it is
possible that a header might miss something too. The problem is caused
by older versions of GCC having header A also pull in header B without
the standard saying that it should do so (which is allowed but
unfortunate). The newer version of header A in a newer GCC then stops
pulling in header B, and suddenly it becomes apparent that header B
should have been included where A was also included, but before it was
invisible that this should have happened.

Cheers
Bjarke
```



---

Comment by drkirkby created at 2010-05-06 23:06:44

Note, gcc 4.5 is *not* the latest gcc, but gcc 4.4.4 is: See

 http://gcc.gnu.org/

```
News

April 29, 2010
    GCC 4.4.4 has been released.
April 14, 2010
    GCC 4.5.0 has been released.
```


Dave


---

Comment by was created at 2010-06-22 04:15:17

Even with gcc-4.4.3, Frobby doesn't build.

If somebody doesn't post a new frobby spkg on this ticket for review this week, I'm moving the frobby spkg to "experimental". 

 -- William


---

Comment by drkirkby created at 2010-06-22 05:40:58

Replying to [comment:6 was]:
> Even with gcc-4.4.3, Frobby doesn't build.
> 
> If somebody doesn't post a new frobby spkg on this ticket for review this week, I'm moving the frobby spkg to "experimental". 
> 
>  -- William

I wish you would clarify in the developers handbook, or even just on sage-devel, what is the difference between "optional" and "experimental". 

Dave


---

Comment by was created at 2010-06-28 17:37:12

I have moved Frobby from optional to experimental.  I'll move it back when this problem is addressed.

http://sagemath.org/packages/optional/

http://sagemath.org/packages/experimental/


---

Comment by broune created at 2010-07-04 15:30:51

I've had some problems on this because I don't have access to a computer that both has Sage on it and that at the same time has a recent enough version of GCC that this issue comes up. What I've done is patch the spkg so that the Frobby code in it compiles on a Cygwin machine I've got, and then I've tested that it still installs on sage.math, which I've recently gotten access to. So if we are lucky this will work, though someone with both Sage and a recent version of gcc should check it. I put the spkg here:

  http://sage.math.washington.edu/home/bjarke/frobby-0.7.6.p1.spkg


---

Comment by broune created at 2010-07-04 15:30:51

Changing status from new to needs_review.


---

Comment by was created at 2010-07-06 08:54:04

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-07-06 08:54:04

I looked at this for 1 minute:

(1)
There are some tmp ~ files laying around

```
wstein@sage:~/tmp/frobby-0.7.6.p1$ ls
patches  spkg-check  spkg-install  spkg-install~  SPKG.txt  SPKG.txt~  src
wstein@sage:~/tmp/frobby-0.7.6.p1$ rm *~
```


(2) The hg repo has lots of files that have been added but not checked in:

```
wstein@sage:~/tmp/frobby-0.7.6.p1$ ls
patches  spkg-check  spkg-install  SPKG.txt  src
wstein@sage:~/tmp/frobby-0.7.6.p1$ hg status
M SPKG.txt
M spkg-install
A patches/Makefile
A patches/Makefile.patch
A patches/src/Action.cpp
A patches/src/Action.cpp.patch
A patches/src/BoolParameter.cpp
A patches/src/BoolParameter.cpp.patch
A patches/src/Ideal.h
A patches/src/Ideal.h.patch
A patches/src/IntegerParameter.cpp
A patches/src/IntegerParameter.cpp.patch
A patches/src/Minimizer.cpp
A patches/src/Minimizer.cpp.patch
A patches/src/Parameter.cpp
A patches/src/Parameter.cpp.patch
A patches/src/ParameterGroup.cpp
A patches/src/ParameterGroup.cpp.patch
A patches/src/Scanner.cpp
A patches/src/Scanner.cpp.patch
A patches/src/VarNames.cpp
A patches/src/VarNames.cpp.patch
A patches/src/dynamicFrobeniusAlgorithm.cpp
A patches/src/dynamicFrobeniusAlgorithm.cpp.patch
A patches/src/frobbyTest.cpp
A patches/src/frobbyTest.cpp.patch
A patches/src/main.cpp
A patches/src/main.cpp.patch
A patches/src/randomDataGenerators.cpp
A patches/src/randomDataGenerators.cpp.patch
wstein@sage:~/tmp/frobby-0.7.6.p1$ 
```


(3) I don't understand why *upstream* -- i.e., the *author* of frobby-- is adding a ton of patches to his own code.  Why not just fix the src/ directly?


---

Comment by was created at 2010-07-06 08:54:44

That said, Frobby *does* build with GCC-4.5.0, which is great news!!

```

if [ -f bin/release/frobby.exe ]; then \
          mv -f bin/release/frobby.exe bin/release/frobby; \
        fi
strip bin/release/frobby
cd bin; rm -f frobby; link ../bin/release/frobby frobby; cd ..

real    0m47.042s
user    0m40.332s
sys     0m4.577s
Successfully installed frobby-0.7.6.p1
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing frobby-0.7.6.p1.spkg
[wstein@eno sage-4.4.4]$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-core2-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-gnu-as=/usr/local/binutils-2.20.1/x86_64-Linux-core2-fc-gcc-4.4.3-rh/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-core2-fc-gcc-4.4.3-rh/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-core2-fc-gcc-4.4.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-core2-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-core2-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3-rh --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-core2-fc
Thread model: posix
gcc version 4.5.0 (GCC) 
[wstein@eno sage-4.4.4]$ 

```



---

Comment by broune created at 2010-07-06 11:50:24

Changing status from needs_work to needs_review.


---

Comment by broune created at 2010-07-06 11:53:37

(Oops, I put my response as the description. Now fixed.)

Thanks for the prompt review. I committed the outstanding files in the repository and removed the two ~ files. The result is up in the same place:

 http://sage.math.washington.edu/home/bjarke/frobby-0.7.6.p1.spkg

I'm adding patches rather than edit src/ because as I understand it the code in src/ must be an official release of the upstream code. No version 0.7.6 of Frobby exists that compiles under gcc 4.3.0, and I'd rather add some patches here than make an official release of an old version.


---

Comment by benjaminfjones created at 2011-08-22 16:32:23

I can verify that the ~ files were removed and the repository is clean. The SPKG successfully builds using GCC 4.4.5. I'm trying GCC 4.5.? now.


---

Comment by benjaminfjones created at 2011-08-23 02:05:59

The SPKG builds using GCC 4.6.1 as well. Here is the build log: https://gist.github.com/1164148

Unless anyone has further comments / concerns, I will give the new SPKG a positive review.


---

Comment by benjaminfjones created at 2011-08-23 20:48:49

Changing status from needs_review to positive_review.


---

Comment by was created at 2011-08-24 23:41:54

Changing keywords from "" to "sd32".


---

Comment by leif created at 2011-09-12 19:59:04

Changing status from positive_review to needs_info.


---

Comment by leif created at 2011-09-12 19:59:04

Did anybody try to build this with `SAGE_CHECK=yes`?

I get hundreds of errors on Ubuntu 10.04.3 (GCC 4.4.3). The build itself succeeds, but the test suite ends with:

```
src/randomDataGenerators.cpp:44: error: ‘mpz_class’ was not declared in this scope
src/randomDataGenerators.cpp:47: error: ‘stderr’ was not declared in this scope
src/randomDataGenerators.cpp:47: error: ‘fputs’ was not declared in this scope
src/IOHandler.cpp: At global scope:
src/IOHandler.cpp:215: error: ‘mpz_class’ was not declared in this scope
src/IOHandler.cpp:215: error: template argument 1 is invalid
src/IOHandler.cpp:215: error: template argument 2 is invalid
src/IOHandler.cpp: In function ‘void readFrobeniusInstance(Scanner&, int&)’:
src/IOHandler.cpp:216: error: request for member ‘clear’ in ‘numbers’, which is of non-class type ‘int’
src/IOHandler.cpp:219: error: ‘mpz_class’ was not declared in this scope
src/IOHandler.cpp:219: error: expected ‘;’ before ‘n’
src/IOHandler.cpp:221: error: ‘n’ was not declared in this scope
src/IOHandler.cpp:225: error: ‘stderr’ was not declared in this scope
src/IOHandler.cpp:228: error: ‘gmp_fprintf’ was not declared in this scope
src/IOHandler.cpp:232: error: request for member ‘push_back’ in ‘numbers’, which is of non-class type ‘int’
src/IOHandler.cpp:235: error: request for member ‘empty’ in ‘numbers’, which is of non-class type ‘int’
src/IOHandler.cpp:237: error: ‘stderr’ was not declared in this scope
src/IOHandler.cpp:237: error: ‘fputs’ was not declared in this scope
src/IOHandler.cpp:241: error: expected ‘;’ before ‘gcd’
src/IOHandler.cpp:242: error: request for member ‘size’ in ‘numbers’, which is of non-class type ‘int’
src/IOHandler.cpp:243: error: request for member ‘get_mpz_t’ in ‘gcd’, which is of non-class type ‘void(Exponent*, const Exponent*, const Exponent*, size_t)’
src/IOHandler.cpp:243: error: request for member ‘get_mpz_t’ in ‘gcd’, which is of non-class type ‘void(Exponent*, const Exponent*, const Exponent*, size_t)’
src/IOHandler.cpp:243: error: invalid types ‘int[size_t]’ for array subscript
src/IOHandler.cpp:243: error: ‘mpz_gcd’ was not declared in this scope
src/IOHandler.cpp:245: error: ISO C++ forbids comparison between pointer and integer
src/IOHandler.cpp:246: error: ‘stderr’ was not declared in this scope
src/IOHandler.cpp:249: error: request for member ‘get_mpz_t’ in ‘gcd’, which is of non-class type ‘void(Exponent*, const Exponent*, const Exponent*, size_t)’
src/IOHandler.cpp:249: error: ‘gmp_fprintf’ was not declared in this scope
src/randomDataGenerators.cpp: At global scope:
src/randomDataGenerators.cpp:157: error: ‘Degree’ was not declared in this scope
src/randomDataGenerators.cpp:157: error: template argument 1 is invalid
src/randomDataGenerators.cpp:157: error: template argument 2 is invalid
src/randomDataGenerators.cpp: In function ‘void generateRandomFrobeniusInstance(int&)’:
src/randomDataGenerators.cpp:161: error: request for member ‘resize’ in ‘degrees’, which is of non-class type ‘int’
src/randomDataGenerators.cpp:163: error: ‘Degree’ was not declared in this scope
src/randomDataGenerators.cpp:163: error: expected ‘;’ before ‘totalGcd’
src/randomDataGenerators.cpp:165: error: expected ‘;’ before ‘number’
src/randomDataGenerators.cpp:166: error: ‘totalGcd’ was not declared in this scope
src/randomDataGenerators.cpp:167: error: ‘number’ was not declared in this scope
src/randomDataGenerators.cpp:171: error: ‘number’ was not declared in this scope
src/randomDataGenerators.cpp:171: error: ‘mpz_gcd’ was not declared in this scope
src/randomDataGenerators.cpp:173: error: invalid types ‘int[int]’ for array subscript
src/randomDataGenerators.cpp:173: error: ‘number’ was not declared in this scope
src/randomDataGenerators.cpp:177: error: invalid types ‘int[int]’ for array subscript
src/randomDataGenerators.cpp:178: error: ‘totalGcd’ was not declared in this scope
src/randomDataGenerators.cpp:180: error: request for member ‘begin’ in ‘degrees’, which is of non-class type ‘int’
src/randomDataGenerators.cpp:180: error: request for member ‘end’ in ‘degrees’, which is of non-class type ‘int’
make: *** [bin/debug/IOHandler.o] Error 1
make: *** [bin/debug/BigIdeal.o] Error 1
make: *** [bin/debug/randomDataGenerators.o] Error 1
mkdir -p bin/release/ 
cd bin; rm -f frobby; link ../bin/release/frobby frobby; cd ..
export frobby=bin/frobby; ./test/runtests
decom      ..........................
frob       ..............................
intersect  ..........
assoprimes ............
minimize   ..........
transform  .....
latformat  .....
alexdual   ...............
radical    .........
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing frobby-0.7.6.p1.spkg
```

The main problem seems a wrong or missing include path, which of course causes further errors.


---

Comment by leif created at 2011-09-12 20:09:07

Build with `SAGE_CHECK=yes` on Ubuntu 10.04, GCC 4.3.3


---

Attachment

Ooops, should read 4.*4*.3, but the version shouldn't matter much anyway... ;-)

(Attached the build log.)


---

Comment by benjaminfjones created at 2011-09-13 01:38:10

I didn't run the build with SAGE_CHECK=yes when I reviewed the package, but I did run the test suite manually. This was on skynet/eno which has GCC 4.6.1 installed. 

I just ran the build under Sage 4.7.2.alpha1 on skynet/eno using `export SAGE_CHECK=yes; ./sage -f frobby-0.7.6.p1.spkg` and both the build and the test suite finish without errors. I'll attach the build log.


---

Attachment

frobby build log with SAGE_CHECK=yes on skynet/eno


---

Comment by swenson created at 2012-01-22 21:06:38

Ping.


---

Comment by benjaminfjones created at 2012-05-25 20:27:33

Closing as a duplicate in light of #13007.


---

Comment by jdemeyer created at 2012-05-26 01:11:06

Resolution: duplicate
