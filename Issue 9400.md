# Issue 9400: modify the NumberField constructor to pass in optional integer B such that all the internal pari routines will replace the discriminant by its gcd with B, making some things massively faster.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-07-01 03:43:21

Assignee: davidloeffler

CC:  jdemeyer




---

Comment by was created at 2010-07-01 06:48:16

Example of what this makes possible:

```
~wstein/bin/sagedb
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = QQ[]
sage: f = (x^20 - 3*x^19 - 29*x^18 + 91*x^17 + 338*x^16 - 1130*x^15 -
2023*x^14 +
....: 7432*x^13 + 6558*x^12 - 28021*x^11 - 10909*x^10 + 61267*x^9 + 6954*x^8 -
....: 74752*x^7 + 1407*x^6 + 46330*x^5 - 1087*x^4 - 12558*x^3 - 942*x^2 +
....: 960*x + 148)
sage: K.<a> = NumberField(f^2+2, maximize_at_primes=[2])
sage: K.degree()
40
sage: time z = K.factor(2)
CPU times: user 0.59 s, sys: 0.01 s, total: 0.60 s
Wall time: 0.60 s
sage: time k = z[0][0].residue_field()
CPU times: user 1.68 s, sys: 0.03 s, total: 1.71 s
Wall time: 1.98 s
sage: time k(a^3+3)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
abar^3 + 1
```



---

Comment by was created at 2010-08-11 22:12:36

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-08-12 06:23:39

It is clear from a very first look at the patch that this will massively conflict with #9343 (why did nobody point this out to me earlier???).  Personally, I would prefer to postpone the last two points of the description, i.e.

    * implement hashing for number field ideals that isn't a stupid string repr, hence vastly faster 

    * make number field ideals *not* print in reduced form; this will look uglier, but is massively faster and more sensible for any real applications, as people learned constantly at sage days 22.

and do them after #9343 is merged (I also want to change the hashing of PARI objects, see #9667).  Also, I'm personally not completely convinced about the best way to print NumberFieldIdeals (see also my post at sage-devel).


---

Comment by was created at 2010-08-12 11:15:31

> It is clear from a very first look at the patch that this will massively conflict with #9343 (why 

I'm sure this will be easy to merge with #9343.  It's probably best to get 9343 in first, since it is much more difficult, then rebase the current patch against it.

> I would prefer to postpone:  hashing, printing

The current hashing and printing setup is complete and total crap, and needs to be removed ASAP.  It renders number fields completely useless for any nontrivial applications that involve prime ideals. 

> Also, I'm personally not completely convinced about the best way to print 

I saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be). Print in reduced form only in small trivial cases (by default), but allow the user to easily up the cutoff if they want, for some reason.


---

Comment by jdemeyer created at 2010-08-12 17:16:44

Replying to [comment:6 was]:
> I saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be).

Why not hash based on the HNF representation, as I propsed in #9666?  I think this is more canonical than gens() and it is the native PARI format.


---

Comment by was created at 2010-08-14 00:39:08

Replying to [comment:7 jdemeyer]:
> Replying to [comment:6 was]:
> > I saw that.  I think the best solution is exactly what I implemented in the attached patch.  Hash based on gens (trivial, as a hash should be).
> 
> Why not hash based on the HNF representation, as I propsed in #9666?  
> I think this is more canonical than gens() and it is the native PARI format.

CONS:
I think number fields will frequently be relative extensions, and we'll also consider ideals both in the maximal order and in suborders.  Pari will likely have almost nothing to do with our general relative extensions (it's only currently used for relative extensions as a miserable crutch), and HNF doesn't apply for ideals in orders.

PROS:
When it works, hashing based on the HNF has the property that if I==J then hash(I) == hash(J).  That's a very good property to have.   With hashing of gens that fails. 

Thus taken together, I'm OK with your proposal with the caveat that at some future time it has to be revisited for *relative* extensions.


---

Comment by was created at 2010-08-14 00:57:06

apply only this patch (which also addresses the referees issue with __hash__)


---

Attachment

OK, new patch up that changes __hash__.  It passes all doctests on sage.math.


---

Comment by jdemeyer created at 2010-08-14 22:36:27

The patch introduces an inconsistency:


