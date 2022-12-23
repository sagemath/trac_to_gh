# Issue 8335: Finite Field lattices

Issue created by migration from https://trac.sagemath.org/ticket/8335

Original creator: roed

Original creation time: 2010-02-23 17:26:08

Assignee: AlexGhitza

CC:  defeo rbeezer hds simonking zimmerma caruso pbruin mraum fstromberg jcooley davidloeffler dfesti

Implements coercion within lattices of finite fields lying above the same prime.


```
sage: k = GF(9)
sage: l = GF(27)
sage: x = k.gen() + l.gen(); x
z6^5 + 2*z6^4 + 2*z6^3 + z6^2 + 2*z6 + 1
sage: x.parent()
Finite Field in z6 of size 3^6
```


This feature is implemented for fields outside the range of the Conway polynomial database by the implementation of a function for finding pseudo-Conway polynomials: polynomials that satisfy all of the algebraic constraints on Conway polynomials without the lexicographic constraint that imposes uniqueness.

Finite fields no longer require an explicit variable name (though they still accept one).  If a variable name is given, then outside the range of the Conway polynomial database a random or sparse polynomial is used for speed reasons; if no variable name is given then either a Conway polynomial or pseudo-Conway polynomial is used.

Also adds methods `any_root` and `squarefree_decomposition` to polynomials over finite fields.


---

Comment by roed created at 2010-02-23 17:33:25

Changing status from new to needs_review.


---

Comment by roed created at 2010-02-23 17:33:25

Changing type from defect to enhancement.


---

Comment by roed created at 2010-02-23 17:37:08

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.


---

Comment by roed created at 2010-02-23 17:50:46

Includes everything in 8218, 8332, 7880, 7883, 8333, 8334 and 8335 except the 8218 bundle, which you must apply first.


---

Attachment

For convenience, I added a giant patch which includes all the changes except the bundle at 8218 (which we want to leave as a bundle in order to preserve file history).


---

Comment by davidloeffler created at 2010-04-20 10:31:13

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-04-20 10:31:13

This doesn't apply cleanly: the patch `8335_pseudo_conway.patch` seems to conflict with something. FWIW, I am using 4.4.alpha0 with qseries

```
trac_8446.patch
trac_8446_microfix.patch
trac_8722.patch
7883_ideals.patch
8333_parent_init.patch
8333_finite_fields_to_new_coercion.patch
7585_9_1_frac_and_coerce_updates.patch
8334_residue_fields-rebased_for_8446.patch
7585_12_1_fixes.patch
8335_pseudo_conway.patch
```



---

Attachment

Apply first


---

Comment by roed created at 2011-06-21 21:43:48

Changing status from needs_work to needs_review.


---

Comment by roed created at 2011-06-22 07:51:14

To work against 4.7, apply 8335_pseudo_conway.patch then 8335_finite_field_coerce_vs_47.patch.


---

Comment by roed created at 2011-06-22 08:53:25

Apply second


---

Attachment

Against 4.7 for patchbot


---

Attachment

To work against 4.7, apply 8335_pseudo_conway.patch then 8335_finite_field_coerce_vs_47.patch.


---

Comment by roed created at 2011-06-22 08:56:02

Apply 8335_pseudo_conway.patch, 8335_finite_field_coerce_vs_47.patch


---

Comment by defeo created at 2011-07-13 07:04:11

Changing status from needs_review to needs_work.


---

Comment by defeo created at 2011-07-13 07:04:11

I still get the following failures on 4.7.1.alpha4 with 8335_pseudo_conway.patch and 8335_finite_field_coerce_vs_47.patch applied:


```
	sage -t -long devel/sage/sage/matrix/matrix2.pyx # 2 doctests failed
	sage -t -long devel/sage/sage/rings/finite_rings/constructor.py # 1 doctests failed
```



---

Comment by defeo created at 2011-07-13 18:20:57

I also get 7 warnings when building the docs. These all seem to be missing blank lines and unmatched backquoutes in `sage/rings/finite_rings/constructor.py`


---

Attachment

Patch for PCP; rebased on top of 5.7.beta3.


---

Attachment

Patch for coercion; rebased on top of 5.7.beta3.


---

Comment by jpflori created at 2013-02-08 14:31:06

Patch for doc fixes; rebased on top of 5.7.beta3.


---

Attachment

These patches were quite old and things have moved around since they were written.
As a consequence, part of the old patches now apply to different files, that is the case of the NTL GF2E implementation which has been split in a Python and a Cython file.

Some pseudo Conway polys changed so that two doctests now fail (not corrected in the patches cause I did not take the time to think about it, feel free to do it).
As these pseudo Conway polynomials are not unique, I'm not sure if the procedure to generate them is deterministic or to which point randomness comes into play and if the failing doctests are just due to some routine called during the generation which may give a different result since the patches were originally written.

Not really sure how to cast restriction on the is_square and squarefree_decomposition methods, nor what I've changed makes sense, I've come up with this quickly, feel free to correct it.
The basic problem was that now Sage supports function fields where we have no p-th roots and that raised an AttributeError when calling is_square which called squarefree_decomposition in some doctests.

The doc now builds ok and looks nice (although I did not have LaTeX on my computer), but may need some revamping.
Nonetheless it would be great to get this in quickly.


---

Comment by jpflori created at 2013-02-08 14:40:16

Changing status from needs_work to needs_info.


---

Comment by jpflori created at 2013-02-08 14:59:55

I've just launche "make ptestlong" (only tested the ring dir before) and saw some errors on screen, will report later.


---

Comment by jpflori created at 2013-02-09 13:57:17

Fixes


---

Attachment

There were problem doing coercion because Sage now tried to define algebraic extension of Integers(1) and failed on ArithmeticError when trying 0^0, or depth of recursion if that was changed to return 1.

I've added an extension method to the IntegerModring_generic class to handle separatly this ring.

Did not check everything is fine though.


---

Comment by hds created at 2013-02-14 09:53:21

