# Issue 6609: GNUism in lcalc-20080205.p2 passing GNU flags directly to the Sun assembler.

archive/issues_006609.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: GNUism gas assembler\n\nHere's there error messages:\n\n```\nlcalc-20080205.p2/src/src/make_ggo\nlcalc-20080205.p2/src/src/Makefile\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240\n****************************************************\n****************************************************\nGCC Version\ngcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: ../gcc-4.2.4/configure --prefix=/usr/local/gcc-4.2.4-sun-linker/ --with-as=/usr/ccs/bin/as --without-gnu-as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++,fortran --with-mpfr-include=/usr/local/include --with-mpfr-lib=/usr/local/lib --with-gmp-include=/usr/local/include --with-gmp-lib=/usr/local/lib\nThread model: posix\ngcc version 4.2.4\n****************************************************\nBuilding Rubinstein's lcalc program using g++...\ng++  -O2 -g -Wa,-W -fno-exceptions -Wno-deprecated  -DINCLUDE_PARI   \\\n      -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/pari -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include\\\n      -I ../include/ -L/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/lib \\\n      cmdline.c \\\n      Lcommandline.cc Lcommandline_elliptic.cc Lcommandline_globals.cc \\\n      Lcommandline_misc.cc Lcommandline_numbertheory.cc \\\n      Lcommandline_twist.cc Lcommandline_values_zeros.cc \\\n      Lgamma.cc Lglobals.cc Lmisc.cc Lriemannsiegel.cc \\\n            -o lcalc -lpari -lmpfr -lgmpxx -lgmp -liberty\n/usr/ccs/bin/as: error: unknown option 'W'\nusage: /usr/ccs/bin/as [-V] [-Q{y,n}] [-q] [-s]\n        [-S] [-K {pic,PIC}] [-o objfile] [-L] [-T]\n        [-P [[-Yc,path] [-Ipath] [-Dname] [-Dname=def] [-Uname]]...]\n        [-m [-Ym,path]] [-n] [-ul] [-xF]\n        [-m32] [-m64]\n        [-xarch={v7,v8,v8a,v8plus,v8plusa,v8plusb,v9,v9a,v9b,sparc,sparcvis, sparcvis2,sparcfmaf,sparcima}]\n        [-xcode={pic13,pic32}] file.s...\n/usr/ccs/bin/as: error: unknown option 'W'\nusage: /usr/ccs/bin/as [-V] [-Q{y,n}] [-q] [-s]\n        [-S] [-K {pic,PIC}] [-o objfile] [-L] [-T]\n        [-P [[-Yc,path] [-Ipath] [-Dname] [-Dname=def] [-Uname]]...]\n        [-m [-Ym,path]] [-n] [-ul] [-xF]\n        [-m32] [-m64]\n        [-xarch={v7,v8,v8a,v8plus,v8plusa,v8plusb,v9,v9a,v9b,sparc,sparcvis, sparcvis2,sparcfmaf,sparcima}]\n        [-xcode={pic13,pic32}] file.s...\n\n```\n\n\nThe -Wa option to g++ passes the next item (in this case -W) directly to the assembler, in much the same was as -Wl will pass the next item directly to the linker. \n\nlcalc-20080205.p2 is passing -W directly to the assembler, but since gcc was configured to use the Sun assembler, not the GNU one, so it breaks. \n\nUnfortunately, the web page which is supposed to have the documentation for the GNU assembler is down, so I can't actually look up what the -W option does to the GNU assembler and so find out what the Sun equivalent one is. \n\nDave \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6609\n\n",
    "created_at": "2009-07-24T02:24:09Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "GNUism in lcalc-20080205.p2 passing GNU flags directly to the Sun assembler.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6609",
    "user": "drkirkby"
}
```
Assignee: tbd

Keywords: GNUism gas assembler

Here's there error messages:

