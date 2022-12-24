# Issue 9286: Add an spkg-check file for boehm_gc

archive/issues_009286.json:
```json
{
    "body": "Assignee: tbd\n\nboehm_gc is one of many files in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to \"yes\", no self-tests of the package will be run. This is silly, as boehm_gc  has a test suite. \n\nAfter adding the required file, the test suite is run. This has been checked on OpenSolaris x64 in 64-bit mode and Solaris 10 SPARC in 32-bit mode. \n {{{\ncreating threadleaktest\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6/src'\nmake  check-TESTS\nmake[2]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6/src'\nCompleted 3 tests\nAllocated 4030601 collectable objects\nAllocated 306 uncollectable objects\nAllocated 2527886 atomic objects\nAllocated 34362 stubborn objects\nFinalized 6761/6761 objects - finalization is probably ok\nTotal number of bytes allocated is 227907342\nFinal heap size is 19632128 bytes\nCollector appears to work\nCompleted 106 collections\nPASS: gctest\nLeaked composite object at 4daec0 (tests/leak_test.c:19, sz=8, NORMAL)\n\nPASS: leaktest\nFinal heap size is 524288\nPASS: middletest\nGC_check_heap_block: found smashed heap objects:\n4e8fe8 in or near object at 4e8fc0(tests/smash_test.c:21, sz=40)\nGC_check_heap_block: found smashed heap objects:\n55bae8 in or near object at 55bac0(tests/smash_test.c:21, sz=40)\n4e8fe8 in or near object at 4e8fc0(tests/smash_test.c:21, sz=40)\nPASS: smashtest\nGC Warning: Out of Memory!  Returning NIL!\nGC Warning: Out of Memory!  Returning NIL!\nGC Warning: Out of Memory!  Returning NIL!\nPASS: hugetest\nLeaked composite object at 4daf80 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nLeaked composite object at start: 4daf90, appr. length: 48\nLeaked composite object at 4dae00 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nLeaked composite object at 4daef0 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nLeaked composite object at start: 4dae10, appr. length: 48\nLeaked composite object at 4dadd0 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nLeaked composite object at 4dae90 (tests/thread_leak_test.c:14, sz=4, NORMAL)\n\nPASS: threadleaktest\n==================\nAll 6 tests passed\n==================\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6/src'\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6/src'\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing boehm_gc-7.1.p6.spkg\n }}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/9286\n\n",
    "created_at": "2010-06-20T21:41:54Z",
    "labels": [
        "spkg-check",
        "minor",
        "bug"
    ],
    "title": "Add an spkg-check file for boehm_gc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9286",
    "user": "drkirkby"
}
```
Assignee: tbd

boehm_gc is one of many files in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to "yes", no self-tests of the package will be run. This is silly, as boehm_gc  has a test suite. 

After adding the required file, the test suite is run. This has been checked on OpenSolaris x64 in 64-bit mode and Solaris 10 SPARC in 32-bit mode. 
 {{{
creating threadleaktest
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6/src'
make  check-TESTS
make[2]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6/src'
Completed 3 tests
Allocated 4030601 collectable objects
Allocated 306 uncollectable objects
Allocated 2527886 atomic objects
Allocated 34362 stubborn objects
Finalized 6761/6761 objects - finalization is probably ok
Total number of bytes allocated is 227907342
Final heap size is 19632128 bytes
Collector appears to work
Completed 106 collections
PASS: gctest
Leaked composite object at 4daec0 (tests/leak_test.c:19, sz=8, NORMAL)

PASS: leaktest
Final heap size is 524288
PASS: middletest
GC_check_heap_block: found smashed heap objects:
4e8fe8 in or near object at 4e8fc0(tests/smash_test.c:21, sz=40)
GC_check_heap_block: found smashed heap objects:
55bae8 in or near object at 55bac0(tests/smash_test.c:21, sz=40)
4e8fe8 in or near object at 4e8fc0(tests/smash_test.c:21, sz=40)
PASS: smashtest
GC Warning: Out of Memory!  Returning NIL!
GC Warning: Out of Memory!  Returning NIL!
GC Warning: Out of Memory!  Returning NIL!
PASS: hugetest
Leaked composite object at 4daf80 (tests/thread_leak_test.c:14, sz=4, NORMAL)

Leaked composite object at start: 4daf90, appr. length: 48
Leaked composite object at 4dae00 (tests/thread_leak_test.c:14, sz=4, NORMAL)

Leaked composite object at 4daef0 (tests/thread_leak_test.c:14, sz=4, NORMAL)

Leaked composite object at start: 4dae10, appr. length: 48
Leaked composite object at 4dadd0 (tests/thread_leak_test.c:14, sz=4, NORMAL)

Leaked composite object at 4dae90 (tests/thread_leak_test.c:14, sz=4, NORMAL)

PASS: threadleaktest
==================
All 6 tests passed
==================
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6/src'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/boehm_gc-7.1.p6
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing boehm_gc-7.1.p6.spkg
 }}}

