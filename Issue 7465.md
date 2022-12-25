# Issue 7465: %fortran in the notebook (and fortran.eval on command line) is completely broken on OS X

archive/issues_007465.json:
```json
{
    "body": "Assignee: @williamstein\n\nTry this in a notebook cell on OS X:\n\n\n```\n%fortran          \t\nC FILE: FIB1.F\n      SUBROUTINE FIB(A,N)\nC\nC     CALCULATE FIRST N FIBONACCI NUMBERS\nC\n      INTEGER N\n      REAL*8 A(N)\n      DO I=1,N\n         IF (I.EQ.1) THEN\n            A(I) = 0.0D0\n         ELSEIF (I.EQ.2) THEN\n            A(I) = 1.0D0\n         ELSE \n            A(I) = A(I-1) + A(I-2)\n         ENDIF\n      ENDDO\n      END\nC END FILE FIB1.F\n```\n\n\nBoom!!  This despite us shipping a Fortran compiler. \n\nThe problem is really that the doctests for `fortran.eval` were marked (by me, doh) as optional, and we don't test optional doctests frequently.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7465\n\n",
    "created_at": "2009-11-14T22:13:25Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "%fortran in the notebook (and fortran.eval on command line) is completely broken on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7465",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

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

Issue created by migration from https://trac.sagemath.org/ticket/7465





---

archive/issue_comments_062758.json:
```json
{
    "body": "#8010 is a duplicate of this",
    "created_at": "2010-11-03T05:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7465#issuecomment-62758",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

#8010 is a duplicate of this



---

archive/issue_comments_062759.json:
```json
{
    "body": "Attachment [trac-8010_numpy.patch](tarball://root/attachments/some-uuid/ticket7465/trac-8010_numpy.patch) by mvngu created at 2010-11-04 11:55:08",
    "created_at": "2010-11-04T11:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7465#issuecomment-62759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac-8010_numpy.patch](tarball://root/attachments/some-uuid/ticket7465/trac-8010_numpy.patch) by mvngu created at 2010-11-04 11:55:08



---

archive/issue_comments_062760.json:
```json
{
    "body": "No such problem in 4.6.1alpha0 on a computer that previously had this problem.  No further patch required.  This ticket can be closed.",
    "created_at": "2010-11-05T06:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7465#issuecomment-62760",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

No such problem in 4.6.1alpha0 on a computer that previously had this problem.  No further patch required.  This ticket can be closed.



---

archive/issue_comments_062761.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-11-05T06:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7465#issuecomment-62761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: worksforme
