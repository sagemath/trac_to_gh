# Issue 4513: Action of MatrixGroup on a MPolynomialRing

Issue created by migration from https://trac.sagemath.org/ticket/4513

Original creator: SimonKing

Original creation time: 2008-11-13 16:03:53

Assignee: tbd

CC:  wdj malb

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


---

Comment by SimonKing created at 2008-11-13 22:11:34

Changing assignee from tbd to malb.


---

Comment by SimonKing created at 2008-11-13 22:11:34

Sorry, in the above code I forgot to copy/paste the line

```
sage: R.<x,y> = GF(3)[]
```


Moreover, for the reasons above, the ticket should belong to *commutative* algebra, not just algebra (I was clicking on the wrong button).


---

Comment by SimonKing created at 2008-11-13 22:11:34

Changing component from algebra to commutative algebra.


---

Comment by SimonKing created at 2008-11-13 22:23:29

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

Attachment

call method for MatrixGroupelement (this time with doc test) and left_matrix_action for MPolynomial


---

Comment by SimonKing created at 2008-11-14 07:43:22

Changing assignee from malb to SimonKing.


---

Comment by SimonKing created at 2008-11-14 07:43:22

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

Comment by SimonKing created at 2008-11-14 09:32:17

Another version of left_matrix_action


---

Attachment

In `matrixgroupCallNew.patch` (to be applied after the first patch), I modified the method according to my above concerns. In the example from my original post, the average running time improves from ~240 microseconds to 164 microseconds, and in a larger example it improved from 6.5s to 5.4s

Nevertheless, I made two separate patches, so that the reviewer (if there is any...) can compare by him- or herself.

Cheers
   Simon


---

Comment by SimonKing created at 2008-11-14 10:06:58

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

Comment by SimonKing created at 2008-11-14 12:17:51

Slight improvement; extended functionality


---

Attachment

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

The `left_matrix_action` shall eventually be used for computing the Reynolds operator of a group action; moreover, the Reynolds operator should be applicable on a _list_ of polynomials. Then, the function would repeatedly compute the image of the ring variables under the action of some group element. But then it would be better to compute that image only _once_ and pass it to `left_matrix_action`. The new patch provides this functionality. Example (continuing the original example):

```
sage: L=[X.left_matrix_action(g) for X in R.gens()]
sage: p.left_matrix_action(L)
x^3 + x^2*y - x*y^2 - y^3
```



---

Comment by wdj created at 2008-11-15 06:05:33

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

Comment by malb created at 2008-11-23 11:59:24


```
cdef list Im 
if isinstance(M,list): 
  Im = M 
```


shouldn't Im = M take care of the type checking anyway, so that a try-except block is sufficient? Also, I think maybe the type of p should be checked in the `__call__` method and a friendly error message raised? Not sure though.


---

Comment by malb created at 2008-11-23 12:01:25

Cython code looks good (just read it).


---

Comment by was created at 2008-11-28 07:25:53

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

Comment by SimonKing created at 2008-11-29 14:38:06

Really Oops. Sorry.

I implemented it analogous to what is done in Singular. Perhaps I am mistaken in the sense that it is supposed to be a right action (which then would deserve another notation).

```
sage: (G.0(G.1((p))))
-x^2*y + x*y^2 - y^3
sage: (G.1*G.0)(p)
-x^2*y + x*y^2 - y^3
```


However, I think it doesn't matter what Singular does. I will look up the literature whether one really wants a _right_ or _left_ action, and how the left action is supposed to be.


---

Comment by SimonKing created at 2008-11-29 14:46:36

Replying to [comment:12 SimonKing]:
> However, I think it doesn't matter what Singular does. I will look up the literature whether one really wants a _right_ or _left_ action...

I mean, something like "one has a left action on a variety, which gives rise to a right action on the coordinate ring". I have to sort it out.

If this is the case, then it should be better implemented in the `__mul__` method of polynomials, isn't it? Such as

```
sage: p*G.1*G.0==p*(G.1*G.0)
True
```



---

Comment by was created at 2008-11-29 18:55:25

Left actions should use __call__, right actions should use *exponentiation*.

Substitution is a right action. Substitution of the *inverse* is a left action.


---

Attachment

Replaces the other patches


---

Comment by SimonKing created at 2010-07-17 13:51:57

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-07-17 13:51:57

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

Comment by SimonKing created at 2010-07-17 13:53:27

I made Cc to malb and wdj, since it both concerns polynomials and groups.


---

Comment by nharris created at 2010-11-05 21:37:21

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

Comment by nharris created at 2010-11-05 21:37:21

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-11-06 12:37:25

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

So, unless a doc test _fails_ because of my patch, the criticism about not raising the doc test coverage is invalid.


---

Comment by SimonKing created at 2010-11-06 12:37:25

Changing status from needs_work to needs_review.


---

Comment by nharris created at 2010-11-06 17:57:37

I'm sorry if I did something that I shouldn't have. I was just following this guideline for reviewing patches (found here [http://www.sagemath.org/doc/developer/trac.html#section-review-patches](http://www.sagemath.org/doc/developer/trac.html#section-review-patches)):

Is it documented sufficiently, including both explanation and doctests? This is very important: all code in Sage must have doctests, *so even if the patch is for code which did not have a doctest before, the new version must include one*. In particular, all new code must be 100% doctested. Use the command sage -coverage <files> to see the coverage percentage of <files>.


---

Comment by SimonKing created at 2010-11-08 13:35:44

Replying to [comment:21 nharris]:
> Is it documented sufficiently, including both explanation and doctests? This is very important: all code in Sage must have doctests, *so even if the patch is for code which did not have a doctest before, the new version must include one*. In particular, all new code must be 100% doctested. Use the command sage -coverage <files> to see the coverage percentage of <files>.

If you would read the patch, you would find:

1. The patch adds one case to an existing method, namely `_act_on_`.

2. The patch adds several doc tests to `_act_on_`, covering the new functionality.

3. The original version of `_act_on_` already had a doc test.

In particular, it is _impossible_ to detect the doc test change without reading the patch, by just using `sage -coverage`: The coverage script detects whether `_act_on_` has any test (this is the case with or without my patch), but it does not detect whether the patch extends existing documentation to cover a new case.


---

Comment by davidloeffler created at 2010-12-31 17:16:42

Apply `trac-4513_matrix_action_on_polynomials.patch`

(for patchbot -- it's trying to apply all the patches at once)


---

Comment by davidloeffler created at 2010-12-31 17:17:36

`Apply trac-4513_matrix_action_on_polynomials.patch`

(maybe it will work this time?)


---

Comment by davidloeffler created at 2010-12-31 17:22:00


```
Apply trac-4513_matrix_action_on_polynomials.patch
```


(For some reason patchbot's not picking this up -- I apologise to all human beings reading this for the spam!)


---

Comment by davidloeffler created at 2011-01-20 09:09:47

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

Comment by davidloeffler created at 2011-01-20 09:09:47

Changing status from needs_review to needs_work.
