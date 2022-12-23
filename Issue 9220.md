# Issue 9220: Upredictable parent for polynomial evaluation

Issue created by migration from https://trac.sagemath.org/ticket/9220

Original creator: nbruin

Original creation time: 2010-06-11 21:06:02

Assignee: robertwb

I doubt that it is intended that the names of the variables of a polynomial ring can affect the parent of the result of evaluating such a polynomial:


```
sage: R=QQ['x']
sage: S=QQ['x','y']
sage: h=S.0^2
sage: parent(h(R.0,0))
Multivariate Polynomial Ring in x, y over Rational Field

sage: R=QQ['x']
sage: S=QQ['u','v']
sage: h=S.0^2
sage: parent(h(R.0,0))
Univariate Polynomial Ring in x over Rational Field 
```

I would expect the result of the second example in both cases.

In

http://groups.google.com/group/sage-devel/browse_thread/thread/4607f62126303ddd?pli=1

John Cremona mentions #8502 as fixing a different but similar issue.


---

Comment by robertwb created at 2010-06-11 23:43:29

I agree, the result should only be a function of the base ring and evaluation argument parents.


---

Comment by nbruin created at 2010-06-14 18:36:03

I think I've found the culprit in:

```
built-in method __call__ of sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular
```

Indeed, it tries to coerce the evaluation values into the polynomial ring. Perhaps it should try to coerce into the base ring of the parent instead?

```
        if l != parent._ring.N:
            raise TypeError, "number of arguments does not match number of variables in parent"

        try:
            x = [parent._coerce_c(e) for e in x]
        except TypeError:
            # give up, evaluate functional
            y = parent.base_ring()(0)
            for (m,c) in self.dict().iteritems():
                y += c*mul([ x[i]**m[i] for i in m.nonzero_positions()])
            return y

```

If I were to fix this code, I'd simply always do the code under the "except", but someone probably had a good reason for doing it the way it's done. Probably because `singular_polynomial_call` is more efficient? I see several options:

 * Ask the coercion system for a common overring of the base ring of parent and all the parents of x. If that is parent, then coerce and use singular_polynomial_call. Otherwise just multiply out manually.

 * see if the parent of all members of x is equal to parent (due to the lax coercion rules, *coercible into* isn't good enough)

 * just always evaluate by multiplying out

The first one is the "proper" one in that it uses the coercion system to figure out if a more efficient option is available. The second option should be cheap and catch the case where most speed-up should be attainable. The third option wouldn't waste any time on checking parents, but would need coercion calls for each coefficient-monomial multiplication.


---

Comment by nbruin created at 2010-06-14 18:41:33

Indeed the present code does seem to address real overhead:

```
sage: R=QQ['x']
sage: S=QQ['x','y']
sage: h=S.0^2
sage: timeit('h(R.0,0)')
625 loops, best of 3: 269 µs per loop
```

but

```
sage: R=QQ['x']
sage: S=QQ['u','v']
sage: h=S.0^2
sage: timeit('h(R.0,0)')
625 loops, best of 3: 523 µs per loop
```

so option one or two above is probably the proper one.


---

Comment by nbruin created at 2010-06-14 19:47:21

Changing status from new to needs_review.


---

Comment by nbruin created at 2010-06-14 19:51:52

Attached patch is efficient when evaluation point has the same parent. I guess previously some efficiency was gained when a point was in the base ring as well (the result was subsequently recognised as a constant and coerced back?) by used libsingular evaluation directly. This is lost with attached patch. This probably means that this patch solves #8502 independently as well.

To reviewer or merger: feel free to change patch. I won't be touching the code anymore.


---

Attachment

add instead of previous


---

Comment by robertwb created at 2010-06-22 23:45:25

I've attached a patch that returns the correct parent without sacrificing the singular efficiency (together with a utility method in the coercion model to make this kind of thing easier elsewhere).


---

Comment by robertwb created at 2011-01-26 06:31:04

Apply only 9220-poly-evaluation-coerce.patch


---

Comment by boothby created at 2012-03-20 02:26:03

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2012-03-20 02:26:03

Works with 4.7.1.


---

Comment by jdemeyer created at 2012-03-29 14:44:44

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-03-29 14:44:44

Needs to be rebased to sage-5.0.beta11:

```
applying 9220-poly-evaluation-coerce.patch
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #2 succeeded at 4512 with fuzz 2 (offset 2764 lines).
Hunk #4 FAILED at 1785
1 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh 9220-poly-evaluation-coerce.patch
```



---

Attachment

Rebased on sage-5.4.rc2, apply only this patch.


---

Comment by robertwb created at 2012-10-24 07:02:56

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2012-10-27 22:57:49

Some docstring things:
- Please use auto-trac linking `:trac:`9220``
- For `common_parent()`, I would recommend:

```
Computes a common parent for all the inputs.

This is essentially an `n`-ary canonical coercion except it
can operate on parents rather than just elements. 

INPUT: 

- ``args`` -- a set of elements and/or parents

OUTPUT: 

A :class:`Parent` into which each input should coerce, or raises a 
``TypeError`` if no such :class:`Parent` can be found. 
```

  In particular, there is should not be an indent on the `INPUT:` and `OUTPUT:` blocks.

Thanks, 

Travis


---

Comment by tscrim created at 2012-11-26 06:28:37

Changing status from needs_review to needs_work.


---

Attachment

minor docstring fixes


---

Comment by robertwb created at 2013-01-22 05:24:34

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-01-31 17:03:55

Minor fixes to docstrings


---

Attachment

The rebased version worked for me. I've attached a small reviewer patch which just does the minor tweaks to the docstrings. Jeroen, I hope you don't mind me setting this back to a positive review.

Best,

Travis

For patchbot:

Apply only: 9220-poly-evaluation-coerce-5.4.rebase.patch, trac_9220-poly_evaluation-review-ts.patch


---

Comment by tscrim created at 2013-01-31 17:12:04

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-05 08:17:24

Resolution: fixed
