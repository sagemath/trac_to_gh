# Issue 4249: Inconsistency in number field integral bases

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-10-07 11:21:35

Assignee: was

CC:  "maite aranes" <m.t.aranes@warwick.ac.uk>

Keywords: number fields

This is unacceptable (in  my opinion):

```
sage: K.<a>=NumberField(x^2+23)
sage: K.integral_basis()
[1, 1/2*a + 1/2]
sage: K.ring_of_integers().basis()
[1/2*a + 1/2, a]
```


I think these should be the same.  The problem is that K.integral_basis() gets the basis from pari, but when the ring_of_integers is constructed it uses that basis in the constructions but then creates its own, different, basis!

Suggested solution:  make the existing integral_basis() function an internal one used by the ring_of_integers() function only, and have K.integra_basis() return the basis of the ring of integers instead.


---

Comment by was created at 2008-10-08 04:31:38

I strongly agree with John Cremona's suggested fix.


---

Attachment


---

Comment by cremona created at 2008-10-14 20:47:11

The attached patch (which applies to 3.1.3) does what was proposed.  All doctests in sage/rings/number_fields/ pass *except* for a couple in totallyreal_rel.py where one of the totally real quadratic extensions of Q(sqrt(5)) is now missing.  I do not know why but suggest that there might be a bug in that file, so will ask John Voight to look into it.


---

Comment by jvoight created at 2008-10-14 22:47:07

I can't test this yet because I can't apply the patch to 3.1.2, and the upgrade is apparently not yet working.  I'm worried about all of the changes to reduced_basis which resulted from the change, but will have a look ASAP.  JV


---

Comment by cremona created at 2008-10-15 06:01:19

Thanks John.  I put "not ready for review" since we don't yet know exactly what is going on.  John


---

Comment by jvoight created at 2008-10-16 00:49:27

Hm.  John, what bug exactly were you getting?  I just applied your sage-4249.patch to a clean build of sage-3.1.3 and it indeed gives me 21 totally real quadratic extensions of Q(sqrt(5)) with discriminant <= 10^4.  In particular, for this example the output of F.reduced_basis() does not seem to change after the patch, and so I would not expect anything to change.

JV


---

Comment by cremona created at 2008-10-16 05:53:54

When I apply my patch to 3.1.3 I get this (testing all files in number_field):

```
******************************
File "/home/john/sage-3.1.3/tmp/totallyreal_rel.py", line 658:
    sage: [ f[0] for f in ls ]
Expected:
    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725, 9225]
Got:
    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7600, 7625, 8000, 8525, 8725, 9225]
**********************************************************************
File "/home/john/sage-3.1.3/tmp/totallyreal_rel.py", line 661:
    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]
Expected:
    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, True, False, False, True, False, False, False]
Got:
    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False]
**********************************************************************
1 items had failures:
   2 of  12 in __main__.example_6
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/john/sage-3.1.3/tmp/.doctest_totallyreal_rel.py
```



---

Comment by jvoight created at 2008-10-16 23:22:23

Huh.  Applying the patch on sage.math (on 3.1.3) gives:
 {{{
 sage: F.<t> = NumberField(x^2-5)
 sage: enumerate_totallyreal_fields_rel?
 sage: ls = enumerate_totallyreal_fields_rel(F, 2, 10^4)
 sage: enumerate_totallyreal_fields_rel?
 sage: [ f[0] for f in ls ]
 [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525,
 5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725,
 9225]
 }}}
Not really sure what could be causing this, unless it's an ugly platform-dependent precision issue or something.


---

Comment by cremona created at 2008-10-17 06:56:12

I agree, it is likely to be a precision issue.  My laptop is 32-bit while sage.math is 64.


---

Comment by jvoight created at 2008-10-20 00:53:22

I downloaded a clean 3.1.3 and installed it on a 32-bit Ubuntu and it again worked fine.  I'm not sure what's going on.  JV


---

Comment by cremona created at 2008-10-20 11:41:39

Replying to [comment:10 jvoight]:
> I downloaded a clean 3.1.3 and installed it on a 32-bit Ubuntu and it again worked fine.  I'm not sure what's going on.  JV

Nor me.  I just tried again on a fresh 3.1.4 and got the same problem as before.

I think we need to ask someone else to help with this!  JEC


---

Comment by jvoight created at 2008-11-06 15:23:57

Hi John,

I'm hoping to tackle this at Sage Days 11, or at least find someone willing to help.  What system are you using?  Maybe I can find someone with the same system so as to reproduce the bug...

JV


---

Comment by cremona created at 2008-11-06 15:26:03

