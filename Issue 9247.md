# Issue 9247: A collection of little improvements to elliptic curves

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-06-15 20:32:55

Assignee: cremona

CC:  wuthrich

These are some of the things I did while working on my thesis.


---

Comment by rlm created at 2010-06-15 20:33:58

Changing status from new to needs_review.


---

Comment by cremona created at 2010-06-15 21:24:48

Looks like a job for me -- but probably not until I have finished preparing for SD22!


---

Comment by rlm created at 2010-06-15 21:35:43

I'm wondering if by default, E.saturate() shouldn't print all that stuff from `mwrank`. Oddly, it doesn't show up in doctests, since it goes straight to the terminal.

There are also still failures in:

```
sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py"
sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/padics.py"
```


John, Can you give some opinion on those?


---

Comment by rlm created at 2010-06-15 21:36:01

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-06-17 21:19:57

Looks good and applies to 4.4.4.alpha0.  I am currently testing all sage/schemes/elliptic_curves.

One point about the (good) new rank_bound parameter for the point_search function:  is it not rather inefficient to saturate completely after every point found?  In my code (in eclib's points own search function) I only partially saturate after each point, using a bound (i.e. max_prime) of 19.  Then one the rank bound is reached (or at the end, if rank_bound is None) so a complete saturation.

I also think we should have an option for this function to not do the saturation step (which also discards all points found and replaces them for a Z-basis for their saturation), and just returns a list of the raw points actually found.  If you agree, we should open a new ticket.  (Obviously the current behaviour would be the default, for backward compatibility).

Test failure in sha_tate: 

```
File "/home/john/sage-4.4.4.alpha0/devel/sage-tests/sage/schemes/elliptic_curves/sha_tate.py", line 637:
    sage: e.sha().an_padic(7)
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[14]>", line 1, in <module>
        e.sha().an_padic(Integer(7))###line 637:
    sage: e.sha().an_padic(7)
      File "/home/john/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py", line 464, in an_padic
        ms = self.E.modular_symbol(sign=+1, normalize='L_ratio')
      File "/home/john/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1277, in modular_symbol
        M = ell_modular_symbols.ModularSymbolECLIB(self, sign, normalize=normalize)
      File "/home/john/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_modular_symbols.py", line 474, in __init__
        self._modsym = ECModularSymbol(E)
      File "newforms.pyx", line 75, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1794)
    OverflowError: long int too large to convert to int
```


and similar in padics:

```

File "/home/john/sage-4.4.4.alpha0/devel/sage-tests/sage/schemes/elliptic_curves/padics.py", line 91:
    sage: [ms(1/11), ms(1/3), ms(0), ms(oo)]
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[7]>", line 1, in <module>
        [ms(Integer(1)/Integer(11)), ms(Integer(1)/Integer(3)), ms(Integer(0)), ms(oo)]###line 91:
    sage: [ms(1/11), ms(1/3), ms(0), ms(oo)]
      File "/home/john/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_modular_symbols.py", line 523, in __call__
        return (self._atzero - self._modsym(r))*self._scaling
      File "newforms.pyx", line 130, in sage.libs.cremona.newforms.ECModularSymbol.__call__ (sage/libs/cremona/newforms.cpp:2024)
      File "rational.pyx", line 367, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:5781)
      File "rational.pyx", line 521, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7052)
    TypeError: Unable to coerce +Infinity (<class 'sage.rings.infinity.PlusInfinity'>) to Rational
```

but I have no idea what in the patch could have caused this!
And finally:

```

File "/home/john/sage-4.4.4.alpha0/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 1211:
    sage: M=E.modular_symbol()
Expected nothing
Got:
    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.
**********************************************************************
File "/home/john/sage-4.4.4.alpha0/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 1212:
    sage: M(1/7)
Expected:
    2
Got:
    -2
**********************************************************************
```



---

Comment by rlm created at 2010-06-17 21:57:44

Replying to [comment:5 cremona]:
> ... the (good) new rank_bound parameter ... is it not rather inefficient to saturate completely after every point found?  In my code (in eclib's points own search function) I only partially saturate after each point, using a bound (i.e. max_prime) of 19.  Then one the rank bound is reached (or at the end, if rank_bound is None) so a complete saturation.

Sounds like a better option to me!

> I also think we should have an option for this function to not do the saturation step (which also discards all points found and replaces them for a Z-basis for their saturation), and just returns a list of the raw points actually found.  If you agree, we should open a new ticket.  (Obviously the current behaviour would be the default, for backward compatibility).

I do agree!

> ... but I have no idea what in the patch could have caused this!

E.modular_symbol() now uses eclib if the sign is +1, for efficiency purposes. It is probably what is causing all the failures... I'm not sure whether this is practical or not, but it definitely sped up E.sha().p_primary_bound(p) in the cases I was looking at.


---

Comment by rlm created at 2010-06-24 16:18:13

Replying to [comment:3 rlm]:
> I'm wondering if by default, E.saturate() shouldn't print all that stuff from `mwrank`. Oddly, it doesn't show up in doctests, since it goes straight to the terminal.

More specifically, with the patch here applied to `sage-4.4.4.alpha1` the following doctest illustrates the printing I'm talking about:

```
sage: EllipticCurve([0, 0, 1, -79, 342]).regulator(proof=False)  # long time (seconds)
Saturation index bound = 265
WARNING: saturation at primes p > 100 will not be done;  
points may be unsaturated at primes between 100 and index bound
Failed to saturate MW basis at primes [ ]
*** saturation possibly incomplete at primes [ ]
14.7905275701311
```


When I do this from the command line, that is exactly what I get. However, when I run long doctests in `ell_rational_field.py` the following part appears in the terminal from which I'm running the tests, and is a little misleading:


```
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py", line 1212:
    sage: M(1/7)
Expected:
    2
Got:
    -2
Saturation index bound = 265
WARNING: saturation at primes p > 100 will not be done;  
points may be unsaturated at primes between 100 and index bound
Failed to saturate MW basis at primes [ ]
*** saturation possibly incomplete at primes [ ]
**********************************************************************
```



---

Comment by cremona created at 2010-06-25 05:22:32

OK, so the problem is that the warning output from the regulator call appears in the wrong place in the output -- right?

I have solved this by avoiding it as follows.  The gens() function uses mwrank_lib (default) or mwrank_console to do a two-descent after constructing the mwrank_EllipticCurve C.  But it was failing to call the saturate function on C.  Some default saturation is done by the gens() call (on C), but the default saturation bound is rather low (100, set in eclib).

So I added a new parameter sat_bound to the gens() function in ell_rational_field, default 1000, and made sure that both mwrank_lib and mwrank_console option use it.
Now we have

```

sage: E = EllipticCurve([0, 0, 1, -79, 342])
sage: E.gens()
[(-10 : 11 : 1), (-39/4 : 105/8 : 1), (-8 : 21 : 1), (-7 : 23 : 1), (-6 : 24 : 1)]
```


```
sage: E = EllipticCurve([0, 0, 1, -79, 342])
sage: E.gens(algorithm='mwrank_console')
[(-10 : 11 : 1), (-39/4 : 105/8 : 1), (-8 : 21 : 1), (-7 : 23 : 1), (-6 : 24 : 1)]
```

compared with

```

sage: E = EllipticCurve([0, 0, 1, -79, 342])
sage: E.gens(sat_bound=100)
Saturation index bound = 265
WARNING: saturation at primes p > 100 will not be done;  
points may be unsaturated at primes between 100 and index bound
Failed to saturate MW basis at primes [ ]
*** saturation possibly incomplete at primes [ ]
[(-10 : 11 : 1), (-39/4 : 105/8 : 1), (-8 : 21 : 1), (-7 : 23 : 1), (-6 : 24 : 1)]
```

I will post an additional patch in a minute.


---

Comment by cremona created at 2010-06-25 06:15:03

Apply after previous


---

Attachment

My patch solves the issue with annoying output of warnings from saturation, since we now use a higher bound for saturation primes in finding the gens of an elliptic curve.  (This provides useful functionality as well as fixing this particular case).

The other issues remain, but I think that Robert could review my patch!


---

Comment by rlm created at 2010-07-15 13:51:01

New patch looks good. What to do about the others...


---

Comment by wuthrich created at 2010-07-15 14:04:57

I would suggst to remove the modification to padic_lseries.py. In the future we should use eclib by default, but currently eclib does not provide negative modular symbols and they are needed in some cases (e.g. twisting by a negative D). A careful user can currently choose to use eclib, if he knows  that he will not need negative modular symbols.


---

Comment by cremona created at 2010-07-15 14:57:02

Replying to [comment:11 wuthrich]:
> I would suggst to remove the modification to padic_lseries.py. In the future we should use eclib by default, but currently eclib does not provide negative modular symbols and they are needed in some cases (e.g. twisting by a negative D). 

Yes it does now!   Review my patch and you can have them!  I implemented this while at MSRI.  See #9476

A careful user can currently choose to use eclib, if he knows  that he will not need negative modular symbols.


---

Comment by wuthrich created at 2010-07-15 15:02:06

Replying to [comment:12 cremona]:

> Yes it does now!   Review my patch and you can have them!  I implemented this while at MSRI.  See #9476
>

Ohhh, I did not know. I hope I will have time to look at that tomorrow.


---

Comment by rlm created at 2010-07-17 15:03:42

Apply before saturation patch


---

Comment by rlm created at 2010-07-17 15:04:31

Changing status from needs_work to needs_review.


---

Attachment

Okay, I've changed the default for elliptic curve modular symbols back to what it originally was. Now all tests pass, and this ticket is ready for a review.


---

Comment by rlm created at 2010-07-18 08:10:46

See also #9535


---

Comment by was created at 2010-07-21 14:35:22

Works and seems reasonable in light of the above remarks.


---

Comment by was created at 2010-07-21 14:35:22

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:50:15

Resolution: fixed
