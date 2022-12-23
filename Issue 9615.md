# Issue 9615: doctest failures with lcalc functions in 4.5.2.alpha1

archive/issues_009615.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  bober craigcitro cremona mrubinst@math.uwaterloo.ca mpatel mvngu rishi ylchapuy rbeezer\n\nKeywords: lcalc\n\nDoctest failures in alpha1: https://groups.google.com/group/sage-release/msg/8807ed7073c6793f :\n\n```\nFile \"/scratch/scratch/schilly/sage/sage-4.5.2.alpha1/devel/sage/sage/\nlibs/lcalc/lcalc_Lfunction.pyx\", line 780:\n    sage: L.value(0.5)\nExpected:\n    0\nGot:\n    -1.28235854574334e-17\n----------------------------------------------- \n```\n\nThis is related to #5396.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9615\n\n",
    "created_at": "2010-07-28T02:41:49Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "doctest failures with lcalc functions in 4.5.2.alpha1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9615",
    "user": "ddrake"
}
```
Assignee: mvngu

CC:  bober craigcitro cremona mrubinst@math.uwaterloo.ca mpatel mvngu rishi ylchapuy rbeezer

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

archive/issue_comments_093107.json:
```json
{
    "body": "Just for the record: I get exactly the same number with\n* Ubuntu 7.10 x86, Pentium 4 (Northwood), gcc 4.2.1\n* Ubuntu 9.04 x86, Pentium 4 Prescott, gcc 4.3.3\n\nFrom sage-release:\n\n  ''There is one numerical noise from #5396 ticket.  I will write a patch\n  which tests that L.value(0.5).abs() is less than 1e-14, instead of\n  current value of 0.''\n\n\n  ''The long messages giving out some data about L  function are from a\n  test function in lcalc library. It is helpful in testing. It just\n  prints out to standard output. Please ignore them.''\n\n  *Rishi*",
    "created_at": "2010-07-28T02:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93107",
    "user": "leif"
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

archive/issue_comments_093108.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-28T12:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93108",
    "user": "rishi"
}
```

Attachment



---

archive/issue_comments_093109.json:
```json
{
    "body": "I did not check my email before creating a duplicate ticket and submitting a patch. Please close #9624",
    "created_at": "2010-07-28T12:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93109",
    "user": "rishi"
}
```

I did not check my email before creating a duplicate ticket and submitting a patch. Please close #9624



---

archive/issue_comments_093110.json:
```json
{
    "body": "Changing assignee from mvngu to rishi.",
    "created_at": "2010-07-28T12:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93110",
    "user": "rishi"
}
```

Changing assignee from mvngu to rishi.



---

archive/issue_comments_093111.json:
```json
{
    "body": "I'm changing the status to `needs_review`.  Is that OK?\n\nAlso, if I don't do it, someone should prepend the ticket number in the patch commit string.",
    "created_at": "2010-07-28T22:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93111",
    "user": "mpatel"
}
```

I'm changing the status to `needs_review`.  Is that OK?

Also, if I don't do it, someone should prepend the ticket number in the patch commit string.



---

archive/issue_comments_093112.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T22:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93112",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093113.json:
```json
{
    "body": "Attachment\n\nTicket number and somewhat more general comment in commit string.  Apply only this patch.",
    "created_at": "2010-07-28T23:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93113",
    "user": "mpatel"
}
```

Attachment

Ticket number and somewhat more general comment in commit string.  Apply only this patch.



---

archive/issue_comments_093114.json:
```json
{
    "body": "The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.\n\nOne question, though: is lcalc expected to return precisely zero, or a \"noisy zero\"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. \n\nIf this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)",
    "created_at": "2010-07-29T00:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93114",
    "user": "ddrake"
}
```

The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.

One question, though: is lcalc expected to return precisely zero, or a "noisy zero"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. 

If this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)



---

archive/issue_comments_093115.json:
```json
{
    "body": "Replying to [comment:5 ddrake]:\n> [...] It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. \n> \n> If this kind of behavior is expected on 32-bit versus 64-bit machines, [...]\n\nI can only imagine this is related to (unintentionally) different [default] rounding modes on different processors.\n\nSo this patch fixes the failing doctest (which is IMHO ok for the moment), but doesn't address its reason.\n\nUnless the involved `abs()` (or `<`) is somehow broken, I can give this a positive review without applying the patch and actually testing it... ;-)",
    "created_at": "2010-07-29T01:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93115",
    "user": "leif"
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

archive/issue_comments_093116.json:
```json
{
    "body": "The patched doctest lacks an explanation/reference back to this ticket, which I think would be appropriate in this case.\n\nNot surprisingly passes all (long) tests in `sage/libs/lcalc/` on Ubuntu 9.04 x86 (Pentium 4 Prescott, gcc 4.3.3), where the doctest previously failed.\n\nI remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).",
    "created_at": "2010-07-29T02:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93116",
    "user": "leif"
}
```

The patched doctest lacks an explanation/reference back to this ticket, which I think would be appropriate in this case.

Not surprisingly passes all (long) tests in `sage/libs/lcalc/` on Ubuntu 9.04 x86 (Pentium 4 Prescott, gcc 4.3.3), where the doctest previously failed.

I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).



---

