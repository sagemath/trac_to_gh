# Issue 7324: improve order_from_multiple

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-10-27 19:40:00

Assignee: tbd

CC:  cremona rhinton

This function is used in many places, and can be greatly improved.


---

Comment by ylchapuy created at 2009-10-27 19:49:04

Changing status from new to needs_review.


---

Attachment

The provided patch should give no slowdown on small examples, and great speed up for bigger ones.
e.g.

* BEFORE:

```
sage: K.<a>=GF(3^108)
sage: time ord = order_from_multiple(a,3^108-1,operation="*")
CPU times: user 6.51 s, sys: 0.02 s, total: 6.53 s
Wall time: 6.56 s
```


* AFTER:

```
sage: K.<a>=GF(3^108)
sage: time ord = order_from_multiple(a,3^108-1,operation="*")
CPU times: user 1.98 s, sys: 0.02 s, total: 2.00 s
Wall time: 2.01 s
```


(it's based on 4.1.2, but I hope it applies fine to 4.2)

I also get rid of the power function in generic.py which is exactly the same as the generic_power in sage.structure.element

Finally, with sage 4.1.2, sage -testall reports no failure.


---

Comment by fwclarke created at 2009-10-29 10:15:24

This is a significant improvement, and it does apply to 4.2.  I'd give a 
fully positive review, but I've noticed a couple of things about this 
function which could be considered.

Most important, the function always checks whether `M*P` equals the
identity.  When this function is used one will normally be sure of the
order of the group (or of a subgroup in which the element lies), so that
this verification is unnecessary.  I think the function should have an
optional parameter `check` (with default value `True` for backwards
compatibility) and that the `assert` line should be executed only if 
`check is True`.  
I found that your GF(3<sup>108</sup>) example ran about 25% faster with the
`assert` line commented out.

I noticed that `plist` now only gets used to create the factorization `F`, and to check whether `M` is prime.
Thus the line 

```
        plist = [p for p,e in F]
```

isn't really needed.  This leads me to 
think that really the factorization of `M` is what should be cached 
by the caller, for giving `plist` requires that the exponents get computed each time the 
function is called.  Thus maybe there should be an optional parameter 
`factorization` (with `plist` kept for compatibility), with code such as such as

```
    if factorization:
        F = factorization
    elif plist:
        F = [(p, M.valuation(p)) for p in plist]
    else:
        F = M.factor()

    if list(F) == [(M, 1)]:
        return M
```


I notice that your GF(3<sup>108</sup>) example is nearly 4 times faster than 
`a.multiplicative_order()`, and I've opened ticket #7324 for this function 
to use `order_from_multiple`.


---

Attachment

The second patch addresses the comments from fwclarke.
It also removes the optional arguments 'op' 'inverses' and 'identity' as the were buggy and untested.


---

Comment by fwclarke created at 2009-11-06 10:47:57

Changing status from needs_review to positive_review.


---

Comment by fwclarke created at 2009-11-06 10:47:57

A positive review.  The suggestions I made have been implemented, and there's a doctest illustrating the new `check` parameter.  Some other parts of the code have been tidied up; in particular, the error raised for using an unknown operation now works properly.

It makes sense to remove the parameters `op`, `identity` and `inverse`, because they weren't being used, at least not in any consistent way.

All doctests still pass.

One triviality remains: a spelling correction; see the third patch.


---

Attachment


---

Comment by mhansen created at 2009-11-07 12:15:14

Resolution: fixed
