# Issue 6671: [with patch, needs review] Speed of Victor Miller basis

Issue created by migration from https://trac.sagemath.org/ticket/6671

Original creator: mraum

Original creation time: 2009-08-03 21:01:37

Assignee: mraum

CC:  craigcitro

This cythonfies Eisenstein series and uses FLINT instead of NTL to speed up Victor Miller basis by factor 2 and Eisenstein series even more.

Old

```
sage: %timeit eisenstein_series_qexp(18, 1000)
10 loops, best of 3: 19.3 ms per loop
sage: %timeit victor_miller_basis(18, 1000)
10 loops, best of 3: 51 ms per loop
sage: %timeit victor_miller_basis(18, 10000)
10 loops, best of 3: 711 ms per loop
sage: %timeit victor_miller_basis(18, 100000)
10 loops, best of 3: 9.86 s per loop
```


New

```
sage: %timeit eisenstein_series_qexp(18, 1000)
100 loops, best of 3: 4.17 ms per loop
sage: %timeit victor_miller_basis(18, 1000)
10 loops, best of 3: 22.9 ms per loop
sage: %timeit victor_miller_basis(18, 10000)
10 loops, best of 3: 263 ms per loop
sage: %timeit victor_miller_basis(18, 100000)
10 loops, best of 3: 4.29 s per loop
```


This also has some effect on echelon basis of modular forms.

Old

```
sage: %time h = ModularForms(1, 18).echelon_basis()[0].qexp(10000)
CPU times: user 5.00 s, sys: 0.12 s, total: 5.12 s
Wall time: 5.13 s
```


New

```
sage: %time h = ModularForms(1, 18).echelon_basis()[0].qexp(10000)
CPU times: user 4.70 s, sys: 0.09 s, total: 4.79 s
Wall time: 4.80 s
```



---

Comment by mvngu created at 2009-08-04 06:18:21

Martin: The patch should contain your username so it can be identified as your contribution. Your username should follow the convention:

```
Full Name <your-email@somewhere.com>
```

You can set your username in your Mercurial configuration file `~/.hgrc`. Furthermore, the patch must have a meaningful commit message. Again, one convention to follow is:

```
trac #xxxx: <insert-meaningful-commit-message-here>
```

where `#xxxx` is the ticket number.


---

Attachment


---

Comment by mraum created at 2009-11-16 17:19:57

This provides an implementation which is twice as fast but now depends on #7474.


---

Attachment

This is good code, but a little more work is needed:

- It is *unacceptable* that the function delta_qexp now has no docstring at all -- this must be changed.

- The docstring of delta_poly refers to options from delta_qexp that are not actually accepted by delta_poly, and also the return type it describes is clearly wrong.

- The following comment doesn't seem to match the actual code:

```
# then use NTL to compute the remaining fourth power
f = Fmpz_poly(v)
```


See also #6020, where the NTL/FLINT speed issue was discussed extensively (although without any clear conclusion, since NTL seems to win on some platforms and FLINT on others)

David


---

Comment by davidloeffler created at 2010-04-04 15:29:48

Changing status from needs_review to needs_work.


---

Comment by mraum created at 2010-04-05 23:06:23

I added the docstrings and modified them, such that there is a reference to the credits for William and Craig. Besides I modified the code slightly, such that it uses the new code in flint.fmpz_poly (same functionality there; This was a patch also provided by me).

Please, consider this : Due to formating issues, that I don't understand, I had to reformat many doctests for victor_miller_basis(...).

Martin


---

Comment by mraum created at 2010-04-05 23:06:23

Changing status from needs_work to needs_review.


---

Attachment

Sorry, this still isn't up to scratch.

- The "formatting issues that you don't understand" are because the old code always returns a Sequence object which prints each entry on a new line, while your new code inconsistently sometimes returns a Sequence and sometimes a list. It would have been wise to try and understand what was happening here, rather than just casually changing all the doctests to match whatever results your code happened to produce.


- Docstrings. Docstrings! They are important! Many of your docstrings bear only very scanty resemblance to the actual code, e.g. the docstring for eisenstein_series_poly claims it returns a list whereas in fact it's returning a Fmpz_poly object. Furthermore, the normalisation it uses is not either of the standard ones (i.e. neither the constant nor linear coeffs are 1) so you should document what it is actually doing, and add a doctest to prove it. On a similar note, in the "authors" section for the top-level Victor Miller basis function you've put "Martin Raum (2009-08-02) : Use FLINT, eisenstein_series_list and delta_list" -- this presumably refers to some previous versions of the functions you've since deleted. 

