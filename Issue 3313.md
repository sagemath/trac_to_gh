# Issue 3313: Add code to lift SL2(Z/NZ) to SL2(Z) (and for m not equal 2)

archive/issues_003313.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan @mstreng @mmasdeu\n\nKeywords: lift symplectic sl sl2 sl2z special linear\n\nThis is very handy in the theory of abelian varieties... here's some code to do it.  Maybe someday I'll write the patch.\n\n\n```\ndef lift(A, N):\n    r\"\"\"\n    Lift a matrix A from SL_m(Z/NZ) to SL_m(Z).\n\n    Follows Shimura, Lemma 1.38, p21.\n\n    sage: N = 11\n    sage: A = matrix(ZZ, 4, 4, [6, 0, 0, 9, 1, 6, 9, 4, 4, 4, 8, 0, 4, 0, 0, 8])\n    sage: A.det()\n    144\n    sage: A.change_ring(Zmod(N)).det()\n    1\n    sage: L = lift(A, N)\n    sage: L.det()\n    1\n    sage: (L - A) * Mod(1, N) == 0\n    True\n\n    sage: N = 19\n    sage: B = matrix(ZZ, 4, 4, [1, 6, 10, 4, 4, 14, 15, 4, 13, 0, 1, 15, 15, 15, 17, 10])\n    sage: B.det()\n    4447\n    sage: B.change_ring(Zmod(N)).det()\n    1\n    sage: L = lift(B, N)\n    sage: L.det()\n    1\n    sage: (L - B) * Mod(1, N) == 0\n    True\n    \"\"\"\n    assert A.is_square()\n    assert det(A) != 0\n    m = A.nrows()\n    if m == 1:\n        return identity_matrix(1)\n\n    D, U, V = A.smith_form()\n    assert det(U) == 1\n    assert det(V) == 1\n#     print\n#     print \"D\"\n#     print D\n\n    a = [ D[i, i] for i in range(m) ]\n    b = prod(a[1:])\n    W = identity_matrix(m)\n    W[0, 0] = b\n    W[1, 0] = b-1\n    W[0, 1] = 1\n#     print\n#     print \"W\"\n#     print W\n\n    X = identity_matrix(m)\n    X[0, 1] = -a[1]\n#     print\n#     print \"X\"\n#     print X\n\n    Ap = D.copy()\n    Ap[0, 0] = 1\n    Ap[1, 0] = 1-a[0]\n    Ap[1, 1] *= a[0]\n#     print\n#     print \"Ap\"\n#     print Ap\n\n    assert (W*U*A*V*X).change_ring(Zmod(N)) == Ap.change_ring(Zmod(N))\n    Cp = diagonal_matrix(a[1:])\n    Cp[0, 0] *= a[0]\n    C = lift(Cp, N)\n#     print \"C\"\n#     print C\n\n    Cpp = block_diagonal_matrix(identity_matrix(1), C)\n    Cpp[1, 0] = 1-a[0]\n#     print \"Cpp\"\n#     print Cpp\n\n#     print\n    return (~U * ~W * Cpp * ~X * ~V).change_ring(ZZ)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3313\n\n",
    "created_at": "2008-05-27T04:30:49Z",
    "labels": [
        "component: number theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "Add code to lift SL2(Z/NZ) to SL2(Z) (and for m not equal 2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3313",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @ncalexan @mstreng @mmasdeu

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


Issue created by migration from https://trac.sagemath.org/ticket/3313





---

archive/issue_comments_022865.json:
```json
{
    "body": "There seems to be a fix for matrices arising with determinant -1 instead of +1 at [this ask question](http://ask.sagemath.org/question/2634/lifting-matrices-to-sl_2mathbbz).",
    "created_at": "2013-06-01T11:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22865",
    "user": "https://trac.sagemath.org/admin/accounts/users/tmonteil"
}
```

There seems to be a fix for matrices arising with determinant -1 instead of +1 at [this ask question](http://ask.sagemath.org/question/2634/lifting-matrices-to-sl_2mathbbz).



---

archive/issue_comments_022866.json:
```json
{
    "body": "The case m=2 is already in there, but a bit hidden.\n\n```\nsage: from sage.modular.local_comp.liftings import lift_matrix_to_sl2z\nsage: Matrix(ZZ, 2, lift_matrix_to_sl2z([3,7,5,6], 18))\n\n[21 25]\n[ 5  6]\n```\n\nIt also has no examples in its documentation: [http://doc.sagemath.org/html/en/reference/modmisc/sage/modular/local_comp/liftings.html](http://doc.sagemath.org/html/en/reference/modmisc/sage/modular/local_comp/liftings.html)",
    "created_at": "2017-06-30T09:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22866",
    "user": "https://github.com/mstreng"
}
```

The case m=2 is already in there, but a bit hidden.

```
sage: from sage.modular.local_comp.liftings import lift_matrix_to_sl2z
sage: Matrix(ZZ, 2, lift_matrix_to_sl2z([3,7,5,6], 18))