```
lcalc-20080205.p2/src/src/make_ggo
lcalc-20080205.p2/src/src/Makefile
Finished extraction
****************************************************
Host system
uname -a:
SunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.2.4/configure --prefix=/usr/local/gcc-4.2.4-sun-linker/ --with-as=/usr/ccs/bin/as --without-gnu-as --with-ld=/usr/ccs/bin/ld --without-gnu-ld --enable-languages=c,c++,fortran --with-mpfr-include=/usr/local/include --with-mpfr-lib=/usr/local/lib --with-gmp-include=/usr/local/include --with-gmp-lib=/usr/local/lib
Thread model: posix
gcc version 4.2.4
****************************************************
Building Rubinstein's lcalc program using g++...
g++  -O2 -g -Wa,-W -fno-exceptions -Wno-deprecated  -DINCLUDE_PARI   \
      -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/pari -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include\
      -I ../include/ -L/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/lib \
      cmdline.c \
      Lcommandline.cc Lcommandline_elliptic.cc Lcommandline_globals.cc \
      Lcommandline_misc.cc Lcommandline_numbertheory.cc \
      Lcommandline_twist.cc Lcommandline_values_zeros.cc \
      Lgamma.cc Lglobals.cc Lmisc.cc Lriemannsiegel.cc \
            -o lcalc -lpari -lmpfr -lgmpxx -lgmp -liberty
/usr/ccs/bin/as: error: unknown option 'W'
usage: /usr/ccs/bin/as [-V] [-Q{y,n}] [-q] [-s]
        [-S] [-K {pic,PIC}] [-o objfile] [-L] [-T]
        [-P [[-Yc,path] [-Ipath] [-Dname] [-Dname=def] [-Uname]]...]
        [-m [-Ym,path]] [-n] [-ul] [-xF]
        [-m32] [-m64]
        [-xarch={v7,v8,v8a,v8plus,v8plusa,v8plusb,v9,v9a,v9b,sparc,sparcvis, sparcvis2,sparcfmaf,sparcima}]
        [-xcode={pic13,pic32}] file.s...
/usr/ccs/bin/as: error: unknown option 'W'
usage: /usr/ccs/bin/as [-V] [-Q{y,n}] [-q] [-s]
        [-S] [-K {pic,PIC}] [-o objfile] [-L] [-T]
        [-P [[-Yc,path] [-Ipath] [-Dname] [-Dname=def] [-Uname]]...]
        [-m [-Ym,path]] [-n] [-ul] [-xF]
        [-m32] [-m64]
        [-xarch={v7,v8,v8a,v8plus,v8plusa,v8plusb,v9,v9a,v9b,sparc,sparcvis, sparcvis2,sparcfmaf,sparcima}]
        [-xcode={pic13,pic32}] file.s...

```


The -Wa option to g++ passes the next item (in this case -W) directly to the assembler, in much the same was as -Wl will pass the next item directly to the linker. 

lcalc-20080205.p2 is passing -W directly to the assembler, but since gcc was configured to use the Sun assembler, not the GNU one, so it breaks. 

Unfortunately, the web page which is supposed to have the documentation for the GNU assembler is down, so I can't actually look up what the -W option does to the GNU assembler and so find out what the Sun equivalent one is. 

Dave 


Issue created by migration from https://trac.sagemath.org/ticket/6609





---

archive/issue_comments_054104.json:
```json
{
    "body": "I now know what -W is supposed to do on the GNU linker - suppress warnings from the assembler.",
    "created_at": "2009-08-09T09:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6609#issuecomment-54104",
    "user": "drkirkby"
}
```

I now know what -W is supposed to do on the GNU linker - suppress warnings from the assembler.



---

archive/issue_comments_054105.json:
```json
{
    "body": "I've created a new .spkg file, \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/lcalc-20080205.p3/lcalc-20080205.p3.spkg\n\nwhich removes this flag, designed to suppress warnings. I've also added the compiler option -Wall, to show all warnings, if the compilers are gcc. There are other improvements to the spkg-install file too. \n\nA makefile was updated too, as CFLAGS was used in the makefile, even though no C compiler (only C++) compiler was used. The CXXFLAGS are now set properly, and those used for compiler the C++ code. \n\nThis allows lcalc to build on Solaris, even if the assembler used is Suns. Without this, lcalc will fail if the Sun assembler is used. \n\nSee \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/lcalc-20080205.p3/\nfor all files,",
    "created_at": "2009-09-15T08:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6609#issuecomment-54105",
    "user": "drkirkby"
}
```

I've created a new .spkg file, 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/lcalc-20080205.p3/lcalc-20080205.p3.spkg

which removes this flag, designed to suppress warnings. I've also added the compiler option -Wall, to show all warnings, if the compilers are gcc. There are other improvements to the spkg-install file too. 

