# Issue 9549: InfinitePolynomialRing_sparse.is_field lacks `proof=...` option

Issue created by migration from https://trac.sagemath.org/ticket/9549

Original creator: mmezzarobba

Original creation time: 2010-07-19 11:47:08

Assignee: malb

The class `InfinitePolynomialRing_sparse` defines two methods called `is_field()`. The second definition rejects keyword arguments. This prevents from creating polynomial rings over infinite polynomial rings:

```
$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: InfinitePolynomialRing(QQ, 'a')['x']
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.5, Release Date: 2010-07-16                         |
| Type notebook() for the GUI, and license() for information.        |
/home/marc/opt/sage-4.5/<ipython console> in <module>()

/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2550)()

/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)
    341                 raise TypeError, "if second arguments is a string with no commas, then there must be no other non-optional arguments"
    342             name = arg1
--> 343             R = _single_variate(base_ring, name, sparse, implementation)
    344         else:
    345             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):

/home/marc/opt/sage-4.5/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)
    420             R = m.PolynomialRing_dense_padic_ring_fixed_mod(base_ring, name)
    421 
--> 422         elif base_ring.is_field(proof = False):
    423             R = m.PolynomialRing_field(base_ring, name, sparse, implementation=implementation)
    424 

TypeError: is_field() got an unexpected keyword argument 'proof'
```


There is a similar issue with ``is_integral_domain``, too.


---

Comment by mmezzarobba created at 2010-07-19 12:08:39

Please disregard (or better, delete) the previous attachment.


---

Comment by mmezzarobba created at 2010-07-19 12:54:54

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2010-07-19 12:54:54

Replying to [comment:1 mmezzarobba]:
> Please disregard (or better, delete) the previous attachment.

I have now replaced it with the correct file. (It seems that for some reason, unprivilegied trac users are allowed to replace attached files but not to delete them??!)


---

Comment by mhansen created at 2010-07-19 17:41:21

You probably don't want the line


```
print "coucou" 
```


in the patch.


---

Comment by mhansen created at 2010-07-19 17:41:21

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by mmezzarobba created at 2010-07-19 20:16:03

Changing status from needs_work to needs_review.


---

Comment by mmezzarobba created at 2010-07-19 20:16:03

Replying to [comment:3 mhansen]:
> You probably don't want the line
> 
> {{{
> print "coucou" 
> }}}
> 
> in the patch.

Sorry--I was sure I had double-checked that it wasn't in the patch after uploading it... :-/ Thanks for spotting my blunder.


---

Comment by mhansen created at 2010-08-11 20:38:42

In is_integral_domain, we should pass on the keywords to self._base.is_integral_domain() so that that can take a proof option.


---

Comment by mhansen created at 2010-08-11 20:38:42

Changing status from needs_review to needs_work.


---

Comment by fwclarke created at 2010-11-05 12:49:26

This has been fixed by #9443.


---

Comment by fwclarke created at 2010-11-05 12:49:26

Resolution: duplicate
