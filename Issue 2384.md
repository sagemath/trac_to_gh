# Issue 2384: reduce finite field implementations

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-03-04 11:38:04

Assignee: malb

CC:  dmharvey ncalexan mderickx


```
[Tue Mar 4 2008] [05:06:54] <dmharvey>  how many finite field implementations do we have?
[Tue Mar 4 2008] [05:06:56] <dmharvey>  it's crazy.
```


I propose:
 * implement `FiniteField_ntl` which covers `ntl.GF2E`, `ntl.ZZ_pE` and `ntl.lzz_pE` via a bunch of function pointers. This introduces a pointer dereference as overhead but this should be relatively cheap compared to the actual operations (small fields are implemented via Givaro anyway). 
 * kill `FiniteField_ext_pari` 

This would leave us with two implementations: one for small extension fields and one for larger (in terms of the order)


---

Comment by dmharvey created at 2008-03-04 14:16:06

Actually, malb, I retract my statement. The problem is not that we have way too many implementations of finite fields (and your proposed solution wouldn't fix that anyway, because `FiniteField_ntl` would need to split into three underlying implementations, so it's just window-dressing).

I think the real problem is just that the PARI version is slow! It's slow because:
 * it's in python
 * it uses crazy decimal-string formats internally for all kinds of operations
 * PARI does not use asymptotically fast algorithms for arithmetic. (This is not a problem for small fields, but it's precisely when the fields become large that it's a problem, and this is precisely when we're using PARI.)

Another problem is that for prime fields, we still use the python implementation `FiniteField_prime_modn`.

So I propose the following. As malb says, kill `FiniteField_ext_pari`. Replace with the following, all in cython:
 * `FiniteField_prime_modn` (already exists, but needs to be cythonised)
 * `FiniteField_ntl_gf2e` (already exists).
 * `FiniteField_givaro` (already exists).
 * `FiniteField_ntl_zz_pE`
 * `FiniteField_ntl_ZZ_pE`

Possible the first one needs to be split into two, one for "small" moduli (word-sized) and one for "large" moduli (mpz).


---

Comment by was created at 2008-03-04 15:02:57

> So I propose the following. As malb says, kill FiniteField_ext_pari. 

Hi, I wrote FiniteField_ext_pari long ago and only ever meant it is
a "reference implementation" to fix the API.  I'm very happy that you're
talking about doing a real fast implementation as you suggest above. 

William


---

Comment by malb created at 2008-03-04 15:09:30

> Actually, malb, I retract my statement. The problem is not that we have way too 
> many implementations of finite fields (and your proposed solution wouldn't fix
> that anyway, because FiniteField_ntl would need to split into three underlying
> implementations, so it's just window-dressing).

Maybe we should still consider this window-dressing to keep the number of classes down and make writing fast code easier. With this cosmetic change the author only needs to check for one rather than three types.

> I think the real problem is just that the PARI version is slow! It's slow because:
>  * it's in python
>  * it uses crazy decimal-string formats internally for all kinds of operations
>  * PARI does not use asymptotically fast algorithms for arithmetic. (This is not a problem for small fields, but it's precisely when the fields become large that it's a problem, and this is precisely when we're using PARI.)

This is #417

> Another problem is that for prime fields, we still use the python implementation `FiniteField_prime_modn`.

The field is Python but the elements are not:


```
sage: k = IntegerModRing(7)
sage: type(k)
<class 'sage.rings.integer_mod_ring.IntegerModRing_generic'>
sage: type(k.random_element())
<type 'sage.rings.integer_mod.IntegerMod_int'>

sage: k = GF(7)
sage: type(k)
<class 'sage.rings.finite_field.FiniteField_prime_modn'>
sage: type(k.random_element())
<type 'sage.rings.integer_mod.IntegerMod_int'>
```



---

Comment by dmharvey created at 2008-03-04 15:24:21

Replying to [comment:3 malb]:
> > Actually, malb, I retract my statement. The problem is not that we have way too 
> > many implementations of finite fields (and your proposed solution wouldn't fix
> > that anyway, because FiniteField_ntl would need to split into three underlying
> > implementations, so it's just window-dressing).
> 
> Maybe we should still consider this window-dressing to keep the number of classes down and make writing fast code easier. With this cosmetic change the author only needs to check for one rather than three types.

I don't understand. If `ntl.GF2E`, `ntl.ZZ_pE` and `ntl.lzz_pE` all should be covered by the same class `FiniteField_ntl`, why shouldn't the givaro implementation also be covered there? What do the NTL classes have in common that makes them different from e.g. givaro?

> > I think the real problem is just that the PARI version is slow! It's slow because:
> This is #417

ok thanks

> > Another problem is that for prime fields, we still use the python implementation `FiniteField_prime_modn`.
> 
> The field is Python but the elements are not:

ok I missed that.


---

Comment by malb created at 2008-03-04 15:33:27

> I don't understand. If `ntl.GF2E`, `ntl.ZZ_pE` and `ntl.lzz_pE` all 
> should be covered by the same class `FiniteField_ntl`, why shouldn't the
> givaro implementation also be covered there? What do the NTL classes have in
> common that makes them different from e.g. givaro?

They have the same C++ interface, i.e. it should be easy to setup a struct of function pointers for arithmetic and other stuff. I'm not pushing for it though. Also, for Givaro the extra pointer lookup would hurt but for the NTL classes probably not.


---

Comment by dmharvey created at 2008-03-04 15:44:28

Replying to [comment:5 malb]:
> They have the same C++ interface, i.e. it should be easy to setup a struct of function pointers for arithmetic and other stuff. I'm not pushing for it though. Also, for Givaro the extra pointer lookup would hurt but for the NTL classes probably not.

I don't think they have the same C++ interface. Well, syntactically they're pretty close, like for example `add(x, y)` works for all NTL types. But there are syntactic differences: for example `ZZ_pContext` and `zz_pContext` have different names. And the underlying types are totally unrelated (e.g. `ZZ_pX` and `zz_pX`), so I don't see how you can do anything safely with function pointers.


---

Comment by robertwb created at 2008-03-05 18:21:26

Just a note, I did a lot of work with Finite Fields for the coercion model (tangential to what is being discussed here) so it might be prudent to wait until that is merged before doing a lot of big changes. 

I would imagine that the parent for all the finite_field_ntl could be the same, and there should be a finite_field_ntl_element class that could contain common functionality. 

What C++isms would Cython have to support to take advantage of the similarity between, say, ZZ_pX and xx_pX?


---

Comment by robertwb created at 2008-03-06 01:13:46

Here's a possible idea: we could use the include directive in Cython to write generic code for all 3 types of NTL polynomials, and then use the cdef extern string trick to generate the three classes. 

On another note, I think I remember hearing somewhere that magma uses zech logs as coefficients, e.g. GF(p^n) is implemented as a relative extension of GF(p^d) where p^d is small enough for the log representation. Would this be worth looking at?


---

Comment by dmharvey created at 2008-03-06 01:19:53

Replying to [comment:8 robertwb]:
> On another note, I think I remember hearing somewhere that magma uses zech logs as coefficients, e.g. GF(p^n) is implemented as a relative extension of GF(p^d) where p^d is small enough for the log representation. Would this be worth looking at? 

This would only work when n is sufficiently composite, but in that case I think it's a great idea. Still, you need to have very good generic polynomial arithmetic to make this work. I think this is something to work on later.


---

Comment by malb created at 2008-03-28 11:42:58

What shall we do about this ticket? I propose: close it as `wontfix` and open another ticket for Robert's idea maybe.


---

Comment by malb created at 2008-04-01 12:04:50

This is now #2750.


---

Comment by malb created at 2008-06-12 22:55:48

Resolution: wontfix


---

Comment by malb created at 2008-06-12 22:55:48

Okay, closing it now.