I went looking through some papers by Heath and Loehr and it appears that the output of an algorithm to compute a pseudo-conway polynomial will most likely not be deterministic unless `f.any_root()` is deterministic for polynomials in finite fields (something I'm not entirely sure about).

In this case, I'm not sure what to do about the tests, but I agree that it would be nice to move this patch along - but I'm not qualified to review it.


---

Comment by jpflori created at 2013-02-14 09:56:15

We have some Sage meeting near Paris in France today, with a tutorial about ... finite fields.
We'll try to polish this one up there.


---

Comment by roed created at 2013-02-14 10:45:41

Fantastic!  I've been meaning to get back to this but have been busy with other things.  Let me know what comes up and I can review your changes if necessary.


---

Comment by jpflori created at 2013-02-14 16:08:26

That got broken again in 5.7.b4 by #13064.


---

Comment by jpflori created at 2013-02-14 16:22:35

Rebased on top of 5.7.b4.


---

Comment by jpflori created at 2013-02-14 18:53:52

With the last set of patches, it passes make ptestlong except:
* one test in finite_rings/constructor.py because of a warning about Cunningham table, this does not seem harmful, so we should just change the test.
* two tests in matrix2.py which is more worrying, although I did not really looked at it, because some "is in prime field?" fails.


---

Comment by jpflori created at 2013-02-18 16:21:36

I've fixed some additional stuff and have new two concerns (in addition to the matrix2 stuff I've not dealt with):
* the cunningham tables did not get standard so we cannot really use them (or we'll get that warning which will make one doctest fail), not sure we can trigger their use iff they are installed to avoid this spurious warning
* as of now, if no name is provided when an extension field is trigerred and modulus is 'default' then it becomes 'conway' and that will potentially need the factorization (or the prime factors) of (p^n - 1), which might not be a good idea, so i'd prefer to just look to raise an error as before, or at least trigger a warning.


---

Comment by jpflori created at 2013-02-18 16:34:51

The problem with matrix2.pyx is with multiplying a matrix with coefficients living in Q with a matrix with elements in an extension field.
It seems the coercion model tries to put the second one in the prime subfield and fails with the "not in prime field" TypeError.


---

Comment by jpflori created at 2013-02-18 16:50:06

This is caused by the "fix" I proposed before to return IntegerMod(1) for algebraic extension of IntegerMod(1), because now I feel a common parent is chosen as IntegerMod(1), but this is a prime field and the element from the extension field "cannot" be cast there.

A proper solution could be to investigate the infinite loop we get when the ArithmeticError is replaced with returning a unit when computing 0^0.
Another solution might be to forbid extension of IntegerMod(1) so that we don't get crappy common parents.


---

Comment by jpflori created at 2013-02-19 18:05:58

I think I got the infinite loop.

During the initialization of the quotient ring, when trying to create the "one" element from the quotient ring of integer mod 1 quotiented by something, it tries to compute a remainder in polynomial_quotient_ring_element.py: "polynomial %= f" around line 137 but the mod operation is not defined for the Polynomial_ring_dense class, so this raises an AttributeError and falls back to the fallback implementation which tries to compute 0^0 which now tries to create 1 which is looked up for at the position 1 of a table of precomputed value of length the modulus+1 = 1 which is surely non sense, fails to create a IntegerrMod_int and raises a TypeError which gets caught in polynomial_quotient_ring.py around line 430 and loops...


---

Comment by jpflori created at 2013-02-19 18:16:43

And of course if we return 0 (== 1) for 0^0, then the generic quo_rem loops forever as we are computing 0 % 0 and the degree will never fall...


---

Comment by jpflori created at 2013-02-20 16:08:47

Forget my rant about something becoming conway and having potential performance issues.
It only occurs if we have the conway polynomial precomputed, so no worries.

I've removed the code calling factor_cunningham unconditionally (or rather, not through an option as in finite_rings/element_base.pyx).
At some point this should get automatically triggered when cunningham tables are included (#7240, #12133) and integer factorization is improved (#12125, #12117), so calling factor_cunningham directly won't be that useful anyway.


---

Comment by jpflori created at 2013-02-21 10:11:58

The doctests which changed were surely not caused by different randomness but because some checks in compute_pseudo_conway_polynomial were wrong, e.g. the results for next_prime(10000)**11 was x^11 + x + 7 whose root is not of order p^11-1 but p^11-1/2


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by jpflori created at 2013-02-22 10:54:33

Changing status from needs_info to needs_review.


---

Comment by jpflori created at 2013-02-22 10:54:33

The patches should be quite ok now.
This needs 5.8.beta0, or at least > 5.7.beta4.
I've made quite a bit of changes to all the coercion stuff, so that definitely needs review.
With a minimal set of changes to sources files you can now create algebraic extensions of the Integers(1) and let it be considered as a quotient of a univariate poly ring, etc. and everything that came up when I was trying to rebase the patches.
In particular, now the modulus var of an AlgebraicExtensionFunctor is always a polynomial, but I've added an additional optional field named conway to encode the fact we're dealing with pseudo-conway extensions of ff.

Please test, rant, whatever!


---

Comment by jpflori created at 2013-02-22 12:04:28

This passes "make ptestlong" on a usual x86_64 ubuntu 12.04.1.


---

Comment by roed created at 2013-02-22 12:05:52

Awesome!  I will take a look this weekend.


---

Attachment

Previous version was not qrefreshed...


---

Attachment

Should really be ok now... sorry for the noise.


---

Comment by defeo created at 2013-02-25 18:27:29

Got the following failures


```
sage -t -long devel/sage/sage/coding/code_constructions.py # 90 doctests failed
sage -t -long devel/sage/doc/en/thematic_tutorials/group_theory.rst # 1 doctests failed
sage -t -long devel/sage/sage/modular/arithgroup/arithgroup_perm.py # 1 doctests failed
sage -t -long devel/sage/sage/groups/matrix_gps/matrix_group.py # 1 doctests failed
sage -t -long devel/sage/sage/homology/examples.py # 7 doctests failed
```


They seem unrelated, though, and disapperead upon second testing. I'll dig the code and try to give a review in the next weeks.


---

Comment by saraedum created at 2013-03-18 06:54:20

Apply trac_8335-pseudo_conway-5.8.b0.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.8.b0.patch


---

Comment by jpflori created at 2013-05-13 14:39:02

Did anyone actually had the time to look at this?
It would have been great to have that in Sage during the FLINT workshop last week to check some results using Sage rather than Magma.

I'm ok with what David initially did modulo what had to be fixed and that I hopefully fixed.
So what's left to do is to review the rebasing and changes I introduced.
Note that I did not check that the patches still cleanly apply, that may be an issue now.


---

Comment by saraedum created at 2013-05-13 16:41:43

Replying to [comment:42 jpflori]:
> Did anyone actually had the time to look at this?
I started to look at it a while ago…

> So what's left to do is to review the rebasing and changes I introduced.
That's good to know. I don't want to make any promises about reviewing this but I would certainly like to see this in sage. In any case, I won't review this in the next three weeks.


---

Comment by jpflori created at 2013-05-15 14:48:33

Apart from fuzz 2, it still applies cleanly to 5.10.beta3 and all tests passes.
Not sure what the patchbot complains about, missing docstrings?


---

Attachment

Apply trac_8335-pseudo_conway-5.8.b0.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.10.b3.patch


---

Comment by saraedum created at 2013-05-16 13:15:05

apply trac_8335-pseudo_conway-5.10.b3.patch trac_8335-finite_field_coerce-5.8.b0.patch trac_8335-fixes-5.8.b0.patch


---

Comment by jpflori created at 2013-06-04 09:09:14

This definitely lacks "going down", e.g. taking the trace from a finite field to a subfield and being able to recognize that as an element of the subfield.
But let's keep that for another ticket.


---

Comment by defeo created at 2013-06-17 16:45:48

Changing keywords from "" to "days49".


---

Comment by defeo created at 2013-06-17 16:45:48

Changing status from needs_review to needs_info.


---

Comment by defeo created at 2013-06-17 16:45:48

Hi,

The doc in `constructor.py` says


```
 - ``modulus`` - blabla
   - 'default': a Conway polynomial is used if in the database. Otherwise 
     a sparse polynomial is used for binary fields and a 
     random polynomial is used for other characteristics. 
```


but I got the impression that the default is to use pseudo-conway. By the way, is it reasonable to use pseudo-conway as default ? It is utterly slow !


```
sage: %time k = GF(next_prime(100000)^2) 
CPU times: user 16.41 s, sys: 0.05 s, total: 16.45 s
Wall time: 16.18 s
sage: %time l = GF(next_prime(100000)^3) 
CPU times: user 60.19 s, sys: 0.07 s, total: 60.26 s
Wall time: 59.97 s
sage: %time (k.gen() + l.gen()).parent()
CPU times: user 0.08 s, sys: 0.00 s, total: 0.09 s
Wall time: 0.07 s
Finite Field in z6 of size 100003^6
```


Compare this with Magma


```
> time k := GF(NextPrime(100000)^2);                                                                                                  
Time: 0.000
> time l := GF(NextPrime(100000)^3); 
Time: 0.000

> time CommonOverfield(l, k);              
Time: 0.030
```


Wouldn't it be better to keep using ``random`` as default, and give error messages suggesting to use ``conway`` when the user tries to add/multiply/whatever two elements in different fields?


On another note, I get the following messages (I suppressed them from the output above for readability).


```
sage: k = GF(next_prime(10000)^11)
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
  ***   Warning: Mod(a,b)^n with n >> b : wasteful.
```


Any ideas on these?


---

Comment by jpflori created at 2013-06-17 16:53:53

Replying to [comment:49 defeo]:
> Hi,
> 
> The doc in `constructor.py` says
> 
> {{{
>  - ``modulus`` - blabla
>    - 'default': a Conway polynomial is used if in the database. Otherwise 
>      a sparse polynomial is used for binary fields and a 
>      random polynomial is used for other characteristics. 
> }}}
> 
> but I got the impression that the default is to use pseudo-conway. By the way, is it reasonable to use pseudo-conway as default ? It is utterly slow !
It is and is expected to be.
> 
> {{{
> sage: %time k = GF(next_prime(100000)^2) 
> CPU times: user 16.41 s, sys: 0.05 s, total: 16.45 s
> Wall time: 16.18 s
> sage: %time l = GF(next_prime(100000)^3) 
> CPU times: user 60.19 s, sys: 0.07 s, total: 60.26 s
> Wall time: 59.97 s
> sage: %time (k.gen() + l.gen()).parent()
> CPU times: user 0.08 s, sys: 0.00 s, total: 0.09 s
> Wall time: 0.07 s
> Finite Field in z6 of size 100003^6
> }}}
> 
> Compare this with Magma
> 
> {{{
> > time k := GF(NextPrime(100000)^2);                                                                                                  
> Time: 0.000
> > time l := GF(NextPrime(100000)^3); 
> Time: 0.000
> 
> > time CommonOverfield(l, k);              
> Time: 0.030
> }}}
> 
I think the rationale is that Sage did not support finite fields with unnamed generator before this patch.
So IIRC you could simply not do the above.
If you do something which used to work like

```
K.<a> = GF(182918291829182918291892819)
```

(assuming the random typing is some prime power)
I think it still picks up a random modulus as before (and is fast enough).

I agree it's kind of a bad thing to provide a new (but still natural, especially for Magma's users) way to create finite fields which is horribly slow.
So we might want to fix this.

Also note that this ticket only provides lattices for finite fields created with pseudo-conway polynomials.
The goal is not to provide (compatible) embeddings for all finite fields (as Magma is capable of).
> Wouldn't it be better to keep using ``random`` as default, and give error messages suggesting to use ``conway`` when the user tries to add/multiply/whatever two elements in different fields?
> 
> 
> On another note, I get the following messages (I suppressed them from the output above for readability).
> 
> {{{
> sage: k = GF(next_prime(10000)^11)
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
>   ***   Warning: Mod(a,b)^n with n >> b : wasteful.
> }}}
> 
> Any ideas on these?
No idea, I'll check tomorrow.


---

Attachment


---

Comment by jpflori created at 2013-06-18 14:32:09

Changing status from needs_info to needs_review.


---

Comment by jpflori created at 2013-06-18 14:32:09

There was some actual bug in the code which triggered the computation of the pseudo-Conway polynomials tree twice in the case where the extension degree was prime.
First the way it should, and then using the same arguments as in the case where this degree is not prime which at some point triggered the computation of the power of modular integer with a small modulus and a huge exponent and PARI rants when you do that;
just try

```
Mod(3,5)._pari_()**28172187218728127182718271821982918291829182918291
```


So the newly uploaded patch makes it so we only build the tree once as we always should have, and at least in Luca's example it prevents PARI rants to get on the screen.


---

Comment by jpflori created at 2013-06-18 14:38:33

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-06-18 14:38:33

If you try

```
GF(next_prime(10000)^12
```

which is a non-prime extension you still get PARI's rants on-screen.

More worrying is that

```
GF(next_prime(10000)^14)
```

fails with an AssertionError.


---

Comment by jpflori created at 2013-06-18 15:12:38

All these troubles seem to come from the _find_pow_of_frobenius function (the algo used inside and arguments passed to it).


---

Comment by jpflori created at 2013-06-18 15:44:05

New patch which pushouts elements of two extension fields of same characteristic into the extension field with degree the lcm rather than the product as the old code used to do.


---

Comment by jpflori created at 2013-06-19 12:24:25

Thanks to Luca I had a look at the math part of the algorithms implemented and am not sure about all of it.
In particular, after a quick look, it seems to me that all the _frobenius_shift part is useless and all that should be implemented is the algorithm form HL99 without the last loop checking that the polynomial is indeed minimal for some order (e.g. the one used for conway polynomials).


---

Comment by jpflori created at 2013-06-19 20:58:12

I think I missed something in the algo so the above message is surely wrong, I need some more time...


---

Comment by jpflori created at 2013-06-20 11:49:57

I had another look at the proofs in the paper and the _frobenius_shift stuff definitely seems to make sense (on top of the fact that without it everything is broken :)), due to the fact we use actual concrete representations of the fields whereas the algorithm is somehow more abstract.

