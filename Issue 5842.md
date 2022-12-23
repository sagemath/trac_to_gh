# Issue 5842: [with patch, needs review] Various number field improvements

Issue created by migration from https://trac.sagemath.org/ticket/5842

Original creator: fwclarke

Original creation time: 2009-04-21 08:34:09

Assignee: was

The attached patch (relative to 3.4.1.rc4) implements a number of changes to the number field
code.  All have corresponding doctests verifying the new behaviour.

In particular:

 * The following now works:    
   {{{
   sage: K.<a> = NumberField(x^2 + 5)
   sage: L.<b> = K.extension(x^2 + 1)
   sage: L.ideal(K.ideal(2, a + 1))
   Fractional ideal (-b - 1)
   }}}

 * `K.prime_factors` is defined for a number field `K`.  Thus
   {{{
   sage: CyclotomicField(3).prime_factors(7)
   [Fractional ideal (-2 *zeta3 + 1), Fractional ideal (2 *zeta3 + 3)]
   }}}

 * `K.pari_polynomial('a')` is now valid when `K` is a relative number field.
   Previously one could only specify the variable name for an absolute
   number field.

 * `list` has been rewritten for the class `CyclotomicFieldHomset` in `morphism.py`.
   Previously this failed for homomorphisms from `CyclotomicField(n)` to a 
   non-cyclotomic number_field if there were no `n`-th roots of unity in the 
   codomain.  The new code uses `zeta_order` to check whether there are any 
   homomorphisms.  This should be faster.

 * In `number_field_ideal.py`, `element_1_mod` has been rewritten to use the 
   pari function `idealaddtoone0`.  This is considerably faster.

 * `maximal_order` has been rewritten for relative number fields.  The
   previous version was repetitive and grossly wasteful of memory.  This 
   solves one aspect of #4738 ("finding maximal_orders of relative number 
   fields is very slow").  

 * `is_principal` and `gens_reduced` have been changed in
   `number_field_ideal_rel.py` so that if the ideal is principal, there is
   only one reduced generator (as already happens for ideals in absolute number
   fields).  The previous code did not work in all cases.  As a result, 
   the output of several doctests have needed changing, and (mostly) simplifying.

 * Minor change have been made to `reduced_basis` so that it works for cyclotomic 
   fields:
   {{{
   sage: CyclotomicField(12).reduced_basis()
   [1, zeta12^2, zeta12, zeta12^3]
   }}}

 * `zeta_function` now works for relative number fields.

 * In several places the code has been tidied up using the `map` function.

 * A version of `uniformizer` has been introduced for relative number fields.

 * The valuation at a prime ideal for elements of relative number fields has 
   been defined.

 * A minor change to the `conjugate` function settles #4725.

 * `relative_discriminant` in `number_field_rel.py` has been rewritten so that it
   uses PARI's `nf` rather than `bnf`, and is able to handle relative fields whose 
   base field is a relative field.

 * Made minor change to error messages for `zeta` in `number_field.py` and
   `order.py` to make them compatible.

 * A `subfields` function for relative number fields has been introduced. 
   Doctests have been added, and a minor change made, to the absolute version.

 * The relative version of `automorphisms` has been rewritten so that it handles 
   correctly fields where the base field is relative.




---

Attachment

Partial review:  this all looks fantastically useful.  I have only skimmed the patch so far, and checked that it applies cleanly to 3.4.1.rc4.  But there are some test failures in sage/rings/number_fields (on a 64-bit machine):

