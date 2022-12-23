# Issue 4741: [with patch, not yet ready for review] Implement S-integral point finding for elliptic curves over Q

Issue created by migration from https://trac.sagemath.org/ticket/4741

Original creator: cremona

Original creation time: 2008-12-08 12:37:24

Assignee: was

CC:  mardaus tnagel

This follows on from #3674, where integral points for elliptic curves over Q were implemented.

The work here was done (again) by Tobias Nagel and Michael Mardaus, with some necessary backup functionality for elliptic curve local data by me (John Cremona) which has already been merged.

Two functions are defined:  (1) `padic_elliptic_logarithm()` for points on curves over number fields, in ell_point.py; (2) `S_integral_points()` for curves over Q only (so far!), in ell_rational field.py.

The patch s_int_pts.patch applies to 3.2.1 + the patches at #4715.  Should be ready for review soon...


---

Attachment


---

Comment by cremona created at 2008-12-08 15:28:05

The second patch fixes various issues with the padic_log function:

    1. Bug: points of finite order have log 0 and this case should be dealt with at the beginning.  The code breaks on E(0), for example.
    2. I deleted the "print_mode" parameter since it was actually changing the output type from p-adic to rational;  callers can lift if they want.
    3. The test "if xde == p**(xde.valuation(p))" seems to be wrong.  I changed it to "if x.valuation(p)>=0", which is the condition that P is not in the formal group.
    4. It did not multiply P by the Tamagawa exponent.
    5. It did not divide the answer by the factor you multiplied the point by! 
    6. The precision was artificially capped at 20, since the prec parameter to log() was not used and defaults to 20.  That is the precision of the power series in t, where we will substitute t=-x/y, so I added "prec=1+precision//v"  where v is the valuation of -x/y.  (N.B. in `E^1` one has val(x)=-2*v and val(y)=-3*v for some v>0, so v=val(-x/y).
    7. I added some doctests to show that log(k*P)/log(P)==k in various examples.  That is how I discovered the precision problem.  Now it looks pretty good.


---

Attachment


---

Comment by cremona created at 2008-12-11 14:18:59

The third patch fixes a bug (missed a 2-integral points on 37a1) and makes  `S_integral_x_coords_with_abs_bounded_by()` slightly more efficient, but we are way slower than Magma and I think that the main culprits are that function and  `S_integral_points_with_bounded_mw_coeffs()`.   In the integral points case we made the latter much faster by using real points (since you can tell if a real number is approximately integral) but th analogous thing for S-integral points is more complicated.  Rather than wait, as we are getting the right points (after substantial testing against Magma, for example), I would like this to go in now and we can look into making things faster later.

Details of what is in the 3rd patch:
    1. p-adic elliptic log: default precision now 20 not 100, which works fine.  Also converts points to p-adic earlier which avoids dealing with large rationals when the multiplier factor is needed.
    2. Calls to p-adic log from S_integral_points() now multiply by the necessary factor after taking logs instead of before: it is a homomorphism, and again this avoinds dealing with larger rationals.
    3. Correct use of proof flag (though it is rather crude that when proof==False we just omit the time-consuming call to  S_integral_x_coords_with_abs_bounded_by(abs_bound)).
    4. Some speed improvements to S_integral_x_coords_with_abs_bounded_by(), and improved comments including some TODOs.

[Note to Tobias and Michael M: this patch includes the changes in the patch you sent me.]

I have a timing comparison table and will include it here once I have worked out how to do wiki tables.


---

Comment by cremona created at 2008-12-11 14:53:19

I keep on thinking of more things which should be done to speed this up.  I'm putting them here so they do not get lost.

p-adic elliptic log:  we call this on several points for each prime, but a lot of the code does not depend on the point (construction of p-adic field, and the formal group, and the series), so this code should be reorganised: this probably means having a new class to store all that stuff.


---

Comment by mardaus created at 2008-12-12 06:48:56

Hey John,

I'm having a hard time with the latest patch. It does not apply on a fresh clone from 3.2.1 with the patches from ticket 4715 and the 2 others from this ticket.

It gives me:

```
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 FAILED at 4532
Hunk #4 succeeded at 4611 with fuzz 2 (offset 0 lines).
Hunk #5 FAILED at 4633
Hunk #6 FAILED at 4655
Hunk #11 FAILED at 4822
Hunk #12 FAILED at 4845
5 out of 16 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
abort: patch failed to apply
```

when I try. Perhaps you changed something else in your file before exporting this one.
Or am I doing something wrong?


---

Comment by mabshoff created at 2008-12-12 06:58:15

Yep, same thing for me in my current 3.2.2.alpha2 merge tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/devel/sage$ patch -p1 < trac-4741-fix2.patch\?format\=raw patching file sage/schemes/elliptic_curves/ell_point.py
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 FAILED at 4533.
Hunk #2 succeeded at 4547 (offset 1 line).
Hunk #4 succeeded at 4609 with fuzz 2.
Hunk #5 FAILED at 4634.
Hunk #6 FAILED at 4662.
Hunk #7 succeeded at 4669 (offset -10 lines).
Hunk #8 succeeded at 4695 (offset -10 lines).
Hunk #9 succeeded at 4728 (offset -10 lines).
Hunk #10 succeeded at 4744 (offset -10 lines).
Hunk #11 FAILED at 4819.
Hunk #12 FAILED at 4854.
Hunk #13 succeeded at 4936 (offset -19 lines).
Hunk #14 succeeded at 4972 (offset -19 lines).
Hunk #15 succeeded at 5014 (offset -19 lines).
Hunk #16 succeeded at 5094 (offset -19 lines).
5 out of 16 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
```

The only changes post 3.2.1 to that file were:

```
hangeset:   11145:614177b99fa2
user:        John Cremona <john.cremona@gmail.com>
date:        Fri Dec 05 13:34:53 2008 +0000
summary:     #4715 second patch

changeset:   11144:84cee787fc0f
user:        John Cremona <john.cremona@gmail.com>
date:        Fri Dec 05 11:58:48 2008 +0000
summary:     #4715: tiny bug fix in KodairaSymbol + doctest
```

But even reverting those two patches does not make fix2 apply, so are we missing a patch?

Cheers,

Michael


---

Comment by cremona created at 2008-12-12 08:49:29

Sorry everyone.  I'll make a new patch which works properly, and with 3.2.2.alpha1.  Since our patches essentially just add two separate functions, one each in two files, it should not be too difficult but I'll wait until I get into the office.


---

Attachment

Replaces all the above; based on 3.2.2.alpha1


---

Comment by cremona created at 2008-12-12 09:49:53

OK, I have posted a new patch which replaces all the earlier ones and is based on 3.2.2.alpha1.  I tested it on a fresh clone of that version and all seems well.


---

Comment by mabshoff created at 2008-12-12 17:04:15

trac-4741-rebase.patch applies cleanly to my Sage 3.2.2.alpha2 merge tree. But I am seeing one doctest failure with -long on sage.math:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2$ ./sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 3338, in __main__.example_110
Failed example:
    time E.rank(), len(E.S_integral_points([Integer(3),Integer(5),Integer(7)]))  # long time (~15s)###line 4619:_sage_    >>> time E.rank(), len(E.S_integral_points([3,5,7]))  # long time (~15s)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_110[10]>", line 1
         time E.rank(), len(E.S_integral_points([Integer(3),Integer(5),Integer(7)]))  # long time (~15s)###line 4619:_sage_    >>> time E.rank(), len(E.S_integral_points([3,5,7]))  # long time (~15s)
              ^
     SyntaxError: invalid syntax
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_110
***Test Failed*** 1 failures.

         [221.0 s]
exit code: 1024
```


Cheers,

Michael


---

Attachment


---

Comment by cremona created at 2008-12-12 17:18:06

Sorry about that, clearly I did not do a -long test.  I just left the "time"  command in the doctest by mistake.  Testing this again I find that instead of 15s this example only takes 7.5s (my work yesterday was good, wasn't it!) but I have left in the # long time sdince this files so much in it already.

New minipatch should so the trick.


---

Comment by mardaus created at 2008-12-13 03:51:47

Here we go, now it applies on my 3.2.1 build and all tests, but the long passed.
How long should the long test for ell_rational_field take? I ran it 3h and nothing.
Thanks


---

Comment by mardaus created at 2008-12-13 08:15:04

Ok no idea, what was wrong on my 3.2.1 but with a fresh built 3.2.2 alpha1 and the 2 patches here, doctest worked fine. (normal and long). So I guess we are good to go for 3.2.2.

Cheers Michael


---

Comment by cremona created at 2008-12-13 10:13:42

Thanks Michael (M).  Michael (A), can we put a positive review on this?  I would have preferred someone other than the three of us reviewing eachothers' code!


---

Comment by was created at 2008-12-13 21:39:21

REFEREE REPORT:

Two trivial typo fixes:

 * "It is not necessary to specify mw_base, then the Mordell-Weil basis must be computed (may take much longer)" --> "It is not necessary to specify mw_base; if it is not specified, then the Mordell-Weil basis must be computed, which may take much longer."

 * "Computes the p-adic elliptic logarithm of self" --> "Computes the p-adic elliptic logarithm of self."

A BUG:

```
sage: E = EllipticCurve('794a1')
sage: E.S_integral_points([2,3,5])
Traceback (most recent call last):
...
sage.rings.padics.precision_error.PrecisionError: cannot divide by something indistinguishable from zero
```



---

Attachment


---

Comment by cremona created at 2008-12-13 22:17:10

The *-prec.patch fixes that for your example but a more itelligent solution would be preferable...


---

Attachment

Sorry, forgot to fix the typos: see *-typos.patch.  Sorry for the extra hassle.


---

Attachment

OK, so I found 2 more trivial bugs in kodaira which only mattered in the tamagawa_exponent() function used (only) in S_integral_points and padic_elliptic_log functions.  Fixed, and tested that tamagawa_exponent() works on all curves in the database to 6000, with all bad primes for each.  (Sorry, I have not checked that this covers all Kodaira types, but I think so.  The code even failed on 1 curve of conductor 15.)

That revealed a but in pari_curve(), for example 903b3, where the default pari precision was not enough.  I now test for this (with try: ... except PariError) and double the precision on failure, continuing until success.  The crazy thing is that I remember fixing that bug before, but it must have been while working on something which never got submitted (or is bitrotting on trac perhaps;)).

Next I tested again the database curves of rank at least 2 with S=[2,3,5].  No problems until 2175c3, and that just takes a long time.  So I think it is safe to proceed (famous last words, but it's my bedtime).  The *-fix3.patch contains the above-mentioned fixes and also adapts the doctests to agree with the output from the enhanced p-adic precision which I forgot earlier.


---

Comment by mabshoff created at 2008-12-14 08:27:59


```
[12:23am] wstein: I can't apply trac-4741-fix3.patch  from cremona's ticket cleanly...
[12:24am] wstein: If the patch passes all doctests and you can apply it, then positive review.
[12:24am] mabshoff: mk
[12:24am] wstein: He addressed my issues, and did a good test of running the code.
[12:24am] mabshoff: ok
```



---

Comment by was created at 2008-12-14 08:28:18

So sort of positive review.  I have read all the latest changes and they *look* good, but I have *not* actually tried the new code or run doctests, since I can't apply the last patch.


---

Comment by mabshoff created at 2008-12-14 08:35:29

Yep, I am seeing the same issue as William:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage$ patch -p1 < trac_4741_part_1_rebase.patch 
patching file sage/schemes/elliptic_curves/ell_point.py
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 succeeded at 4585 (offset 53 lines).
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage$ patch -p1 < trac_4741_part_2_doctest.patch 
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 succeeded at 4669 (offset 53 lines).
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage$ patch -p1 < trac_4741_part_3_prec.patch 
patching file sage/schemes/elliptic_curves/ell_point.py
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage$ patch -p1 < trac_4741_part_4_typos.patch 
patching file sage/schemes/elliptic_curves/ell_point.py
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 succeeded at 4651 (offset 66 lines).
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage$ patch -p1 --dry-run < trac_4741_part_5_fix3.patch 
patching file sage/schemes/elliptic_curves/ell_point.py
patching file sage/schemes/elliptic_curves/ell_rational_field.py
Hunk #1 FAILED at 485.
Hunk #2 FAILED at 509.
Hunk #3 succeeded at 4644 (offset 66 lines).
2 out of 3 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_rational_field.py.rej
patching file sage/schemes/elliptic_curves/kodaira_symbol.py
Hunk #1 FAILED at 78.
1 out of 1 hunk FAILED -- saving rejects to file sage/schemes/elliptic_curves/kodaira_symbol.py.rej
```

So either I am doing something wrong, i.e. merging the wrong patches or fix3 needs a rebase.

Cheers,

Michael


---

Comment by cremona created at 2008-12-14 11:04:19

I think my problem is that I had just done a -upgrade to 3.2.2.alpha1 which -- as usual with upgrades -- toally and utterly confused me.  Upgrades leave with with a Sage version which does not match the name of the directory that it is in.

So now I'll try to make it work properly with 3.2.2.alpha2 (not alpha1) and while I am at it, combine those 3 little patches into one.


---

Attachment

I was right: last night's 3 patches were all based on the previous release.  This explains two things:  the kodaira bugs I re-fixed last night had already been fixed, as had the pari_curve precision problem.

So now we have trac-4741-rebased-fixes.patch which (1) replaces the previous 3; (2) is properly based on 3.2.2.alpha2; (3) improves on the earlier fixes by handling the p-adic precision more intelligently (it uses try/except, first trying p-adci precision 20 and doubling if that fails).

I tried the patch on a new clone of 3.2.2.alpha2.  To recap, apply these three patches in this order and ignore the others:
    1. trac-4741-rebase.patch
    2. trac-4741-doctest.patch
    3. trac-4741-rebased-fixes.patch
and you should find that all doctests in sage/schemes/elliptic_curves pass, and that for all database curves to conductor 2000 of rank>1 E.S_integral_points([2,3,5]) works fine.


---

Comment by mabshoff created at 2008-12-14 16:55:53

Replying to [comment:18 was]:
> 
> 
> So sort of positive review.  I have read all the latest changes and they *look* good, but I have *not* actually tried the new code or run doctests, since I can't apply the last patch. 

Applying 

 1. trac-4741-rebase.patch
 1. trac-4741-doctest.patch
 1. trac-4741-rebased-fixes.patch

leads to a working Sage as well as passing doctests.

William: I assume you want to give this the final positive review once you poke around a little more.

Cheers,

Michael


---

Comment by was created at 2008-12-14 19:27:15

REFEREE REPORT:

I broke it again with a simple for loop.


```
sage: EllipticCurve('2534g1').S_integral_points([13,2])
...
--> 576             return self[0]/self[2], self[1]/self[2]
    577 
    578     def is_divisible_by(self, m):

/home/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9074)()

/home/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/rings/padics/padic_capped_relative_element.so in sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement._div_ (sage/rings/padics/padic_capped_relative_element.c:11055)()

ZeroDivisionError: cannot divide by zero
```


This is the loop that got it:

```
sage: for E in cremona_optimal_curves([1000..10000]):
    if E.rank() == 2:
        print E.cremona_label(), E.S_integral_points([13]+[E.conductor().factor()[0][0]])
```



---

Comment by mabshoff created at 2008-12-14 20:09:31

Fix the summary so that this ticket isn't picked up by report 19.

Cheers,

Michael


---

Comment by cremona created at 2008-12-14 20:57:16

Don't you just love thorough reviewing (seriously).  I was not trapping enough errors in my padic log fix.  Now as well as PariError I trap ZeroDivisionError and TypeError, which can all happen when the precision is too low.  That run fine on was's loop until 2666e1.  This may not get finished tonight...


---

Attachment

Various p-adic precision bandaids applied, so that William's loop now runs up to this one:

sage: EllipticCurve("7690e1").S_integral_points([13,2])

at which point there's an error raised deep in the p-adic code.  I can't deal with that now, so someone will have to make a judgement about whether this is now "good enough".

Working with p-adics is an acquired skill which I'm not sure I have enough of -- perhaps we need reinforcements?  For example, you cannot just do E.change_ring(Qp(p,precision)) for E an elliptic curve over Q, since an error will be raised if the precision is too low (only of p is a prime of bad reduction I think, so one should be able to work out the necessary precision).

Tobias and Michael, the try/except I put in around line 5077 of ell_rational_field.py was not fully thought through, perhaps that is something you should look into?


trac-4741-padic.patch


---

Comment by tnagel created at 2008-12-15 09:00:20

I will have a look at the try/except statement.Unfortunately I have to attend some courses at university this morning, so I will do that this afternoon. Was there a special curve you needed this try/except?

I hope the rest of the code will get a "good enough" judgment.


---

Comment by mabshoff created at 2008-12-15 09:02:25

I am inclined to merge this code and then open a new ticket for the remaining issues. This code has gotten beaten up quite a bit and it seems certainly to be a lot less buggy than any currently released Magma code :)

Cheers,

Michael


---

Comment by cremona created at 2008-12-15 09:41:34

Thanks for the encouragement, Michael!

Here's the strategy I propose.  We separate out as an issue the computation of the p-adic elliptic log (of a point on an elliptic curve over Q, and later over number fields).  A lot of this work does not depend on the point, only on the curve and the prime (specifically, construction of the base-change curve over Qp, and the integer f such that `f*E(Qp)\subseteq E^1(Qp)`, which is the product of the tamagawa exponent (already cached) and the exponent of the group mod p).  This could be stored in the local_data class which we already have.  The p-adic part of this would need some work to compute the suitable precision needed (which may be more than the user asks for).

The second issue is then the S_integral points code itself, where I had one difficulty.  I'll recover the curve which caused that and send it to tnagel.


---

Comment by was created at 2008-12-15 15:33:18

I am OK with merging the code as is now, as long as a "NOTE:" is added to the docstring for S_integral_points (etc.) that it is known to fail on some input, with a pointer to the appropriate trac ticket.  I much prefer that to the Ma* approach of "there are no bugs here" approach, where one lets the user discover bugs.

So "positive review" modulo adding such a note.


---

Comment by cremona created at 2008-12-15 15:55:23

Replying to [comment:30 was]:
> I am OK with merging the code as is now, as long as a "NOTE:" is added to the docstring for S_integral_points (etc.) that it is known to fail on some input, with a pointer to the appropriate trac ticket.  I much prefer that to the Ma* approach of "there are no bugs here" approach, where one lets the user discover bugs.
> 
> So "positive review" modulo adding such a note.

Sounds good to me.  I'll try to add such a NOTE today.  JEC


---

Attachment

Replying to [comment:31 cremona]:
> Replying to [comment:30 was]:
> > I am OK with merging the code as is now, as long as a "NOTE:" is added to the docstring for S_integral_points (etc.) that it is known to fail on some input, with a pointer to the appropriate trac ticket.  I much prefer that to the Ma* approach of "there are no bugs here" approach, where one lets the user discover bugs.
> > 
> > So "positive review" modulo adding such a note.
> 
> Sounds good to me.  I'll try to add such a NOTE today.  JEC  -- done


---

Comment by was created at 2008-12-15 16:41:36

Positive review pending deletion of the question mark "?" in this line of the last patch:

```
EllipticCurve?("7690e1").S_integral_points([13,2])
```


William


---

Comment by mabshoff created at 2008-12-15 16:43:07

John,

please also open a new ticket for that known failure and mention that ticket in the NOTE since this ticket will then be closed and finding the info about that curve is much easier at a clean and new ticket.

Cheers,

Michael


---

Attachment

Replying to [comment:34 mabshoff]:
> John,
> 
> please also open a new ticket for that known failure and mention that ticket in the NOTE since this ticket will then be closed and finding the info about that curve is much easier at a clean and new ticket.
> 
> Cheers,
> 
> Michael

Typo fixed and reference to new ticket #4805 added in *-note2.patch.


---

Comment by cremona created at 2008-12-15 17:03:52

Replying to [comment:33 was]:
> Positive review pending deletion of the question mark "?" in this line of the last patch:
> {{{
> EllipticCurve?("7690e1").S_integral_points([13,2])
> }}}
> 
> William

Perfectionist!  Of course I notived that after uploading the patch (after which there is no way of deleting it for us ordinary mortals ;)).


---

Comment by mabshoff created at 2008-12-15 17:09:35

Positive review. Finally ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-15 17:12:40

Merged 
 * trac_4741_part_1_rebase.patch
 * trac_4741_part_2_doctest.patch
 * trac_4741_part_3_rebased-fixes.patch
 * trac_4741_part_4_note.patch
 * trac_4741_part_5_note2.patch

in Sage 3.2.2.rc0


---

Comment by mabshoff created at 2008-12-15 17:12:40

Resolution: fixed
