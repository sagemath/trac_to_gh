# Issue 9591: Upgrade genus2reduction to pari 2.4.3

archive/issues_009591.json:
```json
{
    "body": "Assignee: tbd\n\nAfter upgrading PARI/GP to version 2.4.3 (#9343), genus2reduction no longer compiles properly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9591\n\n",
    "created_at": "2010-07-24T11:56:21Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Upgrade genus2reduction to pari 2.4.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9591",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: tbd

After upgrading PARI/GP to version 2.4.3 (#9343), genus2reduction no longer compiles properly.

Issue created by migration from https://trac.sagemath.org/ticket/9591





---

archive/issue_comments_092593.json:
```json
{
    "body": "New version which works with PARI 2.4.3: [http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg](http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg)\n\nAll I had to do was to rename some functions (digging in earlier versions of PARI to see what the undefined functions meant).",
    "created_at": "2010-07-24T12:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92593",
    "user": "https://github.com/jdemeyer"
}
```

New version which works with PARI 2.4.3: [http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg](http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p7.spkg)

All I had to do was to rename some functions (digging in earlier versions of PARI to see what the undefined functions meant).



---

archive/issue_comments_092594.json:
```json
{
    "body": "out of curiosity what did you replace \"gi\" with? \n\nI had a hard figuring that one out when I tried to fix this myself.",
    "created_at": "2010-07-24T18:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92594",
    "user": "https://github.com/kiwifb"
}
```

out of curiosity what did you replace "gi" with? 

I had a hard figuring that one out when I tried to fix this myself.



---

archive/issue_comments_092595.json:
```json
{
    "body": "Replying to [comment:2 fbissey]:\n> out of curiosity what did you replace \"gi\" with? \n\n\n> I had a hard figuring that one out when I tried to fix this myself. \n\n\ngi should be replaced by gen_I().",
    "created_at": "2010-07-24T22:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92595",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:2 fbissey]:
> out of curiosity what did you replace "gi" with? 


> I had a hard figuring that one out when I tried to fix this myself. 


gi should be replaced by gen_I().



---

