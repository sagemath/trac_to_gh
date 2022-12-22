# Issue 4726: Creating homomorphisms of relative number fields seems totally broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-06 18:41:24

Assignee: was

CC:  lftabera

The following _should_ create the correct homomorphism (complex conjugation, see #4724):

```
sage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]
sage: conj = K.hom([-j, b])
boom!
```


However it doesn't.


---

Comment by davidloeffler created at 2009-07-20 20:23:04

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-20 20:23:04

Changing assignee from was to davidloeffler.


---

Comment by robharron created at 2013-04-08 15:48:43

I just uploaded a patch that allows you to construct relative number field morphisms as above (the code simply wasn't written accept something like that). I just made it go recursively through the list you provide, so in a tower of fields, you only need to provide the images up to the point where your morphism is the identity.

I'll set this to needs review after I do a full doctest overnight (the number_field module passes all doctests).


---

Comment by robharron created at 2013-04-09 18:01:24

Changing status from new to needs_review.


---

Comment by fwclarke created at 2013-04-17 15:35:30

Changing status from needs_review to needs_work.


---

Comment by fwclarke created at 2013-04-17 15:35:30

This mostly works well.  I tried it on some cases where the relative 
degrees were different.  For example

```
sage: C.<z> = CyclotomicField(15)
sage: K = C.relativize(z^5 + 1, 'a'); K
Number Field in a0 with defining polynomial x^4 - a1*x^3 + (a1 - 1)*x^2 + x - a1 over its base field
sage: K.inject_variables()
Defining a0, a1
sage: L = C.relativize(z^4 + z, 'b'); L
Number Field in b0 with defining polynomial x^2 - b1*x - 1/2*b1^3 + b1^2 - b1 - 1/2 over its base field
sage: H = Hom(K, L)
sage: K.hom(map(H[2], K.gens()))
Relative number field morphism:
  From: Number Field in a0 with defining polynomial x^4 - a1*x^3 + (a1 - 1)*x^2 + x - a1 over its base field
  To:   Number Field in b0 with defining polynomial x^2 - b1*x - 1/2*b1^3 + b1^2 - b1 - 1/2 over its base field
  Defn: a0 |--> -b0 + b1
        a1 |--> -1/2*b1^3 + b1^2 - b1 + 1/2
```


My concerns are about when the default base homomorphism is used.  It is certainly not correct to describe `default_base_hom` as "trivial", and not clear anyway what that would mean if the domain and codomain differ.  Its docstring says 

  _Pick an embedding of the base field of self into the codomain of this homset.  This is done in an essentially arbitrary way._

Since the value is cached, see line 526 of `sage/rings/number_field/morphism.py` (after your patch is applied), using the default argument `base_hom=None` should always give the same restriction to the base_field.  However, continuing the above example,

``` 
sage: [K.hom([h(a0)])(a1) for h in H]
[-1/2*b1^3 + b1^2 - b1 + 1/2,
 1/2*b1^3 - b1^2 + b1 + 1/2,
 -1/2*b1^3 + b1^2 - b1 + 1/2,
 1/2*b1^3 - b1^2 + b1 + 1/2,
 -1/2*b1^3 + b1^2 - b1 + 1/2,
 1/2*b1^3 - b1^2 + b1 + 1/2,
 1/2*b1^3 - b1^2 + b1 + 1/2,
 -1/2*b1^3 + b1^2 - b1 + 1/2]
```


This happens because 
`sage.rings.number_field.morphism.RelativeNumberFieldHomset._from_im` doesn't do what it claims.  With again the same definitions:

```
sage: b0 = L.gen(); b1 = L.base_field().gen()
sage: base_hom = K.base_field().hom([1/2*b1^3 - b1^2 + b1 + 1/2]); base_hom
Ring morphism:
  From: Number Field in a1 with defining polynomial x^2 - x + 1
  To:   Number Field in b1 with defining polynomial x^4 - x^3 + 2*x^2 + x + 1
  Defn: a1 |--> 1/2*b1^3 - b1^2 + b1 + 1/2
sage: H._from_im([b0], base_hom)
Relative number field morphism:
  From: Number Field in a0 with defining polynomial x^4 - a1*x^3 + (a1 - 1)*x^2 + x - a1 over its base field
  To:   Number Field in b0 with defining polynomial x^2 - b1*x - 1/2*b1^3 + b1^2 - b1 - 1/2 over its base field
  Defn: a0 |--> b0
        a1 |--> -1/2*b1^3 + b1^2 - b1 + 1/2
```

which does not restrict to the base_field correctly.  I note that at present `_from_im` is not used anywhere else in Sage.  

In fact since

```
sage: K.absolute_generator()
a0
```

there is only one homomorphism from `K` to `L` that sends `a0` to `b0`, so an error should have been raised by `H._from_im([b0], base_hom)`.


---

Comment by robharron created at 2013-04-17 18:13:30

Nice catch. I've written a fix for _from_im and have mostly done writing up code that given a "short" list for im_gens attempts to find a base_hom that works. I'll upload it when I get that done.


---

Attachment


---

Comment by robharron created at 2013-04-18 18:58:09

Changing status from needs_work to needs_review.


---

Comment by robharron created at 2013-04-18 18:58:09

Alright, I've updated the patch. I added a check in _from_im for whether the morphism agrees with base_hom. And I added a new method _from_im_without_base_hom which is like _from_im, but attempts to find a base_hom compatible with the im_gen passed.


---

Comment by fwclarke created at 2013-04-23 18:14:34

This improves things significantly.  

But I'm not too happy about `_from_im` having the default `check=False`.  For all other constructors of homomorphisms, the `check` paramater has default `True`.  The idea being that other methods can set it as `False` in cases where checking has already been done; see #10843, which still needs reviewing (once it's rebased).

The real problem is that the present code for `_from_im` is mathematically incorrect.  Once a rigourous version is defined, it is possible to write `_from_im_without_base_hom` much more simply.

I attach a patch (to be applied after your latest patch) which implements these changes. In addition it rewrites `default_base_hom`, the point being that it is unnecessary to cache its output since caching is already done by `embeddings`.

There are some problems too with the docstring for `RelativeNumberFieldHomset.__call__`.  In particular, it is not true that "if the list specifies a morphism that maps the generators of the base fields to themselves, then truncating that list will yield the same morphism."  For example,

```
sage: K.<a,b,c> = NumberField([x^2 - 2, x^2 - 3, x^2 - 5])
sage: K.hom([-a, b, -c])
Relative number field endomorphism of Number Field in a with defining polynomial x^2 - 2 over its base field
  Defn: a |--> -a
        b |--> b
        c |--> -c
sage: K.hom([-a])
Relative number field endomorphism of Number Field in a with defining polynomial x^2 - 2 over its base field
  Defn: a |--> -a
        b |--> b
        c |--> c
```


I also think that there needs to be a warning that a homomorphism for which a partial list of generators is given may not be uniquely defined.  In
other words, the "essentially arbitrary" remarks in the docstrings for `_from_im_without_base_hom` and `default_base_hom` need promoting to this level.  Moreover the resulting modification to the syntax of `hom` for relative number fields needs to be directly available to users.  At the moment `K.hom?`, where `K` is a relative number field, yields the docstring for the generic `sage.structure.parent_gens.ParentWithGens.hom`.


---

Comment by fwclarke created at 2013-04-23 18:14:34

Changing status from needs_review to needs_work.


---

Attachment

To be applied on top of trac_4726_enhance_relative_number_morphism_constructor.patch