archive/issue_comments_093117.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).\n\n    \n  ''[...] On 32-bit Ubuntu 10.04 on Pentium M I get the same results as Harald,\n  though the non-zero value in the lcalc test is slightly different (~e-18). [...]''\n  \n  *Rob*\n\nRob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)",
    "created_at": "2010-07-29T02:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93117",
    "user": "leif"
}
```

Replying to [comment:7 leif]:
> I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).

    
  ''[...] On 32-bit Ubuntu 10.04 on Pentium M I get the same results as Harald,
  though the non-zero value in the lcalc test is slightly different (~e-18). [...]''
  
  *Rob*

Rob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)



---

archive/issue_comments_093118.json:
```json
{
    "body": "In lcalc, the function being tested returns a complex number (double precision). It is probably the way different processors do the computations, that the doctest failures are occurring. The earlier doctest passed on all the machines I have access to. \n\nThe calculation of L-function is pretty involved, you can see the papers which are referred to in the patch in #5396. \n\nReplying to [comment:5 ddrake]:\n> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.\n> \n> One question, though: is lcalc expected to return precisely zero, or a \"noisy zero\"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. \n> \n> If this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)",
    "created_at": "2010-07-29T03:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93118",
    "user": "rishi"
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

archive/issue_comments_093119.json:
```json
{
    "body": "Same 32-bit system as before, applied \".2\" patch.  Then\n\n\n```\nsage -t -long \"devel/sage-main/sage/libs/lcalc/lcalc_Lfunction.pyx\"\n\t [3.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 3.3 seconds\n```\n\n\nReplying to [comment:8 leif]:\n> Replying to [comment:7 leif]:\n> > I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).\n> \n>     \n>   ''[...] On 32-bit Ubuntu 10.04 on Pentium M I get the same results as Harald,\n>   though the non-zero value in the lcalc test is slightly different (~e-18). [...]''\n>   \n>   *Rob*\n> \n> Rob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)",
    "created_at": "2010-07-29T03:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93119",
    "user": "rbeezer"
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

archive/issue_comments_093120.json:
```json
{
    "body": "Replying to [comment:5 ddrake]:\n> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.\n\nFor what it's worth, it also fixes it on two different skynet machines which had the failure: cicero (x86-Linux-pentium4-fc) and iras (ia64-Linux-suse).",
    "created_at": "2010-07-29T04:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93120",
    "user": "jhpalmieri"
}
```

Replying to [comment:5 ddrake]:
> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.

For what it's worth, it also fixes it on two different skynet machines which had the failure: cicero (x86-Linux-pentium4-fc) and iras (ia64-Linux-suse).



---

archive/issue_comments_093121.json:
```json
{
    "body": "Add a note with the ticket number.  Apply on top of [attachment:9615.2.patch]",
    "created_at": "2010-07-29T05:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93121",
    "user": "mpatel"
}
```

Add a note with the ticket number.  Apply on top of [attachment:9615.2.patch]



---

archive/issue_comments_093122.json:
```json
{
    "body": "Attachment\n\nUnless anyone objects, I'm changing the status to *positive_review* and merging\n\n* [attachment:9615.2.patch]\n* [attachment:trac_9615-lcalc_doctest_note.patch]\n\nin 4.5.2.rc0.  The latter, which someone should review, follows up on [comment:7 Leif's suggestion].  Or should I exclude it?",
    "created_at": "2010-07-29T05:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93122",
    "user": "mpatel"
}
```

Attachment

Unless anyone objects, I'm changing the status to *positive_review* and merging

* [attachment:9615.2.patch]
* [attachment:trac_9615-lcalc_doctest_note.patch]

in 4.5.2.rc0.  The latter, which someone should review, follows up on [comment:7 Leif's suggestion].  Or should I exclude it?



---

archive/issue_comments_093123.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-29T05:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93123",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093124.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-29T05:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93124",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_093125.json:
```json
{
    "body": "Replying to [comment:11 jhpalmieri]:\n> Replying to [comment:5 ddrake]:\n> > The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.\n> \n> For what it's worth, it also fixes it on two different skynet machines which had the failure: cicero (x86-Linux-pentium4-fc) and iras (ia64-Linux-suse).\n\nDoes iras default to 32-bit builds? (I only know it's running a 64-bit SuSE.)\n\nI ask this because Harald also saw this doctest failure on a (newer) 64-bit processor running a 32-bit OS (Core2 quad, Ubuntu 8.10 x86).\n\n----\n\nI think someone should track down if this difference is an lcalc \"feature\" or perhaps a Sage library interface issue (and in the latter case open a new ticket).",
    "created_at": "2010-07-29T17:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93125",
    "user": "leif"
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

archive/issue_comments_093126.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n>  * [attachment:trac_9615-lcalc_doctest_note.patch]\n> \n>  [...] which someone should review, follows up on [comment:7 Leif's suggestion].  Or should I exclude it?\n\nWell, I would have written\n\n```\n          ... # \"noisy\" zero on some platforms (see #9615)\n```\n\n\nBut now it's too late...",
    "created_at": "2010-07-29T17:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93126",
    "user": "leif"
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

archive/issue_comments_093127.json:
```json
{
    "body": "Attachment\n\nUse Leif's better note.  Replaces previous version.  Apply on top of [attachment:9615.2.patch]",
    "created_at": "2010-08-01T08:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93127",
    "user": "mpatel"
}
```

Attachment

Use Leif's better note.  Replaces previous version.  Apply on top of [attachment:9615.2.patch]



---

archive/issue_comments_093128.json:
```json
{
    "body": "Replying to [comment:15 leif]:\n> But now it's too late...\n\nI've attached an update with Leif's better comment.  I'll merge\n\n* [attachment:9615.2.patch]\n* [attachment:trac_9615-lcalc_doctest_note.2.patch]\n\ninto 4.5.2.rc0.  I'm adding Leif as an author and me as a reviewer.",
    "created_at": "2010-08-01T08:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9615#issuecomment-93128",
    "user": "mpatel"
}
```

Replying to [comment:15 leif]:
> But now it's too late...

I've attached an update with Leif's better comment.  I'll merge

* [attachment:9615.2.patch]
* [attachment:trac_9615-lcalc_doctest_note.2.patch]

into 4.5.2.rc0.  I'm adding Leif as an author and me as a reviewer.