[21 25]
[ 5  6]
```

It also has no examples in its documentation: [http://doc.sagemath.org/html/en/reference/modmisc/sage/modular/local_comp/liftings.html](http://doc.sagemath.org/html/en/reference/modmisc/sage/modular/local_comp/liftings.html)



---

archive/issue_comments_022867.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-09-13T20:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22867",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_022868.json:
```json
{
    "body": "done\n----\nNew commits:",
    "created_at": "2017-09-13T20:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22868",
    "user": "https://github.com/fchapoton"
}
```

done
----
New commits:



---

archive/issue_comments_022869.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-14T08:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22869",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022870.json:
```json
{
    "body": "green bot, please review",
    "created_at": "2017-09-14T18:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22870",
    "user": "https://github.com/fchapoton"
}
```

green bot, please review



---

archive/issue_comments_022871.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-09-19T14:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22871",
    "user": "https://github.com/koffie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_022872.json:
```json
{
    "body": "Could you tell me which article of Shimura you are following? That makes it easier to review.\n\nAlso the reference to shimura should be formatted as explained under the references section in http://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings",
    "created_at": "2017-09-19T14:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22872",
    "user": "https://github.com/koffie"
}
```

Could you tell me which article of Shimura you are following? That makes it easier to review.

Also the reference to shimura should be formatted as explained under the references section in http://doc.sagemath.org/html/en/developer/coding_basics.html#documentation-strings



---

archive/issue_comments_022873.json:
```json
{
    "body": "As you may guess, given the number of the ticket, this was archeological work..\n\nI can only guess that this refers to Shimura's book \"Introduction to the arithmetic theory of automorphic functions\".\n\nSee https://math.stackexchange.com/questions/1409197/induced-group-homomorphism-textsl-n-mathbbz-twoheadrightarrow-textsl\n\nand https://mathoverflow.net/questions/164232/modular-group-modulo-n",
    "created_at": "2017-09-19T15:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22873",
    "user": "https://github.com/fchapoton"
}
```

As you may guess, given the number of the ticket, this was archeological work..

I can only guess that this refers to Shimura's book "Introduction to the arithmetic theory of automorphic functions".

See https://math.stackexchange.com/questions/1409197/induced-group-homomorphism-textsl-n-mathbbz-twoheadrightarrow-textsl

and https://mathoverflow.net/questions/164232/modular-group-modulo-n



---

archive/issue_comments_022874.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-19T16:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22874",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022875.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-09-19T16:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22875",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_022876.json:
```json
{
    "body": "done",
    "created_at": "2017-09-19T16:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22876",
    "user": "https://github.com/fchapoton"
}
```

done



---

archive/issue_comments_022877.json:
```json
{
    "body": "author?",
    "created_at": "2017-09-29T06:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22877",
    "user": "https://github.com/videlec"
}
```

author?



---

archive/issue_comments_022878.json:
```json
{
    "body": "review?",
    "created_at": "2017-09-30T12:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22878",
    "user": "https://github.com/fchapoton"
}
```

review?



---

archive/issue_comments_022879.json:
```json
{
    "body": "- `INPUT` section of the doc is missing\n\n- such function would better accept matrices from `SL(m, Z/NZ)` (in which case the `N` argument should be optional)\n\n```\nsage: A = matrix(Zmod(7), 2, [1,0,0,1])\nsage: L = lift_for_SL(A, 7)\nTraceback (most recent call last):\n...\nTypeError: unsupported operand parent(s) for *: 'Full MatrixSpace of 2 by 2 dense matrices over Ring of integers modulo 7' and 'Full MatrixSpace of 2 by 2 dense matrices over Rational Field'\n```\n\n\n- you are using inverses `~U * ~W * Cpp * ~X * ~V` but at least two of them are trivial (`W` and `X`). Why not constructing the inverses directly?\n\n- The matrix `Ap` is constructed but not used\n\n- in the matrix `D = U * A * V` you seem to be using only the diagonal terms. Would be smarter to compute only them (that would result in computing `n` terms instead of `n^2`).\n\n- the call to `C = lift_for_SL(Cp, N)` is making the function recursive. But `Cp` is a diagonal matrix, case for which the lifting is trivial.",
    "created_at": "2017-10-03T17:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22879",
    "user": "https://github.com/videlec"
}
```

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

archive/issue_comments_022880.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-10-03T17:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22880",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_events_007441.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2017-10-03T17:16:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "milestone": "sage-8.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3313#event-7441"
}
```



---

archive/issue_comments_022881.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-11-30T16:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22881",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022882.json:
```json
{
    "body": "some work done. Remains to get rid of the recursive call.",
    "created_at": "2017-11-30T16:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22882",
    "user": "https://github.com/fchapoton"
}
```

some work done. Remains to get rid of the recursive call.



---