```
jec@host-57-44%sage -t devel/sage-5842/sage/rings/number_field/
sage -t  "devel/sage-5842/sage/rings/number_field/totallyreal_phc.py"
         [1.0 s]
sage -t  "devel/sage-5842/sage/rings/number_field/number_field.py"
**********************************************************************
File "/home/jec/sage-3.4.1.rc4/devel/sage-5842/sage/rings/number_field/number_field.py", line 1788:
    sage: M.ideal(K.ideal(2, a))
Expected:
    Fractional ideal (-1/2*a*c - 1/2*a*b)
Got:
    Fractional ideal (1/2*a*c + 1/2*a*b)
**********************************************************************
File "/home/jec/sage-3.4.1.rc4/devel/sage-5842/sage/rings/number_field/number_field.py", line 2952:
    sage: L.factor(a + 1)
Expected:
    (Fractional ideal (1/2*b + 1/2*a + 1)) * (Fractional ideal (-1/2*b + 1/2*a - 1))
Got:
    (Fractional ideal (1/2*a*b - a - 1/2)) * (Fractional ideal (-1/2*b + 1/2*a - 1))

  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.
**********************************************************************
2 items had failures:
   1 of  10 in __main__.example_40
   1 of  13 in __main__.example_64
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/jec/sage-3.4.1.rc4/tmp/.doctest_number_field.py
         [18.7 s]
sage -t  "devel/sage-5842/sage/rings/number_field/number_field_morphisms.pyx"
         [2.2 s]
sage -t  "devel/sage-5842/sage/rings/number_field/totallyreal_data.pyx"
         [1.1 s]
sage -t  "devel/sage-5842/sage/rings/number_field/galois_group.py"
         [6.5 s]
sage -t  "devel/sage-5842/sage/rings/number_field/number_field_element_quadratic.pyx"
         [1.9 s]
sage -t  "devel/sage-5842/sage/rings/number_field/number_field_rel.py"
**********************************************************************
File "/home/jec/sage-3.4.1.rc4/devel/sage-5842/sage/rings/number_field/number_field_rel.py", line 2035:
    sage: list(K.ideal(u).factor())
Expected:
    [(Fractional ideal (2, -1/2*a + b + 3/2), 1),
     (Fractional ideal (2, -1/2*a + b + 1/2), 1),
     (Fractional ideal (5, (-1/2*b + 5/2)*a - 5/2*b - 11/2), 1),
     (Fractional ideal (7, (-1/2*b + 7/2)*a - 7/2*b - 15/2), 1)]
Got:
    [(Fractional ideal (2, -1/2*a + b + 1/2), 1), (Fractional ideal (2, -1/2*a + b + 3/2), 1), (Fractional ideal (5, (-1/2*b + 5/2)*a - 5/2*b - 11/2), 1), (Fractional ideal (7, (-1/2*b + 7/2)*a - 7/2*b - 15/2), 1)]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_66
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jec/sage-3.4.1.rc4/tmp/.doctest_number_field_rel.py
         [11.1 s]
sage -t  "devel/sage-5842/sage/rings/number_field/number_field_element.pyx"
**********************************************************************
File "/home/jec/sage-3.4.1.rc4/devel/sage-5842/sage/rings/number_field/number_field_element.pyx", line 2719:
    sage: P = K.prime_factors(5)[0]; P
Expected:
    Fractional ideal (((1/4*c + 1/4)*b - 1/4*c - 1/4)*a + (1/2*c + 1/2)*b - 1/2*c - 3/2)
Got:
    Fractional ideal ((-1/2*b - 1/2)*a + b + 1/2*c + 1/2)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_75
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jec/sage-3.4.1.rc4/tmp/.doctest_number_field_element.py
         [7.8 s]
sage -t  "devel/sage-5842/sage/rings/number_field/number_field_ideal_rel.py"
**********************************************************************
File "/home/jec/sage-3.4.1.rc4/devel/sage-5842/sage/rings/number_field/number_field_ideal_rel.py", line 436:
    sage: K.ideal(c).factor()
Expected:
    (Fractional ideal ((1/2*b*a - 1/2*b - 1/2)*c + (1/2*b - 1/2)*a))^2 * (Fractional ideal ((1/2*a - 1/2*b - 1/2)*c))
Got:
    (Fractional ideal ((-1/2*b*a + 1/2*b + 1/2)*c - a + 1))^2 * (Fractional ideal ((-1/2*b*a + 1/2*b + 1/2)*c))
**********************************************************************
File "/home/jec/sage-3.4.1.rc4/devel/sage-5842/sage/rings/number_field/number_field_ideal_rel.py", line 617:
    sage: z = I.element_1_mod(J); z
Expected:
    -8*b*a + 24
Got:
    -b*a + 1
**********************************************************************
File "/home/jec/sage-3.4.1.rc4/devel/sage-5842/sage/rings/number_field/number_field_ideal_rel.py", line 250:
    sage: I
Expected:
    Fractional ideal ((1/2*b + 1/2)*a - 3/2*b - 3/2)
Got:
    Fractional ideal ((-1/2*b + 1/2)*a + 3/2*b - 3/2)
**********************************************************************
3 items had failures:
   1 of  11 in __main__.example_13
   1 of   8 in __main__.example_22
   1 of   6 in __main__.example_8
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/jec/sage-3.4.1.rc4/tmp/.doctest_number_field_ideal_rel.py
         [3.1 s]
sage -t  "devel/sage-5842/sage/rings/number_field/order.py"
         [4.1 s]
sage -t  "devel/sage-5842/sage/rings/number_field/unit_group.py"
         [2.1 s]
sage -t  "devel/sage-5842/sage/rings/number_field/maps.py"
         [1.7 s]
sage -t  "devel/sage-5842/sage/rings/number_field/small_primes_of_degree_one.py"
         [2.3 s]
sage -t  "devel/sage-5842/sage/rings/number_field/totallyreal_rel.py"
         [2.0 s]
sage -t  "devel/sage-5842/sage/rings/number_field/all.py"
         [0.0 s]
sage -t  "devel/sage-5842/sage/rings/number_field/totallyreal.pyx"
         [3.8 s]
sage -t  "devel/sage-5842/sage/rings/number_field/class_group.py"
         [2.5 s]
sage -t  "devel/sage-5842/sage/rings/number_field/morphism.py"
         [2.0 s]
sage -t  "devel/sage-5842/sage/rings/number_field/number_field_base.pyx"
         [2.7 s]
sage -t  "devel/sage-5842/sage/rings/number_field/number_field_ideal.py"
**********************************************************************
File "/home/jec/sage-3.4.1.rc4/devel/sage-5842/sage/rings/number_field/number_field_ideal.py", line 719:
    sage: I
Expected:
    Fractional ideal (-1/2*a + 3/2)
Got:
    Fractional ideal (1/2*a + 3/2)
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jec/sage-3.4.1.rc4/tmp/.doctest_number_field_ideal.py
         [5.8 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-5842/sage/rings/number_field/number_field.py"
        sage -t  "devel/sage-5842/sage/rings/number_field/number_field_rel.py"
        sage -t  "devel/sage-5842/sage/rings/number_field/number_field_element.pyx"
        sage -t  "devel/sage-5842/sage/rings/number_field/number_field_ideal_rel.py"
        sage -t  "devel/sage-5842/sage/rings/number_field/number_field_ideal.py"
Total time for all tests: 82.1 seconds
```

