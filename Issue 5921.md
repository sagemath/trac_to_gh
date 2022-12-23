# Issue 5921: factoring integer polynomials does not factor the content

Issue created by migration from https://trac.sagemath.org/ticket/5921

Original creator: cremona

Original creation time: 2009-04-28 19:54:00

Assignee: tbd

I think this is wrong:

```
sage: R.<x> = ZZ[]
sage: f = 30*x
sage: f.factor()
30 * x
```

since in the ring ZZ[] 30 is not irreducible;  it should return 2*3*5*x.



---

Attachment


---

Comment by AlexGhitza created at 2009-04-28 22:47:00

Hi John,

The changes in the patch look fine, but for some reason they make doctests fail in two places: `polynomial_zmod_flint.pyx` (with some errors) and `polynomial_modn_dense_ntl.pyx` (killed after timeout).  I'm rushing to teach right now, but I'll try to investigate afterward.


---

Comment by AlexGhitza created at 2009-04-29 00:53:04

OK, I've found a very simple example where this bombs:


```
sage: P.<x> = ZZ[]
sage: f = 2*x + 2
sage: f.roots()
...
NotImplementedError:
```



---

Comment by AlexGhitza created at 2009-04-29 01:44:13

Hmmm.  We just had this situation happen on a different ticket: the code in this patch is fine but breaks something, which really exposes a pre-existing bug.

In this case, John's code factors the content and the "normalised, content-free" polynomial separately and multiplies the two factorisations.  The problem is the with the types: the first factorisation consists of integers, while the second one consists of polynomials.  Multiplying them together yields a factorisation where some factors are of type integer and the others of type polynomial, and then this breaks all sorts of things later on.

I've made a new ticket at #5928 and will have a patch up there soon.  Then John's patch on this ticket will be good to go.


---

Comment by AlexGhitza created at 2009-04-29 05:53:44

There's now a patch up at #5928.  I've tested again with John's patch applied and the `polynomial_zmod_flint.pyx` problems are gone, but I'm still getting timeouts in `polynomial_modn_dense_ntl.pyx`.  So there's more to this than I thought.


---

Comment by AlexGhitza created at 2009-04-29 06:42:44

Yes, the problem is in `f.roots()` for a polynomial f with integer coefficients.  The code used to just run `f.factor()`, but of course now if the content is a huge integer it's gonna take a while for the factoring to finish.  There's a doctest in the sage library that runs into precisely this problem now, since it's an illustration of RSA and has huge coefficients (and a huge content) floating around.  However, you don't care about the content if you just want the roots of the polynomial.

So the attached patch makes `roots()` divide by the content first, then call `factor()`.  It also adds a warning to this effect in the docstrings of the two `factor()` methods.

I'm happy with John's patch, so if someone reviews my patch we're done.


---

Comment by AlexGhitza created at 2009-04-29 06:44:28

I forgot to mention this again: this ticket depends on the patch at #5928, so that should be applied first.


---

Comment by cremona created at 2009-04-29 08:30:13

I am happy with Alex's patch.  I made mine a bit too quickly or I would have thought about the universes being different.  So I will give this a positive review as soon as I have gone to look at #5928.


---

Comment by cremona created at 2009-04-29 09:05:36

I applied both patches after #5928 on top of 3.4.2.alpha0, fine.  Ran all tests in sage/rings/polynomial (all fine) and sage/rings/number_field (all fine).

So I have given this a positive review since Alex and I have reviewed eachothers' patches.


---

Comment by mabshoff created at 2009-04-30 02:56:23

These two patches break

```
sage -t -long devel/sage/sage/modular/overconvergent/genus0.py
```


Cheers,

Michael


---

Comment by AlexGhitza created at 2009-04-30 03:35:18

Replying to [comment:10 mabshoff]:
> These two patches break
> {{{
> sage -t -long devel/sage/sage/modular/overconvergent/genus0.py
> }}}
> 

This is due to a bug in p-adics, more precisely in the content method for p-adic polynomials:


```
sage: P.<x> = ZZ[]
sage: f = x + 2
sage: f.content()
1
sage: fp = f.change_ring(pAdicField(2, 10))
sage: fp
(1 + O(2^10))*x + (2 + O(2^11))
sage: fp.content()
0
```


I have checked and the monster p-adic patch bomb at #5778 doesn't help with this.  I'll see what we can do.


---

Comment by AlexGhitza created at 2009-04-30 06:45:51

OK, I've made a simple modification in my patch that sidesteps the p-adic polynomial bug (for which there is now a new trac ticket #5946).

I have replaced my patch with the new version, so one still needs to apply both patches.


---

Attachment

With Alex's new patch (on top of mine all tests in modular/overconvergent/* pass  as well as all in rings/polynomial

I reinstated Positive Review and am keeping my fingers crossed!


---

Comment by mabshoff created at 2009-04-30 09:20:52

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 09:20:52

Merged both patches in Sage 3.4.2.rc0.

Cheers,

Michael
