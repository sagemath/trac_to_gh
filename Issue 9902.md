# Issue 9902: is_prime should document proof flag

archive/issues_009902.json:
```json
{
    "body": "Assignee: mvngu\n\nThe documentation for `Integer.is_prime()` should document the effect of the global proof.arithmetic flag. Similarly for the global `is_prime` function.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9903\n\n",
    "created_at": "2010-09-13T17:29:07Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.7",
    "title": "is_prime should document proof flag",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9902",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: mvngu

The documentation for `Integer.is_prime()` should document the effect of the global proof.arithmetic flag. Similarly for the global `is_prime` function.


Issue created by migration from https://trac.sagemath.org/ticket/9903





---

archive/issue_comments_098278.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-04-13T13:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98278",
    "user": "https://github.com/mezzarobba"
}
```

New commits:



---

archive/issue_comments_098279.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T13:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98279",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098280.json:
```json
{
    "body": "Hello,\n\nNote that there was already an example at the end of `Integer.is_prime`:\n\n```\nsage: proof.arithmetic()\nTrue\nsage: n = 10^100 + 267\nsage: timeit(\"n.is_prime()\")  # not tested\n5 loops, best of 3: 163 ms per loop\nsage: proof.arithmetic(False)\nsage: proof.arithmetic()\nFalse\nsage: timeit(\"n.is_prime()\")  # not tested\n1000 loops, best of 3: 573 us per loop\n```\n\nWhat about a similar one in `arith.is_prime`\n\n```\nsage: a = 2**2048 + 981\nsage: is_prime(a)    # not tested - takes ~ 1min\nsage: proof.arithmetic(False)\nsage: is_prime(a)    # instantaneous!\nTrue\nsage: proof.arithmetic(True)\n```\n\n\nVincent",
    "created_at": "2015-04-20T11:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98280",
    "user": "https://github.com/videlec"
}
```

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

archive/issue_comments_098281.json:
```json
{
    "body": "And since we're at it, the `IMPLEMENTATION` block at the end of `Integer.is_prime` should be a `ALGORITHM` one.\n\nVincent",
    "created_at": "2015-04-20T11:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98281",
    "user": "https://github.com/videlec"
}
```

And since we're at it, the `IMPLEMENTATION` block at the end of `Integer.is_prime` should be a `ALGORITHM` one.

Vincent



---

archive/issue_comments_098282.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-04-22T13:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98282",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_098283.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-22T13:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98283",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098284.json:
```json
{
    "body": "Good!",
    "created_at": "2015-04-22T13:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98284",
    "user": "https://github.com/videlec"
}
```

Good!



---

archive/issue_comments_098285.json:
```json
{
    "body": "Not sure if you did this intentionally, but tickets without milestone will not be merged",
    "created_at": "2015-04-23T01:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98285",
    "user": "https://github.com/vbraun"
}
```

Not sure if you did this intentionally, but tickets without milestone will not be merged



---

archive/issue_comments_098286.json:
```json
{
    "body": "Replying to [comment:6 vbraun]:\n> Not sure if you did this intentionally, but tickets without milestone will not be merged\n\nNo, I just didn't notice that there was no milestone set. Thanks!",
    "created_at": "2015-04-23T06:53:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98286",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:6 vbraun]:
> Not sure if you did this intentionally, but tickets without milestone will not be merged

No, I just didn't notice that there was no milestone set. Thanks!



---

archive/issue_comments_098287.json:
```json
{
    "body": "\n```\n sage -t --long src/sage/sets/set_from_iterator.py\n **********************************************************************\n File \"src/sage/sets/set_from_iterator.py\", line 443, in\n sage.sets.set_from_iterator.Decorator._sage_doc_\n Failed example:\n     print sage_getdoc(d)   # indirect doctest\n Expected:\n        Test whether \"self\" is prime.\n     ...\n        IMPLEMENTATION: Calls the PARI \"isprime\" function.\n     <BLANKLINE>\n Got:\n        Test whether \"self\" is prime.\n     <BLANKLINE>\n        INPUT:\n     <BLANKLINE>\n        * \"proof\" -- Boolean or \"None\" (default). If False, use a strong\n          pseudo-primality test (see \"is_pseudoprime()\"). If True, use a\n          provable primality test.  If unset, use the \"default arithmetic\n          proof flag\".\n     <BLANKLINE>\n        Note: Integer primes are by definition *positive*! This is\n          different than Magma, but the same as in PARI. See also the\n          \"is_irreducible()\" method.\n     <BLANKLINE>\n        EXAMPLES:\n     <BLANKLINE>\n           sage: z = 2^31 - 1\n           sage: z.is_prime()\n           True\n           sage: z = 2^31\n           sage: z.is_prime()\n           False\n           sage: z = 7\n           sage: z.is_prime()\n           True\n           sage: z = -7\n           sage: z.is_prime()\n           False\n           sage: z.is_irreducible()\n           True\n     <BLANKLINE>\n           sage: z = 10^80 + 129\n           sage: z.is_prime(proof=False)\n           True\n           sage: z.is_prime(proof=True)\n           True\n     <BLANKLINE>\n        When starting Sage the arithmetic proof flag is True. We can change\n        it to False as follows:\n     <BLANKLINE>\n           sage: proof.arithmetic()\n           True\n           sage: n = 10^100 + 267\n           sage: timeit(\"n.is_prime()\")  # not tested\n           5 loops, best of 3: 163 ms per loop\n           sage: proof.arithmetic(False)\n           sage: proof.arithmetic()\n           False\n           sage: timeit(\"n.is_prime()\")  # not tested\n           1000 loops, best of 3: 573 us per loop\n     <BLANKLINE>\n        ALGORITHM:\n     <BLANKLINE>\n        Calls the PARI \"isprime\" function.\n     <BLANKLINE>\n **********************************************************************\n 1 item had failures:\n    1 of   6 in sage.sets.set_from_iterator.Decorator._sage_doc_\n     [213 tests, 1 failure, 4.14 s]\n```\n",
    "created_at": "2015-04-25T01:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98287",
    "user": "https://github.com/vbraun"
}
```


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

archive/issue_comments_098288.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2015-04-25T01:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98288",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_098289.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-04-25T10:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98289",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_098290.json:
```json
{
    "body": "Replying to [comment:8 vbraun]:\n> {{{\n>  sage -t --long src/sage/sets/set_from_iterator.py\n>  **********************************************************************\n>  File \"src/sage/sets/set_from_iterator.py\", line 443, in\n> }}}\n\nThanks, fixed.",
    "created_at": "2015-04-25T10:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98290",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:8 vbraun]:
> {{{
>  sage -t --long src/sage/sets/set_from_iterator.py
>  **********************************************************************
>  File "src/sage/sets/set_from_iterator.py", line 443, in
> }}}

Thanks, fixed.



---

archive/issue_comments_098291.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-04-25T10:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98291",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098292.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-04-25T11:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98292",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098293.json:
```json
{
    "body": "Could you remove the `<BLANKLINE>` in the doctest in `set_from_iterator.py` (it was there but it is not needed)?\n\nVincent",
    "created_at": "2015-04-25T11:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98293",
    "user": "https://github.com/videlec"
}
```

Could you remove the `<BLANKLINE>` in the doctest in `set_from_iterator.py` (it was there but it is not needed)?

Vincent



---

archive/issue_comments_098294.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-04-25T12:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98294",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_098295.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-04-25T12:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98295",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098296.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-25T12:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98296",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_010030.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-04-26T02:21:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9902#event-10030"
}
```



---

archive/issue_comments_098297.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-26T02:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9902#issuecomment-98297",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
