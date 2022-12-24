# Issue 8770: gfan fails to build on Fedora Core 12 wtih GCC-4.5.0 (lena)

archive/issues_008770.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\n\n```\ng++  -O2 -DGMPRATIONAL -g -I /home/wstein/screen/lena/sage-4.4/local/include    -c halfopencone.cpp\ng++  -O2 -DGMPRATIONAL -g -I /home/wstein/screen/lena/sage-4.4/local/include    -c lll.cpp\n/tmp/ccngbXYk.s: Assembler messages:\n/tmp/ccngbXYk.s:16711: Error: symbol `_ZZN6MatrixIiEixEPiPP6VektorIiEiE19__PRETTY_FUNCTION__' is already defined\nmake[2]: *** [lll.o] Error 1\nmake[2]: Leaving directory `/home/wstein/screen/lena/sage-4.4/spkg/build/gfan-0.4plus/src'\nError building gfan\n\nreal    0m54.211s\nuser    0m50.094s\nsys     0m3.030s\nsage: An error occurred while installing gfan-0.4plus\n```\n\n\nAbout the machine:\n\n```\n[wstein@lena sage-4.4]$ gcc -v\nUsing built-in specs.\nCOLLECT_GCC=gcc\nCOLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-k10-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper\nTarget: x86_64-unknown-linux-gnu\nConfigured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-gnu-as=/usr/local/binutils-2.20.1/x86_64-Linux-k10-fc-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-k10-fc-gcc-4.4.3/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-k10-gcc-4.2.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-k10-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-k10-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3 --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-k10-fc\nThread model: posix\ngcc version 4.5.0 (GCC)\n[wstein@lena sage-4.4]$ uname -a\nLinux lena 2.6.31.12-174.2.19.fc12.x86_64 #1 SMP Thu Feb 11 07:07:16 UTC 2010 x86_64 x86_64 x86_64 GNU/Linux\n[wstein@lena sage-4.4]$ cat /etc/issue\nFedora release 12 (Constantine)\nKernel \\r on an \\m (\\l)\n                          \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8770\n\n",
    "created_at": "2010-04-26T20:08:26Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "gfan fails to build on Fedora Core 12 wtih GCC-4.5.0 (lena)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8770",
    "user": "@williamstein"
}
```
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
[wstein@lena sage-4.4]$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-k10-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-gnu-as=/usr/local/binutils-2.20.1/x86_64-Linux-k10-fc-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-k10-fc-gcc-4.4.3/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-k10-gcc-4.2.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-k10-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-k10-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3 --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-k10-fc
Thread model: posix
gcc version 4.5.0 (GCC)
[wstein@lena sage-4.4]$ uname -a
Linux lena 2.6.31.12-174.2.19.fc12.x86_64 #1 SMP Thu Feb 11 07:07:16 UTC 2010 x86_64 x86_64 x86_64 GNU/Linux
[wstein@lena sage-4.4]$ cat /etc/issue
Fedora release 12 (Constantine)
Kernel \r on an \m (\l)
                          
```


Issue created by migration from https://trac.sagemath.org/ticket/8770





---

