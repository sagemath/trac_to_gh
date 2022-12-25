# Issue 8783: frobby optional spkg doesn't build with newer GCC's

archive/issues_008783.json:
```json
{
    "body": "Assignee: tbd\n\n```\nfrobby-0.7.6/src/test/transform/t3.gen.m2\nfrobby-0.7.6/src/test/transform/t3.gen.nm\nFinished extraction\n****************************************************\nHost system\nuname -a:\nLinux eno 2.6.32.10-90.fc12.x86_64 #1 SMP Tue Mar 23 09:47:08 UTC 2010 x86_64 x86_64 x86_64 GNU/Linux\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nCOLLECT_GCC=gcc\nCOLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-core2-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper\nTarget: x86_64-unknown-linux-gnu\nConfigured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-gnu-as=/usr/local/binutils-2.20.1/x86_64-Linux-core2-fc-gcc-4.4.3-rh/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-core2-fc-gcc-4.4.3-rh/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-core2-fc-gcc-4.4.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-core2-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-core2-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3-rh --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-core2-fc\nThread model: posix\ngcc version 4.5.0 (GCC)\n****************************************************\nmkdir -p bin/release/\ng++ -Wall -ansi -pedantic -Wextra -Wno-uninitialized -Wno-unused-parameter -Werror -isystem /home/wstein/screen/eno/sage-4.3/local/include -O3 -c src/main.cpp -o bin/release/main.o\nsrc/main.cpp: In function \u2018int main(int, const char**)\u2019:\nsrc/main.cpp:30:16: error: \u2018srand\u2019 was not declared in this scope\nmake: *** [bin/release/main.o] Error 1\nError building Frobby.\n\nreal    0m0.614s\nuser    0m0.283s\nsys     0m0.052s\nsage: An error occurred while installing frobby-0.7.6\nPlease email sage-devel http://groups.google.com/group/sag\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8783\n\n",
    "created_at": "2010-04-27T20:14:41Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "frobby optional spkg doesn't build with newer GCC's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8783",
    "user": "https://github.com/williamstein"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/8783





---

archive/issue_comments_080263.json:
```json
{
    "body": "Note that this still builds on sage.math with GCC-4.2.4...  But it doesn't build on Skynet with newer GCC's.",
    "created_at": "2010-04-27T20:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80263",
    "user": "https://github.com/williamstein"
}
```

Note that this still builds on sage.math with GCC-4.2.4...  But it doesn't build on Skynet with newer GCC's.



---