So now we're back with the problems from http://trac.sagemath.org/sage_trac/ticket/8335#comment:52.


---

Comment by jpflori created at 2013-06-20 11:57:34

This already fails with:

```
find_pseudo_conway_polynomial_tree(5,6,False)
```



---

Comment by jpflori created at 2013-06-20 12:12:45

I think the problem is that we don't (or not anymore, there used to be two calls to the PCPT constructor before in the case where n is prime) ensure consistency of roots chosen for prime degree extension (basically running kind of _frobenius_shift when n is prime).


---

Comment by jpflori created at 2013-06-20 12:19:56

That was easily fixed.

Note that

```
find_pseudo_conway_polynomial_tree(11,14,False)
```

seems to enter an infinite loop.


---

Comment by jpflori created at 2013-06-20 13:04:49

Ok, it seems the main issue now is that nth_root is slow for big parameters (or make the range() function oveflow).


---

Comment by jpflori created at 2013-06-20 13:11:49

The ovrflow happens because I wanted to let nth_root return all roots rather than just one as in David's code.

Using David's approach let the calculation for

```
GF(next_prime(10000**14))
```

finish (although we still get PARI's warnings but that's "not really" a problem).


---

Comment by jpflori created at 2013-06-20 13:14:00

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-06-20 13:14:00

