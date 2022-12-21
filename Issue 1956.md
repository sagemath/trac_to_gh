# Issue 1956: implement multivariate power series arithmetic

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-28 02:26:47

Assignee: malb

CC:  mhansen simonking malb hlaw

Multivariate power series arithmetic has been requested a *lot*.


---

Comment by was created at 2008-01-28 02:27:03

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-07-08 01:17:47

Hi Mike,

hasn't something happened in that direction already or am I confused?

Cheers,

Michael


---

Comment by niles created at 2010-07-09 21:00:58

I just attached a first version of multivariate power series.  In order to pass all tests, one also needs the patches at #9457 and #9443.  Without these, everything still works though.

The implementation is based on an idea mentioned in this sage-devel [thread](http://groups.google.com/group/sage-devel/browse_thread/thread/40eb14f877b6218a/c30e824e24eee69d?lnk=gst&q=multivariate+power+series#c30e824e24eee69d):
use univariate power series over multivariate polynomial ring to do arithmetic and track total-degree precision, but display as multivariate power series.

Although there are some limitations of this approach, I think there's a useful amount of functionality here and I'm happy with how this first version works.  Having said that, here are some of the issues that are still unresolved.  I'd be happy to hear recommendations about how to prioritize them, or others :)

  * sparse:  I tried to include sparse=True in the right places, but I haven't really tested to see whether it's actually better.

  * inherited functions: some of them (e.g. 'variable') don't make sense; is there a way to block inheritance of certain attributes?  (del or delattr?) For now, they just return "`NotImplementedError`"s

  * inherited functions 2: for multi_power_series_ring_element, there is a pile of functions that could be implemented but aren't (e.g. sqrt, derivative, generating functions, etc).  They're noted in the documentation and lumped together in the code.

  * (rich) comparison: comparisons seem to work, but someone who understands the past and future of sage/python comparisons should take a look at it.  (The classes I'm inheriting from seem to use an older system.)

  * _l_action_ for multivariate power series:  the function works, but doesn't get called when it should; I don't understand how to fix that. (This only affects cases where the scalar isn't already in the base ring, like when you want to multiply a power series over ZZ by a rational and have the result automatically move to a power series over QQ.)

  * division of multivariate power series:  works fine when the denominator is a unit, but not in other cases (even when the result would not be a Laurent series).

  * un/pickling: I don't understand this so I haven't done anything with it.

  * cython where appropriate:  I don't know C or python, so I've ignored this.

  * unifying multivariate and univariate power series, as has been done for polynomials:  seems like a project for another time.


---

Comment by niles created at 2010-07-09 21:00:58

Changing status from new to needs_review.


---

Comment by niles created at 2010-07-10 20:10:20

Uploaded a revised patch which now includes doctests for all* functions.  And yes, I did find a fix a number of bugs while doing that.  So thanks, whoever decided to require 100% doctest coverage :)

* note:  multi_power_series_ring.py has 100% doctest coverage,
multi_power_series_ring_element.py has 61% doctest coverage, but the functions with missing doctests are *all* inherited functions that (as described above) raise "`NotImplementedError`"s.

further note:  I commented out the function _im_gens_ which was supposed to be based on the same function for multivariate polynomial rings.  I couldn't get it to work even for the polynomial case, so I let it go (after little effort, I admit).


---

Comment by malb created at 2010-07-14 08:25:39

Hi, I took a quick look, here are some examples:

 * You don't need #random for random output, the seed of the pseudo random number generator is reset for each doctest plot
 * It would be nice if you could add line breaks around 80 for the doc strings
 * the arithmetic functions doctests do not test correctness of the output

I know very little about multivariate power series, thus I'm clueless about whether your implementation strategy is (a) standard and/or (b) clever. Is it something that is usually done?


---

Comment by niles created at 2010-07-14 14:51:19

Replying to [comment:5 malb]:

Thanks!


>  * You don't need #random for random output, the seed of the pseudo random number generator is reset for each doctest plot

fixed now.


>  * It would be nice if you could add line breaks around 80 for the doc strings

sorry, not sure what you mean by 80 here; I'm happy to add linebreaks though :)


>  * the arithmetic functions doctests do not test correctness of the output

I've added comparisons with polynomial arithmetic; do you think I need to also have the output printed?


 
> I know very little about multivariate power series, thus I'm clueless about whether your implementation strategy is (a) standard and/or (b) clever. Is it something that is usually done?

I don't know much about this either, but it seems like a natural enough idea.  After a quick look around google, here's one example:

http://algo.inria.fr/seminars/sem00-01/lecerf.html

I'll take a look for more complete references too.


---

Comment by malb created at 2010-07-14 20:42:56

Replying to [comment:6 niles]:

> > * It would be nice if you could add line breaks around 80 for the doc strings
> sorry, not sure what you mean by 80 here; I'm happy to add linebreaks though :)

Sorry, I meant around 80 characters, which is the standard UNIX terminal width.

> > * the arithmetic functions doctests do not test correctness of the output
> I've added comparisons with polynomial arithmetic; do you think I need to also have the output printed?

I'd prefer that to be honest.

> > I know very little about multivariate power series, thus I'm clueless about whether your implementation strategy is (a) standard and/or (b) clever. Is it something that is usually done?
> I don't know much about this either, but it seems like a natural enough idea.  After a quick look around google, here's one example: http://algo.inria.fr/seminars/sem00-01/lecerf.html I'll take a look for more complete references too.

Have you compared the speed with, say, Magma?


---

Comment by niles created at 2010-07-17 10:54:51

Replying to [comment:7 malb]:
> Replying to [comment:6 niles]:
> 
> > > * It would be nice if you could add line breaks around 80 for the doc strings
fixed now


> > > * the arithmetic functions doctests do not test correctness of the output
arithmetic tests now printed, and confirmed with polynomial tests


> Have you compared the speed with, say, Magma?

Here are five simple comparisons, three with 2 variables and two with 4 variables, all over QQ.  This sage patch performs substantially better in 3/4 cases, with magma performing substantially better in the other case.  Using polynomial multiplication easily beats magma's restriction on the number of coefficients it will compute for a lazy power series (test 3).

Processor: `6-core:  model name:  Intel(R) Xeon(R) CPU  X7460  `@` 2.66GHz`

sage: 

```
sage: L.<a,b,c,d> = MPowerSeriesRing(QQ,4)
sage: %timeit s = (1 + 2*a + 3*b + 4*d + L(0).O(16))^-5
5 loops, best of 3: 3.18 s per loop

sage: time (1 + a^3 + b^3 + c^4 + d^4 + L(0).O(15))^-20
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
<SNIP>

sage: f = -1/6*b^6*d^14 - 1/9*a^4*b^10*c^4*d^12 + b^10*c^11*d^21 - a*b^14*c^24*d^4 - 1/66*a^16*b^11*c^17 + L(0).O(50)
sage: time f^20
CPU times: user 0.16 s, sys: 0.00 s, total: 0.16 s
Wall time: 0.16 s
1/3656158440062976*b^120*d^280 
+ 5/1371059415023616*a^4*b^124*c^4*d^278 
+ 95/4113178245070848*a^8*b^128*c^8*d^276 
- 5/152339935002624*b^124*c^11*d^287 
+ 5/152339935002624*a*b^128*c^24*d^270 
+ 5/10054435710173184*a^16*b^125*c^17*d^266 
+ O(a, b, c, d)^430
```


magma:

```
> L<a, b, c, d> := LazyPowerSeriesRing(Rationals(), 4);
> s := (1 + 2*a + 3*b + 4*d)^-5;
> time Coefficients(s, 15);
<SNIP>
Time: 29.020

> s := (1 + a^3 + b^3 + c^4 + d^4)^-20;
> time Coefficients(s, 14);
<SNIP>
Time: 48.850

> s := (-1/6*b^6*d^14 - 1/9*a^4*b^10*c^4*d^12 + b^10*c^11*d^21 - a*b^14*c^24*d^4 - 1/66*a^16*b^11*c^17)^20;
> time Coefficients(s, 14); 
<SNIP> 
Time: 16.340
> time Coefficients(s, 429);                                                                               

>> time Coefficients(s, 429);
                    ^
Runtime error in 'Coefficients': The number of coefficients to be returned must be small
```



sage: 

```
sage: Z.<a,b> = MPowerSeriesRing(QQ,2)
sage: time (1 + 1/2*a + 3*b + 4*a*b + 1/5*a^2 + 5/6*b^2 + Z(0).O(30))^-20
CPU times: user 12.67 s, sys: 0.01 s, total: 12.68 s
Wall time: 12.68 s
<SNIP>

sage: f = 1 + a^14*b^9 + 8/3*a^22*b^11 - 1/13*a^23*b^19 + a^15*b^28 + Z(0).O(51)
sage: time f^-20
CPU times: user 0.05 s, sys: 0.00 s, total: 0.05 s
Wall time: 0.05 s
1 - 20*a^14*b^9 - 160/3*a^22*b^11 + 20/13*a^23*b^19 
- 20*a^15*b^28 + 210*a^28*b^18 + O(a, b)^51
```



magma:

```
> Z<a, b> := LazyPowerSeriesRing(Rationals(), 2);
> t := (1 + 1/2*a + 3*b + 4*a*b + 1/5*a^2 + 5/6*b^2)^-20;
> time Coefficients(t, 29);  
<SNIP>                            
Time: 1.580

> s := (1 + a^14*b^9 + 8/3*a^22*b^11 - 1/13*a^23*b^19 + a^15*b^28)^-20;
> time Coefficients(s, 50);
<SNIP>
Time: 90.840
```



In the case where this package performs badly, it seems to be caused by the rational coefficients:


```
sage: Z.<a,b> = MPowerSeriesRing(QQ,2)

sage: time (1 + a + b + a*b + a^2 + b^2 + Z(0).O(30))^-20;
CPU times: user 1.90 s, sys: 0.00 s, total: 1.90 s
Wall time: 1.90 s

sage: time (1 + a + 2*b - a*b + 3*a^2 - b^2 + Z(0).O(30))^-20;
CPU times: user 2.78 s, sys: 0.00 s, total: 2.78 s
Wall time: 2.78 s

sage: time (1 + a + 12*b - 10*a*b + 13*a^2 - 7*b^2 + Z(0).O(30))^-20;
CPU times: user 3.14 s, sys: 0.00 s, total: 3.14 s
Wall time: 3.14 s
```



---

Comment by niles created at 2010-07-17 10:57:27

Replying to [comment:8 niles]:
> This sage patch performs substantially better in 3/4 cases...

oops; should be "This patch performs substantially better in 4/5 cases..."


---

Comment by SimonKing created at 2010-07-21 16:48:38

Changing keywords from "" to "multivariate power series".


---

Comment by SimonKing created at 2010-07-21 16:48:38

First of all: It would certainly be good to have multivariate power series in Sage. Also the performance seems to be pretty good. Thank you!

I have some criticism, though.

1. `__contains__` and coercion

I was reading part of the patch, and I see that your multivariate power series rings have a custom `__contains__` method. I think it should be possible to simply inherit it.

Moreover, the custom method seems to provide a non-standard behaviour: Usual in Sage is to have `a in R` if and only if `a==R(a)` is True (of course, if `R(a)` raises an error then a is not in R).

Another formulation of the rule is: If a.parent() is P and R has a coercion map from P then a is in R: Since there is a coercion map, R(a) is supposed to work, and `a==R(a)` is equivalent to `R(a)==R(a)`, because this is how comparison with the coercion model works.

But you have in your doctests

```
sage: a in R
False
sage: R(a) in R
True
```

in a situation were apparently a coercion from `a.parent()` to `R` exists.

2. Use of double-underscore methods

In your `__cmp__` method, you do 
`self._bg_value.__cmp__(other._bg_value)`
Generally, one should avoid to call double-underscore methods directly. So, better do 
`cmp(self._bg_value, other._bg_value)`

The same applies to doctests. So, instead of

```
sage: R.<x,y> = MPowerSeriesRing(GF(17)) 
sage: R   
Multivariate Power Series Ring in x, y over Finite Field of size 17 
sage: R.__repr__() 
'Multivariate Power Series Ring in x, y over Finite Field of size 17'
```

you should do

```
sage: R     # indirect doctest
Multivariate Power Series Ring in x, y over Finite Field of size 17
```

and instead of 

```
sage: M = MPowerSeriesRing(ZZ,5,'t');
sage: N = M.remove_var(M.gens()[2])
sage: M.__contains__(N.random_element(10))
False
sage: M.__contains__(M.random_element(10))
True
```

you should have

```
sage: M.random_element(10) in M
True
```



I think it should even be

```
sage: N.random_element(10) in M
True   # not False!
```

because, if I understand correctly,  there is a coercion from N to M -- see point 1.

I am now running `make ptestlong`, and will then have a closer look at the code - so, no review yet. But I think you should address the points above.


---

Comment by SimonKing created at 2010-07-21 22:07:23

With `make ptestlong`, I obtained:

```
The following tests failed:

        sage -t  -long devel/sage/sage/rings/multi_power_series_ring.py # 15 doctests failed
        sage -t  -long devel/sage/sage/rings/multi_power_series_ring_element.py # 28 doctests failed
```


These are quite many failures. So, this needs work.


---

Comment by SimonKing created at 2010-07-21 22:07:23

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-07-22 07:50:27

PS:

It would be nice if the double square bracket notation would work in the multivariate case:

```
sage: QQ[This is the Trac macro *'x'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'x'-macro)
Power Series Ring in x over Rational Field
sage: QQ[This is the Trac macro *'x','y'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'x','y'-macro)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/king/SAGE/<ipython console> in <module>()

/home/king/SAGE/sage-4.4.2/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2612)()

NotImplementedError: Power series rings only implemented in 1 variable
```



---

Comment by niles created at 2010-07-24 08:17:00

Thanks for taking a look at this; I'll address the other work issues soon, but for now I wanted to check the doctests.  There aren't any tests flagged as `#long`, so I didn't think `sage -t -long` should be different from `sage -t`.  And in any case, I get


```
sage -t -long "devel/sage/sage/rings/multi_power_series_ring.py"
	 [2.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.7 seconds

sage -t -long "devel/sage/sage/rings/multi_power_series_ring_element.py"
	 [3.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.3 seconds
```


Do you get all tests passed without `-long`?  If not, maybe you forgot to add the patches at #9457 and #9443 (mentioned in my first trac comment)?  If you still have doctest failures, could you send me a little more about what's failing?


---

Comment by SimonKing created at 2010-07-24 10:08:36

Replying to [comment:14 niles]:
> Do you get all tests passed without `-long`?  If not, maybe you forgot to add the patches at #9457 and #9443 (mentioned in my first trac comment)? 

Outch! Sorry, I missed that. I think I'll not be able to resume work before Monday, but then I'll try again with #9457 and #9433.

Cheers, Simon


---

Comment by niles created at 2010-08-01 15:58:43

Thanks for the tips!

Replying to [comment:11 SimonKing]:
> 1. `__contains__` and coercion

`__contains__` is now inherited, and non-standard behaviour fixed (I wasn't aware of the standard).

> 
> 2. Use of double-underscore methods

I have fixed as many of these as I could find (probably all of them, but let me know if there are more issues).

> 
> 
> I am now running `make ptestlong`, and will then have a closer look at the code - so, no review yet. But I think you should address the points above.

Indeed; I have found that my installation of sage fails some long doctests even before the patches are applied, so I will have to do a fresh installation before I can test this myself properly.

Also, I had some time to kill so I've added support for the double bracket method, and this is included in the documentation.

```
sage: ZZ[This is the Trac macro *'s,t,u'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'s,t,u'-macro)
Multivariate Power Series Ring in s, t, u over Integer Ring
```


Finally, with a little more free time I added support for `exponents` and a basic version of the verschiebung, `V`.  These were among the pile of not-yet-implemented methods inherited from univariate power series.


---

Comment by niles created at 2010-08-03 22:25:11

Since the patch at #9457 seems to be running into trouble, I decided to see if I could make this patch independent from it.  As it turns out, this has happened already somehow! 

`make ptestlong` just finished, passing all tests, with this patch and the one at #9443.  To verify this, I recommend first doctesting just the files `sage/rings/multi_power_series_ring.py`, `sage/rings/multi_power_series_ring_element.py`, and `sage/schemes/elliptic_curves/sha_tate.py` (with `-long`); if these pass all tests, then `make ptestlong` should too.  I'm changing the status to "needs review" since all of the work issues have been addressed, but of course it can be switched back if there are further issues.


---

Comment by niles created at 2010-08-03 22:25:11

Changing status from needs_work to needs_review.


---

Comment by niles created at 2010-08-23 16:59:38

Changing the milestone to 4.5.3 in an effort to generate attention.  Since dependence on #9457 has been removed, there's no reason to wait until 5.0, is there?


---

Comment by malb created at 2010-09-14 16:57:31

I ran doctests on sage.math and those fail because (I assume) the random seed somehow differs. Niles, does it work for you on sage.math with 4.5.3?


---

Comment by niles created at 2010-09-14 17:08:56

Replying to [comment:19 malb]:
> I ran doctests on sage.math and those fail because (I assume) the random seed somehow differs. Niles, does it work for you on sage.math with 4.5.3?

Ah; I don't have an account on sage.math.  Most of the uses of random_element could be avoided, so I'll submit a new patch without them.


---

Attachment

apply only this patch;  removes needless uses of random_element, adds some doctests, cleans up some documentation


---

Comment by niles created at 2010-09-15 21:49:59

Attached a new, combined patch which removes some unnecessary uses of `random_element`, cleans up some of the documentation, and adds doctests for `NotImplemented` functions inherited from univariate power series (c.f. [comment 4](http://trac.sagemath.org/sage_trac/ticket/1956#comment:4)).  

I now have (agian) the patch passing its own tests and documentation building without warning; `make ptestlong` is currently in progress on sage.math.


---

Comment by malb created at 2010-09-16 12:03:14

I get two long doctest failures


```
File "/mnt/usb1/scratch/malb/sage-4.5.3/devel/sage/sage/rings/multi_power_series_ring.py", line 496:
    sage: W = MPowerSeriesRing(InfinitePolynomialRing(ZZ,'a'),2,'x,y')
Exception raised:
    Traceback (most recent call last):
    ...
    TypeError: is_integral_domain() takes exactly 1 argument (2 given)
```



```
    sage: W.is_noetherian()
Exception raised:
    Traceback (most recent call last):
    ...
    NameError: name 'W' is not defined
```


I'll start reading the code now.


---

Comment by malb created at 2010-09-16 12:03:14

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-09-16 12:09:00

Replying to [comment:22 malb]:
> I get two long doctest failures
> 
>     TypeError: is_integral_domain() takes exactly 1 argument (2 given)
> 

It is originally stated on this ticket that "one also needs the patches at #9457 and #9443". Did you take this into account?

The purpose of #9443 is to make `is_integral_domain` accept optional arguments, and this should solve the problem. Therefore, I switch back to "needs review".


---

Comment by SimonKing created at 2010-09-16 12:09:00

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-09-16 12:48:37

The code looks good modulo some tiny issues:

 * I'll attach a referee patch in a sec which improves the Sphinx typesetting slightly
 * I'm not happy about the docstring "This function works, but doesn't get called when it should." Either the function should get removed or the problem fixed.

Modulo those I give this patch a positive review.

PS:http://sage.math.washington.edu/home/malb/scratch_sage/sage-4.5.3/devel/sage/doc/output/html/en/reference/sage/rings/multi_power_series_ring_element.html to see how it looks like in the reference manual.


---

Comment by malb created at 2010-09-16 12:49:42

Sorry for not checking the original description carefully enough.


---

Comment by malb created at 2010-09-16 12:49:42

Changing status from needs_review to needs_work.


---

Comment by niles created at 2010-09-16 17:08:19

sorry; I should have mentioned the dependency in the description (fixed now).

While trying to write a detailed email explaining how I can't understand the coercion model, I realized that the problem with `_l_action_` not being called is probably that the `Completion` functor didn't know how to complete multivariate polynomial rings to multivariate power series rings . . . so that's fixed now, and it does fix the `_l_action_` problem :)

After I check for new doctest failures, I'll upload the new patch.


---

Comment by niles created at 2010-09-16 17:24:53

apply only this patch; fixes coercion problems coming from incomplete functorial construction


---

Comment by niles created at 2010-09-16 17:29:42

Changing status from needs_work to needs_review.


---

Attachment

Ok, the latest patch [attachment:trac_1956_multi_power_series_new_2.patch] passes all tests in the `sage/rings` directory, so I'm uploading it and starting `ptestlong`.

At this point, I'd like to start thinking that any other limitations of this patch should be filed under a new ticket, but we'll see what comes up.


---

Comment by niles created at 2010-09-16 17:53:55

apply only this patch; minor docstring fixes, and update to `remove_var`


---

Attachment

forgot to check the documentation!  There's just one minor fix, and it reminded me to update the behavior of `remove_var` to be consistent with the (new) behavior of `remove_var` for multivariate polynomial rings.  Here's the new patch: [attachment:trac_1956_multi_power_series_new_3.patch].

sorry for the rapid-fire posts!


---

Comment by malb created at 2010-09-16 20:17:36

All looks good to me now.


---

Comment by malb created at 2010-09-16 20:17:36

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-09-19 19:59:15

Changing status from positive_review to needs_work.


---

Comment by mhansen created at 2010-09-19 19:59:15

I think there are still some problems with this.  For example:

1. Pickling does not work for these objects -- one needs to define a proper !__reduce!__ method. 

2. I don't think we should continue the use of !__ attributes as they just cause problems.  For example, the code in here has to set attributes like _PowerSeriesRing_generic!__power_series_class in subclasses.

3. There are formating issues in some of the docstrings like '_latex_'

4. We shouldn't have a 'MPowerSeriesRing' -- that functionality should just be in PowerSeriesRing.  MPolynomialRing was deprecated for the same reason a long time ago.


---

Comment by niles created at 2010-09-20 17:58:04

Replying to [comment:31 mhansen]:
> I think there are still some problems with this.  For example:
> 
> 1. Pickling does not work for these objects -- one needs to define a proper !__reduce!__ method. 

done now; patch forthcoming.

> 
> 2. I don't think we should continue the use of !__ attributes as they just cause problems.  For example, the code in here has to set attributes like _PowerSeriesRing_generic!__power_series_class in subclasses.

The use of `__` attributes here is modeled after their use (for better or worse) in `PowerSeriesRing_generic` (see 4. below); it is also in keeping with the python philosophy, that `__` attributes or methods may be removed or changed in future versions.  It is entirely possible that someone will eventually want to significantly rework multi/univariate power series.  Having said that, they can be removed without too much trouble if sage development policy is strongly against them (in this case, perhaps the developer guide should mention it clearly somewhere).

> 
> 3. There are formating issues in some of the docstrings like '_latex_'

`_latex_` is fixed now, and I looked for other problems but didn't see any; my best known method for checking docstring formatting is using `sage -docbuild`, which only shows warnings/errors for non-underscore methods . . . can you recommend a better way?

> 
> 4. We shouldn't have a 'MPowerSeriesRing' -- that functionality should just be in PowerSeriesRing.  MPolynomialRing was deprecated for the same reason a long time ago.

I agree, but I think that issue is beyond the scope of this ticket.  Implementing multivariate power series arithmetic is already long and complex enough, without having to also worry about integrating them with the univariate power series code (which is heavily specialized for the single-variable case).  I have spent time thinking about how to do this, and I think it will be a subtle problem to solve; there is a sizable body of code that depends on `PowerSeriesRing` as it stands, and one will have to be careful about extending its functionality without breaking any of the current uses.  So I suggest that we merge this ticket and then open a new ticket for _Unify construction of uni- and multi-variate power series rings, as has been done for polynomial rings_.

It would probably be good if the other people involved in this ticket could comment on this last point.


---

Comment by niles created at 2010-09-20 17:58:04

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-09-20 18:17:42

Replying to [comment:32 niles]:

> I agree, but I think that issue is beyond the scope of this ticket.  Implementing multivariate power series arithmetic is already long and complex enough, without having to also worry about integrating them with the univariate power series code (which is heavily specialized for the single-variable case).  I have spent time thinking about how to do this, and I think it will be a subtle problem to solve; there is a sizable body of code that depends on `PowerSeriesRing` as it stands, and one will have to be careful about extending its functionality without breaking any of the current uses.  So I suggest that we merge this ticket and then open a new ticket for _Unify construction of uni- and multi-variate power series rings, as has been done for polynomial rings_. It would probably be good if the other people involved in this ticket could comment on this last point

I think you may have misunderstood what I meant. In the patch, you've made a function "MPowerSeriesRing" which is basically a copy of the function "PowerSeriesRing" defined in power_series_ring.py.  It is just responsible for caching and returning the correct type.  There is an assert statement in PowerSeriesRing that makes sure that you're only trying to make a univariate power series ring.  This function should just be changed to return the appropriate thing in the multivariate case.  This is maybe like 10 lines of code or so (and changing doctests).


---

Comment by niles created at 2010-09-20 18:31:48

Replying to [comment:34 mhansen]:
> 
> I think you may have misunderstood what I meant. In the patch, you've made a function "MPowerSeriesRing" which is basically a copy of the function "PowerSeriesRing" defined in power_series_ring.py.  It is just responsible for caching and returning the correct type.  There is an assert statement in PowerSeriesRing that makes sure that you're only trying to make a univariate power series ring.  This function should just be changed to return the appropriate thing in the multivariate case.  This is maybe like 10 lines of code or so (and changing doctests).

Well, I'm slightly embarrassed to say it, but I think did understand what you meant.  I have tried a few times now, but each time I look at the code for `PowerSeriesRing`, I find it confusing and a bit overwhelming.  I thought perhaps looking at the code for `PolynomialRing` would offer some guidance, but that only made things worse.  It seems that each of these go to great lengths to allow (positional) arguments to be given in a variety of orders, and somehow I find this intimidating.  (I have a hard time telling how various input cases are handled, for example.)

I'll spend a couple more days on it, but I won't be heartbroken if someone reassigns it to a new patch, or decides that it's so easy they can do it themselves in under an hour ;)


---

Comment by mhansen created at 2010-09-20 18:34:02

I'll update the patch to take care of this.


---

Comment by niles created at 2010-09-20 20:54:12

Replying to [comment:36 mhansen]:
> I'll update the patch to take care of this.

that would be great!  thanks :)


---

Comment by niles created at 2010-09-21 13:50:34

Changing status from needs_review to needs_work.


---

Comment by niles created at 2010-09-21 13:50:34

For what it's worth, here is the specific issue I'm stuck on: `PowerSeries` allows the argument `default_prec` to be specified using either the first or second position:


```
sage: T = PowerSeriesRing(QQ,'t',3)
sage: T.default_prec()
3

sage: T = PowerSeriesRing(QQ,3,names='t')
sage: T.default_prec()
3
sage: T.variable_name()
't'
```


So what's the best way to preserve this functionality, but also allow creation of multivariate power series using the same (or similar) syntax as `PolynomialRing` uses? e.g.


```
sage: R = PolynomialRing(QQ,3,'r'); R
Multivariate Polynomial Ring in r0, r1, r2 over Rational Field
sage: R = PolynomialRing(QQ,'r',3); R
Multivariate Polynomial Ring in r0, r1, r2 over Rational Field
```


Note, on the other hand, that the following give errors:

```
sage: T = PowerSeriesRing(QQ,3,'t')
Traceback (most recent call last):
...
ValueError: first letter of variable name must be a letter

sage: T = PowerSeriesRing(QQ,3,name='t')
Traceback (most recent call last):
...
TypeError: PowerSeriesRing() got multiple values for keyword argument 'name'
```


To me, it seems that the current behavior (assuming integer arguments are meant to be `default_prec`) should be deprecated, and the allowed syntax of `PowerSeriesRing` should mirror that of `PolynomialRing`.


Oh, I just realized what I should try:  Make `PowerSeriesRing(QQ,3,'t')` and `PowerSeriesRing(QQ,'t,u,v')` create multivariate power series rings, and raise deprecation warnings in the other cases (as long as the rest of sage doesn't depend too heavily on this behavior); then `MPowerSeriesRing` never has to exist, `PowerSeriesRing` will sort of work as expected, and eventually it can be brought properly in line with `PolynomialRing`.  How does that sound to other people here?


---

Comment by niles created at 2010-09-23 17:17:36

implements multivariate power series rings through `PowerSeriesRing`


---

Attachment

Ok, I've attached a new patch which carries out the plan above.  After running doctests, it seems that there is a non-trivial body of code (elliptic curves, and maybe p-adics) that makes use of the syntax


```
T = PowerSeriesRing(QQ,'t',3)
```


or


```
T.<t> = PowerSeriesRing(QQ,3)
```


to construct univariate power series rings.  I will mention this and a few other things in a new ticket for merging univariate and multivariate power series rings.

This new patch passes all doctests (with -long), and documentation builds cleanly, looks good.


---

Comment by niles created at 2010-09-23 17:35:14

Changing status from needs_work to needs_review.


---

Comment by niles created at 2010-09-23 17:52:57

New tickets:

 * #9980 asks for the confounding behavior of `PowerSeriesRing` to be deprecated.
 * #9981 calls for unifying univariate and multivariate power series rings.


---

Comment by niles created at 2010-09-24 18:24:07

Note: these patches apply cleanly to sage 4.6.alpha1


---

Attachment

minor change fixing `_im_gens_` for use with ring homomorphisms


---

Comment by niles created at 2010-10-10 20:20:27

Hello,

Although we've probably missed the 4.6 release by now, maybe someone could take a look at this in time for the 4.7 release?

best,
Niles


---

Comment by malb created at 2010-10-12 12:43:18

Hi, I tried to apply the patch against 4.6.alpha3 and it failed (bitrot). I can take a look once that's fixed but I think it would be best if Mike would take a look as well.


---

Comment by niles created at 2010-10-19 12:45:53

Replying to [comment:44 malb]:
> Hi, I tried to apply the patch against 4.6.alpha3 and it failed (bitrot). I can take a look once that's fixed but I think it would be best if Mike would take a look as well.

I finally got 4.6.alpha3 built, but I didn't have any errors applying the patches . . . can you double check that you first applied [attachment:trac_1956_multi_power_series_new_4.patch] and then [attachment:trac_1956_uni_multi_ps_2.patch]? (I did get errors when applying only the second of these)  If there are still errors, could you send me a snippet of the failure message?

Thanks for staying with this!


---

Comment by malb created at 2010-10-19 17:19:51

You are right, I cannot reproduce my problem. As instructed above, I can indeed apply the patch cleanly.

Some more comments (I'm really not the best person to review this code):

Here are some performance figures:


```python
sage: R.<t,u,v> = PowerSeriesRing(QQ); R
Multivariate Power Series Ring in t, u, v over Rational Field
sage: f = R.random_element(prec=20,bound=20)
sage: fp = f.polynomial()
sage: %timeit f^2 # power series
125 loops, best of 3: 2.89 ms per loop

sage: %timeit fp^2 # polynomials
625 loops, best of 3: 82.4 µs per loop

sage: R.<t,u,v> = PowerSeriesRing(GF(127)); R
Multivariate Power Series Ring in t, u, v over Finite Field of size 127
sage: f = R.random_element(prec=20,bound=20)
sage: fp = f.polynomial()

sage: %timeit f^2 # power series
625 loops, best of 3: 1.06 ms per loop

sage: %timeit fp^2 # polynomials
625 loops, best of 3: 15.3 µs per loop
```


I also noticed that this is rather slow:


```python
sage: sage: R.<t,u,v> = PowerSeriesRing(GF(127)); R
Multivariate Power Series Ring in t, u, v over Finite Field of size 127
sage: f = R.random_element(prec=20,bound=20)
sage: p = f.polynomial()
sage: fp = f.polynomial()
sage: %timeit R(fp)
25 loops, best of 3: 11.1 ms per loop
```


Conversion to Magma didn't seem to work at all, or am I doing it wrong?


```python
sage: magma(f)
In file "/home/malb/.sage//temp/road/7093//interface//tmp7130", line 1, column 16:
>> _sage_[4]:=-63*u^4 + 11*t*v^8 - 17*t^3*u^4*v^3 - 61*t^4*u^5*v^2 + 16*t^5*u^
                  ^
User error: Identifier 'u' has not been declared or assigned
```



---

Comment by niles created at 2010-10-19 17:58:15

Replying to [comment:46 malb]:

> 
> Here are some performance figures:
> <SNIP>

Thanks; I think these are outside the scope of this ticket (although important!)  Here are the numbers I get:


```
sage: R.<t,u,v> = PowerSeriesRing(QQ); R
Multivariate Power Series Ring in t, u, v over Rational Field
sage: f = R.random_element(prec=20,bound=20)
sage: fp = f.polynomial()
sage: %timeit f^2 # power series
125 loops, best of 3: 2.67 ms per loop

sage: %timeit fp^2 # polynomials
625 loops, best of 3: 52.3 µs per loop
```


The arithmetic is done in a univariate power series ring over a multivariate power series ring (called the "background ring" in the code):

```
sage: R._bg_ps_ring()
Power Series Ring in T over Multivariate Polynomial Ring in t, u, v over Rational Field
sage: fb = f._bg_value
sage: %timeit fb^2
125 loops, best of 3: 2.61 ms per loop
```


So the speed is a limitation of univariate power series rings over multivariate polynomial rings . . .


```
sage: R.<t,u,v> = PowerSeriesRing(GF(127)); R
Multivariate Power Series Ring in t, u, v over Finite Field of size 127
sage: f = R.random_element(prec=20,bound=20)
sage: fp = f.polynomial()

sage: %timeit f^2 # power series
625 loops, best of 3: 1.48 ms per loop

sage: %timeit fp^2 # polynomials
625 loops, best of 3: 20.8 µs per loop

sage: fb = f._bg_value # univariate power series over multivariate polynomials
sage: %timeit fb^2
625 loops, best of 3: 1.42 ms per loop
```


> 
> Conversion to Magma didn't seem to work at all, or am I doing it wrong?
> 
I don't know anything about converting to magma, but the following are also broken:


```
sage: magma(fp)
TypeError: Error evaluating Magma code.
IN:_sage_[5]:=SageCreateWithNames(PolynomialRing(_sage_ref2,3,negdeglex),["t","u","v"]);
OUT:
>> _sage_[5]:=SageCreateWithNames(PolynomialRing(_sage_ref2,3,negdeglex),["t",
                                                              ^

User error: Identifier 'negdeglex' has not been declared or assigned

sage:magma(fb)
>> _sage_[6]:=32*t^4*T^4 + 30*t^2*u*v^5*T^8 - 21*t^3*u^3*v^3*T^9 + 56*t*u^7*v^
                 ^
User error: Identifier 't' has not been declared or assigned

```



---

Comment by malb created at 2010-10-19 18:23:35

Replying to [comment:47 niles]:
> I don't know anything about converting to magma, but the following are also broken:
> 
> {{{
> sage: magma(fp)
> TypeError: Error evaluating Magma code.
> IN:_sage_[5]:=SageCreateWithNames(PolynomialRing(_sage_ref2,3,negdeglex),["t","u","v"]);
> OUT:
> >> _sage_[5]:=SageCreateWithNames(PolynomialRing(_sage_ref2,3,negdeglex),["t",
>                                                               ^
> 
> User error: Identifier 'negdeglex' has not been declared or assigned

Magma doesn't support local orderings for multivariate polynomial rings.


---

Comment by niles created at 2010-10-26 17:39:11

Replying to [comment:47 niles]:

Mike, would you be able to take a look at this some time?  

Here are some further comparisons with polynomial arithmetic, computing ``f**k`` for various values of ``k``.  Obviously the power series computation has a greater and greater advantage over the polynomial computation as ``k`` grows, since the polynomial arithmetic computes many more (irrelevant) terms.  So the time tests below aren't exactly fair -- one could compute the necessary terms by computing small polynomial powers, truncating, and repeating -- but part of the point of the power series code is to automate this for the user.  One side effect is that arithmetic for small powers is slower, but for large powers the power series arithmetic is fairly good: below, I have a comparison in a simple special case: ``k = 2**n`` and non-zero constant coefficient.

In any case, the point of this ticket is to implement the basic arithmetic.  The code should be fast enough for basic use, and speed improvement can be part of a separate ticket.

## Timings for ``f**k`` v.s. ``fp**k``


```
sage: BaseRingList = [ZZ,QQ,GF(11),GF(65537)]

sage: for B in BaseRingList:
    R = PowerSeriesRing(B,4,'t'); R
    f = R.random_element(prec=10,bound=20)
    fp = f.polynomial()
    for k in [2,5,8,11]:   
        print 'f**'+str(k)+': (power series)'
        timeit('f**k',number=5)
        print 'fp**'+str(k)+': (polynomial)'
        timeit('fp**k',number=5)
        print '--'
....:         
Multivariate Power Series Ring in t0, t1, t2, t3 over Integer Ring
f**2: (power series)
5 loops, best of 3: 879 µs per loop
fp**2: (polynomial)
5 loops, best of 3: 33.2 µs per loop
--
f**5: (power series)
5 loops, best of 3: 4.12 ms per loop
fp**5: (polynomial)
5 loops, best of 3: 2.52 ms per loop
--
f**8: (power series)
5 loops, best of 3: 6.47 ms per loop
fp**8: (polynomial)
5 loops, best of 3: 51.5 ms per loop
--
f**11: (power series)
5 loops, best of 3: 10.8 ms per loop
fp**11: (polynomial)
5 loops, best of 3: 652 ms per loop
--

Multivariate Power Series Ring in t0, t1, t2, t3 over Rational Field
f**2: (power series)
5 loops, best of 3: 1 ms per loop
fp**2: (polynomial)
5 loops, best of 3: 44.8 µs per loop
--
f**5: (power series)
5 loops, best of 3: 8.68 ms per loop
fp**5: (polynomial)
5 loops, best of 3: 4.12 ms per loop
--
f**8: (power series)
5 loops, best of 3: 26.4 ms per loop
fp**8: (polynomial)
5 loops, best of 3: 119 ms per loop
--
f**11: (power series)
5 loops, best of 3: 58.4 ms per loop
fp**11: (polynomial)
5 loops, best of 3: 2.28 s per loop
--

Multivariate Power Series Ring in t0, t1, t2, t3 over Finite Field of size 11
f**2: (power series)
5 loops, best of 3: 480 µs per loop
fp**2: (polynomial)
5 loops, best of 3: 10.4 µs per loop
--
f**5: (power series)
5 loops, best of 3: 2.49 ms per loop
fp**5: (polynomial)
5 loops, best of 3: 547 µs per loop
--
f**8: (power series)
5 loops, best of 3: 4.23 ms per loop
fp**8: (polynomial)
5 loops, best of 3: 11 ms per loop
--
f**11: (power series)
5 loops, best of 3: 8.6 ms per loop
fp**11: (polynomial)
5 loops, best of 3: 190 ms per loop
--

Multivariate Power Series Ring in t0, t1, t2, t3 over Finite Field of size 65537
f**2: (power series)
5 loops, best of 3: 614 µs per loop
fp**2: (polynomial)
5 loops, best of 3: 18.8 µs per loop
--
f**5: (power series)
5 loops, best of 3: 4.37 ms per loop
fp**5: (polynomial)
5 loops, best of 3: 3.13 ms per loop
--
f**8: (power series)
5 loops, best of 3: 16.5 ms per loop
fp**8: (polynomial)
5 loops, best of 3: 231 ms per loop
--
f**11: (power series)
5 loops, best of 3: 29.7 ms per loop
fp**11: (polynomial)
5 loops, best of 3: 4.85 s per loop
--
```



## Timings for ``f**(2**n)`` v.s. iterated square-and-truncate for ``fp**(2**n)``

Here is a simple special case:  for a power series `f` with non-zero constant coefficient, the total-degree precision of `f**k` is equal to the total-degree precision of `f` for all `k`.  Below is a function which uses polynomial arithmetic to compute coefficients of `fp**k` up to given total degree for `k = 2^n`, where `fp = f.polynomial()`.


```
sage: def tot_deg_truncate(g,d):
    return sum(g.monomial_coefficient(m)*m for m in [x for x in g.monomials() if x.degree() < d])
....: 

sage: def pow_recursive(g,k,d):
    if k == 2:
        return tot_deg_truncate(g**2,d)
    else:
        return pow_recursive(tot_deg_truncate(g**2,d),k/2,d)
....:     

sage: R = PowerSeriesRing(ZZ,4,'t')
sage: f = 1 + R.random_element(prec=10,bound=20)
sage: f.constant_coefficient()
1
sage: fp = f.polynomial()
```


Check that ``pow_recursive`` gets the right answer:

```
sage: f**16 - pow_recursive(fp,16,10)
0 + O(t0, t1, t2, t3)^10
sage: f**64 - pow_recursive(fp,64,10)
0 + O(t0, t1, t2, t3)^10
```


Compare timings; although the polynomial arithmetic is faster, they are on roughly the same order of magnitude.

```
sage: %timeit f**16
125 loops, best of 3: 4.8 ms per loop
sage: %timeit pow_recursive(fp,16,10)
625 loops, best of 3: 1.18 ms per loop

sage: %timeit f**64
125 loops, best of 3: 7.21 ms per loop
sage: %timeit pow_recursive(fp,64,10)
125 loops, best of 3: 1.76 ms per loop
```


Increasing the precision exaggerates the difference:


```
sage: f = 1 + R.random_element(prec=30,bound=20)
sage: f.constant_coefficient()
1
sage: fp = f.polynomial()
sage: f**16 - pow_recursive(fp,16,30)
0 + O(t0, t1, t2, t3)^30
sage: f**64 - pow_recursive(fp,64,30)
0 + O(t0, t1, t2, t3)^30

sage: %timeit f**16
25 loops, best of 3: 15.9 ms per loop
sage: %timeit pow_recursive(fp,16,30)
125 loops, best of 3: 1.81 ms per loop

sage: %timeit f**64
25 loops, best of 3: 23.9 ms per loop
sage: %timeit pow_recursive(fp,64,30)
125 loops, best of 3: 2.65 ms per loop
```



---

Comment by malb created at 2010-11-23 18:40:14

I just ran long doctests on 4.6.1.alpha2 and they still pass. I'll ask people for feedback on [sage-devel], if there is none within a few days, I'll just give this patch a positive review. This patch shouldn't have bit rotted so long!


---

Comment by was created at 2010-11-23 20:19:50

Looking with my eyes... I found one bug not mentioned or fixed elsewhere:

```
733	        except TypeError,AttributeError:
```

This should be

```
733	        except (TypeError,AttributeError):
```

otherwise, AttributeError gets *set* to the string that the TypeError raises.  Do check for other cases of this issue in the code. 

This scares me a little:

```
raise TypeError("action of "+c.parent()+" on "+f.parent()+" not defined.")
```

the reason is that any exception such that constructing a string as part of it could take time, can potentially *MASSIVELY* slow down Sage.   Just do:

```
raise TypeError
```

or

```
raise TypeError, "action not defined"
```

instead.  Since otherwise, constructing that string might dominate arithmetic... (the coercion model will try to do the arithmetic, get the error, then try something else).   Also, it is easy enough using "%debug" to see what all the relevant variables are when one gets an exception.

I see this also

```
 	1062	            except: 
```

I am against using naked excepts unless their is a very good reason to do so.

I also think that whenever possible all the inputs to a function should be documented.  For example look at this one:

```
109	109	    def completion(self, p, prec=20, extras=None): 
 	110	        """ 
 	111	        Return the completion of self with respect to the ideal generated 
 	112	        by the variable(s) ``p``. 
 	113	 
 	114	        INPUT: 
 	115	 
 	116	        - ``p`` -- variable or tuple of variables 
 	117	 
 	118	        EXAMPLES:: 
```


I think prec and extras should be documented.  Especially important is "extras", since that is not self-explanatory at all.  There is also a function `def solve_linear_de(self, prec = infinity, b=None, f0=None): ` with no docs on its input.  Since it just does `raise NotImplementedError` I think that's fine. 

I don't like all this "type(obj)==type" stuff.  I think isinstance(obj,type) is much better:

```
        140	        if p in self or type(p) == str and set(p).issubset(set([str(g) for g in self.gens()])): 
 	141	            p = tuple([p]) 
 	142	        elif type(p) == list or type(p) == tuple: 
```



---

Comment by was created at 2010-11-23 20:19:50

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-11-23 20:21:26

I should have added -- having read/skimmed through all the code, I think this is a *wonderful* contribution to Sage, and it's really excellent code.  Thanks for finally pulling this off!!


---

Comment by cremona created at 2010-11-23 20:33:04

Replying to [comment:52 was]:
> I should have added -- having read/skimmed through all the code, I think this is a *wonderful* contribution to Sage, and it's really excellent code.  Thanks for finally pulling this off!!

I strongly agree -- and I'm sorry that I have not had time to contribute, not even by reviewing.  I certainly expect to use this code.

Reading through the posts on this ticket, I think it is a really good example of good-natured cooperation and constructive criticism producing something excellent.


---

Comment by niles created at 2010-11-24 01:27:37

Replying to [comment:53 cremona]:
> Replying to [comment:52 was]:

Thanks for the feedback, and the encouragement; I'll try to get back to this next week, since I would really like to have this patch finished up (it will turn 4 in January :)


---

Attachment

code cleanup, addressing comments of was


---

Comment by niles created at 2010-11-29 20:12:53

Changing status from needs_work to needs_review.


---

Comment by niles created at 2010-11-29 20:12:53

Thanks for the comments; these have been addressed now.

Replying to [comment:51 was]:
> 
 {{{
 733	        except TypeError,AttributeError:
 }}}
> This should be
> 
 {{{
 733	        except (TypeError,AttributeError):
 }}}


fixed.

 

> This scares me a little:
> 
 {{{
 raise TypeError("action of "+c.parent()+" on "+f.parent()+" not defined.")
 }}}
> the reason is that any exception such that constructing a string as part of it could take time, can potentially *MASSIVELY* slow down Sage.   Just do:
>
 {{{
 raise TypeError
 }}}
> or
>
 {{{
 raise TypeError, "action not defined"
 }}}
> instead.  

This has been fixed, and I've checked every occurrence of "raise ..." for similar problems (there are quite a few, since I've never heard of %debug, or pdb, until now -- perhaps this would be a useful addition to the developer's guide) 

> I see this also
>
 {{{
  	1062	            except: 
 }}}


There were two naked excepts; in both cases the code has been rewritten to avoid them.


> I also think that whenever possible all the inputs to a function should be documented.  For example look at this one ...


I've double-checked all functions now; the example you gave was one of the toughest because I was modifying an existing function (from the multivariate polynomial code).  In any case, it's fixed now.


> I don't like all this "type(obj)==type" stuff.  I think isinstance(obj,type) is much better:

fixed.


---

Comment by niles created at 2010-12-03 20:45:19

Apply trac_1956_multi_power_series_new_4.patch, trac_1956_uni_multi_ps_2.patch, trac_1956_multi_ps_cleanup.patch


---

Comment by pernici created at 2010-12-16 10:40:55

Hi,
  I opened ticket 10480 on fast PowerSeries_poly multiplication.
  Using it multiplication in the multivariate power series implemented here
  should also be much faster,
  since it uses univariate power series multiplication internally.
  
Mario


---

Comment by niles created at 2010-12-20 19:45:05

Anyone interested in setting this to positive review?


---

Attachment


---

Attachment


---

Attachment


---

Comment by pernici created at 2010-12-28 06:49:44

Changing assignee from malb to pernici.


---

Comment by pernici created at 2010-12-28 06:49:44

After applying trac_1956_multi_power_series_new_4.patch,
trac_1956_uni_multi_ps_2.patch,
trac_1956_multi_ps_cleanup.patch
(main version), apply
trac_10480_fast_PowerSeries_poly_multiplication2.patch from ticket #10480 and
trac_1956_faster_MPowerSeries_mul.patch
(version (1) in benchmarks below)

In the attached patch MPowerSeries._mul_ uses the do_mul_trunc_generic
algorithm in polynomial_element.pyx.

The first benchmark has the 8 inversions posted here by Niles to compare
with Magma, but with precisions multiplied by N; times are in seconds;
processor:4-core: Intel Core i7 CPU 860 `@` 2.80GHz
on x86_64 GNU/Linux


```
test no. 1     2     3     4     5     6     7     8
N=1
main     2.72  0.02  0.18  10.5  0.05  1.55  2.33  2.61
(1)      0.05  0.01  0.05  0.24  0.03  0.04  0.07  0.09
N=2
main     290   1.7   0.75  1024  0.16  49.0  64.3  73.8
(1)      2.37  0.02  0.07  5.53  0.05  0.68  1.24  1.41
N=3
main     7743  67    4.4   24272 0.84  432   566   651
(1)      32    0.12  0.11  56    0.08  5.2   7.8   9.1
```

The next benchmark takes a random series and performs p = p*(p+1) N times;
the same series is used in testing with the two versions; see attached mu.sage


```
        N=1   2     3     4
n=2
prec=20 bound=20
main   0.002  0.005 0.005 0.005
(1)    6e-4   6e-4  6e-4  5e-4

prec=100 bound=100
main    0.084 0.81  2.6   3.3
(1)     0.003 0.005 0.006 0.006

prec=200 bound=200
main    0.52  153   3932  7337
(1)     0.03  0.31  1.1   1.2


n=4
prec=20 bound=20
main    0.003 0.003 0.003 0.003
(1)     6e-4  5e-4  5e-4  5e-4

prec=100 bound=100
main    0.087 0.19  0.19  0.19
(1)     0.002 0.002 0.002 0.002

prec=200 bound=200
main    0.59  1.97  1.91  1.66
(1)     0.008 0.008 0.008 0.008
```


Applying only trac_10480_fast_PowerSeries_poly_multiplication2.patch, not
trac_1956_faster_MPowerSeries_mul.patch, MPowerSeries._mul_ uses
univariate series multiplication, which uses the do_mul_trunc algorithm
instead of the do_mul_trunc_generic algorithm; the latter is slower
than the unpatched version in some test in un.sage in #10480,
while the former is always faster.
The latter algorithm is always faster than main in the tests above,
and most of the times a few times faster than the former algorithm, so
it seems a better choice for multivariate series.


With this patch _send_to_bg and _send_to_fg are faster; using
the attached benchmark file bg.sage,
n=number of variables, h=precision, N=100 random polynomials,
bg=_send_to_bg, fg=_send_to_fg


```
     n=2 h=20     n=2 h=100   n=4 h=20     n=4 h=100
     bg    fg     bg    fg    bg    fg     bg   fg
main 0.89  0.02   42    0.06  1.18  0.02   58   0.06
(1)  0.019 0.002  0.09  0.02  0.018 0.002  0.09 0.01
```



---

Comment by niles created at 2010-12-28 14:21:45

Replying to [comment:59 pernici]:

This is great -- on my machine adding your [attachment: trac_1956_faster_MPowerSeries_mul.patch] and `trac_10480_fast_PowerSeries_poly_multiplication2.patch` from #10480 drops the total time for doctests in `sage.rings.multi_power_series_ring_element` from 3.5 seconds to 2.8 seconds.

After reading the discussion at #10480, it looks like speeding up the multiplication is a somewhat subtle problem, so I propose opening a separate ticket for this issue.  Then we can look into the relative advantages of `do_mul_trunc_generic` and the Karatsuba algorithm, and patch `MPowerSeries._mul_` to take advantage of the optimal one.  I'll do this unless you think #10480 already includes this issue.


---

Comment by niles created at 2010-12-28 14:26:21

Oh, I think one of the earlier posts confused the buildbot (it scans for the word "apply").  Here's a clarification:

Apply trac_1956_multi_power_series_new_4.patch, trac_1956_uni_multi_ps_2.patch, trac_1956_multi_ps_cleanup.patch


---

Comment by pernici created at 2010-12-28 17:37:58

Niles wrote:
> After reading the discussion at #10480, it looks like speeding up the multiplication is a somewhat subtle problem, so I propose opening a separate ticket for this issue. Then we can look into the relative advantages of do_mul_trunc_generic and the Karatsuba algorithm, and patch MPowerSeries._mul_ to take advantage of the optimal one. I'll do this unless you think #10480 already includes this issue. 

Nice idea to have a separate ticket for MPowerSeries._mul_ .


---

Comment by niles created at 2010-12-29 15:59:31

Replying to [comment:62 pernici]:
> Nice idea to have a separate ticket for MPowerSeries._mul_ .

This is now #10532; I've added your patch there already :)


---

Comment by pernici created at 2011-01-03 10:20:28

Multivariate series in one variable differ from univariate series;
is it the intended behaviour?


```
sage: R = PowerSeriesRing(GF(127),'t');R
Power Series Ring in t over Finite Field of size 127
sage: %timeit R.random_element(100)
625 loops, best of 3: 856 µs per loop
sage: K = PowerSeriesRing(GF(127),1,'a'); K
Multivariate Power Series Ring in a over Finite Field of size 127
sage: %timeit K.random_element(100)
5 loops, best of 3: 146 ms per loop
```


I noticed this since
the patch trac_1956_faster_MPowerSeries_mul.patch does not work in this
case, because _send_to_bg calls the degrees method


```
sage: %timeit K.random_element(100)
AttributeError: 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint' object has no attribute 'degrees'
```


If multivariate series in one variable are meant to differ from 
univariate series I will modify _send_to_bg to deal with this case.


---

Comment by niles created at 2011-01-03 12:50:21

Replying to [comment:64 pernici]:
> 
> Multivariate series in one variable differ from univariate series;
> is it the intended behaviour?
> 

No, they should be the same -- I'll fix this pretty soon.


---

Comment by niles created at 2011-01-03 12:50:21

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-01-03 12:58:53

Replying to [comment:64 pernici]:
> Multivariate series in one variable differ from univariate series;
> is it the intended behaviour?

I don't know whether it is intended, but I'd like to mention that there already is a difference between univariate polynomials and multivariate polynomials in one variable:

```
sage: R_uni = PolynomialRing(QQ,'x')
sage: R_uni
Univariate Polynomial Ring in x over Rational Field
sage: R_multi = PolynomialRing(QQ,'x',1)
sage: R_multi
Multivariate Polynomial Ring in x over Rational Field
sage: timeit('a = R_uni.random_element()')
625 loops, best of 3: 48.4 Âµs per loop
sage: timeit('a = R_multi.random_element()')
625 loops, best of 3: 192 Âµs per loop
sage: a = R_uni.random_element()
sage: b = R_multi(a)
sage: a.leading_coefficient()
-27
sage: hasattr(b,'leading_coefficient')
False
sage: b.lc()
-27
sage: hasattr(a,'lc')
False
```


While it is clear that there is a difference in the timings for `random_element`, I don't like that the names are different for methods that do essentially the same.

Things are different in the case of `degrees` (which exists only for multivariate polynomials). Since the word is plural (it denotes the tuple of maximal exponents of each variable, not necessarily occuring in a single monomial), it doesn't really make sense in the univariate case. However, I do think that in that case (and similar cases) there should be a method of univariate polynomials emulating the corresponding method for multivariate polynomials with one variable.

So, I don't mind about the different timings; but I think methods should be more or less equivalent.


---

Attachment

apply on top of other patches; return univariate ring rather than multivariate ring in one variable


---

Comment by niles created at 2011-01-04 13:51:54

Changing status from needs_work to needs_review.


---

Comment by niles created at 2011-01-04 13:51:54

I think that the top-level constructors `PolynomialRing` and `PowerSeriesRing` should return univariate rings instead of multivariate rings in one variable.  It is difficult to imagine a situation where someone would want access to the "multivariate in one variable" versions (e.g. they want to use some algorithm implemented for the multivariate case that is not available in the univariate case), and even more difficult to imagine that this is the preferred option of most users.  Someone who does need this functionality can still import the multivariate constructor directly.

With [attachment:trac_1956_one_variable_fix.patch] we have:


```
sage: PowerSeriesRing(QQ,1,'a')
Power Series Ring in a over Rational Field

sage: PowerSeriesRing(QQ,1,'a') is PowerSeriesRing(QQ,'a')
True
```



```
sage: from sage.rings.multi_power_series_ring import MPowerSeriesRing_generic
sage: MPowerSeriesRing_generic(QQ,1,'a')
Multivariate Power Series Ring in a over Rational Field
```


Unless someone here can think of a compelling reason to reverse this change, I think we should also open a new ticket for the polynomial case.  In a related vein, we also have polynomial rings in no variables, and these are different from the base ring:


```
sage: PolynomialRing(ZZ,'a',0)
Multivariate Polynomial Ring in no variables over Integer Ring
sage: PolynomialRing(ZZ,'a',0) is ZZ
False
```


For consistency, I've implemented the same behavior for power series rings:


```
sage: PowerSeriesRing(QQ,0,'a')
Multivariate Power Series Ring in no variables over Rational Field
```


Perhaps these should both simply return the base ring -- I'm not so sure, but in any case I hope it can be handled for both polynomials and power series in a separate ticket.


---

Comment by SimonKing created at 2011-01-04 16:39:26

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-01-04 16:39:26

Replying to [comment:67 niles]:
> I think that the top-level constructors `PolynomialRing` and `PowerSeriesRing` should return univariate rings instead of multivariate rings in one variable. 

It already does:

```
sage: R.<x> = QQ[]
sage: R
Univariate Polynomial Ring in x over Rational Field
sage: R2.<x> = PolynomialRing(QQ)
sage: R2
Univariate Polynomial Ring in x over Rational Field
```


Only when you explicitly request it, you'll get a multivariate ring with one variable:

```
sage: R3.<x> = PolynomialRing(QQ,1)
sage: R3
Multivariate Polynomial Ring in x over Rational Field
```


> It is difficult to imagine a situation where someone would want access to the "multivariate in one variable" versions

I find it very easy to imagine. I sometimes want it so, because multi- and univariate polynomials have different methods, and thus I want to make sure that my programs will always get a _multi_variate polynomial.

> (e.g. they want to use some algorithm implemented for the multivariate case that is not available in the univariate case), and even more difficult to imagine that this is the preferred option of most users.

Agreed, and this is why the polynomial ring constructor returns a univariate ring, unless requested otherwise (in contrast to your claim).

>  Someone who does need this functionality can still import the multivariate constructor directly.

No, one shouldn't, it is deprecated:

```
sage: MPolynomialRing(QQ,1,'a')
/mnt/local/king/SAGE/sage-4.6/local/bin/sage-ipython:1: DeprecationWarning: MPolynomialRing is deprecated, use PolynomialRing instead!
  #!/usr/bin/env python
Multivariate Polynomial Ring in a over Rational Field
```


Instead, one should choose the arguments of the polynomial ring contructor appropriately (as I did above).
 
> With [attachment:trac_1956_one_variable_fix.patch] we have:
> 
> {{{
> sage: PowerSeriesRing(QQ,1,'a')
> Power Series Ring in a over Rational Field
> 
> sage: PowerSeriesRing(QQ,1,'a') is PowerSeriesRing(QQ,'a')
> True
> }}}

I am strongly -1 to that suggestion, because the user must have the possibility to choose the implementation by providing appropriate arguments (with the argument `1` versus without it).
 
> {{{
> sage: from sage.rings.multi_power_series_ring import MPowerSeriesRing_generic
> sage: MPowerSeriesRing_generic(QQ,1,'a')
> Multivariate Power Series Ring in a over Rational Field
> }}}

Using a non-generic constructor should be deprecated, IMO.

> Unless someone here can think of a compelling reason to reverse this change, I think we should also open a new ticket for the polynomial case.

I don't know if you find my argument compelling, but I am strongly against that suggestion.

>  In a related vein, we also have polynomial rings in no variables, and these are different from the base ring:
> 
> {{{
> sage: PolynomialRing(ZZ,'a',0)
> Multivariate Polynomial Ring in no variables over Integer Ring
> sage: PolynomialRing(ZZ,'a',0) is ZZ
> False
> }}}
> 
> For consistency, I've implemented the same behavior for power series rings:
> 
> {{{
> sage: PowerSeriesRing(QQ,0,'a')
> Multivariate Power Series Ring in no variables over Rational Field
> }}}

That's fine.

> Perhaps these should both simply return the base ring -- 

No! The user has _explicitly_ requested a polynomial ring. So, s/he _must not_ get the base ring in return, since s/he may rely on particular methods that may only be implemented for polynomial rings, but not for general rings.


---

Comment by niles created at 2011-01-04 19:27:00

Changing status from needs_work to needs_info.


---

Comment by niles created at 2011-01-04 19:27:00

Hi Simon!

Replying to [comment:68 SimonKing]:
> Replying to [comment:67 niles]:

> > It is difficult to imagine a situation where someone would want access to the "multivariate in one variable" versions
> 
> I find it very easy to imagine. I sometimes want it so, because multi- and univariate polynomials have different methods, and thus I want to make sure that my programs will always get a _multi_variate polynomial.
> 
> > (e.g. they want to use some algorithm implemented for the multivariate case that is not available in the univariate case), and even more difficult to imagine that this is the preferred option of most users.
> 
> Agreed, and this is why the polynomial ring constructor returns a univariate ring, unless requested otherwise (in contrast to your claim).
> 

Thanks for this -- actually I find your arguments here quite compelling.  I was thinking before that arithmetic for univariate power series and polynomials are probably optimized for that case, and so would be preferable to the "multivariate in one variable" algorithms.  But I neglected, as you have pointed out, that one might want to write code which, for simplicity, treats univariate and multivariate rings the same and thus depends on the methods written for multivariate rings.  This would be especially likely if the code one were writing didn't depend on the optimal univariate algorithms.

Of course this is precisely not the case for pernici and others who are working on faster multiplication algorithms.  Pernici, does this seem reasonable to you?  How difficult will it be for you to treat the "multivariate in one variable" case?


---

Comment by SimonKing created at 2011-01-04 20:00:19

Replying to [comment:69 niles]:
> Hi Simon!
> 
> Replying to [comment:68 SimonKing]:
> Thanks for this -- actually I find your arguments here quite compelling.  I was thinking before that arithmetic for univariate power series and polynomials are probably optimized for that case, and so would be preferable to the "multivariate in one variable" algorithms. 

Sure univariate rings are usually preferable! I do think that most users could care less about the different methods of univariate and singly multivariate polynomials - they want speed!

> Of course this is precisely not the case for pernici and others who are working on faster multiplication algorithms.  Pernici, does this seem reasonable to you?  How difficult will it be for you to treat the "multivariate in one variable" case?

I did not suggest that _by default_ the polynomial ring (or power series ring) constructor should return a multivariate ring in one variable. I do think that

```
sage: R.<x> = QQ[[]]
```

should turn `R` into a univariate ring.

What I was trying to explain was: The user must be able to override the default implementation by passing appropriate arguments to the ring constructor. Hence: `PowerSeriesRing(QQ,'x')` should return the default (a univariate ring), but `PowerSeriesRing(QQ,1,'x')` should return a multivariate ring.

In other words: I suggest that you just mimmick the current behaviour of th polynomial ring constructor.

Cheers,
Simon


---

Comment by niles created at 2011-01-07 14:00:37

Replying to [comment:70 SimonKing]:

> In other words: I suggest that you just mimmick the current behaviour of th polynomial ring constructor.
> 

Good--that's the behavior without the "one variable fix" patch :)

This morning I had an idea for helping this code get reviewed (note that the ticket turns 4 at the end of this month):  Could we break the review process into several manageable pieces, and have different people take responsibility for different parts?  For example, I'd propose something like the following:

 1. The underlying concept of the implementation (foreground ring & background ring, etc.)
 1. Documentation and tests
 1. `multi_power_series_ring.py`: the code accurately does what it claims to do
 1. `multi_power_series_ring_element.py`: the code accurately does what it claims to do
 1. Integration with the rest of sage: construction and use of `PowerSeriesRings` works correctly, and parallels behavior of polynomial rings
 1. Completeness of the review:  do these pieces give an essentially complete breakdown of the review?


---

Comment by niles created at 2011-01-07 14:00:37

Changing status from needs_info to needs_review.


---

Comment by pernici created at 2011-01-08 16:04:03

I think that random_element does not give good random multivariate series;
the lowest total degree is usually not zero


```
sage: R.<x,y> = QQ[[]]
sage: def mval(p,N):
....:     print '%.2f' % (sum([sum(R.random_element(p,p).exponents()[0]) for _ in range(N)])/float(N))
....:
sage: mval(20,100)
3.94
sage: mval(100,100)
8.34
```


while in the univariate case it is usually zero

```
sage: R.<x> = QQ[[]]
sage: def mval(p,N):                                                             
....:     print '%.2f' % (sum([R.random_element(p,p).exponents()[0] for _ in range(N)])/float(N))
....:
sage: mval(20,100)
0.02
sage: mval(100,100)
0.01
```


As a quick fix to get pseudo random series I changed the benchmark file mu.sage 
shifting by 1 the variables in the random polynomials

```
sage: R.<x,y> = QQ[[]]        
sage: for prec in range(10,50,10):
....:     p = R.random_element(prec,prec)
....:     p1 = p.polynomial()(x+1,y+1) + R.O(prec)
....:     print 'prec=',prec
....:     %timeit p^10
....:     %timeit p1^10
....:     
prec= 10
625 loops, best of 3: 752 µs per loop
125 loops, best of 3: 3.77 ms per loop
prec= 20
125 loops, best of 3: 3.4 ms per loop
25 loops, best of 3: 25.2 ms per loop
prec= 30
125 loops, best of 3: 5.14 ms per loop
5 loops, best of 3: 151 ms per loop
prec= 40
25 loops, best of 3: 13.3 ms per loop
5 loops, best of 3: 484 ms per loop
```



---

Comment by pernici created at 2011-01-12 12:39:53

This is a follow-up of my previous mail on random_element
in multivariate series.

`R.random_element` calls `R.__poly_ring.random_element`.
From the documentation of `MPolynomialRing_generic.random_element`:

`First monomials are chosen uniformly random from the set of all
possible monomials of degree up to `d` (inclusive). This means
that it is more likely that a monomial of degree `d` appears than
a monomial of degree `d-1` because the former class is bigger.`

This argument is relevant also for multivariate series

```
sage: R.<a,b,c,d> = PowerSeriesRing(QQ,4)
sage: p = (1 + a + 2*b + 3*c + 4*d + R(0).O(16))^-5

sage: [len(x.exponents()) for x in p._bg_value]
[1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286, 364, 455, 560, 680, 816]
```

There are many more terms with high degrees for the reason
given in the quote.

Take a random series of comparable length

```
sage: p1 = R.random_element(16,4000)
sage: [len(x.exponents()) for x in p1._bg_value]
[0, 4, 3, 13, 22, 44, 54, 75, 114, 150, 190, 236, 307, 371, 440, 554]
```

The distribution is fairly similar.

However taking `bound` small in R.random_element(prec,bound)
the lowest total degree is high

```
sage: p1 = R.random_element(16)
sage: [len(x.exponents()) for x in p1._bg_value]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
sage: p1 = R.random_element(16,16)
sage: [len(x.exponents()) for x in p1._bg_value]
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 0, 1, 3, 0, 2]
```


With a high number of variables the situation gets worse;
to get series starting with small lowest total degree
`bound` should be extremely high


```
sage: R = PowerSeriesRing(QQ,100,'t')
sage: p = R.random_element(10,100); sum(p.exponents()[0])
9
sage: p = R.random_element(10,1000); sum(p.exponents()[0])
7
sage: p = R.random_element(10,10000); sum(p.exponents()[0])
7
```

In power series with finite precision `prec`
lower degrees are more important than higher degrees;
if this were not so it would not make sense to throw away terms
with degree higher than prec-1. So I think that lower degrees
should weight more than high degrees in the choice of random
elements.


---

Comment by niles created at 2011-01-12 16:13:13

Replying to [comment:73 pernici]:
> This is a follow-up of my previous mail on random_element
> in multivariate series.

Hi pernici,

Thanks for clarifying this, but I'm not sure how to proceed.  I think I understand what you mean about lower degree terms being "more important" (in the same way that earlier decimal digits are "more important" in a real number).  But I also think it makes a lot of sense for `random_element` to be very similar between multivariate polynomials and multivariate power series -- this is the principle behind a number of implementation choices for multivariate power series.  Nowhere is it promised that `random_element`s are chosen with uniform distribution and, as you point out, the docstring for multivariate polynomials says explicitly that it is using a non-uniform distribution.

So now I wonder what the motivation is for changing the power series `random_element` method:  am I right to guess that you want to use the random elements to test your multiplication code?  If so, let me suggest that it would be better to do this with a [test suite](http://www.sagemath.org/doc/reference/sage/misc/sage_unittest.html), where you can write different custom algorithms for different random distributions and not have to worry about which of these should used for the `random_element` method of polynomials or power series.  (Having said that, I admit that I've found it difficult to get started with sage's test suite classes.  I think there are some implementations for general rings and for integrals, so these might be good examples to follow if you want. )

Or maybe you have a different reason to think about `random_element`?

best,
Niles


---

Comment by pernici created at 2011-01-12 21:37:18

Hi Niles,
I agree that it has some advantages to keep the same random_element as for polynomials;
at least it is well defined mathematically in terms of sets of monomials.

>am I right to guess that you want to use the random elements to test your multiplication code? 

Yes, my motivation for using random polynomials was for benchmarking multiplication;
when I found out that random_element generates typically series without low order terms
I replaced it with a generator which gave them.

>Or maybe you have a different reason to think about random_element? 
No.

Mario


---

Comment by pernici created at 2011-01-13 21:19:28

In this ticket series with total degree truncation are considered. 

How does the case of partial degree truncation work, 
say with `p` a polynomial

```
f = p + O(x^prec_x,y^prec_y)
```

Can one define the partial degree truncation as the total degree truncation with
`prec = prec1+prec2-1`, and if `f._bg_value` has valuation `0` truncate 
`x^prec_x and y^prec_y` ?

With such a definition multiplication would work as in the total degree case, with a truncation of the result, if needed.


---

Comment by pernici created at 2011-01-14 09:05:44

Please disregard my previous message :(

In this ticket series with total degree truncation are considered.

I would like to ask how the case of series with partial degree truncation works.

Consider for example the product of two series in variables `x,y`
with precisions `prec_x,prec_y`; if they start with a constant term one can
just truncate with `O(x^prec_x) , O(y^prec_y)`.

I do not see how it works if there are no constant terms; consider for example
two series with precision 3 in both variables; add a variable `b` to track
the monomials which should be eliminated

```
sage: R.<x,y,b> = QQ[]
sage: p1 = x + y + x^2 + x*y + y^2 + b*(x^3 + y^3)
sage: p2 = x^2 + x*y + y^2 + b*(x^3 + y^3)
sage: p3 = p1*p2
sage: p3.coefficient({b:0})
x^4 + 2*x^3*y + 3*x^2*y^2 + 2*x*y^3 + y^4 + x^3 + 2*x^2*y + 2*x*y^2 + y^3
sage: p3.coefficient({b:1})
2*x^5 + 2*x^4*y + 2*x^3*y^2 + 2*x^2*y^3 + 2*x*y^4 + 2*y^5 + x^4 + x^3*y + x*y^3 + y^4
```


`x^4, x^3*y, x*y^3, y^4` appear in `p3.coefficient({b:1})`
so they should be disregarded; the product of the series should be

```
3*x^2*y^2 + x^3 + 2*x^2*y + 2*x*y^2 + y^3
```

but I do not see how to get this simply with truncations;
neglecting `3*x<sup>2*y</sup>2` one would get the total degree truncation

```
sage: R.<x,y> = QQ[[]]
sage: p1 = x + y + x^2 + x*y + y^2 + R.O(3)
sage: p2 = x^2 + x*y + y^2 + R.O(3)
sage: p1*p2
x^3 + 2*x^2*y + 2*x*y^2 + y^3 + O(x, y)^4
```



---

Comment by niles created at 2011-01-14 12:57:22

Replying to [comment:77 pernici]:
> ...
> but I do not see how to get this simply with truncations;
> ...

I haven't been able to see how to do it either.  There have been a number of unsuccessful tries to get multivariate series in sage, and I think the problem of separate variable precision has been one of the major barriers...


---

Attachment


---

Comment by pernici created at 2011-01-16 17:33:51

attached patch to be applied after
applying trac_1956_multi_power_series_new_4.patch,
trac_1956_uni_multi_ps_2.patch,
trac_1956_multi_ps_cleanup.patch

The univariate series has the property that its representation
can be used to define it

```
sage: S.<t> = QQ[[]]
sage: 1 + t + t^3 + O(t^5)
1 + t + t^3 + O(t^5)
```

In the case of multivariate series this property does not currently hold

```
sage: R.<x,y> = QQ[[]]
sage: p = 1 + x + y^2 + R.O(5); p
1 + x + y^2 + O(x, y)^5
sage: 1 + x + y^2 + O(x, y)^5
TypeError
```

The attached patch is a hack to satisfy this property

```
sage: R.<x,y> = QQ[[]]
sage: 1 + x + y^2 + O(x, y)^5
1 + x + y^2 + O(x, y)^5
```



---

Comment by nthiery created at 2011-01-21 08:41:03

Replying to [comment:79 pernici]:
> The attached patch is a hack to satisfy this property
> {{{
> sage: R.<x,y> = QQ[[]]
> sage: 1 + x + y^2 + O(x, y)^5
> 1 + x + y^2 + O(x, y)^5
> }}}

Very nice syntax!

Btw: I allowed myself to edit the description and title of this ticket, since it took me a bit of time to figure out from the discussion which kind series it was about. That's a cool feature; thanks to all of you for working on it!


---

Comment by pernici created at 2011-01-26 18:01:16

I get some strange behaviour; I want to use the reduce method for a
polynomial extracted from a multivariate series


```
sage: S.<x,y> = QQ[[]]
sage: p = (1+x+y)^3
sage: pp = p.polynomial()
sage: R = S._poly_ring()
sage: xv = R.gens()
sage: pp.reduce([xv[0]^2,xv[1]^2])
1
```


while the expected behavior is as working directly with polynomials

```
sage: R.<x,y> = QQ[]
sage: p = (1+x+y)^3
sage: p.reduce([x^2,y^2])
6*x*y + 3*x + 3*y + 1
```


After some trials I got the expected result by creating a new ring 
and casting the polynomial with it.

```
sage: S.<x,y> = QQ[[]]
sage: p = (1+x+y)^3
sage: pp = p.polynomial()
sage: R = PolynomialRing(QQ,S.variable_names())
sage: xv = R.gens()
sage: pp = R(pp)
sage: pp.reduce([xv[0]^2,xv[1]^2])
6*x*y + 3*x + 3*y + 1
```


This is unsatisfactory because it should not be necessary to introduce
a new MPolynomial_libsingular ring, and cast the polynomial.

Am I doing something wrong or is there a bug?


---

Comment by pernici created at 2011-01-27 12:43:13

pernici wrote:
> while the expected behavior is as working directly with polynomials 

Sorry, there is no problem; the default ordering for multivariate series in `negdeglex`,
while the default ordering of `PolynomialRing` is `degrevlex`, so that 
`reduce` acts differently in the two cases.


---

Comment by pernici created at 2011-02-02 12:01:21

The method sqrt of MPowerSeries does not work because sqrt does not
currently work for series on polynomial rings.

In ticket #10720 nth_root is added;
applying trac_10720_power_series_nth_root_2.patch

the definition of nth_root for MPowerSeries is

```
sage: def nth_root(self, n):
....:     return self.parent(self._bg_value.nth_root(n))
....:
```


Examples:

```
sage: R.<x,y> = QQ[[]]
sage: p = 1 + 2*x + 3*y + R.O(20)
sage: nth_root(p^10,2) - p^5
0 + O(x, y)^20
sage: nth_root(p^10,5) - p^2
0 + O(x, y)^20
sage: nth_root(p^-10,2) - p^-5
0 + O(x, y)^20
sage: nth_root(p^-10,5) - p^-2
0 + O(x, y)^20
```



---

Comment by niles created at 2011-02-08 14:18:41

Hello all,

Here is a more refined attempt to distribute the review of this patch.  If you can give any one of the following items positive review, please do so!

thanks,
Niles

 * Sage passes all doctests with this patch (buildbot gives this positive review)
 * All code is documented and doctested thoroughly; documentation builds without error or warning
 * The underlying concept of the implementation (a wrapper for certain univariate power series over multivariate polynomials) is sound
 * multi_power_series_ring.py: the code accurately does what it claims to do
 * multi_power_series_ring_element.py: the code accurately does what it claims to do
 * Integration with the rest of sage: construction and use of PowerSeriesRings works correctly, and parallels behavior of polynomial rings
 * Performance:  the multivariate power series arithmetic is fast enough to be included in Sage
 * Coding:  the code is free from obvious inefficiencies in error handling, memory management, etc.
 * The items on this list constitute a complete review

For the buildbot:

Apply trac_1956_multi_power_series_new_4.patch, trac_1956_uni_multi_ps_2.patch, trac_1956_multi_ps_cleanup.patch


---

Comment by pernici created at 2011-02-10 12:26:30

Niles,
going back to the benchmarks you posted in ticket #1956 (see also bench1.sage
posted here), here is a comparison with PARI


```
(2)  latest patch in this ticket
(3)  PARI/GP
times in ms
test no.  1     2     3     4     5     6     7      8
(2)       28.2  2.3   24.8  166   8.16  21    45.2   56.7
(3)       27.8  20    19.7  94.4  16    43.2  47.2   48
```

PARI ranges from 8.7x slower to 1.8x faster; it is slowest in the
second example; the timings for (3) fluctuate a lot, unlike those of (2);
above I gave the first timings I got.

I took a few times the timings for (3) in the second example

```
sage: %timeit gp('(1 + T^3*(a^3 + b^3) + T^4*(c^4 + d^4) + O(T^(15)))^-20')
25 loops, best of 3: 17.3 ms per loop
```

I got timings from 14 ms to 23 ms, while I get regularly 2.3 ms for (2)

```
sage: L.<a,b,c,d> = PowerSeriesRing(QQ,4)
sage: %timeit (1 + a^3 + b^3 + c^4 + d^4 + L.O(15))^-20
125 loops, best of 3: 2.3 ms per loop
```

even taking the best time for PARI in this example, it is still 6x slower.

I decided to make comparison with PARI/GP prompted by your post in ticket
#1956 about distributing the review of that ticket.

I thought that another item there could be:

comparison with other CAS

and so I tried the comparison with PARI.

IMHO this ticket could be closed: I consider settled that generic truncated
multiplication is faster than Karatsuba for multivariate series.
The comparison with PARI is fairly favorable; the latest patch is
from 6x faster to 2.5x slower than PARI/GP in the given benchmarks with
the QQ field, and it is generic code, working with any ring.

These benchmarks should help reviewers in settling the item:

Performance: the multivariate power series arithmetic is fast enough to be included in Sage


---

Comment by niles created at 2011-02-10 14:30:51

Replying to [comment:86 pernici]:

> I thought that another item there could be:
> 
> comparison with other CAS
> 
> and so I tried the comparison with PARI.

Thanks for doing this.  A comparison with Magma also appears in [comment 8 above](http://trac.sagemath.org/sage_trac/ticket/1956?replyto=86#comment:8).

> 
> IMHO this ticket could be closed: I consider settled that generic truncated
> multiplication is faster than Karatsuba for multivariate series.
> The comparison with PARI is fairly favorable; the latest patch is
> from 6x faster to 2.5x slower than PARI/GP in the given benchmarks with
> the QQ field, and it is generic code, working with any ring.

Thanks!  Really we're just waiting for someone (other than me) to click "positive review" -- this will initiate the process of merging it in the next version of Sage.

> 
> These benchmarks should help reviewers in settling the item:
> 
> Performance: the multivariate power series arithmetic is fast enough to be included in Sage

It sounds like you're willing to give that item a positive review.  Are you also willing to say that "The underlying concept is sound"?  If there are any other items you can say should have positive review, please do :)


---

Comment by pernici created at 2011-02-14 15:46:58

niles wrote:
> It sounds like you're willing to give that item a positive review. Are you also willing to say that "The underlying concept is sound"?

I think it is sound to use a background univariate series
to implement total degree precision.

Concerning the 6th item (integration with the rest of sage)
we should discuss what other approaches are available in Sage to deal with
multivariate series.

Another approach to multivariate series is using series of series;
this can be done with Sage's univariate power series or `gp`.

It is a bit cumbersome to convert a polynomial into a series of series with
Sage's univariate power series


```
sage: R.<x1> = QQ[[]]
sage: S.<x0> = R[[]]
sage: p = (1 + x0 + x1)^3
sage: a = p.list()
sage: q = sum((a[i] + O(x1^3))*x0^i for i in range(len(a))) + O(x0^3)
sage: q^-5
1 - 15*x1 + 120*x1^2 + O(x1^3) + (-15 + 240*x1 - 2040*x1^2 + O(x1^3))*x0 + (120 - 2040*x1 + 18360*x1^2 + O(x1^3))*x0^2 + O(x0^3)
sage: (q-1)^2
9*x1^2 + 18*x1^3 + O(x1^4) + (18*x1 + 54*x1^2 + O(x1^3))*x0 + (9 + 54*x1 + 90*x1^2 + O(x1^3))*x0^2 + O(x0^3)
```


Using `gp` the notation is simpler

```
sage: q = gp('(1+x0+x1)^3 + O(x0^3) + O(x1^3)')
```

giving the same output for `q^-5` and `(q-1)^2` .

For long computations `gp` is much faster, especially with more than two variables.

Should one integrate the multi-series multivariate series approach
with `PowerSeriesRing` ? It could be something like

```
sage: R = PowerSeriesRing(QQ, 2, 'x', "ms")
sage: q = (1 + x0 + x1)^3 + O(x0^3,x1^3)
sage: q
1 + 3*x1 + 3*x1^2 + O(x1^3) + (3 + 6*x1 + 3*x1^2 + O(x1^3))*x0 + (3 + 3*x1 + O(x1^3))*x0^2 + O(x0^3)
```


One could implement series of series with Sage's univariate power series,
or better using PARI.

Clearly implementing this does not belong to this ticket.
The only thing to be decided in this ticket is if it is OK to keep the
total degree precision as the default option in `PowerSeriesRing`.


---

Comment by pernici created at 2011-02-15 17:19:44

In ticket #10532 the patch trac_10532_send_to_bg.patch fixes the bug in _send_to_bg
in the case of multivariate series with one variable, see comments 64-70 in this ticket.


---

Comment by niles created at 2011-02-15 18:03:33

Replying to [comment:88 pernici]:
> niles wrote:
> > It sounds like you're willing to give that item a positive review. Are you also willing to say that "The underlying concept is sound"?
> 
> I think it is sound to use a background univariate series
> to implement total degree precision.

Thanks :)

> 
> Concerning the 6th item (integration with the rest of sage)
> we should discuss what other approaches are available in Sage to deal with
> multivariate series.
> 
> Another approach to multivariate series is using series of series;
> this can be done with Sage's univariate power series or `gp`.
> ...
> The only thing to be decided in this ticket is if it is OK to keep the
> total degree precision as the default option in `PowerSeriesRing`.
> 

With regard to "series of series", I believe there are some theoretical subtleties which make this tricky.  The [Pari User's Manual](http://pari.math.u-bordeaux.fr/pub/pari/manuals/2.3.3/users.pdf) contains the following warning (1.2.4, page 22):

>> In the present version 2.3.3 of PARI, there are bugs in the handling of power series of power series, i.e. power series in several variables. ... This bug is difficult to correct because the mathematical problem itself contains some amount of imprecision, and it is not easy to design an intuitive generic interface for such beasts.

So I think total-degree precision should be the the default, until someone writes code to carefully handle the other possibilities (or to call `gp` -- see the next point).

> For long computations gp is much faster, especially with more than two variables. 

Yes, a more complete interface with `gp` is probably the right way to go.  However I think `PowerSeriesRing`, and its elements, should be native Sage objects -- this is not the case with `gp` series, which makes them unsuitable for the default power series.  For example:


```
sage: q = gp('(1+x0+x1)^3 + O(x0^3) + O(x1^3)')
sage: type(q)
<class 'sage.interfaces.gp.GpElement'>
sage: q.parent()
PARI/GP interpreter
sage: q.base_ring()
PARI/GP interpreter
```



---

Comment by pernici created at 2011-02-15 23:13:27

niles wrote:
> So I think total-degree precision should be the the default, until someone writes code to carefully handle the other possibilities (or to call gp -- see the next point).

Maybe total-degree precision is a better default anyway, even if there were available an excellent multi-series (I mean series of series ... N times, I do not know the standard name for these _really_ multivariate series) implementation; I have the impression that few times multi-series are used, and that univariate series (which total-degree precision multivariate series really is) or at most bivariate series are used frequently in practice.

> Yes, a more complete interface with gp is probably the right way to go. However I think PowerSeriesRing?, and its elements, should be native Sage objects -- this is not the case with gp series, which makes them unsuitable for the default power series.

Right.


---

Comment by pernici created at 2011-02-24 15:54:13

Replying to [comment:87 niles]:
> Replying to [comment:86 pernici]:
> 
> > I thought that another item there could be:
> > 
> > comparison with other CAS
> > 
> > and so I tried the comparison with PARI.
> 
> Thanks for doing this.  A comparison with Magma also appears in [comment 8 above](http://trac.sagemath.org/sage_trac/ticket/1956?replyto=86#comment:8).

I do not have Magma; according to the timings in comment 8 it seems that in the first
benchmark Magma is 3 orders of magnitude slower.

I found this [http://wiki.sagemath.org/sagebeatsmagma](http://wiki.sagemath.org/sagebeatsmagma) ; such a benchmark could be added there.


---

Comment by niles created at 2011-03-17 20:21:27

updated for sage 4.6.2


---

Attachment

More code rot; patches should all apply to 4.6.2 now.


For the buildbot: 

Apply 
trac_1956_multi_power_series_new_4.patch,
trac_1956_uni_multi_ps_3.patch,
trac_1956_multi_ps_cleanup.patch


---

Comment by niles created at 2011-03-17 20:28:02

correction to buildbot:

Apply trac_1956_multi_power_series_new_4.patch, trac_1956_uni_multi_ps_3.patch, trac_1956_multi_ps_cleanup.patch


---

Attachment

pickling fixed, minor docstring formatting fixed


---

Comment by niles created at 2011-03-18 14:00:27

updated [attachment:trac_1956_multi_power_series_new_4.patch] to include `#random` flag in doctests of `.random_element()` (lines 291 and 294 of this patch).  Although I've tried to avoid `#random` throughout, it's necessary here unless I explicitly set the random seed before the tests.  However, even then, the result of the test may change from one version of Sage to the next (as it has now).

Buildbot:

Apply trac_1956_multi_power_series_new_4.patch, trac_1956_uni_multi_ps_3.patch, trac_1956_multi_ps_cleanup.patch


---

Comment by hlaw created at 2011-03-22 18:26:25

First, thanks for all your work Niles, what you've done has already saved me hours of pain!

There seems to be a problem with how coercion/evaluation works between two multivariate power series rings when the number of variables in each differs.  For example:


```
sage: A.<a, b, c> = PowerSeriesRing(QQ)
sage: B.<s, t> = PowerSeriesRing(QQ)
sage: s(a, b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/hlaw/Dropbox/org/<ipython console> in <module>()

/home/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/multi_power_series_ring_element.pyc in __call__(self, *x, **kwds)
    419         for i in range(len(x)):
    420             try:
--> 421                  xi = self.parent(x[i])
    422             except AttributeError:
    423                 raise AttributeError(str(x[i])+" does not coerce to parent ring.")

/home/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.parent (sage/structure/element.c:4069)()

/home/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/power_series_ring.pyc in __call__(self, f, prec, check)
    604             v = sage_eval(f.Eltseq())
    605             return self(v) * (self.gen(0)**f.Valuation())
--> 606         return self.__power_series_class(self, f, prec, check=check)
    607         
    608     def construction(self):

/home/hlaw/src/sage-src/local/lib/python2.6/site-packages/sage/rings/multi_power_series_ring_element.pyc in __init__(self, parent, x, prec, is_gen, check)
    352                     self._bg_value = parent._bg_ps_ring(x._bg_value)
    353                 except TypeError:
--> 354                     raise TypeError("Unable to coerce into background ring.")
    355                 
    356             elif xparent == parent._bg_ps_ring():

TypeError: Unable to coerce into background ring.
```

I would expect this to print `a`.  Similar permutations with `s^2`, `s + t`, etc. produce the same result.

Another problem, possibly related, is the following:


```
sage: B.<s, t> = PowerSeriesRing(QQ)
sage: C.<z> = PowerSeriesRing(QQ)
sage: s(z, z)  # expect z
1
sage: s(z, z^2)  # expect z
1
sage: s(0, z^2)  # expect 0
0
sage: s(z^2, 0)  # expect z^2
1
sage: (2*s^2)(z, z)  # expect 2*z^2
2
sage: (2*s^2 + 3*t)(z, z)  # expect 3*z + 2*z^2
5
sage: t(0, z)  # expect z
1
sage: t(z, z)  # expect z
1
sage: z(s + t) # expect s + t
s + t
sage: z(s)  # expect s
s
sage: z(t)  # expect t
t
```

Clearly `z` is being sent to 1 (one) somehow when going from `QQ[This is the Trac macro *s,t* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#s,t-macro)` to `QQ[This is the Trac macro *z* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#z-macro)`, but the maps in the other direction work fine.

Both of these problems (assuming they're distinct) disappear when one does the analogous calculations directly with multivariate _polynomial_ rings.

Cheers, Hamish.

(Using Sage 4.6.2 +power series patches, on Ubuntu 10.10 64bit, Macbook 5.1.)


---

Comment by niles created at 2011-03-22 20:21:47

Replying to [comment:96 hlaw]:
> First, thanks for all your work Niles, what you've done has already saved me hours of pain!
> 

Thanks -- glad to hear it!  It has cost me many hours, so I hope the review will be finished soon (after I fix this problem :)

> There seems to be a problem with how coercion/evaluation works between two multivariate power series rings when the number of variables in each differs. 

Actually it never occurred to me that people would want to substitute into a power series from one ring elements from a different ring, or that such behavior should be supported, but I can see now why it might be useful.  The problem is occurring in the `__call__` method of `MPowerSeries`, which assumes that the inputs should coerce to the parent of the power series they're being substituted into.  A separate part of the problem is that elements from one power series ring are incorrectly coercing to 1 in the other power series ring:


```
sage: B.<s, t> = PowerSeriesRing(QQ)
sage: C.<z> = PowerSeriesRing(QQ)
sage: B(z)
1
sage: C(s)
---------------------------------------------------------------------------
...
TypeError: Unable to coerce s (<class 'sage.rings.multi_power_series_ring_element.MPowerSeries'>) to Rational
```


So I will have to figure out what is going wrong here.  In the meantime, if you need to actually use this, you can use `._value()` to recover the underlying multivariate polynomial, do the substitution there, and then `.add_bigoh()` to get a power series again.  The important idea is that the precision of the power series after substitution should be `n*v`, where `n` is the precision of the original power series, and `v` is the minimum of the valuations of the input power series.

Something smarter might be done by mimicking the `__call__` method of `MPolynomial_element`, but I haven't thought through that yet -- let me know if you do :)


---

Comment by niles created at 2011-03-22 20:21:47

Changing status from needs_review to needs_work.


---

Comment by niles created at 2011-03-27 01:20:00

Replying to [comment:97 niles]:
> Replying to [comment:96 hlaw]:

> > There seems to be a problem with how coercion/evaluation works between two multivariate power series rings when the number of variables in each differs. 

I tracked down this bug -- it was unique to the case where one of the power series rings is univariate, and comes from the fact that (univariate) power series rings automatically convert any univariate power series from a given variable to another:


```
sage: R.<a> = PowerSeriesRing(ZZ)sage: S.<b> = PowerSeriesRing(ZZ)
sage: b in R
False
sage: R.has_coerce_map_from(S)
False
sage: R(b)
a
```


I was thinking this should be filed as a separate bug, but polynomials have the same behavior, so perhaps it is intentional.  In any case, I've fixed multivariate power series to take this into account, so an error is raised when the variables don't match:


```
sage: B.<s, t> = PowerSeriesRing(QQ)
sage: C.<z> = PowerSeriesRing(QQ)
sage: B(z)
...
TypeError: Cannot coerce input to polynomial ring.
```


> > Another problem, possibly related, is the following...

I also implemented a `._subs_formal` method, which is called automatically by `.__call__`.  This method substitutes *anything* into the power series, requiring only that multiplication and exponentiation be defined for the inputs.  This gives all of the "expected" results from above.  Some further examples (from the new doctests):

```
sage: B.<s, t> = PowerSeriesRing(QQ)
sage: C.<z> = PowerSeriesRing(QQ)
sage: s(z,z)
z

sage: f = -2/33*s*t^2 - 1/5*t^5 - s^5*t + s^2*t^4
sage: f(z,z)
-2/33*z^3 - 1/5*z^5
sage: f(z,1)
-1/5 - 2/33*z + z^2 - z^5
sage: RF = RealField(10)
sage: f(z,RF(1))
-0.20 - 0.061*z + 1.0*z^2 - 0.00*z^3 - 0.00*z^4 - 1.0*z^5

sage: m = matrix(QQ,[[1,0,1],[0,2,1],[-1,0,0]])
sage: m
[ 1  0  1]
[ 0  2  1]
[-1  0  0]
sage: f(m,m)
[     2/33         0       1/5]
[   131/55 -1136/165    -24/11]
[     -1/5         0   -23/165]
sage: f(m,m) == -2/33*m^3 - 1/5*m^5
True

sage: f = f.add_bigoh(10)
sage: f(z,z)
-2/33*z^3 - 1/5*z^5 + O(z^10)
sage: f(m,m) # cannot substitute arbitrary elements when f has finite precision
Traceback (most recent call last):
...
AttributeError: 'sage.matrix.matrix_rational_dense.Matrix_rational_dense' object has no attribute 'add_bigoh'
```


Please test it out and let me know how it goes!
-Niles


---

Comment by niles created at 2011-03-27 01:23:30

attached the patch which implements the changes described above; now updating "Apply" instructions

Buildbot:

Apply trac_1956_multi_power_series_new_4.patch, trac_1956_uni_multi_ps_3.patch, trac_1956_multi_ps_cleanup.patch, trac_1956_multi_ps_coercion.patch


---

Comment by niles created at 2011-03-27 01:29:30

improved coercion and substitution; also fixed minor typo


---

Attachment

improved coercion and substitution; also fixed minor typos


---

Attachment

apologies for the many rapid updates -- fixing some stupid typos and trying to get the buildbot to apply the right patches.

Apply trac_1956_multi_power_series_new_4.patch, trac_1956_uni_multi_ps_3.patch, trac_1956_multi_ps_cleanup.patch, trac_1956_multi_ps_coercion.patch


---

Comment by hlaw created at 2011-03-27 11:50:13

Replying to [comment:98 niles]:

> Please test it out and let me know how it goes! -Niles

Works great!  The quick turnaround is appreciated!

Cheers, Hamish.


---

Comment by niles created at 2011-03-29 00:58:51

Replying to [comment:101 hlaw]:
> 
> Works great!  The quick turnaround is appreciated!
> 

Glad to hear it!  If you feel capable of reviewing some part of the patch, that would be *greatly* appreciated.  Here is the current status of the various items:

1. Sage passes all doctests with this patch
(positive review; buildbot)

2. All code is documented and doctested thoroughly; documentation builds without error or warning
(needs review)

3. The underlying concept of the implementation (a wrapper for certain univariate power series over multivariate polynomials) is sound
(positive review; Mario Pernici)

4. multi_power_series_ring.py: the code accurately does what it claims to do
(needs review)

5. multi_power_series_ring_element.py: the code accurately does what it claims to do
(needs review)

6. Integration with the rest of sage: construction and use of `PowerSeriesRings` works correctly, and parallels behavior of polynomial rings
(needs review)

7. Performance: the multivariate power series arithmetic is fast enough to be included in Sage
(positive review; Mario Pernici)

8. Coding: the code is free from obvious inefficiencies in error handling, memory management, etc.
(needs review)

9. The items on this list constitute a complete review 
(needs review)


---

Comment by niles created at 2011-03-29 00:58:51

Changing status from needs_work to needs_review.


---

Attachment

all patches at once


---

Comment by niles created at 2011-04-15 01:05:37

I've combined all of the partial patches into a single patch.  There are still a number of items needing review.  

If you've suggested improvements to this patch in the past, please verify that the issues have been resolved, and mark "positive review" for anything you can!

Much thanks,
Niles

Buildbot: Apply trac_1956_combined.patch


---

Comment by niles created at 2011-04-26 12:09:41

Replying to [comment:79 pernici]:
> The attached patch [attachment:mo1.patch] is a hack to satisfy this property
> 
  {{{
  sage: R.<x,y> = QQ[[]]
  sage: 1 + x + y^2 + O(x, y)^5
  1 + x + y^2 + O(x, y)^5
  }}}

I've created a separate ticket for this now, at #11256, so that it can be reviewed independently of this already extensive patch.


---

Comment by malb created at 2011-04-30 19:02:14

Changing status from needs_review to needs_work.


---

Comment by malb created at 2011-04-30 19:02:14

> 1. Sage passes all doctests with this patch (positive review; buildbot)

I think the buildbot gets confused by the "Apply" instruction in the ticket's description. Hence, it didn't run the big patch yet.

> 2. All code is documented and doctested thoroughly; documentation builds without 
> error or warning (needs review)

*needs work*


```
sage -coverage devel/sage/sage/rings/multi_power_series_ring.py 
----------------------------------------------------------------------
devel/sage/sage/rings/multi_power_series_ring.py
SCORE devel/sage/sage/rings/multi_power_series_ring.py: 96% (30 of 31)

Missing documentation:
         * unpickle_multi_power_series_ring_v0(base_ring, num_gens, names, order, default_prec, sparse):
```


These just need `#indirect doctest` added:


```
sage -coverage devel/sage/sage/rings/multi_power_series_ring_element.py 
----------------------------------------------------------------------
devel/sage/sage/rings/multi_power_series_ring_element.py
SCORE devel/sage/sage/rings/multi_power_series_ring_element.py: 100% (52 of 52)

Possibly wrong (function name doesn't occur in doctests):
         * _subs_formal(self,*x,**kwds):
         * _add_(left, right):
         * _sub_(left, right):
         * _mul_(left, right):
         * _lmul_(self, c):
         * _div_(self, denom_r):

----------------------------------------------------------------------
```


But the docs build without warnings etc.

> 3. The underlying concept of the implementation (a wrapper for certain univariate 
> power series over multivariate polynomials) is sound (positive review; Mario 
> Pernici)

> 4. multi_power_series_ring.py: the code accurately does what it claims to do (needs_review)

Shouldn't `def _element_constructor_(self,f)` use the default precision of the ring?

> 5. multi_power_series_ring_element.py: the code accurately does what it claims to 
> do (needs review)

> 6. Integration with the rest of sage: construction and use of PowerSeriesRings 
> works correctly, and parallels behavior of polynomial rings (needs review)

*needs work*

The `default_prec` parameter does not seem to work as expected (or is my expectation wrong?)


```python
sage: P.<x,y> = PowerSeriesRing(GF(127),default_prec=20)
sage: x.prec()
+Infinity
```


> 7. Performance: the multivariate power series arithmetic is fast enough to be 
> included in Sage (positive review; Mario Pernici)

> 8. Coding: the code is free from obvious inefficiencies in error handling, memory 
> management, etc. (needs review)

If the performance is good (7), then I think we can just assume it's okay. We can always come back and fix stuff later which is too slow.

I have to say that I don't like the excessive use of double underscore attributes. It makes it harder to inherit from it or reach into the internals (just as you have to write `_PowerSeriesRing_generic__poly_ring`) I'd just use a single underscore. I'll leave it up to you (i.e., not make my review dependent on it) whether you insist on keeping them.

> 9. The items on this list constitute a complete review (needs review)

Fine by me.


---

Attachment


---

Comment by niles created at 2011-05-01 23:48:19

Replying to [comment:106 niles]:

Patchbot: Apply trac_1956_combined_2.patch


---

Comment by niles created at 2011-05-02 00:35:31

Replying to [comment:105 malb]:

Thanks for taking a look; sorry for the coverage negligence.  I've added the `#indirect notes`, and a docstring for `unpickle`.  Now `sage -coverage` returns 100% for both `multi_power_series` files.  As a bonus, I've added a docstring for the unpickle function of univariate power series too.

I believe your other comments do not require changes -- I've elaborated below.  This means we are once again ready for review :)

> 
> > 4. multi_power_series_ring.py: the code accurately does what it claims to do (needs_review)
> 
> Shouldn't ```def _element_constructor_(self,f)``` use the default precision of the ring?
> 

No, I believe not.  Default precision is used only when absolutely necessary to convert an infinite precision element to a finite precision one (e.g. for inversion or reversion).  But, for example, coercion of a polynomial should result in an infinite precision element, not a finite precision one.  This is consistent with the behavior of univariate power series rings:


```
sage: P = QQ[x]; P
Univariate Polynomial Ring in x over Rational Field

sage: S = P.completion(P.gen()); S
Power Series Ring in x over Rational Field

sage: S(P.random_element()).prec()
+Infinity
```


```
sage: P = QQ['x,y,z']; P
Multivariate Polynomial Ring in x, y, z over Rational Field

sage: S = P.completion(P.gens()); S
Multivariate Power Series Ring in x, y, z over Rational Field

sage: S(P.random_element()).prec()
+Infinity
```



> > 6. Integration with the rest of sage: construction and use of `PowerSeriesRing` 
> > works correctly, and parallels behavior of polynomial rings (needs review)
> 
> *needs work*
> 
> The `default_prec` parameter does not seem to work as expected (or is my expectation wrong?)
> 
> 

```python
sage: P.<x,y> = PowerSeriesRing(GF(127),default_prec=20)
sage: x.prec()
+Infinity
```



I believe that your expectation is wrong, as described above.  Note the parallel behavior for univariate power series rings:

```
sage: P.<x> = PowerSeriesRing(GF(127),default_prec=20)
sage: x.prec()
+Infinity
```



> > 8. Coding: the code is free from obvious inefficiencies in error handling, memory 
> > management, etc. (needs review)
> 
> If the performance is good (7), then I think we can just assume it's okay. We can always come back and fix stuff later which is too slow.

so...I'm reading 'positive review', right? ;)
(free from *obvious* inefficiencies, etc.)


> 
> I have to say that I don't like the excessive use of double underscore attributes. It makes it harder to inherit from it or reach into the internals (just as you have to write `_PowerSeriesRing_generic__poly_ring`) I'd just use a single underscore. I'll leave it up to you (i.e., not make my review dependent on it) whether you insist on keeping them.

Excessive or not, each of the double underscore methods is necessary to replace the corresponding method of `PowerSeries` or `PowerSeriesRing_generic`, from which the `MPowerSeries*` classes inherit.  Here's a complete list of the double underscore attributes:


```
MPowerSeries.__init__
MPowerSeries.__reduce__
MPowerSeries.__call__
MPowerSeries.__getitem__
MPowerSeries.__invert__
MPowerSeries.__cmp__
MPowerSeries.__mod__
MPowerSeries.__lshift__
MPowerSeries.__rshift__

MPowerSeriesRing_generic.__init__
MPowerSeriesRing_generic.__reduce__
MPowerSeriesRing_generic.__cmp__
```



---

Comment by niles created at 2011-05-02 00:35:31

Changing status from needs_work to needs_review.


---

Comment by niles created at 2011-05-02 00:42:44

Replying to [comment:108 niles]:
>  Here's a complete list of the double underscore attributes...

To clarify:  that's a complete list of such attributes defined in the code I've written.  You will see many more (50 or 60) if you use tab-completion to see what double underscore methods a multivariate power series or multivariate power series ring has.  I have not added any new ones (from the univariate case), simply redefined some.


---

Comment by niles created at 2011-05-02 00:50:23

diff between `trac_1956_combined.patch` and `trac_1956_combined_2.patch`


---

Attachment

This seems to be the current status:

1. Sage passes all doctests with this patch

waiting for patchbot :)

2. All code is documented and doctested thoroughly; documentation builds without error or warning

*positive review*

3. The underlying concept of the implementation (a wrapper for certain univariate power series over multivariate polynomials) is sound

*positive review*

4. multi_power_series_ring.py: the code accurately does what it claims to do

*positive review*

5. multi_power_series_ring_element.py: the code accurately does what it claims to do

*needs review*

6. Integration with the rest of sage: construction and use of PowerSeriesRings works correctly, and parallels behavior of polynomial rings

*positive review*

7. Performance: the multivariate power series arithmetic is fast enough to be included in Sage

*positive review*

8. Coding: the code is free from obvious inefficiencies in error handling, memory management, etc.

*positive review*

9. The items on this list constitute a complete review

*positive review*


----

Thanks for explaining the default precision business to me! As I said, I rarely touch power series.

----
> Excessive or not, each of the double underscore methods is necessary to replace the corresponding method of `PowerSeries` or `PowerSeriesRing_generic`, from which the `MPowerSeries*` classes inherit.  Here's a complete list of the double underscore attributes:

Sorry, I didn't mean stuff like `__init__` which of course has to be like it is. I meant stuff like `__poly_ring` which could easily be `_poly_ring`.


---

Comment by niles created at 2011-05-02 11:57:47

Replying to [comment:110 malb]:
> This seems to be the current status:
>
> `...`

Great!  Thanks :)

----

> 
> Thanks for explaining the default precision business to me! As I said, I rarely touch power series.
> 

Glad my explanation made sense :)


----
> > Excessive or not, each of the double underscore methods is necessary ...
> Sorry, I didn't mean stuff like `__init__` which of course has to be like it is. I meant stuff like `__poly_ring` which could easily be `_poly_ring`.
> 

Ah, I agree.  This came up once before (perhaps with you, or with Simon), and indeed I've eliminated the unnecessary double underscore attributes.  Those listed above are the only ones remaining.


---

Comment by malb created at 2011-05-02 19:51:29

looking at [attachment:trac_1956_combined_2.patch] I see `__ngens`, `__term_order` and `__poly_ring`, did you forget to upload the patch where you replaced those by `_ngens`, `_term_order` and `_poly_ring`. Or are we talking about different things?


---

Comment by malb created at 2011-05-02 19:57:30

Shouldn't this be a value error instead of a type error? Since it's a wrong value and not type?


```python
 if len(x) != self.parent().ngens(): 
  raise TypeError("Number of arguments does not match number of variables in parent.") 
```


Other than that, I think the code in `multi_power_series_ring_element.py` looks fine.


---

Comment by niles created at 2011-05-02 20:11:41

Replying to [comment:112 malb]:
> looking at [attachment:trac_1956_combined_2.patch] I see `__ngens`, `__term_order` and `__poly_ring`, did you forget to upload the patch where you replaced those by `_ngens`, `_term_order` and `_poly_ring`. Or are we talking about different things?

Ack!  No, but I was looking for double underscore attributes defined by ``def __*``, totally forgetting about these others which are not methods.  I'll upload a new version tomorrow.


---

Comment by niles created at 2011-05-02 20:11:41

Changing status from needs_review to needs_work.


---

Comment by niles created at 2011-05-02 20:14:11

...*sigh*... I wish I could update my previous comment to fix the syntax:

Replying to [comment:114 niles]:
> Replying to [comment:112 malb]:
> > looking at [attachment:trac_1956_combined_2.patch] I see `__ngens`, `__term_order` and `__poly_ring`, did you forget to upload the patch where you replaced those by `_ngens`, `_term_order` and `_poly_ring`. Or are we talking about different things?
> 

I was looking for double underscore attributes defined by "`def __*`", totally forgetting about these others which are not methods.  I'll upload a new version tomorrow.


---

Comment by malb created at 2011-05-02 20:18:53

I'll make an honest attempt to look at it tomorrow even (GMT). So if by the day after tomorrow you haven't got a review, feel free to bug me about it!


---

Comment by niles created at 2011-05-03 02:05:48

Now that I've looked carefully at these, and read documents like [PEP 8 style guide](http://www.python.org/dev/peps/pep-0008/) about double underscore attributes, I think I'm inclined to leave them as is.  There are three contributing reasons: consistency with multivariate polynomial rings, consistency with univariate power series rings, and not wanting the background power series ring to be treated casually.

Here is the list of the double underscore attributes of `MPowerSeriesRing_generic` :

* Those which parallel multivariate polynomials:
  {{{
__term_order
__ngens
}}}

* Those which parallel univariate power series:
  {{{
__poly_ring
__is_sparse
__params
}}}

* Others, which I'd rather leave double-underscore for consistency with the rest and because I don't think the background ring should be treated casually:
  {{{
__bg_power_series_ring
__bg_indeterminate
__base_ring
}}}


---

Attachment


---

Comment by niles created at 2011-05-03 02:18:05

Now I've added `combined_3.patch`:  It changes `TypeError` to `ValueError` as suggested above, and also in one other place (where again input of wrong length raises the error).  The error types in the rest of the code seem good to me.

I've also changed the name of the indeterminate in the background power series ring from `'T'` to `'Tbg'`.  It's conceivable that bugs could arise if a user happens to work with a multivariate power series ring, and also with a univariate power series ring having the same indeterminate name as that of the background ring of the multivariate ring.  

Since I don't know exactly how these might come up, if ever, I'd like to let this be sufficient for now, and add a more robust system of protections against possible bugs in a separate ticket.


---

Comment by niles created at 2011-05-03 02:18:05

Changing status from needs_work to needs_review.


---

Comment by niles created at 2011-05-03 02:18:52

Patchbot:  apply trac_1956_combined_3.patch


---

Comment by SimonKing created at 2011-05-03 05:49:44

Replying to [comment:117 niles]:
> * Others, which I'd rather leave double-underscore for consistency with the rest and because I don't think the background ring should be treated casually:
>   {{{
> __bg_power_series_ring
> __bg_indeterminate
> __base_ring
> }}}

Why is there a `__base_ring` at all? The base ring is usually taken care of by inheritance of `sage.structure.parent.Parent` or other base classes. So, it should certainly be possible to work without a new attribute -- it seems to be a duplicate.


---

Comment by malb created at 2011-05-03 07:25:13

Hi, Simon good catch about the `__base_ring` attribute. 

`@`Niles: as you realised in your code (in `__init__` of the ring), having double underscore attributes makes it hard to inherit because double underscore names are prefixed by the class name. If you want subclasses to use these attributes then you'll need to switch to a single underscore. The single underscore expresses that the attribute is meant to be private, i.e., not treated casually. 

With double underscores there is no such thing as consistency, the point of them is to break consistency to *prevent* people from using them, if they are not in exactly the right class of the hierarchy. The design is broken if you have to set `__poly_ring` yourself twice to make it work for the various classes in the inheritance hierarchy.

I agree that other rings do it wrong, too. But there's no need to repeat this wrong approach in a new class?


---

Comment by SimonKing created at 2011-05-03 07:34:36

Replying to [comment:121 malb]:
> `@`Niles: as you realised in your code (in `__init__` of the ring), having double underscore attributes makes it hard to inherit because double underscore names are prefixed by the class name.

To be precise: Double underscore names are only problematic if they _start_ with two underscores but do not end with two underscores.


---

Attachment

removed unnecessary double underscore attributes from `MPowerSeries_generic`


---

Comment by niles created at 2011-05-03 12:07:38

Very well, I've been convinced -- thanks for being patient.  The double underscore attributes [#comment:117 mentioned above] have all been replaced with single underscore versions.  For `__poly_ring`, I had to use `_poly_ring_`, since there is a class method `_poly_ring` already inherited from univariate power series.

All tests pass for the `multi_power_series*` files; the rest should be fine so I'll wait for the patchbot to verify them.


---

Comment by niles created at 2011-05-03 12:10:29

Patchbot: apply trac_1956_combined_4.patch


---

Comment by malb created at 2011-05-05 10:16:08

Okay, let's push the button: positive review.


---

Comment by malb created at 2011-05-05 10:16:08

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-11 13:05:18

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-05-11 13:05:18


```
sage -t  -force_lib devel/sage/sage/rings/multi_power_series_ring.py
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha1/devel/sage-main/sage/rings/multi_power_series_ring.py", line 456:
    sage: (c,R) = M.construction(); (c,R)
Expected:
    (CompletionFunctor,
    Multivariate Polynomial Ring in f0, f1, f2, f3 over Rational Field)
Got:
    (Completion[('f0', 'f1', 'f2', 'f3')], Multivariate Polynomial Ring in f0, f1, f2, f3 over Rational Field)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha1/devel/sage-main/sage/rings/multi_power_series_ring.py", line 459:
    sage: c
Expected:
    CompletionFunctor
Got:
    Completion[('f0', 'f1', 'f2', 'f3')]
**********************************************************************
```



---

Attachment

updated for new repr of completion functor


---

Comment by niles created at 2011-05-11 18:45:36

Changing status from needs_work to needs_review.


---

Comment by niles created at 2011-05-11 18:45:36

A new patch, updated according to the repr string of the completion functor.  No other changes.


---

Comment by niles created at 2011-05-11 18:46:20

Patchbot: apply trac_1956_combined_5.patch


---

Comment by jdemeyer created at 2011-05-12 12:56:34

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-05-12 12:56:34

Please rebase properly to sage-4.7.rc2:

```
sage -t  -force_lib devel/sage/sage/rings/multi_power_series_ring_element.py
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha1/devel/sage-main/sage/rings/multi_power_series_ring_element.py", line 1299:
    sage: f.sqrt()
Expected:
    Traceback (most recent call last):
    ...
    AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular' object has no attribute 'sqrt'
Got:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_39[4]>", line 1, in <module>
        f.sqrt()###line 1299:
    sage: f.sqrt()
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.1.alpha1/local/lib/python/site-packages/sage/rings/multi_power_series_ring_element.py", line 1304, in sqrt
        return self.parent(self._bg_value.sqrt())
      File "power_series_ring_element.pyx", line 1205, in sage.rings.power_series_ring_element.PowerSeries.sqrt (sage/rings/power_series_ring_element.c:8919)
        s = u[0].sqrt(extend=False)
      File "element.pyx", line 2003, in sage.structure.element.CommutativeRingElement.sqrt (sage/structure/element.c:14899)
      File "element.pyx", line 1906, in sage.structure.element.CommutativeRingElement.is_square (sage/structure/element.c:14740)
    NotImplementedError: is_square() not implemented for elements of Multivariate Polynomial Ring in a, b over Integer Ring
**********************************************************************
```



---

Comment by niles created at 2011-05-12 14:11:58

Replying to [comment:130 jdemeyer]:
> Please rebase properly to sage-4.7.rc2:
>

```
sage -t  -force_lib devel/sage/sage/rings/multi_power_series_ring_element.py
**********************************************************************
```


I've addressed this problem, but I see other issues with `sage/interfaces/maxima.py` that I don't understand since this patch does not touch maxima . . . are those spurious failures?


---

Attachment


---

Comment by niles created at 2011-05-12 14:59:21

Changing status from needs_work to needs_review.


---

Comment by niles created at 2011-05-12 14:59:21

Ah; problems with `interfaces/maxima.py` are independent of this patch, since they occur in my newly-installed 4.7.rc2.  Patch 6 here fixes the error raised by `sqrt` to be the same as that raised by `square_root`, thus passing the doctest as it did before.  All tests in `rings/multi_power_series*` now pass.


Patchbot:  apply trac_1956_combined_6.patch


---

Comment by niles created at 2011-05-19 19:27:10

Can we get this switched back to positive review?  Sage 4.7.rc3 fixes the problems with `interfaces/maxima.py`; this patch applies cleanly and passes all tests under that release.


---

Comment by jdemeyer created at 2011-05-24 12:48:41

Replying to [comment:133 niles]:
> Can we get this switched back to positive review?

*bump*

Any reviewers?


---

Comment by malb created at 2011-05-24 13:59:51

Changing status from needs_review to positive_review.


---

Comment by malb created at 2011-05-24 13:59:51

okay


---

Comment by jdemeyer created at 2011-06-07 08:34:52

Resolution: fixed