```
sage: K.<a> = NumberField(x^3-7)
sage: K.ideal(12*a + 5).factor()
(Fractional ideal (101, a - 8)) * (Fractional ideal (11, a + 5))^2
```



```
sage: K.<b> = NumberField(x^3-10001)
sage: L.ideal(b+1).factor()
(Fractional ideal (b + 1, 1667)) * (Fractional ideal (b + 1, 2)) * (Fractional ideal (b + 1, 3))
```


Note how the integer is printed first in the first case but last in the second case (and personally I find it clearer when the integer is put first).  Maybe the sorting and uniqueing should be done in the NumberFieldIdeal constructor instead of when the ideal is printed?


---

Comment by was created at 2010-08-15 17:16:40

> Note how the integer is printed first in the first case but last in the second case (and personally I find it clearer when the integer is put first).  Maybe the sorting and uniqueing should be done in the NumberFieldIdeal constructor instead of when the ideal is printed?

Would that make any difference?  The difference above is that in one case the number field has a very small discriminant (-1323), and in the other it doesn't (-2700540027).   When the discriminant is small, then reduced generators are used for printing.   A solution could be to apply the sorting and "uniquing" in both cases before printing -- right now it is only applied in the case of large discriminant.


---

Comment by was created at 2010-08-15 17:46:31

Hi,

I retract my comment.  The issue may be that sorting of elements of number fields is now useless.  Observe:

```
sage: L.<b> = NumberField(x^3-10001)
sage: b+1 < L(1667)
False
sage: L(1667) < b + 1
False
```

Thus it doesn't matter *what* you do with sorting and uniquing the gens before or after -- there's no sensible ordering that will come out of this, unless elements of number fields get a total (non-algebraic) ordering.  I thought they had one. 

Oh, now I remember -- there is a *major bug* in the way elements of number fields are ordered.  You can see this by looking at the code (I think Joel Mohler) wrote in number_field_element.pyx.  I fixed this a few weeks ago as part of the patch bomb #9541.   

So my advice is to not worry about sorting issues as part of *this* patch, but keep in mind that it is has to be fixed later.  I've opened ticket #9752 to fix this.


---

Comment by jdemeyer created at 2010-08-16 20:23:22

Always using `gens()` for printing is also silly, because for larger degrees you can get something like:


```
sage: x=polygen(QQ); K.<a> = NumberField(x^8+x-1);
sage: J1 = K.ideal(a+1); J2 = K.ideal(a+2); J = J1.intersection(J2)
sage: J
Fractional ideal (a^2 + 249, -a^7 + 125, a + 2, a^3 + 8, a^4 + 237, -a^7 - a^6 + 189, a^7 + a^6 + a^5 + 96, 253)
```


In my opinion, the best way would be to use `idealtwoelt()` for large discriminants instead of simply printing all generators (or alternatively: reduce the generators using `idealtwoelt()` in `__init__`).


---

Comment by was created at 2010-08-18 00:18:14


```
On Tue, Aug 17, 2010 at 5:03 PM, Chan-Ho Kim <chanho.math> wrote:
> Dear William,
> I think that there is a bug on trac 9400 patch.
> My current SAGE is (SAGE 4.5.2 + trac 9400 patch only) in VM.
> When I use `maximize_at_prime,'
>
> K.<a> = NumberField(x^6 + 9*x^5 - 8410*x^4 - 88580*x^3 + 18705368*x^2 +
> 99820416*x - 12230355456, maximize_at_primes=[3]) ; K.primes_above(3)
> this decomposition in K works as you mentioned.
>
> However, in this ``small'' number field
>
> F.<a> = NumberField(x^3 - x^2 - 24*x + 32, maximize_at_primes=[3]) ;
> F.primes_above(3)
> the low precision error occurs if I add `maximize_at_primes=[3].'

That's not a bug in maximize_at_primes or finding the primes above 3.   But it *is* an issue with *printing* the ideals out that it finds over 3.   Evidently, when printing is_principal is called on each ideal currently, and this leads to a problem.  This is not surprising, given that deciding whether or not an ideal is principal requires knowing the class group in general, and the equation order of F that you define above is not only deficient at 3.  You need to also maximize at 2.   See:

sage: F.<a> = NumberField(x^3 - x^2 - 24*x + 32, maximize_at_primes=[2,3]) 
sage: F.primes_above(3)
[Fractional ideal (-1/2*a^2 - 3/2*a + 5), Fractional ideal (-1/2*a^2 + 5/2*a - 1)]

So in short, this is not a bug.  If you try to compute with number fields and pass in the maximize_at_primes option, certain things can't possibly work.

That said, I'm not a big fan of how ideals print.  Maybe Jereon's suggestion -- just *always* print with the PARI 2-element representation -- is the way to go.  That might get around this problem. 


> BTW, I also have one more question:
> Can I add `maximize_at_prime=[p]' in `hecke_eigenvalue_field()'?

