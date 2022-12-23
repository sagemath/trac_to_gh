# Issue 6059: speed regresion in hilbert_symbol after #5834

Issue created by migration from https://trac.sagemath.org/ticket/6059

Original creator: tornaria

Original creation time: 2009-05-17 22:54:54

Assignee: tornaria

CC:  cremona

Keywords: regression

The following hilbert symbol computation

```
sage: a=(next_prime(10**22)*next_prime(10**23))
sage: time hilbert_symbol(a,-1,2)
CPU times: user 0.62 s, sys: 0.06 s, total: 0.68 s
Wall time: 0.68 s
1
```

used to be almost instant before the patch in #5834 (in 4.0.alpha0).

The patch extends hilbert_symbol to work with rationals, by using the `squarefree_part()` function. However, that function needs to factor. Fortunately, we don't need the actual squarefree part to compute the hilbert symbol, rather we could use `numerator()*denominator()` to achieve the same result; the hilbert symbol can thus be computed without factoring.



---

Comment by tornaria created at 2009-05-18 02:44:53

Since this fixes a speed regression, and the patch is really simple, I think it's good if it can make it into 4.0.


---

Attachment

Fix speed regression in hilbert_symbol (revised)


---

Comment by tornaria created at 2009-05-18 03:33:53

I screwed it up the first version, because I was trying to avoid overhead. The original code, good for integers only (before #5834) was:

```
a = ZZ(a)
```

My first version was

```
a = ZZ(a.numerator() * a.denominator())
```

which breaks when `a` is a (python) `int`. The new version is

```
a = QQ(a).numerator() * QQ(a).denominator()
```

which should be safe for all purposes (my first version was in between).

Indeed, I'm a bit concerned about overhead. Compare the trivial

```
sage: timeit("hilbert_symbol(1,1,-1)")
625 loops, best of 3: 10.3 µs per loop
```

using the original code (only good for integers) vs.

```
sage: timeit("hilbert_symbol(1,1,-1)")
625 loops, best of 3: 19.1 µs per loop
```

with the new code (good for rationals).

And check out the speed of the actual computation:

```
sage: a = ZZ.random_element(10^50)
sage: b = ZZ.random_element(10^50)
sage: p = next_prime(ZZ.random_element(10^50))
sage: timeit("pari(a).hilbert(b,p)")
625 loops, best of 3: 3.13 µs per loop
```


Is there a standard/suggested way of writing the preamble of a function (where parameters are checked, coerced, etc) to minimize overhead in a fast path?
(I guess this is what one buys with a dynamic language... and moving this to cython could help if really necessary).


---

Comment by cremona created at 2009-05-18 09:12:23

Looks good to me.  Sorry about the regression which was my fault.  I needed an integer in the same square class as a (and b) and did the obvious thing without thinking about the conseqences regarding factorization.

Would it be better to check for integrality, since if a and b are integral then using ZZ(a), ZZ(b) would save the conversion to rational and back?  i.e. do something like try: a=ZZ(a); b=ZZ(b) first.


---

Comment by mabshoff created at 2009-05-18 15:54:15

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-18 15:54:15

Resolution: fixed
