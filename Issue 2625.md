# Issue 2625: [with patch, needs review] BooleanPolynomial to Singular conversion

Issue created by migration from https://trac.sagemath.org/ticket/2625

Original creator: malb

Original creation time: 2008-03-21 01:52:52

Assignee: malb

CC:  burcin

`BooleanPolynomialRing`
 * more general constructor
 * cover_ring
 * defining_ideal
 * _singular_init_
 * some whitespace changes for docstrings

`MPolynomial`
 * is_homogenous

`BooleanMonomial`
 * degree method (same as deg method)


---

Attachment

I wasn't able to apply this to 2.10.4


```
patching file sage/rings/polynomial/pbori.pyx
Hunk #1 FAILED at 120
Hunk #2 FAILED at 148
2 out of 11 hunks FAILED -- saving rejects to file sage/rings/polynomial/pbori.pyx.rej
abort: patch failed to apply
```


are there other dependancies? 

Looking at the patch, it looks pretty good. The only comment I have is that __interface shouldn't have to be declared in `pbori.pxd`--it should already be there from ring.pxd


---

Comment by robertwb created at 2008-03-26 06:40:31

(sorry about the underline, I meant to type `__interface`)


---

Comment by malb created at 2008-03-26 11:28:42

Replying to [comment:1 robertwb]:
> I wasn't able to apply this to 2.10.4
> 
> {{{
> patching file sage/rings/polynomial/pbori.pyx
> Hunk #1 FAILED at 120
> Hunk #2 FAILED at 148
> 2 out of 11 hunks FAILED -- saving rejects to file sage/rings/polynomial/pbori.pyx.rej
> abort: patch failed to apply
> }}}
> 
> are there other dependancies? 

I just checked, this ticket depends on #2622 and #2611 . After these two have been applied it applies cleanly.

> Looking at the patch, it looks pretty good. The only comment I have is that `__interface` shouldn't have to be declared in `pbori.pxd` -- it should already be there from `ring.pxd` 

It isn't:

```
sage: search_src("__interface")
----------------------------------------------------------------------
----------------------------------------------------------------------
structure/sage_object.pyx:                X = self.__interface[I]
structure/sage_object.pyx:                    self.__interface = {}
structure/sage_object.pyx:                    # an __interface attribute.
structure/sage_object.pyx:                self.__interface[I] = X
rings/polynomial/pbori.pyx:        self.__interface = {}
rings/ring.pxd:    cdef public object __interface
rings/polynomial/pbori.pxd:    cdef public object __interface
```

| SAGE Version 2.10.4, Release Date: 2008-03-17                      |
| Type notebook() for the GUI, and license() for information.        |
That definition in `ring.pxd` is for `FiniteField`.


---

Comment by robertwb created at 2008-03-28 20:41:34

You are correct about `__interaface`, sorry. Still trying to figure out all the dependancies I need to test this (#2622 seems nontrivial).


---

Comment by malb created at 2008-04-01 13:17:57

Resolution: wontfix


---

Comment by malb created at 2008-04-01 13:17:57

Don't apply this patch, I'm splitting this up in the not PolyBoRi related parts and the PolyBoRi parts which I base on the 0.3.1 patch.