You'll have to dive in and start hacking at the source code of Sage to do that....

 -- William
```



---

Comment by jdemeyer created at 2010-08-18 21:20:49

I am not familiar with `_pari_` and `_pari_init_`, but why does NumberField need `_pari_init_`?  Can't we add instead a `_pari_` method which returns `pari_nf()`?


---

Comment by jdemeyer created at 2010-08-18 21:26:11

Rebasing to #9343 will be easier if we seperate the "maximize_at_primes part" from the "printing and hashing of ideals" part.  So I will cut this patch in two pieces.


---

Comment by jdemeyer created at 2010-08-18 22:02:15

Patch for the "maximize at primes" part, rebased to sage-4.6.prealpha1 (see #9343)


---

Attachment


---

Comment by jdemeyer created at 2010-08-20 15:48:34

I attached a big reviewer patch (to be applied on top of 9400_maximize_at_primes.patch) changing:
 * the PARI functions `nfbasis()` and `nfinit()`: document and fix implementation.
 * change `pari_nf()` to always use `integral_basis()` (this means that all the `maximize_at_primes` code can be moved out of `pari_nf()`).
 * rename `_compute_integral_basis` to `_pari_integral_basis` and don't convert from PARI to Sage.
 * make the code for CyclotomicField more analogous to NumberField_generic (such that only `_pari_integral_basis` needs to be specialized, not `integral_basis()`.

Since the purpose of `_pari_init_()` is very unclear to me, I'm not sure what to do with that.


---

Comment by jdemeyer created at 2010-08-21 10:31:29

Apply on top of 9400_maximize_at_primes.patc


---

Attachment


---

Comment by jdemeyer created at 2010-08-24 19:34:30

Changing assignee from davidloeffler to jdemeyer.


---

Comment by jdemeyer created at 2010-08-24 19:34:30

Changing keywords from "" to "PARI number field".


---

Comment by cremona created at 2010-08-30 16:09:10

Since this ismarked "needs review" could the authors clarify which patches are up for review?  I assume it is 

```
9400_maximize_at_primes.patch 
Patch for the "maximize at primes" part, rebased to sage-4.6.prealpha1 (see #9343)
```

and

```
9400_jd_review.patch 
Apply on top of 9400_maximize_at_primes.patch
```

and not the first one.

Secondly, since these patches have been merged into 4.6.prealpha3 which I have successfully built and tested, I reckon that the only (!) remaining task as a reviewer is to look at the code in the patch, with the additional explanations on the ticket, and approve (or otherwise, maybe) of it?

I will try to do this before I go away on Friday for a week.  No promises...


---

Comment by cremona created at 2010-08-30 16:33:13

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-08-30 16:33:13

Looking at the 2nd and 3rd patches (separately) it looks very good to me.  For the benefit of others reading this, the essence of these patches (apart from some ReSTification) is to expose some additional functionality from the pari library to Sage, so that some computations can be mande very much faster (a *lot* faster!).

I spotted a few minor issues in docstrings (numbers refer to the ones I see in the third patch):


6451: second 'it' --> 'the'

6466: should have a preceding #, or replace ":" by "::" and insert a blank line after and change the preceding "TESTS::" to "TESTS:"

6592: change "TESTS::" to "TESTS:"

and also when I rebuilt the docs after "sage -ba"  (using 4.6.prealpha3) I got these ReST warnings:


```
docstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.
```


```
docstring of sage.libs.pari.gen.gen.nfbasis:8: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
```


```
docstring of sage.libs.pari.gen.gen.nfinit:19: (WARNING/2) Literal block expected; none found.
```


Modulo these, a positive review is on offer.  Hence "needs work", but it is only trivial work.


---

Comment by jdemeyer created at 2010-08-30 21:30:02

Thanks John, I will take care of these issues when I have time.


---

Attachment

Apply on top of previous 2 patches, small documentation fixes


---

Comment by jdemeyer created at 2010-09-05 13:28:43

Changing status from needs_work to needs_review.


---

Attachment

All 3 patches combined (apply only this patch)


---

Comment by jdemeyer created at 2010-09-05 18:46:31

I did all the changes requested by the reviewer.

Replying to [comment:22 cremona]:
> {{{
> docstring of sage.libs.pari.gen:136: (WARNING/2) Literal block expected; none found.
> }}}
This belongs to #9636 and is fixed there.  The other warnings are fixed here.


---

Comment by was created at 2010-09-07 16:14:42

Hi,

I tried to apply my patch to 4.5.2.rc0 and it works fine:


```
adding trac_9400.patch to series file
applying trac_9400.patch
now at: trac_9400.patch
```


I tried to apply your patch (9400_combined.patch) and there are a massive number of rejects:

```
adding 9400_combined.patch to series file
applying 9400_combined.patch
patching file sage/libs/pari/gen.pyx
Hunk #1 succeeded at 6408 with fuzz 2 (offset -32 lines).
Hunk #4 FAILED at 6964
Hunk #5 FAILED at 6991
2 out of 7 hunks FAILED -- saving rejects to file sage/libs/pari/gen.pyx.rej
patching file sage/rings/number_field/number_field.py
Hunk #13 FAILED at 2870
Hunk #16 FAILED at 3727
2 out of 25 hunks FAILED -- saving rejects to file sage/rings/number_field/number_field.py.rej
patching file sage/rings/number_field/number_field_ideal_rel.py
Hunk #2 FAILED at 592
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/number_field/number_field_ideal_rel.py.rej
patching file sage/rings/polynomial/polynomial_quotient_ring.py
Hunk #1 FAILED at 688
Hunk #2 FAILED at 1068
2 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_quotient_ring.py.rej
patching file sage/rings/residue_field.pyx
Hunk #17 succeeded at 427 with fuzz 2 (offset 0 lines).
Hunk #18 succeeded at 444 with fuzz 2 (offset 0 lines).
Hunk #19 FAILED at 463
Hunk #26 succeeded at 572 with fuzz 1 (offset -1 lines).
Hunk #27 FAILED at 589
2 out of 48 hunks FAILED -- saving rejects to file sage/rings/residue_field.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 9400_combined.patch
```



---

Comment by was created at 2010-09-07 16:14:42

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-09-07 16:34:14

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-09-07 16:34:14

Replying to [comment:28 was]:
> I tried to apply your patch (9400_combined.patch) and there are a massive number of rejects:

It is meant to be applied after #9343, then it works fine.


---

Comment by mpatel created at 2010-09-09 11:12:00

John, do Jeroen's most recent changes look good to you?


---

Comment by cremona created at 2010-09-09 14:39:47

Replying to [comment:30 mpatel]:
> John, do Jeroen's most recent changes look good to you?

Sorry for delay -- Jeroen has nudged me on this and I'll look at it as soon as I can, but I'm at a conference this week...


---

Comment by cremona created at 2010-09-11 16:31:03

Replying to [comment:30 mpatel]:
> John, do Jeroen's most recent changes look good to you?

The new combined patch does look good.  It applies smoothly to 4.6.alpha0, and the docs (re)build with no warnings.  I am currently doing a full test just to make sure.  Will report back shortly.


---

Comment by cremona created at 2010-09-11 16:43:08

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-09-11 16:43:08

Replying to [comment:32 cremona]:
> Replying to [comment:30 mpatel]:
> > John, do Jeroen's most recent changes look good to you?
> 
> The new combined patch does look good.  It applies smoothly to 4.6.alpha0, and the docs (re)build with no warnings.  I am currently doing a full test just to make sure.  Will report back shortly.

All (long) tests pass -- positive review.


---

Comment by mpatel created at 2010-09-15 10:39:38

Resolution: fixed


---

Comment by jdemeyer created at 2010-09-19 10:47:26

Replying to [comment:34 mpatel]:

Note that I mentioned  in this ticket (and on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ff993da70fc9f7ac)) that I do not understand `_pari_init_()`. I don't know if the reviewers do, so I'm a little bit worried about this.
