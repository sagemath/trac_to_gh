# Issue 8527: libcocoa-0.9930 indicates its sucessfully installed when it has not.

archive/issues_008527.json:
```json
{
    "body": "Assignee: tbd\n\nIn trying to rid libcocoa-0.9930 of the GNUims that \nprevents this installing on on Solaris (see #8521), I found another problem with this package. It appears that the error codes are not properly checked, so even if there are build failures, the package indicates it has been successfully installed. See below:\n\n\n```\nCompiling RegisterServerOps.o\nCompiling TmpFrobby.o\nCompiling RegisterServerOpsFrobby.o\nCompiling directory CoCoALib/src/AlgebraicCore/TmpFactorDir/\nmake[4]: Entering directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore/TmpFactorDir'\nMakefile:4: ../../../../configuration/autoconf.mk: No such file or directory\nmake[4]: *** No rule to make target `../../../../configuration/autoconf.mk'.  Stop.\nmake[4]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore/TmpFactorDir'\n***** Compilation of CoCoALib/src/AlgebraicCore/TmpFactorDir/ FAILED *****\nmake[3]: *** [../../lib/libcocoa.a] Error 1\nmake[3]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore'\n*****[[Compilation[failed[in[CoCoA[library[source[subdirectory[AlgebraicCore/[[*****\n*****  Compilation failed in CoCoA library source subdirectory AlgebraicCore/  *****\n*****[[Compilation[failed[in[CoCoA[library[source[subdirectory[AlgebraicCore/[[*****\nmake[2]: *** [library] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src'\nmake[1]: *** [library] Error 2\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src'\nmake: *** [default] Error 2\nDoing the build in the following directory:\n/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0\n./configure  --with-libgmp=$SAGE_LOCAL/lib/libgmp.so\nNow running Make\nmake\nThere are known test failures that should be listed above.\nThey are literally 'not yet implemented' errors from the\nCoCOA library.   I.e., CoCOA releases purposely don't pass\ntheir own test suite at present.\nlibcocoa.a built!\n\n----------------------------------------------------------------------\n\nTo play with libcocoa, type 'sage -sh', then cd to the directory\n\n   /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/examples\n\nand try making and running some of the examples.\nWhen you're done, it is completely safe to delete directory:\n\n   /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0\n\n----------------------------------------------------------------------\n\nreal    4m38.333s\nuser    4m13.925s\nsys     0m21.973s\nSuccessfully installed libcocoa-0.9930.p0\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8527\n\n",
    "created_at": "2010-03-13T20:00:31Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "libcocoa-0.9930 indicates its sucessfully installed when it has not.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8527",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

In trying to rid libcocoa-0.9930 of the GNUims that 
prevents this installing on on Solaris (see #8521), I found another problem with this package. It appears that the error codes are not properly checked, so even if there are build failures, the package indicates it has been successfully installed. See below:


```
Compiling RegisterServerOps.o
Compiling TmpFrobby.o
Compiling RegisterServerOpsFrobby.o
Compiling directory CoCoALib/src/AlgebraicCore/TmpFactorDir/
make[4]: Entering directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore/TmpFactorDir'
Makefile:4: ../../../../configuration/autoconf.mk: No such file or directory
make[4]: *** No rule to make target `../../../../configuration/autoconf.mk'.  Stop.
make[4]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore/TmpFactorDir'
***** Compilation of CoCoALib/src/AlgebraicCore/TmpFactorDir/ FAILED *****
make[3]: *** [../../lib/libcocoa.a] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src/AlgebraicCore'
*****[[Compilation[failed[in[CoCoA[library[source[subdirectory[AlgebraicCore/[[*****
*****  Compilation failed in CoCoA library source subdirectory AlgebraicCore/  *****
*****[[Compilation[failed[in[CoCoA[library[source[subdirectory[AlgebraicCore/[[*****
make[2]: *** [library] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/src'
make[1]: *** [library] Error 2
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src'
make: *** [default] Error 2
Doing the build in the following directory:
/export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0
./configure  --with-libgmp=$SAGE_LOCAL/lib/libgmp.so
Now running Make
make
There are known test failures that should be listed above.
They are literally 'not yet implemented' errors from the
CoCOA library.   I.e., CoCOA releases purposely don't pass
their own test suite at present.
libcocoa.a built!

----------------------------------------------------------------------

To play with libcocoa, type 'sage -sh', then cd to the directory

   /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0/src/examples

and try making and running some of the examples.
When you're done, it is completely safe to delete directory:

   /export/home/drkirkby/sage-4.3.4.alpha1/local/lib/cocoa-0.9930.p0

----------------------------------------------------------------------

real    4m38.333s
user    4m13.925s
sys     0m21.973s
Successfully installed libcocoa-0.9930.p0
```



Issue created by migration from https://trac.sagemath.org/ticket/8527





---

archive/issue_comments_076934.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-04-13T13:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8527#issuecomment-76934",
    "user": "https://github.com/slel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076935.json:
```json
{
    "body": "Propose to close this ticket as obsolete.\n- The experimental libcocoa package seems to have been removed long ago, see #14962.\n- There is a new cocoalib package, see #25707.\nPlease review.",
    "created_at": "2019-04-13T13:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8527#issuecomment-76935",
    "user": "https://github.com/slel"
}
```

Propose to close this ticket as obsolete.
- The experimental libcocoa package seems to have been removed long ago, see #14962.
- There is a new cocoalib package, see #25707.
Please review.



---

archive/issue_comments_076936.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-06-06T18:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8527#issuecomment-76936",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076937.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2019-06-06T18:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8527#issuecomment-76937",
    "user": "https://github.com/fchapoton"
}
```

Resolution: wontfix
