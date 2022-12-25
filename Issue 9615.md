# Issue 9615: doctest failures with lcalc functions in 4.5.2.alpha1

archive/issues_009615.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  bober @craigcitro @JohnCremona mrubinst@math.uwaterloo.ca @qed777 mvngu @rishikesha ylchapuy @rbeezer\n\nKeywords: lcalc\n\nDoctest failures in alpha1: https://groups.google.com/group/sage-release/msg/8807ed7073c6793f :\n\n```\nFile \"/scratch/scratch/schilly/sage/sage-4.5.2.alpha1/devel/sage/sage/\nlibs/lcalc/lcalc_Lfunction.pyx\", line 780:\n    sage: L.value(0.5)\nExpected:\n    0\nGot:\n    -1.28235854574334e-17\n----------------------------------------------- \n```\n\nThis is related to #5396.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9615\n\n",
    "created_at": "2010-07-28T02:41:49Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "doctest failures with lcalc functions in 4.5.2.alpha1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9615",
    "user": "https://github.com/dandrake"
}
```
Assignee: mvngu

CC:  bober @craigcitro @JohnCremona mrubinst@math.uwaterloo.ca @qed777 mvngu @rishikesha ylchapuy @rbeezer

Keywords: lcalc

Doctest failures in alpha1: https://groups.google.com/group/sage-release/msg/8807ed7073c6793f :

```
File "/scratch/scratch/schilly/sage/sage-4.5.2.alpha1/devel/sage/sage/
libs/lcalc/lcalc_Lfunction.pyx", line 780:
    sage: L.value(0.5)
Expected:
    0
Got:
    -1.28235854574334e-17
----------------------------------------------- 
```

This is related to #5396.



Issue created by migration from https://trac.sagemath.org/ticket/9615





---

archive/issue_comments_092952.json:
```json
{
    "body": "Just for the record: I get exactly the same number with\n* Ubuntu 7.10 x86, Pentium 4 (Northwood), gcc 4.2.1\n* Ubuntu 9.04 x86, Pentium 4 Prescott, gcc 4.3.3\n\nFrom sage-release:\n\n  ''There is one numerical noise from #5396 ticket.  I will write a patch\n  which tests that L.value(0.5).abs() is less than 1e-14, instead of\n  current value of 0.''\n\n\n  ''The long messages giving out some data about L  function are from a\n  test function in lcalc library. It is helpful in testing. It just\n  prints out to standard output. Please ignore them.''\n\n  *Rishi*",
    "created_at": "2010-07-28T02:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92952",
    "user": "https://github.com/nexttime"
}
```

Just for the record: I get exactly the same number with
* Ubuntu 7.10 x86, Pentium 4 (Northwood), gcc 4.2.1
* Ubuntu 9.04 x86, Pentium 4 Prescott, gcc 4.3.3

From sage-release:

  ''There is one numerical noise from #5396 ticket.  I will write a patch
  which tests that L.value(0.5).abs() is less than 1e-14, instead of
  current value of 0.''


  ''The long messages giving out some data about L  function are from a
  test function in lcalc library. It is helpful in testing. It just
  prints out to standard output. Please ignore them.''

  *Rishi*



---

archive/issue_comments_092953.json:
```json
{
    "body": "Attachment [9615.patch](tarball://root/attachments/some-uuid/ticket9615/9615.patch) by @rishikesha created at 2010-07-28 12:00:01",
    "created_at": "2010-07-28T12:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92953",
    "user": "https://github.com/rishikesha"
}
```

Attachment [9615.patch](tarball://root/attachments/some-uuid/ticket9615/9615.patch) by @rishikesha created at 2010-07-28 12:00:01



---

archive/issue_comments_092954.json:
```json
{
    "body": "I did not check my email before creating a duplicate ticket and submitting a patch. Please close #9624",
    "created_at": "2010-07-28T12:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92954",
    "user": "https://github.com/rishikesha"
}
```

I did not check my email before creating a duplicate ticket and submitting a patch. Please close #9624



---

archive/issue_comments_092955.json:
```json
{
    "body": "Changing assignee from mvngu to @rishikesha.",
    "created_at": "2010-07-28T12:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92955",
    "user": "https://github.com/rishikesha"
}
```

Changing assignee from mvngu to @rishikesha.



---

archive/issue_comments_092956.json:
```json
{
    "body": "I'm changing the status to `needs_review`.  Is that OK?\n\nAlso, if I don't do it, someone should prepend the ticket number in the patch commit string.",
    "created_at": "2010-07-28T22:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92956",
    "user": "https://github.com/qed777"
}
```

I'm changing the status to `needs_review`.  Is that OK?

Also, if I don't do it, someone should prepend the ticket number in the patch commit string.



---

archive/issue_comments_092957.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T22:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92957",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092958.json:
```json
{
    "body": "Attachment [9615.2.patch](tarball://root/attachments/some-uuid/ticket9615/9615.2.patch) by @qed777 created at 2010-07-28 23:08:06\n\nTicket number and somewhat more general comment in commit string.  Apply only this patch.",
    "created_at": "2010-07-28T23:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92958",
    "user": "https://github.com/qed777"
}
```

Attachment [9615.2.patch](tarball://root/attachments/some-uuid/ticket9615/9615.2.patch) by @qed777 created at 2010-07-28 23:08:06

Ticket number and somewhat more general comment in commit string.  Apply only this patch.



---

archive/issue_comments_092959.json:
```json
{
    "body": "The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.\n\nOne question, though: is lcalc expected to return precisely zero, or a \"noisy zero\"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. \n\nIf this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)",
    "created_at": "2010-07-29T00:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92959",
    "user": "https://github.com/dandrake"
}
```

The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.

One question, though: is lcalc expected to return precisely zero, or a "noisy zero"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. 

If this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)



---

archive/issue_comments_092960.json:
```json
{
    "body": "Replying to [comment:5 ddrake]:\n> [...] It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. \n> \n> If this kind of behavior is expected on 32-bit versus 64-bit machines, [...]\n\nI can only imagine this is related to (unintentionally) different [default] rounding modes on different processors.\n\nSo this patch fixes the failing doctest (which is IMHO ok for the moment), but doesn't address its reason.\n\nUnless the involved `abs()` (or `<`) is somehow broken, I can give this a positive review without applying the patch and actually testing it... ;-)",
    "created_at": "2010-07-29T01:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92960",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:5 ddrake]:
