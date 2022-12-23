# Issue 9902: is_prime should document proof flag

Issue created by migration from https://trac.sagemath.org/ticket/9903

Original creator: dmharvey

Original creation time: 2010-09-13 17:29:07

Assignee: mvngu

The documentation for `Integer.is_prime()` should document the effect of the global proof.arithmetic flag. Similarly for the global `is_prime` function.



---

Comment by mmezzarobba created at 2015-04-13 13:44:30

New commits:


---

Comment by mmezzarobba created at 2015-04-13 13:44:30

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-04-20 11:12:27

Hello,

Note that there was already an example at the end of `Integer.is_prime`:

```
sage: proof.arithmetic()
True
sage: n = 10^100 + 267
sage: timeit("n.is_prime()")  # not tested
5 loops, best of 3: 163 ms per loop
sage: proof.arithmetic(False)
sage: proof.arithmetic()
False
sage: timeit("n.is_prime()")  # not tested
1000 loops, best of 3: 573 us per loop
```

What about a similar one in `arith.is_prime`

```
sage: a = 2**2048 + 981
sage: is_prime(a)    # not tested - takes ~ 1min
sage: proof.arithmetic(False)
sage: is_prime(a)    # instantaneous!
True
sage: proof.arithmetic(True)
```


Vincent


---

Comment by vdelecroix created at 2015-04-20 11:51:43

And since we're at it, the `IMPLEMENTATION` block at the end of `Integer.is_prime` should be a `ALGORITHM` one.

Vincent


---

Comment by git created at 2015-04-22 13:08:54

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by vdelecroix created at 2015-04-22 13:11:27

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2015-04-22 13:11:27

Good!


---

Comment by vbraun created at 2015-04-23 01:47:27

Not sure if you did this intentionally, but tickets without milestone will not be merged


---

Comment by mmezzarobba created at 2015-04-23 06:53:57

Replying to [comment:6 vbraun]:
> Not sure if you did this intentionally, but tickets without milestone will not be merged

No, I just didn't notice that there was no milestone set. Thanks!


---

Comment by vbraun created at 2015-04-25 01:55:30


```
 sage -t --long src/sage/sets/set_from_iterator.py
 **********************************************************************
 File "src/sage/sets/set_from_iterator.py", line 443, in
 sage.sets.set_from_iterator.Decorator._sage_doc_
 Failed example:
     print sage_getdoc(d)   # indirect doctest
 Expected:
        Test whether "self" is prime.
     ...
        IMPLEMENTATION: Calls the PARI "isprime" function.
     <BLANKLINE>
 Got:
        Test whether "self" is prime.
     <BLANKLINE>
        INPUT:
     <BLANKLINE>
        * "proof" -- Boolean or "None" (default). If False, use a strong
          pseudo-primality test (see "is_pseudoprime()"). If True, use a
          provable primality test.  If unset, use the "default arithmetic
          proof flag".
     <BLANKLINE>
        Note: Integer primes are by definition *positive*! This is
          different than Magma, but the same as in PARI. See also the
          "is_irreducible()" method.
     <BLANKLINE>
        EXAMPLES:
     <BLANKLINE>
           sage: z = 2^31 - 1
           sage: z.is_prime()
           True
           sage: z = 2^31
           sage: z.is_prime()
           False
           sage: z = 7
           sage: z.is_prime()
           True
           sage: z = -7
           sage: z.is_prime()
           False
           sage: z.is_irreducible()
           True
     <BLANKLINE>
           sage: z = 10^80 + 129
           sage: z.is_prime(proof=False)
           True
           sage: z.is_prime(proof=True)
           True
     <BLANKLINE>
        When starting Sage the arithmetic proof flag is True. We can change
        it to False as follows:
     <BLANKLINE>
           sage: proof.arithmetic()
           True
           sage: n = 10^100 + 267
           sage: timeit("n.is_prime()")  # not tested
           5 loops, best of 3: 163 ms per loop
           sage: proof.arithmetic(False)
           sage: proof.arithmetic()
           False
           sage: timeit("n.is_prime()")  # not tested
           1000 loops, best of 3: 573 us per loop
     <BLANKLINE>
        ALGORITHM:
     <BLANKLINE>
        Calls the PARI "isprime" function.
     <BLANKLINE>
 **********************************************************************
 1 item had failures:
    1 of   6 in sage.sets.set_from_iterator.Decorator._sage_doc_
     [213 tests, 1 failure, 4.14 s]
```



---

Comment by vbraun created at 2015-04-25 01:55:30

Changing status from positive_review to needs_work.


---

Comment by git created at 2015-04-25 10:43:07

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mmezzarobba created at 2015-04-25 10:44:03

Replying to [comment:8 vbraun]:
> {{{
>  sage -t --long src/sage/sets/set_from_iterator.py
>  **********************************************************************
>  File "src/sage/sets/set_from_iterator.py", line 443, in
> }}}

Thanks, fixed.


---

Comment by mmezzarobba created at 2015-04-25 10:44:03

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2015-04-25 11:06:44

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2015-04-25 11:06:44

Could you remove the `<BLANKLINE>` in the doctest in `set_from_iterator.py` (it was there but it is not needed)?

Vincent


---

Comment by git created at 2015-04-25 12:09:27

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mmezzarobba created at 2015-04-25 12:09:55

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2015-04-25 12:28:40

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-26 02:21:43

Resolution: fixed