Ok, the set of patch looks quite clean now, so back to needs_review.

The only thing not perfect is that we still get PARI's warning in some cases...


---

Comment by jpflori created at 2013-06-20 13:18:53

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-06-20 13:18:53

And back to needs_work, I did not check the doctests in the modified files.


---

Comment by jpflori created at 2013-06-20 13:32:39

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-06-20 13:32:39

Should be ok now.
Reverted David's test for primitivity rather than using is_primitive which would waste a lot of time factoring over and over q = p**n -1.


---

Comment by jpflori created at 2013-06-20 13:54:04

(Small fix to a silly typo)


---

Comment by jpflori created at 2013-06-20 15:43:51

Added some doctests hopefully showing that embeddings are correct and compatible.


---

Comment by jpflori created at 2013-06-20 17:23:38

Ok, the last tests I added:

```

        sage: old_exists_cp = sage.rings.finite_rings.constructor.exists_conway_polynomial
        sage: sage.rings.finite_rings.constructor.exists_conway_polynomial = lambda p, n: False
        sage: k = GF(3**10)
        sage: l = GF(3**20)
        sage: k.modulus() == conway_polynomial(3, 10)
        False
        sage: l(k.gen()**10) == l(k.gen())**10
        True
        sage: del k, l
        sage: import gc
        sage: gc.collect();
        sage: sage.rings.finite_rings.constructor.exists_conway_polynomial = old_exists_cp
```

introduced some failures in the test:

```
sage: GF.other_keys(key, K)
            [(9, ('a',), x^2 + 2*x + 2, None, '{}', 3, 2, True),
             (9, ('a',), x^2 + 2*x + 2, 'givaro', '{}', 3, 2, True)]
```

Indeed, although I explicitely asked to delete k and l and restored a proper exists_... function, the field GF(3**20) stay cached and so the pseudo-Conway, but not Conway, modulus used to build GF(3**2).

The reason for that is that we performed arithmetic on elements of k and l which triggered creation of an embedding of k into l which prevents the collection of k and l.
This is bad and is surely the same problem as in #14711.

So I just removed the hack forcing the use of pseudo-Conway polynomials.


---

Attachment


---

Comment by pbruin created at 2013-06-26 10:27:34

In relation to #12142, I am currently working on a patch that makes the construction of irreducible polynomials independent of the finite field implementations (prime_modn, givaro, ntl_gf2e, ext_pari and the future pari_ffelt).  Currently every finite field implementation has to do its own parsing of string values of modulus (like 'conway', 'random' etc.).  It would be more elegant to handle all these string values in the generic constructor, and always pass an actual polynomial to the finite field implementation.

In the current version of Sage, the only situation in which the implementation needs to know whether the field is defined by a Conway polynomial is when converting elements to GAP.  This means that always passing a polynomial as the modulus is fine, as long as one can check if the polynomial is a Conway polynomial if and when it is needed.  This is easy to do by checking the database.

With your patch, each implementation gets an increased dependence on string values for the modulus parameter.  I am wondering if this can be avoided by doing all the pseudo-Conway related stuff inside the generic finite field code.

[...to be continued...]


---

Comment by jpflori created at 2013-06-26 10:35:48

Replying to [comment:71 pbruin]:
> In relation to #12142, I am currently working on a patch that makes the construction of irreducible polynomials independent of the finite field implementations (prime_modn, givaro, ntl_gf2e, ext_pari and the future pari_ffelt).  Currently every finite field implementation has to do its own parsing of string values of modulus (like 'conway', 'random' etc.).  It would be more elegant to handle all these string values in the generic constructor, and always pass an actual polynomial to the finite field implementation.
> 
> In the current version of Sage, the only situation in which the implementation needs to know whether the field is defined by a Conway polynomial is when converting elements to GAP.  This means that always passing a polynomial as the modulus is fine, as long as one can check if the polynomial is a Conway polynomial if and when it is needed.  This is easy to do by checking the database.
Beware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.
In particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.

Also note that the real nice addition of this patch is mainly the compatible embeddings.
Indeed, for practical purposes, it seems that only the Conway polynomials from the databse will be used.
Constructing pseudo-Conway polynomials is quite as  slow as contructions genuine Conway polynomials so when you will actually use them, i.e. for quite large parameters because you have to be outside of the Conway database, it will already be quite slow and unpractical.

> 
> With your patch, each implementation gets an increased dependence on string values for the modulus parameter.  I am wondering if this can be avoided by doing all the pseudo-Conway related stuff inside the generic finite field code.
> 
> [...to be continued...]


---

Comment by pbruin created at 2013-06-26 12:16:44

Replying to [comment:72 jpflori]:
> Beware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.
> In particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.

OK, I'll try to find out if and how my ideas about making the choice of polynomial independently of the finite field implementation can be harmonised with your patch.  At first sight there does not seem to be a huge clash.  I am mostly worried about the use of strings like 'conwayz' as a modulus, which really seems to be overloading this parameter too much.

> Also note that the real nice addition of this patch is mainly the compatible embeddings.

I agree that this is a very desirable thing to have, and it is also nice to be able to simply type ``F = GF(p<sup>n</sup>)`` without having to care about variable names and embeddings.  I do think it is good to think carefully about how exactly to accomplish this.

In particular, I am not sure if it is wise to say in the documentation/specification that this compatibility is achieved using (pseudo-)Conway polynomials, since different implementations are imaginable.  I am thinking of the standard models for finite fields by Lenstra and de Smit, which are constructed in a way that does not seem to be related to Conway polynomials.