- (Relatively minor quibble): The docstring of `eisenstein_series_poly` doesn't appear in the reference manual, while that of `eisenstein_series_qexp` does, so I think the explanatory note about the algorithm should go in the latter, although the logic it documents is in the former. On a related note, the function `delta_poly` is for internal use only, so it would probably be better to rename it as `_delta_poly` to keep it from appearing in the reference manual.


- Before: 

```
sage: time f = eisenstein_series_qexp(300, prec=300)
CPU times: user 0.08 s, sys: 0.00 s, total: 0.08 s
Wall time: 0.08 s
sage: f[17]
80209810833685322547441216640793046418531912652780577247188195636352386970411639577599796091104012101130717894701055491951622698591353123624261645540716464351344232869435068758174405683700539108020074191942626567981338004282490220912228333614228282202627549912059318605175057042490646040306263891324441973189409859729207141378843824365061425627861617456672310716754354
```

After:

```
sage: f = eisenstein_series_qexp(300, prec=300)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/david/sage-4.3.5/devel/sage-vmiller/sage/modular/modform/<ipython console> in <module>()

/home/david/sage-4.3.5/local/lib/python2.6/site-packages/sage/modular/modform/eis_series.pyc in eisenstein_series_qexp(k, prec, K, var)
     76     R = PowerSeriesRing(K, var)
     77     if K is QQ :
---> 78         return a0fac*R(eisenstein_series_poly(k, prec).list(), prec=prec, check=False)
     79     else:
     80         # this is a temporary fix due to a change in the

/home/david/sage-4.3.5/local/lib/python2.6/site-packages/sage/modular/modform/eis_series_cython.so in sage.modular.modform.eis_series_cython.eisenstein_series_poly (sage/modular/modform/eis_series_cython.c:3931)()
     12
     13
---> 14 cpdef eisenstein_series_poly(int k, int prec = 10) :
     15     r"""
     16     Return the q-expansion up to precision 'prec' of the

/home/david/sage-4.3.5/local/lib/python2.6/site-packages/sage/modular/modform/eis_series_cython.so in sage.modular.modform.eis_series_cython.eisenstein_series_poly (sage/modular/modform/eis_series_cython.c:3490)()
     62     expt = <unsigned long int>(k - 1)
     63     a0 = - bernoulli(k) / (2*k)
---> 64     a0den = a0.denominator()
     65     #if a0 < 0 : a0den = -a0den
     66

OverflowError: value too large to convert to int
```


Frankly I think we've now got to the point where it'll be quicker for me to fix the above myself rather than go through a fourth iteration. I'll upload a second patch that fixes the above issues, later today or possibly tomorrow.

David


---

Comment by davidloeffler created at 2010-04-07 14:04:08

Changing status from needs_review to needs_work.


---

Comment by mraum created at 2010-04-07 15:43:04

It's me who has to be sorry; Especially for the Sequence/List thing where I didn't pay attention. If you feel it's better that you correct these mistakes, you can. But orginally I am obligated to do this, so don't hesitate to ask.

Martin


---

Comment by craigcitro created at 2010-04-07 17:35:37

Hi guys,

I keep meaning to chime in on this ticket and not getting the chance. I just wanted to mention that as part of the tickets Alex filed for eisenstein series over finite fields, I ended up coming up with a new algorithm (really basically the same as the old one in spirit) to compute it over `GF(p)`, which turned out to be faster for `ZZ`, too. I've got some pretty insanely optimized code for working with `mpz_t`s right now, and I'm hoping to finish up the case over finite fields using zn_poly as soon as I have a few spare cycles. (We randomly discovered a house we loved and bought it, which is taking up huge amounts of time ... plus I'm teaching ...) In fact, I ended up coming up with about four or five different versions, and I've set up some framework to test them all -- I just haven't had a chance to run it on various sizes across machines to see if the winner changes with `k` and `prec`. (At some point I suspected it would, but I don't remember why I thought that.) 

That said, there's one serious issue that I don't have a good idea of how to handle, and I'd love input from both of you: as it stands, FLINT stores polynomials in a "packed" representation, requiring that each coefficient have the *same number* of limbs allocated. So that means that the total storage used by an eisenstein series will be `(number of limbs in largest coefficient) * (total number of coefficients)`, which might get fairly unpleasant if you want, say, several million coefficients for `E_4`. On the other hand, NTL doesn't do this -- it will let each coefficient get allocated separately as you'd like. So I was thinking that the natural solution would just be to have a cutoff that's a function of `k` and `prec`, and return an NTL or FLINT polynomial as appropriate. What do you guys think?


