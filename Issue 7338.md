# Issue 7338: Singular fails to build on cygwin

archive/issues_007338.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein\n\nIt fails with \n\n\n```\n  Info: resolving vtable for std::basic_ofstream<char, std::char_traits<char> > by linking to __imp___ZTVSt14basic_ofstreamIcSt11char_traitsIcEE (auto-import/usr/lib/gcc/i686-pc-cygwin/4.3.2/../../../../i686-pc-cygwin/bin/ld: warning: auto-importing has been activated without --enable-auto-import specified on the command line.\n  This should work unless it involves constant data structures referencing symbols from auto-imported DLLs.Warning: .drectve `-defaultlib:uuid.lib ' unrecognized\n  Warning: .drectve `-defaultlib:uuid.lib ' unrecognized\n  Cannot export ??_C@_00A@?$AA@: symbol not found\n  Cannot export ?pHtmlHelpA@@3P6GPAUHWND__@@PAU1@PBDIK@ZA: symbol not found\n  Cannot export ?pHtmlHelpW@@3P6GPAUHWND__@@PAU1@PBGIK@ZA: symbol not found\n  collect2: ld returned 1 exit status\n  )\n  make[3]: *** [libsingular] Error 1\n  make[3]: Leaving directory `/home/mhansen/sage-4.2/spkg/build/singular-3-1-0-4-20090818.p1/src/Singular'\n  make[2]: *** [libsingular] Error 2\n  make[2]: Leaving directory `/home/mhansen/sage-4.2/spkg/build/singular-3-1-0-4-20090818.p1/src'\n  Unable to build Singular.\n```\n\n\nOne fix is to comment out the HtmlHelpA line from sing_win.cc\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7338\n\n",
    "created_at": "2009-10-28T19:39:08Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Singular fails to build on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7338",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

CC:  @williamstein

It fails with 


```
  Info: resolving vtable for std::basic_ofstream<char, std::char_traits<char> > by linking to __imp___ZTVSt14basic_ofstreamIcSt11char_traitsIcEE (auto-import/usr/lib/gcc/i686-pc-cygwin/4.3.2/../../../../i686-pc-cygwin/bin/ld: warning: auto-importing has been activated without --enable-auto-import specified on the command line.
  This should work unless it involves constant data structures referencing symbols from auto-imported DLLs.Warning: .drectve `-defaultlib:uuid.lib ' unrecognized
  Warning: .drectve `-defaultlib:uuid.lib ' unrecognized
  Cannot export ??_C@_00A@?$AA@: symbol not found
  Cannot export ?pHtmlHelpA@@3P6GPAUHWND__@@PAU1@PBDIK@ZA: symbol not found
  Cannot export ?pHtmlHelpW@@3P6GPAUHWND__@@PAU1@PBGIK@ZA: symbol not found
  collect2: ld returned 1 exit status
  )
  make[3]: *** [libsingular] Error 1
  make[3]: Leaving directory `/home/mhansen/sage-4.2/spkg/build/singular-3-1-0-4-20090818.p1/src/Singular'
  make[2]: *** [libsingular] Error 2
  make[2]: Leaving directory `/home/mhansen/sage-4.2/spkg/build/singular-3-1-0-4-20090818.p1/src'
  Unable to build Singular.
```


One fix is to comment out the HtmlHelpA line from sing_win.cc


Issue created by migration from https://trac.sagemath.org/ticket/7338





---

archive/issue_comments_061292.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T18:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61292",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061293.json:
```json
{
    "body": "I've posted an spkg here:\n    http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg",
    "created_at": "2010-02-14T18:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61293",
    "user": "https://github.com/williamstein"
}
```

I've posted an spkg here:
    http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg



---

