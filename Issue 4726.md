# Issue 4726: Creating homomorphisms of relative number fields seems totally broken

archive/issues_004726.json:
```json
{
    "body": "Assignee: was\n\nCC:  lftabera\n\nThe following _should_ create the correct homomorphism (complex conjugation, see #4724):\n\n```\nsage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]\nsage: conj = K.hom([-j, b])\nboom!\n```\n\n\nHowever it doesn't.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4726\n\n",
    "created_at": "2008-12-06T18:41:24Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Creating homomorphisms of relative number fields seems totally broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4726",
    "user": "was"
}
```
Assignee: was

CC:  lftabera

The following _should_ create the correct homomorphism (complex conjugation, see #4724):

```
sage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]
sage: conj = K.hom([-j, b])
boom!
```


However it doesn't.

Issue created by migration from https://trac.sagemath.org/ticket/4726





---

archive/issue_comments_035676.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T20:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35676",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_035677.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-20T20:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35677",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_035678.json:
```json
{
    "body": "I just uploaded a patch that allows you to construct relative number field morphisms as above (the code simply wasn't written accept something like that). I just made it go recursively through the list you provide, so in a tower of fields, you only need to provide the images up to the point where your morphism is the identity.\n\nI'll set this to needs review after I do a full doctest overnight (the number_field module passes all doctests).",
    "created_at": "2013-04-08T15:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35678",
    "user": "robharron"
}
```

I just uploaded a patch that allows you to construct relative number field morphisms as above (the code simply wasn't written accept something like that). I just made it go recursively through the list you provide, so in a tower of fields, you only need to provide the images up to the point where your morphism is the identity.

I'll set this to needs review after I do a full doctest overnight (the number_field module passes all doctests).



---

archive/issue_comments_035679.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-09T18:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35679",
    "user": "robharron"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_035680.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-04-17T15:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35680",
    "user": "fwclarke"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_035681.json:
```json
{
    "body": "This mostly works well.  I tried it on some cases where the relative \ndegrees were different.  For example\n\n```\nsage: C.<z> = CyclotomicField(15)\nsage: K = C.relativize(z^5 + 1, 'a'); K\nNumber Field in a0 with defining polynomial x^4 - a1*x^3 + (a1 - 1)*x^2 + x - a1 over its base field\nsage: K.inject_variables()\nDefining a0, a1\nsage: L = C.relativize(z^4 + z, 'b'); L\nNumber Field in b0 with defining polynomial x^2 - b1*x - 1/2*b1^3 + b1^2 - b1 - 1/2 over its base field\nsage: H = Hom(K, L)\nsage: K.hom(map(H[2], K.gens()))\nRelative number field morphism:\n  From: Number Field in a0 with defining polynomial x^4 - a1*x^3 + (a1 - 1)*x^2 + x - a1 over its base field\n  To:   Number Field in b0 with defining polynomial x^2 - b1*x - 1/2*b1^3 + b1^2 - b1 - 1/2 over its base field\n  Defn: a0 |--> -b0 + b1\n        a1 |--> -1/2*b1^3 + b1^2 - b1 + 1/2\n```\n\n\nMy concerns are about when the default base homomorphism is used.  It is certainly not correct to describe `default_base_hom` as \"trivial\", and not clear anyway what that would mean if the domain and codomain differ.  Its docstring says \n\n  *Pick an embedding of the base field of self into the codomain of this homset.  This is done in an essentially arbitrary way.*\n\nSince the value is cached, see line 526 of `sage/rings/number_field/morphism.py` (after your patch is applied), using the default argument `base_hom=None` should always give the same restriction to the base_field.  However, continuing the above example,\n\n``` \nsage: [K.hom([h(a0)])(a1) for h in H]\n[-1/2*b1^3 + b1^2 - b1 + 1/2,\n 1/2*b1^3 - b1^2 + b1 + 1/2,\n -1/2*b1^3 + b1^2 - b1 + 1/2,\n 1/2*b1^3 - b1^2 + b1 + 1/2,\n -1/2*b1^3 + b1^2 - b1 + 1/2,\n 1/2*b1^3 - b1^2 + b1 + 1/2,\n 1/2*b1^3 - b1^2 + b1 + 1/2,\n -1/2*b1^3 + b1^2 - b1 + 1/2]\n```\n\n\nThis happens because \n`sage.rings.number_field.morphism.RelativeNumberFieldHomset._from_im` doesn't do what it claims.  With again the same definitions:\n\n```\nsage: b0 = L.gen(); b1 = L.base_field().gen()\nsage: base_hom = K.base_field().hom([1/2*b1^3 - b1^2 + b1 + 1/2]); base_hom\nRing morphism:\n  From: Number Field in a1 with defining polynomial x^2 - x + 1\n  To:   Number Field in b1 with defining polynomial x^4 - x^3 + 2*x^2 + x + 1\n  Defn: a1 |--> 1/2*b1^3 - b1^2 + b1 + 1/2\nsage: H._from_im([b0], base_hom)\nRelative number field morphism:\n  From: Number Field in a0 with defining polynomial x^4 - a1*x^3 + (a1 - 1)*x^2 + x - a1 over its base field\n  To:   Number Field in b0 with defining polynomial x^2 - b1*x - 1/2*b1^3 + b1^2 - b1 - 1/2 over its base field\n  Defn: a0 |--> b0\n        a1 |--> -1/2*b1^3 + b1^2 - b1 + 1/2\n```\n\nwhich does not restrict to the base_field correctly.  I note that at present `_from_im` is not used anywhere else in Sage.  \n\nIn fact since\n\n```\nsage: K.absolute_generator()\na0\n```\n\nthere is only one homomorphism from `K` to `L` that sends `a0` to `b0`, so an error should have been raised by `H._from_im([b0], base_hom)`.",
    "created_at": "2013-04-17T15:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35681",
    "user": "fwclarke"
}
```

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

  *Pick an embedding of the base field of self into the codomain of this homset.  This is done in an essentially arbitrary way.*

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

archive/issue_comments_035682.json:
```json
{
    "body": "Nice catch. I've written a fix for _from_im and have mostly done writing up code that given a \"short\" list for im_gens attempts to find a base_hom that works. I'll upload it when I get that done.",
    "created_at": "2013-04-17T18:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35682",
    "user": "robharron"
}
```

Nice catch. I've written a fix for _from_im and have mostly done writing up code that given a "short" list for im_gens attempts to find a base_hom that works. I'll upload it when I get that done.



---

archive/issue_comments_035683.json:
```json
{
    "body": "Attachment [trac_4726_enhance_relative_number_morphism_constructor.patch](tarball://root/attachments/some-uuid/ticket4726/trac_4726_enhance_relative_number_morphism_constructor.patch) by robharron created at 2013-04-18 18:55:50",
    "created_at": "2013-04-18T18:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35683",
    "user": "robharron"
}
```

Attachment [trac_4726_enhance_relative_number_morphism_constructor.patch](tarball://root/attachments/some-uuid/ticket4726/trac_4726_enhance_relative_number_morphism_constructor.patch) by robharron created at 2013-04-18 18:55:50



---

archive/issue_comments_035684.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-04-18T18:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35684",
    "user": "robharron"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_035685.json:
```json
{
    "body": "Alright, I've updated the patch. I added a check in _from_im for whether the morphism agrees with base_hom. And I added a new method _from_im_without_base_hom which is like _from_im, but attempts to find a base_hom compatible with the im_gen passed.",
    "created_at": "2013-04-18T18:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35685",
    "user": "robharron"
}
```

Alright, I've updated the patch. I added a check in _from_im for whether the morphism agrees with base_hom. And I added a new method _from_im_without_base_hom which is like _from_im, but attempts to find a base_hom compatible with the im_gen passed.



---

archive/issue_comments_035686.json:
```json
{
    "body": "This improves things significantly.  \n\nBut I'm not too happy about `_from_im` having the default `check=False`.  For all other constructors of homomorphisms, the `check` paramater has default `True`.  The idea being that other methods can set it as `False` in cases where checking has already been done; see #10843, which still needs reviewing (once it's rebased).\n\nThe real problem is that the present code for `_from_im` is mathematically incorrect.  Once a rigourous version is defined, it is possible to write `_from_im_without_base_hom` much more simply.\n\nI attach a patch (to be applied after your latest patch) which implements these changes. In addition it rewrites `default_base_hom`, the point being that it is unnecessary to cache its output since caching is already done by `embeddings`.\n\nThere are some problems too with the docstring for `RelativeNumberFieldHomset.__call__`.  In particular, it is not true that \"if the list specifies a morphism that maps the generators of the base fields to themselves, then truncating that list will yield the same morphism.\"  For example,\n\n```\nsage: K.<a,b,c> = NumberField([x^2 - 2, x^2 - 3, x^2 - 5])\nsage: K.hom([-a, b, -c])\nRelative number field endomorphism of Number Field in a with defining polynomial x^2 - 2 over its base field\n  Defn: a |--> -a\n        b |--> b\n        c |--> -c\nsage: K.hom([-a])\nRelative number field endomorphism of Number Field in a with defining polynomial x^2 - 2 over its base field\n  Defn: a |--> -a\n        b |--> b\n        c |--> c\n```\n\n\nI also think that there needs to be a warning that a homomorphism for which a partial list of generators is given may not be uniquely defined.  In\nother words, the \"essentially arbitrary\" remarks in the docstrings for `_from_im_without_base_hom` and `default_base_hom` need promoting to this level.  Moreover the resulting modification to the syntax of `hom` for relative number fields needs to be directly available to users.  At the moment `K.hom?`, where `K` is a relative number field, yields the docstring for the generic `sage.structure.parent_gens.ParentWithGens.hom`.",
    "created_at": "2013-04-23T18:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35686",
    "user": "fwclarke"
}
```

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

archive/issue_comments_035687.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-04-23T18:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35687",
    "user": "fwclarke"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_035688.json:
```json
{
    "body": "Attachment [trac_4726_reviewer.patch](tarball://root/attachments/some-uuid/ticket4726/trac_4726_reviewer.patch) by fwclarke created at 2013-04-23 18:15:46\n\nTo be applied on top of trac_4726_enhance_relative_number_morphism_constructor.patch",
    "created_at": "2013-04-23T18:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4726#issuecomment-35688",
    "user": "fwclarke"
}
```

Attachment [trac_4726_reviewer.patch](tarball://root/attachments/some-uuid/ticket4726/trac_4726_reviewer.patch) by fwclarke created at 2013-04-23 18:15:46

To be applied on top of trac_4726_enhance_relative_number_morphism_constructor.patch
