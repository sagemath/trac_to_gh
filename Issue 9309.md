# Issue 9309: Add an spkg-check file for the IML library

archive/issues_009309.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime @jhpalmieri @peterjeremy\n\nThe IML library is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to \"yes\", no self-tests of the package will be run. This is silly, as the IML library has a test suite, though it only consists of two tests. \n\nAfter adding the required file, the test suite is run. \n\n\n```\ncreating test-largeentry\nPASS: test-smallentry\nPASS: test-largeentry\n==================\nAll 2 tests passed\n==================\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/tests'\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/tests'\nMaking check in examples\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/examples'\nmake[1]: Nothing to be done for `check'.\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/examples'\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src'\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src'\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing iml-1.0.1.p13.spkg\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9309\n\n",
    "created_at": "2010-06-22T14:41:47Z",
    "labels": [
        "spkg-check",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Add an spkg-check file for the IML library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9309",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  @nexttime @jhpalmieri @peterjeremy

The IML library is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to "yes", no self-tests of the package will be run. This is silly, as the IML library has a test suite, though it only consists of two tests. 

After adding the required file, the test suite is run. 


```
creating test-largeentry
PASS: test-smallentry
PASS: test-largeentry
==================
All 2 tests passed
==================
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/tests'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/tests'
Making check in examples
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/examples'
make[1]: Nothing to be done for `check'.
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src/examples'
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13/src'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/iml-1.0.1.p13
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing iml-1.0.1.p13.spkg
```


Issue created by migration from https://trac.sagemath.org/ticket/9309





---

archive/issue_comments_087661.json:
```json
{
    "body": "Attachment [9309.patch](tarball://root/attachments/some-uuid/ticket9309/9309.patch) by drkirkby created at 2010-06-22 14:59:00\n\nMercurial patch to add an spkg-check file to enable self-tests",
    "created_at": "2010-06-22T14:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87661",
    "user": "drkirkby"
}
```

Attachment [9309.patch](tarball://root/attachments/some-uuid/ticket9309/9309.patch) by drkirkby created at 2010-06-22 14:59:00

Mercurial patch to add an spkg-check file to enable self-tests



---

archive/issue_comments_087662.json:
```json
{
    "body": "The package can be found here\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg",
    "created_at": "2010-06-22T14:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87662",
    "user": "drkirkby"
}
```

The package can be found here

http://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg



---

archive/issue_comments_087663.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-22T14:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87663",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087664.json:
```json
{
    "body": "Since you three tend to take quality quite seriously, I'll cc you!\n\nDave",
    "created_at": "2010-07-16T15:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87664",
    "user": "drkirkby"
}
```

Since you three tend to take quality quite seriously, I'll cc you!

Dave



---

archive/issue_comments_087665.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T16:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87665",
    "user": "@malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087666.json:
```json
{
    "body": "The patch looks okay. I also tested in on sage.math.",
    "created_at": "2010-07-21T16:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87666",
    "user": "@malb"
}
```

The patch looks okay. I also tested in on sage.math.



---

archive/issue_comments_087667.json:
```json
{
    "body": "(Dave:) Shouldn't we improve this spkg like we did with the new GSL one (at #9533)? (I must admit I haven't yet looked at its `spkg-install`. If you don't want to spend further time on it, I could do it, say, until this weekend. Then you'd have to review it - or Martin again...)\n\nI would at least add a message reporting that the test suite passed, and append to `CFLAGS` et al. rather than overwrite them (if `SAGE64=yes`).",
    "created_at": "2010-07-21T16:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87667",
    "user": "@nexttime"
}
```

(Dave:) Shouldn't we improve this spkg like we did with the new GSL one (at #9533)? (I must admit I haven't yet looked at its `spkg-install`. If you don't want to spend further time on it, I could do it, say, until this weekend. Then you'd have to review it - or Martin again...)

I would at least add a message reporting that the test suite passed, and append to `CFLAGS` et al. rather than overwrite them (if `SAGE64=yes`).



---

archive/issue_comments_087668.json:
```json
{
    "body": "Replying to [comment:4 leif]:\n> (Dave:) Shouldn't we improve this spkg like we did with the new GSL one (at #9533)? [...]\n\nObviously this would be out of the ticket's current scope, so we could equally well open a new one for that purpose instead.",
    "created_at": "2010-07-21T16:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87668",
    "user": "@nexttime"
}
```

Replying to [comment:4 leif]:
> (Dave:) Shouldn't we improve this spkg like we did with the new GSL one (at #9533)? [...]

Obviously this would be out of the ticket's current scope, so we could equally well open a new one for that purpose instead.



---

archive/issue_comments_087669.json:
```json
{
    "body": "At least [IML's home page](http://www.cs.uwaterloo.ca/~astorjoh/iml.html) has moved (the one in `SPKG.txt` gives a 404). From there:\n\n  What is New?\n\n* 2008-07-28 The current release is 1.0.3. This version incorporates a new function nullspaceMP into the library interface which computes the right nullspace of an integer matrix filled with GMP bignums.\n \n* 2007-09-14 The current release is 1.0.2. This version corrects several bugs.\n\n* 2006-11-26 The current release is 1.0.1. This version corrects several bugs as well as incorporates a new function nullspaceLong into the library interface which computes the right nullspace of an integer matrix with type long.\n\n  [...]\n\nSo perhaps really worth a follow-up ticket... (But we should update the address in `SPKG.txt` *here* I think.)\n\nMartin, what do *you* think?",
    "created_at": "2010-07-21T17:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87669",
    "user": "@nexttime"
}
```

At least [IML's home page](http://www.cs.uwaterloo.ca/~astorjoh/iml.html) has moved (the one in `SPKG.txt` gives a 404). From there:

  What is New?

* 2008-07-28 The current release is 1.0.3. This version incorporates a new function nullspaceMP into the library interface which computes the right nullspace of an integer matrix filled with GMP bignums.
 
* 2007-09-14 The current release is 1.0.2. This version corrects several bugs.

* 2006-11-26 The current release is 1.0.1. This version corrects several bugs as well as incorporates a new function nullspaceLong into the library interface which computes the right nullspace of an integer matrix with type long.

  [...]

So perhaps really worth a follow-up ticket... (But we should update the address in `SPKG.txt` *here* I think.)

Martin, what do *you* think?



---

archive/issue_comments_087670.json:
```json
{
    "body": "Sure, let's do both: update SPKG.txt here and then update to the newest upstream release in a different package.",
    "created_at": "2010-07-21T17:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87670",
    "user": "@malb"
}
```

Sure, let's do both: update SPKG.txt here and then update to the newest upstream release in a different package.



---

archive/issue_comments_087671.json:
```json
{
    "body": "Only updates upstream info in SPKG.txt",
    "created_at": "2010-07-21T17:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87671",
    "user": "@nexttime"
}
```

Only updates upstream info in SPKG.txt



---

archive/issue_comments_087672.json:
```json
{
    "body": "Attachment [trac_9309-IML-SPKG.txt_update.patch](tarball://root/attachments/some-uuid/ticket9309/trac_9309-IML-SPKG.txt_update.patch) by @nexttime created at 2010-07-21 17:51:04\n\nDave, can you merge my patch to `SPKG.txt`?",
    "created_at": "2010-07-21T17:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87672",
    "user": "@nexttime"
}
```

Attachment [trac_9309-IML-SPKG.txt_update.patch](tarball://root/attachments/some-uuid/ticket9309/trac_9309-IML-SPKG.txt_update.patch) by @nexttime created at 2010-07-21 17:51:04

Dave, can you merge my patch to `SPKG.txt`?



---

archive/issue_comments_087673.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> Dave, can you merge my patch to `SPKG.txt`?\n\nLeif, \n\nI copied your changes to SPKG.txt to the package at: \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg\n\nI also created #9568 to update the IML library, and improve spkg-install. We should also consider whether that can be built in parallel. Anyway, leave any comments on #9568. \n\n == Note to the release managers == \n\nNo patches need to be applied to any other Sage repositories - all changes are merged into the repository. Just replace the current IML package with this one.\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg\n\nDave",
    "created_at": "2010-07-21T22:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87673",
    "user": "drkirkby"
}
```

Replying to [comment:8 leif]:
> Dave, can you merge my patch to `SPKG.txt`?

Leif, 

I copied your changes to SPKG.txt to the package at: 

http://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg

I also created #9568 to update the IML library, and improve spkg-install. We should also consider whether that can be built in parallel. Anyway, leave any comments on #9568. 

 == Note to the release managers == 

No patches need to be applied to any other Sage repositories - all changes are merged into the repository. Just replace the current IML package with this one.

http://boxen.math.washington.edu/home/kirkby/patches/iml-1.0.1.p13.spkg

Dave



---

archive/issue_comments_087674.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9309#issuecomment-87674",
    "user": "@qed777"
}
```

Resolution: fixed
