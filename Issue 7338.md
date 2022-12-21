# Issue 7338: Singular fails to build on cygwin

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-10-28 19:39:08

Assignee: tbd

CC:  was

It fails with 


```
  Info: resolving vtable for std::basic_ofstream<char, std::char_traits<char> > by linking to __imp___ZTVSt14basic_ofstreamIcSt11char_traitsIcEE (auto-import/usr/lib/gcc/i686-pc-cygwin/4.3.2/../../../../i686-pc-cygwin/bin/ld: warning: auto-importing has been activated without --enable-auto-import specified on the command line.
  This should work unless it involves constant data structures referencing symbols from auto-imported DLLs.Warning: .drectve `-defaultlib:uuid.lib ' unrecognized
  Warning: .drectve `-defaultlib:uuid.lib ' unrecognized
  Cannot export ??_C`@`_00A`@`?$AA`@`: symbol not found
  Cannot export ?pHtmlHelpA`@``@`3P6GPAUHWND__`@``@`PAU1`@`PBDIK`@`ZA: symbol not found
  Cannot export ?pHtmlHelpW`@``@`3P6GPAUHWND__`@``@`PAU1`@`PBGIK`@`ZA: symbol not found
  collect2: ld returned 1 exit status
  )
  make[3]: *** [libsingular] Error 1
  make[3]: Leaving directory `/home/mhansen/sage-4.2/spkg/build/singular-3-1-0-4-20090818.p1/src/Singular'
  make[2]: *** [libsingular] Error 2
  make[2]: Leaving directory `/home/mhansen/sage-4.2/spkg/build/singular-3-1-0-4-20090818.p1/src'
  Unable to build Singular.
```


One fix is to comment out the HtmlHelpA line from sing_win.cc



---

Comment by was created at 2010-02-14 18:29:55

Changing status from new to needs_review.


---

Comment by was created at 2010-02-14 18:29:55

I've posted an spkg here:
    http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg


---

Comment by was created at 2010-02-14 19:34:56

With this new spkg the install still fails with this (a new problem):

```
../mkinstalldirs /home/wstein/build/sage-4.3.3.alpha0/local/bin
/usr/bin/install -c  -s solve_IP /home/wstein/build/sage-4.3.3.alpha0/local/bin
/usr/bin/install: cannot create regular file `/home/wstein/build/sage-4.3.3.alpha0/local/bin/solve_IP': File exists
make[3]: *** [install] Error 1
make[3]: Leaving directory `/home/wstein/build/sage-4.3.3.alpha0/spkg/build/singular-3-1-0-4-20100214/src/IntegerProgramming'
```



---

Comment by was created at 2010-02-14 19:34:56

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-02-14 20:22:54

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

Comment by was created at 2010-02-14 21:32:09

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-02-14 21:32:09

OK, with the above fix rolled into the new spkg at http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg this now builds fine on Cygwin, and 

```
wstein`@`winxp ~/build/sage-4.3.3.alpha0
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

Comment by mhansen created at 2010-02-17 04:36:18

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-02-17 04:36:18

Looks good to me for now.  We can get rid of that error message in the future.


---

Comment by mvngu created at 2010-02-17 20:45:20

Merged [singular-3-1-0-4-20100214.spkg](http://sage.math.washington.edu/home/wstein/ports/cygwin/singular-3-1-0-4-20100214.spkg) in the standard spkg repository.


---

Comment by mvngu created at 2010-02-17 20:45:20

Resolution: fixed


---

Comment by mhansen created at 2010-02-17 21:10:15

For the record, the error message can be removed by 


```
export SINGULAR_EXECUTABLE=$SAGE_LOCAL/bin/Singular
```

