# Issue 9615: doctest failures with lcalc functions in 4.5.2.alpha1

Issue created by migration from https://trac.sagemath.org/ticket/9615

Original creator: ddrake

Original creation time: 2010-07-28 02:41:49

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




---

Comment by leif created at 2010-07-28 02:55:59

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

  _Rishi_


---

Attachment


---

Comment by rishi created at 2010-07-28 12:05:56

I did not check my email before creating a duplicate ticket and submitting a patch. Please close #9624


---

Comment by rishi created at 2010-07-28 12:05:56

Changing assignee from mvngu to rishi.


---

Comment by mpatel created at 2010-07-28 22:02:54

I'm changing the status to `needs_review`.  Is that OK?

Also, if I don't do it, someone should prepend the ticket number in the patch commit string.


---

Comment by mpatel created at 2010-07-28 22:02:54

Changing status from new to needs_review.


---

Attachment

Ticket number and somewhat more general comment in commit string.  Apply only this patch.


---

Comment by ddrake created at 2010-07-29 00:18:00

The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.

One question, though: is lcalc expected to return precisely zero, or a "noisy zero"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. 

If this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)


---

Comment by leif created at 2010-07-29 01:09:40

Replying to [comment:5 ddrake]:
> [...] It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. 
> 
> If this kind of behavior is expected on 32-bit versus 64-bit machines, [...]

I can only imagine this is related to (unintentionally) different [default] rounding modes on different processors.

So this patch fixes the failing doctest (which is IMHO ok for the moment), but doesn't address its reason.

Unless the involved `abs()` (or `<`) is somehow broken, I can give this a positive review without applying the patch and actually testing it... ;-)


---

Comment by leif created at 2010-07-29 02:21:06

The patched doctest lacks an explanation/reference back to this ticket, which I think would be appropriate in this case.

Not surprisingly passes all (long) tests in `sage/libs/lcalc/` on Ubuntu 9.04 x86 (Pentium 4 Prescott, gcc 4.3.3), where the doctest previously failed.

I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).


---

Comment by leif created at 2010-07-29 02:39:18

Replying to [comment:7 leif]:
> I remember there was a single machine reported on sage-release to have a different result than my two 32-bit machines previously had, on which the patch should perhaps be tested, too (but afair also with `abs(...)` below 10<sup>-15</sup>).

    
  ''[...] On 32-bit Ubuntu 10.04 on Pentium M I get the same results as Harald,
  though the non-zero value in the lcalc test is slightly different (~e-18). [...]''
  
  _Rob_

Rob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)


---

Comment by rishi created at 2010-07-29 03:08:44

In lcalc, the function being tested returns a complex number (double precision). It is probably the way different processors do the computations, that the doctest failures are occurring. The earlier doctest passed on all the machines I have access to. 

The calculation of L-function is pretty involved, you can see the papers which are referred to in the patch in #5396. 

Replying to [comment:5 ddrake]:
> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.
> 
> One question, though: is lcalc expected to return precisely zero, or a "noisy zero"? It seems unusual to me that software doing floating point calculations would return precisely zero on some platforms and a noisy zero on others. 
> 
> If this kind of behavior is expected on 32-bit versus 64-bit machines, and if lcalc's answers are imprecise anyway, then I think this can get a positive review. (IOW, my ignorance about lcalc is what's keeping this from a positive review...)


---

Comment by rbeezer created at 2010-07-29 03:53:34

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
>   _Rob_
> 
> Rob, could you perhaps test this patch, too? (Though I don't expect it to fail on your machine either, since your result was even closer to zero.)


---

Comment by jhpalmieri created at 2010-07-29 04:49:56

Replying to [comment:5 ddrake]:
> The patch fixes the problem on a 32-bit Ubuntu Hardy VM which exhibits the doctest failure.

For what it's worth, it also fixes it on two different skynet machines which had the failure: cicero (x86-Linux-pentium4-fc) and iras (ia64-Linux-suse).


---

Comment by mpatel created at 2010-07-29 05:42:57

Add a note with the ticket number.  Apply on top of [attachment:9615.2.patch]


---

Attachment

Unless anyone objects, I'm changing the status to _positive_review_ and merging

 * [attachment:9615.2.patch]
 * [attachment:trac_9615-lcalc_doctest_note.patch]

in 4.5.2.rc0.  The latter, which someone should review, follows up on [comment:7 Leif's suggestion].  Or should I exclude it?


---

Comment by mpatel created at 2010-07-29 05:56:50

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-29 05:57:13

Resolution: fixed


---

Comment by leif created at 2010-07-29 17:25:50

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

Comment by leif created at 2010-07-29 17:39:13

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

Attachment

Use Leif's better note.  Replaces previous version.  Apply on top of [attachment:9615.2.patch]


---

Comment by mpatel created at 2010-08-01 08:12:59

Replying to [comment:15 leif]:
> But now it's too late...

I've attached an update with Leif's better comment.  I'll merge

 * [attachment:9615.2.patch]
 * [attachment:trac_9615-lcalc_doctest_note.2.patch]

into 4.5.2.rc0.  I'm adding Leif as an author and me as a reviewer.
