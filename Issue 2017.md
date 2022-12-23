# Issue 2017: crap -- singular includes surfex as a precompiled binary.  Remove it.

Issue created by migration from https://trac.sagemath.org/ticket/2017

Original creator: was

Original creation time: 2008-01-31 23:28:50

Assignee: mabshoff

Remove it, and make very sure it stays removed in future versions of the singular spkg, e.g., by modifying spkg-install so that if it sees surfex class files, it will bomb out with an error. 


```
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$5.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SolitaryPoint$1.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/jv4surfex.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$9.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$11.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial$Term.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial$Factor.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Defns.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$2.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$removeListener.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePic.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$6.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/pcalc.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ConfigFrame$3.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Equation.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/surfex$1.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/LampAdmin$2.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePicDialog.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$10.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SolitaryPointsAdmin.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SwingWorker.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/OneParameter.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ConfigFrame$5.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovie.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ProgressFrame.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/surfex$3.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePicDialog$3.class

```



---

Comment by was created at 2008-03-12 05:00:17

Changing priority from major to blocker.


---

Comment by was created at 2008-03-12 05:00:17

This must be FIXED.


---

Comment by mabshoff created at 2008-07-19 13:17:58

Resolution: fixed


---

Comment by mabshoff created at 2008-07-19 13:17:58

William did remove the offending Java files in Sage 3.0.5.

Cheers,

Michael
