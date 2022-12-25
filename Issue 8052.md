# Issue 8052: Update prereq to version 0.7 (mostly Fortran issues fixed)

archive/issues_008052.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @williamstein\n\nThis is a further update to the 'prereq' script. The changes are\n\n* Checks for a Fortran compiler on any platform except OS X. This addresses #8024 and #8026, which was a duplicate of #8024.\n* Prints *Using the binary Fortran compiler which is included in Sage* if using the binary included on OS X. \n* In the event GNU tools are used, checks gcc, g++ and gfortran are the same version on all platforms except OS X. If SAGE_FORTRAN is defined as something non-empty, then the test is performed on OS X too. \n* Fully checks there are not a mix of GNU and non-GNU compilers #7021 did this for C and C++ compilers, but Fortran was excluded, as stated in #7903. The Fortran compiler is more difficult than C and C++, as gfortran does not process the -dumpversion option in the same logical way as gcc and g++. That will be fixed in gcc 4.5.\n* Checks that SAGE_FORTRAN_LIB points to a dynamic library which is of the right type (32 or 64 bit), depending on the setting of SAGE64. (**This test is only performed on Solaris** as that is the only platform where I have sufficient information to do it properly). So trying to make a 64-bit version of Sage, whilst SAGE_FORTRAN_LIB points to a 32-bit library, will now be detected. #7021 ensured the file pointed to by SAGE_FORTRAN_LIB actually existed, but did not check it was a library of the correct type. \n* Corrects a typo, where 'hpux' was used instead of 'HP-UX'.\n* Checks that perl is at least version 5.8.0. #7021 ensured perl was version 5.6.0 or later, but that is too old to build 'R'. The R documentation states 5.8.0 or later is needed. \n* Checks for the header file complex.h, and issues a **warning** if this is not found. It might not be on some older systems. The build does not exit, as continuing might be helpful for those porting Sage. \n* Checks for the library function sqrtl() which will be found on modern systems, but may not on older systems. A **warning** is issued if the library function does not exist, but the build continues, to aid porting efforts. (I believe FreeBSD may lack this).\n* Copies stdint.h_Solaris9 on Solaris 8 or 9. (Previously this was only done for Solaris 9). The file stdint.h_Solaris9 is a bit broken, as it ignores 64-bit specific parts. But for now, it is better than nothing as it might allow a 32-bit build on Solaris 8 or 9. (I believe gcc 4.5 might have a better fix, and include the missing header.)\n* If the 'configure' script is going to exit with an error, the lines explaining why are no longer warnings, but just notices (AC_MSG_NOTICE rather than AC_MSG_WARN is used in configure.ac). It looks a bit better I think. \n == How to install ==\n* Download the files prereq-0.7.tar and prereq-0.7-install from \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7/\n\nto the directory $SAGE_ROOT/spkg/base There is no need to extract the tar file - it happens automatically. \n* Change the permissions on prereq-0.7-install so they are executable.\n \n == How to test these changes ==\n\nThese changes ideally need testing on many systems. Here are some suggestions, broken into groups of those that should have impacts on all opperating systems, and those that are operating system specific. In each case, after installing the prereq-0.7.tar and prereq-0.7-install, run \n\n```\n $ make distclean\n```\n === All operating systems except OS X ===\nAttempt a build, where there is no Fortran compiler in the path. In \nthe example below, I temporarily renamed gfortran to something else This addresses #8024 and #8026, which was a duplicate.\n {{{\nchecking for gfortran... no\nchecking for g95... no\nchecking for xlf95... no\nchecking for f95... no\nchecking for fort... no\nchecking for ifort... no\nchecking for ifc... no\nchecking for efc... no\nchecking for pgf95... no\nchecking for lf95... no\nchecking for ftn... no\nchecking for xlf90... no\nchecking for f90... no\nchecking for pgf90... no\nchecking for pghpf... no\nchecking for epcf90... no\nchecking for g77... no\nchecking for xlf... no\nchecking for f77... no\nchecking for frt... no\nchecking for pgf77... no\nchecking for cf77... no\nchecking for fort77... no\nchecking for fl32... no\nchecking for af77... no\nchecking whether we are using the GNU Fortran compiler... no\nchecking whether  accepts -g... no\nconfigure: Since Sage 4.3.1 a Fortran compiler is required on all operating\nconfigure: systems except OS X. A Fortran compiler is included on OS X.\nconfigure: See the file README.txt in the top-level directory.\nconfigure: error: Exiting, since a Fortran compiler was not found.\n ERROR: You do not have all of the prerequisites needed\n to build Sage from source.  See the errors above.\nmake[1]: *** [installed/prereq-0.7] Error 1\n }}}\n === All operating systems ===\n* Attempt a build with the first perl version in the path being older than 5.8.0, and ensure a suitable error message is generated. (Given I only changed the version string from 5.6.0 to 5.8.0, checking this is hardly worthwhile, but do so if you are keen).\n* Attempt a build where there is a mix of versions of gcc, g++ and gfortran. An error should be generated. \n* Attempt to mix a non-GNU Fortran compiler, with GNU C or C++ compilers. The following example was tested on Solaris, where SAGE_FORTRAN pointed to the Sun Fortran compiler, but CC and CXX were unset, so gcc and g++ are used by default. \n {{{\nchecking whether we are using the GNU Fortran compiler... (cached) no\nchecking whether /opt/sunstudio12.1/bin/f95 accepts -g... (cached) yes\nchecking for Fortran flag needed to allow free-form source... -free\nconfigure: Your Fortran compiler accepts free-format source code\nconfigure: which older F77 compilers do not. This does not 100%\nconfigure: guarantee your compiler is suitable for building SAGE\nconfigure: but it probably is.\nchecking if gcc accepts -dumpversion option... yes\nchecking gcc version... 4.4.1\nchecking if g++ accepts -dumpversion option... yes\nchecking g++ version... 4.4.1\nf95: Warning: Option -dumpversion passed to ld, if ld is invoked, ignored otherwise\nUsage: f95 [ options ] files.  Use 'f95 -flags' for details\nconfigure: Although gcc and g++ are both version 4.4.1\nconfigure: the Fortran compiler /opt/sunstudio12.1/bin/f95 is some other version.\nconfigure: The output from /opt/sunstudio12.1/bin/f95 --version is below.\n\nf95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise\nUsage: f95 [ options ] files.  Use 'f95 -flags' for details\n\nconfigure: Exiting since the Fortran compiler is not the same\nconfigure: error: version as the C and C++ compilers\n ERROR: You do not have all of the prerequisites needed\n to build Sage from source.  See the errors above.\nmake[1]: *** [installed/prereq-0.7] Error 1\n\n }}}\n\n === OS X ===\n* Attempt a build on a system without a Fortran compiler, ensuring SAGE_FORTRAN is not defined. There should be a message \n {{{\nconfigure: Using the binary Fortran compiler which is\nconfigure: included in Sage.\n }}}\n* Attempt a build on a system without a Fortran compiler, but set SAGE_FORTRAN to something like /bin/ls and ensure that the prereq script tests 'ls' and determines it is not a valid Fortran compiler. You should see the following message:\n {{{\nchecking whether we are using the GNU Fortran compiler... (cached) no\nchecking whether /bin/ls accepts -g... (cached) no\nchecking for Fortran flag needed to allow free-form source... unknown\nconfigure: Your Fortran compiler does not accept free-format source code\nconfigure: which means the compiler is either seriously broken, or\nconfigure: is too old to build Sage.\nconfigure: Note, that on OS X, a Fortran binary is supplied with Sage\nconfigure: so you do not actually need a working Fortran compiler.\nconfigure: You just need to ensure SAGE_FORTRAN is not set to use\nconfigure: the binary Fortran compiler included in Sage. If you set\nconfigure: SAGE_FORTRAN it must point to a working Fortran compiler.\nconfigure: error: Exiting, as the Fortran compiler is not suitable\n ERROR: You do not have all of the prerequisites needed\n to build Sage from source.  See the errors above.\nmake[1]: *** [installed/prereq-0.7] Error 1\n }}}\n \n* Attempt a build on a system with a valid Fortran compiler, setting SAGE_FORTRAN to that compiler. The compiler should be tested. If the versions differ from gcc or g++, this should be indicated. I have not tested this on OS X, as I don't have a system with gfortran installed. But it should work. \n\n === Solaris ===\n* Set SAGE64 to \"yes\", then set SAGE_FORTRAN_LIB to a 32-bit library, which might be /usr/local/lib/libgfortran.so Ensure an informative error message is generated. \n* Unset SAGE64, but set SAGE_FORTRAN_LIB to a 64-bit library, such as /usr/local/lib/sparcv9/ libgfortran.so (SPARC) or /usr/local/lib/amd64/libgfortran.so (Solaris x86) and ensure an informative error message is generated. Something like this \n {{{\nconfigure: The environment variable\nconfigure: SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9/libgfortran.so\nconfigure: is a not a 32-bit dynamic library. SAGE64 was\nconfigure: not set to \"yes\", so you intend to build 32-bit.\nconfigure: The environment variables SAGE_FORTRAN_LIB and/or SAGE64\nconfigure: are not set properly.\n ERROR: You do not have all of the prerequisites needed\n to build Sage from source.  See the errors above.\nmake[1]: *** [installed/prereq-0.7] Error 1\n}}} \n\n == Notes to release manager ==\n* I don't know enough about 'hg' to know how to handle the changes, when a file changes name. Sorry ... \n* prereq-0.7-install must be installed with execute permissions. \n* prereq-0.6-install should be removed. \n* prereq-0.6.tar should be removed. \n* prereq-0.7.tar is not under revision control\n* When this ticket is closed, #8024 and #7903 may be closed too. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8052\n\n",
    "closed_at": "2010-01-31T22:30:28Z",
    "created_at": "2010-01-25T01:10:22Z",
    "labels": [
        "component: build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Update prereq to version 0.7 (mostly Fortran issues fixed)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8052",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @williamstein

This is a further update to the 'prereq' script. The changes are

* Checks for a Fortran compiler on any platform except OS X. This addresses #8024 and #8026, which was a duplicate of #8024.
* Prints *Using the binary Fortran compiler which is included in Sage* if using the binary included on OS X. 
* In the event GNU tools are used, checks gcc, g++ and gfortran are the same version on all platforms except OS X. If SAGE_FORTRAN is defined as something non-empty, then the test is performed on OS X too. 
* Fully checks there are not a mix of GNU and non-GNU compilers #7021 did this for C and C++ compilers, but Fortran was excluded, as stated in #7903. The Fortran compiler is more difficult than C and C++, as gfortran does not process the -dumpversion option in the same logical way as gcc and g++. That will be fixed in gcc 4.5.
* Checks that SAGE_FORTRAN_LIB points to a dynamic library which is of the right type (32 or 64 bit), depending on the setting of SAGE64. (**This test is only performed on Solaris** as that is the only platform where I have sufficient information to do it properly). So trying to make a 64-bit version of Sage, whilst SAGE_FORTRAN_LIB points to a 32-bit library, will now be detected. #7021 ensured the file pointed to by SAGE_FORTRAN_LIB actually existed, but did not check it was a library of the correct type. 
* Corrects a typo, where 'hpux' was used instead of 'HP-UX'.
* Checks that perl is at least version 5.8.0. #7021 ensured perl was version 5.6.0 or later, but that is too old to build 'R'. The R documentation states 5.8.0 or later is needed. 
* Checks for the header file complex.h, and issues a **warning** if this is not found. It might not be on some older systems. The build does not exit, as continuing might be helpful for those porting Sage. 
* Checks for the library function sqrtl() which will be found on modern systems, but may not on older systems. A **warning** is issued if the library function does not exist, but the build continues, to aid porting efforts. (I believe FreeBSD may lack this).
* Copies stdint.h_Solaris9 on Solaris 8 or 9. (Previously this was only done for Solaris 9). The file stdint.h_Solaris9 is a bit broken, as it ignores 64-bit specific parts. But for now, it is better than nothing as it might allow a 32-bit build on Solaris 8 or 9. (I believe gcc 4.5 might have a better fix, and include the missing header.)
* If the 'configure' script is going to exit with an error, the lines explaining why are no longer warnings, but just notices (AC_MSG_NOTICE rather than AC_MSG_WARN is used in configure.ac). It looks a bit better I think. 
 == How to install ==
* Download the files prereq-0.7.tar and prereq-0.7-install from 

http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7/

to the directory $SAGE_ROOT/spkg/base There is no need to extract the tar file - it happens automatically. 
* Change the permissions on prereq-0.7-install so they are executable.
 
 == How to test these changes ==

These changes ideally need testing on many systems. Here are some suggestions, broken into groups of those that should have impacts on all opperating systems, and those that are operating system specific. In each case, after installing the prereq-0.7.tar and prereq-0.7-install, run 

```
 $ make distclean
```
 === All operating systems except OS X ===
Attempt a build, where there is no Fortran compiler in the path. In 
the example below, I temporarily renamed gfortran to something else This addresses #8024 and #8026, which was a duplicate.
 {{{
checking for gfortran... no
checking for g95... no
checking for xlf95... no
checking for f95... no
checking for fort... no
checking for ifort... no
checking for ifc... no
checking for efc... no
checking for pgf95... no
checking for lf95... no
checking for ftn... no
checking for xlf90... no
checking for f90... no
checking for pgf90... no
checking for pghpf... no
checking for epcf90... no
checking for g77... no
checking for xlf... no
checking for f77... no
checking for frt... no
checking for pgf77... no
checking for cf77... no
checking for fort77... no
checking for fl32... no
checking for af77... no
checking whether we are using the GNU Fortran compiler... no
checking whether  accepts -g... no
configure: Since Sage 4.3.1 a Fortran compiler is required on all operating
configure: systems except OS X. A Fortran compiler is included on OS X.
configure: See the file README.txt in the top-level directory.
configure: error: Exiting, since a Fortran compiler was not found.
 ERROR: You do not have all of the prerequisites needed
 to build Sage from source.  See the errors above.
make[1]: *** [installed/prereq-0.7] Error 1
 }}}
 === All operating systems ===
* Attempt a build with the first perl version in the path being older than 5.8.0, and ensure a suitable error message is generated. (Given I only changed the version string from 5.6.0 to 5.8.0, checking this is hardly worthwhile, but do so if you are keen).
* Attempt a build where there is a mix of versions of gcc, g++ and gfortran. An error should be generated. 
* Attempt to mix a non-GNU Fortran compiler, with GNU C or C++ compilers. The following example was tested on Solaris, where SAGE_FORTRAN pointed to the Sun Fortran compiler, but CC and CXX were unset, so gcc and g++ are used by default. 
 {{{
checking whether we are using the GNU Fortran compiler... (cached) no
checking whether /opt/sunstudio12.1/bin/f95 accepts -g... (cached) yes
checking for Fortran flag needed to allow free-form source... -free
configure: Your Fortran compiler accepts free-format source code
configure: which older F77 compilers do not. This does not 100%
configure: guarantee your compiler is suitable for building SAGE
configure: but it probably is.
checking if gcc accepts -dumpversion option... yes
checking gcc version... 4.4.1
checking if g++ accepts -dumpversion option... yes
checking g++ version... 4.4.1
f95: Warning: Option -dumpversion passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details
configure: Although gcc and g++ are both version 4.4.1
configure: the Fortran compiler /opt/sunstudio12.1/bin/f95 is some other version.
configure: The output from /opt/sunstudio12.1/bin/f95 --version is below.

f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details

configure: Exiting since the Fortran compiler is not the same
configure: error: version as the C and C++ compilers
 ERROR: You do not have all of the prerequisites needed
 to build Sage from source.  See the errors above.
make[1]: *** [installed/prereq-0.7] Error 1

 }}}

 === OS X ===
* Attempt a build on a system without a Fortran compiler, ensuring SAGE_FORTRAN is not defined. There should be a message 
 {{{
configure: Using the binary Fortran compiler which is
configure: included in Sage.
 }}}
* Attempt a build on a system without a Fortran compiler, but set SAGE_FORTRAN to something like /bin/ls and ensure that the prereq script tests 'ls' and determines it is not a valid Fortran compiler. You should see the following message:
 {{{
checking whether we are using the GNU Fortran compiler... (cached) no
checking whether /bin/ls accepts -g... (cached) no
checking for Fortran flag needed to allow free-form source... unknown
configure: Your Fortran compiler does not accept free-format source code
configure: which means the compiler is either seriously broken, or
configure: is too old to build Sage.
configure: Note, that on OS X, a Fortran binary is supplied with Sage
configure: so you do not actually need a working Fortran compiler.
configure: You just need to ensure SAGE_FORTRAN is not set to use
configure: the binary Fortran compiler included in Sage. If you set
configure: SAGE_FORTRAN it must point to a working Fortran compiler.
configure: error: Exiting, as the Fortran compiler is not suitable
 ERROR: You do not have all of the prerequisites needed
 to build Sage from source.  See the errors above.
make[1]: *** [installed/prereq-0.7] Error 1
 }}}
 
* Attempt a build on a system with a valid Fortran compiler, setting SAGE_FORTRAN to that compiler. The compiler should be tested. If the versions differ from gcc or g++, this should be indicated. I have not tested this on OS X, as I don't have a system with gfortran installed. But it should work. 

 === Solaris ===
* Set SAGE64 to "yes", then set SAGE_FORTRAN_LIB to a 32-bit library, which might be /usr/local/lib/libgfortran.so Ensure an informative error message is generated. 
* Unset SAGE64, but set SAGE_FORTRAN_LIB to a 64-bit library, such as /usr/local/lib/sparcv9/ libgfortran.so (SPARC) or /usr/local/lib/amd64/libgfortran.so (Solaris x86) and ensure an informative error message is generated. Something like this 
 {{{
configure: The environment variable
configure: SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.1-sun-linker/lib/sparcv9/libgfortran.so
configure: is a not a 32-bit dynamic library. SAGE64 was
configure: not set to "yes", so you intend to build 32-bit.
configure: The environment variables SAGE_FORTRAN_LIB and/or SAGE64
configure: are not set properly.
 ERROR: You do not have all of the prerequisites needed
 to build Sage from source.  See the errors above.
make[1]: *** [installed/prereq-0.7] Error 1
}}} 

 == Notes to release manager ==
* I don't know enough about 'hg' to know how to handle the changes, when a file changes name. Sorry ... 
* prereq-0.7-install must be installed with execute permissions. 
* prereq-0.6-install should be removed. 
* prereq-0.6.tar should be removed. 
* prereq-0.7.tar is not under revision control
* When this ticket is closed, #8024 and #7903 may be closed too. 

Issue created by migration from https://trac.sagemath.org/ticket/8052





---

archive/issue_comments_070315.json:
```json
{
    "body": "> I don't know enough about 'hg' to know how to handle the changes, when a file changes name. Sorry ...\n\n\nDon't worry, David. I can take care of such issues.",
    "created_at": "2010-01-25T01:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

> I don't know enough about 'hg' to know how to handle the changes, when a file changes name. Sorry ...


Don't worry, David. I can take care of such issues.



---

archive/issue_comments_070316.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T01:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70316",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070317.json:
```json
{
    "body": "Replying to [comment:1 mvngu]:\n> > I don't know enough about 'hg' to know how to handle the changes, when a file changes name. Sorry ...\n\n> \n> Don't worry, David. I can take care of such issues.\n\nThank you Minh.",
    "created_at": "2010-01-25T01:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70317",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:1 mvngu]:
> > I don't know enough about 'hg' to know how to handle the changes, when a file changes name. Sorry ...

> 
> Don't worry, David. I can take care of such issues.

Thank you Minh.



---

archive/issue_comments_070318.json:
```json
{
    "body": "patch against configure.ac in prereq-0.6",
    "created_at": "2010-01-26T11:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70318",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

patch against configure.ac in prereq-0.6



---

archive/issue_comments_070319.json:
```json
{
    "body": "Attachment [prereq-install.patch](tarball://root/attachments/some-uuid/ticket8052/prereq-install.patch) by mvngu created at 2010-01-26 11:34:53\n\npatch against prereq-install of prereq-0.6",
    "created_at": "2010-01-26T11:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70319",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [prereq-install.patch](tarball://root/attachments/some-uuid/ticket8052/prereq-install.patch) by mvngu created at 2010-01-26 11:34:53

patch against prereq-install of prereq-0.6



---

archive/issue_comments_070320.json:
```json
{
    "body": "Based on David's [prereq-0.7](http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7), I have attached two patches showing differences between prereq-0.6 and prereq-0.7. I think the changes are made in `prereq-install` and `configure.ac`, so only patches affecting these two files are attached. These patches are for references only to show differences between the older and newer versions. Do not apply them, but instead use the updated package at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7",
    "created_at": "2010-01-26T11:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70320",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Based on David's [prereq-0.7](http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7), I have attached two patches showing differences between prereq-0.6 and prereq-0.7. I think the changes are made in `prereq-install` and `configure.ac`, so only patches affecting these two files are attached. These patches are for references only to show differences between the older and newer versions. Do not apply them, but instead use the updated package at 

http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7



---

archive/issue_comments_070321.json:
```json
{
    "body": "With the updated prereq spkg, Sage 4.3.2.alpha0 still builds on platforms where it previously compiled OK. To test how a build might fail, I followed David's instructions for Linux, Mac OS X, Solaris. On Cygwin (winxp1 on boxen.math), I set the environment variables\n\n```\nexport SAGE_PORT=yes\nexport SAGE_FORTRAN=/usr/bin/ls\n```\nwhich results in a build failure as expected. Overall, the updated spkg looks OK. The instructions for testing are excellent. Thank you, David.",
    "created_at": "2010-01-31T19:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70321",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

With the updated prereq spkg, Sage 4.3.2.alpha0 still builds on platforms where it previously compiled OK. To test how a build might fail, I followed David's instructions for Linux, Mac OS X, Solaris. On Cygwin (winxp1 on boxen.math), I set the environment variables

```
export SAGE_PORT=yes
export SAGE_FORTRAN=/usr/bin/ls
```
which results in a build failure as expected. Overall, the updated spkg looks OK. The instructions for testing are excellent. Thank you, David.



---

archive/issue_comments_070322.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T19:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70322",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070323.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-31T22:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_070324.json:
```json
{
    "body": "Merged [prereq-0.7-install](http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7/prereq-0.7-install) and [prereq-0.7.tar](http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7/prereq-0.7.tar) in the base spkg repository. All changes have been committed in David Kirkby's name.",
    "created_at": "2010-01-31T22:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8052#issuecomment-70324",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [prereq-0.7-install](http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7/prereq-0.7-install) and [prereq-0.7.tar](http://boxen.math.washington.edu/home/kirkby/portability/prereq-0.7/prereq-0.7.tar) in the base spkg repository. All changes have been committed in David Kirkby's name.



---

archive/issue_events_019286.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-31T22:30:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8052",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8052#event-19286"
}
```
