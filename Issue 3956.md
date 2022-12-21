# Issue 3956: Fast hash for matrices over finite fields

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-08-26 13:24:57

Assignee: malb

In ticket #3724, `malb` suggested a very fast hash method for matrices over `GF(2)`, and he wrote that it should be doable over `GF(p)` in general.

Currently, we have:

```
sage: time N=MatrixSpace(GF(7),10000,10000).random_element()
CPU times: user 11.83 s, sys: 2.40 s, total: 14.23 s
Wall time: 14.23 s
```

This, i think, is very slow and ought to be improved as well.


```
sage: N.set_immutable()
sage: time N.__hash__()
CPU times: user 3.17 s, sys: 0.00 s, total: 3.17 s
Wall time: 3.17 s
21008582
```

... and this is quite slow, while (with the patch from #3724) the hash is immediate for matrices over GF(2).



---

Attachment

The attached patch speeds up hashing a bit. However, GF(2) speed is not achievable for e.g. GF(3) since the matrices are not packed. I didn't improve `randomize` since that one could be slightly more tricky.


---

Comment by malb created at 2008-08-26 14:55:08

*Old*

```
sage: time N=MatrixSpace(GF(7),10000,10000).random_element()
CPU times: user 6.77 s, sys: 1.08 s, total: 7.84 s
Wall time: 14.17 s
sage: N.set_immutable()
sage: %time hash(N)
CPU times: user 1.85 s, sys: 0.00 s, total: 1.85 s
Wall time: 1.86 s
737382666
```


*New*


```
sage: time N=MatrixSpace(GF(7),10000,10000).random_element()
CPU times: user 6.66 s, sys: 0.96 s, total: 7.63 s
Wall time: 7.68 s
sage: %time hash(N)
TypeError                                 Traceback (most recent call last)
...
TypeError: mutable matrices are unhashable
sage: N.set_immutable()
sage: %time hash(N)
CPU times: user 0.18 s, sys: 0.00 s, total: 0.18 s
Wall time: 0.19 s
3680002027
```



---

Comment by mabshoff created at 2008-08-27 07:58:58

Simon,

can you review this so it makes it into 3.1.2?

Cheers,

Michael


---

Comment by SimonKing created at 2008-08-27 14:47:09

Changing keywords from "" to "hash, matrix, finite field".


---

Comment by SimonKing created at 2008-08-27 14:47:09

The patch applies, it is faster than before, it seems to produce a reasonable hash value, and it raises an exception for mutable matrices. 

So, mainly i am giving a positive review.

But i have a couple of questions of more general nature concerning the doc tests:
 1. The doc string has a section EXAMPLE and TEST. Will both give rise to doc tests? Or more generally: What exactly must one put into the doc string such that it results in a doc test? E.g., i see that some people write "TEST CASES:", i think some write "EXAMPLES:", you write "EXAMPLE:" (without "S"), some write "TEST:" or "DOCTEST:" or "TESTS:".
 2. Under "EXAMPLE:", you have an "indirect doctest". Why is this test working? The matrix is random, hence, the result is random, but there is no key-word "random".
 3. Am i right that the hash value also depends on the size of `unsigned long`, hence, is machine dependent? Is this why you do not provide an example with a non-trivial hash value?

One remark: AFAIK, often hash values are cached. This is not done here (nor for matrices over GF(2)). Does anybody think that implementing a cache for the hash would be a good idea? (I don't)


---

Comment by malb created at 2008-08-27 15:04:56

>  1. The doc string has a section EXAMPLE and TEST. Will both give rise to doc tests? Or more generally: What exactly must one put into the doc string such that it results in a doc test? E.g., i see that some people write "TEST CASES:", i think some write "EXAMPLES:", you write "EXAMPLE:" (without "S"), some write "TEST:" or "DOCTEST:" or "TESTS:".

What matters is the `sage:` prompt, not the headline. Things under *TEST* are considered boring and not for enduser consumption. Still, they ought to be tested (and they are tested).

>  2. Under "EXAMPLE:", you have an "indirect doctest". Why is this test working? The matrix is random, hence, the result is random, but there is no key-word "random".

We have a *randstate* framework which takes care of pseudo-random doctests such that the same output is guaranteed for each run. The tag `#indirect doctest` indicates that I'm confident that the doctest tests the implementation even though the function name does not appear in the input. Otherwise `sage-coverage` would complaint.

>  3. Am i right that the hash value also depends on the size of `unsigned long`, hence, is machine dependent? Is this why you do not provide an example with a non-trivial hash value?

Yes. I think this is Python default.

> One remark: AFAIK, often hash values are cached. This is not done here (nor for matrices over GF(2)). Does anybody think that implementing a cache for the hash would be a good idea? (I don't)

I should be fast enough for most applications. But if there is demand, we can go ahead and cache it. I have no strong feelings about it.


---

Comment by SimonKing created at 2008-08-27 15:32:35

Thank you for your explanations, Martin.

All my questions are answered, so, there is a positive review.


---

Comment by robertwb created at 2008-08-27 16:38:24

Matrix hashes are specifically designed to be compatible with each other:


```
sage: M = random_matrix(GF(2), 10, 10)
sage: M.set_immutable()
sage: hash(M)
561
sage: MZ = M.change_ring(ZZ)
sage: MZ.set_immutable()
sage: hash(MZ)
561
sage: MS = M.spa
M.sparse_columns  M.sparse_matrix   M.sparse_rows     
sage: MS = M.sparse_matrix()
sage: MS.set_immutable()
sage: hash(MS)
561
```


This patch seems to break that. At a minimum, it seems sparse and dense should hash to the same thing. If we want to change this policy, we should at least ask on sage-devel.


---

Comment by malb created at 2008-08-27 16:56:15

Replying to [comment:7 robertwb]:
> Matrix hashes are specifically designed to be compatible with each other:
> This patch seems to break that. At a minimum, it seems sparse and dense should hash to the same thing. If we want to change this policy, we should at least ask on sage-devel. 

I didn't know about that. The updated patch plays nice.


---

Attachment

That is consistant, but I believe it may fail if rows get swapped (the old version too). Disclaimer: I wrote code to do that at http://hg.sagemath.org/sage-main/rev/b39c832e2eca , though it could potentially be sped up by caching `self._matrix[i]`

This has sparked an interesting discussion on sage-devel :)


---

Attachment


---

Comment by malb created at 2008-08-27 20:55:22

Replying to [comment:9 robertwb]:
> That is consistant, but I believe it may fail if rows get swapped (the old version too). Disclaimer: I wrote code to do that at http://hg.sagemath.org/sage-main/rev/b39c832e2eca , though it could potentially be sped up by caching `self._matrix[i]`

Good catch, I posted a new patch to address this.


---

Comment by robertwb created at 2008-08-30 19:47:38

Looks good to me. Apply only the last patch.


---

Comment by mabshoff created at 2008-08-30 19:53:10

Merged matrix_modn_dense_hash.3.patch in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-30 19:53:10

Resolution: fixed