> [...] It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. 
> 
> If this kind of behavior is expected on 32-bit versus 64-bit machines, [...]

I can only imagine this is related to (unintentionally) different [default] rounding modes on different processors.

So this patch fixes the failing doctest (which is IMHO ok for the moment), but doesn't address its reason.

Unless the involved `abs()` (or `<`) is somehow broken, I can give this a positive review without applying the patch and actually testing it... ;-)



---

archive/issue_comments_092961.json:
```json
{
    "body": "The patched doctest lacks an explanation/reference back to this ticket, which I think would be appropriate in this case.\n\nNot surprisingly passes all (long) tests in `sage/libs/lcalc/` on Ubuntu 9.04 x86 (Pentium 4 Prescott, gcc 4.3.3), where the doctest previously failed.\n\nI remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).",
    "created_at": "2010-07-29T02:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92961",
    "user": "https://github.com/nexttime"
}
```

The patched doctest lacks an explanation/reference back to this ticket, which I think would be appropriate in this case.

Not surprisingly passes all (long) tests in `sage/libs/lcalc/` on Ubuntu 9.04 x86 (Pentium 4 Prescott, gcc 4.3.3), where the doctest previously failed.

I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).



---

archive/issue_comments_092962.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).\n\n    \n  ''[...] On 32-bit Ubuntu 10.04 on Pentium M I get the same results as Harald,\n  though the non-zero value in the lcalc test is slightly different (~e-18). [...]''\n  \n  *Rob*\n\nRob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)",
    "created_at": "2010-07-29T02:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92962",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:7 leif]:
> I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).

    
  ''[...] On 32-bit Ubuntu 10.04 on Pentium M I get the same results as Harald,
  though the non-zero value in the lcalc test is slightly different (~e-18). [...]''
  
  *Rob*

Rob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)



---