From a conceptual point of view, it is desirable that GF(p<sup>n</sup>) without any arguments should refer to the unique subfield of cardinality p<sup>n</sup> _inside a chosen algebraic closure_ of GF(p).  This gives 'compatible embeddings' the very simple meaning of 'inclusions within an algebraic closure'.

Such an algebraic closure could be implemented in different ways, for example via (pseudo-)Conway polynomials; algebraic closures of GF(p) resulting from different methods would be non-canonically isomorphic.  There might be a default choice that could change in the future, and the user should be able to specify which algebraic closure should be taken.

Here is how I would hope a hypothetical future Sage session to look like:


```
sage: p = 5
sage: Fpbar = GF(p).algebraic_closure()
sage: Fpbar
Algebraic closure of Finite Field of size 5
sage: Fa = GF(p^2, 'a')
sage: Fa
Finite field in a of size 5^2
sage: is_subfield(Fa, Fpbar)
False
sage: Fb = GF(p^2)
Subfield of size 5^2 of Algebraic closure of Finite Field of size 5
sage: is_subfield(Fb, Fpbar)
True
sage: type(Fpbar)
<class 'sage.rings.AlgebraicClosureFiniteField_pseudo_conway'>
```

Would something like this be easy to achieve once this ticket has been implemented?


---

Comment by jpflori created at 2013-06-26 12:58:23

Replying to [comment:73 pbruin]:
> Replying to [comment:72 jpflori]:
> > Beware that the last patch which contains my modification to the two original patches by David changes quite a lot of thing.
> > In particular, I think that with it modulus contains the real modulus as well and I use additional attributes to check for pseudo-Conway construction.
> 
> OK, I'll try to find out if and how my ideas about making the choice of polynomial independently of the finite field implementation can be harmonised with your patch.  At first sight there does not seem to be a huge clash.  I am mostly worried about the use of strings like 'conwayz' as a modulus, which really seems to be overloading this parameter too much.
> 
> > Also note that the real nice addition of this patch is mainly the compatible embeddings.
> 
> I agree that this is a very desirable thing to have, and it is also nice to be able to simply type ``F = GF(p<sup>n</sup>)`` without having to care about variable names and embeddings.  I do think it is good to think carefully about how exactly to accomplish this.
Agreed.
But it just happened I stumled upon this ticket which already looked usable (and was two years old) and thought "oh, let's already get this in; later on we can design better constructions of compatible embeddings and get something more general and fast".
So I decided to postpone the design of a cool and fast system in #8751 and only deal with "lattices using (pseudo) Conway polynomials" here.
It's better to have something than nothing.
> 
> In particular, I am not sure if it is wise to say in the documentation/specification that this compatibility is achieved using (pseudo-)Conway polynomials, since different implementations are imaginable.  I am thinking of the standard models for finite fields by Lenstra and de Smit, which are constructed in a way that does not seem to be related to Conway polynomials.
> 
I completely agree that using Conway polynomials is a no go as soon as you quit fields of small cardinalities.
I've met Eric Rains who participated in the Magma implementation (or at least the algos behind it) and he was nice enough to share with me a draft describing the algos used.

De Feo and Schost and others are also producing nice paper on how to build p- or l-adic towers of finite fields.
What is very nice is that they avoid linear algebra (what Magma may not completely do).
> From a conceptual point of view, it is desirable that GF(p<sup>n</sup>) without any arguments should refer to the unique subfield of cardinality p<sup>n</sup> _inside a chosen algebraic closure_ of GF(p).  This gives 'compatible embeddings' the very simple meaning of 'inclusions within an algebraic closure'.
> 
> Such an algebraic closure could be implemented in different ways, for example via (pseudo-)Conway polynomials; algebraic closures of GF(p) resulting from different methods would be non-canonically isomorphic.  There might be a default choice that could change in the future, and the user should be able to specify which algebraic closure should be taken.
> 
I agree, so it makes sense to have a pseudo Conway implementation and other ones later.
> Here is how I would hope a hypothetical future Sage session to look like:
> 
> {{{
> sage: p = 5
> sage: Fpbar = GF(p).algebraic_closure()
> sage: Fpbar
> Algebraic closure of Finite Field of size 5
> sage: Fa = GF(p^2, 'a')
> sage: Fa
> Finite field in a of size 5^2
> sage: is_subfield(Fa, Fpbar)
> False
> sage: Fb = GF(p^2)
> Subfield of size 5^2 of Algebraic closure of Finite Field of size 5
> sage: is_subfield(Fb, Fpbar)
> True
> sage: type(Fpbar)
> <class 'sage.rings.AlgebraicClosureFiniteField_pseudo_conway'>
> }}}
> Would something like this be easy to achieve once this ticket has been implemented?


---

Comment by pbruin created at 2013-06-26 13:08:10

I started to look at the patches, but was immediately struck by a problem that has nothing to do with finite fields.  In `QuotientFunctor._apply_functor`, the functor R -> R/IR (where I is an ideal of the base ring) to arbitrary rings.  This makes perfect sense for any R; you just happen to get the zero ring when IR = R.  The existing behaviour is certainly correct (although it is debatable whether the zero ring should be represented as `Integers(1)`).  Why would you want to raise an exception if R is a field?


---

Comment by jpflori created at 2013-06-26 13:18:23

I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).

I also agree returning the zero ring would be a better thing to do.
But then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...
See http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).


---

Comment by pbruin created at 2013-06-26 13:35:57

Replying to [comment:76 jpflori]:
> I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).

In the comments it says that the behaviour used to be to return the integer 0 (?!), and that this was corrected in #9138.  Now that the current implementation is correct, it would be very bad to change something fundamental like this just to make new patches work.

> I also agree returning the zero ring would be a better thing to do.
> But then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...
> See http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).

Then it seems to me that the generic constructions should be fixed.  Until then, any new code should take care that it does not use these constructions in cases where they fail.


---

Comment by jpflori created at 2013-06-26 14:04:53