A makefile was updated too, as CFLAGS was used in the makefile, even though no C compiler (only C++) compiler was used. The CXXFLAGS are now set properly, and those used for compiler the C++ code. 

This allows lcalc to build on Solaris, even if the assembler used is Suns. Without this, lcalc will fail if the Sun assembler is used. 

See 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/lcalc-20080205.p3/
for all files,



---

archive/issue_comments_054106.json:
```json
{
    "body": "Here is drkirkby's updated package with all changes checked in his name:\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/lcalc-20080205.p3.spkg",
    "created_at": "2009-09-15T15:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6609#issuecomment-54106",
    "user": "mvngu"
}
```

Here is drkirkby's updated package with all changes checked in his name:

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/lcalc-20080205.p3.spkg



---

archive/issue_comments_054107.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-16T01:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6609#issuecomment-54107",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054108.json:
```json
{
    "body": "Here are the results of my testing `lcalc-20080205.p3.spkg`:\n\n* sage.math --- compiles OK; all doctests passed with option `-long`.\n \n* t2.math --- compiles OK; can't run any doctests since Sage doesn't yet compile entirely on t2.math.\n \n* bsd.math (32-bit Mac OS X 10.5.8) --- compiles OK; all doctests passed with option `-long`.\n \n* bsd.math (64-bit Mac OS X 10.5.8) --- compiles OK; got the following doctest failures, all of which had nothing to do with lcalc:\n {{{\nsage -t -long \"ha1-ecl-lcalc/devel/sage/sage/interfaces/maxima.py\"\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/maxima.py\", line 2108:\n    sage: list(v)\nExpected:\n    [0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]\nGot:\n    [0, x, , 3*x^3, 4*x^4, 5*x^5]\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_64\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_maxima.py\n         [17.6 s]\n\n<SNIP>\n\nsage -t -long \"ha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\"\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 445:\n    sage: F == sage0(F)._sage_()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_20[4]>\", line 1, in <module>\n        F == sage0(F)._sage_()###line 445:\n    sage: F == sage0(F)._sage_()\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 455, in _sage_\n        return load(P._local_tmpfile())\n      File \"sage_object.pyx\", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)\n    IOError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/3179//interface//tmp3179.sobj'\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 463:\n    sage: four_gcd(6)\nExpected:\n    2\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 486:\n    sage: sage0(4).gcd\nExpected:\n    <built-in method gcd of sage.rings.integer.Integer object at 0x...>\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 512:\n    sage: half = reduce_load_element(s); half\nExpected:\n    1/2\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 544:\n    sage: sage0_version() == version()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 174:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[2]>\", line 1, in <module>\n        print \"ignore this\";  sage0.cputime()     # random output###line 174:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 185, in cputime\n        return float(s)\n    ValueError: empty string for float()\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 176:\n    sage: sage0('factor(2^157-1)')\nExpected:\n    852133201 * 60726444167 * 1654058017289 * 2134387368610417\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 178:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[4]>\", line 1, in <module>\n        print \"ignore this\";  sage0.cputime()     # random output###line 178:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 185, in cputime\n        return float(s)\n    ValueError: invalid literal for float(): e(None)\n    852133201 * 60726444167 * 1654058017289 * 213438736861041\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 192:\n    sage: len(t) > 100\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[3]>\", line 1, in <module>\n        len(t) > Integer(100)###line 192:\n    sage: len(t) > 100\n    TypeError: object of type 'float' has no len()\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 194:\n    sage: 'gcd' in t\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[4]>\", line 1, in <module>\n        'gcd' in t###line 194:\n    sage: 'gcd' in t\n    TypeError: argument of type 'float' is not iterable\n**********************************************************************\n7 items had failures:\n   1 of   5 in __main__.example_20\n   1 of   4 in __main__.example_21\n   1 of   3 in __main__.example_22\n   1 of   6 in __main__.example_24\n   1 of   4 in __main__.example_26\n   3 of   5 in __main__.example_3\n   2 of   5 in __main__.example_4\n***Test Failed*** 10 failures.\nFor whitespace errors, see the file /scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_sage0.py\n         [16.7 s]\n         \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"ha1-ecl-lcalc/devel/sage/doc/en/bordeaux_2008/birds_other.rst\"\n        sage -t -long \"ha1-ecl-lcalc/devel/sage/sage/interfaces/maxima.py\"\n        sage -t -long \"ha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\"\nTotal time for all tests: 7742.3 seconds\n }}}\n These failures don't have anything to do with the lcalc package.\n \n* cicero on SkyNet (x86 Fedora 9 with GCC 4.4.1) --- compiles OK; I got the following doctest failures, all of which had nothing to do with lcalc:\n {{{\nsage -t -long \"devel/sage/sage/misc/randstate.pyx\"          \n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/misc/randstate.pyx\", line 124:\n    : s = ZZ(subsage('initial_seed()'))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[32]>\", line 1, in <module>\n        s = ZZ(subsage('initial_seed()'))###line 124:\n    : s = ZZ(subsage('initial_seed()'))\n      File \"parent.pyx\", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)\n      File \"coerce_maps.pyx\", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1726, in _integer_\n        return sage.rings.all.Integer(repr(self))\n      File \"integer.pyx\", line 564, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6399)\n    TypeError: unable to convert x (=---------------------------------------------------------------------------\n    AttributeError                            Traceback (most recent call last)\n\n    /home/mvngu/.sage/temp/cicero/21911/_home_mvngu__sage_init_sage_0.py in <module>()\n\n    /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python2.6/site-packages/sage/misc/functional.pyc in gen(x)\n        353     Return the generator of x.\n        354     \"\"\"\n    --> 355     return x.gen()\n        356 \n        357 def gens(x):\n\n    AttributeError: 'int' object has no attribute 'gen') to an integer\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/misc/randstate.pyx\", line 131:\n    : r == ZZ.random_element(2^200)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n   2 of  62 in __main__.example_0\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_randstate.py\n         [21.6 s]\n\n<SNIP>\n\nsage -t -long \"devel/sage/sage/interfaces/expect.py\"        \n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/expect.py\", line 805:\n    sage: print sage0.eval(\"alarm(1); singular._expect_expr('1')\")\nExpected:\n    Control-C pressed.  Interrupting Singular. Please wait a few seconds...\n    ...\n    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds\nGot:\n    ESC[0m\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_15\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_expect.py\n         [16.3 s]\n\n<SNIP>\n\nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"         \n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 55:\n    sage: a^3\nExpected:\n    8\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 62:\n    sage: V.gens()\nExpected:\n    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 75:\n    sage: g = V.0;  g\nExpected:\n    (1, 0, 0, 0)\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 85:\n    sage: s('%s.parent()'%g.name())\nExpected:\n    Vector space of dimension 4 over Rational Field\nGot:\n    (1, 0, 0, 0)\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 93:\n    sage: s('x = 5')\nExpected:\n    5\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 97:\n    sage: s('x')\nExpected:\n    5\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 105:\n    sage: a\nExpected:\n    10\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 114:\n    sage: s3('\"x\"')\nExpected:\n    8\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 116:\n    sage: s('x')\nExpected:\n    5\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 320:\n    sage: sage0.eval('2+2')\nExpected:\n    '4'\nGot:\n    '\\x1b[0m'\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 334:\n    sage: sage0.get('x')\nExpected:\n    '2'\nGot:\n    '4'\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 364:\n    sage: sage0.get('x')\nExpected:\n    \"...NameError: name 'x' is not defined\"\nGot:\n    '2'\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 373:\n    sage: sage0._contains('2', 'QQ')\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 397:\n    sage: sage0.version()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_16[2]>\", line 1, in <module>\n        sage0.version()###line 397:\n    sage: sage0.version()\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 402, in version\n        return sage0_version()\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 547, in sage0_version\n        return str(sage0('version()'))\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 263, in __call__\n        return SageElement(self, x)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1433, in __init__\n        raise TypeError, x\n    TypeError: Error executing code in Sage\n    CODE:\n        sage0=version()\n    Sage ERROR:\n        ---------------------------------------------------------------------------\n    NameError                                 Traceback (most recent call last)\n\n    /home/mvngu/.sage/temp/cicero/16441/_home_mvngu__sage_init_sage_0.py in <module>()\n\n    NameError: name 'x' is not defined\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 399:\n    sage: sage0.version() == version()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 417:\n    sage: sage0.new(2)\nExpected:\n    2\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 445:\n    sage: F == sage0(F)._sage_()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_20[4]>\", line 1, in <module>\n        F == sage0(F)._sage_()###line 445:\n    sage: F == sage0(F)._sage_()\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 455, in _sage_\n        return load(P._local_tmpfile())\n      File \"sage_object.pyx\", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)\n    IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//temp/cicero/16270//interface//tmp16270.sobj'\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 463:\n    sage: four_gcd(6)\nExpected:\n    2\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 486:\n    sage: sage0(4).gcd\nExpected:\n    <built-in method gcd of sage.rings.integer.Integer object at 0x...>\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 512:\n    sage: half = reduce_load_element(s); half\nExpected:\n    1/2\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 544:\n    sage: sage0_version() == version()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 174:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[2]>\", line 1, in <module>\n        print \"ignore this\";  sage0.cputime()     # random output###line 174:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 185, in cputime\n        return float(s)\n    ValueError: invalid literal for float(): Sage Version 4.1.2.alpha1, Release Date: 2009-09-07\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 176:\n    sage: sage0('factor(2^157-1)')\nExpected:\n    852133201 * 60726444167 * 1654058017289 * 2134387368610417\nGot:\n    5.1342189999999999\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 178:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[4]>\", line 1, in <module>\n        print \"ignore this\";  sage0.cputime()     # random output###line 178:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 185, in cputime\n        return float(s)\n    ValueError: empty string for float()\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 192:\n    sage: len(t) > 100\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[3]>\", line 1, in <module>\n        len(t) > Integer(100)###line 192:\n    sage: len(t) > 100\n    TypeError: object of type 'long' has no len()\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 194:\n    sage: 'gcd' in t\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[4]>\", line 1, in <module>\n        'gcd' in t###line 194:\n    sage: 'gcd' in t\n    TypeError: argument of type 'long' is not iterable\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py\", line 204:\n    sage: s.eval('2+2')\nExpected:\n    '4'\nGot:\n    '\\x1b[0m'\n**********************************************************************\n15 items had failures:\n   9 of  23 in __main__.example_1\n   1 of   3 in __main__.example_10\n   1 of   4 in __main__.example_11\n   1 of   6 in __main__.example_13\n   1 of   3 in __main__.example_14\n   2 of   4 in __main__.example_16\n   1 of   4 in __main__.example_18\n   1 of   5 in __main__.example_20\n   1 of   4 in __main__.example_21\n   1 of   3 in __main__.example_22\n   1 of   6 in __main__.example_24\n   1 of   4 in __main__.example_26\n   3 of   5 in __main__.example_3\n   2 of   5 in __main__.example_4\n   1 of   5 in __main__.example_5\n***Test Failed*** 27 failures.\nFor whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_sage0.py\n         [25.3 s]\n\n<SNIP>\n\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"      \n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/server/simple/twist.py\", line 51:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    4\nGot:\n    {\n    \"status\": \"computing\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  24 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_twist.py\n         [18.0 s]\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage/sage/misc/randstate.pyx\"\n        sage -t -long \"devel/sage/sage/interfaces/expect.py\"\n        sage -t -long \"devel/sage/sage/interfaces/sage0.py\"\n        sage -t -long \"devel/sage/sage/server/simple/twist.py\"\nTotal time for all tests: 13572.0 seconds\n }}}\n \n* eno on SkyNet (x86_64 Fedora 9 with GCC 4.4.1) --- compiles OK; I got this doctest failure, which has nothing to do with lcalc:\n {{{\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/lseries_ell.py\"\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n         [0.4 s]\n }}}\n \n* lena on SkyNet (x86_64 RHEL 5.3 with GCC 4.4.1) --- compiles OK; all doctests passed with option `-long`.\n\nThe point is that lcalc now builds on t2.math. So fine by me. Merged in the standard packages repository.",
    "created_at": "2009-09-16T01:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6609",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6609#issuecomment-54108",
    "user": "mvngu"
}
```

