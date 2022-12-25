# Issue 7465: %fortran in the notebook (and fortran.eval on command line) is completely broken on OS X

archive/issues_007465.json:
```json
{
    "body": "Assignee: @williamstein\n\nTry this in a notebook cell on OS X:\n\n```\n%fortran\nC FILE: FIB1.F\n      SUBROUTINE FIB(A,N)\nC\nC     CALCULATE FIRST N FIBONACCI NUMBERS\nC\n      INTEGER N\n      REAL*8 A(N)\n      DO I=1,N\n         IF (I.EQ.1) THEN\n            A(I) = 0.0D0\n         ELSEIF (I.EQ.2) THEN\n            A(I) = 1.0D0\n         ELSE \n            A(I) = A(I-1) + A(I-2)\n         ENDIF\n      ENDDO\n      END\nC END FILE FIB1.F\n```\n\nAny use of f2py, e.g. following the examples at http://www.sagemath.org/doc/numerical_sage/f2py.html lead to a crash:\n\n```\nerror: Command \"sage_fortran -Wall -shared /var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-\n/tmpisjCMl/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-\n/tmpisjCMl/src.macosx-10.6-i386-2.6/fortran_module_0module.o \n/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-\n/tmpisjCMl/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-\n/tmpisjCMl/src.macosx-10.6-i386-2.6/fortranobject.o \n/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-\n/tmpisjCMl/Users/felix/.sage/temp/<my domain name>/52076/tmp_0.o -L\"Using built-in specs.\n/Applications/sage-4.3.1.rc1/local/bin/../lib/gcc/i686-apple-darwin8/4.2.3/x86_64\" \n-lgfortran -o ./fortran_module_0.so\" failed with exit status 1\n\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'\ni686-apple-darwin8-gfortran-4.2: no input files\ni686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'\ni686-apple-darwin8-gfortran-4.2: no input files\nUsing built-in specs.\nTarget: i686-apple-darwin8\nConfigured with: /Builds/unix/gcc/gcc-4.2/configure --prefix=/usr/local \n--mandir=/share/man --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ \n--build=i686-apple-darwin8 --host=i686-apple-darwin8 --target=i686-apple-\ndarwin8 --enable-languages=fortran\nThread model: posix\ngcc version 4.2.3\n\n<SNIP>\n```\n\nThis is using 4.3.1rc1 on 10.6, 64-bit.\n\nThe problem is that local/lib/python2.6/site-packages/numpy/distutils/fcompiler/gnu.py adds a \"-shared\" flag when linking, even though OS X doesn't support it.\n\nMac OS X (Darwin) compilers do not support the \"-shared\" option. The class Sage_FCompiler_1 currently calls compilers on all platforms using the \"-shared\" option. So whenever this class is used on Mac, it fails. On my computer, this led to f2py failing. This is a five line patch (plus documentation) that changes the compiler options on Mac to be in line with those already used in Sage_FCompiler, while leaving the compiler options on other platforms such as Solaris unchanged. If you'd like to check it on Solaris, then go ahead, but the patch was intentionally written to avoid changing behaviour on platforms other than OS X.\n\nThis breaks \"on some mac systems\" - f2py is broken on my 64-bit sage, but seems to be working on 32-bit mac systems without this patch. My guess is that 32-bit macs use Sage_FCompiler rather than Sage_FCompiler_1. Anyone who is familiar with the numpy spkg, please confirm or correct me!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7465\n\n",
    "closed_at": "2010-11-05T06:58:00Z",
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

Any use of f2py, e.g. following the examples at http://www.sagemath.org/doc/numerical_sage/f2py.html lead to a crash:

```
error: Command "sage_fortran -Wall -shared /var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/src.macosx-10.6-i386-2.6/fortran_module_0module.o 
/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/src.macosx-10.6-i386-2.6/fortranobject.o 
/var/folders/LQ/LQFRAKFTGCCurtDiHcxv1k++-5I/-Tmp-
/tmpisjCMl/Users/felix/.sage/temp/<my domain name>/52076/tmp_0.o -L"Using built-in specs.
/Applications/sage-4.3.1.rc1/local/bin/../lib/gcc/i686-apple-darwin8/4.2.3/x86_64" 
-lgfortran -o ./fortran_module_0.so" failed with exit status 1

i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
i686-apple-darwin8-gfortran-4.2: unrecognized option '-shared'
i686-apple-darwin8-gfortran-4.2: no input files
Using built-in specs.
Target: i686-apple-darwin8
Configured with: /Builds/unix/gcc/gcc-4.2/configure --prefix=/usr/local 
--mandir=/share/man --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ 
--build=i686-apple-darwin8 --host=i686-apple-darwin8 --target=i686-apple-
darwin8 --enable-languages=fortran
Thread model: posix
gcc version 4.2.3

<SNIP>
```

This is using 4.3.1rc1 on 10.6, 64-bit.

The problem is that local/lib/python2.6/site-packages/numpy/distutils/fcompiler/gnu.py adds a "-shared" flag when linking, even though OS X doesn't support it.

Mac OS X (Darwin) compilers do not support the "-shared" option. The class Sage_FCompiler_1 currently calls compilers on all platforms using the "-shared" option. So whenever this class is used on Mac, it fails. On my computer, this led to f2py failing. This is a five line patch (plus documentation) that changes the compiler options on Mac to be in line with those already used in Sage_FCompiler, while leaving the compiler options on other platforms such as Solaris unchanged. If you'd like to check it on Solaris, then go ahead, but the patch was intentionally written to avoid changing behaviour on platforms other than OS X.

This breaks "on some mac systems" - f2py is broken on my 64-bit sage, but seems to be working on 32-bit mac systems without this patch. My guess is that 32-bit macs use Sage_FCompiler rather than Sage_FCompiler_1. Anyone who is familiar with the numpy spkg, please confirm or correct me!

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



---

archive/issue_events_017695.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-11-05T06:58:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7465",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7465#event-17695"
}
```



---

archive/issue_events_017696.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-11-05T06:58:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7465",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7465#event-17696"
}
```