archive/issue_events_023889.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-07-29T14:46:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9591#event-23889"
}
```



---

archive/issue_comments_092596.json:
```json
{
    "body": "We may need to coordinate this ticket with #9738, which is about a segfault caused by `SAGE_LOCAL/bin/genus2reduction`.",
    "created_at": "2010-08-13T01:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92596",
    "user": "https://github.com/qed777"
}
```

We may need to coordinate this ticket with #9738, which is about a segfault caused by `SAGE_LOCAL/bin/genus2reduction`.



---

archive/issue_comments_092597.json:
```json
{
    "body": "By the way, would it be worth it to rewrite `genus2reduction.c` in Cython and include it in the Sage library?",
    "created_at": "2010-08-13T10:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92597",
    "user": "https://github.com/qed777"
}
```

By the way, would it be worth it to rewrite `genus2reduction.c` in Cython and include it in the Sage library?



---

archive/issue_comments_092598.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n> By the way, would it be worth it to rewrite `genus2reduction.c` in Cython and include it in the Sage library?\n\n\nI guess it makes sense to include it in the sage library since it's just 1 file.  But I don't think it is very important.",
    "created_at": "2010-08-13T22:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92598",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:7 mpatel]:
> By the way, would it be worth it to rewrite `genus2reduction.c` in Cython and include it in the Sage library?


I guess it makes sense to include it in the sage library since it's just 1 file.  But I don't think it is very important.



---

archive/issue_comments_092599.json:
```json
{
    "body": "I merged my patch from #9738. New spkg at [http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg](http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg)",
    "created_at": "2010-08-14T20:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92599",
    "user": "https://github.com/jdemeyer"
}
```

I merged my patch from #9738. New spkg at [http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg](http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg)



---

archive/issue_comments_092600.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-14T20:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92600",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092601.json:
```json
{
    "body": "If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. \n\nBut this fails to build on OpenSolaris 32-bit, despite the previous version working fine. \n\n```\ndrkirkby@hawk:~/32/sage-4.5.3.alpha0$ ./sage -i http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg\nInstalling http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg\nCalling sage-spkg on http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg\nWarning: Attempted to overwrite SAGE_ROOT environment variable\ngenus2reduction-0.3.p8\nMachine:\nSunOS hawk 5.11 snv_134 i86pc i386 i86pc\nDeleting directories from past builds of previous/current versions of genus2reduction-0.3.p8\nExtracting package /export/home/drkirkby/32/sage-4.5.3.alpha0/spkg/optional/genus2reduction-0.3.p8.spkg ...\n-rw-r--r--   1 drkirkby staff      53471 Aug 14 23:35 /export/home/drkirkby/32/sage-4.5.3.alpha0/spkg/optional/genus2reduction-0.3.p8.spkg\ngenus2reduction-0.3.p8/\ngenus2reduction-0.3.p8/.hg/\ngenus2reduction-0.3.p8/.hg/requires\ngenus2reduction-0.3.p8/.hg/store/\ngenus2reduction-0.3.p8/.hg/store/data/\ngenus2reduction-0.3.p8/.hg/store/data/src/\ngenus2reduction-0.3.p8/.hg/store/data/src/genus2reduction.c.i\ngenus2reduction-0.3.p8/.hg/store/data/.hgignore.i\ngenus2reduction-0.3.p8/.hg/store/data/dist/\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/rules.i\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/control.i\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/compat.i\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/copyright.i\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/series.i\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/makefile.patch.i\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/control.in.i\ngenus2reduction-0.3.p8/.hg/store/data/dist/debian/changelog.i\ngenus2reduction-0.3.p8/.hg/store/data/spkg-install.i\ngenus2reduction-0.3.p8/.hg/store/data/_s_p_k_g.txt.i\ngenus2reduction-0.3.p8/.hg/store/undo\ngenus2reduction-0.3.p8/.hg/store/00manifest.i\ngenus2reduction-0.3.p8/.hg/store/00changelog.i\ngenus2reduction-0.3.p8/.hg/undo.dirstate\ngenus2reduction-0.3.p8/.hg/dirstate\ngenus2reduction-0.3.p8/.hg/00changelog.i\ngenus2reduction-0.3.p8/.hg/branch\ngenus2reduction-0.3.p8/.hg/undo.branch\ngenus2reduction-0.3.p8/src/\ngenus2reduction-0.3.p8/src/.pc/\ngenus2reduction-0.3.p8/src/.pc/.version\ngenus2reduction-0.3.p8/src/TODO\ngenus2reduction-0.3.p8/src/README\ngenus2reduction-0.3.p8/src/THANKS\ngenus2reduction-0.3.p8/src/genus2reduction.c\ngenus2reduction-0.3.p8/src/gpl-email.txt\ngenus2reduction-0.3.p8/src/SAGE.txt\ngenus2reduction-0.3.p8/src/RELEASE.NOTES\ngenus2reduction-0.3.p8/src/WARNING\ngenus2reduction-0.3.p8/src/INSTALL\ngenus2reduction-0.3.p8/src/CHANGES\ngenus2reduction-0.3.p8/src/COPYING\ngenus2reduction-0.3.p8/dist/\ngenus2reduction-0.3.p8/dist/debian/\ngenus2reduction-0.3.p8/dist/debian/control\ngenus2reduction-0.3.p8/dist/debian/rules\ngenus2reduction-0.3.p8/dist/debian/changelog\ngenus2reduction-0.3.p8/dist/debian/compat\ngenus2reduction-0.3.p8/dist/debian/control.in\ngenus2reduction-0.3.p8/dist/debian/patches/\ngenus2reduction-0.3.p8/dist/debian/patches/makefile.patch\ngenus2reduction-0.3.p8/dist/debian/patches/series\ngenus2reduction-0.3.p8/dist/debian/copyright\ngenus2reduction-0.3.p8/.hgignore\ngenus2reduction-0.3.p8/SPKG.txt\ngenus2reduction-0.3.p8/spkg-install\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_134 i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nCOLLECT_GCC=gcc\nCOLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/libexec/gcc/i386-pc-solaris2.10/4.5.0/lto-wrapper\nTarget: i386-pc-solaris2.10\nConfigured with: ../gcc-4.5.0/configure --prefix=/usr/local/gcc-4.5.0 --build=i386-pc-solaris2.10 --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.5.0 --with-mpfr=/usr/local/gcc-4.5.0 --disable-nls --enable-checking=release --enable-werror=no --enable-multilib -with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld\nThread model: posix\ngcc version 4.5.0 (GCC) \n****************************************************\nCompiling genus2reduction.c\ngenus2reduction.c:32:1: error: expected identifier or '(' before 'long'\ngenus2reduction.c:32:1: error: expected ')' before '>' token\ngenus2reduction.c:39:1: error: expected identifier or '(' before 'long'\ngenus2reduction.c:39:1: error: expected ')' before '>' token\ngenus2reduction.c: In function 'main':\ngenus2reduction.c:494:27: error: called object 'pol_1' is not a function\ngenus2reduction.c:545:24: error: called object 'pol_1' is not a function\ngenus2reduction.c:618:37: error: called object 'pol_x' is not a function\ngenus2reduction.c:618:55: error: called object 'pol_x' is not a function\ngenus2reduction.c:676:46: error: called object 'pol_x' is not a function\ngenus2reduction.c:692:46: error: called object 'pol_x' is not a function\ngenus2reduction.c:741:44: error: called object 'pol_x' is not a function\ngenus2reduction.c:770:42: error: called object 'pol_x' is not a function\ngenus2reduction.c: In function 'factorpadicnonun':\ngenus2reduction.c:1685:37: error: subscripted value is neither array nor pointer\ngenus2reduction.c:1694:58: error: called object 'pol_x' is not a function\ngenus2reduction.c:1695:54: error: called object 'pol_x' is not a function\ngenus2reduction.c:1695:7: warning: passing argument 1 of 'gsubst' makes pointer from integer without a cast\n/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1138:9: note: expected 'GEN' but argument is of type 'int'\ngenus2reduction.c: In function 'polymini':\ngenus2reduction.c:1719:28: error: called object 'pol_x' is not a function\ngenus2reduction.c:1719:59: error: called object 'pol_x' is not a function\ngenus2reduction.c:1734:46: error: called object 'pol_x' is not a function\ngenus2reduction.c:1753:33: error: called object 'pol_x' is not a function\ngenus2reduction.c:1762:34: error: called object 'pol_x' is not a function\ngenus2reduction.c:1774:42: error: called object 'pol_x' is not a function\ngenus2reduction.c:1783:31: error: called object 'pol_x' is not a function\ngenus2reduction.c:1789:47: error: called object 'pol_x' is not a function\ngenus2reduction.c: In function 'discpart':\ngenus2reduction.c:1836:13: error: called object 'pol_1' is not a function\ngenus2reduction.c: In function 'polyminizi':\ngenus2reduction.c:1874:3: warning: passing argument 2 of 'gadd' makes pointer from integer without a cast\n/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1014:9: note: expected 'GEN' but argument is of type 'int'\ngenus2reduction.c:1877:32: error: called object 'pol_x' is not a function\ngenus2reduction.c:1882:46: error: called object 'pol_x' is not a function\ngenus2reduction.c:1900:38: error: called object 'pol_x' is not a function\ngenus2reduction.c: In function 'polyminizi2':\ngenus2reduction.c:1956:39: error: called object 'pol_x' is not a function\ngenus2reduction.c:1959:68: warning: assignment makes pointer from integer without a cast\ngenus2reduction.c:1969:32: error: called object 'pol_x' is not a function\ngenus2reduction.c:1974:46: error: called object 'pol_x' is not a function\ngenus2reduction.c: In function 'zi2mod':\ngenus2reduction.c:2018:3: warning: passing argument 2 of 'gmul' makes pointer from integer without a cast\n/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1018:9: note: expected 'GEN' but argument is of type 'int'\nError building genus2reduction\n\nreal\t0m0.069s\nuser\t0m0.052s\nsys\t0m0.014s\nsage: An error occurred while installing genus2reduction-0.3.p8\n```",
    "created_at": "2010-08-14T22:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92601",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. 

But this fails to build on OpenSolaris 32-bit, despite the previous version working fine. 

```
drkirkby@hawk:~/32/sage-4.5.3.alpha0$ ./sage -i http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg
Installing http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg
Calling sage-spkg on http://cage.ugent.be/~jdemeyer/sage/genus2reduction-0.3.p8.spkg
Warning: Attempted to overwrite SAGE_ROOT environment variable
genus2reduction-0.3.p8
Machine:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
Deleting directories from past builds of previous/current versions of genus2reduction-0.3.p8
Extracting package /export/home/drkirkby/32/sage-4.5.3.alpha0/spkg/optional/genus2reduction-0.3.p8.spkg ...
-rw-r--r--   1 drkirkby staff      53471 Aug 14 23:35 /export/home/drkirkby/32/sage-4.5.3.alpha0/spkg/optional/genus2reduction-0.3.p8.spkg
genus2reduction-0.3.p8/
genus2reduction-0.3.p8/.hg/
genus2reduction-0.3.p8/.hg/requires
genus2reduction-0.3.p8/.hg/store/
genus2reduction-0.3.p8/.hg/store/data/
genus2reduction-0.3.p8/.hg/store/data/src/
genus2reduction-0.3.p8/.hg/store/data/src/genus2reduction.c.i
genus2reduction-0.3.p8/.hg/store/data/.hgignore.i
genus2reduction-0.3.p8/.hg/store/data/dist/
genus2reduction-0.3.p8/.hg/store/data/dist/debian/
genus2reduction-0.3.p8/.hg/store/data/dist/debian/rules.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/control.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/compat.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/copyright.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/
genus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/series.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/patches/makefile.patch.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/control.in.i
genus2reduction-0.3.p8/.hg/store/data/dist/debian/changelog.i
genus2reduction-0.3.p8/.hg/store/data/spkg-install.i
genus2reduction-0.3.p8/.hg/store/data/_s_p_k_g.txt.i
genus2reduction-0.3.p8/.hg/store/undo
genus2reduction-0.3.p8/.hg/store/00manifest.i
genus2reduction-0.3.p8/.hg/store/00changelog.i
genus2reduction-0.3.p8/.hg/undo.dirstate
genus2reduction-0.3.p8/.hg/dirstate
genus2reduction-0.3.p8/.hg/00changelog.i
genus2reduction-0.3.p8/.hg/branch
genus2reduction-0.3.p8/.hg/undo.branch
genus2reduction-0.3.p8/src/
genus2reduction-0.3.p8/src/.pc/
genus2reduction-0.3.p8/src/.pc/.version
genus2reduction-0.3.p8/src/TODO
genus2reduction-0.3.p8/src/README
genus2reduction-0.3.p8/src/THANKS
genus2reduction-0.3.p8/src/genus2reduction.c
genus2reduction-0.3.p8/src/gpl-email.txt
genus2reduction-0.3.p8/src/SAGE.txt
genus2reduction-0.3.p8/src/RELEASE.NOTES
genus2reduction-0.3.p8/src/WARNING
genus2reduction-0.3.p8/src/INSTALL
genus2reduction-0.3.p8/src/CHANGES
genus2reduction-0.3.p8/src/COPYING
genus2reduction-0.3.p8/dist/
genus2reduction-0.3.p8/dist/debian/
genus2reduction-0.3.p8/dist/debian/control
genus2reduction-0.3.p8/dist/debian/rules
genus2reduction-0.3.p8/dist/debian/changelog
genus2reduction-0.3.p8/dist/debian/compat
genus2reduction-0.3.p8/dist/debian/control.in
genus2reduction-0.3.p8/dist/debian/patches/
genus2reduction-0.3.p8/dist/debian/patches/makefile.patch
genus2reduction-0.3.p8/dist/debian/patches/series
genus2reduction-0.3.p8/dist/debian/copyright
genus2reduction-0.3.p8/.hgignore
genus2reduction-0.3.p8/SPKG.txt
genus2reduction-0.3.p8/spkg-install
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/libexec/gcc/i386-pc-solaris2.10/4.5.0/lto-wrapper
Target: i386-pc-solaris2.10
Configured with: ../gcc-4.5.0/configure --prefix=/usr/local/gcc-4.5.0 --build=i386-pc-solaris2.10 --enable-languages=c,c++,fortran --with-gmp=/usr/local/gcc-4.5.0 --with-mpfr=/usr/local/gcc-4.5.0 --disable-nls --enable-checking=release --enable-werror=no --enable-multilib -with-system-zlib --enable-bootstrap --with-gnu-as --with-as=/usr/local/binutils-2.20/bin/as --without-gnu-ld --with-ld=/usr/ccs/bin/ld
Thread model: posix
gcc version 4.5.0 (GCC) 
****************************************************
Compiling genus2reduction.c
genus2reduction.c:32:1: error: expected identifier or '(' before 'long'
genus2reduction.c:32:1: error: expected ')' before '>' token
genus2reduction.c:39:1: error: expected identifier or '(' before 'long'
genus2reduction.c:39:1: error: expected ')' before '>' token
genus2reduction.c: In function 'main':
genus2reduction.c:494:27: error: called object 'pol_1' is not a function
genus2reduction.c:545:24: error: called object 'pol_1' is not a function
genus2reduction.c:618:37: error: called object 'pol_x' is not a function
genus2reduction.c:618:55: error: called object 'pol_x' is not a function
genus2reduction.c:676:46: error: called object 'pol_x' is not a function
genus2reduction.c:692:46: error: called object 'pol_x' is not a function
genus2reduction.c:741:44: error: called object 'pol_x' is not a function
genus2reduction.c:770:42: error: called object 'pol_x' is not a function
genus2reduction.c: In function 'factorpadicnonun':
genus2reduction.c:1685:37: error: subscripted value is neither array nor pointer
genus2reduction.c:1694:58: error: called object 'pol_x' is not a function
genus2reduction.c:1695:54: error: called object 'pol_x' is not a function
genus2reduction.c:1695:7: warning: passing argument 1 of 'gsubst' makes pointer from integer without a cast
/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1138:9: note: expected 'GEN' but argument is of type 'int'
genus2reduction.c: In function 'polymini':
genus2reduction.c:1719:28: error: called object 'pol_x' is not a function
genus2reduction.c:1719:59: error: called object 'pol_x' is not a function
genus2reduction.c:1734:46: error: called object 'pol_x' is not a function
genus2reduction.c:1753:33: error: called object 'pol_x' is not a function
genus2reduction.c:1762:34: error: called object 'pol_x' is not a function
genus2reduction.c:1774:42: error: called object 'pol_x' is not a function
genus2reduction.c:1783:31: error: called object 'pol_x' is not a function
genus2reduction.c:1789:47: error: called object 'pol_x' is not a function
genus2reduction.c: In function 'discpart':
genus2reduction.c:1836:13: error: called object 'pol_1' is not a function
genus2reduction.c: In function 'polyminizi':
genus2reduction.c:1874:3: warning: passing argument 2 of 'gadd' makes pointer from integer without a cast
/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1014:9: note: expected 'GEN' but argument is of type 'int'
genus2reduction.c:1877:32: error: called object 'pol_x' is not a function
genus2reduction.c:1882:46: error: called object 'pol_x' is not a function
genus2reduction.c:1900:38: error: called object 'pol_x' is not a function
genus2reduction.c: In function 'polyminizi2':
genus2reduction.c:1956:39: error: called object 'pol_x' is not a function
genus2reduction.c:1959:68: warning: assignment makes pointer from integer without a cast
genus2reduction.c:1969:32: error: called object 'pol_x' is not a function
genus2reduction.c:1974:46: error: called object 'pol_x' is not a function
genus2reduction.c: In function 'zi2mod':
genus2reduction.c:2018:3: warning: passing argument 2 of 'gmul' makes pointer from integer without a cast
/export/home/drkirkby/32/sage-4.5.3.alpha0/local/include/pari/paridecl.h:1018:9: note: expected 'GEN' but argument is of type 'int'
Error building genus2reduction

real	0m0.069s
user	0m0.052s
sys	0m0.014s
sage: An error occurred while installing genus2reduction-0.3.p8
```



---

archive/issue_comments_092602.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-14T22:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92602",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092603.json:
```json
{
    "body": "I had that when making the ebuild for gentoo earlier. You are not compiling it\nagainst pari-2.4.xx - that's what the problem is.",
    "created_at": "2010-08-15T00:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92603",
    "user": "https://github.com/kiwifb"
}
```

I had that when making the ebuild for gentoo earlier. You are not compiling it
against pari-2.4.xx - that's what the problem is.



---

archive/issue_comments_092604.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-15T02:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92604",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092605.json:
```json
{
    "body": "Replying to [comment:12 fbissey]:\n> I had that when making the ebuild for gentoo earlier. You are not compiling it\n> against pari-2.4.xx - that's what the problem is.\n\n\nYes, sorry, my mistake. \n\nI've stuck it back to \"needs review\". I dn't feel able to review it, but after installing the pari package, this installs cleanly. \n\n**I've only tested on OpenSolaris x64 as a 32-bit binary** - so I have not tested on Solaris SPARC (e.g. t2)\n\nDave",
    "created_at": "2010-08-15T02:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92605",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:12 fbissey]:
> I had that when making the ebuild for gentoo earlier. You are not compiling it
> against pari-2.4.xx - that's what the problem is.


Yes, sorry, my mistake. 

I've stuck it back to "needs review". I dn't feel able to review it, but after installing the pari package, this installs cleanly. 

**I've only tested on OpenSolaris x64 as a 32-bit binary** - so I have not tested on Solaris SPARC (e.g. t2)

Dave



---

archive/issue_comments_092606.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. \n\n\nWell, there has been a .p7 on this ticket for a while, even if it was never actually distributed by Sage.  In my opinion it makes sense to call this .p8 then.",
    "created_at": "2010-08-15T06:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92606",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:11 drkirkby]:
> If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. 


Well, there has been a .p7 on this ticket for a while, even if it was never actually distributed by Sage.  In my opinion it makes sense to call this .p8 then.



---

archive/issue_comments_092607.json:
```json
{
    "body": "Replying to [comment:14 jdemeyer]:\n> Replying to [comment:11 drkirkby]:\n> > If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. \n\n> \n> Well, there has been a .p7 on this ticket for a while, even if it was never actually distributed by Sage.  In my opinion it makes sense to call this .p8 then.\n\n\nI think Dave is right strictly speaking, but having .p8 means an easier time for people working on the pari issue to upgrade it. And now that I have updated my own package (after I had created a .p7 less than 12 hours beforehand) for Gentoo I'd like it to stay at that number - if possible.",
    "created_at": "2010-08-15T07:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92607",
    "user": "https://github.com/kiwifb"
}
```

Replying to [comment:14 jdemeyer]:
> Replying to [comment:11 drkirkby]:
> > If I'm not mistaken, it should be .p7, .p8, as the one version in sage-4.5.3.alpha0 is a .p6. 

> 
> Well, there has been a .p7 on this ticket for a while, even if it was never actually distributed by Sage.  In my opinion it makes sense to call this .p8 then.


I think Dave is right strictly speaking, but having .p8 means an easier time for people working on the pari issue to upgrade it. And now that I have updated my own package (after I had created a .p7 less than 12 hours beforehand) for Gentoo I'd like it to stay at that number - if possible.



---

archive/issue_comments_092608.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-08-19T11:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92608",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_092609.json:
```json
{
    "body": "Attachment [genus2reduction-spkg.patch](tarball://root/attachments/some-uuid/ticket9591/genus2reduction-spkg.patch) by @jdemeyer created at 2010-08-21 12:44:14\n\nComplete spkg patch (for reference)",
    "created_at": "2010-08-21T12:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92609",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [genus2reduction-spkg.patch](tarball://root/attachments/some-uuid/ticket9591/genus2reduction-spkg.patch) by @jdemeyer created at 2010-08-21 12:44:14

Complete spkg patch (for reference)



---

archive/issue_comments_092610.json:
```json
{
    "body": "I can give a positive review to the \"EOF\" part of [attachment:ticket:9738:9738_genus2reduction_init_opts.patch Jeroen's patch] from #9738.  With the prerequisites given at [NewPARI](http://wiki.sagemath.org/NewPARI), I get no dumped cores on bsd, redhawk, sage, and t2.math.\n\nUnfortunately, I'm not qualified to review the rest of the patch, since I'm not familiar with the mathematics or PARI's API.",
    "created_at": "2010-08-31T00:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92610",
    "user": "https://github.com/qed777"
}
```

I can give a positive review to the "EOF" part of [attachment:ticket:9738:9738_genus2reduction_init_opts.patch Jeroen's patch] from #9738.  With the prerequisites given at [NewPARI](http://wiki.sagemath.org/NewPARI), I get no dumped cores on bsd, redhawk, sage, and t2.math.

Unfortunately, I'm not qualified to review the rest of the patch, since I'm not familiar with the mathematics or PARI's API.



---

archive/issue_comments_092611.json:
```json
{
    "body": "Replying to [comment:18 mpatel]:\n> I can give a positive review to the \"EOF\" part of [attachment:ticket:9738:9738_genus2reduction_init_opts.patch Jeroen's patch] from #9738.  With the prerequisites given at [NewPARI](http://wiki.sagemath.org/NewPARI), I get no dumped cores on bsd, redhawk, sage, and t2.math.\n\n\nSpecifically, I get no dumped cores from running `genus2reduction` and testing `sage/interfaces/genus2reduction.py`.  There are still unrelated cores stemming probably from the doctesting system (cf. [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/ba4e7b77e4de1b10?#ba4e7b77e4de1b10), #9739).",
    "created_at": "2010-08-31T00:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92611",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:18 mpatel]:
> I can give a positive review to the "EOF" part of [attachment:ticket:9738:9738_genus2reduction_init_opts.patch Jeroen's patch] from #9738.  With the prerequisites given at [NewPARI](http://wiki.sagemath.org/NewPARI), I get no dumped cores on bsd, redhawk, sage, and t2.math.


Specifically, I get no dumped cores from running `genus2reduction` and testing `sage/interfaces/genus2reduction.py`.  There are still unrelated cores stemming probably from the doctesting system (cf. [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/ba4e7b77e4de1b10?#ba4e7b77e4de1b10), #9739).



---

archive/issue_comments_092612.json:
```json
{
    "body": "While I wouldn't claim to be a pari specialist, I had a look at updating genus2reduction myself. I didn't fell confident about giving a positive review because I don't understand the \"EOF\" part but I am willing to give a positive review to the rest.",
    "created_at": "2010-08-31T02:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92612",
    "user": "https://github.com/kiwifb"
}
```

While I wouldn't claim to be a pari specialist, I had a look at updating genus2reduction myself. I didn't fell confident about giving a positive review because I don't understand the "EOF" part but I am willing to give a positive review to the rest.



---

archive/issue_comments_092613.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-02T10:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92613",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092614.json:
```json
{
    "body": "The `dist/` directory should be removed (see #5903).\n\nThen I can revert it to \"positive review\"... :)",
    "created_at": "2010-09-03T23:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92614",
    "user": "https://github.com/nexttime"
}
```

The `dist/` directory should be removed (see #5903).

Then I can revert it to "positive review"... :)



---

archive/issue_comments_092615.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-03T23:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92615",
    "user": "https://github.com/nexttime"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_092616.json:
```json
{
    "body": "Attachment [trac_9591-g2red_remove_dist.patch](tarball://root/attachments/some-uuid/ticket9591/trac_9591-g2red_remove_dist.patch) by @qed777 created at 2010-09-04 07:22:44\n\nRemove `dist/`.  spkg patch.  Apply on top of \"complete\" patch.",
    "created_at": "2010-09-04T07:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92616",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9591-g2red_remove_dist.patch](tarball://root/attachments/some-uuid/ticket9591/trac_9591-g2red_remove_dist.patch) by @qed777 created at 2010-09-04 07:22:44

Remove `dist/`.  spkg patch.  Apply on top of "complete" patch.



---

archive/issue_comments_092617.json:
```json
{
    "body": "I've a put an updated package at\n\n http://sage.math.washington.edu/home/mpatel/trac/9591/genus2reduction-0.3.p8.spkg",
    "created_at": "2010-09-04T07:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92617",
    "user": "https://github.com/qed777"
}
```

I've a put an updated package at

 http://sage.math.washington.edu/home/mpatel/trac/9591/genus2reduction-0.3.p8.spkg



---

archive/issue_comments_092618.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-04T07:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92618",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092619.json:
```json
{
    "body": "Ok, I've really looked at the new spkg. ;-)\n\nThe changelog in `SPKG.txt` cites #9738 for the removal, but never mind. (The commit message is correct.)\n\nReverting to **\"positive review\"**.\n\nMitesh, could you update the link on the NewPARI wiki page?",
    "created_at": "2010-09-04T09:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92619",
    "user": "https://github.com/nexttime"
}
```

Ok, I've really looked at the new spkg. ;-)

The changelog in `SPKG.txt` cites #9738 for the removal, but never mind. (The commit message is correct.)

Reverting to **"positive review"**.

Mitesh, could you update the link on the NewPARI wiki page?



---

archive/issue_comments_092620.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-04T09:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92620",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092621.json:
```json
{
    "body": "Replying to [comment:24 leif]:\n> Mitesh, could you update the link on the NewPARI wiki page?\n\n\nDone.",
    "created_at": "2010-09-04T09:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92621",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:24 leif]:
> Mitesh, could you update the link on the NewPARI wiki page?


Done.



---

archive/issue_comments_092622.json:
```json
{
    "body": "Attachment [genus2reduction-spkg.2.patch](tarball://root/attachments/some-uuid/ticket9591/genus2reduction-spkg.2.patch) by @jdemeyer created at 2010-09-05 13:36:53\n\nNew complete patch including trac_9591-g2red_remove_dist.patch",
    "created_at": "2010-09-05T13:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92622",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [genus2reduction-spkg.2.patch](tarball://root/attachments/some-uuid/ticket9591/genus2reduction-spkg.2.patch) by @jdemeyer created at 2010-09-05 13:36:53

New complete patch including trac_9591-g2red_remove_dist.patch



---

archive/issue_events_023890.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-10T10:39:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9591#event-23890"
}
```



---

archive/issue_comments_092623.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-10T10:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9591",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9591#issuecomment-92623",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