archive/issue_comments_080257.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to @williamstein.",
    "created_at": "2010-04-26T20:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80257",
    "user": "@williamstein"
}
```

Changing assignee from GeorgSWeber to @williamstein.



---

archive/issue_comments_080258.json:
```json
{
    "body": "Discoveries:\n\nIn gfan with GCC-4.5.0 on \"lena (a k10)\" linux box:\n\n```\ng++  -DGMPRATIONAL    -c lll.cpp\n```\n\nworks fine, but\n\n```\nsage subshell$ g++ -O2 -DGMPRATIONAL    -c lll.cpp\n/tmp/cchu2txF.s: Assembler messages:\n/tmp/cchu2txF.s:5145: Error: symbol `_ZZN6MatrixIiEixEPiPP6VektorIiEiE19__PRETTY_FUNCTION__' is already defined\n```\n\n\nDoing make after compiling without -O2 gives:\n\n```\n...\ng++  -O2 -DGMPRATIONAL -g     -c linalg.cpp\nlinalg.cpp:528:1: error: \u2018FieldMatrix::FieldMatrix\u2019 names the constructor, not the type\nmake: *** [linalg.o] Error 1\n/home/wstein/screen/lena/sage-4.4\n```\n",
    "created_at": "2010-04-26T20:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80258",
    "user": "@williamstein"
}
```

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

archive/issue_comments_080259.json:
```json
{
    "body": "The fix for linalg.cpp:528 is to replace that line of linalg.cpp with:\n\n```\nFieldMatrix FieldMatrix::solver()const\n```\n",
    "created_at": "2010-04-26T20:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80259",
    "user": "@williamstein"
}
```

The fix for linalg.cpp:528 is to replace that line of linalg.cpp with:

```
FieldMatrix FieldMatrix::solver()const
```




---

archive/issue_comments_080260.json:
```json
{
    "body": "With the above two fixes:\n\n  (1) build with optimization off\n\n  (2) Make one change in linalg.cpp\n\ngfan builds and installs.",
    "created_at": "2010-04-26T20:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80260",
    "user": "@williamstein"
}
```

With the above two fixes:

  (1) build with optimization off

  (2) Make one change in linalg.cpp

gfan builds and installs.



---

archive/issue_comments_080261.json:
```json
{
    "body": "Some observations on the duplicate symbol:\n\ng++ 4.5 seems to mangle the `__PRETTY_FUNCTION__` symbol of two different `operator[]`'s (differing in their const-ness) to the same symbol, which is most likely a compiler bug, I think.\n\nThese `__PRETTY_FUNCTION__` symbols are only generated because of the asserts in `Matrix::operator[]` in `matrix.h`, so disabling those two asserts would be a workaround.",
    "created_at": "2010-04-26T23:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80261",
    "user": "@wjp"
}
```

Some observations on the duplicate symbol:

g++ 4.5 seems to mangle the `__PRETTY_FUNCTION__` symbol of two different `operator[]`'s (differing in their const-ness) to the same symbol, which is most likely a compiler bug, I think.

These `__PRETTY_FUNCTION__` symbols are only generated because of the asserts in `Matrix::operator[]` in `matrix.h`, so disabling those two asserts would be a workaround.



---

archive/issue_comments_080262.json:
```json
{
    "body": "and from wjp:\n\n```\n17:01 < wjp> something like \"check for gcc 4.5, and pass -fno-ipa-rsa if found\" should do the trick, I think\n```\n",
    "created_at": "2010-04-27T00:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80262",
    "user": "@williamstein"
}
```

and from wjp:

```
17:01 < wjp> something like "check for gcc 4.5, and pass -fno-ipa-rsa if found" should do the trick, I think
```




---

archive/issue_comments_080263.json:
```json
{
    "body": "I submitted the duplicate symbol issue to gcc's bug tracker:\n\nhttp://gcc.gnu.org/bugzilla/show_bug.cgi?id=43905",
    "created_at": "2010-04-27T01:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80263",
    "user": "@wjp"
}
```

I submitted the duplicate symbol issue to gcc's bug tracker:

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=43905



---

archive/issue_comments_080264.json:
```json
{
    "body": "From Upstream:\n\n```\nAnders Nedergaard Jensen to me, Willem\nshow details 2:23 AM (17 hours ago)\nHi William,\nThanks for reporting these \"bugs\".\n\n\"FieldMatrix::FieldMatrix\" should clearly be \"FieldMatrix\".\n\nFor the assert problem, an acceptable solution for you is to remove one of the assert statements.\n\nI will code my way around the gcc4.5 bug for the next gfan release.\n-Anders\n```\n",
    "created_at": "2010-04-28T03:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80264",
    "user": "@williamstein"
}
```

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

archive/issue_comments_080265.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-28T16:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80265",
    "user": "@wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080266.json:
```json
{
    "body": "I created a p1 that applies the changes Anders confirmed.\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/gfan-0.4plus.p1.spkg",
    "created_at": "2010-04-28T16:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80266",
    "user": "@wjp"
}
```

I created a p1 that applies the changes Anders confirmed.

http://www.math.leidenuniv.nl/~wpalenst/sage/gfan-0.4plus.p1.spkg



---

archive/issue_comments_080267.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-28T19:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80267",
    "user": "@williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080268.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-04-28T19:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80268",
    "user": "@williamstein"
}
```

Looks good.



---

archive/issue_comments_080269.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T19:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80269",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_080270.json:
```json
{
    "body": "The gcc bug involved is now fixed in gcc trunk according to\n\nhttp://gcc.gnu.org/bugzilla/show_bug.cgi?id=43905",
    "created_at": "2010-06-24T13:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8770#issuecomment-80270",
    "user": "@wjp"
}
```

The gcc bug involved is now fixed in gcc trunk according to

http://gcc.gnu.org/bugzilla/show_bug.cgi?id=43905