Here are the results of my testing `lcalc-20080205.p3.spkg`:

* sage.math --- compiles OK; all doctests passed with option `-long`.
 
* t2.math --- compiles OK; can't run any doctests since Sage doesn't yet compile entirely on t2.math.
 
* bsd.math (32-bit Mac OS X 10.5.8) --- compiles OK; all doctests passed with option `-long`.
 
* bsd.math (64-bit Mac OS X 10.5.8) --- compiles OK; got the following doctest failures, all of which had nothing to do with lcalc:
 {{{
sage -t -long "ha1-ecl-lcalc/devel/sage/sage/interfaces/maxima.py"
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/maxima.py", line 2108:
    sage: list(v)
Expected:
    [0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]
Got:
    [0, x, , 3*x^3, 4*x^4, 5*x^5]
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_64
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_maxima.py
         [17.6 s]

<SNIP>

sage -t -long "ha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py"
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 445:
    sage: F == sage0(F)._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[4]>", line 1, in <module>
        F == sage0(F)._sage_()###line 445:
    sage: F == sage0(F)._sage_()
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 455, in _sage_
        return load(P._local_tmpfile())
      File "sage_object.pyx", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)
    IOError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/3179//interface//tmp3179.sobj'
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 463:
    sage: four_gcd(6)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 486:
    sage: sage0(4).gcd
Expected:
    <built-in method gcd of sage.rings.integer.Integer object at 0x...>
Got:
    <BLANKLINE>
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 512:
    sage: half = reduce_load_element(s); half
Expected:
    1/2
Got:
    <BLANKLINE>
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 544:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: empty string for float()
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 176:
    sage: sage0('factor(2^157-1)')
Expected:
    852133201 * 60726444167 * 1654058017289 * 2134387368610417
Got:
    <BLANKLINE>
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: invalid literal for float(): e(None)
    852133201 * 60726444167 * 1654058017289 * 213438736861041
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 192:
    sage: len(t) > 100
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        len(t) > Integer(100)###line 192:
    sage: len(t) > 100
    TypeError: object of type 'float' has no len()
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 194:
    sage: 'gcd' in t
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        'gcd' in t###line 194:
    sage: 'gcd' in t
    TypeError: argument of type 'float' is not iterable
**********************************************************************
7 items had failures:
   1 of   5 in __main__.example_20
   1 of   4 in __main__.example_21
   1 of   3 in __main__.example_22
   1 of   6 in __main__.example_24
   1 of   4 in __main__.example_26
   3 of   5 in __main__.example_3
   2 of   5 in __main__.example_4
***Test Failed*** 10 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_sage0.py
         [16.7 s]
         
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "ha1-ecl-lcalc/devel/sage/doc/en/bordeaux_2008/birds_other.rst"
        sage -t -long "ha1-ecl-lcalc/devel/sage/sage/interfaces/maxima.py"
        sage -t -long "ha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py"
Total time for all tests: 7742.3 seconds
 }}}
 These failures don't have anything to do with the lcalc package.
 
