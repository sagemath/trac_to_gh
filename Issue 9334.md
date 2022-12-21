# Issue 9334: hilbert symbols!!!

Issue created by migration from Trac.

Original creator: aly.deines

Original creation time: 2010-06-25 03:51:53

Assignee: davidloeffler

CC:  mstreng jdemeyer

Keywords: hilbert symbol

hilbert symbol over number fields


---

Comment by aly.deines created at 2010-06-25 06:50:05

Here all the functions are better placed.  I still need to fix the code so that generalized_hilbert_symbol(a,b,P) doesn't assume a.valuation(P) and b.valuation(P) are 0 or 1.


---

Comment by aly.deines created at 2010-06-25 06:50:05

Changing status from new to needs_work.


---

Comment by aly.deines created at 2010-06-25 07:05:39

I changed the code as Tim (correctly) suggested so as it doesn't assume reduced input.


---

Comment by aly.deines created at 2010-06-25 07:05:39

Changing status from needs_work to needs_review.


---

Comment by aly.deines created at 2010-06-27 21:08:55

This has better uniformizer code.


---

Comment by davidloeffler created at 2010-06-28 18:01:50

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-06-28 18:01:50

This doesn't seem to apply to 4.4.4. Does it require some other patch as a prerequisite? Also, the docstrings don't seem to be correctly ReST formatted (you should always run `sage -docbuild reference html` and check that there are no warnings before submitting a patch).


---

Comment by davidloeffler created at 2010-06-29 11:13:47

I see. So it's supposed to be applied on top of the patches at #9317. That's fine, but you should explain this in your trac upload messages. Don't repost random patches from other tickets on this ticket -- that's just unnecessary duplication, and it's confusing for the release maintainer when s/he has to merge stuff later.

Anyway: with the #9317 patches in place these four patches apply fine, and all doctests pass. But they're quite hard to review, since you seem to have added code in one place in the first patch and then removed it and added it again somewhere else in the second. Could I suggest that you use the Mercurial "qfold" command to combine the four patches into one single patch? That would make the reviewer's job vastly easier. And don't forget those docstring formatting problems; the two that stand out most at a quick glance are that the LaTeX formulae should be in backticks not dollar signs (``x^2 + 2`` etc), and the LaTeX fraction command is `\frac` not `\frak`.


---

Comment by aly.deines created at 2010-06-29 22:11:57

Here is one single patch.  It does not depend on ticket #9317. This should have all the documentation fixed.  Thank you for your patience, I've learned a lot about Mercurial and ReST formatting recently.  

I also applied this on a clean clone of 4.4.2 to check that it would build, all the doctest pass, and the -docbuild looks correct.


---

Comment by davidloeffler created at 2010-06-30 09:59:50

Most of this looks fine, and the docstring formatting is much better; but there are some technical issues.

- The code in ` solver_mod_p ` is obviously wrong for n > 1: it calculates the inverse modulo P<sup>n</sup> but then takes the square root of this modulo P. You need some kind of Hensel lifting or suchlike to get an answer that's right modulo P<sup>n</sup>.

