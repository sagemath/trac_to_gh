# Issue 9286: Add an spkg-check file for boehm_gc

Issue created by migration from https://trac.sagemath.org/ticket/9286

Original creator: drkirkby

Original creation time: 2010-06-20 21:41:54

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


---

Attachment

Mercurial patch to add an spkg-check to enable self-tests


---

Comment by drkirkby created at 2010-06-20 22:24:26

Here's the package, which will perform some self-tsts if SAGE_CHECK is exported to "yes"

http://boxen.math.washington.edu/home/kirkby/patches/boehm_gc-7.1.p6.spkg


---

Comment by iandrus created at 2010-06-24 03:09:16

Resolution: fixed


---

Comment by iandrus created at 2010-06-24 03:09:16

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

Comment by iandrus created at 2010-06-24 03:13:31

Resolution changed from fixed to 


---

Comment by iandrus created at 2010-06-24 03:13:31

Changing status from closed to new.


---

Comment by iandrus created at 2010-06-24 03:13:37

Changing status from new to needs_review.


---

Comment by iandrus created at 2010-06-24 03:14:05

Oops, I closed it instead of giving positive review.


---

Comment by iandrus created at 2010-06-24 03:14:05

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:52:39

Resolution: fixed