Replying to [comment:77 pbruin]:
> Replying to [comment:76 jpflori]:
> > I think it was the historical Sage behavior until some recent ticket (don't really remember, you should be able to devise which one by looking at the hg log).
> 
> In the comments it says that the behaviour used to be to return the integer 0 (?!), and that this was corrected in #9138.  Now that the current implementation is correct, it would be very bad to change something fundamental like this just to make new patches work.
> 
> > I also agree returning the zero ring would be a better thing to do.
> > But then it breaks a bunch of generic constructions in Sage such as polynomial rings over {0} and quotients of it...
> > See http://trac.sagemath.org/sage_trac/ticket/8335#comment:24 and the few following comments (in case you manage to make some sense of my lonely rants).
> 
> Then it seems to me that the generic constructions should be fixed.  Until then, any new code should 
take care that it does not use these constructions in cases where they fail.
Of course.
But avoiding the coercion model is not that easy.

I'll give it a shot, but I cannot promise to come up with anything working.
Obviously I would have done that earlier if it was really easy.


---

Comment by jpflori created at 2013-06-26 16:00:39

In fact I think that putting back the correct behavior gives no problems and I added all needed fixes to make it work.

The real problem was that the quotient functor was applied before the fraction field one or the other way around and you always ended up working in the trivial ring.
So the easy way was raising an error.
But now the functors are applied in a more sensible it should not be a problem.

I'll upload a fixed patch when I make sure no tests fail.


---

Attachment

I have some failing tests on top of 5.11.b3 but they seem completely unrelated (something with get_test_shell() and I did not test a vanilla install, so they were surely there without these patches).


---

Comment by pbruin created at 2013-06-26 16:44:49

Continuing the discussion from #13214; in the context of my remark

>> there should probably be two categories into which a finite field can be put:
>> - the category of all finite fields. In this category, between any two objects there are either several morphisms or none at all, but no canonical one.
>> - the category of finite subfields of a given algebraic closure of Fp. In this category there is at most one morphism beteen any two objects, namely the inclusion qua subfields of the given algebraic closure.

Jean-Pierre Flori wrote (referring to the second option)

> #8335 provides such an imlementation, though it not really practical for large fields and there is no proper categorical framework as you suggest.
> This framework could be implemented in an independent ticket (and should if we want to be able to merge some tickets in a finite amount of time).

Certainly; both this ticket and #13214 are already large enough.  The question is whether (a draft of) a categorical framework (i.e. algebraic closure of *F*<sub>_p_</sub>) should be made first, or whether the new code from this ticket should be inserted into the current framework (which implements the first of the two categories) and be moved to a new framework as soon as we have it.

I would personally prefer the first option to keep things better packaged; this patch seems to make (pseudo-)Conway polynomials pop up in many different places, and moving them all to one place would require another intrusive Trac ticket later.


---

Comment by jpflori created at 2013-06-26 17:11:57

Replying to [comment:81 pbruin]:
> I would personally prefer the first option to keep things better packaged; this patch seems to make (pseudo-)Conway polynomials pop up in many different places, and moving them all to one place would require another intrusive Trac ticket later.
As far as functionalities are concerned, remember that Sage currently does not support 

```
K = GF(p^n)
```

So pseudo Conway polynomials never appear where they did not use to.
If you issue the command line which is currently supported:

```
K.<a> = GF(p^n)
```

you will get the exact same behavior as before, unless he specifies modulus="conway" and wants an extension of too large cardinality; maybe that should be changed back.

Nevertheless I agree that a user coming from Magma where

```
K := GF(p, n);
```

works might be confused...
Though the user might although expect embeddings of finite fields to work out of the box.

But as I just realized I guess your concern is about the dissemination of code.
From what I see, apart from code in finite_field_base.py, changes to specific finite field implementations mostly consists in replacing the part about Conway polynomials and tweak it to work with pseudo-Conway ones as well.
Nonetheless it's true that properly moving all of that later will be intrusive.

But what about plain Conway polynomials? Shouldn't that be moved as well?
Or do we consider they are standard enough to belong in the FiniteFields() category?
But if they do it would be a waste not to use automagically the fact that they provide simple embeddings into each other, wouldn't it? though it would make the separation between the plain finite fields and subfields of a given algebraic closure blurrier.

(As you can guess, I'd prefer to get this merged first especially because I hate seeing functional code bitrotting for years on trac, but I get your point :))


---

Comment by pbruin created at 2013-06-26 23:20:33

Replying to [comment:82 jpflori]:

> As far as functionalities are concerned, remember that Sage currently does not support 
> {{{
> K = GF(p^n)
> }}}
> So pseudo Conway polynomials never appear where they did not use to.
> If you issue the command line which is currently supported:
> {{{
> K.<a> = GF(p^n)
> }}}
> you will get the exact same behavior as before, unless he specifies modulus="conway" and wants an extension of too large cardinality; maybe that should be changed back.

Deciding what exactly `GF(p^n)` should mean (if it should mean anything at all) is an important design decision, and it is not at all obvious that Sage should make the same choice as Magma.  Probably it is better not to make this decision in this ticket, which already adds a lot of code.  Besides, letting an important change of behaviour depend whether the user specify a variable name or not sounds like a risky idea.  

> But what about plain Conway polynomials? Shouldn't that be moved as well?
> Or do we consider they are standard enough to belong in the FiniteFields() category?

They certainly belong to the general finite fields code, but not in any specific implementation, in my opinion.  In fact, the goal of the (by now 2) patches that I'm about to post is as follows:

- write a method `PolynomialRing_dense_finite_field.irreducible_element` (somewhat surprisingly the class did not exist yet) to generate an irreducible polynomial in that polynomial ring, allowing the user to optionally specify an algorithm (Adleman-Lenstra, Conway, random, lexicographically first, sparse);

- modify the `FiniteField` constructor to call this algorithm if the `modulus` argument is a string or `None`, and always pass an actual polynomial to the implementation class.

For backward compatibility (unpickling), the existing implementations will continue to accept string values for the parameter `modulus`, but new ones (such as the new PARI interface, see #12142) won't have to.  The idea is that the specific implementations should "concentrate on doing their job", and things related to magic values of `modulus` should be in only one place.

> But if they do it would be a waste not to use automagically the fact that they provide simple embeddings into each other, wouldn't it?

As I see it, that should depend on whether you are in the category of all finite fields or in the category of subfields of an algebraic closure of *F*<sub>_p_</sub>.

> (As you can guess, I'd prefer to get this merged first especially because I hate seeing functional code bitrotting for years on trac, but I get your point :))

Of course I understand that you want to see this finally appear in Sage, and I agree that it is a shame that Sage could have had something like this for years and still doesn't.  I guess it will be easier if this big ticket is split into smaller pieces.  It tries to do many rather different things at once: implement pseudo-Conway polynomials, adapt the construction of finite fields to use these, implement automatic coercion between the resulting fields, give a meaning to `GF(p^n)`, and in the process add some new methods to polynomial elements.  This makes it harder than necessary to understand and to review.


---

Comment by defeo created at 2013-06-27 02:55:43

Replying to [comment:83 pbruin]:

This discussion looks like the dear old dichotomy between quick feature integration and long specification design. 

Having some kind of support for lattices of finite fields has been a long standing request. I agree with pbruin that a better interface between generic finite fields and their actual implementation would be beneficial. But this ticket is ready for review, while pbruin's is not. Would it be that hard to adapt pbruin's or any other interface if this ticket is merged? I'm willing to give positive review to this ticket, if it stands some more testing, and it doesn't mess too much with #12142. 

I'm not convinced that the interface can be decided independently of the actual algorithms. Magma's interface is engineered around the fact that constructing fields is fast, but constructing the embeddings is slow (hence the Embed function, which must explicitly be called by the user). If Sage ends up having a different construction (e.g., De Smit-Lenstra lattices... although I've looked into it, and I don't think it is viable in general), I think the interface could be different.

There are many solutions to the compatibly embedded finite fields problem, no one being ideal. I'm more in favor of seeing them emerge in parallel, being developed in different tickets under different namespaces and APIs, rather than fixing the API now, and than realizing that it needs to be amended. Once a construction clearly stands out, then we can thrash it upon the user as the default ``GF(p<sup>n</sup>)`` construction (ok, this ticket is already thrashing, but it has the merit of being the first one!).


---

Comment by pbruin created at 2013-06-27 07:56:50

Replying to [comment:84 defeo]:
> Replying to [comment:83 pbruin]:
> 
> This discussion looks like the dear old dichotomy between quick feature integration and long specification design. 

Not quite; I am not at all advocating long specification design, and quick integration of new features (which I am all for) is in fact easier if they are smaller and don't intrude in places where they don't have to.

> Having some kind of support for lattices of finite fields has been a long standing request. I agree with pbruin that a better interface between generic finite fields and their actual implementation would be beneficial. But this ticket is ready for review, while pbruin's is not.

The part that is relevant for this ticket is now ready for review: see #14832 and #14833.

> Would it be that hard to adapt pbruin's or any other interface if this ticket is merged? I'm willing to give positive review to this ticket, if it stands some more testing, and it doesn't mess too much with #12142. 

I am actually in favour of quickly solving the main things that this ticket does (implementing pseudo-Conway polynomials and coercion between different finite fields).  I just think it shouldn't add more code to the finite fields implementations (Givaro, PARI etc.), and should not (or at least not yet) fix a meaning for `GF(p^n)`.


---

Comment by jpflori created at 2013-06-27 08:11:41

Ok, so I'll be the nice guy and try to rebase this ticket on top of your tickets.


---

Comment by jpflori created at 2013-06-27 08:11:41

Changing status from needs_review to needs_work.


---

Comment by pbruin created at 2013-07-13 21:05:09

Changing keywords from "days49" to "days49 sd51".


---

Comment by pbruin created at 2013-07-13 21:05:09

Replying to [comment:86 jpflori]:
> Ok, so I'll be the nice guy and try to rebase this ticket on top of your tickets.
Wonderful; these (#12142 and dependencies, maybe also #14888) should now be fairly stable.


---

Comment by jpflori created at 2013-07-18 14:18:26

I've begun rebasing, cleaning and splitting in a better way the patches here.

I have one question: in several finite field constructors based on a given implementation (let's say FiniteField_givaro), you can still pass the "modulus" parameter as a string and the routine corresponding to the given type of modulus is called.
IMHO this kind of defeats what Peter tried to do in #14832 and #14833 (though it predates these patcehs of course).
Any objection to change this behavior and instead more or less call the new irreducible_element function with the appropriate "algorithm" parameter?


---

Comment by jpflori created at 2013-07-18 14:27:37

(This will potentially introduce a slow down in some constructors, e.g. in finite_field_ntl_gf2e, but this can't really be helped.)


---

Comment by roed created at 2013-07-18 22:36:47

Replying to [comment:88 jpflori]:
> I've begun rebasing, cleaning and splitting in a better way the patches here.
> 
> I have one question: in several finite field constructors based on a given implementation (let's say FiniteField_givaro), you can still pass the "modulus" parameter as a string and the routine corresponding to the given type of modulus is called.
> IMHO this kind of defeats what Peter tried to do in #14832 and #14833 (though it predates these patcehs of course).
> Any objection to change this behavior and instead more or less call the new irreducible_element function with the appropriate "algorithm" parameter?

No, I have no objection to a more unified way of generating the modulus.


---

Comment by jpflori created at 2013-07-19 09:13:14

Ok so let's go this way.

As I'll be cut from the internet next week while the workshop in Leiden is taking place and I'm not sure what I'll be able to achieve today, here are some hints on what I plan to do.
Of course feel free to do something completely different and merge the ticket next week!

* rebase David's first patch (PC polys construction) on top of Peter's patches and include the relevant fixes (i.e. those only related to Conway and pseudo-Conway polynomials construction) from the "fixes" patch I posted here, move all the conway and pseudo-conway construction stuff to a separate file (I feel two files, one for Conway, one for pseudo-Conway, would be overkill, but all that stuff currently in constructor.py seems too much), maybe use two algo names "conway" for using the database and pseudo-conway to use the new code (and still use the database when possible). With the current patches, the PCPT is stored into the finite field (so that its not garbage collected), that is not possible with the new way of building moduli, so we have to think of another way, maybe store it in the modulus itself... (though the polynomial does not really care it's pseudo-Conway whereas the FF does). I don't think modifying irreducible_element() to return more stuff would be a good idea, any other advice welcomed!
* rebase David's second patch (coercion) on top of Peter's patches, include relevant fixes, do not define "GF" without names.
* keep the design of the AlgebraicClosure stuff for later, note that it should not be too hard to move later to the new framework, much less hard than implementing FFs through templates as for the p-adics and polynomial rings :)


---

Comment by jpflori created at 2013-07-19 14:29:36

I found no time to work on this today, so I'll just post the very rough and incomplete patch I produced yesterday evening, not sure it is worth anything, but just in case you can apply it after applying [attachment:trac_8335-pseudo_conway-5.10.b3.patch] (note that hg will rant and you'll get three rejection files in sage/rings/finite_rings/, just push the new patch on top of that).
Note it does not include anything from [attachment:trac_8335-fixes-5.11.b3.patch] yet.


---

Attachment


---

Comment by pbruin created at 2013-07-22 14:25:07

OK, thanks.  To begin with we'll start by trying to understand better how these patches work.


---

Comment by pbruin created at 2013-07-23 12:55:59

There are a few small problems with applying and testing this set of patches; I am now combining them into one patch that can be applied on top of 5.11.beta3 + (dependencies of this ticket) and that we can use as a starting point during Sage Days 51.


---

Comment by pbruin created at 2013-07-23 14:43:15

I'm going to split the following parts off into separate tickets, which will be dependencies of this one:

- the new squarefree decomposition code and the new `any_root` function;
- the code for pseudo-Conway polynomials.

These will hopefully be relatively easy to review.  We can then concentrate on implementing coercion between finite fields in this ticket.


---

Comment by pbruin created at 2013-07-23 15:47:33

Once #14957 and #14958 are stable enough, the next step will be to update [attachment:trac_8335-finite_field_coerce-5.8.b0.patch] and [attachment:trac_8335-fixes-5.11.b3.patch​], according to Jean-Pierre's plan from [http://trac.sagemath.org/ticket/8335#comment:91](http://trac.sagemath.org/ticket/8335#comment:91).


---

Comment by pbruin created at 2013-07-24 14:22:05

The patch [attachment:trac_8335_sd51.patch] contains the changes that remain after splitting off #14957 and #14958, and has been rebased on 5.11.beta3 + (dependencies of this ticket).

```
Patchbot: apply trac_8335_sd51.patch
```



---

Comment by pbruin created at 2013-07-25 07:27:00

to work on during Sage Days 51


---

Attachment

unified, rebased and cleaned up


---

Attachment

Besides everything else, the latest patch moves `_coerce_map_from_()` from the various finite field implementations to the `FiniteField` base class; it is now implementation-independent.  For this reason, this ticket now depends on #12142.  Various other changes have been made.

The syntax for constructing finite fields using Conway polynomials that admit automatic coercion is now

```
sage: F.<a> = FiniteField(5^3, conway=True, prefix='z')
```

This is not too pretty, but it is meant as a temporary solution until we have algebraic closures of finite fields.

Older patches on this ticket contained various changes that were in older attachments and that do not seem immediately relevant to this ticket.  I deleted those changes that seemed superfluous and kept those that I thought could be necessary after all.

This ticket should be reviewed once #14958 is done.

For patchbot:

```
apply trac_8335-finite_field_coerce-5.11.b3.patch
```



---

Comment by pbruin created at 2013-07-29 12:08:49

Changing status from needs_work to needs_info.


---

Comment by jpflori created at 2013-07-30 12:27:01

Changing status from needs_info to needs_review.


---

Comment by jpflori created at 2013-07-30 12:38:02

Rebased on top of #14888.


---

Attachment


---

Comment by jpflori created at 2013-07-30 12:44:43

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2013-07-30 12:44:43

Need to be rebased because of the name changes in #14958.


---

Comment by jpflori created at 2013-07-30 12:51:54

My bad.
I thought you still cached the lattice in the finite field but you don't.
(Un)fortunately when the lattice is built it is only weak-cached in conway_polynomials.py (so that it can be gc'ed when no finite field uses it anymore).

So either we have to store the lattice in the finite field to keep it alive and be able to use it when building extensions/pushouts and so on, or strongly cache it in conway_polynomials.py (I don't like that solution, in fact I hate caching things too much; note that currently everything is strongly cached anyway because of comment:69, #14711).


---

Attachment

Name changes in #14958.


---

Comment by jpflori created at 2013-07-30 13:31:37

In fact, the more I think about it, the less I like the way things are stored in the pseudo-Conway polynomial code.

We should make some big changes when implementing the AlgebraicClosure thing...
Has anyone open a ticket for that?


---

Comment by pbruin created at 2013-07-31 15:06:43

Replying to [comment:106 jpflori]:
> We should make some big changes when implementing the AlgebraicClosure thing...
> Has anyone open a ticket for that?
Not yet, as far as I have been able to find out; I can do it now.


---

Comment by pbruin created at 2013-07-31 17:00:25

Replying to [comment:106 jpflori]:
> In fact, the more I think about it, the less I like the way things are stored in the pseudo-Conway polynomial code.

I dislike it too.  It is problematic to store pseudo-Conway lattices globally in a Sage session (at least until they are garbage-collected) given that they are not uniquely defined.

It appears that the user could do the following:
- create a finite field _k_<sub>0</sub> using a primitive polynomial _f_<sub>0</sub>
- throw away _k_<sub>0</sub>, causing the pseudo-Conway lattice containing _f_<sub>0</sub> to be garbage-collected
- create a field _k_<sub>1</sub> using exactly the same command as for _k_<sub>0</sub>; this will be isomorphic to _k_<sub>0</sub>, but will in general be defined by a polynomial _f_<sub>1</sub> that is different from _f_<sub>0</sub>
- end up with a _k_<sub>1</sub> that is incompatible with things that were constructed with the help of _k_<sub>0</sub> (e.g. extensions of _k_<sub>0</sub>), even though both of them were generated using pseudo-Conway polynomials.

I was also worried that storing the pseudo-Conway lattice in the finite field would mean that we would forever have to keep suitable pickling/unpickling code around to deal with this.  Actually, this is not necessary, since the pseudo-Conway lattice can be reconstructed from the defining polynomial.  However, this does not seem to solve the above problem.  Using strong references does not solve it either.  In both cases, the user may pickle _k_<sub>0</sub>, restart Sage, create _k_<sub>1</sub>, and finally unpickle _k_<sub>0</sub>; then again _k_<sub>0</sub> and _k_<sub>1</sub> will be different in general.

All of this is basically a manifestation of the fact that "the" field of _p<sup>n</sup>_ elements is only defined up to non-canonical isomorphism.


---

Comment by jpflori created at 2013-07-31 17:09:31

I suggest we store a strong to the (top of the) lattice in the FF for the moment, as used to be done, and merge this ticket.

And let's think of a better design for #14990.
Having AlgebraicClosure object will surely greatly simplify this.


---

Comment by pbruin created at 2013-08-01 14:12:27

Replying to [comment:109 jpflori]:
> I suggest we store a strong to the (top of the) lattice in the FF for the moment

We could do that to make garbage collection less likely, but it won't really solve the problem, see comment:108.

> And let's think of a better design for #14990.
> Having AlgebraicClosure object will surely greatly simplify this.

Yes, the more I think about it, the more convinced I am that algebraic closures are the only real solution to the problem of compatible embeddings.

Jenny Cooley suggested the following idea, which I think is a good compromise: implement this ticket only for standard (not pseudo-) Conway polynomials.  Hopefully this would suffice for most practical purposes, and since they are uniquely determined, we wouldn't have to come up with half-baked solutions to the caching problem.  In #14990 (which I am working on now), pseudo-Conway polynomials can then finally be put to use, and they will be cached in the algebraic closure, where they really belong.


---

Comment by jpflori created at 2013-08-01 14:16:08

I'm ok with that.

I think I could accept anything as long as we close this ticket :)


---

Comment by pbruin created at 2013-08-02 11:02:25

use only (non-pseudo-)Conway polynomials


---

Attachment


---

Comment by pbruin created at 2013-08-02 11:06:44

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2013-08-02 11:10:21

For patchbot:

```
apply trac_8335-finite_field_coerce-5.11.b3-14888.patch​, trac_8335-no_pseudo.patch​ 
```

Note: [attachment:trac_8335-rebase_14958.patch​] is not needed if we go for this approach.


---

Comment by jpflori created at 2013-08-06 11:45:33

Looks ok.
Still depending on #14958 as functions related to (non-pseudo) Conway polys were moved around there.


---

Comment by jpflori created at 2013-08-06 11:45:33

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-10-12 09:45:04

Resolution: fixed