Issue created by migration from https://trac.sagemath.org/ticket/9286





---

archive/issue_comments_087462.json:
```json
{
    "body": "Attachment [9286.patch](tarball://root/attachments/some-uuid/ticket9286/9286.patch) by drkirkby created at 2010-06-20 21:49:36\n\nMercurial patch to add an spkg-check to enable self-tests",
    "created_at": "2010-06-20T21:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87462",
    "user": "drkirkby"
}
```

Attachment [9286.patch](tarball://root/attachments/some-uuid/ticket9286/9286.patch) by drkirkby created at 2010-06-20 21:49:36

Mercurial patch to add an spkg-check to enable self-tests



---

archive/issue_comments_087463.json:
```json
{
    "body": "Here's the package, which will perform some self-tsts if SAGE_CHECK is exported to \"yes\"\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/boehm_gc-7.1.p6.spkg",
    "created_at": "2010-06-20T22:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87463",
    "user": "drkirkby"
}
```

Here's the package, which will perform some self-tsts if SAGE_CHECK is exported to "yes"

http://boxen.math.washington.edu/home/kirkby/patches/boehm_gc-7.1.p6.spkg



---

archive/issue_comments_087464.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-24T03:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87464",
    "user": "iandrus"
}
```

Resolution: fixed



---

archive/issue_comments_087465.json:
```json
{
    "body": "I read the patch and I approve.  I ran\n\n```\nsage -i http://boxen.math.washington.edu/home/kirkby/patches/boehm_gc-7.1.p6.spkg\n```\n\nwhich did not run any tests, and then \n\n```\nSAGE_CHECK=yes sage -f -i http://boxen.math.washington.edu/home/kirkby/patches/boehm_gc-7.1.p6.spkg\n```\n\nwhich did.  All tests passed on \n\n```\nuname -a\nDarwin parduc.home 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386 i386\n```\n\n\nCongratulations, you are now the proud owner of a brand new Positive Review!",
    "created_at": "2010-06-24T03:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87465",
    "user": "iandrus"
}
```

I read the patch and I approve.  I ran

```
sage -i http://boxen.math.washington.edu/home/kirkby/patches/boehm_gc-7.1.p6.spkg
```

which did not run any tests, and then 

```
SAGE_CHECK=yes sage -f -i http://boxen.math.washington.edu/home/kirkby/patches/boehm_gc-7.1.p6.spkg
```

which did.  All tests passed on 

```
uname -a
Darwin parduc.home 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386 i386
```


Congratulations, you are now the proud owner of a brand new Positive Review!



---

archive/issue_comments_087466.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-06-24T03:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87466",
    "user": "iandrus"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_087467.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-06-24T03:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87467",
    "user": "iandrus"
}
```

Changing status from closed to new.



---

archive/issue_comments_087468.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-24T03:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87468",
    "user": "iandrus"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087469.json:
```json
{
    "body": "Oops, I closed it instead of giving positive review.",
    "created_at": "2010-06-24T03:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87469",
    "user": "iandrus"
}
```

Oops, I closed it instead of giving positive review.



---

archive/issue_comments_087470.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T03:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87470",
    "user": "iandrus"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9286#issuecomment-87471",
    "user": "rlm"
}
```

Resolution: fixed