Replying to [comment:12 jvoight]:
> Hi John,
> 
> I'm hoping to tackle this at Sage Days 11, or at least find someone willing to help.  What system are you using?  Maybe I can find someone with the same system so as to reproduce the bug...
> 
> JV

It was probably my laptop (ubuntu linux 8.04 etc).  As I have just built 3.2.alpha3 on a couple of other machines, I'll test my patch on those and see what happens.  Watch this space...


---

Comment by cremona created at 2008-11-06 15:52:17

I applied my patch to 3.2.alpha3 on two machines, a 32-bit Suse linux and a 64-bit ubuntu.
On both machines two files failed doctests:

   1.  sage -t  devel/sage-intpts/sage/rings/number_field/number_field.py
   2.  sage -t  devel/sage-intpts/sage/rings/number_field/totallyreal_rel.py

In totallrel_rel.py we get this:

```
sage -t  devel/sage-intpts/sage/rings/number_field/totallyreal_rel.py**********************************************************************
File "/home/jec/sage-3.2.alpha3/tmp/totallyreal_rel.py", line 658:
    sage: [ f[0] for f in ls ]
Expected:
    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7225, 7600, 7625, 8000, 8525, 8725, 9225]
Got:
    [725, 1125, 1600, 2000, 2225, 2525, 3600, 4225, 4400, 4525, 5125, 5225, 5725, 6125, 7600, 7625, 8000, 8525, 8725, 9225]
**********************************************************************
File "/home/jec/sage-3.2.alpha3/tmp/totallyreal_rel.py", line 661:
    sage: [NumberField(ZZx(x[1]), 't').is_galois() for x in ls]
Expected:
    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, True, False, False, True, False, False, False]
Got:
    [False, True, True, True, False, False, True, True, False, False, False, False, False, True, False, False, True, False, False, False]
**********************************************************************
```

which looks like what I got before.  In number_field.py we get this:

```
sage -t  local/sage-3.2.alpha3/devel/sage-intbasis/sage/rings/number_field//number_field.py**********************************************************************
File "/local/jec/sage-3.2.alpha3/tmp/number_field.py", line 2742:
    sage: F.reduced_gram_matrix(prec=128)
Expected:
    [   4.0000000000000000000000000000000000000   0.00000000000000000000000000000000000000    1.9999999999999999999999999999999999037 -1.0684680000000000000000000000000000000e6]
    [  0.00000000000000000000000000000000000000    46721.539331563218381658483353092335550    11488.910026551724275122749703614966768 -1.1228558200864828963821803781091898982e7]
    [   1.9999999999999999999999999999999999037    11488.910026551724275122749703614966768  5.5658915310500611768713076521847709187e8  8.0619179090987317435751641503958312826e9]
    [-1.0684680000000000000000000000000000000e6 -1.1228558200864828963821803781091898982e7  8.0619179090987317435751641503958312826e9 5.8711879006497804783677635022079228656e12]
Got:
    [   4.0000000000000000000000000000000000000   0.00000000000000000000000000000000000000 -2.1369320000000000000000000000000000000e6 -3.3122478000000000000000000000000000000e7]
    [  0.00000000000000000000000000000000000000    46721.539331563218381658483353092335550 -2.2467769057394530109094755223395819322e7 -3.4807276041138450473611629088647496430e8]
    [-2.1369320000000000000000000000000000000e6 -2.2467769057394530109094755223395819322e7 7.0704243186034907491782135494859351061e12 1.1256636615786237006027526953641297995e14]
    [-3.3122478000000000000000000000000000000e7 -3.4807276041138450473611629088647496430e8 1.1256636615786237006027526953641297995e14 1.7923838231014970520503146603069479547e15]

```

which is new.  I find it slightly encouraging that my 32- and 64-bit tests both give exactly the same above (as each other).  I guess that this second discrepancy will be fixed by just changing the Expected doctest output, but the first one really is a bug since a field which should be returned is not.


---

Comment by jvoight created at 2008-11-09 00:26:52

Argh!  Tried the patch on sage.math on 3.2.alpha3, still can't reproduce the error!  


