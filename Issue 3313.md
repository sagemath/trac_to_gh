# Issue 3313: Add code to lift SL2(Z/NZ) to SL2(Z) (and for m not equal 2)

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-05-27 04:30:49

Assignee: was

CC:  ncalexan mstreng mmasdeu

Keywords: lift symplectic sl sl2 sl2z special linear

This is very handy in the theory of abelian varieties... here's some code to do it.  Maybe someday I'll write the patch.


```
def lift(A, N):
    r"""
    Lift a matrix A from SL_m(Z/NZ) to SL_m(Z).

    Follows Shimura, Lemma 1.38, p21.

    sage: N = 11
    sage: A = matrix(ZZ, 4, 4, [6, 0, 0, 9, 1, 6, 9, 4, 4, 4, 8, 0, 4, 0, 0, 8])
    sage: A.det()
    144
    sage: A.change_ring(Zmod(N)).det()
    1
    sage: L = lift(A, N)
    sage: L.det()
    1
    sage: (L - A) * Mod(1, N) == 0
    True

    sage: N = 19
    sage: B = matrix(ZZ, 4, 4, [1, 6, 10, 4, 4, 14, 15, 4, 13, 0, 1, 15, 15, 15, 17, 10])
    sage: B.det()
    4447
    sage: B.change_ring(Zmod(N)).det()
    1
    sage: L = lift(B, N)
    sage: L.det()
    1
    sage: (L - B) * Mod(1, N) == 0
    True
    """
    assert A.is_square()
    assert det(A) != 0
    m = A.nrows()
    if m == 1:
        return identity_matrix(1)

    D, U, V = A.smith_form()
    assert det(U) == 1
    assert det(V) == 1
#     print
#     print "D"
#     print D

    a = [ D[i, i] for i in range(m) ]
    b = prod(a[1:])
    W = identity_matrix(m)
    W[0, 0] = b
    W[1, 0] = b-1
    W[0, 1] = 1
#     print
#     print "W"
#     print W

    X = identity_matrix(m)
    X[0, 1] = -a[1]
#     print
#     print "X"
#     print X

    Ap = D.copy()
    Ap[0, 0] = 1
    Ap[1, 0] = 1-a[0]
    Ap[1, 1] *= a[0]
#     print
#     print "Ap"
#     print Ap

    assert (W*U*A*V*X).change_ring(Zmod(N)) == Ap.change_ring(Zmod(N))
    Cp = diagonal_matrix(a[1:])
    Cp[0, 0] *= a[0]
    C = lift(Cp, N)
#     print "C"
#     print C

    Cpp = block_diagonal_matrix(identity_matrix(1), C)
    Cpp[1, 0] = 1-a[0]
#     print "Cpp"
#     print Cpp

#     print
    return (~U * ~W * Cpp * ~X * ~V).change_ring(ZZ)
```



---

Comment by tmonteil created at 2013-06-01 11:18:21

