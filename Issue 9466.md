# Issue 9466: square root with all=True should not return ValueError but empty list

Issue created by migration from Trac.

Original creator: mstreng

Original creation time: 2010-07-09 13:18:25

Assignee: AlexGhitza

CC:  mderickx ruckers


```
sage: FiniteField(3)(2).sqrt(all = True)
[]

sage: 2.sqrt(extend = False, all = True)
ValueError: square root of 2 not an integer

sage: FiniteField(next_prime(2^100))(2).sqrt(extend = False, all = True)
ValueError: self must be a square

sage: _.<a>=FiniteField(9)
sage: a.sqrt(extend = False, all = True)
ValueError: must be a perfect square.
```


At sage days 23 we agreed that square root with all=True should not raise an error. If no square roots exist, then it should return an empty list.

Right now, it returns an empty list for elements of small prime finite fields, but raises an error for integers, elements of large prime finite fields, and elements of non-prime finite fields.


---

Comment by ruckers created at 2012-02-08 05:08:45

Fixes the code:   sage: 2.sqrt(extend = False, all = True)


---

Attachment

Fixes the code:  sage: FiniteField(next_prime(2^100))(2).sqrt(extend = False, all = True)


---

Comment by ruckers created at 2012-02-08 05:14:12

I was not able to fix this code.

sage: _.<a>=FiniteField(9)

sage: a.sqrt(extend = False, all = True)

ValueError: must be a perfect square.


---

Comment by mstreng created at 2012-02-08 10:57:38

Thanks! That bug has been around for too long :)

Why were you not able to fix the `FiniteField(9)` case?

Unfortunately, the patches need some more work, for the following three reasons.
 * With my2.patch:
  {{{
  sage: Zmod(7)(3).sqrt(extend=True)
  sqrt3
  sage: Zmod(7)(3).sqrt(all=True, extend=True)
  []
  }}}
  The second one should either output `[sqrt3, -sqrt3]` or raise `NotImplementedError`, but never an empty list.
 * Patches must have your name and email address in them. This is done by putting your email address and name in your `.hgrc` file as specified [here](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change)
 * Add an example of the new functionality to the documentation:
   * This helps the user understand what the function does.
   * Through the doctesting framework, this prevents other people from accidentally breaking your added functionality.
   * This is [required](http://www.sagemath.org/doc/developer/trac.html#reviewing-patches) for your patch to be able to get a positive review. In fact, the manual says that you should also mention the ticket number #9466 with your example.

If you have any questions, let me know!


---

Attachment


---

Attachment


---

Comment by mstreng created at 2013-07-25 18:31:32

Changing keywords from "" to "sd23 sd51 sqrt all".


---

Attachment

Does anyone know who user "ruckers" is? (s)he should be added to the list of authors

apply 9466.patch


---

Comment by mstreng created at 2013-07-25 20:32:44

Changing status from new to needs_review.


---

Comment by mstreng created at 2013-07-25 20:32:44

please review!


---

Comment by akoutsianas created at 2013-07-26 10:04:20

Changing status from needs_review to positive_review.


---

Comment by akoutsianas created at 2013-07-26 10:04:20

The patch passed all the tests for sage 5.11 version.


---

Comment by jdemeyer created at 2013-08-20 12:57:53

Resolution: fixed