That was on a 64-bit machine; no problems on 32-bit.  This is typical behaviour with pari number field functions.  When I made unit_group.py I could not come up with any way of getting around this variability, and ended up adding # random to the offending tests, which is hardly a good solution.


---

Comment by fwclarke created at 2009-04-21 11:53:21

I found a few like this (on a 32-bit machine).  

Unless the output is what is being tested, I think the best way 
round the problem is (taking, for example, the first failure 
listed above) rather than use tests like:

```
sage: M.ideal(K.ideal(2, a))
Fractional ideal (-1/2*a*c - 1/2*a*b)
```

to say:

```
sage: M.ideal(K.ideal(2, a)) == M.ideal(a*(b - c)/2)
True
```


I'll try to make a new patch on these lines.


---

Comment by fwclarke created at 2009-04-21 20:53:17

In a new patch (to apply on top of the first one), I've amended the offending doctests, mostly in the way I described above,
others using # random.  On a my 32-bit machine this meant that a couple of other doctests had to be altered a little.

I hope the 64-bit behaviour is OK.


---

Comment by fwclarke created at 2009-04-21 20:54:28

to apply after trac_5842.patch


---

Attachment

Sorry Francis,  I never noticed that you had put up a second patch.  I'll take another look, though I rather fear this will need some work to rebase onto 4.0.1.  John


---

Comment by davidloeffler created at 2009-06-08 08:38:21

I'm changing the status so this shows up in the "needs review" list.

Even once we get this rebased to 4.0.1, it is highly likely it will conflict with #6188 (and possibly also #6204) -- I will see if I can rebase it to 4.0.1 + these.

David


---

Comment by davidloeffler created at 2009-06-08 15:30:10

rebased, apply over 4.0.1 + the two patches at #6188


---

Attachment

I've done a rebased patch, to be applied to 4.0.1 plus the #6188 patches, which is equivalent to the two patches above. I've also fixed some minor docstring formatting errors. It passes doctests both on my laptop (32-bit) and sage.math (64-bit). As John says above, this is all fantastically useful, and should make relative number field arithmetic much more usable -- which I welcome a great deal, since I need it rather heavily for my research right now :-) Positive review.


---

Comment by ncalexan created at 2009-06-13 20:26:26

Resolution: fixed