archive/issue_comments_092963.json:
```json
{
    "body": "In lcalc, the function being tested returns a complex number (double precision). It is probably the way different processors do the computations, that the doctest failures are occurring. The earlier doctest passed on all the machines I have access to. \n\nThe calculation of L-function is pretty involved, you can see the papers which are referred to in the patch in #5396. \n\nReplying to [comment:5 ddrake]:\n> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.\n> \n> One question, though: is lcalc expected to return precisely zero, or a \"noisy zero\"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. \n> \n> If this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)",
    "created_at": "2010-07-29T03:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92963",
    "user": "https://github.com/rishikesha"
}
```

In lcalc, the function being tested returns a complex number (double precision). It is probably the way different processors do the computations, that the doctest failures are occurring. The earlier doctest passed on all the machines I have access to. 

The calculation of L-function is pretty involved, you can see the papers which are referred to in the patch in #5396. 

Replying to [comment:5 ddrake]:
> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.
> 
> One question, though: is lcalc expected to return precisely zero, or a "noisy zero"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. 
> 
> If this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)



---

archive/issue_comments_092964.json:
```json
{
    "body": "Same 32-bit system as before, applied \".2\" patch.  Then\n\n\n```\nsage -t -long \"devel/sage-main/sage/libs/lcalc/lcalc_Lfunction.pyx\"\n\t [3.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3.3 seconds\n```\n\n\nReplying to [comment:8 leif]:\n> Replying to [comment:7 leif]:\n> > I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).\n> \n>     \n>   ''[...] On 32-bit Ubuntu 10.04 on Pentium M I get the same results as Harald,\n>   though the non-zero value in the lcalc test is slightly different (~e-18). [...]''\n>   \n>   *Rob*\n> \n> Rob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)",
    "created_at": "2010-07-29T03:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92964",
    "user": "https://github.com/rbeezer"
}
```

Same 32-bit system as before, applied ".2" patch.  Then


```
sage -t -long "devel/sage-main/sage/libs/lcalc/lcalc_Lfunction.pyx"
	 [3.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.3 seconds
```


Replying to [comment:8 leif]:
> Replying to [comment:7 leif]:
> > I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).
> 
>     
>   ''[...] On 32-bit Ubuntu 10.04 on Pentium M I get the same results as Harald,
>   though the non-zero value in the lcalc test is slightly different (~e-18). [...]''
>   
>   *Rob*
> 
> Rob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)



---

archive/issue_comments_092965.json:
```json
{
    "body": "Replying to [comment:5 ddrake]:\n> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.\n\nFor what it's worth, it also fixes it on two different skynet machines which had the failure: cicero (x86-Linux-pentium4-fc) and iras (ia64-Linux-suse).",
    "created_at": "2010-07-29T04:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92965",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:5 ddrake]:
> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.

For what it's worth, it also fixes it on two different skynet machines which had the failure: cicero (x86-Linux-pentium4-fc) and iras (ia64-Linux-suse).



---

archive/issue_comments_092966.json:
```json
{
    "body": "Add a note with the ticket number.  Apply on top of [attachment:9615.2.patch]",
    "created_at": "2010-07-29T05:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92966",
    "user": "https://github.com/qed777"
}
```

Add a note with the ticket number.  Apply on top of [attachment:9615.2.patch]



---

archive/issue_comments_092967.json:
```json
{
    "body": "Attachment [trac_9615-lcalc_doctest_note.patch](tarball://root/attachments/some-uuid/ticket9615/trac_9615-lcalc_doctest_note.patch) by @qed777 created at 2010-07-29 05:56:50\n\nUnless anyone objects, I'm changing the status to *positive_review* and merging\n\n* [attachment:9615.2.patch]\n* [attachment:trac_9615-lcalc_doctest_note.patch]\n\nin 4.5.2.rc0.  The latter, which someone should review, follows up on [comment:7 Leif's suggestion].  Or should I exclude it?",
    "created_at": "2010-07-29T05:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92967",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9615-lcalc_doctest_note.patch](tarball://root/attachments/some-uuid/ticket9615/trac_9615-lcalc_doctest_note.patch) by @qed777 created at 2010-07-29 05:56:50

Unless anyone objects, I'm changing the status to *positive_review* and merging

* [attachment:9615.2.patch]
* [attachment:trac_9615-lcalc_doctest_note.patch]

in 4.5.2.rc0.  The latter, which someone should review, follows up on [comment:7 Leif's suggestion].  Or should I exclude it?



---

archive/issue_comments_092968.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-29T05:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92968",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092969.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-29T05:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92969",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_092970.json:
```json
{
    "body": "Replying to [comment:11 jhpalmieri]:\n> Replying to [comment:5 ddrake]:\n> > The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.\n> \n> For what it's worth, it also fixes it on two different skynet machines which had the failure: cicero (x86-Linux-pentium4-fc) and iras (ia64-Linux-suse).\n\nDoes iras default to 32-bit builds? (I only know it's running a 64-bit SuSE.)\n\nI ask this because Harald also saw this doctest failure on a (newer) 64-bit processor running a 32-bit OS (Core2 quad, Ubuntu 8.10 x86).\n\n----\n\nI think someone should track down if this difference is an lcalc \"feature\" or perhaps a Sage library interface issue (and in the latter case open a new ticket).",
    "created_at": "2010-07-29T17:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92970",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 jhpalmieri]:
> Replying to [comment:5 ddrake]:
> > The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.
> 
> For what it's worth, it also fixes it on two different skynet machines which had the failure: cicero (x86-Linux-pentium4-fc) and iras (ia64-Linux-suse).

Does iras default to 32-bit builds? (I only know it's running a 64-bit SuSE.)

I ask this because Harald also saw this doctest failure on a (newer) 64-bit processor running a 32-bit OS (Core2 quad, Ubuntu 8.10 x86).

----

I think someone should track down if this difference is an lcalc "feature" or perhaps a Sage library interface issue (and in the latter case open a new ticket).



---

archive/issue_comments_092971.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n>  * [attachment:trac_9615-lcalc_doctest_note.patch]\n> \n>  [...] which someone should review, follows up on [comment:7 Leif's suggestion].  Or should I exclude it?\n\nWell, I would have written\n\n```\n          ... # \"noisy\" zero on some platforms (see #9615)\n```\n\n\nBut now it's too late...",
    "created_at": "2010-07-29T17:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92971",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:12 mpatel]:
>  * [attachment:trac_9615-lcalc_doctest_note.patch]
> 
>  [...] which someone should review, follows up on [comment:7 Leif's suggestion].  Or should I exclude it?

Well, I would have written

```
          ... # "noisy" zero on some platforms (see #9615)
```


But now it's too late...



---

archive/issue_comments_092972.json:
```json
{
    "body": "Attachment [trac_9615-lcalc_doctest_note.2.patch](tarball://root/attachments/some-uuid/ticket9615/trac_9615-lcalc_doctest_note.2.patch) by @qed777 created at 2010-08-01 08:12:23\n\nUse Leif's better note.  Replaces previous version.  Apply on top of [attachment:9615.2.patch]",
    "created_at": "2010-08-01T08:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92972",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_9615-lcalc_doctest_note.2.patch](tarball://root/attachments/some-uuid/ticket9615/trac_9615-lcalc_doctest_note.2.patch) by @qed777 created at 2010-08-01 08:12:23

Use Leif's better note.  Replaces previous version.  Apply on top of [attachment:9615.2.patch]



---

archive/issue_comments_092973.json:
```json
{
    "body": "Replying to [comment:15 leif]:\n> But now it's too late...\n\nI've attached an update with Leif's better comment.  I'll merge\n\n* [attachment:9615.2.patch]\n* [attachment:trac_9615-lcalc_doctest_note.2.patch]\n\ninto 4.5.2.rc0.  I'm adding Leif as an author and me as a reviewer.",
    "created_at": "2010-08-01T08:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-92973",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:15 leif]:
> But now it's too late...

I've attached an update with Leif's better comment.  I'll merge

* [attachment:9615.2.patch]
* [attachment:trac_9615-lcalc_doctest_note.2.patch]

into 4.5.2.rc0.  I'm adding Leif as an author and me as a reviewer.