* cicero on SkyNet (x86 Fedora 9 with GCC 4.4.1) --- compiles OK; I got the following doctest failures, all of which had nothing to do with lcalc:
 {{{
sage -t -long "devel/sage/sage/misc/randstate.pyx"          
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/misc/randstate.pyx", line 124:
    : s = ZZ(subsage('initial_seed()'))
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[32]>", line 1, in <module>
        s = ZZ(subsage('initial_seed()'))###line 124:
    : s = ZZ(subsage('initial_seed()'))
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)
      File "coerce_maps.pyx", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/expect.py", line 1726, in _integer_
        return sage.rings.all.Integer(repr(self))
      File "integer.pyx", line 564, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6399)
    TypeError: unable to convert x (=---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)

    /home/mvngu/.sage/temp/cicero/21911/_home_mvngu__sage_init_sage_0.py in <module>()

    /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python2.6/site-packages/sage/misc/functional.pyc in gen(x)
        353     Return the generator of x.
        354     """
    --> 355     return x.gen()
        356 
        357 def gens(x):

    AttributeError: 'int' object has no attribute 'gen') to an integer
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/misc/randstate.pyx", line 131:
    : r == ZZ.random_element(2^200)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   2 of  62 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_randstate.py
         [21.6 s]

<SNIP>

sage -t -long "devel/sage/sage/interfaces/expect.py"        
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/expect.py", line 805:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Expected:
    Control-C pressed.  Interrupting Singular. Please wait a few seconds...
    ...
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
Got:
    ESC[0m
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_expect.py
         [16.3 s]

<SNIP>

sage -t -long "devel/sage/sage/interfaces/sage0.py"         
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 55:
    sage: a^3
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 62:
    sage: V.gens()
Expected:
    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 75:
    sage: g = V.0;  g
Expected:
    (1, 0, 0, 0)
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 85:
    sage: s('%s.parent()'%g.name())
Expected:
    Vector space of dimension 4 over Rational Field
Got:
    (1, 0, 0, 0)
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 93:
    sage: s('x = 5')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 97:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 105:
    sage: a
Expected:
    10
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 114:
    sage: s3('"x"')
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 116:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 320:
    sage: sage0.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0m'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 334:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '4'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 364:
    sage: sage0.get('x')
Expected:
    "...NameError: name 'x' is not defined"
Got:
    '2'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 373:
    sage: sage0._contains('2', 'QQ')
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 397:
    sage: sage0.version()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[2]>", line 1, in <module>
        sage0.version()###line 397:
    sage: sage0.version()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 402, in version
        return sage0_version()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 547, in sage0_version
        return str(sage0('version()'))
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 263, in __call__
        return SageElement(self, x)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/expect.py", line 1433, in __init__
        raise TypeError, x
    TypeError: Error executing code in Sage
    CODE:
        sage0=version()
    Sage ERROR:
        ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    /home/mvngu/.sage/temp/cicero/16441/_home_mvngu__sage_init_sage_0.py in <module>()

    NameError: name 'x' is not defined
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 399:
    sage: sage0.version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 417:
    sage: sage0.new(2)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 445:
    sage: F == sage0(F)._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[4]>", line 1, in <module>
        F == sage0(F)._sage_()###line 445:
    sage: F == sage0(F)._sage_()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 455, in _sage_
        return load(P._local_tmpfile())
      File "sage_object.pyx", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)
    IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//temp/cicero/16270//interface//tmp16270.sobj'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 463:
    sage: four_gcd(6)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 486:
    sage: sage0(4).gcd
Expected:
    <built-in method gcd of sage.rings.integer.Integer object at 0x...>
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 512:
    sage: half = reduce_load_element(s); half
Expected:
    1/2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 544:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: invalid literal for float(): Sage Version 4.1.2.alpha1, Release Date: 2009-09-07
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 176:
    sage: sage0('factor(2^157-1)')
Expected:
    852133201 * 60726444167 * 1654058017289 * 2134387368610417
Got:
    5.1342189999999999
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: empty string for float()
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 192:
    sage: len(t) > 100
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        len(t) > Integer(100)###line 192:
    sage: len(t) > 100
    TypeError: object of type 'long' has no len()
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 194:
    sage: 'gcd' in t
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        'gcd' in t###line 194:
    sage: 'gcd' in t
    TypeError: argument of type 'long' is not iterable
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/interfaces/sage0.py", line 204:
    sage: s.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0m'
**********************************************************************
15 items had failures:
   9 of  23 in __main__.example_1
   1 of   3 in __main__.example_10
   1 of   4 in __main__.example_11
   1 of   6 in __main__.example_13
   1 of   3 in __main__.example_14
   2 of   4 in __main__.example_16
   1 of   4 in __main__.example_18
   1 of   5 in __main__.example_20
   1 of   4 in __main__.example_21
   1 of   3 in __main__.example_22
   1 of   6 in __main__.example_24
   1 of   4 in __main__.example_26
   3 of   5 in __main__.example_3
   2 of   5 in __main__.example_4
   1 of   5 in __main__.example_5
***Test Failed*** 27 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_sage0.py
         [25.3 s]

<SNIP>

sage -t -long "devel/sage/sage/server/simple/twist.py"      
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/devel/sage/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "computing",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-ecl-lcalc/tmp/.doctest_twist.py
         [18.0 s]
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/misc/randstate.pyx"
        sage -t -long "devel/sage/sage/interfaces/expect.py"
        sage -t -long "devel/sage/sage/interfaces/sage0.py"
        sage -t -long "devel/sage/sage/server/simple/twist.py"
Total time for all tests: 13572.0 seconds
 }}}
 
* eno on SkyNet (x86_64 Fedora 9 with GCC 4.4.1) --- compiles OK; I got this doctest failure, which has nothing to do with lcalc:
 {{{
sage -t -long "devel/sage/sage/schemes/elliptic_curves/lseries_ell.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [0.4 s]
 }}}
 
* lena on SkyNet (x86_64 RHEL 5.3 with GCC 4.4.1) --- compiles OK; all doctests passed with option `-long`.

The point is that lcalc now builds on t2.math. So fine by me. Merged in the standard packages repository.