---

Comment by davidloeffler created at 2010-04-07 18:25:18

Hi Craig,

Good to hear from you; I had hoped to see you in Montreal -- it's a pity you couldn't make it. It sounds like you have put loads of work into this, but how long do you think it is likely to be before your code is ready to go in? We have the choice of either doing nothing now and waiting for your code, or merging Martin's code now (with a few small changes) and then replacing it with yours when it is ready, which would mean some tedious work rebasing patches. 

As for your question about space requirements, I don't think it will make that much difference. The nth coefficient of E_k is about n^{k-1} and so requires constant * k * log(n) storage space; same for Delta, with a different constant. Since, as is well known, sum_{i=1}^n log(i) is asymptotic to n log n, FLINT's approach is asymptotically no worse than NTL's for this problem.

David


---

Comment by davidloeffler created at 2010-04-07 19:38:39

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-04-07 19:38:39

I've just uploaded a patch, to be applied on top of Martin's, which sorts out the things I mentioned in my last post. It also has a one-line bodge fix to get `delta_qexp` to work over finite fields (by calling the polynomial ring constructor with check=True, as in `eisenstein_series_qexp`), which should settle #6020.

Martin: can you take a quick look at the new patch, in particular at the changes I've made in `eisenstein_series_poly` to fix the overflow error when the denominator of the Bernoulli number is big?


---

Attachment

Apply over trac-6671-3-victor-miller.patch


---

Comment by craigcitro created at 2010-04-07 20:05:26

Replying to [comment:8 davidloeffler]:
> Good to hear from you; I had hoped to see you in Montreal -- it's a pity you couldn't make it. It sounds like you have put loads of work into this, but how long do you think it is likely to be before your code is ready to go in? We have the choice of either doing nothing now and waiting for your code, or merging Martin's code now (with a few small changes) and then replacing it with yours when it is ready, which would mean some tedious work rebasing patches. 
> 

Well, Alex is going to be waiting on me for this code fairly soon, which means it's going to get done fairly soon. That said, it seems like it can't hurt to merge Martin's code first -- it means I'll essentially do a second review when I merge my code, and if there are any clever tricks Martin spotted that I missed, they won't get lost. 

> As for your question about space requirements, I don't think it will make that much difference. The nth coefficient of E_k is about n^{k-1} and so requires constant * k * log(n) storage space; same for Delta, with a different constant. Since, as is well known, sum_{i=1}^n log(i) is asymptotic to n log n, FLINT's approach is asymptotically no worse than NTL's for this problem.
> 

You're right -- there's no real loss to using FLINT (and it means my code will get yet faster, in fact). I knew it was something that shouldn't matter "in principle," but I hadn't sat down and actually worked out the details to find out that it's fine in practice, too. I suspect that you'll still get into a little bit of trouble if you're trying to allocate a q-expansion that's the same order of magnitude as the amount of memory in your machine, but if that's what you're up to, you need specialized code no matter what. 

In regards to #6020 -- the only real pending issue on that ticket was the fact that 32-bit OSX was lagging; since we only compile in 64-bit on OSX these days, we could probably just merge that fix as-is, if Martin's code doesn't completely subsume it.


---

Comment by davidloeffler created at 2010-04-07 20:17:00

I think if we merge Martin's patch and mine, that means the patch at #6020 is superseded. My patch means it will work over finite fields, fixing the original issue at #6020 (although clearly not in the most efficient possible way); and over ZZ, on all the platforms we now care about, Martin's FLINT-based code beats the patch at #6020 which is still using NTL.


---

Attachment

First apply trac-6671-3-victor-miller.patch, then this one


---

Comment by mraum created at 2010-04-07 21:41:38

That looks very good; I suppose that's what good docstrings are and I will take a leaf out of your book.

I looked up whether the Victor-Miller basis normally referes only to cusp forms, but it doesn't seem so (http://www.sagemath.org/doc/bordeaux_2008/level_one_forms.html). I changed this in one doctest.
It is not neccessary to introduce res2 and this will safe half the memory.

I integrated these two minor changes into your patch.

Regarding #6020: This chould be a follow up patch and I will see if I find the time to merge Craig's code with the new patch tomorrow. My code does not subsume it.


---

Comment by mraum created at 2010-04-07 21:41:38

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 05:55:29

Merged in 4.4.alpha0:

 - trac-6671-3-victor-miller.patch
 - trac-6671-reviewer-2.patch


---

Comment by jhpalmieri created at 2010-04-15 05:55:29

Resolution: fixed