archive/issue_comments_061294.json:
```json
{
    "body": "With this new spkg the install still fails with this (a new problem):\n\n```\n../mkinstalldirs /home/wstein/build/sage-4.3.3.alpha0/local/bin\n/usr/bin/install -c  -s solve_IP /home/wstein/build/sage-4.3.3.alpha0/local/bin\n/usr/bin/install: cannot create regular file `/home/wstein/build/sage-4.3.3.alpha0/local/bin/solve_IP': File exists\nmake[3]: *** [install] Error 1\nmake[3]: Leaving directory `/home/wstein/build/sage-4.3.3.alpha0/spkg/build/singular-3-1-0-4-20100214/src/IntegerProgramming'\n```\n",
    "created_at": "2010-02-14T19:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61294",
    "user": "https://github.com/williamstein"
}
```

With this new spkg the install still fails with this (a new problem):

```
../mkinstalldirs /home/wstein/build/sage-4.3.3.alpha0/local/bin
/usr/bin/install -c  -s solve_IP /home/wstein/build/sage-4.3.3.alpha0/local/bin
/usr/bin/install: cannot create regular file `/home/wstein/build/sage-4.3.3.alpha0/local/bin/solve_IP': File exists
make[3]: *** [install] Error 1
make[3]: Leaving directory `/home/wstein/build/sage-4.3.3.alpha0/spkg/build/singular-3-1-0-4-20100214/src/IntegerProgramming'
```




---

archive/issue_comments_061295.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-14T19:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61295",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061296.json:
```json
{
    "body": "Making this change to src/IntegerProgramming/Makefile gets past this particular problem (the change is to add .exe after $(MAIN1) etc. below:\n\n\n```\ninstall: $(MAIN1) $(MAIN2) $(MAIN3) $(MAIN4) $(LLL)\n        ${MKINSTALLDIRS} ${bindir}\n        ${INSTALL_PROGRAM} $(MAIN1).exe ${bindir}\n        ${INSTALL_PROGRAM} $(MAIN2).exe ${bindir}\n        ${INSTALL_PROGRAM} $(MAIN3).exe ${bindir}\n        ${INSTALL_PROGRAM} $(MAIN4).exe ${bindir}\n        ${INSTALL_PROGRAM} $(LLL).exe ${bindir}\n```\n",
    "created_at": "2010-02-14T20:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61296",
    "user": "https://github.com/williamstein"
}
```

Making this change to src/IntegerProgramming/Makefile gets past this particular problem (the change is to add .exe after $(MAIN1) etc. below:


```
install: $(MAIN1) $(MAIN2) $(MAIN3) $(MAIN4) $(LLL)
        ${MKINSTALLDIRS} ${bindir}
        ${INSTALL_PROGRAM} $(MAIN1).exe ${bindir}
        ${INSTALL_PROGRAM} $(MAIN2).exe ${bindir}
        ${INSTALL_PROGRAM} $(MAIN3).exe ${bindir}
        ${INSTALL_PROGRAM} $(MAIN4).exe ${bindir}
        ${INSTALL_PROGRAM} $(LLL).exe ${bindir}
```




---

archive/issue_comments_061297.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-14T21:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61297",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061298.json:
```json
{
    "body": "OK, with the above fix rolled into the new spkg at http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg this now builds fine on Cygwin, and \n\n```\nwstein@winxp ~/build/sage-4.3.3.alpha0\n$ ./sage -singular\n// ** Could not get Singular.\n// ** Either set environment variable SINGULAR_EXECUTABLE to Singular,\n// ** or make sure that Singular is at /home/wstein/build/sage-4.3.3.alpha0/local/ix86-Win/Singular\n// ** Could not get BinDir.\n// ** Either set environment variable SINGULAR_BIN_DIR to BinDir,\n// ** or make sure that BinDir is at /home/wstein/build/sage-4.3.3.alpha0/local/ix86-Win\n                     SINGULAR                             /  Development\n A Computer Algebra System for Polynomial Computations   /   version 3-1-0\n                                                       0<\n     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \\   Mar 2009\nFB Mathematik der Universitaet, D-67653 Kaiserslautern    \\\n> 2+3;\n5\n```\n\n\nThe warning at the top is probably because of the distinction between Singular and Singular.exe, perhaps.  Anyway, this is now ready for review.",
    "created_at": "2010-02-14T21:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61298",
    "user": "https://github.com/williamstein"
}
```

OK, with the above fix rolled into the new spkg at http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg this now builds fine on Cygwin, and 

```
wstein@winxp ~/build/sage-4.3.3.alpha0
$ ./sage -singular
// ** Could not get Singular.
// ** Either set environment variable SINGULAR_EXECUTABLE to Singular,
// ** or make sure that Singular is at /home/wstein/build/sage-4.3.3.alpha0/local/ix86-Win/Singular
// ** Could not get BinDir.
// ** Either set environment variable SINGULAR_BIN_DIR to BinDir,
// ** or make sure that BinDir is at /home/wstein/build/sage-4.3.3.alpha0/local/ix86-Win
                     SINGULAR                             /  Development
 A Computer Algebra System for Polynomial Computations   /   version 3-1-0
                                                       0<
     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \   Mar 2009
FB Mathematik der Universitaet, D-67653 Kaiserslautern    \
> 2+3;
5
```


The warning at the top is probably because of the distinction between Singular and Singular.exe, perhaps.  Anyway, this is now ready for review.



---

archive/issue_comments_061299.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-17T04:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61299",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061300.json:
```json
{
    "body": "Looks good to me for now.  We can get rid of that error message in the future.",
    "created_at": "2010-02-17T04:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61300",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me for now.  We can get rid of that error message in the future.



---

archive/issue_comments_061301.json:
```json
{
    "body": "Merged [singular-3-1-0-4-20100214.spkg](http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg) in the standard spkg repository.",
    "created_at": "2010-02-17T20:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61301",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [singular-3-1-0-4-20100214.spkg](http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg) in the standard spkg repository.



---

archive/issue_comments_061302.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T20:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61302",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007562.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-02-17T20:45:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7338#event-7562"
}
```



---

archive/issue_comments_061303.json:
```json
{
    "body": "For the record, the error message can be removed by \n\n\n```\nexport SINGULAR_EXECUTABLE=$SAGE_LOCAL/bin/Singular\n```\n",
    "created_at": "2010-02-17T21:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7338",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7338#issuecomment-61303",
    "user": "https://github.com/mwhansen"
}
```

For the record, the error message can be removed by 


```
export SINGULAR_EXECUTABLE=$SAGE_LOCAL/bin/Singular
```