```
jvoight`@`sage:~/sage-3.2.alpha3$ ./sage -t ./devel/sage/sage/rings/number_field/totallyreal_rel.py
sage -t  devel/sage/sage/rings/number_field/totallyreal_rel.py
         [4.5 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.5 seconds}}}

I'll see if I can find someone here in Austin.  (I have some ideas about what may be going on, but I can't check any of them!)  JV


---

Comment by craigcitro created at 2008-11-09 02:35:37

Attached patch fixes the issue. It turns out that John Cremona's fix actually exposed a small bug in `integral_elements_with_trace`, which has been fixed and renamed. 

This was written with John Voight.


---

Comment by craigcitro created at 2008-11-09 03:55:02

Whoops. Forgot that we had to look at John's original patch, too. :)


---

Attachment


---

Attachment

This looks good! 

The only complaints I had were one or two naming issues; in particular, I didn't see why `integral_basis_internal` should be visible when you tab complete. (The `internal` in the name really makes it seem weird.) So I've just corrected a few naming issues, and made a new patch. Then I rebased the patch John Voight and I wrote on top of this. So you should apply:


```
sage-4249.patch
trac-4249-1a.patch
trac-4249-pt2a.patch
```


in order. (I've deleted the old pt2 patch, just to help avoid confusion.)


---

Comment by cremona created at 2008-11-14 09:58:16

I strongly approve of the two new patches, which fix the bug which caused the totally_real_rel failure and also improve on my code design.  I tested them against 3.2.alpha3 and all was well (testing all in number_field/).

So I hope there's enough mutual positive reviewing here for these to be merged.

It would be even better if John V agreed!


---

Comment by jvoight created at 2008-11-14 14:28:38

Yes, definitely I agree.  Positive review.  JV


---

Comment by mabshoff created at 2008-11-14 20:05:57

There are some slight doctest failures to fix:

```
sage -t -long devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/rings/number_field/number_field.py", line 2653:
    sage: F.reduced_basis(prec=96)
Expected:
    [1, alpha, alpha^2 - 15*alpha, alpha^3 - 16*alpha^2 + 469*alpha + 267109] 
Got:
    [1, alpha, alpha^3 - 2*alpha^2 + 15*alpha, 16*alpha^3 - 31*alpha^2 + 469*alpha + 267109]

**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_73
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_number_field.py
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.

	 [29.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long devel/sage/sage/rings/number_field/number_field.py
Total time for all tests: 29.4 seconds
sage -t -long devel/doc/tut/tut.tex                         
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/doc/tut/tut.tex", line 2179:
    : K.integral_basis()
Expected:
    [1, a, 1/2*a^2 + 1/2*a]
Got:
    [1, 1/2*a^2 + 1/2*a, a^2]
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_99
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_tut.py
	 [25.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long devel/doc/tut/tut.tex
Total time for all tests: 25.2 seconds
sage -t -long devel/doc/const/const.tex                     **********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/doc/const/const.tex", line 3450:
    : K.integral_basis()
Expected:
    [1, a, 1/2*a^2 + 1/2*a]
Got:
    [1, 1/2*a^2 + 1/2*a, a^2]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_123
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_const.py
	 [31.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long devel/doc/const/const.tex
Total time for all tests: 31.0 seconds
```



---

Attachment


---

Attachment


---

Comment by cremona created at 2008-11-14 20:48:48

Strange about that first one -- it was one where I had had different output on 32- and 64-bit machines, but now they are the same.  Fixed in trac-4249-3.patch.

The doc ones are in a separate patch  trac-4249-doc.patch which I hope can be dealt with: I did "hg ci" and then "hg export tip" from devel/doc.  For some reason the patch also affects patchlevel.tex.


---

Comment by craigcitro created at 2008-11-15 09:31:23

Yep, last patches look good.


---

Comment by mabshoff created at 2008-11-15 09:38:46

What is the credit situation, i.e. authorship here: John Cremona, John Voight? Review Craig Citro?

What about Aranes Maite?

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-15 09:44:07

I think John C wrote sage-4249.patch, I wrote trac-4249-1a.patch as part of the review, John Voight and I each wrote half of trac-4249-pt2a.patch and reviewed the other, and John Cremona also reviewed this patch. Then John Cremona wrote pt3 and the doc patch.

Either that, or it was Col. Mustard in the study, with the candlestick. (I would be completely in favor of that actually appearing in the release notes.)

I'm not sure if the original patch was written with Aranes Maite.


---

Comment by cremona created at 2008-11-15 10:03:14

Replying to [comment:25 craigcitro]:
> I think John C wrote sage-4249.patch, I wrote trac-4249-1a.patch as part of the review, John Voight and I each wrote half of trac-4249-pt2a.patch and reviewed the other, and John Cremona also reviewed this patch. Then John Cremona wrote pt3 and the doc patch.
> 

That is accurate as far as I am concerned.

> Either that, or it was Col. Mustard in the study, with the candlestick. (I would be completely in favor of that actually appearing in the release notes.)
> 
> I'm not sure if the original patch was written with Aranes Maite.

No, but she (my student) was the one who alerted me to the problem in the first place.


---

Comment by mabshoff created at 2008-11-15 10:27:49

Resolution: fixed


---

Comment by mabshoff created at 2008-11-15 10:27:49

Merged all five patches in Sage 3.2.rc1
