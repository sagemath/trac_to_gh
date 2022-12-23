# Issue 7598: NumberField embedding slightly off

Issue created by migration from https://trac.sagemath.org/ticket/7598

Original creator: mhansen

Original creation time: 2009-12-04 05:35:08

Assignee: davidloeffler

CC:  burcin


```
sage: Q.<i> = NumberField(x^2+1)
sage: complex(i)
0.99999999999999967j
```


It should give `1j` instead.


---

Comment by mhansen created at 2009-12-14 06:02:23

This is probably caused by the roots method using NumPy which uses Fortran which is a little off.  If you specify algorithm='pari' to the roots command when computing them, things should be fine.


```
sage: Q.<i> = NumberField(x^2+1)
sage: Q.defining_polynomial().change_ring(CC).roots()[1][0].imag().exact_rational()
9007199254740989/9007199254740992
sage: Q.defining_polynomial().change_ring(ComplexField(100)).roots()[1][0].imag().exact_rational()
1
```


Note that NumPy is not used for the second example.


---

Attachment

trac_7598-more_serious_version.patch  -- this deals with the problems more at the root.  Unfortunately, there are doctests in this file that fail:

```
	sage -t  devel/sage-main/sage/modular/dirichlet.py # 4 doctests failed
```

and I haven't had time to figure out what is wrong.  It probably has to do with a complex embedding not being defined automatically, whereas before it was...

The design of embeddings was really bad before and relied on numerical errors to mess up the order of roots in case of 53 bit precision.  This was potentially *very* buggy and was I think the result of some absolutely terrible design decisions.    This absolutely must be fixed before releasing sage-4.3.  This patch basically fixes it, modulo some small remaining issue.

Here is an example from sage-4.2.1 that illustrates just how horrendously bad the previous design was (with using CDF when prec=53 but ComplexField(prec) otherwise):

```
sage: K.<i> = QuadraticField(-1)
sage: i.complex_em
i.complex_embedding   i.complex_embeddings  
sage: i.complex_embedding()
1.0*I
sage: i.complex_embedding(100)
-1.0000000000000000000000000000*I
```



---

Comment by mhansen created at 2009-12-14 13:01:28

I think the errors in dirichlet.py comes from the following:


```
sage: a = mod(1,3)
sage: CDF.zeta(3)^a
-0.5 + 0.866025403784*I
sage: CC.zeta(3)^a
---------------------------------------------------------------------------
Traceback (most recent call last)
...
TypeError: unable to coerce <type 'sage.rings.complex_number.ComplexNumber'> to an integer
```


It'd be nice if the {{{__pow__}} methods were standardized.


---

Attachment


---

Comment by mhansen created at 2009-12-15 03:18:41

I've added a patch which fixes the errors in dirichlet.py by just forcing the exponent to be an int.

William's changes look good to me so the only thing that needs review is trac_7598-dirichlet.patch.

We should open another ticket for the `__pow__` discrepencies.


---

Comment by mhansen created at 2009-12-15 03:18:41

Changing status from new to needs_review.


---

Comment by cremona created at 2009-12-15 09:29:19

Do we need to apply both patches?  Or is it that Mike has given a positive review to the first and only needs a review of the second?  I was hoping to test this (being someone who experienced the problems) but as it will take a long time to rebuild, I want to make sure that the time is not wasted.


---

Comment by mhansen created at 2009-12-15 09:32:53

You need to apply both patches.  I've given a positive review to the first.  The second is pretty easy since it makes the exponent an integer instead of an integermod.


---

Comment by AlexGhitza created at 2009-12-15 11:22:18

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2009-12-15 11:22:18

Running long doctests on a 32-bit Arch Linux machine gives one doctest failure related to this ticket:


```
sage -t -long "devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst"
**********************************************************************
File "/opt/sage-4.3.rc0/devel/sage/doc/en/bordeaux_2008/nf_galois_groups.rst", line 109:
    sage: K.complex_embeddings()
Expected:
    [
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Double Field
      Defn: a |--> -0.629960524947 - 1.09112363597*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Double Field
      Defn: a |--> -0.629960524947 + 1.09112363597*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Double Field
      Defn: a |--> 1.25992104989
    ]
Got:
    [
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Field with 53 bits of precision
      Defn: a |--> -0.629960524947437 - 1.09112363597172*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Field with 53 bits of precision
      Defn: a |--> -0.629960524947437 + 1.09112363597172*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 - 2
      To:   Complex Field with 53 bits of precision
      Defn: a |--> 1.25992104989487
    ]
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_nf_galois_groups.py
	 [5.9 s]
exit code: 1024
}}} 

Apart from this small issue, everything looks good.


---

Comment by AlexGhitza created at 2009-12-15 11:42:27

OK, I've added a trivial patch that fixes the last doctest failure.


---

Attachment

apply after the previous two patches


---

Comment by AlexGhitza created at 2009-12-15 11:43:15

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2009-12-15 14:37:40

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2009-12-15 14:37:40

Applied all 3 patches to 4.3.rc0 on both 32-bit Suse (built using system gfortran) and 64-bit ubuntu (using Sage's gfortran).  No problems.  All tests in the files touched pass.  I still get a failure in doc/en/bordeaux_2008/nf_introduction.rst but that has a different cause.

So, positive review.


---

Comment by mhansen created at 2009-12-15 14:57:38

Excellent.  I'm glad we (you guys) tracked that down.  I'm not sure why I didn't think that the number field was just using the alternate embedding.


---

Comment by mhansen created at 2009-12-15 15:16:37

Resolution: fixed
