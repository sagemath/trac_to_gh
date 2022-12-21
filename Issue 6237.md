# Issue 6237: repeated roots with roots(CDF, multiplicities=False)

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-06 22:30:12

Assignee: somebody

Keywords: roots CDF multiplicities


```
sage: pari('v')
v
sage: pari('u')
u
sage: u = QQ['u'].0
sage: v = QQ['u']['v'].0
sage: f = v^3 - u^7 + 2*u^3*v
sage: f.discriminant()
-27*u^14 - 32*u^9
sage: f.discriminant().roots(CDF, multiplicities=False)

[-1.03456371594,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 0,
 -0.31969776999 - 0.983928563571*I,
 -0.31969776999 + 0.983928563571*I,
 0.836979627962 - 0.608101294789*I,
 0.836979627962 + 0.608101294789*I]
```


Note the repetition of 0.


---

Comment by AlexGhitza created at 2010-01-02 04:53:32

And if you run it with just `roots(CDF)` you get nine different occurrences of (0, 1), i.e. root 0 with multiplicity 1.

The attached patch fixes this.


---

Comment by AlexGhitza created at 2010-01-02 04:53:32

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-01-04 15:37:10

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2010-01-04 15:37:10

This is fine overall, assuming the answer to the following question is yes.

```
            if output_complex:
                rts = sort_complex_numbers_for_display([L(root) for root in ext_rts])
            else:
                rts = [L(root.real()) for root in ext_rts if root.imag() == 0]
```

The first list gives a canonical ordering, so using 

```
                rts_mult.append((rt, mult))
                j += mult
```

is okay, it won't append the same thing twice.  Is that also true for the second list?  I couldn't come up with an example that breaks it, but that just means I don't know much about how polynomials are represented internally.  At any rate, it should probably be ordered, just to be on the safe side, if you use that way of finding multiplicities.  Does Pari not compute multiplicities for this?  Maxima's implementation does, though perhaps it doesn't do arbitrary precision.  I assume numpy definitely doesn't do multiplicities.


---

Comment by AlexGhitza created at 2010-01-04 23:20:19

Thanks for catching this.

From Pari's documentation for the function we're using:


```
polroots(pol,{flag = 0})

complex roots of the polynomial pol, given as a column vector where each root is repeated according to its multiplicity. [...]

The algorithm used is a modification of A.Sch¨nhage's root-finding algorithm, due to and implemented by X.Gourdon. Barring bugs, it is guaranteed to converge and to give the roots to the required accuracy.
```


There is no mention of the roots being sorted.  I guess I could read the source code and find out, but I like you suggestion of sorting the Pari output anyway -- just in case they change the behaviour in the future.

Also from the above snippet, Pari indeed does not give the multiplicities, it just repeats each root the correct number of times.

I will replace the patch soon.


---

Comment by AlexGhitza created at 2010-01-04 23:20:19

Changing status from needs_info to needs_work.


---

Comment by AlexGhitza created at 2010-01-04 23:56:23

Changing status from needs_work to needs_review.


---

Attachment

OK, the revised patch is up.


---

Comment by kcrisman created at 2010-01-05 04:03:08

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-05 04:03:08

Looks good.  Passes relevant tests.

I did find something else weird, perhaps just my install is somehow corrupt... Did you try the original thing from the description as well?  It seems to be broken at the calculation of the discriminant both before and after the patch.  I get an error message about PariError(8).  However, this does not appear on sage.math, so I assume something weird happened in my local install.  But I thought I'd mention it in case you find it.

Anyway, positive review!


---

Comment by AlexGhitza created at 2010-01-05 06:10:31

Did you try the whole thing, including `pari('v')` and `pari('u')` ?

It seems to work for me.  Of course, if I had written the example I would have tried something like


```
sage: R.<u> = QQ[]
sage: S.<v> = R[]
sage: f = v^3 - u^7 + 2*u^3*v
sage: f.discriminant()
```


This does indeed fail with a `PariError(8)`.  And this is apparently documented in the docstring for `discriminant`.  It's a shame that it doesn't work out of the box.  In fact, I would even like something like the following to work:


```
sage: R.<u, v> = QQ[]
sage: f = v^3 - u^7 + 2*u^3*v
sage: f.discriminant(v)
```


Anyway, it's beyond the scope of this ticket.  I might open an enhancement ticket about it.


---

Comment by kcrisman created at 2010-01-05 13:36:38

Replying to [comment:6 AlexGhitza]:
> Did you try the whole thing, including `pari('v')` and `pari('u')` ?
Yes.  Again, oddly enough, the same thing did work when I tried it on sage.math, so it must be highly sensitive to something, though not sure what - maybe I had typed in something earlier that made it work/not work.
> 
> It seems to work for me.  Of course, if I had written the example I would have tried something like
> 
> {{{
> sage: R.<u> = QQ[]
> sage: S.<v> = R[]
> sage: f = v^3 - u^7 + 2*u^3*v
> sage: f.discriminant()
> }}}
> 
> This does indeed fail with a `PariError(8)`.  And this is apparently documented in the docstring for `discriminant`.  
Huh.  Well, glad to know it.
> Anyway, it's beyond the scope of this ticket.  I might open an enhancement ticket about it.
Go for it, though I won't be able to help on it.


---

Comment by rlm created at 2010-01-13 08:29:51

Resolution: fixed
