# Issue 5912: %fortran mode is broken in the notebook

archive/issues_005912.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5912\n\n",
    "created_at": "2009-04-27T18:10:34Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "%fortran mode is broken in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5912",
    "user": "was"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/5912





---

archive/issue_comments_046731.json:
```json
{
    "body": "Here's how to test the attached patch:\n\n```\nUntitled\nsystem:sage\n\n{{{id=69|\n%fortran\n\nC FILE: FIB1.F\n      SUBROUTINE FIB(A,N)\nC\nC     CALCULATE FIRST N FIBONACCI NUMBERS\nC\n      INTEGER N\n      REAL*8 A(N)\n      DO I=1,N\n         IF (I.EQ.1) THEN\n            A(I) = 0.0D0\n         ELSEIF (I.EQ.2) THEN\n            A(I) = 1.0D0\n         ELSE \n            A(I) = A(I-1) + A(I-2)\n         ENDIF\n      ENDDO\n      END\nC END FILE FIB1.F\n///\n\nNone\n}}}\n\n{{{id=70|\nimport numpy\nn = numpy.array(range(10),dtype=float)\nfib(n)\n///\n}}}\n\n{{{id=71|\nn\n///\n\narray([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])\n}}}",
    "created_at": "2009-04-27T18:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5912#issuecomment-46731",
    "user": "was"
}
```

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

archive/issue_comments_046732.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-27T18:14:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5912#issuecomment-46732",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_046733.json:
```json
{
    "body": "Works well!\n\nI noticed that it only works with Fortran 77 code. Not a bug, really, but Fortran 95 / 2003 seem to be much more popular in the applied sciences world. In the future it would be",
    "created_at": "2009-04-27T20:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5912#issuecomment-46733",
    "user": "cswiercz"
}
```

Works well!

I noticed that it only works with Fortran 77 code. Not a bug, really, but Fortran 95 / 2003 seem to be much more popular in the applied sciences world. In the future it would be



---

archive/issue_comments_046734.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T07:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5912#issuecomment-46734",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_046735.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T07:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5912#issuecomment-46735",
    "user": "mabshoff"
}
```

Resolution: fixed
