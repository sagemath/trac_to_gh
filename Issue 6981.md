# Issue 6981: include 64-bit OS X gfortran in standard SAge

archive/issues_006981.json:
```json
{
    "body": "Assignee: tbd\n\nThis will make the tarball bigger (by 24MB), but is the only way to go at present.   With this one spkg update, building Sage 64-bit on OS X will be as simple as typing:\n\n\n```\nexport SAGE64=\"yes\"\nmake\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6981\n\n",
    "created_at": "2009-09-22T01:42:38Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "include 64-bit OS X gfortran in standard SAge",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6981",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

This will make the tarball bigger (by 24MB), but is the only way to go at present.   With this one spkg update, building Sage 64-bit on OS X will be as simple as typing:


```
export SAGE64="yes"
make
```




Issue created by migration from https://trac.sagemath.org/ticket/6981





---

archive/issue_comments_057624.json:
```json
{
    "body": "The spkg is here:\n\n  http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p6.spkg",
    "created_at": "2009-09-22T02:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57624",
    "user": "https://github.com/williamstein"
}
```

The spkg is here:

  http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p6.spkg



---

archive/issue_comments_057625.json:
```json
{
    "body": "For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines\n\n```\ncp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL\ncd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .\n```\n\nshould be changed to something like\n\n```\ncd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .\n```\n\nAlso, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function `install_fortran_osx64` could start with a message like\n\n```\nprint \"Installing OSX 64-bit gfortran compiler\"\n```\n\nSome people who are sticklers might complain about the format of SPGK.txt, but I don't care that much.",
    "created_at": "2009-09-22T04:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57625",
    "user": "https://github.com/jhpalmieri"
}
```

For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines

```
cp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL
cd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .
```

should be changed to something like

```
cd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .
```

Also, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function `install_fortran_osx64` could start with a message like

```
print "Installing OSX 64-bit gfortran compiler"
```

Some people who are sticklers might complain about the format of SPGK.txt, but I don't care that much.



---

archive/issue_comments_057626.json:
```json
{
    "body": "Changing component from build to packages.",
    "created_at": "2009-09-22T07:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from build to packages.



---

archive/issue_comments_057627.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines\n> {{{\n> cp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL\n> cd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .\n> }}}\n> should be changed to something like\n> {{{\n> cd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .\n> }}}\nDone. I have added your reviewer comment to `src/gfortran/fortran-OSX64-20090120/spkg-install` and committed this change in your name.\n\n\n\n\n> Also, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function `install_fortran_osx64` could start with a message like\n> {{{\n> print \"Installing OSX 64-bit gfortran compiler\"\n> }}}\nDone. This line is now in the main `spkg-install`. The change has been committed in your name.\n\n\n\n\n\n> Some people who are sticklers might complain about the format of SPGK.txt, but I don't care that much.\nAlso taken care of. An updated spkg with reviewer changes can be found at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/fortran-20071120.p6.spkg\n\nI'm reviewing the actual building of that package now. You're more than welcome to try building Sage 4.1.2.alpha2 from source with this updated Fortran package. The more the merrier :-)",
    "created_at": "2009-09-22T07:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57627",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 jhpalmieri]:
> For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines
> {{{
> cp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL
> cd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .
> }}}
> should be changed to something like
> {{{
> cd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .
> }}}
Done. I have added your reviewer comment to `src/gfortran/fortran-OSX64-20090120/spkg-install` and committed this change in your name.




> Also, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function `install_fortran_osx64` could start with a message like
> {{{
> print "Installing OSX 64-bit gfortran compiler"
> }}}
Done. This line is now in the main `spkg-install`. The change has been committed in your name.





> Some people who are sticklers might complain about the format of SPGK.txt, but I don't care that much.
Also taken care of. An updated spkg with reviewer changes can be found at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/fortran-20071120.p6.spkg

I'm reviewing the actual building of that package now. You're more than welcome to try building Sage 4.1.2.alpha2 from source with this updated Fortran package. The more the merrier :-)



---

archive/issue_comments_057628.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-09-22T07:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_057629.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines\n> {{{\n> cp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL\n> cd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .\n> }}}\n> should be changed to something like\n> {{{\n> cd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .\n> }}}\nThis results in the following error:\n\n```\ntar (child): /Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha2/spkg/build/fortran-20071120.p6/src/gfortran/fortran-OSX64-20090120/gfortran-4.2.3.tar.bz2: Cannot open: No such file or directory\ntar (child): Error is not recoverable: exiting now\ntar: Child returned status 2\ntar: Error exit delayed from previous errors\nInstalling OS X 64-bit gfortran compiler\n\n\n\n\n\n\n**********************************************************************\n\n\n\n\n\n\nError installing Fortran: Error installing OS X 64-bit gfortran\n```\n\nThe actual command should be \n\n```\ncd $SAGE_LOCAL; tar -xjf $CUR/src/gfortran-4.2.3.tar.bz2 -C .\n```\n\nNotice the \"src\" part. The updated spkg includes this fix.",
    "created_at": "2009-09-22T07:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 jhpalmieri]:
> For the 64-bit version, is there a reason to copy a big bzipped tar file to SAGE_LOCAL?  If not, then I think that in the file [{{/src/gfortran/fortran-OSX64-20090120/spkg-install}}}, the lines
> {{{
> cp src/gfortran-4.2.3.tar.bz2 $SAGE_LOCAL
> cd $SAGE_LOCAL; tar -xjf gfortran-4.2.3.tar.bz2 -C .
> }}}
> should be changed to something like
> {{{
> cd $SAGE_LOCAL; tar -xjf $CUR/gfortran-4.2.3.tar.bz2 -C .
> }}}
This results in the following error:

```
tar (child): /Volumes/LACIE/scratch/mvngu/sandbox-32/sage-4.1.2.alpha2/spkg/build/fortran-20071120.p6/src/gfortran/fortran-OSX64-20090120/gfortran-4.2.3.tar.bz2: Cannot open: No such file or directory
tar (child): Error is not recoverable: exiting now
tar: Child returned status 2
tar: Error exit delayed from previous errors
Installing OS X 64-bit gfortran compiler






**********************************************************************






Error installing Fortran: Error installing OS X 64-bit gfortran
```

The actual command should be 

```
cd $SAGE_LOCAL; tar -xjf $CUR/src/gfortran-4.2.3.tar.bz2 -C .
```

Notice the "src" part. The updated spkg includes this fix.



---

archive/issue_comments_057630.json:
```json
{
    "body": "Mac OS 10.5: open a new terminal (and doublecheck that SAGE64 is not set).  Untar sage-4.1.2.alpha2 and replace the fortran package there with the new one.  Type 'make' and wait: I see\n\n```\nInstalling OS X 64-bit gfortran compiler\n```\n\nI don't know why...",
    "created_at": "2009-09-22T14:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57630",
    "user": "https://github.com/jhpalmieri"
}
```

Mac OS 10.5: open a new terminal (and doublecheck that SAGE64 is not set).  Untar sage-4.1.2.alpha2 and replace the fortran package there with the new one.  Type 'make' and wait: I see

```
Installing OS X 64-bit gfortran compiler
```

I don't know why...



---

archive/issue_comments_057631.json:
```json
{
    "body": "New spkg up here: http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p7.spkg",
    "created_at": "2009-09-22T15:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57631",
    "user": "https://github.com/williamstein"
}
```

New spkg up here: http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p7.spkg



---

archive/issue_comments_057632.json:
```json
{
    "body": "Almost perfect.  To make it perfect, I would like to see this change from mvngu's version re-incorporated:\n\n> Also, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function install_fortran_osx64 could start with a message like\n\n```\nprint \"Installing OSX 64-bit gfortran compiler\"\n```\n",
    "created_at": "2009-09-22T15:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57632",
    "user": "https://github.com/jhpalmieri"
}
```

Almost perfect.  To make it perfect, I would like to see this change from mvngu's version re-incorporated:

> Also, there should be a message about the 64-bit version being installed: in the main spkg-install file, the function install_fortran_osx64 could start with a message like

```
print "Installing OSX 64-bit gfortran compiler"
```




---

archive/issue_comments_057633.json:
```json
{
    "body": "OK, I refreshed the spkg with that.",
    "created_at": "2009-09-22T15:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57633",
    "user": "https://github.com/williamstein"
}
```

OK, I refreshed the spkg with that.



---

archive/issue_comments_057634.json:
```json
{
    "body": "Looks good to me.  The SPKG.txt file isn't in the right format, but I don't care.",
    "created_at": "2009-09-22T15:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57634",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.  The SPKG.txt file isn't in the right format, but I don't care.



---

archive/issue_comments_057635.json:
```json
{
    "body": "I've made a major improvement to how this spkg detects \"64 bit\" so it will work when building Sage on OS X 10.6 without explicitly specifying SAGE64.  Instead of using that flag it simply checks the bitness of Python.  Without this we would get a 32-bit compiler, which is completely wrong. \n\n  New spkg: http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p8.spkg",
    "created_at": "2009-09-25T06:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57635",
    "user": "https://github.com/williamstein"
}
```

I've made a major improvement to how this spkg detects "64 bit" so it will work when building Sage on OS X 10.6 without explicitly specifying SAGE64.  Instead of using that flag it simply checks the bitness of Python.  Without this we would get a 32-bit compiler, which is completely wrong. 

  New spkg: http://sage.math.washington.edu/home/wstein/patches/fortran-20071120.p8.spkg



---

archive/issue_comments_057636.json:
```json
{
    "body": "New spkg up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/fortran-20071120.p9.spkg\n\nThe only changes from .p8 are:\n\n* remove junk files: `spkg-install~` and `SPKG.txt~`\n* add info to SPKG.txt",
    "created_at": "2009-09-27T00:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57636",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

New spkg up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/fortran-20071120.p9.spkg

The only changes from .p8 are:

* remove junk files: `spkg-install~` and `SPKG.txt~`
* add info to SPKG.txt



---

archive/issue_comments_057637.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-27T02:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57637",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057638.json:
```json
{
    "body": "See palmieri's and my reports at #6849.",
    "created_at": "2009-09-27T02:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57638",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See palmieri's and my reports at #6849.



---

archive/issue_comments_057639.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6981#issuecomment-57639",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
