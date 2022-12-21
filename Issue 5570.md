# Issue 5570: determinants of matrices over Z/nZ with n composite are dog slow

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-19 23:11:08

Assignee: was

CC:  mvngu

In Sage it is not feasable to directly compute the determinant of a 20x20 matrix over Integers(26)!


```
David Kohel:
> A related problem I had recently was in finding a random
> element of GL_n(ZZ/26ZZ) where n was 20-30.  It was
> failing to terminate in the determinant computation.  My
> guess is that a  determinant over ZZ was being computed
> and reduced but that the resulting determinant was too big.
> I didn't verify this, but invite someone to check.

It is trivial to compute the determinant of an nxn matrix over ZZ when n <= 30 and the entries of the matrix have 2 digits.  That would be the case in your example. Sage wasn't computing your det over ZZ; if it had, then doing that computation would have worked fine.  For example:

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = random_matrix(Integers(26), 7)
sage: time a.det()
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.05 s
6
sage: a = random_matrix(Integers(26), 8)
sage: time a.det()
CPU times: user 0.15 s, sys: 0.00 s, total: 0.15 s
Wall time: 0.16 s
9
sage: a = random_matrix(Integers(26), 9)
sage: time a.det()
CPU times: user 1.37 s, sys: 0.01 s, total: 1.37 s
Wall time: 1.38 s
23
sage: time Integers(26)(a.lift().det())
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 0.39 s
23
sage: time Integers(26)(a.lift().det())
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
23
sage: a = random_matrix(Integers(26), 9)
sage: time Integers(26)(a.lift().det())
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
10
sage: a = random_matrix(Integers(26), 30)
sage: time Integers(26)(a.lift().det())
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
20
sage: a = random_matrix(Integers(26), 200)
sage: time Integers(26)(a.lift().det())
CPU times: user 0.30 s, sys: 0.04 s, total: 0.33 s
Wall time: 0.34 s
15
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |

It would thus be far better for now if Sage were to lift to ZZ, do the det, then reduce again.
For square-free modulus, a multimodular algorithm would of course be even better.
```



---

Comment by was created at 2009-03-19 23:15:04

More comments:

```
>
> Instead I worked around this by computing the determinants
> mod 2 and mod 13 and using CRT (if the determinants were
> both units).  The time was then almost trivial.  Suppose I
> replace this problem over ZZ/25ZZ or ZZ/256ZZ. I would
> still hope that the problem would NOT be lifted to ZZ for
> computation, since this would certainly not terminate in
> reasonable time for a dense matrix.

Yes it would.  Even for a dense 200x200 matrix over ZZ/256ZZ it only take 0.35 seconds total time to lift *and* compute the determinant, then reduce the result. 

sage: a = random_matrix(Integers(256), 30)
sage: time Integers(256)(a.lift().det())
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
222
sage: a = random_matrix(Integers(256), 200)
sage: time Integers(256)(a.lift().det())
CPU times: user 0.32 s, sys: 0.04 s, total: 0.35 s

Just out of curiosity, why didn't you try any of the above before writing this email?  :-)

> Taking the approach of lifting to ZZ for charpolys of matrices
> of non-trivial size will undoubtably lead to exactly the same
> coefficient explosion which is the presumed source of the
> problem with determinants over ZZ/26ZZ.
>
> --David

Except it isn't anywhere nearly so bad as you think:

sage: a = random_matrix(Integers(256), 500)
sage: time Integers(256)(a.lift().det())
CPU times: user 3.70 s, sys: 0.49 s, total: 4.19 s
Wall time: 4.04 s
188
sage: a = random_matrix(Integers(2^20), 500)
sage: time Integers(256)(a.lift().det())
CPU times: user 7.23 s, sys: 0.81 s, total: 8.04 s
Wall time: 7.94 s
208

All timings above on my 2GB of RAM Macbook laptop. 

William
```



---

Attachment


---

Comment by jhpalmieri created at 2009-03-21 15:40:40

This is about as naive a fix as could be imagined, although it does speed things up.


---

Attachment


---

Comment by was created at 2009-03-22 00:26:50

I give John's patch a positive review, modulo that I added doctests and made it not use generic code mod p if p is a large prime, since then the generic code still sucks right now.


---

Comment by jhpalmieri created at 2009-03-22 01:36:44

Looks good to me, although the generic mod p stuff isn't nearly as bad as the Z/nZ for n composite (these timings are before applying was's patch):

```
sage: R = Integers(nth_prime(50000))
sage: time mat.det()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
457476
sage: time R(mat.lift().det())
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
457476
sage: mat = random_matrix(R, 80)
sage: time mat.det()
CPU times: user 0.35 s, sys: 0.00 s, total: 0.36 s
Wall time: 0.36 s
296893
sage: time R(mat.lift().det())
CPU times: user 0.12 s, sys: 0.01 s, total: 0.13 s
Wall time: 0.13 s
296893
```



---

Comment by mabshoff created at 2009-03-23 20:46:43

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 20:46:43

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-28 20:55:26

The numbers for the improvement in the Sage 3.4.1 release tour are *completely* wrong:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = random_matrix(Integers(26), 10)
sage: time a.determinant()
CPU times: user 8.07 s, sys: 0.02 s, total: 8.09 s
Wall time: 8.11 s
3
sage: b = random_matrix(Integers(256), 10)
sage: time b.determinant()
CPU times: user 7.98 s, sys: 0.01 s, total: 7.99 s
Wall time: 7.98 s
0
```

vs.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = random_matrix(Integers(26), 10)
sage: time a.determinant()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.01 s
7
sage: b = random_matrix(Integers(256), 10)
sage: time b.determinant()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.00 s
89
```

| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
| Sage Version 3.4.1.alpha0, Release Date: 2009-03-26                |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael
