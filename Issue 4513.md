# Issue 4513: Action of MatrixGroup on a MPolynomialRing

archive/issues_004513.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @wdjoyner @malb\n\nKeywords: matrix group, action, polynomial ring\n\nA group of n by n matrices over a field K acts on a polynomial ring with n variables over K. However, this is not implemented yet.\n\nOff list, David Joyner suggested to implement it with a `__call__` method in `matrix_group_element.py`. Then, the following should work:\n\n```\nsage: M=Matrix(GF(3),[[1,2],[1,1]])\nsage: G=MatrixGroup([M])\nsage: g=G.0\nsage: p=x*y^2\nsage: g(p)\nx^3 + x^2*y - x*y^2 - y^3\nsage: _==(x+2*y)*(x+y)^2\nTrue\n```\n\n\nAlthough it concerns `matrix_group_element.py`, I believe this ticket belongs to Commutative Algebra, for two reasons:\n1. An efficient implementation probably requires knowledge of the guts of MPolynomialElement.\n2. My long-term goal is to re-implement my algorithms for the computation of non-modular invariant rings. The current implementation is in the `finvar.lib` library of Singular -- the slow Singular interpreter sometimes is a bottle necks.\n\nOne more general technical question: It is `matrix_group_element.py`, hence seems to be pure python. Is it possible to define an additional method in some `.pyx` file using Cython? I don't know if this would be reasonable to do here, but perhaps this could come in handy at some point...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4513\n\n",
    "created_at": "2008-11-13T16:03:53Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Action of MatrixGroup on a MPolynomialRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4513",
    "user": "@simon-king-jena"
}
```
Assignee: tbd

CC:  @wdjoyner @malb

Keywords: matrix group, action, polynomial ring

A group of n by n matrices over a field K acts on a polynomial ring with n variables over K. However, this is not implemented yet.

Off list, David Joyner suggested to implement it with a `__call__` method in `matrix_group_element.py`. Then, the following should work:

```
sage: M=Matrix(GF(3),[[1,2],[1,1]])
sage: G=MatrixGroup([M])
sage: g=G.0
sage: p=x*y^2
sage: g(p)
x^3 + x^2*y - x*y^2 - y^3
sage: _==(x+2*y)*(x+y)^2
True
```


Although it concerns `matrix_group_element.py`, I believe this ticket belongs to Commutative Algebra, for two reasons:
1. An efficient implementation probably requires knowledge of the guts of MPolynomialElement.
2. My long-term goal is to re-implement my algorithms for the computation of non-modular invariant rings. The current implementation is in the `finvar.lib` library of Singular -- the slow Singular interpreter sometimes is a bottle necks.

One more general technical question: It is `matrix_group_element.py`, hence seems to be pure python. Is it possible to define an additional method in some `.pyx` file using Cython? I don't know if this would be reasonable to do here, but perhaps this could come in handy at some point...

Issue created by migration from https://trac.sagemath.org/ticket/4513





---

archive/issue_comments_033473.json:
```json
{
    "body": "Changing assignee from tbd to @malb.",
    "created_at": "2008-11-13T22:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33473",
    "user": "@simon-king-jena"
}
```

Changing assignee from tbd to @malb.



---

archive/issue_comments_033474.json:
```json
{
    "body": "Sorry, in the above code I forgot to copy/paste the line\n\n```\nsage: R.<x,y> = GF(3)[]\n```\n\n\nMoreover, for the reasons above, the ticket should belong to *commutative* algebra, not just algebra (I was clicking on the wrong button).",
    "created_at": "2008-11-13T22:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33474",
    "user": "@simon-king-jena"
}
```

Sorry, in the above code I forgot to copy/paste the line

```
sage: R.<x,y> = GF(3)[]
```


Moreover, for the reasons above, the ticket should belong to *commutative* algebra, not just algebra (I was clicking on the wrong button).



---

archive/issue_comments_033475.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2008-11-13T22:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33475",
    "user": "@simon-king-jena"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_033476.json:
```json
{
    "body": "The patch `matrixgroupCall.patch` is without doctests, and I am not sure if it couldn't be done better. So, it needs more work.\n\nFor example, Martin mentioned the possibility (off list) to create a pyx file with a Cython function, and then the call method would use that function. It might pay off here, since there are tight loops and since the method has to deal with tuples or lists. So Cdefining might speed things up.\n\nOpinions?\n\nAt least, the following now works:\n\n```\nsage: R.<x,y>=GF(3)[]\nsage: M=Matrix(GF(3),[[1,2],[1,1]])\nsage: G=MatrixGroup([M])\nsage: g=G.0\nsage: p=x*y^2\nsage: g(p)\nx^3 + x^2*y - x*y^2 - y^3\n```\n",
    "created_at": "2008-11-13T22:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33476",
    "user": "@simon-king-jena"
}
```

The patch `matrixgroupCall.patch` is without doctests, and I am not sure if it couldn't be done better. So, it needs more work.

For example, Martin mentioned the possibility (off list) to create a pyx file with a Cython function, and then the call method would use that function. It might pay off here, since there are tight loops and since the method has to deal with tuples or lists. So Cdefining might speed things up.

Opinions?

At least, the following now works:

```
sage: R.<x,y>=GF(3)[]
sage: M=Matrix(GF(3),[[1,2],[1,1]])
sage: G=MatrixGroup([M])
sage: g=G.0
sage: p=x*y^2
sage: g(p)
x^3 + x^2*y - x*y^2 - y^3
```




---

archive/issue_comments_033477.json:
```json
{
    "body": "Attachment [matrixgroupCall.patch](tarball://root/attachments/some-uuid/ticket4513/matrixgroupCall.patch) by @simon-king-jena created at 2008-11-14 07:26:53\n\ncall method for MatrixGroupelement (this time with doc test) and left_matrix_action for MPolynomial",
    "created_at": "2008-11-14T07:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33477",
    "user": "@simon-king-jena"
}
```

Attachment [matrixgroupCall.patch](tarball://root/attachments/some-uuid/ticket4513/matrixgroupCall.patch) by @simon-king-jena created at 2008-11-14 07:26:53

call method for MatrixGroupelement (this time with doc test) and left_matrix_action for MPolynomial



---

archive/issue_comments_033478.json:
```json
{
    "body": "Changing assignee from @malb to @simon-king-jena.",
    "created_at": "2008-11-14T07:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33478",
    "user": "@simon-king-jena"
}
```

Changing assignee from @malb to @simon-king-jena.



---

archive/issue_comments_033479.json:
```json
{
    "body": "Some changes:\n\nNicolas Thi\u00e9ry suggested to implement the action of matrix groups by a method for polynomials (I call the method `left_matrix_action`), and, for convenience, also provide a `__call__` method for MatrixGroupElement that refers to `left_matrix_action`.\n\nThis has several advantages:\n* The `__call__` works for any class that has a `left_matrix_action` method, hence, it is not a-priori restricted to polynomials.\n* I've put `left_matrix_action` into `multi_polynomial.pyx`, hence, I can use Cython.\n\nI have two Cython concerns left:\n1. The innerst loop is \n {{{\nprod([Im[k]**X[k] for k in xrange(n)])\n }}}\n where `k` is c'defined as `int`. Should this better be done in a for-loop, rather then creating a list and calling `prod`?\n2. The variable `X` is of type `polydict.ETuple`, so I can not directly c'define `X`. One could do\n {{{\n    cdef tuple X\n    for i from 0<i<l:\n        X = tuple(Expo[i])\n }}}\n But would this be faster?",
    "created_at": "2008-11-14T07:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33479",
    "user": "@simon-king-jena"
}
```

Some changes:

Nicolas Thiéry suggested to implement the action of matrix groups by a method for polynomials (I call the method `left_matrix_action`), and, for convenience, also provide a `__call__` method for MatrixGroupElement that refers to `left_matrix_action`.

This has several advantages:
* The `__call__` works for any class that has a `left_matrix_action` method, hence, it is not a-priori restricted to polynomials.
* I've put `left_matrix_action` into `multi_polynomial.pyx`, hence, I can use Cython.

I have two Cython concerns left:
1. The innerst loop is 
 {{{
prod([Im[k]**X[k] for k in xrange(n)])
 }}}
 where `k` is c'defined as `int`. Should this better be done in a for-loop, rather then creating a list and calling `prod`?
2. The variable `X` is of type `polydict.ETuple`, so I can not directly c'define `X`. One could do
 {{{
    cdef tuple X
    for i from 0<i<l:
        X = tuple(Expo[i])
 }}}
 But would this be faster?



---

archive/issue_comments_033480.json:
```json
{
    "body": "Another version of left_matrix_action",
    "created_at": "2008-11-14T09:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33480",
    "user": "@simon-king-jena"
}
```

Another version of left_matrix_action



---

archive/issue_comments_033481.json:
```json
{
    "body": "Attachment [matrixgroupCallNew.patch](tarball://root/attachments/some-uuid/ticket4513/matrixgroupCallNew.patch) by @simon-king-jena created at 2008-11-14 09:36:29\n\nIn `matrixgroupCallNew.patch` (to be applied after the first patch), I modified the method according to my above concerns. In the example from my original post, the average running time improves from ~240 microseconds to 164 microseconds, and in a larger example it improved from 6.5s to 5.4s\n\nNevertheless, I made two separate patches, so that the reviewer (if there is any...) can compare by him- or herself.\n\nCheers\n   Simon",
    "created_at": "2008-11-14T09:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33481",
    "user": "@simon-king-jena"
}
```

Attachment [matrixgroupCallNew.patch](tarball://root/attachments/some-uuid/ticket4513/matrixgroupCallNew.patch) by @simon-king-jena created at 2008-11-14 09:36:29

In `matrixgroupCallNew.patch` (to be applied after the first patch), I modified the method according to my above concerns. In the example from my original post, the average running time improves from ~240 microseconds to 164 microseconds, and in a larger example it improved from 6.5s to 5.4s

Nevertheless, I made two separate patches, so that the reviewer (if there is any...) can compare by him- or herself.

Cheers
   Simon



---

archive/issue_comments_033482.json:
```json
{
    "body": "One observation: \nReverse the outer loop\n\n```\n        for i from l>i>=0:\n            X = tuple(Expo[i])\n            c = Coef[i]\n            for k from 0<=k<n:\n                if X[k]:\n                    c *= Im[k]**X[k]\n            q += c\n```\n\nIt results in a further improvement of computation time. Is this coincidence? Or is it since summation of polynomials should better start with the smallest summands?\n\nAnyway, I didn't change the patch yet.",
    "created_at": "2008-11-14T10:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33482",
    "user": "@simon-king-jena"
}
```

One observation: 
Reverse the outer loop

```
        for i from l>i>=0:
            X = tuple(Expo[i])
            c = Coef[i]
            for k from 0<=k<n:
                if X[k]:
                    c *= Im[k]**X[k]
            q += c
```

It results in a further improvement of computation time. Is this coincidence? Or is it since summation of polynomials should better start with the smallest summands?

Anyway, I didn't change the patch yet.



---

archive/issue_comments_033483.json:
```json
{
    "body": "Slight improvement; extended functionality",
    "created_at": "2008-11-14T12:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33483",
    "user": "@simon-king-jena"
}
```

Slight improvement; extended functionality



---

archive/issue_comments_033484.json:
```json
{
    "body": "Attachment [matrixgroupCallNew2.patch](tarball://root/attachments/some-uuid/ticket4513/matrixgroupCallNew2.patch) by @simon-king-jena created at 2008-11-14 12:25:13\n\nReplying to [comment:6 SimonKing]:\n> One observation: \n> Reverse the outer loop\n> {{{\n>         for i from l>i>=0:\n>             X = tuple(Expo[i])\n>             c = Coef[i]\n>             for k from 0<=k<n:\n>                 if X[k]:\n>                     c *= Im[k]**X[k]\n>             q += c\n> }}}\n> It results in a further improvement of computation time. Is this coincidence? Or is it since summation of polynomials should better start with the smallest summands?\n\nI made a couple of tests, and there was a small but consistent improvement. So, in the third patch (to be applied after the other two) I did it in that way.\n\nThe `left_matrix_action` shall eventually be used for computing the Reynolds operator of a group action; moreover, the Reynolds operator should be applicable on a *list* of polynomials. Then, the function would repeatedly compute the image of the ring variables under the action of some group element. But then it would be better to compute that image only *once* and pass it to `left_matrix_action`. The new patch provides this functionality. Example (continuing the original example):\n\n```\nsage: L=[X.left_matrix_action(g) for X in R.gens()]\nsage: p.left_matrix_action(L)\nx^3 + x^2*y - x*y^2 - y^3\n```\n",
    "created_at": "2008-11-14T12:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33484",
    "user": "@simon-king-jena"
}
```

Attachment [matrixgroupCallNew2.patch](tarball://root/attachments/some-uuid/ticket4513/matrixgroupCallNew2.patch) by @simon-king-jena created at 2008-11-14 12:25:13

Replying to [comment:6 SimonKing]:
> One observation: 
> Reverse the outer loop
> {{{
>         for i from l>i>=0:
>             X = tuple(Expo[i])
>             c = Coef[i]
>             for k from 0<=k<n:
>                 if X[k]:
>                     c *= Im[k]**X[k]
>             q += c
> }}}
> It results in a further improvement of computation time. Is this coincidence? Or is it since summation of polynomials should better start with the smallest summands?

I made a couple of tests, and there was a small but consistent improvement. So, in the third patch (to be applied after the other two) I did it in that way.

The `left_matrix_action` shall eventually be used for computing the Reynolds operator of a group action; moreover, the Reynolds operator should be applicable on a *list* of polynomials. Then, the function would repeatedly compute the image of the ring variables under the action of some group element. But then it would be better to compute that image only *once* and pass it to `left_matrix_action`. The new patch provides this functionality. Example (continuing the original example):

```
sage: L=[X.left_matrix_action(g) for X in R.gens()]
sage: p.left_matrix_action(L)
x^3 + x^2*y - x*y^2 - y^3
```




---

archive/issue_comments_033485.json:
```json
{
    "body": "I did confirm that the patches apply cleanly,\nthat\n\n\n```\nsage: M = Matrix(GF(3),[[1,2],[1,1]])\nsage: G = MatrixGroup([M])\nsage: g = G.0\nsage: g\n\n[1 2]\n[1 1]\nsage: P.<x,y> = PolynomialRing(GF(3),2)\nsage: p = x*y^2\nsage: g(p)\nx^3 + x^2*y - x*y^2 - y^3\nsage: (x+2*y)*(x+y)^2\nx^3 + x^2*y - x*y^2 - y^3\n\n```\n\nworks, and that the code seems well-documented.\n\nHowever, I can't do testing on this machine \n(intrepid ubuntu) and some of the code is written in \nCython, which I can't really 100% vouch for. \nSeems okay though and simple enough. Since speed was a\ntopic of the comments above, my only question is that the \nsegment\n\n```\n \t396\t        for i from 0<=i<l: \n \t397\t            X = Expo[i] \n \t398\t            c = Coef[i] \n \t399\t            q += c*prod([Im[k]**X[k] for k in xrange(n)]) \n```\n\ncould probably be rewritten as a one-line sum, which might \n(or might not) be faster.\n\nMaybe Martin Albrecht could comment on the Cython code?\n\nIf Martin (for example) passes the Cython code, and the\ndocstrings pass sage -testall, I would give it a positive review.",
    "created_at": "2008-11-15T06:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33485",
    "user": "@wdjoyner"
}
```

I did confirm that the patches apply cleanly,
that


```
sage: M = Matrix(GF(3),[[1,2],[1,1]])
sage: G = MatrixGroup([M])
sage: g = G.0
sage: g

[1 2]
[1 1]
sage: P.<x,y> = PolynomialRing(GF(3),2)
sage: p = x*y^2
sage: g(p)
x^3 + x^2*y - x*y^2 - y^3
sage: (x+2*y)*(x+y)^2
x^3 + x^2*y - x*y^2 - y^3

```

works, and that the code seems well-documented.

However, I can't do testing on this machine 
(intrepid ubuntu) and some of the code is written in 
Cython, which I can't really 100% vouch for. 
Seems okay though and simple enough. Since speed was a
topic of the comments above, my only question is that the 
segment

```
 	396	        for i from 0<=i<l: 
 	397	            X = Expo[i] 
 	398	            c = Coef[i] 
 	399	            q += c*prod([Im[k]**X[k] for k in xrange(n)]) 
```

could probably be rewritten as a one-line sum, which might 
(or might not) be faster.

Maybe Martin Albrecht could comment on the Cython code?

If Martin (for example) passes the Cython code, and the
docstrings pass sage -testall, I would give it a positive review.



---

archive/issue_comments_033486.json:
```json
{
    "body": "\n```\ncdef list Im \nif isinstance(M,list): \n  Im = M \n```\n\n\nshouldn't Im = M take care of the type checking anyway, so that a try-except block is sufficient? Also, I think maybe the type of p should be checked in the `__call__` method and a friendly error message raised? Not sure though.",
    "created_at": "2008-11-23T11:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33486",
    "user": "@malb"
}
```


```
cdef list Im 
if isinstance(M,list): 
  Im = M 
```


shouldn't Im = M take care of the type checking anyway, so that a try-except block is sufficient? Also, I think maybe the type of p should be checked in the `__call__` method and a friendly error message raised? Not sure though.



---

archive/issue_comments_033487.json:
```json
{
    "body": "Cython code looks good (just read it).",
    "created_at": "2008-11-23T12:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33487",
    "user": "@malb"
}
```

Cython code looks good (just read it).



---

archive/issue_comments_033488.json:
```json
{
    "body": "REFEREE REPORT:\n\nCheck this out:\n\n```\nsage: R.<x,y> = GF(3)[]\nsage: M=Matrix(GF(3),[[1,2],[1,1]])\nsage: M2=Matrix(GF(3),[[1,2],[1,0]])\nsage: G=MatrixGroup([M, M2])\nsage: (G.0*G.1)(p)\n-x^2*y + x*y^2 - y^3\nsage: G.0(G.1(p))\nx^2*y + x*y^2 + y^3\n```\n\n\nOops, your *left action* -- which it better be if you use that notation -- ain't a left action!  Oops\n\n -- William",
    "created_at": "2008-11-28T07:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33488",
    "user": "@williamstein"
}
```

REFEREE REPORT:

Check this out:

```
sage: R.<x,y> = GF(3)[]
sage: M=Matrix(GF(3),[[1,2],[1,1]])
sage: M2=Matrix(GF(3),[[1,2],[1,0]])
sage: G=MatrixGroup([M, M2])
sage: (G.0*G.1)(p)
-x^2*y + x*y^2 - y^3
sage: G.0(G.1(p))
x^2*y + x*y^2 + y^3
```


Oops, your *left action* -- which it better be if you use that notation -- ain't a left action!  Oops

 -- William



---

archive/issue_comments_033489.json:
```json
{
    "body": "Really Oops. Sorry.\n\nI implemented it analogous to what is done in Singular. Perhaps I am mistaken in the sense that it is supposed to be a right action (which then would deserve another notation).\n\n```\nsage: (G.0(G.1((p))))\n-x^2*y + x*y^2 - y^3\nsage: (G.1*G.0)(p)\n-x^2*y + x*y^2 - y^3\n```\n\n\nHowever, I think it doesn't matter what Singular does. I will look up the literature whether one really wants a *right* or *left* action, and how the left action is supposed to be.",
    "created_at": "2008-11-29T14:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33489",
    "user": "@simon-king-jena"
}
```

Really Oops. Sorry.

I implemented it analogous to what is done in Singular. Perhaps I am mistaken in the sense that it is supposed to be a right action (which then would deserve another notation).

```
sage: (G.0(G.1((p))))
-x^2*y + x*y^2 - y^3
sage: (G.1*G.0)(p)
-x^2*y + x*y^2 - y^3
```


However, I think it doesn't matter what Singular does. I will look up the literature whether one really wants a *right* or *left* action, and how the left action is supposed to be.



---

archive/issue_comments_033490.json:
```json
{
    "body": "Replying to [comment:12 SimonKing]:\n> However, I think it doesn't matter what Singular does. I will look up the literature whether one really wants a *right* or *left* action...\n\nI mean, something like \"one has a left action on a variety, which gives rise to a right action on the coordinate ring\". I have to sort it out.\n\nIf this is the case, then it should be better implemented in the `__mul__` method of polynomials, isn't it? Such as\n\n```\nsage: p*G.1*G.0==p*(G.1*G.0)\nTrue\n```\n",
    "created_at": "2008-11-29T14:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33490",
    "user": "@simon-king-jena"
}
```

Replying to [comment:12 SimonKing]:
> However, I think it doesn't matter what Singular does. I will look up the literature whether one really wants a *right* or *left* action...

I mean, something like "one has a left action on a variety, which gives rise to a right action on the coordinate ring". I have to sort it out.

If this is the case, then it should be better implemented in the `__mul__` method of polynomials, isn't it? Such as

```
sage: p*G.1*G.0==p*(G.1*G.0)
True
```




---

archive/issue_comments_033491.json:
```json
{
    "body": "Left actions should use __call__, right actions should use *exponentiation*.\n\nSubstitution is a right action. Substitution of the *inverse* is a left action.",
    "created_at": "2008-11-29T18:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33491",
    "user": "@williamstein"
}
```

Left actions should use __call__, right actions should use *exponentiation*.

Substitution is a right action. Substitution of the *inverse* is a left action.



---

archive/issue_comments_033492.json:
```json
{
    "body": "Attachment [trac-4513_matrix_action_on_polynomials.patch](tarball://root/attachments/some-uuid/ticket4513/trac-4513_matrix_action_on_polynomials.patch) by @simon-king-jena created at 2010-07-17 13:49:02\n\nReplaces the other patches",
    "created_at": "2010-07-17T13:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33492",
    "user": "@simon-king-jena"
}
```

Attachment [trac-4513_matrix_action_on_polynomials.patch](tarball://root/attachments/some-uuid/ticket4513/trac-4513_matrix_action_on_polynomials.patch) by @simon-king-jena created at 2010-07-17 13:49:02

Replaces the other patches



---

archive/issue_comments_033493.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-17T13:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33493",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033494.json:
```json
{
    "body": "The new patch solves the problems addressed in the new ticket description.\n\nI worked on top of several other tickets, since I somehow cared about number fields. To be precise, I did\n\n```\nhg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9205/trac_9205-discrete_log.patch')\nhg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9205/trac_9205-doctest.patch')\nhg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9438/trac_9438_IntegerMod_log_vs_PARI.patch')\nhg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9423/trac_9423_gap_for_numberfields.patch')\nhg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8909/8909_gap2cyclotomic.patch')\nhg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8909/trac_8909_catch_exception.patch')\nhg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5618/trac_5618_gap_for_cyclotomic_fields.patch')\n```\n\nbefore creating my pacth. But this shouldn't matter, I guess the patch applies cleanly to `sage-4.4`.",
    "created_at": "2010-07-17T13:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33494",
    "user": "@simon-king-jena"
}
```

The new patch solves the problems addressed in the new ticket description.

I worked on top of several other tickets, since I somehow cared about number fields. To be precise, I did

```
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9205/trac_9205-discrete_log.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9205/trac_9205-doctest.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9438/trac_9438_IntegerMod_log_vs_PARI.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9423/trac_9423_gap_for_numberfields.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8909/8909_gap2cyclotomic.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8909/trac_8909_catch_exception.patch')
hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5618/trac_5618_gap_for_cyclotomic_fields.patch')
```

before creating my pacth. But this shouldn't matter, I guess the patch applies cleanly to `sage-4.4`.



---

archive/issue_comments_033495.json:
```json
{
    "body": "I made Cc to malb and wdj, since it both concerns polynomials and groups.",
    "created_at": "2010-07-17T13:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33495",
    "user": "@simon-king-jena"
}
```

I made Cc to malb and wdj, since it both concerns polynomials and groups.



---

archive/issue_comments_033496.json:
```json
{
    "body": "Sorry to be a nag, but matrix_group_element.py doesn't pass the doctests:\n\n\n```\n----------------------------------------------------------------------\nmatrix_group_element.py\nSCORE matrix_group_element.py: 87% (14 of 16)\n\nMissing documentation:\n\t * is_MatrixGroupElement(x):\n\t * __invert__(self):\n\n----------------------------------------------------------------------\n```\n\n\nThis is the same doctest score that the old unpatched file gets too.",
    "created_at": "2010-11-05T21:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33496",
    "user": "nharris"
}
```

Sorry to be a nag, but matrix_group_element.py doesn't pass the doctests:


```
----------------------------------------------------------------------
matrix_group_element.py
SCORE matrix_group_element.py: 87% (14 of 16)