There seems to be a fix for matrices arising with determinant -1 instead of +1 at [this ask question](http://ask.sagemath.org/question/2634/lifting-matrices-to-sl_2mathbbz).


---

Comment by mstreng created at 2017-06-30 09:53:12

The case m=2 is already in there, but a bit hidden.

```
sage: from sage.modular.local_comp.liftings import lift_matrix_to_sl2z
sage: Matrix(ZZ, 2, lift_matrix_to_sl2z([3,7,5,6], 18))

[21 25]
[ 5  6]
```

It also has no examples in its documentation: [http://doc.sagemath.org/html/en/reference/modmisc/sage/modular/local_comp/liftings.html](http://doc.sagemath.org/html/en/reference/modmisc/sage/modular/local_comp/liftings.html)


---

Comment by chapoton created at 2017-09-13 20:07:43

Changing status from new to needs_review.


---

Comment by chapoton created at 2017-09-13 20:07:43

done
----
New commits:


---

Comment by git created at 2017-09-14 08:36:08

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-09-14 18:11:41

green bot, please review


---

Comment by mderickx created at 2017-09-19 14:59:43

Changing status from needs_review to needs_work.


---

Comment by mderickx created at 2017-09-19 14:59:43

Could you tell me which article of Shimura you are following? That makes it easier to review.

Also the reference to shimura should be formatted as explained under the references section in http://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings


---

Comment by chapoton created at 2017-09-19 15:09:45

As you may guess, given the number of the ticket, this was archeological work..

I can only guess that this refers to Shimura's book "Introduction to the arithmetic theory of automorphic functions".

See https://math.stackexchange.com/questions/1409197/induced-group-homomorphism-textsl-n-mathbbz-twoheadrightarrow-textsl

and https://mathoverflow.net/questions/164232/modular-group-modulo-n


---

Comment by git created at 2017-09-19 16:36:27

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-09-19 16:37:34

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2017-09-19 16:37:34

done


---

Comment by vdelecroix created at 2017-09-29 06:49:47

author?


---

Comment by chapoton created at 2017-09-30 12:12:58

review?


---

Comment by vdelecroix created at 2017-10-03 17:16:51

- `INPUT` section of the doc is missing

- such function would better accept matrices from `SL(m, Z/NZ)` (in which case the `N` argument should be optional)

```
sage: A = matrix(Zmod(7), 2, [1,0,0,1])
sage: L = lift_for_SL(A, 7)
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for *: 'Full MatrixSpace of 2 by 2 dense matrices over Ring of integers modulo 7' and 'Full MatrixSpace of 2 by 2 dense matrices over Rational Field'
```


- you are using inverses `~U * ~W * Cpp * ~X * ~V` but at least two of them are trivial (`W` and `X`). Why not constructing the inverses directly?

- The matrix `Ap` is constructed but not used

- in the matrix `D = U * A * V` you seem to be using only the diagonal terms. Would be smarter to compute only them (that would result in computing `n` terms instead of `n^2`).

- the call to `C = lift_for_SL(Cp, N)` is making the function recursive. But `Cp` is a diagonal matrix, case for which the lifting is trivial.


---

Comment by vdelecroix created at 2017-10-03 17:16:51

Changing status from needs_review to needs_work.


---

Comment by git created at 2017-11-30 16:55:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-11-30 16:56:06

some work done. Remains to get rid of the recursive call.


---

Comment by git created at 2017-12-06 12:41:55

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-12-06 12:43:00

It is not true that the lift of diagonal matrices is trivial.

So this is now ready for review.


---

Comment by chapoton created at 2017-12-06 12:43:00

Changing status from needs_work to needs_review.


---

Comment by git created at 2017-12-06 17:00:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2017-12-06 20:16:21

Salut Frédéric,

I don't understand completely why recursion is needed. In the recursive call, you are calling the function with a diagonal matrix as input that only depends on the Smith form. But this Smith form is trivial (U=V=identité and D=the input matrix). Of course `Winv` and `Xinv` are non trivial. But it should not be so complicated to include them in a loop. Though I did not give a try. Perhaps you want me to?

Instead of

```
    diag = diagonal_matrix([-1] + [1] * (m - 1))
    if U.det() == -1:
        U = diag * U
    if V.det() == -1:
        V = V * diag
```

wouldn't

```
    if U.det() * V.det() == -1:
        diag = diagonal_matrix([-1] + [1] * (m - 1))
        U = diag * U
```

be ok?


---

Comment by chapoton created at 2017-12-07 16:56:00

I would rather not spend a too large amount of time on that ticket. I would prefer to have feedback on #22397, potentially useful for my research.

Smith form of a diagonal matrix may not be totally trivial:

```
sage: m = diagonal_matrix(ZZ,[2*2*3,2*3*5,2*3*5*7])
sage: m.smith_form()

(
[  6   0   0]  [  1   0   1]  [-17   0 -35]
[  0  30   0]  [  0   1   0]  [  0   1   0]
[  0   0 420], [-35   0 -34], [  1   0   2]
)
```



---

Comment by vdelecroix created at 2017-12-08 22:12:54

I see now. Thanks for the example.

- What about input matrices being defined over `ZZ/N ZZ`? (see also [This is the Trac macro *comment:14* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#comment:14-macro)) 

- Could you add some random tests

```
sage: for _ in range(100):
....:     d = randint(0, 10)
....:     p = choice([2,3,5,7,11])
....:     M = random_matrix(Zmod(p), d, algorithm='unimodular')
....:     lift_for_SL(M)
```



---

Comment by git created at 2017-12-09 07:57:43

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-12-09 07:59:24

Random tests were added.

And the function already accepts both matrices in ZZ and in Zmod.


---

Comment by vdelecroix created at 2017-12-15 14:33:48

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-12-17 10:52:16

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2017-12-17 10:52:16

Merge conflict


---

Comment by git created at 2018-01-12 13:02:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2018-01-12 13:02:51

Changing status from needs_work to positive_review.


---

Comment by chapoton created at 2018-01-12 13:02:51

after a trivial rebase, I allow myself to set this back to positive


---

Comment by vbraun created at 2018-01-14 12:03:22

Documentation doesn't build (see patchbot)


---

Comment by vbraun created at 2018-01-14 12:03:22

Changing status from positive_review to needs_work.


---

Comment by git created at 2018-01-14 15:40:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2018-01-14 18:00:37

Changing status from needs_work to positive_review.


---

Comment by chapoton created at 2018-01-14 18:00:37

ok, bot is now green


---

Comment by vbraun created at 2018-01-20 10:42:45

Resolution: fixed
