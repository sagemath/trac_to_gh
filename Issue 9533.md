# Issue 9533: Update GSL to the latest upstream release

archive/issues_009533.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  leif mpatel\n\nThe version of the [GNU Scientific Library (GSL)](http://www.gnu.org/software/gsl/) in Sage is 1.10, which is almost 3 years old. The latest, 1.14 was released about 4 months ago. \n\nThere is also a large number of bugs in the `spkg-check` and `spkg-install` files\n \n* `spkg-check` did not exit with a non-zero error code if the `make check` failed. It did however report the error, but it is highly likely to be missed in a large log file. This issue was reported at #9531, so that ticket can be closed when this one is closed. \n* `spkg-install` did not exit if `configure` failed to configure properly. Again the error was reported. \n* `spkg-install` did not exit if `make` failed to build GSL correctly. Again the error was reported. \n* `spkg-install` did not exit if `make install` failed to install GSL properly. Again the error was reported. \n* The self-tests were failing on some platforms, due to the fact `/bin/rm: cannot remove `libtoolT`. This was also true of the latest version, but exporting RM to \"rm -f\" solved that, as discussed at [solution for libtoolT error](http://toxpenguin.blogspot.com/2009/09/solution-for-libtoolt-error.html)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9533\n\n",
    "created_at": "2010-07-17T21:00:52Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Update GSL to the latest upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9533",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  leif mpatel

The version of the [GNU Scientific Library (GSL)](http://www.gnu.org/software/gsl/) in Sage is 1.10, which is almost 3 years old. The latest, 1.14 was released about 4 months ago. 

There is also a large number of bugs in the `spkg-check` and `spkg-install` files
 
* `spkg-check` did not exit with a non-zero error code if the `make check` failed. It did however report the error, but it is highly likely to be missed in a large log file. This issue was reported at #9531, so that ticket can be closed when this one is closed. 
* `spkg-install` did not exit if `configure` failed to configure properly. Again the error was reported. 
* `spkg-install` did not exit if `make` failed to build GSL correctly. Again the error was reported. 
* `spkg-install` did not exit if `make install` failed to install GSL properly. Again the error was reported. 
* The self-tests were failing on some platforms, due to the fact `/bin/rm: cannot remove `libtoolT`. This was also true of the latest version, but exporting RM to "rm -f" solved that, as discussed at [solution for libtoolT error](http://toxpenguin.blogspot.com/2009/09/solution-for-libtoolt-error.html)

Issue created by migration from https://trac.sagemath.org/ticket/9533





---

archive/issue_comments_091768.json:
```json
{
    "body": "A possibility for another ticket: Checking whether we can replace `make` with `$MAKE` in GSL's `spkg-install`.",
    "created_at": "2010-07-17T21:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91768",
    "user": "mpatel"
}
```

A possibility for another ticket: Checking whether we can replace `make` with `$MAKE` in GSL's `spkg-install`.



---

archive/issue_comments_091769.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> A possibility for another ticket: Checking whether we can replace `make` with `$MAKE` in GSL's `spkg-install`.\n\nI'm pretty sure we can, since I have built this multiple times on my Sun Blade 2000 SPARC with 2 threads and on my Sun Ultra 27 with 12 threads. This is outside the Sage environment, so my settings for MAKE would have been used. There were no problems building on either in parallel, so I don't think it will be a problem building with $MAKE. \n\nI'll test that before uploading a patch and providing a link. \n\nDave",
    "created_at": "2010-07-17T21:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91769",
    "user": "drkirkby"
}
```

Replying to [comment:1 mpatel]:
> A possibility for another ticket: Checking whether we can replace `make` with `$MAKE` in GSL's `spkg-install`.

I'm pretty sure we can, since I have built this multiple times on my Sun Blade 2000 SPARC with 2 threads and on my Sun Ultra 27 with 12 threads. This is outside the Sage environment, so my settings for MAKE would have been used. There were no problems building on either in parallel, so I don't think it will be a problem building with $MAKE. 

I'll test that before uploading a patch and providing a link. 

Dave



---

archive/issue_comments_091770.json:
```json
{
    "body": "I'm convinced this is ok built in parallel. I tested it several times in parallel (outside of Sage) before you even mentioned it. But after you said this, I used $MAKE in `spkg-install` and systematically checked it on different systems\n\n* 19 parallel builds on a Sun Ultra 27, with OpenSolaris using between 2 and 1000 threads. \n* 5 parallel builds on bsd.math, with OS 10.6, using 4 threads.\n* 5 parallel builds on sage.math, with Ubunta, using 8 threads.\n* 3 parallel builds on a Sun Blade 2000, with Solaris 10, using between 2 and 4 threads. (Code compiled 64-bit)\n* 3 parallel builds on a Sun Blade 2000, with Solaris 10, using between 2 and 4 threads. (Code compiled 32-bit)\n \n \nIn all cases, all the self-tests for GSL passed. \n\n\nI've run the doctests on sage.math. I was quite expecting to get a few failures due to different results from different algorithms that might be used in the GSL library, but to my surprise:\n\n\n```\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 1095.8 seconds\nkirkby@sage:/scratch/kirkby/sage-4.5$ \n```\n\n\nHere's a link to the package. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg\n\nI'm going to upload 3 patches. The first was all the updates. The second uses {{{$MAKE}} and the final one just prints an informative message when the tests pass. Is there a sensible way of reversing these patches once they are commited, so I don't need 3 of them? Anyway, the patches are for review only. They don't need to be applied to the package. \n\nThe first patch is quite large, as it removes a big patch. \n\nDave \nDave",
    "created_at": "2010-07-18T00:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91770",
    "user": "drkirkby"
}
```

I'm convinced this is ok built in parallel. I tested it several times in parallel (outside of Sage) before you even mentioned it. But after you said this, I used $MAKE in `spkg-install` and systematically checked it on different systems

* 19 parallel builds on a Sun Ultra 27, with OpenSolaris using between 2 and 1000 threads. 
* 5 parallel builds on bsd.math, with OS 10.6, using 4 threads.
* 5 parallel builds on sage.math, with Ubunta, using 8 threads.
* 3 parallel builds on a Sun Blade 2000, with Solaris 10, using between 2 and 4 threads. (Code compiled 64-bit)
* 3 parallel builds on a Sun Blade 2000, with Solaris 10, using between 2 and 4 threads. (Code compiled 32-bit)
 
 
In all cases, all the self-tests for GSL passed. 


I've run the doctests on sage.math. I was quite expecting to get a few failures due to different results from different algorithms that might be used in the GSL library, but to my surprise:


```
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 1095.8 seconds
kirkby@sage:/scratch/kirkby/sage-4.5$ 
```


Here's a link to the package. 

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

I'm going to upload 3 patches. The first was all the updates. The second uses {{{$MAKE}} and the final one just prints an informative message when the tests pass. Is there a sensible way of reversing these patches once they are commited, so I don't need 3 of them? Anyway, the patches are for review only. They don't need to be applied to the package. 

The first patch is quite large, as it removes a big patch. 

Dave 
Dave



---

archive/issue_comments_091771.json:
```json
{
    "body": "Attachment [9533.patch](tarball://root/attachments/some-uuid/ticket9533/9533.patch) by drkirkby created at 2010-07-18 00:22:19\n\nMain patch, which makes many changes to clean up the spkg-check and spkg-install.",
    "created_at": "2010-07-18T00:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91771",
    "user": "drkirkby"
}
```

Attachment [9533.patch](tarball://root/attachments/some-uuid/ticket9533/9533.patch) by drkirkby created at 2010-07-18 00:22:19

Main patch, which makes many changes to clean up the spkg-check and spkg-install.



---

archive/issue_comments_091772.json:
```json
{
    "body": "Attachment [9533.use-Dollar-MAKE.patch](tarball://root/attachments/some-uuid/ticket9533/9533.use-Dollar-MAKE.patch) by drkirkby created at 2010-07-18 00:23:01\n\nChanges 'make' to '$MAKE' to allow faster parallel builds. This has been extensively tested",
    "created_at": "2010-07-18T00:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91772",
    "user": "drkirkby"
}
```

Attachment [9533.use-Dollar-MAKE.patch](tarball://root/attachments/some-uuid/ticket9533/9533.use-Dollar-MAKE.patch) by drkirkby created at 2010-07-18 00:23:01

Changes 'make' to '$MAKE' to allow faster parallel builds. This has been extensively tested



---

archive/issue_comments_091773.json:
```json
{
    "body": "Add a message to indicate the tests have passed.",
    "created_at": "2010-07-18T00:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91773",
    "user": "drkirkby"
}
```

Add a message to indicate the tests have passed.



---

archive/issue_comments_091774.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-18T00:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91774",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091775.json:
```json
{
    "body": "Attachment [9533.print-passed-message.patch](tarball://root/attachments/some-uuid/ticket9533/9533.print-passed-message.patch) by drkirkby created at 2010-07-18 00:23:49",
    "created_at": "2010-07-18T00:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91775",
    "user": "drkirkby"
}
```

Attachment [9533.print-passed-message.patch](tarball://root/attachments/some-uuid/ticket9533/9533.print-passed-message.patch) by drkirkby created at 2010-07-18 00:23:49



---

archive/issue_comments_091776.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-07-18T00:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91776",
    "user": "drkirkby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_091777.json:
```json
{
    "body": "On bsd.math\n\n\n```\n$ make ptestlong\n\n<SNIP> \n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2503.7 seconds\n[kirkby@bsd sage-4.5.rc1]$ \n```\n",
    "created_at": "2010-07-18T00:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91777",
    "user": "drkirkby"
}
```

On bsd.math


```
$ make ptestlong

<SNIP> 

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2503.7 seconds
[kirkby@bsd sage-4.5.rc1]$ 
```




---

archive/issue_comments_091778.json:
```json
{
    "body": "At first glance (I only looked at the patches) ok, except\n* *Append* to `CFLAGS` et al. rather than set/overwrite them\n* Typo: 1x s/builing/building/ (2nd patch SPKG.txt)\n* Perhaps add to SPKG.txt that `spkg-check` also now uses `$MAKE`\n* Move the \"successful check\" message out of the else part, right to the bottom ;-)\n\nI don't know why you want to create a single patch, but you can simply take an old vanilla GSL spkg and apply your patches in order with `hg import --no-commit ...` (or use `patch`), and after that, just do a commit.\n\nI'll take a closer look at the package tomorrow, I think.",
    "created_at": "2010-07-18T01:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91778",
    "user": "leif"
}
```

At first glance (I only looked at the patches) ok, except
* *Append* to `CFLAGS` et al. rather than set/overwrite them
* Typo: 1x s/builing/building/ (2nd patch SPKG.txt)
* Perhaps add to SPKG.txt that `spkg-check` also now uses `$MAKE`
* Move the "successful check" message out of the else part, right to the bottom ;-)

I don't know why you want to create a single patch, but you can simply take an old vanilla GSL spkg and apply your patches in order with `hg import --no-commit ...` (or use `patch`), and after that, just do a commit.

I'll take a closer look at the package tomorrow, I think.



---

archive/issue_comments_091779.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> you can simply take an old vanilla GSL spkg and apply your patches in order with `hg import --no-commit ...` (or use `patch`), and after that, just do a commit.\n\nOh, I just noticed Mercurial doesn't like successive imports without commit, simply use `patch < ...` for the second and third.",
    "created_at": "2010-07-18T02:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91779",
    "user": "leif"
}
```

Replying to [comment:7 leif]:
> you can simply take an old vanilla GSL spkg and apply your patches in order with `hg import --no-commit ...` (or use `patch`), and after that, just do a commit.

Oh, I just noticed Mercurial doesn't like successive imports without commit, simply use `patch < ...` for the second and third.



---

archive/issue_comments_091780.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> Oh, I just noticed Mercurial doesn't like successive imports without commit, simply use `patch < ...` for the second and third.\n\n`hg import -f --no-commit ...` (three times) does the trick as well... :)",
    "created_at": "2010-07-18T02:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91780",
    "user": "leif"
}
```

Replying to [comment:8 leif]:
> Oh, I just noticed Mercurial doesn't like successive imports without commit, simply use `patch < ...` for the second and third.

`hg import -f --no-commit ...` (three times) does the trick as well... :)



---

archive/issue_comments_091781.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> At first glance (I only looked at the patches) ok, except\n>  * *Append* to `CFLAGS` et al. rather than set/overwrite them\n\nOK. \n\n>  * Typo: 1x s/builing/building/ (2nd patch SPKG.txt)\nCheers\n\n>  * Perhaps add to SPKG.txt that `spkg-check` also now uses `$MAKE`\n\nYes.\n\n>  * Move the \"successful check\" message out of the else part, right to the bottom ;-)\n\nYes, good idea. It saves a few bytes. \n\n> I don't know why you want to create a single patch\nI think its more difficult to read patches when they are very small. I'd personally rather see one patch that fixes all the problems, rather than loads of patches fixing parts of it. But I'll just add another patch here. \n\nDave",
    "created_at": "2010-07-18T07:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91781",
    "user": "drkirkby"
}
```

Replying to [comment:7 leif]:
> At first glance (I only looked at the patches) ok, except
>  * *Append* to `CFLAGS` et al. rather than set/overwrite them

OK. 

>  * Typo: 1x s/builing/building/ (2nd patch SPKG.txt)
Cheers

>  * Perhaps add to SPKG.txt that `spkg-check` also now uses `$MAKE`

Yes.

>  * Move the "successful check" message out of the else part, right to the bottom ;-)

Yes, good idea. It saves a few bytes. 

> I don't know why you want to create a single patch
I think its more difficult to read patches when they are very small. I'd personally rather see one patch that fixes all the problems, rather than loads of patches fixing parts of it. But I'll just add another patch here. 

Dave



---

archive/issue_comments_091782.json:
```json
{
    "body": "Patch taking into account comments by reviewer, and a bit of a tidyup.",
    "created_at": "2010-07-18T08:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91782",
    "user": "drkirkby"
}
```

Patch taking into account comments by reviewer, and a bit of a tidyup.



---

archive/issue_comments_091783.json:
```json
{
    "body": "Attachment [9533-tidyup-and-resolve-flag-issues.patch](tarball://root/attachments/some-uuid/ticket9533/9533-tidyup-and-resolve-flag-issues.patch) by drkirkby created at 2010-07-18 08:43:45\n\nLeif,\nI've taken your comments into account. I realised that despite what src/INSTALL says, -g -O2 were not added. So I've added them back, as they were before. I also noticed the web site I gave for the solution to the libtool problem (export RM=\"rm -f\") was not the correct one. So I updated the web link in the description of this, and also in SPKG.txt\n\nI also reformatted SPKG.txt so no lines are wider than 80 characters. \n\nI've replaced the package, so it can still be found at http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg\n\nDave",
    "created_at": "2010-07-18T08:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91783",
    "user": "drkirkby"
}
```

Attachment [9533-tidyup-and-resolve-flag-issues.patch](tarball://root/attachments/some-uuid/ticket9533/9533-tidyup-and-resolve-flag-issues.patch) by drkirkby created at 2010-07-18 08:43:45

Leif,
I've taken your comments into account. I realised that despite what src/INSTALL says, -g -O2 were not added. So I've added them back, as they were before. I also noticed the web site I gave for the solution to the libtool problem (export RM="rm -f") was not the correct one. So I updated the web link in the description of this, and also in SPKG.txt

I also reformatted SPKG.txt so no lines are wider than 80 characters. 

I've replaced the package, so it can still be found at http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

Dave



---

archive/issue_comments_091784.json:
```json
{
    "body": "Slightlly simpler spkg-check",
    "created_at": "2010-07-18T08:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91784",
    "user": "drkirkby"
}
```

Slightlly simpler spkg-check



---

archive/issue_comments_091785.json:
```json
{
    "body": "Attachment [9533-improve-spkg-check.patch](tarball://root/attachments/some-uuid/ticket9533/9533-improve-spkg-check.patch) by leif created at 2010-07-18 18:43:34\n\nA few (more general) questions:\n* Should we make sure that `$SAGE_LOCAL` is set? (in both `spkg-install` and `spkg-check`)\n* Should optimization be disabled (`-O0`) if `SAGE_DEBUG` is `yes` as some other packages do?\n* Anything to add if `SAGE_FAT_BINARY` is `yes`?\n* I think `CFLAGS` et al. should be set in `spkg-check` as well, as `make check` usually involves compilation, too.\n* Also modifying `LDFLAGS`, e.g. if `SAGE64=yes`, even if currently not directly used by upstream, should be safe.\n\nP.S.: My intention regarding the `else ... exit 0` part was rather avoiding other people adding \"dead code\" below it. Looking at the (fairly small) file in whole this seems less a danger... :)",
    "created_at": "2010-07-18T18:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91785",
    "user": "leif"
}
```

Attachment [9533-improve-spkg-check.patch](tarball://root/attachments/some-uuid/ticket9533/9533-improve-spkg-check.patch) by leif created at 2010-07-18 18:43:34

A few (more general) questions:
* Should we make sure that `$SAGE_LOCAL` is set? (in both `spkg-install` and `spkg-check`)
* Should optimization be disabled (`-O0`) if `SAGE_DEBUG` is `yes` as some other packages do?
* Anything to add if `SAGE_FAT_BINARY` is `yes`?
* I think `CFLAGS` et al. should be set in `spkg-check` as well, as `make check` usually involves compilation, too.
* Also modifying `LDFLAGS`, e.g. if `SAGE64=yes`, even if currently not directly used by upstream, should be safe.

P.S.: My intention regarding the `else ... exit 0` part was rather avoiding other people adding "dead code" below it. Looking at the (fairly small) file in whole this seems less a danger... :)



---

archive/issue_comments_091786.json:
```json
{
    "body": "Just for the record (mhansen?):\n  *\"GSL should compile with GCC under Cygwin on Microsoft Windows.There is a gsl package in the standard Cygwin distribution which contains any patches needed.\"*",
    "created_at": "2010-07-18T19:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91786",
    "user": "leif"
}
```

Just for the record (mhansen?):
  *"GSL should compile with GCC under Cygwin on Microsoft Windows.There is a gsl package in the standard Cygwin distribution which contains any patches needed."*



---

archive/issue_comments_091787.json:
```json
{
    "body": "Replying to [comment:13 leif]:\n> A few (more general) questions:\n>  * Should we make sure that `$SAGE_LOCAL` is set? (in both `spkg-install` and `spkg-check`)\n\nI think that would be wise. I will address that. \n\n>  * Should optimization be disabled (`-O0`) if `SAGE_DEBUG` is `yes` as some other packages do?\n\nTo be practical, SAGE_DEBUG is not really going to be very useful, as too few packages use it. But I can make that change. Even if every .spkg in Sage used SAGE_DEBUG that way, many upstream packages add -O2 anyway. \n\n>  * Anything to add if `SAGE_FAT_BINARY` is `yes`?\n\nI do not believe so. This does not link with anything other than ATLAS. \n\n>  * I think `CFLAGS` et al. should be set in `spkg-check` as well, as `make check` usually involves compilation, too.\n\nIn general you are right, but in this case it is not necessary. I know that, as I was using SAGE64 set to yes to add the -m64 option. That's a pretty critical option on 64-bit builds, but it was not necessary to add it. I assume that's in the Makefile which has already been created. \n\nBut I accept it would be safer, just in case GSL change the build process in some way. I am aware of cases where this has been an issue in `spkg-check`. I'll modify that. \n\n>  * Also modifying `LDFLAGS`, e.g. if `SAGE64=yes`, even if currently not directly used by upstream, should be safe.\n\nYes, again, it may be safer to do this. \n\n> P.S.: My intention regarding the `else ... exit 0` part was rather avoiding other people adding \"dead code\" below it. Looking at the (fairly small) file in whole this seems less a danger... :)\n\nNo problem. I did wonder if its best to exit a script with `exit 0` rather than just let it exit. I know you can get away without specifying an exit code, but I'm not sure if it's good practice or not. \n\nDave",
    "created_at": "2010-07-18T20:42:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91787",
    "user": "drkirkby"
}
```

Replying to [comment:13 leif]:
> A few (more general) questions:
>  * Should we make sure that `$SAGE_LOCAL` is set? (in both `spkg-install` and `spkg-check`)

I think that would be wise. I will address that. 

>  * Should optimization be disabled (`-O0`) if `SAGE_DEBUG` is `yes` as some other packages do?

To be practical, SAGE_DEBUG is not really going to be very useful, as too few packages use it. But I can make that change. Even if every .spkg in Sage used SAGE_DEBUG that way, many upstream packages add -O2 anyway. 

>  * Anything to add if `SAGE_FAT_BINARY` is `yes`?

I do not believe so. This does not link with anything other than ATLAS. 

>  * I think `CFLAGS` et al. should be set in `spkg-check` as well, as `make check` usually involves compilation, too.

In general you are right, but in this case it is not necessary. I know that, as I was using SAGE64 set to yes to add the -m64 option. That's a pretty critical option on 64-bit builds, but it was not necessary to add it. I assume that's in the Makefile which has already been created. 

But I accept it would be safer, just in case GSL change the build process in some way. I am aware of cases where this has been an issue in `spkg-check`. I'll modify that. 

>  * Also modifying `LDFLAGS`, e.g. if `SAGE64=yes`, even if currently not directly used by upstream, should be safe.

Yes, again, it may be safer to do this. 

> P.S.: My intention regarding the `else ... exit 0` part was rather avoiding other people adding "dead code" below it. Looking at the (fairly small) file in whole this seems less a danger... :)

No problem. I did wonder if its best to exit a script with `exit 0` rather than just let it exit. I know you can get away without specifying an exit code, but I'm not sure if it's good practice or not. 

Dave



---

archive/issue_comments_091788.json:
```json
{
    "body": "Attachment [9533-add-SAGE_DEBUG-and_CFLAG64.patch](tarball://root/attachments/some-uuid/ticket9533/9533-add-SAGE_DEBUG-and_CFLAG64.patch) by drkirkby created at 2010-07-18 21:52:50\n\nAdds support for SAGE_DEBUG, CFLAG64, checks SAGE_ROOT and exports LDFLAGS on 64-bit builds",
    "created_at": "2010-07-18T21:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91788",
    "user": "drkirkby"
}
```

Attachment [9533-add-SAGE_DEBUG-and_CFLAG64.patch](tarball://root/attachments/some-uuid/ticket9533/9533-add-SAGE_DEBUG-and_CFLAG64.patch) by drkirkby created at 2010-07-18 21:52:50

Adds support for SAGE_DEBUG, CFLAG64, checks SAGE_ROOT and exports LDFLAGS on 64-bit builds



---

archive/issue_comments_091789.json:
```json
{
    "body": "I've made those changes. The package can be found here\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg\n\nIt's interesting to compare compile and test times both with and without SAGE_DEBUG\n\n* SAGE_DEBUG=yes, SAGE_CHECK unset =  30.7s\n* SAGE_DEBUG unset, SAGE_CHECK unset = 50.7s\n* SAGE_DEBUG=yes, SAGE_CHECK=yes 1m:24s\n* SAGE_DEBUG unset, SAGE_CHECK=yes 1m:34s\n\nSo it takes 20 seconds longer to build when using optimisation. That time penalty drops to 10 seconds when the tests are run, as they obviously run quicker. (All times are measured on a 3.33 GHz Sun Ultra 27)",
    "created_at": "2010-07-18T22:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91789",
    "user": "drkirkby"
}
```

I've made those changes. The package can be found here

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

It's interesting to compare compile and test times both with and without SAGE_DEBUG

* SAGE_DEBUG=yes, SAGE_CHECK unset =  30.7s
* SAGE_DEBUG unset, SAGE_CHECK unset = 50.7s
* SAGE_DEBUG=yes, SAGE_CHECK=yes 1m:24s
* SAGE_DEBUG unset, SAGE_CHECK=yes 1m:34s

So it takes 20 seconds longer to build when using optimisation. That time penalty drops to 10 seconds when the tests are run, as they obviously run quicker. (All times are measured on a 3.33 GHz Sun Ultra 27)



---

archive/issue_comments_091790.json:
```json
{
    "body": "Replying to [comment:15 drkirkby]:\n> I did wonder if its best to exit a script with `exit 0` rather than just let it exit. I know you can get away without specifying an exit code, but I'm not sure if it's good practice or not. \n\nWell, without `exit` the script returns `$?`, which is even better, though in some cases (or bad scripts) this is not desirable.\n\n----\nI must admit I don't understand that ATLAS thing. It seems to me `configure` doesn't look for anything related to it. If it did, we had to add `-I$SAGE_LOCAL/include` and `-L$SAGE_LOCAL/lib`. I tried that, but it doesn't make any difference. I also couldn't find any `configure` options to build extra stuff or use external packages. Or does this only matter if one puts additional packages into the source tree?",
    "created_at": "2010-07-18T22:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91790",
    "user": "leif"
}
```

Replying to [comment:15 drkirkby]:
> I did wonder if its best to exit a script with `exit 0` rather than just let it exit. I know you can get away without specifying an exit code, but I'm not sure if it's good practice or not. 

Well, without `exit` the script returns `$?`, which is even better, though in some cases (or bad scripts) this is not desirable.

----
I must admit I don't understand that ATLAS thing. It seems to me `configure` doesn't look for anything related to it. If it did, we had to add `-I$SAGE_LOCAL/include` and `-L$SAGE_LOCAL/lib`. I tried that, but it doesn't make any difference. I also couldn't find any `configure` options to build extra stuff or use external packages. Or does this only matter if one puts additional packages into the source tree?



---

archive/issue_comments_091791.json:
```json
{
    "body": "Replying to [comment:17 leif]:\n\n> I must admit I don't understand that ATLAS thing. It seems to me `configure` doesn't look for anything related to it. If it did, we had to add `-I$SAGE_LOCAL/include` and `-L$SAGE_LOCAL/lib`. I tried that, but it doesn't make any difference. I also couldn't find any `configure` options to build extra stuff or use external packages. Or does this only matter if one puts additional packages into the source tree?\n\nLike you, I can't understand the ATLAS thing. The [GSL web site](http://www.gnu.org/software/gsl/) mentions it:\n\n*GSL requires a BLAS library for vector and matrix operations. The default CBLAS library supplied with GSL can be replaced by the tuned ATLAS library for better performance*\n\nBut when I tried building a 32-bit GSL in Sage, where there were all 64-bit libraries (including ATLAS), this built fine. Had it really tried to link to the ATLAS library, then the build would have failed. So quite how you link to ATLAS to get better performance is beyond me. It is certainly not linking to ATLAS in Sage. That means there is an unnecessary dependency in 'deps' but I'm not going to worry over this. \n\nDave",
    "created_at": "2010-07-18T22:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91791",
    "user": "drkirkby"
}
```

Replying to [comment:17 leif]:

> I must admit I don't understand that ATLAS thing. It seems to me `configure` doesn't look for anything related to it. If it did, we had to add `-I$SAGE_LOCAL/include` and `-L$SAGE_LOCAL/lib`. I tried that, but it doesn't make any difference. I also couldn't find any `configure` options to build extra stuff or use external packages. Or does this only matter if one puts additional packages into the source tree?

Like you, I can't understand the ATLAS thing. The [GSL web site](http://www.gnu.org/software/gsl/) mentions it:

*GSL requires a BLAS library for vector and matrix operations. The default CBLAS library supplied with GSL can be replaced by the tuned ATLAS library for better performance*

But when I tried building a 32-bit GSL in Sage, where there were all 64-bit libraries (including ATLAS), this built fine. Had it really tried to link to the ATLAS library, then the build would have failed. So quite how you link to ATLAS to get better performance is beyond me. It is certainly not linking to ATLAS in Sage. That means there is an unnecessary dependency in 'deps' but I'm not going to worry over this. 

Dave



---

archive/issue_comments_091792.json:
```json
{
    "body": "Any attempt to use ATLAS rather than CBLAS should be on another ticket.",
    "created_at": "2010-07-18T22:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91792",
    "user": "drkirkby"
}
```

Any attempt to use ATLAS rather than CBLAS should be on another ticket.



---

archive/issue_comments_091793.json:
```json
{
    "body": "Replying to [comment:19 drkirkby]:\n> Any attempt to use ATLAS rather than CBLAS should be on another ticket.\n\nI agree, but then ATLAS should be removed from GSL's dependencies in `spkg/standard/deps`.",
    "created_at": "2010-07-18T22:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91793",
    "user": "leif"
}
```

Replying to [comment:19 drkirkby]:
> Any attempt to use ATLAS rather than CBLAS should be on another ticket.

I agree, but then ATLAS should be removed from GSL's dependencies in `spkg/standard/deps`.



---

archive/issue_comments_091794.json:
```json
{
    "body": "The GSL web site also lists *\"Some applications using GSL that we know of\"*; Sage is missing there... ;-)",
    "created_at": "2010-07-18T23:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91794",
    "user": "leif"
}
```

The GSL web site also lists *"Some applications using GSL that we know of"*; Sage is missing there... ;-)



---

archive/issue_comments_091795.json:
```json
{
    "body": "Replying to [comment:20 leif]:\n> Replying to [comment:19 drkirkby]:\n> > Any attempt to use ATLAS rather than CBLAS should be on another ticket.\n> \n> I agree, but then ATLAS should be removed from GSL's dependencies in `spkg/standard/deps`.\nAgreed. but that should be on another ticket too. It is unrelated to the update of the package, and could potentially cause problems due to a change in the build order, if the deps file is not 100% OK. We still seem to be uncovering errors in that file with the parallel builds, so I'm not keen to do that change on this ticket. \n\nDave",
    "created_at": "2010-07-18T23:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91795",
    "user": "drkirkby"
}
```

Replying to [comment:20 leif]:
> Replying to [comment:19 drkirkby]:
> > Any attempt to use ATLAS rather than CBLAS should be on another ticket.
> 
> I agree, but then ATLAS should be removed from GSL's dependencies in `spkg/standard/deps`.
Agreed. but that should be on another ticket too. It is unrelated to the update of the package, and could potentially cause problems due to a change in the build order, if the deps file is not 100% OK. We still seem to be uncovering errors in that file with the parallel builds, so I'm not keen to do that change on this ticket. 

Dave



---

archive/issue_comments_091796.json:
```json
{
    "body": "Mike Hansen has reported that this builds on Cygwin, and all tests pass\n\n\n```\n> > If you export SAGE_CHECK=yes, the self-tests will run. So far they pass on\n> > every system I've checked this on.\nI forgot to post this yesterday, but I built it on Cygwin and all tests passed.\n\n--Mike\n```\n\n\nIt's now been tested on \n* Cygwin\n* Linux\n* OpenSolaris\n* OS X\n* Solaris\n\nCan this get a positive review? \n\nDave",
    "created_at": "2010-07-19T01:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91796",
    "user": "drkirkby"
}
```

Mike Hansen has reported that this builds on Cygwin, and all tests pass


```
> > If you export SAGE_CHECK=yes, the self-tests will run. So far they pass on
> > every system I've checked this on.
I forgot to post this yesterday, but I built it on Cygwin and all tests passed.

--Mike
```


It's now been tested on 
* Cygwin
* Linux
* OpenSolaris
* OS X
* Solaris

Can this get a positive review? 

Dave



---

archive/issue_comments_091797.json:
```json
{
    "body": "sage-check also succeeds for mw on both FreeBSD-8.1/amd64 and Cygwin 1.7.5",
    "created_at": "2010-07-19T22:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91797",
    "user": "pjeremy"
}
```

sage-check also succeeds for mw on both FreeBSD-8.1/amd64 and Cygwin 1.7.5



---

archive/issue_comments_091798.json:
```json
{
    "body": "Also on the HP-UX operating system\n\n\n```\n-bash-4.0$ uname -a\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n```\n\n\non an old HP C3600 (552 MHz, big-endian PA-RISC processor)\n\n\n```\nThe self-tests of GSL were successfully passed\nNow cleaning up tmp files.\nrm: directory /home/drkirkby/sage-4.3/spkg/build/gsl-1.14 not removed.  Cannot remove current directory\nMaking Sage/Python scripts relocatable...\nNo such file or directory: python\nFinished installing gsl-1.14.spkg\n\nreal\t30m47.515s\nuser\t27m32.320s\nsys\t2m0.120s\n```\n\n\nSo the GSL library has now been shown to build and pass all tests on:\n\n* Cygwin \n* FreeBSD\n* HP-UX\n* Linux\n* OpenSolaris \n* OS X \n* Solaris\n\nI wish all the code in Sage was as portable!\n\nDave",
    "created_at": "2010-07-20T00:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91798",
    "user": "drkirkby"
}
```

Also on the HP-UX operating system


```
-bash-4.0$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
```


on an old HP C3600 (552 MHz, big-endian PA-RISC processor)


```
The self-tests of GSL were successfully passed
Now cleaning up tmp files.
rm: directory /home/drkirkby/sage-4.3/spkg/build/gsl-1.14 not removed.  Cannot remove current directory
Making Sage/Python scripts relocatable...
No such file or directory: python
Finished installing gsl-1.14.spkg

real	30m47.515s
user	27m32.320s
sys	2m0.120s
```


So the GSL library has now been shown to build and pass all tests on:

* Cygwin 
* FreeBSD
* HP-UX
* Linux
* OpenSolaris 
* OS X 
* Solaris

I wish all the code in Sage was as portable!

Dave



---

archive/issue_comments_091799.json:
```json
{
    "body": "As a final change, could we clarify the ATLAS/CBLAS issue in `SPKG.txt`, i.e.\n* Dependencies: **None** - GSL does currently **not** depend on any other Sage package (though ATLAS is currently listed in `spkg/standard/deps`\n* Add a *\"Special Update/Build Instructions\"* section that mentions that GSL could **in principle** use ATLAS's CBLAS implementation rather than the one shipped with GSL (but so far never did in Sage).\n\nCurrently building Sage 4.5.1 with GSL 1.14 from scratch...\n\n(I've already tested the spkg with 4.5 \"final\" on two machines, but only by forcing installation of the new package. This btw discovered even more flaws in the doctesting \"frame\"work regarding parallel testing and timeouts on the slower machine...)",
    "created_at": "2010-07-20T15:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91799",
    "user": "leif"
}
```

As a final change, could we clarify the ATLAS/CBLAS issue in `SPKG.txt`, i.e.
* Dependencies: **None** - GSL does currently **not** depend on any other Sage package (though ATLAS is currently listed in `spkg/standard/deps`
* Add a *"Special Update/Build Instructions"* section that mentions that GSL could **in principle** use ATLAS's CBLAS implementation rather than the one shipped with GSL (but so far never did in Sage).

Currently building Sage 4.5.1 with GSL 1.14 from scratch...

(I've already tested the spkg with 4.5 "final" on two machines, but only by forcing installation of the new package. This btw discovered even more flaws in the doctesting "frame"work regarding parallel testing and timeouts on the slower machine...)



---

archive/issue_comments_091800.json:
```json
{
    "body": "Attachment [9533-improved-SPKG.text_file.patch](tarball://root/attachments/some-uuid/ticket9533/9533-improved-SPKG.text_file.patch) by drkirkby created at 2010-07-20 17:07:48\n\nChanges only to SPKG.txt (nothing to actual code). Reflects reviewer comments, and some extra information I thought was informative.",
    "created_at": "2010-07-20T17:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91800",
    "user": "drkirkby"
}
```

Attachment [9533-improved-SPKG.text_file.patch](tarball://root/attachments/some-uuid/ticket9533/9533-improved-SPKG.text_file.patch) by drkirkby created at 2010-07-20 17:07:48

Changes only to SPKG.txt (nothing to actual code). Reflects reviewer comments, and some extra information I thought was informative.



---

archive/issue_comments_091801.json:
```json
{
    "body": "Fix a silly typo",
    "created_at": "2010-07-20T17:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91801",
    "user": "drkirkby"
}
```

Fix a silly typo



---

archive/issue_comments_091802.json:
```json
{
    "body": "Attachment [9533-typo.patch](tarball://root/attachments/some-uuid/ticket9533/9533-typo.patch) by drkirkby created at 2010-07-20 17:15:27\n\nReplying to [comment:26 leif]:\n> As a final change, could we clarify the ATLAS/CBLAS issue in `SPKG.txt`, i.e.\n>  * Dependencies: **None** - GSL does currently **not** depend on any other Sage package (though ATLAS is currently listed in `spkg/standard/deps`\n>  * Add a *\"Special Update/Build Instructions\"* section that mentions that GSL could **in principle** use ATLAS's CBLAS implementation rather than the one shipped with GSL (but so far never did in Sage).\n> \n\nSure. I made a few other changes to that file too - hopefully to your approval. No code was changed. \n\n> Currently building Sage 4.5.1 with GSL 1.14 from scratch...\n\nGood. \n \n> (I've already tested the spkg with 4.5 \"final\" on two machines, but only by forcing installation of the new package. This btw discovered even more flaws in the doctesting \"frame\"work regarding parallel testing and timeouts on the slower machine...)\n\nYou do not surprise me with regard to the doctesting framework. However, before wasting any time on them, do check to see if there are any patches recently added to trac for this, as I know there were several such patches. I'm not the release manager, but if I were, I'd get those patches in on the alpha0. If you can't rely on the test code, what can you rely on? \n\nDave",
    "created_at": "2010-07-20T17:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91802",
    "user": "drkirkby"
}
```

Attachment [9533-typo.patch](tarball://root/attachments/some-uuid/ticket9533/9533-typo.patch) by drkirkby created at 2010-07-20 17:15:27

Replying to [comment:26 leif]:
> As a final change, could we clarify the ATLAS/CBLAS issue in `SPKG.txt`, i.e.
>  * Dependencies: **None** - GSL does currently **not** depend on any other Sage package (though ATLAS is currently listed in `spkg/standard/deps`
>  * Add a *"Special Update/Build Instructions"* section that mentions that GSL could **in principle** use ATLAS's CBLAS implementation rather than the one shipped with GSL (but so far never did in Sage).
> 

Sure. I made a few other changes to that file too - hopefully to your approval. No code was changed. 

> Currently building Sage 4.5.1 with GSL 1.14 from scratch...

Good. 
 
> (I've already tested the spkg with 4.5 "final" on two machines, but only by forcing installation of the new package. This btw discovered even more flaws in the doctesting "frame"work regarding parallel testing and timeouts on the slower machine...)

You do not surprise me with regard to the doctesting framework. However, before wasting any time on them, do check to see if there are any patches recently added to trac for this, as I know there were several such patches. I'm not the release manager, but if I were, I'd get those patches in on the alpha0. If you can't rely on the test code, what can you rely on? 

Dave



---

archive/issue_comments_091803.json:
```json
{
    "body": "Oh, I actually took the *\"val\"* as an abbreviation, and thought you did mean this one:\n  *Force GSL to be buil**d** with no optimisation if SAGE_DEBUG is set to \"yes\"*\n\nMaybe to your surprise, I'm ok with the rest. ;-)\n\n(The only thing that could be clarified is *\"64-bit builds\"* meaning 64-bit builds on systems where the compiler default is 32-bit, i.e. when `SAGE64` is \"yes\".)\n\nLeif",
    "created_at": "2010-07-20T17:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91803",
    "user": "leif"
}
```

Oh, I actually took the *"val"* as an abbreviation, and thought you did mean this one:
  *Force GSL to be buil**d** with no optimisation if SAGE_DEBUG is set to "yes"*

Maybe to your surprise, I'm ok with the rest. ;-)

(The only thing that could be clarified is *"64-bit builds"* meaning 64-bit builds on systems where the compiler default is 32-bit, i.e. when `SAGE64` is "yes".)

Leif



---

archive/issue_comments_091804.json:
```json
{
    "body": "Attachment [64-bit-build-clarification.patch](tarball://root/attachments/some-uuid/ticket9533/64-bit-build-clarification.patch) by drkirkby created at 2010-07-20 18:10:13\n\nClarify what are 64-bit builds",
    "created_at": "2010-07-20T18:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91804",
    "user": "drkirkby"
}
```

Attachment [64-bit-build-clarification.patch](tarball://root/attachments/some-uuid/ticket9533/64-bit-build-clarification.patch) by drkirkby created at 2010-07-20 18:10:13

Clarify what are 64-bit builds



---

archive/issue_comments_091805.json:
```json
{
    "body": "I've updated SPKG.txt to make it clearer what are 64-bit builds. \n\nPackage can be found here. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg",
    "created_at": "2010-07-20T18:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91805",
    "user": "drkirkby"
}
```

I've updated SPKG.txt to make it clearer what are 64-bit builds. 

Package can be found here. 

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg



---

archive/issue_comments_091806.json:
```json
{
    "body": "I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: **Nothing! 8D**\n\n(A closer look at `$SAGE_ROOT/devel/sage-main/module_list.py` helped. I hope other *Sage packages* that require CBLAS will also link with `libcblas.*`, not `libgslcblas.*`.)\n\nThe only thing we could (but perhaps shouldn't) do is run GSL's testsuite with ATLAS's CBLAS library instead.\nBut since GSL's implementation is used as a fall-back in Sage, we should leave it as is, and - if at all - only do an *additional* run of the testsuite with ATLAS's CBLAS library. (But I've not yet figured out how simple that is; in worst case we'd have to `make clean`, `make` again with `LDFLAGS=\"$LDFLAGS -L$SAGE_LOCAL/lib -lcblas -latlas\"` and then `make check`.)",
    "created_at": "2010-07-20T19:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91806",
    "user": "leif"
}
```

I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: **Nothing! 8D**

(A closer look at `$SAGE_ROOT/devel/sage-main/module_list.py` helped. I hope other *Sage packages* that require CBLAS will also link with `libcblas.*`, not `libgslcblas.*`.)

The only thing we could (but perhaps shouldn't) do is run GSL's testsuite with ATLAS's CBLAS library instead.
But since GSL's implementation is used as a fall-back in Sage, we should leave it as is, and - if at all - only do an *additional* run of the testsuite with ATLAS's CBLAS library. (But I've not yet figured out how simple that is; in worst case we'd have to `make clean`, `make` again with `LDFLAGS="$LDFLAGS -L$SAGE_LOCAL/lib -lcblas -latlas"` and then `make check`.)



---

archive/issue_comments_091807.json:
```json
{
    "body": "Final `ptestlong` now running - will take nearly 4 hours...",
    "created_at": "2010-07-20T21:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91807",
    "user": "leif"
}
```

Final `ptestlong` now running - will take nearly 4 hours...



---

archive/issue_comments_091808.json:
```json
{
    "body": "Replying to [comment:30 leif]:\n> I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: **Nothing! 8D**\n> \n> (A closer look at `$SAGE_ROOT/devel/sage-main/module_list.py` helped. I hope other *Sage packages* that require CBLAS will also link with `libcblas.*`, not `libgslcblas.*`.)\n> \n> The only thing we could (but perhaps shouldn't) do is run GSL's testsuite with ATLAS's CBLAS library instead.\n> But since GSL's implementation is used as a fall-back in Sage, we should leave it as is, and - if at all - only do an *additional* run of the testsuite with ATLAS's CBLAS library. (But I've not yet figured out how simple that is; in worst case we'd have to `make clean`, `make` again with `LDFLAGS=\"$LDFLAGS -L$SAGE_LOCAL/lib -lcblas -latlas\"` and then `make check`.)\n\nI think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket. \n\nOther tasks, **if** we tackle them, should be on another ticket. \n\nThere are three related issues I am aware of\n\n* Sage ships with `blas-20070724.spkg` which is a BLAS library, and according to Fran\u00e7ois Bissey, this is unnecessary, as we have ATLAS. http://groups.google.co.uk/group/sage-devel/msg/a75a7e796a5c3a91\n* We should be updating ATLAS. It was agreed to update ATLAS, and I said I would do it, but it far from a trivial affair. I need to discuss with Carl Witty how to build this in parallel. ATLAS takes about 8-10 hours to build in 't2' as there are no tuning parameters for that processor. \n* I've got no idea what GSL is used for in Sage. If it's just special functions, which is quite possible, then its pointless worrying about it anyway. \n\nMy biggest priority now is to get Sage working properly on OpenSolaris - it builds, but just dumps core as soon as one starts it. Hence I want to be able to verify the different parts of Sage are working - I'm less concerned if they are fully optimised. \n\nIf I believe the tools on Solaris, starting Sage, before one gets to the \n\n```\nsage:\n```\n\n\nprompt, there is already several memory leaks. I see the quality control issues in Sage (doctest, self-tests, memory leaks), more important than addling extra functionality, or speeding Sage up. \n\nDave",
    "created_at": "2010-07-20T21:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91808",
    "user": "drkirkby"
}
```

Replying to [comment:30 leif]:
> I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: **Nothing! 8D**
> 
> (A closer look at `$SAGE_ROOT/devel/sage-main/module_list.py` helped. I hope other *Sage packages* that require CBLAS will also link with `libcblas.*`, not `libgslcblas.*`.)
> 
> The only thing we could (but perhaps shouldn't) do is run GSL's testsuite with ATLAS's CBLAS library instead.
> But since GSL's implementation is used as a fall-back in Sage, we should leave it as is, and - if at all - only do an *additional* run of the testsuite with ATLAS's CBLAS library. (But I've not yet figured out how simple that is; in worst case we'd have to `make clean`, `make` again with `LDFLAGS="$LDFLAGS -L$SAGE_LOCAL/lib -lcblas -latlas"` and then `make check`.)

I think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket. 

Other tasks, **if** we tackle them, should be on another ticket. 

There are three related issues I am aware of

* Sage ships with `blas-20070724.spkg` which is a BLAS library, and according to François Bissey, this is unnecessary, as we have ATLAS. http://groups.google.co.uk/group/sage-devel/msg/a75a7e796a5c3a91
* We should be updating ATLAS. It was agreed to update ATLAS, and I said I would do it, but it far from a trivial affair. I need to discuss with Carl Witty how to build this in parallel. ATLAS takes about 8-10 hours to build in 't2' as there are no tuning parameters for that processor. 
* I've got no idea what GSL is used for in Sage. If it's just special functions, which is quite possible, then its pointless worrying about it anyway. 

My biggest priority now is to get Sage working properly on OpenSolaris - it builds, but just dumps core as soon as one starts it. Hence I want to be able to verify the different parts of Sage are working - I'm less concerned if they are fully optimised. 

If I believe the tools on Solaris, starting Sage, before one gets to the 

```
sage:
```


prompt, there is already several memory leaks. I see the quality control issues in Sage (doctest, self-tests, memory leaks), more important than addling extra functionality, or speeding Sage up. 

Dave



---

archive/issue_comments_091809.json:
```json
{
    "body": "Replying to [comment:32 drkirkby]:\n> Replying to [comment:30 leif]:\n> > I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: **Nothing! 8D** [...]\n> \n> I think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket.\n\nYes, I agree. I only wanted to say that regarding GSL *nothing* further has to be done - not even on a follow-up ticket.\n\n> [...]\n> I see the quality control issues in Sage (doctest, self-tests, memory leaks), more important than addling extra functionality, or speeding Sage up. \n\nAgree on that, too. Removing unnecessary parts or extra upstream baggage and improving the documentation are other things I consider important, the former of course less.",
    "created_at": "2010-07-20T21:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91809",
    "user": "leif"
}
```

Replying to [comment:32 drkirkby]:
> Replying to [comment:30 leif]:
> > I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: **Nothing! 8D** [...]
> 
> I think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket.

Yes, I agree. I only wanted to say that regarding GSL *nothing* further has to be done - not even on a follow-up ticket.

> [...]
> I see the quality control issues in Sage (doctest, self-tests, memory leaks), more important than addling extra functionality, or speeding Sage up. 

Agree on that, too. Removing unnecessary parts or extra upstream baggage and improving the documentation are other things I consider important, the former of course less.



---

archive/issue_comments_091810.json:
```json
{
    "body": "Replying to [comment:33 leif]:\n> Replying to [comment:32 drkirkby]:\n> > Replying to [comment:30 leif]:\n> > > I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: **Nothing! 8D** [...]\n> > \n> > I think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket.\n> \n> Yes, I agree. I only wanted to say that regarding GSL *nothing* further has to be done - not even on a follow-up ticket.\n\nGiven what you have discovered, I suspect SPKG.txt in this package should be changed again. Can you suggest a set of changes. I'll then make sure the information is correct. \n\nDave",
    "created_at": "2010-07-20T21:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91810",
    "user": "drkirkby"
}
```

Replying to [comment:33 leif]:
> Replying to [comment:32 drkirkby]:
> > Replying to [comment:30 leif]:
> > > I finally found out what we have to do to make GSL use ATLAS's CBLAS in Sage: **Nothing! 8D** [...]
> > 
> > I think at this point in time, just merging the updated GSL is sufficient. That was the aim of the ticket.
> 
> Yes, I agree. I only wanted to say that regarding GSL *nothing* further has to be done - not even on a follow-up ticket.

Given what you have discovered, I suspect SPKG.txt in this package should be changed again. Can you suggest a set of changes. I'll then make sure the information is correct. 

Dave



---

archive/issue_comments_091811.json:
```json
{
    "body": "Suggestion:\n\n```patch\ndiff --git a/SPKG.txt b/SPKG.txt\n--- a/SPKG.txt\n+++ b/SPKG.txt\n@@ -38,17 +38,15 @@\n\n == Dependencies ==\n\n- * None - GSL does currently not depend on any other Sage package to \n-   compile, link and pass all GSL's self-tests. However, as of \n-   20th July 2010, ATLAS is listed as a dependency in spkg/standard/deps. \n+ * None - GSL 1.14 does not depend on any other Sage package to compile,\n+   link and pass all of GSL's self-tests. Despite that fact, as of \n+   20th July 2010, ATLAS is listed as a dependency in spkg/standard/deps.\n+   (It comes with its own CBLAS implementation that is e.g. used when running\n+   the GSL test suite during installation; however, the Sage library only\n+   uses it as a fall-back, if e.g. ATLAS's CBLAS library is not present.)\n\n == Special Update/Build Instructions ==\n- * According to the GSL web page: http://www.gnu.org/software/gsl/\n-   \"GSL requires a BLAS library for vector and matrix operations. The \n-   default CBLAS library supplied with GSL can be replaced by the tuned \n-   ATLAS library for better performance\". Exactly how one would use ATLAS is\n-   not clear (there are no obvious options for the 'configure' script), \n-   but in principle it could be done. \n+ * Currently nothing special to be done.\n```\n",
    "created_at": "2010-07-20T22:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91811",
    "user": "leif"
}
```

Suggestion:

```patch
diff --git a/SPKG.txt b/SPKG.txt
--- a/SPKG.txt
+++ b/SPKG.txt
@@ -38,17 +38,15 @@

 == Dependencies ==

- * None - GSL does currently not depend on any other Sage package to 
-   compile, link and pass all GSL's self-tests. However, as of 
-   20th July 2010, ATLAS is listed as a dependency in spkg/standard/deps. 
+ * None - GSL 1.14 does not depend on any other Sage package to compile,
+   link and pass all of GSL's self-tests. Despite that fact, as of 
+   20th July 2010, ATLAS is listed as a dependency in spkg/standard/deps.
+   (It comes with its own CBLAS implementation that is e.g. used when running
+   the GSL test suite during installation; however, the Sage library only
+   uses it as a fall-back, if e.g. ATLAS's CBLAS library is not present.)

 == Special Update/Build Instructions ==
- * According to the GSL web page: http://www.gnu.org/software/gsl/
-   "GSL requires a BLAS library for vector and matrix operations. The 
-   default CBLAS library supplied with GSL can be replaced by the tuned 
-   ATLAS library for better performance". Exactly how one would use ATLAS is
-   not clear (there are no obvious options for the 'configure' script), 
-   but in principle it could be done. 
+ * Currently nothing special to be done.
```




---

archive/issue_comments_091812.json:
```json
{
    "body": "Oh, I also changed the item regarding the addition of the *\"Special Update/Build Instructions\"* section, which is missing above...",
    "created_at": "2010-07-20T23:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91812",
    "user": "leif"
}
```

Oh, I also changed the item regarding the addition of the *"Special Update/Build Instructions"* section, which is missing above...



---

archive/issue_comments_091813.json:
```json
{
    "body": "\n```diff\n\n- * Added the \"Special Update/Build Instructions\" section from SPKG.txt which\n-   was previously missing. \n+ * Added the \"Special Update/Build Instructions\" section to SPKG.txt which\n+   was previously missing, though currently no special steps are required.\n\n  * Added notes to SPKG.txt about an unnecessary ATLAS dependency in\n-   $SAGE_ROOT/spkg/standard/deps\n+   $SAGE_ROOT/spkg/standard/deps, and an explanation why GSL does *not*\n+   depend on ATLAS.\n\n- * Added notes to SPKG.txt about how ATLAS could in principle be used to \n-   improve the performance of some of GSL's functionality. \n\n- * Force GSL to be build with no optimisation if SAGE_DEBUG is set to \"yes\"\n+ * Force GSL to be built with no optimisation if SAGE_DEBUG is set to \"yes\"\n```\n\n(This snippet looks a bit funny, but one should be able to see what I've changed in addition.)",
    "created_at": "2010-07-20T23:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91813",
    "user": "leif"
}
```


```diff

- * Added the "Special Update/Build Instructions" section from SPKG.txt which
-   was previously missing. 
+ * Added the "Special Update/Build Instructions" section to SPKG.txt which
+   was previously missing, though currently no special steps are required.

  * Added notes to SPKG.txt about an unnecessary ATLAS dependency in
-   $SAGE_ROOT/spkg/standard/deps
+   $SAGE_ROOT/spkg/standard/deps, and an explanation why GSL does *not*
+   depend on ATLAS.

- * Added notes to SPKG.txt about how ATLAS could in principle be used to 
-   improve the performance of some of GSL's functionality. 

- * Force GSL to be build with no optimisation if SAGE_DEBUG is set to "yes"
+ * Force GSL to be built with no optimisation if SAGE_DEBUG is set to "yes"
```

(This snippet looks a bit funny, but one should be able to see what I've changed in addition.)



---

archive/issue_comments_091814.json:
```json
{
    "body": "Just found something else:\n\nThere should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.",
    "created_at": "2010-07-20T23:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91814",
    "user": "leif"
}
```

Just found something else:

There should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.



---

archive/issue_comments_091815.json:
```json
{
    "body": "Replying to [comment:38 leif]:\n> Just found something else:\n> \n> There should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.\n\nI disagree. Can you show me an example of how `[ -z $foobar ]` produces a syntax error, which can be solved by use of `[ -z \"$foobar\" ]`? I accept the quotes can do no harm, but I do not believe they are necessary. \n\nI need to go out soon - I look at the other changes later today. \n\nBTW, what was the result of your ptestlong? \n\nDave",
    "created_at": "2010-07-21T07:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91815",
    "user": "drkirkby"
}
```

Replying to [comment:38 leif]:
> Just found something else:
> 
> There should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.

I disagree. Can you show me an example of how `[ -z $foobar ]` produces a syntax error, which can be solved by use of `[ -z "$foobar" ]`? I accept the quotes can do no harm, but I do not believe they are necessary. 

I need to go out soon - I look at the other changes later today. 

BTW, what was the result of your ptestlong? 

Dave



---

archive/issue_comments_091816.json:
```json
{
    "body": "Attachment [9533-resolve-CFLAG64-and-SAGE_ROOT-issues.patch](tarball://root/attachments/some-uuid/ticket9533/9533-resolve-CFLAG64-and-SAGE_ROOT-issues.patch) by drkirkby created at 2010-07-21 11:19:56\n\nPut quotes around CFLAG64 and SPKG_ROOT and update SPKG.txt to reflect discoveries about ATLAS",
    "created_at": "2010-07-21T11:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91816",
    "user": "drkirkby"
}
```

Attachment [9533-resolve-CFLAG64-and-SAGE_ROOT-issues.patch](tarball://root/attachments/some-uuid/ticket9533/9533-resolve-CFLAG64-and-SAGE_ROOT-issues.patch) by drkirkby created at 2010-07-21 11:19:56

Put quotes around CFLAG64 and SPKG_ROOT and update SPKG.txt to reflect discoveries about ATLAS



---

archive/issue_comments_091817.json:
```json
{
    "body": "Replying to [comment:39 drkirkby]:\n> Replying to [comment:38 leif]:\n> > Just found something else:\n> > \n> > There should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.\n> \nI now accept you were right over this (someone else has [confirmed you were right on comp.unix.shell](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/8541f3ab19a1766b#)).  I've made what I think are all the changes you suggest now.\n\nThe package is at\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg\n\nIs that OK now? \n\nDave",
    "created_at": "2010-07-21T11:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91817",
    "user": "drkirkby"
}
```

Replying to [comment:39 drkirkby]:
> Replying to [comment:38 leif]:
> > Just found something else:
> > 
> > There should be quotes around the environment variables tested with `-z` (`$SAGE_LOCAL` and `$CFLAG64`) in both `spkg-check` and `spkg-install`, otherwise these tests could give syntax errors.
> 
I now accept you were right over this (someone else has [confirmed you were right on comp.unix.shell](http://groups.google.com/group/comp.unix.shell/browse_thread/thread/8541f3ab19a1766b#)).  I've made what I think are all the changes you suggest now.

The package is at

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

Is that OK now? 

Dave



---

archive/issue_comments_091818.json:
```json
{
    "body": "Well, this one:\n\n```\n * Added notes to SPKG.txt about how ATLAS could in principle be used to\n   improve the performance of some of GSL's functionality.\n```\n\nis still there, but never mind.\n\n## Note to the release managers\n\n**All patches here are to the spkg's repo, i.e. no patches have to be applied to the Sage library.**",
    "created_at": "2010-07-21T12:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91818",
    "user": "leif"
}
```

Well, this one:

```
 * Added notes to SPKG.txt about how ATLAS could in principle be used to
   improve the performance of some of GSL's functionality.
```

is still there, but never mind.

## Note to the release managers

**All patches here are to the spkg's repo, i.e. no patches have to be applied to the Sage library.**



---

archive/issue_comments_091819.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T12:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91819",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091820.json:
```json
{
    "body": "Replying to [comment:41 leif]:\n> Well, this one:\n> {{{\n>  * Added notes to SPKG.txt about how ATLAS could in principle be used to\n>    improve the performance of some of GSL's functionality.\n> }}}\n> is still there, but never mind.\n\nThank you for the positive review. \n\nI thought I might as well fix it, so just removed that from SPKG.txt. \n\nDave",
    "created_at": "2010-07-21T13:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91820",
    "user": "drkirkby"
}
```

Replying to [comment:41 leif]:
> Well, this one:
> {{{
>  * Added notes to SPKG.txt about how ATLAS could in principle be used to
>    improve the performance of some of GSL's functionality.
> }}}
> is still there, but never mind.

Thank you for the positive review. 

I thought I might as well fix it, so just removed that from SPKG.txt. 

Dave



---

archive/issue_comments_091821.json:
```json
{
    "body": "Attachment [remove-unnecessary-comment.patch](tarball://root/attachments/some-uuid/ticket9533/remove-unnecessary-comment.patch) by drkirkby created at 2010-07-21 13:17:12\n\nRemove a minor erro in the coments.",
    "created_at": "2010-07-21T13:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91821",
    "user": "drkirkby"
}
```

Attachment [remove-unnecessary-comment.patch](tarball://root/attachments/some-uuid/ticket9533/remove-unnecessary-comment.patch) by drkirkby created at 2010-07-21 13:17:12

Remove a minor erro in the coments.



---

archive/issue_comments_091822.json:
```json
{
    "body": "## Note to the release managers\n'''As Leif says above, all the patches here are in the package repository. Nothing is needed for the Sage library\n\nThe package can be found here.''' \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg",
    "created_at": "2010-07-21T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91822",
    "user": "drkirkby"
}
```

## Note to the release managers
'''As Leif says above, all the patches here are in the package repository. Nothing is needed for the Sage library

The package can be found here.''' 

http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg



---

archive/issue_comments_091823.json:
```json
{
    "body": "Replying to [comment:31 leif]:\n> Final `ptestlong` now running - will take nearly 4 hours...\n\nIn addition to the numerous tests by others above, I've successfully tested the new package with both Sage 4.5 and 4.5.1 on Ubuntu 9.04 x86 and x86_64, gcc 4.3.3 and gcc 4.5.0, by installing the package as well as building Sage from scratch with it. (All `ptestlong`s passed.)",
    "created_at": "2010-07-21T14:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91823",
    "user": "leif"
}
```

Replying to [comment:31 leif]:
> Final `ptestlong` now running - will take nearly 4 hours...

In addition to the numerous tests by others above, I've successfully tested the new package with both Sage 4.5 and 4.5.1 on Ubuntu 9.04 x86 and x86_64, gcc 4.3.3 and gcc 4.5.0, by installing the package as well as building Sage from scratch with it. (All `ptestlong`s passed.)



---

archive/issue_comments_091824.json:
```json
{
    "body": "## Note to the release managers\n\nPerhaps this is stating it too many times, but better too often than too rare. \n\nThe positively reviewed package can be found here.\n\n http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg\n\nNo changes are needed to the Sage library - you do **not** t need to apply any of the patches on this ticket - they are all in the repository for the .spkg.",
    "created_at": "2010-07-21T23:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91824",
    "user": "drkirkby"
}
```

## Note to the release managers

Perhaps this is stating it too many times, but better too often than too rare. 

The positively reviewed package can be found here.

 http://boxen.math.washington.edu/home/kirkby/patches/gsl-1.14.spkg

No changes are needed to the Sage library - you do **not** t need to apply any of the patches on this ticket - they are all in the repository for the .spkg.



---

archive/issue_comments_091825.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9533#issuecomment-91825",
    "user": "mpatel"
}
```

Resolution: fixed
