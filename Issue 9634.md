# Issue 9634: binomial does not accept variable when only in the lower argument

Issue created by migration from Trac.

Original creator: Henryk.Trappmann

Original creation time: 2010-07-29 07:29:28

Assignee: AlexGhitza

CC:  kcrisman jpflori rws


```
sage: var('k')
k 
sage: binomial(x,3)
1/6*(x - 2)*(x - 1)*x
sage: binomial(3,k)
---------------------------------------------------------------------------
TypeError: Either m or x-m must be an integer 
```


From kcrisman:
Is this a bug?  I would say yes, because

```
sage: binomial(x,k)
binomial(x, k)
```

works, but maybe we want to have it be a specific integer if the top
number is given?  Any input?


---

Comment by kcrisman created at 2010-07-29 13:05:40

Changing component from basic arithmetic to symbolics.


---

Comment by kcrisman created at 2010-07-29 13:05:40

Changing assignee from AlexGhitza to burcin.


---

Comment by burcin created at 2010-10-11 15:15:13

make the top level binomial() function symbolic


---

Comment by burcin created at 2010-10-11 15:20:12

Changing status from new to needs_work.


---

Attachment

attachment:trac_9634-symbolic_binomial.patch replaces the top level `binomial()` function with the one defined in `sage.functions.other`. This version can handle symbolic input, as opposed to the previous one from `sage.rings.arith`.

This still needs work, since the files `sage/functions/other.py` and `sage/rings/arith.py` don't pass doctests yet. We need to improve the speed of numerical approximation using the `gamma` trick from `sage.rings.arith.binomial` and change `sage.symbolic.pynac.py_binomial()` to handle large integers.


---

Comment by kcrisman created at 2011-04-25 15:51:35

Replying to [comment:2 burcin]:
> attachment:trac_9634-symbolic_binomial.patch replaces the top level `binomial()` function with the one defined in `sage.functions.other`. This version can handle symbolic input, as opposed to the previous one from `sage.rings.arith`.
> 

Good catch; I was pretty sure we had rewritten that at some point, but I have trouble following the imports.

> This still needs work, since the files `sage/functions/other.py` and `sage/rings/arith.py` don't pass doctests yet. 

> We need to improve the speed of numerical approximation using the `gamma` trick from `sage.rings.arith.binomial` and change `sage.symbolic.pynac.py_binomial()` to handle large integers.
Is that part of this ticket?  Are you saying that the numerical approximation has slowed down dramatically from the `rings.arith` version?


---

Comment by was created at 2012-01-04 05:49:41

This very bug trips up many potential users.  Ping.   Let's fix it!!


---

Attachment

I uploaded a new patch that fixes doctests as well. This meant reimplementing the `_eval_()` and `_evalf_()` methods to override those defined in pynac.

Patchbot, apply only trac_9634-symbolic_binomial.take2.patch.


---

Comment by burcin created at 2013-07-01 06:23:27

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2013-07-23 09:49:29

for the bot:

apply trac_9634-symbolic_binomial.take2.patch​


---

Comment by rws created at 2014-02-14 15:21:13

Changing status from needs_review to needs_work.


---

Comment by rws created at 2014-02-14 15:21:13

The patch2 does not apply cleanly, with two hunks failing, which I fixed manually, and push it to git. However:

```
sage -t src/sage/functions/other.py  # 18 doctests failed
sage -t src/sage/combinat/partition.py  # 2 doctests failed
sage -t src/sage/rings/arith.py  # 1 doctest failed
sage -t src/sage/symbolic/expression.pyx  # 2 doctests failed
```

----
New commits:


---

Comment by rws created at 2014-02-15 09:56:49

Never mind, it's all fine, I had an incomplete installation.


---

Comment by rws created at 2014-02-15 09:56:49

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2014-02-20 15:27:38

merge conflict, please merge the latest beta into this branch.


---

Comment by git created at 2014-02-20 16:42:41

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by git created at 2014-02-20 16:42:41

Changing status from positive_review to needs_review.


---

Comment by rws created at 2014-02-20 16:45:55

Changing status from needs_review to positive_review.


---

Comment by rws created at 2014-02-20 16:45:55

OK I retested after merge, though only combinat. The number in that commit message is wrong, please ignore.


---

Comment by vbraun created at 2014-02-21 14:34:52

The branch loses the "Polynomial" global which causes a number of doctest falures

```
sage -t --long src/sage/rings/polynomial/polynomial_element.pyx
**********************************************************************
File "src/sage/rings/polynomial/polynomial_element.pyx", line 2592, in sage.rings.polynomial.polynomial_element.Polynomial.denominator
Failed example:
    isinstance(x.numerator() / x.denominator(), Polynomial)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/buildbot/sage/redhawk-1/sage_git/build/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 480, in _run
        self.execute(example, compiled, test.globs)
      File "/scratch/buildbot/sage/redhawk-1/sage_git/build/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 839, in execute
        exec compiled in globs
      File "<doctest sage.rings.polynomial.polynomial_element.Polynomial.denominator[13]>", line 1, in <module>
        isinstance(x.numerator() / x.denominator(), Polynomial)
    NameError: name 'Polynomial' is not defined
```



---

Comment by rws created at 2014-02-21 17:15:09

The funny thing is, it appears the global definition of `Polynomial` now missing is in `power_series_ring_element.pyx` which was indirectly and illogically imported in `polynomial_ring_element.pyx` before the author's patch.

Evidently he should have submitted the import cleanup separately.

Offhand, I'm not able to fix this, any takers?


---

Comment by rws created at 2014-02-21 17:15:09

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2014-02-21 17:58:47

Replying to [comment:17 rws]:
> Evidently he should have submitted the import cleanup separately.
Indeed.


---

Comment by vbraun created at 2014-02-21 20:11:49

In any case, Polynomial should just be imported into the global namespace in `src/sage/rings/polynomial/all.py`. The import cleanup is good, even though it should have been separate.


---

Comment by vbraun created at 2014-02-21 23:03:30

New commits:


---

Comment by vbraun created at 2014-02-21 23:03:30

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2014-02-22 06:45:43

Resolution: fixed


---

Comment by ppurka created at 2014-08-01 14:34:05

Please follow up in #16726
