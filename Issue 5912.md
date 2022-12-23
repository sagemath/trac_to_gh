# Issue 5912: %fortran mode is broken in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/5912

Original creator: was

Original creation time: 2009-04-27 18:10:34

Assignee: boothby




---

Comment by was created at 2009-04-27 18:13:10

Here's how to test the attached patch:

```
Untitled
system:sage

{{{id=69|
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
///

None
}}}

{{{id=70|
import numpy
n = numpy.array(range(10),dtype=float)
fib(n)
///
}}}

{{{id=71|
n
///

array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])
}}}


---

Attachment


---

Comment by cswiercz created at 2009-04-27 20:51:59

Works well!

I noticed that it only works with Fortran 77 code. Not a bug, really, but Fortran 95 / 2003 seem to be much more popular in the applied sciences world. In the future it would be


---

Comment by mabshoff created at 2009-04-30 07:02:44

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 07:02:44

Resolution: fixed