- The code in ` uniformizer ` is a mess (e.g. it trivially fails for any non-principal ideal in a number field of degree > 2, because you've assumed ` self.integral_basis()` has length 2). But there's already a method ` sage.rings.number_field.number_field.NumberField_generic.uniformizer ` (taking a prime as an argument). I agree that it is worth having uniformizers accessible via a method of ideals as well, but it should just be a thin wrapper around the existing code.


---

Comment by cremona created at 2010-07-06 20:06:25

I generally agree with David's points. This code will be very useful for a topic begin done at SD23 (solving conics over various fields) so I am keen to get this in (suitably modified).

In generalized_legendre_symbol: (1) test P for primality first, before trying to construct its residue field. (2) instead of K(2).valuation(P) just test that n is odd. (3) don't raise run-time errors, make them ValueErrors?. (4) make the return types consistent: you return either +1 in k or -1 as a python int. I would return a Sage integer in either case. (5) you do not test if P divides self. If so, return 0 (as a Sage integer)>

Why are generalized_hilbert_symbol and _legendre_symbol in sage/rings/arith.py? I would put them both in number_fields -- where you put the even one in fact.

In generalized_even_hilbert_symbol you define but do not use iprime, so delete it. And do the simple calculation to get the coefficients of jprime**2 so you don't need to construct the quaternion algebra. (You can leave in a comment about that).

_voight_alg_6_2 has some ^ symbols which should be **. Check for others.

Do what David said about uniformizer -- just call the existing function.

Sort out the solve function.


---

Comment by mstreng created at 2010-07-12 12:07:51

Great, I could use this.

While you are still at it, I have a small wish list as well. Could you

 * Let the generalized even Hilbert symbol accept fractions (as the odd one and the QQ one do)?
   {{{
sage: hilbert_symbol(1/3, 1, 2)
1
sage: K.<i> = QuadraticField(-1)
sage: O = K.maximal_order()
sage: generalized_hilbert_symbol(K(1/2), K(1), 3*O)
1
sage: generalized_hilbert_symbol(K(1/3), K(1), (1+i)*O)
NotImplementedError: inverse_mod is not implemented for non-integral elements
   }}}

 * Also add the Hilbert symbol for infinite places? See e.g.
   {{{
sage: hilbert_symbol(-1, -1, -1)
-1
   }}}
   This is almost trivial compared to what you've already done. I have code, contact me if you have questions.

 * Correct the doc text. The doc of generalized_even_hilbert_symbol should say that P must divide 2, while generalized_hilbert_symbol should not say that P must be odd


---

Comment by mstreng created at 2010-07-12 12:16:11

In addition to the first part of my precious comment: generalized_even_hilbert_symbol should accept a and b to both be divisible by p.

```
sage: hilbert_symbol(2,2,2)
1
sage: K.<i>=QuadraticField(-1)
sage: O=K.maximal_order()
sage: generalized_hilbert_symbol(3,3,3*O)
1
sage: generalized_hilbert_symbol(2,2,2*O)
ValueError: P must be a prime
```



---

Comment by mstreng created at 2010-07-12 12:17:52

Oops, the last two lines of my previous comment should of course read

```
sage: p = 1+i
sage: generalized_hilbert_symbol(p,p,p*O)
RuntimeError: ord_P(a) or ord_P(b) must be zero
```



---

Comment by mstreng created at 2010-07-12 14:08:48

Changing priority from minor to major.


---

Comment by cremona created at 2010-08-11 20:48:07

Alyson, are you intending to fix the various points raised by reviewers here?  If not, someone else should.  Ticket #9320 is waiting on this one.


---

Comment by aly.deines created at 2010-08-11 22:18:41

Here are the changes I've made so far: 
1. in generalized_legendred_symbol I test for primality first
2. instead of K(2).valuation(P) I just test that n is odd
3. I've changed RunTime Errors to ValueErrors
4. I return +/- 1 as sage integers
5. I test if P|self and if so return 0 (as a sage integer)
6. in generalized_hilbert_symbol I deleted iprime
7. I did the calculation and have hard coded jprime^2
8. I've replace ^ with ** where necessary in _voight_alg_6_2
9. Things should work for fractions
10. generalized_hilbert_symbol should also accept a,b, divisible by p

One question I have, does anyone know about hensel lifting in sage?


---

Comment by cremona created at 2010-08-12 09:13:53

Excellent -- should it be "needs review" again then?

There must be places in Sage where Hensel lifting is done, but I do not know of any general framework for it.  You could try asking David Roe, who (I think) wrote a lot of the p-adic code.


---

Comment by aly.deines created at 2010-08-12 17:56:39

No, it shouldn't be "needs review" yet.  I still need to fix solver_mod_p.


---

Comment by aly.deines created at 2010-08-19 18:20:54

I have fixed solver_mod so that it computes the square root mod P^n.


---

Comment by aly.deines created at 2010-08-19 18:20:54

Changing status from needs_work to needs_review.


---

Comment by aly.deines created at 2010-08-19 21:04:47

Fixes/added documentation.  Has the examples above in the documentation.


---

Comment by rlm created at 2010-08-20 00:36:06

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-08-20 00:36:06

Based on 4.5.3.alpha1:


```
sage -t  sage/rings/number_field/number_field_ideal.py
**********************************************************************
File "/home/rlmill/sage-4.5.3.alpha1/devel/sage-main/sage/rings/number_field/number_field_ideal.py", line 1212:
    sage: P.uniformizer()
Expected:
    a + 4
Got:
    -2*a + 1
**********************************************************************
File "/home/rlmill/sage-4.5.3.alpha1/devel/sage-main/sage/rings/number_field/number_field_ideal.py", line 1219:
    sage: P.uniformizer()
Expected:
    -7*a^4 + 13*a^3 - 13*a^2 - 2*a + 50
Got:
    a^4 - a^3 + a^2 - a + 1
**********************************************************************
```



---

Comment by aly.deines created at 2010-08-20 01:19:28

Fixes some documentation.


---

Comment by aly.deines created at 2010-08-20 01:20:53

Changing status from needs_work to needs_review.


---

Attachment

Ok, I checked at P.uniformizer() is just wrapping K.uniformizer(P).  So assuming K.uniformizer(P) is correct (which it appears to be), I've fixed the documentation for P.uniformizer().


---

Comment by mstreng created at 2010-08-20 12:30:08

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2010-08-20 12:30:08

Here are some comments have already been mentioned above:
 * why aren't generalized_hilbert_symbol and generalized_even_hilbert_symbol in the same file? (e.g. both in number_field as John suggested)
 * the documentation of generalized_hilbert_symbol says that the prime should be odd, which isn't necessary, in fact, it would be good to have an even example in the doctest so this functionality doesn't get broken
 * the documentation of generalized_even_hilbert_symbol doesn't say that the prime must be even, which it should!

Also, generalized_even_hilbert_symbol is less powerful than the general one:

```
sage: K.<i> = QuadraticField(-1)                            
sage: O = K.maximal_order()
sage: generalized_hilbert_symbol(K(1/3), K(1), (1+i)*O)     
1
sage: generalized_even_hilbert_symbol(K(1/3), K(1), (1+i)*O)
...
NotImplementedError: inverse_mod is not implemented for non-integral elements
```

So I guess the documentation of generalized_even_hilbert_symbol should say that the input should consist of integral elements? Possibly the documentation of generalized_even_hilbert_symbol could say that this is simply an auxiliary function and the user should call generalized_hilbert_symbol instead?

needs_work because of the documentation issues for generalized_even_hilbert_symbol


---

Comment by mstreng created at 2010-08-20 13:00:10

here's a non-documentation reason for `needs_work`:

```
sage: K.<i> = QuadraticField(-1)                           
sage: O = K.maximal_order()
sage: generalized_hilbert_symbol(K(-1/3), K(-2/3), (1+i)*O)
...
ValueError: self is not a square root mod P^n
```



---

Comment by mstreng created at 2010-08-20 13:26:13

And here's another one. In Magma, I get:

```
> L := QuadraticField(5);
> O := MaximalOrder(L);    
> HilbertSymbol(L!-3, L!-2, 2*O);
1 1/2 + 1/2*i j
```

In pari, I get:

```
? k = nfinit(x^2-5)
...
? nfhilbert(k, -3, -2, idealprimedec(k, 2)[1])
%2 = 1
```

But the patch gives:

```
sage: L.<a> = QuadraticField(5)
sage: generalized_hilbert_symbol(L(-3), L(-2), 2*O)
-1
```

Something is wrong...


---

Comment by cremona created at 2010-08-20 14:54:32

In fact, what are the reasons for implementing this independently rather than using pari's function?


---

Comment by mstreng created at 2010-12-08 09:48:00

interface to pari's nfhilbert, apply only this file


---

Attachment

All that needed to be done was wrap pari's nfhilbert function and copy Aly's doctests, but...

One of those doctests revealed yet another bug introduced by the pari upgrade. See [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1147](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1147)

Apply trac_9334_nfhilbert.patch once pari bug 1147 is fixed and that fix reaches Sage.

Possible future improvements:

* implement also for relative number fields by simply delegating to the absolute case

* implement also for QQ by wrapping the global function hilbert_symbol as a member of QQ


---

Comment by mstreng created at 2011-04-05 14:48:56

The pari bug resulting in incorrect outputs of nfhilbert was fixed in Pari svn revision 13063 2011-04-05 14:03:38 +0100 (Tue, 05 Apr 2011).

How do we get this fix into Sage?


---

Comment by jdemeyer created at 2011-04-05 14:55:39

Replying to [comment:29 mstreng]:
> The pari bug resulting in incorrect outputs of nfhilbert was fixed in Pari svn revision 13063 2011-04-05 14:03:38 +0100 (Tue, 05 Apr 2011).
> 
> How do we get this fix into Sage?

I am currently maintaining the PARI spkg for Sage, so asking me is the best way.


---

Comment by jdemeyer created at 2011-04-05 15:01:40

See #11130.


---

Comment by mstreng created at 2011-09-27 10:06:40

apply trac_9334_nfhilbert.patch


---

Comment by cremona created at 2011-09-27 10:46:31

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2011-09-27 10:46:31

Patch applies fine to 4.7.2.alpha2 + #11130;  testing now.  Meanwhile, just a small point -- in the docstring it says that P must be a prime ideal of self, but it can also be (1) an element of self which generates a prime ideal, or (2) a real or complex place of self.  This is well illustrated in the examples, but it should also be stated in the INPUT block.

Any chance you could change the docstring while I am doing the testing?


---

Comment by mstreng created at 2011-09-27 10:48:06

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2011-09-27 10:48:06

Some doctests disagree with Magma, so I hope they will fail!


---

Comment by mstreng created at 2011-09-27 10:56:38

According to Magma V2.17-9, the following changes make the doctests correct:

replace

```
sage: K.hilbert_symbol(p,p,p*O)  
-1
```

by

```
sage: K.hilbert_symbol(p,p,p)  
1
sage: K.hilbert_symbol(p,3*p,p)
-1
sage: K.hilbert_symbol(3,p,p)
-1
```


remove duplicate

```
sage: K.hilbert_symbol(a,b,P)
-1
```

and for the remaining one, replace -1 by 1

replace -1 by 1 in

```
sage: K.hilbert_symbol(a, 2, P)  
-1  
```


Then the "various other examples" contain a lot of uninteresting 1s, of which we can remove a few.


---

Comment by cremona created at 2011-09-27 11:55:55

Testing on 4.7.2.alpha2+#11130 I get these failures:

```
sage -t -long "devel/sage-main/sage/rings/number_field/number_field.py"
**********************************************************************
File "/home/jec/sage-4.7.2.alpha2.11130/devel/sage-main/sage/rings/number_field/number_field.py", line 6737:
    sage: K.hilbert_symbol(p,p,p*O)
Expected:
    -1
Got:
    1
**********************************************************************
File "/home/jec/sage-4.7.2.alpha2.11130/devel/sage-main/sage/rings/number_field/number_field.py", line 6763:
    sage: K.hilbert_symbol(a,b,P)
Expected:
    -1
Got:
    1
**********************************************************************
File "/home/jec/sage-4.7.2.alpha2.11130/devel/sage-main/sage/rings/number_field/number_field.py", line 6770:
    sage: K.hilbert_symbol(a, b, P)
Expected:
    -1
Got:
    1
**********************************************************************
File "/home/jec/sage-4.7.2.alpha2.11130/devel/sage-main/sage/rings/number_field/number_field.py", line 6772:
    sage: K.hilbert_symbol(a, 2, P)
Expected:
    -1
Got:
    1
**********************************************************************
```



---

Comment by jdemeyer created at 2011-09-27 12:23:11

This looks bad:

```
sage: K.<t> = NumberField(x^3 - x + 1)
sage: K.pari_nf().nfhilbert(t,t+1)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/usr/local/src/sage-4.7.2.alpha2/<ipython console> in <module>()

/usr/local/src/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen.gen.nfhilbert (sage/libs/pari/gen.c:29966)()

RuntimeError: Segmentation fault
```


I can't immediately figure out the cause, it is probably a bug somewhere in PARI or the Sage-PARI interface,


---

Comment by jdemeyer created at 2011-09-27 12:43:42

The Segmentation Fault is probably #11854.


---

Comment by mstreng created at 2011-09-27 15:09:21

Replying to [comment:38 jdemeyer]:
> This looks bad:

This is about global Hilbert symbols, while all the doctests are about local ones. Thanks for noticing.

Do you want to close this ticket at the same time as #11130? If not, then I'll wait until I can download a version with #11130 included, and then try to fix the problems here.


---

Comment by jdemeyer created at 2011-09-27 16:32:12

Replying to [comment:40 mstreng]:
> Do you want to close this ticket at the same time as #11130?
I don't think there is any reason to do so.  I will leave it up to you to decide what to do.  For now, I will continue investigating the Segmentation Fault issue.


---

Comment by jdemeyer created at 2011-09-28 07:20:19

Unfortunately, #11854 does _not_ fix the Segmentation Fault.


---

Comment by jdemeyer created at 2011-09-28 08:05:24

The Segmentation Fault actually shows a major design problem with the Sage->PARI interface (essentially, the `t0GEN` system is broken by design).

As for this ticket, as far as I'm concerned you may ignore this.  It has essentially nothing to do with this ticket and (hopefully) it can only be reproduced by _directly_ calling PARI (i.e. doing `K.pari_nf().nfhilbert(t,t+1)` instead of `K.hilbert_symbol(t,t+1)`.)


---

Comment by cremona created at 2011-09-28 09:01:37

Replying to [comment:43 jdemeyer]:
> The Segmentation Fault actually shows a major design problem with the Sage->PARI interface (essentially, the `t0GEN` system is broken by design).
> 

So there should be a new ticket made which explains this major design problem, so that it is on our todo-list at least.


---

Comment by jdemeyer created at 2011-09-29 08:53:26

Replying to [comment:44 cremona]:
> So there should be a new ticket made which explains this major design problem, so that it is on our todo-list at least.
See #11868.


---

Comment by davidloeffler created at 2011-09-29 09:53:29

I presume you didn't mean to apply two copies of the same patch! Is this ready for review again now?


---

Comment by jdemeyer created at 2011-09-29 10:03:27

I'm going to make some further changes.


---

Comment by mstreng created at 2011-09-29 10:12:18

Replying to [comment:48 davidloeffler]:
> Is this ready for review again now?

There is still a duplicate example, and a lot of examples that return 1 now that they are corrected. I think we should remove some of these, and add some -1's such as the ones in my comment 2 days ago.

Also, what is the output type now? In my patch, I converted it to Integer. Jeroen removed that conversion, but what does cdef long give us?

Finally, in my patch, I had self(a), but Jeroen turned this into a. How carefully does Pari check whether stuff is in the right field?


---

Comment by mstreng created at 2011-09-29 10:22:09

Replying to [comment:50 mstreng]:
> Finally, in my patch, I had self(a), but Jeroen turned this into a. How carefully does Pari check whether stuff is in the right field?

Wow, even Sage doesn't check this:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<a> = NumberField(x^3+x+1)
sage: L.<b> = NumberField(x^3+2*x+2)
sage: K(b)
a
```

so my `self(a)` was pretty useless and we may want to do this:

```
if not (a in self and b in self):
    raise ValueError, ...
```



---

Attachment


---

Comment by jdemeyer created at 2011-09-29 10:28:33

Replying to [comment:50 mstreng]:
> There is still a duplicate example, and a lot of examples that return 1 now that they are corrected. I think we should remove some of these, and add some -1's such as the ones in my comment 2 days ago.
Please do it!

> Also, what is the output type now? In my patch, I converted it to Integer. Jeroen removed that conversion, but what does cdef long give us?
It will be Python `int`.  I see no reason to return a Sage Integer.

> Finally, in my patch, I had self(a), but Jeroen turned this into a. How carefully does Pari check whether stuff is in the right field?
I only _moved_ ``a = self(a)`` up in the code.


---

Comment by cremona created at 2011-09-29 10:35:46

Replying to [comment:51 mstreng]:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<a> = NumberField(x^3+x+1)
sage: L.<b> = NumberField(x^3+2*x+2)
sage: K(b)
a
```

| Sage Version 4.7.1, Release Date: 2011-08-11                       |
| Type notebook() for the GUI, and license() for information.        |
I think this is a horrible bug. There is no embedding from L to K!  A very generic `__call__` method is used, and is definitely not doing the right thing here.


---

Comment by davidloeffler created at 2011-09-29 10:39:31

Replying to [comment:53 cremona]:
> Replying to [comment:51 mstreng]:
> {{{
> ----------------------------------------------------------------------
> | Sage Version 4.7.1, Release Date: 2011-08-11                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: K.<a> = NumberField(x^3+x+1)
> sage: L.<b> = NumberField(x^3+2*x+2)
> sage: K(b)
> a
> }}}
> 
> I think this is a horrible bug. There is no embedding from L to K!  A very generic `__call__` method is used, and is definitely not doing the right thing here.
> 

I agree -- that's horrible! It's not so generic actually: the offending code is the  method `NumberField_absolute._coerce_from_other_number_field` which just converts to a polynomial and back: 

```
f = self.polynomial_ring()(x.polynomial())
return self._element_class(self, f)
```


This is mathematically meaningless unless either the other field is isomorphic to self, or x is actually in Q. I suggest we raise this on sage-nt, and maybe open a ticket to fix it ASAP.


---

Comment by mstreng created at 2011-09-29 10:46:26

Replying to [comment:52 jdemeyer]:
> It will be Python `int`.  I see no reason to return a Sage Integer.

Python ints are fine with me, I was afraid it would be a pari object. I would have liked some uniformity, but that's missing already.

```
sage: type(legendre_symbol(3,5))
<type 'int'>
sage: type(hilbert_symbol(3,5,7))
<type 'sage.rings.integer.Integer'>
sage: type(jacobi_symbol(3,5))
<type 'sage.rings.integer.Integer'>
```

I want all symbols to behave nicely with division by Sage integers, but that's fine with `int`

```
sage: int(1)/ZZ(2)
1/2
```



---

Comment by mstreng created at 2011-09-29 10:49:14

Replying to [comment:53 cremona]:
> I think this is a horrible bug. There is no embedding from L to K!  A very generic `__call__` method is used, and is definitely not doing the right thing here.

Is there a ticket for this yet?


---

Comment by davidloeffler created at 2011-09-29 10:57:33

Sage-nt thread here: http://groups.google.com/group/sage-nt/browse_thread/thread/9108218411e7f0a6


---

Comment by jdemeyer created at 2011-09-29 12:13:56

Replying to [comment:56 mstreng]:
> Replying to [comment:53 cremona]:
> > I think this is a horrible bug. There is no embedding from L to K!  A very generic `__call__` method is used, and is definitely not doing the right thing here.
> 
> Is there a ticket for this yet? 

Just made one: #11869.


---

Comment by mstreng created at 2011-09-29 21:18:49

Replying to [comment:52 jdemeyer]:
> Replying to [comment:50 mstreng]:
> > There is still a duplicate example, and a lot of examples that return 1 now that they are corrected. I think we should remove some of these, and add some -1's such as the ones in my comment 2 days ago.
> Please do it!

I could, but I wouldn't be able to test it, and it may need to be rebased afterwards: I failed to install #11130.


---

Comment by mstreng created at 2011-09-30 19:24:10

Positive review for the reviewer patch. I noticed that it included extra -1 examples and removed the duplicate example, and I did not find removing examples worth the trouble.

I also managed to build #11130 and found that all tests pass. I'm assuming Jeroen gives a positive review to what he didn't change, and that his reviewer patch was ready for review, so I'm setting the whole ticket to positive review.


---

Comment by mstreng created at 2011-09-30 19:24:10

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-11-03 16:14:43

Milestone sage-4.7.3 deleted


---

Comment by jdemeyer created at 2011-11-07 10:11:32

Resolution: fixed