archive/issue_comments_080264.json:
```json
{
    "body": "```\nHi William,\n\nYes, it is just a question of a few extra includes. I haven't fixed it\nsince I was making a new release of Frobby anyway. That new release\nhas become rather large since that has been convenient for my\nresearch, and so it is taking longer than expected. I'll submit a fix\nonce I get back from this conference next week.\n\nCheers\nBjarke\n```",
    "created_at": "2010-04-27T21:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80264",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_080265.json:
```json
{
    "body": "```\nThe error in the ticket mentions srand. What I do is google srand and I get e.g.\n\n http://www.cplusplus.com/reference/clibrary/cstdlib/srand/\n\nit says it is in cstdlib, so add\n\n #include <cstdlib>\n\nto the cpp file that is having a problem. Then likely another file\nwill have the same problem due to the same or another missing header,\nand after a few iterations of this the problem should be solved. Most\nlikely all the missing includes are in cpp files, though it is\npossible that a header might miss something too. The problem is caused\nby older versions of GCC having header A also pull in header B without\nthe standard saying that it should do so (which is allowed but\nunfortunate). The newer version of header A in a newer GCC then stops\npulling in header B, and suddenly it becomes apparent that header B\nshould have been included where A was also included, but before it was\ninvisible that this should have happened.\n\nCheers\nBjarke\n```",
    "created_at": "2010-04-27T22:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80265",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_080266.json:
```json
{
    "body": "Note, gcc 4.5 is **not** the latest gcc, but gcc 4.4.4 is: See\n\n http://gcc.gnu.org/\n\n```\nNews\n\nApril 29, 2010\n    GCC 4.4.4 has been released.\nApril 14, 2010\n    GCC 4.5.0 has been released.\n```\n\nDave",
    "created_at": "2010-05-06T23:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80266",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Note, gcc 4.5 is **not** the latest gcc, but gcc 4.4.4 is: See

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

archive/issue_comments_080267.json:
```json
{
    "body": "Even with gcc-4.4.3, Frobby doesn't build.\n\nIf somebody doesn't post a new frobby spkg on this ticket for review this week, I'm moving the frobby spkg to \"experimental\". \n\n -- William",
    "created_at": "2010-06-22T04:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80267",
    "user": "https://github.com/williamstein"
}
```

Even with gcc-4.4.3, Frobby doesn't build.

If somebody doesn't post a new frobby spkg on this ticket for review this week, I'm moving the frobby spkg to "experimental". 

 -- William



---

archive/issue_comments_080268.json:
```json
{
    "body": "Replying to [comment:6 was]:\n> Even with gcc-4.4.3, Frobby doesn't build.\n> \n> If somebody doesn't post a new frobby spkg on this ticket for review this week, I'm moving the frobby spkg to \"experimental\". \n> \n>  -- William\n\n\nI wish you would clarify in the developers handbook, or even just on sage-devel, what is the difference between \"optional\" and \"experimental\". \n\nDave",
    "created_at": "2010-06-22T05:40:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80268",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:6 was]:
> Even with gcc-4.4.3, Frobby doesn't build.
> 
> If somebody doesn't post a new frobby spkg on this ticket for review this week, I'm moving the frobby spkg to "experimental". 
> 
>  -- William


I wish you would clarify in the developers handbook, or even just on sage-devel, what is the difference between "optional" and "experimental". 

Dave



---

archive/issue_comments_080269.json:
```json
{
    "body": "I have moved Frobby from optional to experimental.  I'll move it back when this problem is addressed.\n\nhttp://sagemath.org/packages/optional/\n\nhttp://sagemath.org/packages/experimental/",
    "created_at": "2010-06-28T17:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80269",
    "user": "https://github.com/williamstein"
}
```

I have moved Frobby from optional to experimental.  I'll move it back when this problem is addressed.

http://sagemath.org/packages/optional/

http://sagemath.org/packages/experimental/



---

archive/issue_comments_080270.json:
```json
{
    "body": "I've had some problems on this because I don't have access to a computer that both has Sage on it and that at the same time has a recent enough version of GCC that this issue comes up. What I've done is patch the spkg so that the Frobby code in it compiles on a Cygwin machine I've got, and then I've tested that it still installs on sage.math, which I've recently gotten access to. So if we are lucky this will work, though someone with both Sage and a recent version of gcc should check it. I put the spkg here:\n\n  http://sage.math.washington.edu/home/bjarke/frobby-0.7.6.p1.spkg",
    "created_at": "2010-07-04T15:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80270",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

I've had some problems on this because I don't have access to a computer that both has Sage on it and that at the same time has a recent enough version of GCC that this issue comes up. What I've done is patch the spkg so that the Frobby code in it compiles on a Cygwin machine I've got, and then I've tested that it still installs on sage.math, which I've recently gotten access to. So if we are lucky this will work, though someone with both Sage and a recent version of gcc should check it. I put the spkg here:

  http://sage.math.washington.edu/home/bjarke/frobby-0.7.6.p1.spkg



---

archive/issue_comments_080271.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-04T15:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80271",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080272.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-06T08:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80272",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080273.json:
```json
{
    "body": "I looked at this for 1 minute:\n\n(1)\nThere are some tmp ~ files laying around\n\n```\nwstein@sage:~/tmp/frobby-0.7.6.p1$ ls\npatches  spkg-check  spkg-install  spkg-install~  SPKG.txt  SPKG.txt~  src\nwstein@sage:~/tmp/frobby-0.7.6.p1$ rm *~\n```\n\n(2) The hg repo has lots of files that have been added but not checked in:\n\n```\nwstein@sage:~/tmp/frobby-0.7.6.p1$ ls\npatches  spkg-check  spkg-install  SPKG.txt  src\nwstein@sage:~/tmp/frobby-0.7.6.p1$ hg status\nM SPKG.txt\nM spkg-install\nA patches/Makefile\nA patches/Makefile.patch\nA patches/src/Action.cpp\nA patches/src/Action.cpp.patch\nA patches/src/BoolParameter.cpp\nA patches/src/BoolParameter.cpp.patch\nA patches/src/Ideal.h\nA patches/src/Ideal.h.patch\nA patches/src/IntegerParameter.cpp\nA patches/src/IntegerParameter.cpp.patch\nA patches/src/Minimizer.cpp\nA patches/src/Minimizer.cpp.patch\nA patches/src/Parameter.cpp\nA patches/src/Parameter.cpp.patch\nA patches/src/ParameterGroup.cpp\nA patches/src/ParameterGroup.cpp.patch\nA patches/src/Scanner.cpp\nA patches/src/Scanner.cpp.patch\nA patches/src/VarNames.cpp\nA patches/src/VarNames.cpp.patch\nA patches/src/dynamicFrobeniusAlgorithm.cpp\nA patches/src/dynamicFrobeniusAlgorithm.cpp.patch\nA patches/src/frobbyTest.cpp\nA patches/src/frobbyTest.cpp.patch\nA patches/src/main.cpp\nA patches/src/main.cpp.patch\nA patches/src/randomDataGenerators.cpp\nA patches/src/randomDataGenerators.cpp.patch\nwstein@sage:~/tmp/frobby-0.7.6.p1$ \n```\n\n(3) I don't understand why *upstream* -- i.e., the *author* of frobby-- is adding a ton of patches to his own code.  Why not just fix the src/ directly?",
    "created_at": "2010-07-06T08:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80273",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_080274.json:
```json
{
    "body": "That said, Frobby *does* build with GCC-4.5.0, which is great news!!\n\n```\n\nif [ -f bin/release/frobby.exe ]; then \\\n          mv -f bin/release/frobby.exe bin/release/frobby; \\\n        fi\nstrip bin/release/frobby\ncd bin; rm -f frobby; link ../bin/release/frobby frobby; cd ..\n\nreal    0m47.042s\nuser    0m40.332s\nsys     0m4.577s\nSuccessfully installed frobby-0.7.6.p1\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing frobby-0.7.6.p1.spkg\n[wstein@eno sage-4.4.4]$ gcc -v\nUsing built-in specs.\nCOLLECT_GCC=gcc\nCOLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-core2-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper\nTarget: x86_64-unknown-linux-gnu\nConfigured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-gnu-as=/usr/local/binutils-2.20.1/x86_64-Linux-core2-fc-gcc-4.4.3-rh/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-core2-fc-gcc-4.4.3-rh/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-core2-fc-gcc-4.4.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-core2-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-core2-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3-rh --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-core2-fc\nThread model: posix\ngcc version 4.5.0 (GCC) \n[wstein@eno sage-4.4.4]$ \n\n```",
    "created_at": "2010-07-06T08:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80274",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_080275.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-06T11:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80275",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080276.json:
```json
{
    "body": "(Oops, I put my response as the description. Now fixed.)\n\nThanks for the prompt review. I committed the outstanding files in the repository and removed the two ~ files. The result is up in the same place:\n\n http://sage.math.washington.edu/home/bjarke/frobby-0.7.6.p1.spkg\n\nI'm adding patches rather than edit src/ because as I understand it the code in src/ must be an official release of the upstream code. No version 0.7.6 of Frobby exists that compiles under gcc 4.3.0, and I'd rather add some patches here than make an official release of an old version.",
    "created_at": "2010-07-06T11:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80276",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

(Oops, I put my response as the description. Now fixed.)

Thanks for the prompt review. I committed the outstanding files in the repository and removed the two ~ files. The result is up in the same place:

 http://sage.math.washington.edu/home/bjarke/frobby-0.7.6.p1.spkg

I'm adding patches rather than edit src/ because as I understand it the code in src/ must be an official release of the upstream code. No version 0.7.6 of Frobby exists that compiles under gcc 4.3.0, and I'd rather add some patches here than make an official release of an old version.



---

archive/issue_comments_080277.json:
```json
{
    "body": "I can verify that the ~ files were removed and the repository is clean. The SPKG successfully builds using GCC 4.4.5. I'm trying GCC 4.5.? now.",
    "created_at": "2011-08-22T16:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80277",
    "user": "https://github.com/benjaminfjones"
}
```

I can verify that the ~ files were removed and the repository is clean. The SPKG successfully builds using GCC 4.4.5. I'm trying GCC 4.5.? now.



---

archive/issue_comments_080278.json:
```json
{
    "body": "The SPKG builds using GCC 4.6.1 as well. Here is the build log: https://gist.github.com/1164148\n\nUnless anyone has further comments / concerns, I will give the new SPKG a positive review.",
    "created_at": "2011-08-23T02:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80278",
    "user": "https://github.com/benjaminfjones"
}
```

The SPKG builds using GCC 4.6.1 as well. Here is the build log: https://gist.github.com/1164148

Unless anyone has further comments / concerns, I will give the new SPKG a positive review.



---

archive/issue_comments_080279.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-23T20:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80279",
    "user": "https://github.com/benjaminfjones"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080280.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80280",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_080281.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-09-12T19:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80281",
    "user": "https://github.com/nexttime"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_080282.json:
```json
{
    "body": "Did anybody try to build this with `SAGE_CHECK=yes`?\n\nI get hundreds of errors on Ubuntu 10.04.3 (GCC 4.4.3). The build itself succeeds, but the test suite ends with:\n\n```\nsrc/randomDataGenerators.cpp:44: error: \u2018mpz_class\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:47: error: \u2018stderr\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:47: error: \u2018fputs\u2019 was not declared in this scope\nsrc/IOHandler.cpp: At global scope:\nsrc/IOHandler.cpp:215: error: \u2018mpz_class\u2019 was not declared in this scope\nsrc/IOHandler.cpp:215: error: template argument 1 is invalid\nsrc/IOHandler.cpp:215: error: template argument 2 is invalid\nsrc/IOHandler.cpp: In function \u2018void readFrobeniusInstance(Scanner&, int&)\u2019:\nsrc/IOHandler.cpp:216: error: request for member \u2018clear\u2019 in \u2018numbers\u2019, which is of non-class type \u2018int\u2019\nsrc/IOHandler.cpp:219: error: \u2018mpz_class\u2019 was not declared in this scope\nsrc/IOHandler.cpp:219: error: expected \u2018;\u2019 before \u2018n\u2019\nsrc/IOHandler.cpp:221: error: \u2018n\u2019 was not declared in this scope\nsrc/IOHandler.cpp:225: error: \u2018stderr\u2019 was not declared in this scope\nsrc/IOHandler.cpp:228: error: \u2018gmp_fprintf\u2019 was not declared in this scope\nsrc/IOHandler.cpp:232: error: request for member \u2018push_back\u2019 in \u2018numbers\u2019, which is of non-class type \u2018int\u2019\nsrc/IOHandler.cpp:235: error: request for member \u2018empty\u2019 in \u2018numbers\u2019, which is of non-class type \u2018int\u2019\nsrc/IOHandler.cpp:237: error: \u2018stderr\u2019 was not declared in this scope\nsrc/IOHandler.cpp:237: error: \u2018fputs\u2019 was not declared in this scope\nsrc/IOHandler.cpp:241: error: expected \u2018;\u2019 before \u2018gcd\u2019\nsrc/IOHandler.cpp:242: error: request for member \u2018size\u2019 in \u2018numbers\u2019, which is of non-class type \u2018int\u2019\nsrc/IOHandler.cpp:243: error: request for member \u2018get_mpz_t\u2019 in \u2018gcd\u2019, which is of non-class type \u2018void(Exponent*, const Exponent*, const Exponent*, size_t)\u2019\nsrc/IOHandler.cpp:243: error: request for member \u2018get_mpz_t\u2019 in \u2018gcd\u2019, which is of non-class type \u2018void(Exponent*, const Exponent*, const Exponent*, size_t)\u2019\nsrc/IOHandler.cpp:243: error: invalid types \u2018int[size_t]\u2019 for array subscript\nsrc/IOHandler.cpp:243: error: \u2018mpz_gcd\u2019 was not declared in this scope\nsrc/IOHandler.cpp:245: error: ISO C++ forbids comparison between pointer and integer\nsrc/IOHandler.cpp:246: error: \u2018stderr\u2019 was not declared in this scope\nsrc/IOHandler.cpp:249: error: request for member \u2018get_mpz_t\u2019 in \u2018gcd\u2019, which is of non-class type \u2018void(Exponent*, const Exponent*, const Exponent*, size_t)\u2019\nsrc/IOHandler.cpp:249: error: \u2018gmp_fprintf\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp: At global scope:\nsrc/randomDataGenerators.cpp:157: error: \u2018Degree\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:157: error: template argument 1 is invalid\nsrc/randomDataGenerators.cpp:157: error: template argument 2 is invalid\nsrc/randomDataGenerators.cpp: In function \u2018void generateRandomFrobeniusInstance(int&)\u2019:\nsrc/randomDataGenerators.cpp:161: error: request for member \u2018resize\u2019 in \u2018degrees\u2019, which is of non-class type \u2018int\u2019\nsrc/randomDataGenerators.cpp:163: error: \u2018Degree\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:163: error: expected \u2018;\u2019 before \u2018totalGcd\u2019\nsrc/randomDataGenerators.cpp:165: error: expected \u2018;\u2019 before \u2018number\u2019\nsrc/randomDataGenerators.cpp:166: error: \u2018totalGcd\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:167: error: \u2018number\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:171: error: \u2018number\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:171: error: \u2018mpz_gcd\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:173: error: invalid types \u2018int[int]\u2019 for array subscript\nsrc/randomDataGenerators.cpp:173: error: \u2018number\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:177: error: invalid types \u2018int[int]\u2019 for array subscript\nsrc/randomDataGenerators.cpp:178: error: \u2018totalGcd\u2019 was not declared in this scope\nsrc/randomDataGenerators.cpp:180: error: request for member \u2018begin\u2019 in \u2018degrees\u2019, which is of non-class type \u2018int\u2019\nsrc/randomDataGenerators.cpp:180: error: request for member \u2018end\u2019 in \u2018degrees\u2019, which is of non-class type \u2018int\u2019\nmake: *** [bin/debug/IOHandler.o] Error 1\nmake: *** [bin/debug/BigIdeal.o] Error 1\nmake: *** [bin/debug/randomDataGenerators.o] Error 1\nmkdir -p bin/release/ \ncd bin; rm -f frobby; link ../bin/release/frobby frobby; cd ..\nexport frobby=bin/frobby; ./test/runtests\ndecom      ..........................\nfrob       ..............................\nintersect  ..........\nassoprimes ............\nminimize   ..........\ntransform  .....\nlatformat  .....\nalexdual   ...............\nradical    .........\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing frobby-0.7.6.p1.spkg\n```\nThe main problem seems a wrong or missing include path, which of course causes further errors.",
    "created_at": "2011-09-12T19:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80282",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_080283.json:
```json
{
    "body": "Build with `SAGE_CHECK=yes` on Ubuntu 10.04, GCC 4.3.3",
    "created_at": "2011-09-12T20:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80283",
    "user": "https://github.com/nexttime"
}
```

Build with `SAGE_CHECK=yes` on Ubuntu 10.04, GCC 4.3.3



---

archive/issue_comments_080284.json:
```json
{
    "body": "Attachment [frobby-0.7.6.p1-redhawk-SAGE_CHECK.log](tarball://root/attachments/some-uuid/ticket8783/frobby-0.7.6.p1-redhawk-SAGE_CHECK.log) by @nexttime created at 2011-09-12 20:12:09\n\nOoops, should read 4.**4**.3, but the version shouldn't matter much anyway... ;-)\n\n(Attached the build log.)",
    "created_at": "2011-09-12T20:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80284",
    "user": "https://github.com/nexttime"
}
```

Attachment [frobby-0.7.6.p1-redhawk-SAGE_CHECK.log](tarball://root/attachments/some-uuid/ticket8783/frobby-0.7.6.p1-redhawk-SAGE_CHECK.log) by @nexttime created at 2011-09-12 20:12:09

Ooops, should read 4.**4**.3, but the version shouldn't matter much anyway... ;-)

(Attached the build log.)



---

archive/issue_comments_080285.json:
```json
{
    "body": "I didn't run the build with SAGE_CHECK=yes when I reviewed the package, but I did run the test suite manually. This was on skynet/eno which has GCC 4.6.1 installed. \n\nI just ran the build under Sage 4.7.2.alpha1 on skynet/eno using `export SAGE_CHECK=yes; ./sage -f frobby-0.7.6.p1.spkg` and both the build and the test suite finish without errors. I'll attach the build log.",
    "created_at": "2011-09-13T01:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80285",
    "user": "https://github.com/benjaminfjones"
}
```

I didn't run the build with SAGE_CHECK=yes when I reviewed the package, but I did run the test suite manually. This was on skynet/eno which has GCC 4.6.1 installed. 

I just ran the build under Sage 4.7.2.alpha1 on skynet/eno using `export SAGE_CHECK=yes; ./sage -f frobby-0.7.6.p1.spkg` and both the build and the test suite finish without errors. I'll attach the build log.



---

archive/issue_comments_080286.json:
```json
{
    "body": "Attachment [frobby_build_4.7.2.alpha1.eno.log](tarball://root/attachments/some-uuid/ticket8783/frobby_build_4.7.2.alpha1.eno.log) by @benjaminfjones created at 2011-09-13 01:39:31\n\nfrobby build log with SAGE_CHECK=yes on skynet/eno",
    "created_at": "2011-09-13T01:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80286",
    "user": "https://github.com/benjaminfjones"
}
```

Attachment [frobby_build_4.7.2.alpha1.eno.log](tarball://root/attachments/some-uuid/ticket8783/frobby_build_4.7.2.alpha1.eno.log) by @benjaminfjones created at 2011-09-13 01:39:31

frobby build log with SAGE_CHECK=yes on skynet/eno



---

archive/issue_comments_080287.json:
```json
{
    "body": "Ping.",
    "created_at": "2012-01-22T21:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80287",
    "user": "https://github.com/swenson"
}
```

Ping.



---

archive/issue_comments_080288.json:
```json
{
    "body": "Closing as a duplicate in light of #13007.",
    "created_at": "2012-05-25T20:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80288",
    "user": "https://github.com/benjaminfjones"
}
```

Closing as a duplicate in light of #13007.



---

archive/issue_events_021407.json:
```json
{
    "actor": "https://github.com/benjaminfjones",
    "created_at": "2012-05-25T20:27:33Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8783#event-21407"
}
```



---

archive/issue_comments_080289.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-05-26T01:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8783#issuecomment-80289",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_021408.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-26T01:11:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8783",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8783#event-21408"
}
```
