# Issue 8159: Updated Cython backend for mpmath

archive/issues_008159.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  burcin\n\nKeywords: mpmath\n\nThis update of sage.libs.mpmath, along with recent changes to mpmath itself and the patch in !#6199, results in a 3x overall speedup of mpmath (as measured by `mpmath.runtests()` performance). Elementary functions, hypergeometric series, and other \"low-level\" transcendental functions are not affected much, but functions that do a lot of arithmetic with mpf/mpc instances (examples: lambertw, polylog, bernpoly and many others; numerical summation, numerical integration, etc) can be 3x-10x faster. A similar speedup should be attainable in the future for the \"low-level\" functions by implementing those in Cython as well.\n\nThis extension works if site-packages/mpmath is replaced with an svn trunk checkout. There are essentially no tests in the Cython modules themselves; testing can be done with\n\n`import mpmath; mpmath.runtests(); mpmath.doctests()`\n\n(There is a very small number of doctests that fail due to numerical noise; this is nothing to worry about.)\n\nThis is not the final version of the code to be committed (it will synchronized with the next release of mpmath), but I'm uploading it to have a safe copy and for potential early review. I have not tested this on a 32-bit system. There could be some subtle overflow or memory leak issues that aren't caught by the tests.\n\nIt's not thread-safe due to the use of global state (which is used mostly because I was lazy, but it possibly also helps performance). I don't consider this a serious bug since vanilla-Python mpmath isn't fully thread-safe either. But it should be fixed some time in the future.\n\nI think a number of optimizations are possible, including optimizing MPF_normalize and caching MPF and mpf/mpc instances. I have also not updated the mpmath <-> Sage conversion code, which could be improved not to go via tuple values.\n\nSorry that it's not in the form of a patch (my current hg copy of Sage being dirty).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8159\n\n",
    "created_at": "2010-02-03T01:37:53Z",
    "labels": [
        "performance",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Updated Cython backend for mpmath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8159",
    "user": "fredrik.johansson"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/8159





---

archive/issue_comments_071754.json:
```json
{
    "body": "Attachment [mpmath_cython.tar.gz](tarball://root/attachments/some-uuid/ticket8159/mpmath_cython.tar.gz) by fredrik.johansson created at 2010-02-04 04:24:30\n\ncontains edited sage.libs.mpmath (update: old files removed)",
    "created_at": "2010-02-04T04:24:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71754",
    "user": "fredrik.johansson"
}
```

Attachment [mpmath_cython.tar.gz](tarball://root/attachments/some-uuid/ticket8159/mpmath_cython.tar.gz) by fredrik.johansson created at 2010-02-04 04:24:30

contains edited sage.libs.mpmath (update: old files removed)



---

archive/issue_comments_071755.json:
```json
{
    "body": "Here is an\u00a0[0.14 spkg](http://boxen.math.washington.edu/home/schilly/sage/spkg/)",
    "created_at": "2010-02-04T11:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71755",
    "user": "schilly"
}
```

Here is an [0.14 spkg](http://boxen.math.washington.edu/home/schilly/sage/spkg/)



---

archive/issue_comments_071756.json:
```json
{
    "body": "Attachment [mpmath_cython.patch](tarball://root/attachments/some-uuid/ticket8159/mpmath_cython.patch) by fredrik.johansson created at 2010-02-04 18:01:46",
    "created_at": "2010-02-04T18:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71756",
    "user": "fredrik.johansson"
}
```

Attachment [mpmath_cython.patch](tarball://root/attachments/some-uuid/ticket8159/mpmath_cython.patch) by fredrik.johansson created at 2010-02-04 18:01:46



---

archive/issue_comments_071757.json:
```json
{
    "body": "Patch uploaded; let's see if it works.\n\nSlightly updated spkg (still might make some minor changes before making it 0.14 final): !http://boxen.math.washington.edu/home/fredrik/spkg/mpmath-0.14.spkg",
    "created_at": "2010-02-04T18:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71757",
    "user": "fredrik.johansson"
}
```

Patch uploaded; let's see if it works.

Slightly updated spkg (still might make some minor changes before making it 0.14 final): !http://boxen.math.washington.edu/home/fredrik/spkg/mpmath-0.14.spkg



---

archive/issue_comments_071758.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-04T19:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71758",
    "user": "schilly"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_071759.json:
```json
{
    "body": "Hi, I applied the patch and installed your spkg. works + your tests pass.\n\nI also tried the patch+spkg on 4.3.2.rc0 ... and it worked! all tests+your doctests pass here too! I also doctested the entire sage library, but there were some complaints.\n\nTherefore positive review for the spkg from me, but others should test it on other platforms, too. Negative for the implications on the sage library because doctests fail on 4.3.1 and 4.3.2.rc0 /w mpmath 0.14 and above patch in\n`sage/libs/mpmath/utils.pyx` and `/sage/functions/transcendental.py`\nall say:\n\n```\nImportError: No module named mptypes\n```\n\nThis exception pops up about 20 times ...",
    "created_at": "2010-02-04T19:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71759",
    "user": "schilly"
}
```

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

archive/issue_comments_071760.json:
```json
{
    "body": "Attachment [importfix.patch](tarball://root/attachments/some-uuid/ticket8159/importfix.patch) by fredrik.johansson created at 2010-02-04 20:01:58\n\nAttached a fix for the ImportError.",
    "created_at": "2010-02-04T20:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71760",
    "user": "fredrik.johansson"
}
```

Attachment [importfix.patch](tarball://root/attachments/some-uuid/ticket8159/importfix.patch) by fredrik.johansson created at 2010-02-04 20:01:58

Attached a fix for the ImportError.



---

archive/issue_comments_071761.json:
```json
{
    "body": "That was easy, all tests pass ... green light from me!\n\nI'm setting this to needs_review, and start with a positiv review from me.",
    "created_at": "2010-02-04T20:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71761",
    "user": "schilly"
}
```

That was easy, all tests pass ... green light from me!

I'm setting this to needs_review, and start with a positiv review from me.



---

archive/issue_comments_071762.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-04T20:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71762",
    "user": "schilly"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071763.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T11:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71763",
    "user": "schilly"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071764.json:
```json
{
    "body": "Just a reminder: the spkg should be updated to the actual 0.14 release version.",
    "created_at": "2010-02-09T14:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71764",
    "user": "fredrik.johansson"
}
```

Just a reminder: the spkg should be updated to the actual 0.14 release version.



---

archive/issue_comments_071765.json:
```json
{
    "body": "Where is the new spkg? \u00a0It does not seem to be\u00a0[here](http://boxen.math.washington.edu/home/schilly/sage/spkg/).",
    "created_at": "2010-02-10T15:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71765",
    "user": "mpatel"
}
```

Where is the new spkg?  It does not seem to be [here](http://boxen.math.washington.edu/home/schilly/sage/spkg/).



---

archive/issue_comments_071766.json:
```json
{
    "body": "I don't know, there seems there was a misunderstanding. I've build a new 0.14 spkg with the actual 0.14 release.",
    "created_at": "2010-02-20T18:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71766",
    "user": "schilly"
}
```

I don't know, there seems there was a misunderstanding. I've build a new 0.14 spkg with the actual 0.14 release.



---

archive/issue_comments_071767.json:
```json
{
    "body": "I've tested this once again with 4.3.3 and it's still working and my positive review is still valid.",
    "created_at": "2010-02-26T23:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71767",
    "user": "schilly"
}
```

I've tested this once again with 4.3.3 and it's still working and my positive review is still valid.



---

archive/issue_comments_071768.json:
```json
{
    "body": "dear release manager. to get this done, merge the mpmath_cython.patch and the importfix.patch patch. after that get the updated spkg from [here](http://boxen.math.washington.edu/home/schilly/sage/spkg/) and that's it ;)",
    "created_at": "2010-03-01T22:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71768",
    "user": "schilly"
}
```

dear release manager. to get this done, merge the mpmath_cython.patch and the importfix.patch patch. after that get the updated spkg from [here](http://boxen.math.washington.edu/home/schilly/sage/spkg/) and that's it ;)



---

archive/issue_comments_071769.json:
```json
{
    "body": "Harald's mpmath spkg has some changes that are not yet checked in:\n\n```sh\n[mvngu@sage mpmath-0.14]$ hg diff\ndiff -r fa9536e74343 SPKG.txt\n--- a/SPKG.txt\n+++ b/SPKG.txt\n@@ -21,6 +21,9 @@\n \n == Changelog ==\n \n+=== mpmath-0.14 (Harald Schilly, Feb 20th, 2010) ===\n+ * updated to mpmath-0.14.\n+\n === mpmath-0.13 (Fredrik Johansson, August 14th, 2009) ===\n  * Updated to mpmath-0.13.\n```\n\nI have committed these changes in his name and uploaded the resulting spkg to\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/mpmath/mpmath-0.14.spkg",
    "created_at": "2010-03-02T13:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71769",
    "user": "mvngu"
}
```

Harald's mpmath spkg has some changes that are not yet checked in:

```sh
[mvngu@sage mpmath-0.14]$ hg diff
diff -r fa9536e74343 SPKG.txt
--- a/SPKG.txt
+++ b/SPKG.txt
@@ -21,6 +21,9 @@
 
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

archive/issue_comments_071770.json:
```json
{
    "body": "Merged in this order:\n\n1. [mpmath_cython.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8159/mpmath_cython.patch)\n2. [importfix.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8159/importfix.patch)\n3. Merged [mpmath-0.14.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/mpmath/mpmath-0.14.spkg) in the standard spkg repository.",
    "created_at": "2010-03-03T00:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71770",
    "user": "mvngu"
}
```

Merged in this order:

1. [mpmath_cython.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8159/mpmath_cython.patch)
2. [importfix.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8159/importfix.patch)
3. Merged [mpmath-0.14.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/mpmath/mpmath-0.14.spkg) in the standard spkg repository.



---

archive/issue_comments_071771.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T00:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71771",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071772.json:
```json
{
    "body": "Harald, Minh, thanks a lot!",
    "created_at": "2010-03-03T17:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8159#issuecomment-71772",
    "user": "fredrik.johansson"
}
```

Harald, Minh, thanks a lot!
