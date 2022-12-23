# Issue 7465: %fortran in the notebook (and fortran.eval on command line) is completely broken on OS X

Issue created by migration from https://trac.sagemath.org/ticket/7465

Original creator: was

Original creation time: 2009-11-14 22:13:25

Assignee: was

Try this in a notebook cell on OS X:


```
%fortran          	
C FILE: FIB1.F
      SUBROUTINE FIB(A,N)
C
C     CALCULATE FIRST N FIBONACCI NUMBERS
C
      INTEGER N
      REAL*8 A(N)
      DO I=1,N
         IF (I.EQ.1) THEN
            A(I) = 0.0D0
         ELSEIF (I.EQ.2) THEN
            A(I) = 1.0D0
         ELSE 
            A(I) = A(I-1) + A(I-2)
         ENDIF
      ENDDO
      END
C END FILE FIB1.F
```


Boom!!  This despite us shipping a Fortran compiler. 

The problem is really that the doctests for `fortran.eval` were marked (by me, doh) as optional, and we don't test optional doctests frequently.


---

Comment by flawrence created at 2010-11-03 05:56:06

#8010 is a duplicate of this


---

Attachment


---

Comment by flawrence created at 2010-11-05 06:48:21

No such problem in 4.6.1alpha0 on a computer that previously had this problem.  No further patch required.  This ticket can be closed.


---

Comment by mvngu created at 2010-11-05 06:58:00

Resolution: worksforme
