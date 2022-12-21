# Issue 8159: Updated Cython backend for mpmath

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2010-02-03 01:37:53

Assignee: tbd

CC:  burcin

Keywords: mpmath

This update of sage.libs.mpmath, along with recent changes to mpmath itself and the patch in !#6199, results in a 3x overall speedup of mpmath (as measured by `mpmath.runtests()` performance). Elementary functions, hypergeometric series, and other "low-level" transcendental functions are not affected much, but functions that do a lot of arithmetic with mpf/mpc instances (examples: lambertw, polylog, bernpoly and many others; numerical summation, numerical integration, etc) can be 3x-10x faster. A similar speedup should be attainable in the future for the "low-level" functions by implementing those in Cython as well.

This extension works if site-packages/mpmath is replaced with an svn trunk checkout. There are essentially no tests in the Cython modules themselves; testing can be done with

`import mpmath; mpmath.runtests(); mpmath.doctests()`

(There is a very small number of doctests that fail due to numerical noise; this is nothing to worry about.)

This is not the final version of the code to be committed (it will synchronized with the next release of mpmath), but I'm uploading it to have a safe copy and for potential early review. I have not tested this on a 32-bit system. There could be some subtle overflow or memory leak issues that aren't caught by the tests.

It's not thread-safe due to the use of global state (which is used mostly because I was lazy, but it possibly also helps performance). I don't consider this a serious bug since vanilla-Python mpmath isn't fully thread-safe either. But it should be fixed some time in the future.

I think a number of optimizations are possible, including optimizing MPF_normalize and caching MPF and mpf/mpc instances. I have also not updated the mpmath <-> Sage conversion code, which could be improved not to go via tuple values.

Sorry that it's not in the form of a patch (my current hg copy of Sage being dirty).


---

Attachment

contains edited sage.libs.mpmath (update: old files removed)


---

Comment by schilly created at 2010-02-04 11:32:32

Here is an [0.14 spkg](http://boxen.math.washington.edu/home/schilly/sage/spkg/)


---

Attachment


---

Comment by fredrik.johansson created at 2010-02-04 18:05:14

Patch uploaded; let's see if it works.

Slightly updated spkg (still might make some minor changes before making it 0.14 final): !http://boxen.math.washington.edu/home/fredrik/spkg/mpmath-0.14.spkg


---

Comment by schilly created at 2010-02-04 19:35:22

Changing status from new to needs_work.


---

Comment by schilly created at 2010-02-04 19:35:22

Hi, I applied the patch and installed your spkg. works + your tests pass.

I also tried the patch+spkg on 4.3.2.rc0 ... and it worked! all tests+your doctests pass here too! I also doctested the entire sage library, but there were some complaints.

Therefore positive review for the spkg from me, but others should test it on other platforms, too. Negative for the implications on the sage library because doctests fail on 4.3.1 and 4.3.2.rc0 /w mpmath 0.14 and above patch in
`sage/libs/mpmath/utils.pyx` and `/sage/functions/transcendental.py`
all say:

```
ImportError: No module named mptypes
```

This exception pops up about 20 times ...


---

Attachment

Attached a fix for the ImportError.


---

Comment by schilly created at 2010-02-04 20:11:11

That was easy, all tests pass ... green light from me!

I'm setting this to needs_review, and start with a positiv review from me.


---

Comment by schilly created at 2010-02-04 20:11:11

Changing status from needs_work to needs_review.


---

Comment by schilly created at 2010-02-07 11:01:37

Changing status from needs_review to positive_review.


---

Comment by fredrik.johansson created at 2010-02-09 14:31:12

Just a reminder: the spkg should be updated to the actual 0.14 release version.


---

Comment by mpatel created at 2010-02-10 15:37:31

Where is the new spkg?  It does not seem to be [here](http://boxen.math.washington.edu/home/schilly/sage/spkg/).


---

Comment by schilly created at 2010-02-20 18:07:09

I don't know, there seems there was a misunderstanding. I've build a new 0.14 spkg with the actual 0.14 release.


---

Comment by schilly created at 2010-02-26 23:22:00

I've tested this once again with 4.3.3 and it's still working and my positive review is still valid.


---

Comment by schilly created at 2010-03-01 22:02:26

dear release manager. to get this done, merge the mpmath_cython.patch and the importfix.patch patch. after that get the updated spkg from [here](http://boxen.math.washington.edu/home/schilly/sage/spkg/) and that's it ;)


---

Comment by mvngu created at 2010-03-02 13:57:09

Harald's mpmath spkg has some changes that are not yet checked in:

```sh
[mvngu`@`sage mpmath-0.14]$ hg diff
diff -r fa9536e74343 SPKG.txt
--- a/SPKG.txt
+++ b/SPKG.txt
`@``@` -21,6 +21,9 `@``@`
 
 == Changelog ==
 
+=== mpmath-0.14 (Harald Schilly, Feb 20th, 2010) ===
+ * updated to mpmath-0.14.
+
 === mpmath-0.13 (Fredrik Johansson, August 14th, 2009) ===
  * Updated to mpmath-0.13.
```

I have committed these changes in his name and uploaded the resulting spkg to

http://sage.math.washington.edu/home/mvngu/spkg/standard/mpmath/mpmath-0.14.spkg


---

Comment by mvngu created at 2010-03-03 00:48:11

Merged in this order:

 1. [mpmath_cython.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8159/mpmath_cython.patch)
 1. [importfix.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8159/importfix.patch)
 1. Merged [mpmath-0.14.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/mpmath/mpmath-0.14.spkg) in the standard spkg repository.


---

Comment by mvngu created at 2010-03-03 00:48:11

Resolution: fixed


---

Comment by fredrik.johansson created at 2010-03-03 17:22:13

Harald, Minh, thanks a lot!