archive/issue_comments_022883.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-12-06T12:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22883",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022884.json:
```json
{
    "body": "It is not true that the lift of diagonal matrices is trivial.\n\nSo this is now ready for review.",
    "created_at": "2017-12-06T12:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22884",
    "user": "https://github.com/fchapoton"
}
```

It is not true that the lift of diagonal matrices is trivial.

So this is now ready for review.



---

archive/issue_comments_022885.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-12-06T12:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22885",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_022886.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-12-06T17:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22886",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022887.json:
```json
{
    "body": "Salut Fr\u00e9d\u00e9ric,\n\nI don't understand completely why recursion is needed. In the recursive call, you are calling the function with a diagonal matrix as input that only depends on the Smith form. But this Smith form is trivial (U=V=identit\u00e9 and D=the input matrix). Of course `Winv` and `Xinv` are non trivial. But it should not be so complicated to include them in a loop. Though I did not give a try. Perhaps you want me to?\n\nInstead of\n\n```\n    diag = diagonal_matrix([-1] + [1] * (m - 1))\n    if U.det() == -1:\n        U = diag * U\n    if V.det() == -1:\n        V = V * diag\n```\n\nwouldn't\n\n```\n    if U.det() * V.det() == -1:\n        diag = diagonal_matrix([-1] + [1] * (m - 1))\n        U = diag * U\n```\n\nbe ok?",
    "created_at": "2017-12-06T20:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22887",
    "user": "https://github.com/videlec"
}
```

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

archive/issue_comments_022888.json:
```json
{
    "body": "I would rather not spend a too large amount of time on that ticket. I would prefer to have feedback on #22397, potentially useful for my research.\n\nSmith form of a diagonal matrix may not be totally trivial:\n\n```\nsage: m = diagonal_matrix(ZZ,[2*2*3,2*3*5,2*3*5*7])\nsage: m.smith_form()\n\n(\n[  6   0   0]  [  1   0   1]  [-17   0 -35]\n[  0  30   0]  [  0   1   0]  [  0   1   0]\n[  0   0 420], [-35   0 -34], [  1   0   2]\n)\n```\n",
    "created_at": "2017-12-07T16:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22888",
    "user": "https://github.com/fchapoton"
}
```

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

archive/issue_comments_022889.json:
```json
{
    "body": "I see now. Thanks for the example.\n\n- What about input matrices being defined over `ZZ/N ZZ`? (see also [This is the Trac macro *comment:14* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#comment:14-macro)) \n\n- Could you add some random tests\n\n```\nsage: for _ in range(100):\n....:     d = randint(0, 10)\n....:     p = choice([2,3,5,7,11])\n....:     M = random_matrix(Zmod(p), d, algorithm='unimodular')\n....:     lift_for_SL(M)\n```\n",
    "created_at": "2017-12-08T22:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22889",
    "user": "https://github.com/videlec"
}
```

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

archive/issue_comments_022890.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-12-09T07:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22890",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022891.json:
```json
{
    "body": "Random tests were added.\n\nAnd the function already accepts both matrices in ZZ and in Zmod.",
    "created_at": "2017-12-09T07:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22891",
    "user": "https://github.com/fchapoton"
}
```

Random tests were added.

And the function already accepts both matrices in ZZ and in Zmod.



---

archive/issue_comments_022892.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-12-15T14:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22892",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007442.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2017-12-15T14:33:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "milestone": "sage-8.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3313#event-7442"
}
```



---

archive/issue_events_007443.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2017-12-15T14:33:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "milestone": "sage-8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3313#event-7443"
}
```



---

archive/issue_comments_022893.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2017-12-17T10:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22893",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_022894.json:
```json
{
    "body": "Merge conflict",
    "created_at": "2017-12-17T10:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22894",
    "user": "https://github.com/vbraun"
}
```

Merge conflict



---

archive/issue_comments_022895.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-01-12T13:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22895",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022896.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2018-01-12T13:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22896",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_022897.json:
```json
{
    "body": "after a trivial rebase, I allow myself to set this back to positive",
    "created_at": "2018-01-12T13:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22897",
    "user": "https://github.com/fchapoton"
}
```

after a trivial rebase, I allow myself to set this back to positive



---

archive/issue_comments_022898.json:
```json
{
    "body": "Documentation doesn't build (see patchbot)",
    "created_at": "2018-01-14T12:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22898",
    "user": "https://github.com/vbraun"
}
```

Documentation doesn't build (see patchbot)



---

archive/issue_comments_022899.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2018-01-14T12:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22899",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_022900.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-01-14T15:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22900",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022901.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2018-01-14T18:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22901",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_022902.json:
```json
{
    "body": "ok, bot is now green",
    "created_at": "2018-01-14T18:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22902",
    "user": "https://github.com/fchapoton"
}
```

ok, bot is now green



---

archive/issue_comments_022903.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-01-20T10:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3313#issuecomment-22903",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_007444.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2018-01-20T10:42:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3313",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3313#event-7444"
}
```