Missing documentation:
	 * is_MatrixGroupElement(x):
	 * __invert__(self):

----------------------------------------------------------------------
```


This is the same doctest score that the old unpatched file gets too.



---

archive/issue_comments_033497.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-05T21:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33497",
    "user": "nharris"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033498.json:
```json
{
    "body": "Replying to [comment:19 nharris]:\n> Sorry to be a nag, but matrix_group_element.py doesn't pass the doctests:\n\nWhich one fails?\n\n> {{{\n> ----------------------------------------------------------------------\n> matrix_group_element.py\n> SCORE matrix_group_element.py: 87% (14 of 16)\n> \n> Missing documentation:\n> \t * is_MatrixGroupElement(x):\n> \t * __invert__(self):\n> \n> ----------------------------------------------------------------------\n> }}}\n> \n> This is the same doctest score that the old unpatched file gets too.\n\nOf course there is no change. I added code to one already existing method, extending its functionality, and added tests for the new functionality. But this patch is not about inversion of matrix group elements, and I think the patch is not supposed to add documentation to methods that are not in its scope.\n\nSo, unless a doc test *fails* because of my patch, the criticism about not raising the doc test coverage is invalid.",
    "created_at": "2010-11-06T12:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33498",
    "user": "@simon-king-jena"
}
```

Replying to [comment:19 nharris]:
> Sorry to be a nag, but matrix_group_element.py doesn't pass the doctests:

Which one fails?

> {{{
> ----------------------------------------------------------------------
> matrix_group_element.py
> SCORE matrix_group_element.py: 87% (14 of 16)
> 
> Missing documentation:
> 	 * is_MatrixGroupElement(x):
> 	 * __invert__(self):
> 
> ----------------------------------------------------------------------
> }}}
> 
> This is the same doctest score that the old unpatched file gets too.

Of course there is no change. I added code to one already existing method, extending its functionality, and added tests for the new functionality. But this patch is not about inversion of matrix group elements, and I think the patch is not supposed to add documentation to methods that are not in its scope.

So, unless a doc test *fails* because of my patch, the criticism about not raising the doc test coverage is invalid.



---

archive/issue_comments_033499.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-06T12:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33499",
    "user": "@simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033500.json:
```json
{
    "body": "I'm sorry if I did something that I shouldn't have. I was just following this guideline for reviewing patches (found here [http://www.sagemath.org/doc/developer/trac.html#section-review-patches](http://www.sagemath.org/doc/developer/trac.html#section-review-patches)):\n\nIs it documented sufficiently, including both explanation and doctests? This is very important: all code in Sage must have doctests, **so even if the patch is for code which did not have a doctest before, the new version must include one**. In particular, all new code must be 100% doctested. Use the command sage -coverage <files> to see the coverage percentage of <files>.",
    "created_at": "2010-11-06T17:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33500",
    "user": "nharris"
}
```

I'm sorry if I did something that I shouldn't have. I was just following this guideline for reviewing patches (found here [http://www.sagemath.org/doc/developer/trac.html#section-review-patches](http://www.sagemath.org/doc/developer/trac.html#section-review-patches)):

Is it documented sufficiently, including both explanation and doctests? This is very important: all code in Sage must have doctests, **so even if the patch is for code which did not have a doctest before, the new version must include one**. In particular, all new code must be 100% doctested. Use the command sage -coverage <files> to see the coverage percentage of <files>.



---

archive/issue_comments_033501.json:
```json
{
    "body": "Replying to [comment:21 nharris]:\n> Is it documented sufficiently, including both explanation and doctests? This is very important: all code in Sage must have doctests, **so even if the patch is for code which did not have a doctest before, the new version must include one**. In particular, all new code must be 100% doctested. Use the command sage -coverage <files> to see the coverage percentage of <files>.\n\nIf you would read the patch, you would find:\n\n1. The patch adds one case to an existing method, namely `_act_on_`.\n\n2. The patch adds several doc tests to `_act_on_`, covering the new functionality.\n\n3. The original version of `_act_on_` already had a doc test.\n\nIn particular, it is *impossible* to detect the doc test change without reading the patch, by just using `sage -coverage`: The coverage script detects whether `_act_on_` has any test (this is the case with or without my patch), but it does not detect whether the patch extends existing documentation to cover a new case.",
    "created_at": "2010-11-08T13:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33501",
    "user": "@simon-king-jena"
}
```

Replying to [comment:21 nharris]:
> Is it documented sufficiently, including both explanation and doctests? This is very important: all code in Sage must have doctests, **so even if the patch is for code which did not have a doctest before, the new version must include one**. In particular, all new code must be 100% doctested. Use the command sage -coverage <files> to see the coverage percentage of <files>.

If you would read the patch, you would find:

1. The patch adds one case to an existing method, namely `_act_on_`.

2. The patch adds several doc tests to `_act_on_`, covering the new functionality.

3. The original version of `_act_on_` already had a doc test.

In particular, it is *impossible* to detect the doc test change without reading the patch, by just using `sage -coverage`: The coverage script detects whether `_act_on_` has any test (this is the case with or without my patch), but it does not detect whether the patch extends existing documentation to cover a new case.



---

archive/issue_comments_033502.json:
```json
{
    "body": "Apply `trac-4513_matrix_action_on_polynomials.patch`\n\n(for patchbot -- it's trying to apply all the patches at once)",
    "created_at": "2010-12-31T17:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33502",
    "user": "@loefflerd"
}
```

Apply `trac-4513_matrix_action_on_polynomials.patch`

(for patchbot -- it's trying to apply all the patches at once)



---

archive/issue_comments_033503.json:
```json
{
    "body": "`Apply trac-4513_matrix_action_on_polynomials.patch`\n\n(maybe it will work this time?)",
    "created_at": "2010-12-31T17:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33503",
    "user": "@loefflerd"
}
```

`Apply trac-4513_matrix_action_on_polynomials.patch`

(maybe it will work this time?)



---

archive/issue_comments_033504.json:
```json
{
    "body": "\n```\nApply trac-4513_matrix_action_on_polynomials.patch\n```\n\n\n(For some reason patchbot's not picking this up -- I apologise to all human beings reading this for the spam!)",
    "created_at": "2010-12-31T17:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33504",
    "user": "@loefflerd"
}
```


```
Apply trac-4513_matrix_action_on_polynomials.patch
```


(For some reason patchbot's not picking this up -- I apologise to all human beings reading this for the spam!)



---

archive/issue_comments_033505.json:
```json
{
    "body": "I've had a look at the patch, and I don't think you've addressed William's comment #14 from two years back. The following makes me *extremely* uneasy:\n\n```\nsage: G = GL(3, 7)\nsage: R.<a, b> = GF(7)[]\nsage: G.0 * a\n[3*a   0   0]\n[  0   a   0]\n[  0   0   a]\nsage: R.<a,b,c> = GF(7)[]\nsage: G.0 * a\n3*a\n```\n\nIt looks like there's some pre-existing coercion mechanism which returns elements of the matrix space over R, and you're overriding it in one case with an alternative coercion that returns completely different answers; this violates a Sage coercion axiom (where there are multiple paths in the coercion diagram, all must give the same answer up to numerical precision issues). Moreover, if you look at the patchbot logs it seems to have found an example where the preexisting coercion gets picked up instead of the new one.\n\nSorry, that's a thumbs down from me. \n\nDavid",
    "created_at": "2011-01-20T09:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33505",
    "user": "@loefflerd"
}
```

I've had a look at the patch, and I don't think you've addressed William's comment #14 from two years back. The following makes me *extremely* uneasy:

```
sage: G = GL(3, 7)
sage: R.<a, b> = GF(7)[]
sage: G.0 * a
[3*a   0   0]
[  0   a   0]
[  0   0   a]
sage: R.<a,b,c> = GF(7)[]
sage: G.0 * a
3*a
```

It looks like there's some pre-existing coercion mechanism which returns elements of the matrix space over R, and you're overriding it in one case with an alternative coercion that returns completely different answers; this violates a Sage coercion axiom (where there are multiple paths in the coercion diagram, all must give the same answer up to numerical precision issues). Moreover, if you look at the patchbot logs it seems to have found an example where the preexisting coercion gets picked up instead of the new one.

Sorry, that's a thumbs down from me. 

David



---

archive/issue_comments_033506.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-20T09:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4513#issuecomment-33506",
    "user": "@loefflerd"
}
```

Changing status from needs_review to needs_work.
