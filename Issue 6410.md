# Issue 6410: optimize creation of diagonal matrices

Issue created by migration from https://trac.sagemath.org/ticket/6410

Original creator: was

Original creation time: 2009-06-25 16:13:11

Assignee: was

CC:  jason


```

Actually there are two issues.

Sure, the determinant issue is fairly easily diagnosed. No wonder that an n!
algorithm takes time. I'll try to look into this.

But it's not the only thing.

> sage: p=3
> sage: n=1000
> sage: K=GF(p)
> sage: KP.<x>=PolynomialRing(K)
> sage: time xI=diagonal_matrix([x for i in range(n)])
> CPU times: user 32.18 s, sys: 0.14 s, total: 32.33 s
> Wall time: 32.34 s

While in comparison, doing
M=matrix(KP,n)
for i in range(n): M[i,i]=x

returns instantly.

Tracing it down, it seems that when calling diagonal_matrix:

- The list is converted to a dictionary.
- Because a dense matrix was requested, this dictionary is in turn converted
to a flat list of n^2 entries.
- The base __matrix_class constructor is called, and calls the parent ring
conversion routine for each entry.

I don't know whether it's reasonable or not to have a million coercions of
zero take thirty seconds total (quite possibly not), but in any case these
can be avoided.

I suggest the attached patch.

Emmanuel.Thome at gmail.com
```



---

Attachment


---

Comment by cremona created at 2009-06-28 15:21:35

Sorry, Emmanuel, but you'll have to remove the accent from your name since the patch cannot be applied:

```
john@ubuntu%sage -hg qpush
applying diagonal_matrix.patch
transaction abort!
rollback completed
cleaning up working directory...done
abort: decoding near 'anuel Thom� <Emmanue': 'utf8' codec can't decode bytes in position 13-15: invalid data!
```


I edited the patch in order to apply it, but found that your example was just as slow afterwards.  Is the diagonal_matrix() function actually calling the function you changed?

Also, there should be a doctest with your example in.


---

Comment by cremona created at 2009-06-28 15:31:03

Apologies -- I had two clones mixed up.  After the patch it *is* much faster (instantaneous).  But you still need to remove the accent and add a doctest!


---

Comment by mhansen created at 2009-10-19 19:45:07

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-10-19 19:45:07

Apply only trac_6410.patch.

I've updated it to take care of the issues that John pointed out.


---

Comment by rbeezer created at 2009-10-27 04:12:30

Changing status from needs_review to needs_work.


---

Attachment

It appears to me the slowdown results when a dense matrix has many entries that need to be coerced.  So for a diagonal matrix built as a dense matrix, this means all of the off-diagonal entries need to be coerced.  But the behavior is caused more generally by `matrix()`.  Consider the following session:


```
sage: K=GF(3)
sage: KP.<x>=PolynomialRing(K)
sage: G={}; H={}
sage: for i in range(200):
....:     for j in range(200):
....:         H[(i,j)]=KP(1)
....:         G[(i,j)]=1
....:
sage: timeit('matrix(KP,200,H,sparse=False)')
5 loops, best of 3: 136 ms per loop
sage: timeit('matrix(KP,200,G,sparse=False)')
5 loops, best of 3: 1.09 s per loop
```


This is with the patch applied.  The only difference is the dictionary H has the elements coerced, while the dictionary G does not.  The timings are nearly identical to pre-patch behavior.

It seems to me that in the patch, the line `A = self(0)` still causes `n^2` coercions of the zero element in `__call__` (of which it is a part)?  I could very well be mistaken, but I can't see a method one can use to semi-automatically coerce 0 once (and only once) and then fill a dense matrix with that single coerced zero.  Should the behavior of `zero_matrix()` be changed, so it does not just use `__call__`?

Ina any event, this review is not for nought.  The doctest has `sage;` (w/ a semi-colon) and not a `sage:` (w/ a colon) so it seems to not even be coming through in the documentation, and likely the test is not run?


---

Comment by mmezzarobba created at 2014-03-15 08:09:34

sage-6.2.beta4:

```
sage: p=3
sage: n=1000
sage: K = GF(p)
sage: KP.<x> = K[]                                                                            
sage: %timeit xI=diagonal_matrix([x for i in range(n)])                                       
10 loops, best of 3: 15.8 ms per loop                                                         
```



---

Comment by mmezzarobba created at 2014-03-15 08:09:34

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2014-03-25 12:35:51

(set a ticket to positive review when it is invalid)


---

Comment by ncohen created at 2014-03-25 12:35:51

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-31 12:29:50

Resolution: fixed
