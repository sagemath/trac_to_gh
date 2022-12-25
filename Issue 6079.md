# Issue 6079: modernize base inclusion morphism of relative number fields

archive/issues_006079.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb @craigcitro @williamstein @mstreng\n\nKeywords: base inclusion morphism relative number field\n\nThe patch adds a class for the morphism embedding the base into a relative number field extension, and (much more useful) the partially defined section going back.\n\nIt also adds a verbose(level=4) stack trace whenever nfinit and rnfinit are called.  It's a huge pain trying to work around such calls without a mechanism to see them, so here it is.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6079\n\n",
    "created_at": "2009-05-19T02:18:22Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "modernize base inclusion morphism of relative number fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6079",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @robertwb @craigcitro @williamstein @mstreng

Keywords: base inclusion morphism relative number field

The patch adds a class for the morphism embedding the base into a relative number field extension, and (much more useful) the partially defined section going back.

It also adds a verbose(level=4) stack trace whenever nfinit and rnfinit are called.  It's a huge pain trying to work around such calls without a mechanism to see them, so here it is.

Issue created by migration from https://trac.sagemath.org/ticket/6079





---

archive/issue_comments_048290.json:
```json
{
    "body": "Attachment [trac_6079-base-inclusion-morphism.patch](tarball://root/attachments/some-uuid/ticket6079/trac_6079-base-inclusion-morphism.patch) by @ncalexan created at 2009-05-19 03:02:11\n\nSecond patch relies on first; might as well be on same ticket.  Adds a subfield_containing that tries to do a bit more than naive trial and error to find the smallest subfield of a number field containing the specified elements.",
    "created_at": "2009-05-19T03:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48290",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_6079-base-inclusion-morphism.patch](tarball://root/attachments/some-uuid/ticket6079/trac_6079-base-inclusion-morphism.patch) by @ncalexan created at 2009-05-19 03:02:11

Second patch relies on first; might as well be on same ticket.  Adds a subfield_containing that tries to do a bit more than naive trial and error to find the smallest subfield of a number field containing the specified elements.



---

archive/issue_comments_048291.json:
```json
{
    "body": "## Two comments\n\n\n1. I can see that \"Isomorphism map\" is clumsy in, for example,\n\n```\nIsomorphism map: \n  From: Number Field in a with defining polynomial x^6 - 3*x^5 + 6*x^4 - 11*x^3 + 12*x^2 + 3*x + 1 \n  To:   Number Field in cuberoot2 with defining polynomial x^3 - 2 over its base field \n```\n\nbut surely \"Isomorphism morphism\" is worse.  What's wrong with \"Isomorphism\"?\n\n2.  Why make `subfield_containing` a new function.  To my mind it would make more sense to allow `subfield` \nto take a list of elements, as well as a single element (as at present), as its second argument?",
    "created_at": "2009-05-19T06:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48291",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

## Two comments


1. I can see that "Isomorphism map" is clumsy in, for example,

```
Isomorphism map: 
  From: Number Field in a with defining polynomial x^6 - 3*x^5 + 6*x^4 - 11*x^3 + 12*x^2 + 3*x + 1 
  To:   Number Field in cuberoot2 with defining polynomial x^3 - 2 over its base field 
```

but surely "Isomorphism morphism" is worse.  What's wrong with "Isomorphism"?

2.  Why make `subfield_containing` a new function.  To my mind it would make more sense to allow `subfield` 
to take a list of elements, as well as a single element (as at present), as its second argument?



---

archive/issue_comments_048292.json:
```json
{
    "body": "For point 1, removing the \"map\" at the end is not hard but really isn't worth it.  Notice that I'm defining _repr_type_; it's the base class's _repr_ that's adding map/morphism.  Just not worth it.\n\nFor point 2, subfield and subfield_containing do not do the same thing.  subfield guarantees that your element is a generator of the returned field; subfield_containing does no such thing.  Also, subfield_containing is not yet implemented for relative fields, while subfield is (And, I think, would mean different things in that case.)  Finally, having a single element vs. list of elements option causes problems -- it's annoying to use with iterators, for example.  (Although I rule out using iterators precisely to catch errors when you give me a single element.)\n\nThanks for the quick review, can I have another?",
    "created_at": "2009-05-19T16:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48292",
    "user": "https://github.com/ncalexan"
}
```

For point 1, removing the "map" at the end is not hard but really isn't worth it.  Notice that I'm defining _repr_type_; it's the base class's _repr_ that's adding map/morphism.  Just not worth it.

For point 2, subfield and subfield_containing do not do the same thing.  subfield guarantees that your element is a generator of the returned field; subfield_containing does no such thing.  Also, subfield_containing is not yet implemented for relative fields, while subfield is (And, I think, would mean different things in that case.)  Finally, having a single element vs. list of elements option causes problems -- it's annoying to use with iterators, for example.  (Although I rule out using iterators precisely to catch errors when you give me a single element.)

Thanks for the quick review, can I have another?



---

archive/issue_comments_048293.json:
```json
{
    "body": "Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.\n\nThe first patch should still be good.",
    "created_at": "2009-05-19T23:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48293",
    "user": "https://github.com/ncalexan"
}
```

Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.

The first patch should still be good.



---

archive/issue_comments_048294.json:
```json
{
    "body": "Replying to [comment:6 ncalexan]:\n> Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.\n\nI would have thought that the simplest way to implement the function would be by a recursive use of `relativize`.  **Except** this function does not, in my opinion, work correctly with relative extensions.  If L/K is a relative extensions, and alpha is in L, then `L.relativize(alpha, 'alpha') returns the relative extension L/QQ(alpha).  I think it would be much more useful if it returned L/K(alpha).  This should be easy to fix, and then `subfields_containing` would follow, including the relative case.\n\nSome other remarks :\n\nI take the point about the difference between `subfield` and \n`subfield_containing` (I didn't read carefully enough), but there needs to be a reference to the latter in \nthe documentation for the former.\n\nHowever the function is implemented, `K.subfields_containing([a], 'b')[:2]` and \n`K.subfield(a, 'b')` should give the same answer.\n\nIt should be possible to leave the name out as in\n\n```\nsage: C.<z> = CyclotomicField(20)\nsage: C.subfield(z^4)\n(Number Field in z0 with defining polynomial x^4 + x^3 + x^2 + x + 1,\n Ring morphism:\n  From: Number Field in z0 with defining polynomial x^4 + x^3 + x^2 + x + 1\n  To:   Cyclotomic Field of order 20 and degree 8\n  Defn: z0 |--> z^4)\n```\n\n\nI suggest there's a doctest looking like\n\n```\nsage: D.<u>, phi, alphas = C.subfield_containing([z^4, z^6])\nsage: alphas\n(1/4*u2^2, 1/8*u2^3)\nsage: phi\nsage: map(phi, alphas)\n[z^4, z^6]\n```\n\nBut, at present,\n\n```\nsage: u\nu2\n```\n\nwhich can't be right.\n\nI note that the corresponding\n\n```\nsage: D.<w>, phi = C.subfield(z^4)\n```\n\nfails because the variable name in `subfield` is `name` rather than `names`.  \nI'll open a ticket for this.",
    "created_at": "2009-05-20T06:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48294",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:6 ncalexan]:
> Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.

I would have thought that the simplest way to implement the function would be by a recursive use of `relativize`.  **Except** this function does not, in my opinion, work correctly with relative extensions.  If L/K is a relative extensions, and alpha is in L, then `L.relativize(alpha, 'alpha') returns the relative extension L/QQ(alpha).  I think it would be much more useful if it returned L/K(alpha).  This should be easy to fix, and then `subfields_containing` would follow, including the relative case.

Some other remarks :

I take the point about the difference between `subfield` and 
`subfield_containing` (I didn't read carefully enough), but there needs to be a reference to the latter in 
the documentation for the former.

However the function is implemented, `K.subfields_containing([a], 'b')[:2]` and 
`K.subfield(a, 'b')` should give the same answer.

It should be possible to leave the name out as in

```
sage: C.<z> = CyclotomicField(20)
sage: C.subfield(z^4)
(Number Field in z0 with defining polynomial x^4 + x^3 + x^2 + x + 1,
 Ring morphism:
  From: Number Field in z0 with defining polynomial x^4 + x^3 + x^2 + x + 1
  To:   Cyclotomic Field of order 20 and degree 8
  Defn: z0 |--> z^4)
```


I suggest there's a doctest looking like

```
sage: D.<u>, phi, alphas = C.subfield_containing([z^4, z^6])
sage: alphas
(1/4*u2^2, 1/8*u2^3)
sage: phi
sage: map(phi, alphas)
[z^4, z^6]
```

But, at present,

```
sage: u
u2
```

which can't be right.

I note that the corresponding

```
sage: D.<w>, phi = C.subfield(z^4)
```

fails because the variable name in `subfield` is `name` rather than `names`.  
I'll open a ticket for this.



---

archive/issue_comments_048295.json:
```json
{
    "body": "I'm withdrawing the second patch for the time being (even though the uniqueness problem was wrong -- it was unique, I was confused).  All of these comments seem to be about the second patch; if that's true, can we just review the first patch?  I've responded to your comments anyway.\n\nReplying to [comment:7 fwclarke]:\n> Replying to [comment:6 ncalexan]:\n> > Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.\n> \n> I would have thought that the simplest way to implement the function would be by a recursive use of `relativize`.\n\nSo did I.  After trying to do a recursive relativize, I came to this.  (I found this method to work a lot better, but that was before my patches making relativize work quickly were in place.)\n\n  **Except** this function does not, in my opinion, work correctly with relative extensions.  If L/K is a relative extensions, and alpha is in L, then `L.relativize(alpha, 'alpha') returns the relative extension L/QQ(alpha).  I think it would be much more useful if it returned L/K(alpha).  This should be easy to fix, and then `subfields_containing` would follow, including the relative case.\n\nLook, this is just not what relativize does:\n\n```\n        Given an element in self or an embedding of a subfield into self,\n        return a relative number field $K$ isomorphic to self that is relative\n        over the absolute field $\\QQ(\\alpha)$ or the domain of $alpha$, along\n        with isomorphisms from $K$ to self and from self to K.\n```\n\nThis behaviour was in place before I started improving it; I'm not averse to changing it, but then we have to deprecate and add new names, etc.  That's what I'm doing -- adding new names for new functionality.\n\n> \n> Some other remarks :\n> \n> I take the point about the difference between `subfield` and \n> `subfield_containing` (I didn't read carefully enough), but there needs to be a reference to the latter in \n> the documentation for the former.\n\nFine.\n \n> However the function is implemented, `K.subfields_containing([a], 'b')[:2]` and \n> `K.subfield(a, 'b')` should give the same answer.\n\nThey don't do the same thing.  If you want to make them do the same thing, that could be done.  But nowhere do I claim that they do the same thing.\n\n> It should be possible to leave the name out as in\n\nNope -- explicit is always the way in Sage.\n\n> {{{\n> sage: C.<z> = CyclotomicField(20)\n> sage: C.subfield(z^4)\n> (Number Field in z0 with defining polynomial x^4 + x^3 + x^2 + x + 1,\n>  Ring morphism:\n>   From: Number Field in z0 with defining polynomial x^4 + x^3 + x^2 + x + 1\n>   To:   Cyclotomic Field of order 20 and degree 8\n>   Defn: z0 |--> z^4)\n> }}}\n> \n> I suggest there's a doctest looking like\n> {{{\n> sage: D.<u>, phi, alphas = C.subfield_containing([z^4, z^6])\n> sage: alphas\n> (1/4*u2^2, 1/8*u2^3)\n> sage: phi\n> sage: map(phi, alphas)\n> [z^4, z^6]\n\nThere are -- several.\n\n> }}}\n> But, at present,\n> {{{\n> sage: u\n> u2\n> }}}\n> which can't be right.\n\nWell, maybe.  Look at subfields and several of the other functions which take a name parameter -- it doesn't mean what you think it means.  It's annoying, and I'd like it to be fixed, but that's not the subject of this patch.\n\n> I note that the corresponding\n> {{{\n> sage: D.<w>, phi = C.subfield(z^4)\n> }}}\n> fails because the variable name in `subfield` is `name` rather than `names`.  \n> I'll open a ticket for this.\n\nPlease do.",
    "created_at": "2009-05-20T06:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48295",
    "user": "https://github.com/ncalexan"
}
```

I'm withdrawing the second patch for the time being (even though the uniqueness problem was wrong -- it was unique, I was confused).  All of these comments seem to be about the second patch; if that's true, can we just review the first patch?  I've responded to your comments anyway.

Replying to [comment:7 fwclarke]:
> Replying to [comment:6 ncalexan]:
> > Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.
> 
> I would have thought that the simplest way to implement the function would be by a recursive use of `relativize`.

So did I.  After trying to do a recursive relativize, I came to this.  (I found this method to work a lot better, but that was before my patches making relativize work quickly were in place.)

  **Except** this function does not, in my opinion, work correctly with relative extensions.  If L/K is a relative extensions, and alpha is in L, then `L.relativize(alpha, 'alpha') returns the relative extension L/QQ(alpha).  I think it would be much more useful if it returned L/K(alpha).  This should be easy to fix, and then `subfields_containing` would follow, including the relative case.

Look, this is just not what relativize does:

```
        Given an element in self or an embedding of a subfield into self,
        return a relative number field $K$ isomorphic to self that is relative
        over the absolute field $\QQ(\alpha)$ or the domain of $alpha$, along
        with isomorphisms from $K$ to self and from self to K.
```

This behaviour was in place before I started improving it; I'm not averse to changing it, but then we have to deprecate and add new names, etc.  That's what I'm doing -- adding new names for new functionality.

> 
> Some other remarks :
> 
> I take the point about the difference between `subfield` and 
> `subfield_containing` (I didn't read carefully enough), but there needs to be a reference to the latter in 
> the documentation for the former.

Fine.
 
> However the function is implemented, `K.subfields_containing([a], 'b')[:2]` and 
> `K.subfield(a, 'b')` should give the same answer.

They don't do the same thing.  If you want to make them do the same thing, that could be done.  But nowhere do I claim that they do the same thing.

> It should be possible to leave the name out as in

Nope -- explicit is always the way in Sage.

> {{{
> sage: C.<z> = CyclotomicField(20)
> sage: C.subfield(z^4)
> (Number Field in z0 with defining polynomial x^4 + x^3 + x^2 + x + 1,
>  Ring morphism:
>   From: Number Field in z0 with defining polynomial x^4 + x^3 + x^2 + x + 1
>   To:   Cyclotomic Field of order 20 and degree 8
>   Defn: z0 |--> z^4)
> }}}
> 
> I suggest there's a doctest looking like
> {{{
> sage: D.<u>, phi, alphas = C.subfield_containing([z^4, z^6])
> sage: alphas
> (1/4*u2^2, 1/8*u2^3)
> sage: phi
> sage: map(phi, alphas)
> [z^4, z^6]

There are -- several.

> }}}
> But, at present,
> {{{
> sage: u
> u2
> }}}
> which can't be right.

Well, maybe.  Look at subfields and several of the other functions which take a name parameter -- it doesn't mean what you think it means.  It's annoying, and I'd like it to be fixed, but that's not the subject of this patch.

> I note that the corresponding
> {{{
> sage: D.<w>, phi = C.subfield(z^4)
> }}}
> fails because the variable name in `subfield` is `name` rather than `names`.  
> I'll open a ticket for this.

Please do.



---

archive/issue_comments_048296.json:
```json
{
    "body": "I've made a new ticket, #6092, for discussing the second part of this patch.  I'd really like to get the first part merged before it rots, but it seems clear that the second part needs work.",
    "created_at": "2009-05-20T07:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48296",
    "user": "https://github.com/ncalexan"
}
```

I've made a new ticket, #6092, for discussing the second part of this patch.  I'd really like to get the first part merged before it rots, but it seems clear that the second part needs work.



---

archive/issue_comments_048297.json:
```json
{
    "body": "Nick: I deleted trac_6079-subfield-containing.patch from this trac ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T11:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nick: I deleted trac_6079-subfield-containing.patch from this trac ticket.

Cheers,

Michael



---

archive/issue_comments_048298.json:
```json
{
    "body": "Some remarks about `recognize_in_subfield` \nThe function works fine for absolute fields and some \nrelative cases.  But\n\n```\nsage: L.<a0, b0> = NumberField([x^4 + 2, x^4 + 3])\nsage: K.<c> = NumberField(x^2 + 3)\nsage: psi = K.embeddings(L)[0]\nsage: psi(c)\nb0^2\nsage: L.recognize_in_subfield([2*b0^2 + 3])\nTraceback (most recent call last)\n...\nTypeError: unsupported operand parent(s) for '*': \n'Full MatrixSpace of 1 by 2 dense matrices over Number Field in b0 with defining polynomial x^4 + 3' \nand 'Vector space of dimension 2 over Number Field in c with defining polynomial x^2 + 3'\n```\n\nI believe that this is solved by the following revision:\n\n```\n    def recognize_in_subfield(self, K_into_self, elements_of_self):\n        V, _, self_into_V = self.absolute_vector_space()\n        K = K_into_self.domain()\n        U, U_into_K, _ = K.absolute_vector_space()\n        M = matrix(map(self_into_V * K_into_self * U_into_K, U.basis()))\n        es = matrix([ self_into_V(e) for e in elements_of_self ])\n        try:\n            vs = M.solve_left(es)\n        except:\n            raise ValueError, \"Not all elements are in subfield\"\n        return map(U_into_K, vs * U.basis())\n```\n\nso that, for example, the following works\n\n```\nsage: PQ.<X> = QQ[]\nsage: F.<a, b> = NumberField([X^2 - 2, X^2 - 3])\nsage: K.<c> = F.extension(Y^2 - (1 + a)*(a + b)*a*b)\nsage: phi = F.embeddings(K)[2]; phi\nRelative number field morphism:\n  From: Number Field in a with defining polynomial X^2 - 2 over its base field\n  To:   Number Field in c with defining polynomial Y^2 + (-2*b - 3)*a - 2*b - 6 over its base field\n  Defn: a |--> -a\n        b |--> b\nsage: K.recognize_in_subfield(phi, [a, b])\n[-a, b]\n```\n\n\nAnother issue: `recognize_in_subfield` is a useful function, but I\ndon't think it should be defined to apply to a *list* of elements.  Conceptually\nit is a function of a single element (and an inclusion), and the error\nmessage \"Not all elements are in subfield\" is particularly unhelpful.  I\nknow that since it uses linear algebra it is quicker to solve a list\nall at once than one by one, but it's rather unlikely that this function is\never going to be used for a particularly large list, and a user for\nwhom speed was crucial could easily write an alternative.\n\nI found the doctests for this function rather too technical, and too long\n(in `number_field.py` only `NumberField` and `composite_fields` have longer\ndoctests).  A user who'd not used this function would suffer information\noverload (129 lines of doctest).  In particular, I don't understand the\nfirst example at all.  What is the section `n` doing there?\n\nI would start off with a simple example (which as written depends \non the patch in #6091) like:\n\n```\nsage: L.<z> = NumberField(x^4 + 10*x^2 + 1)\nsage: K.<a>, phi = L.subfield(z^3 + 11*z)\nsage: L.recognize_in_subfield(phi, [3*z^3 + 33*z + 7])\n(3*a + 7)\nsage: phi(3*a + 7)\n3*z^3 + 33*z + 7\nsage: L.recognize_in_subfield(phi, [z^2])\nTraceback (most recent call last):\n...\nValueError: Not all elements are in subfield\n```\n\nThough, as I said, think I think the two applications of the function\nshould read:\n\n```\nsage: L.recognize_in_subfield(phi, 3*z^3 + 33*z + 7)\n3*a + 7\n```\n\nand\n\n```\nsage: L.recognize_in_subfield(phi, z^2)\nTraceback (most recent call last):\n...\nValueError: z^2 is not in the image of\nRing morphism:\n  From: Number Field in a with defining polynomial x^2 + 12\n  To:   Number Field in z with defining polynomial x^4 + 10*x^2 + 1\n  Defn: a |--> z^3 + 11*z\n```\n\nAnd then include a few more variants.",
    "created_at": "2009-05-22T07:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48298",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Some remarks about `recognize_in_subfield` 
The function works fine for absolute fields and some 
relative cases.  But

```
sage: L.<a0, b0> = NumberField([x^4 + 2, x^4 + 3])
sage: K.<c> = NumberField(x^2 + 3)
sage: psi = K.embeddings(L)[0]
sage: psi(c)
b0^2
sage: L.recognize_in_subfield([2*b0^2 + 3])
Traceback (most recent call last)
...
TypeError: unsupported operand parent(s) for '*': 
'Full MatrixSpace of 1 by 2 dense matrices over Number Field in b0 with defining polynomial x^4 + 3' 
and 'Vector space of dimension 2 over Number Field in c with defining polynomial x^2 + 3'
```

I believe that this is solved by the following revision:

```
    def recognize_in_subfield(self, K_into_self, elements_of_self):
        V, _, self_into_V = self.absolute_vector_space()
        K = K_into_self.domain()
        U, U_into_K, _ = K.absolute_vector_space()
        M = matrix(map(self_into_V * K_into_self * U_into_K, U.basis()))
        es = matrix([ self_into_V(e) for e in elements_of_self ])
        try:
            vs = M.solve_left(es)
        except:
            raise ValueError, "Not all elements are in subfield"
        return map(U_into_K, vs * U.basis())
```

so that, for example, the following works

```
sage: PQ.<X> = QQ[]
sage: F.<a, b> = NumberField([X^2 - 2, X^2 - 3])
sage: K.<c> = F.extension(Y^2 - (1 + a)*(a + b)*a*b)
sage: phi = F.embeddings(K)[2]; phi
Relative number field morphism:
  From: Number Field in a with defining polynomial X^2 - 2 over its base field
  To:   Number Field in c with defining polynomial Y^2 + (-2*b - 3)*a - 2*b - 6 over its base field
  Defn: a |--> -a
        b |--> b
sage: K.recognize_in_subfield(phi, [a, b])
[-a, b]
```


Another issue: `recognize_in_subfield` is a useful function, but I
don't think it should be defined to apply to a *list* of elements.  Conceptually
it is a function of a single element (and an inclusion), and the error
message "Not all elements are in subfield" is particularly unhelpful.  I
know that since it uses linear algebra it is quicker to solve a list
all at once than one by one, but it's rather unlikely that this function is
ever going to be used for a particularly large list, and a user for
whom speed was crucial could easily write an alternative.

I found the doctests for this function rather too technical, and too long
(in `number_field.py` only `NumberField` and `composite_fields` have longer
doctests).  A user who'd not used this function would suffer information
overload (129 lines of doctest).  In particular, I don't understand the
first example at all.  What is the section `n` doing there?

I would start off with a simple example (which as written depends 
on the patch in #6091) like:

```
sage: L.<z> = NumberField(x^4 + 10*x^2 + 1)
sage: K.<a>, phi = L.subfield(z^3 + 11*z)
sage: L.recognize_in_subfield(phi, [3*z^3 + 33*z + 7])
(3*a + 7)
sage: phi(3*a + 7)
3*z^3 + 33*z + 7
sage: L.recognize_in_subfield(phi, [z^2])
Traceback (most recent call last):
...
ValueError: Not all elements are in subfield
```

Though, as I said, think I think the two applications of the function
should read:

```
sage: L.recognize_in_subfield(phi, 3*z^3 + 33*z + 7)
3*a + 7
```

and

```
sage: L.recognize_in_subfield(phi, z^2)
Traceback (most recent call last):
...
ValueError: z^2 is not in the image of
Ring morphism:
  From: Number Field in a with defining polynomial x^2 + 12
  To:   Number Field in z with defining polynomial x^4 + 10*x^2 + 1
  Defn: a |--> z^3 + 11*z
```

And then include a few more variants.



---

archive/issue_comments_048299.json:
```json
{
    "body": "> I found the doctests for this function rather too technical, and too long\n> (in `number_field.py` only `NumberField` and `composite_fields` have longer\n> doctests).  A user who'd not used this function would suffer information\n> overload (129 lines of doctest).  In particular, I don't understand the\n> first example at all.  What is the section `n` doing there?\n\nI love that you're reviewing this and obviously putting in a lot of time -- thank you -- but it's as if you're not reading what's written.  The docstring explicitly says that if you're looking for the functionality that you want to reduce this function to, that section is how to get it.  And then it shows you what the differences are, including how the error message is more to your liking!\n\n\n```\n If you want a map that takes elements of ``self`` and returns elements \n \t4285\t        of a subfield, try the following: \n \t4286\t \n \t4287\t        EXAMPLES:: \n \t4288\t \n \t4289\t            sage: K.<a, b> = NumberField([x^3 + x + 1, x^2 + 100]) \n \t4290\t            sage: m = K.coerce_map_from(K.base_field()); n = m.section(); n \n \t4291\t            Projection onto base field map: \n \t4292\t              From: Number Field in a with defining polynomial x^3 + x + 1 over its base field \n \t4293\t              To:   Number Field in b with defining polynomial x^2 + 100 \n \t4294\t            sage: m(a^3 + a) \n \t4295\t            -1 \n \t4296\t            sage: K.recognize_in_subfield(m, [a^3 + a]) \n \t4297\t            (-1) \n \t4298\t \n \t4299\t            sage: m(a^2) \n \t4300\t            Traceback (most recent call last): \n \t4301\t            ... \n \t4302\t            TypeError: a^2 must be coercible into Number Field in b with defining polynomial x^2 + 100 \n \t4303\t \n \t4304\t            sage: K.recognize_in_subfield(m, [a^2]) \n \t4305\t            Traceback (most recent call last): \n \t4306\t            ... \n \t4307\t            ValueError: Not all elements are in subfield\n```\n\n\nI would be happy to move lots of EXAMPLES:: to TESTS::.  But this is a tricky function -- even with me doctesting this in tons of situations, of large degree, varying numbers of elements, etc, relative extensions -- even with all that, you claim to have found a bug.  So removing doctests?  Each one of which I have written to test a different situation?  That's crazy.\n\nWhy don't we rename `recognize_in_subfield` to `_recognize_many_in_subfield` and add a `recognize_in_subfield` with a simpler docstring that does the list wrapping.  But please, I am the user who needs to recognize many elements in a subfield so I want that functionality to be available.",
    "created_at": "2009-05-22T14:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48299",
    "user": "https://github.com/ncalexan"
}
```

> I found the doctests for this function rather too technical, and too long
> (in `number_field.py` only `NumberField` and `composite_fields` have longer
> doctests).  A user who'd not used this function would suffer information
> overload (129 lines of doctest).  In particular, I don't understand the
> first example at all.  What is the section `n` doing there?

I love that you're reviewing this and obviously putting in a lot of time -- thank you -- but it's as if you're not reading what's written.  The docstring explicitly says that if you're looking for the functionality that you want to reduce this function to, that section is how to get it.  And then it shows you what the differences are, including how the error message is more to your liking!


```
 If you want a map that takes elements of ``self`` and returns elements 
 	4285	        of a subfield, try the following: 
 	4286	 
 	4287	        EXAMPLES:: 
 	4288	 
 	4289	            sage: K.<a, b> = NumberField([x^3 + x + 1, x^2 + 100]) 
 	4290	            sage: m = K.coerce_map_from(K.base_field()); n = m.section(); n 
 	4291	            Projection onto base field map: 
 	4292	              From: Number Field in a with defining polynomial x^3 + x + 1 over its base field 
 	4293	              To:   Number Field in b with defining polynomial x^2 + 100 
 	4294	            sage: m(a^3 + a) 
 	4295	            -1 
 	4296	            sage: K.recognize_in_subfield(m, [a^3 + a]) 
 	4297	            (-1) 
 	4298	 
 	4299	            sage: m(a^2) 
 	4300	            Traceback (most recent call last): 
 	4301	            ... 
 	4302	            TypeError: a^2 must be coercible into Number Field in b with defining polynomial x^2 + 100 
 	4303	 
 	4304	            sage: K.recognize_in_subfield(m, [a^2]) 
 	4305	            Traceback (most recent call last): 
 	4306	            ... 
 	4307	            ValueError: Not all elements are in subfield
```


I would be happy to move lots of EXAMPLES:: to TESTS::.  But this is a tricky function -- even with me doctesting this in tons of situations, of large degree, varying numbers of elements, etc, relative extensions -- even with all that, you claim to have found a bug.  So removing doctests?  Each one of which I have written to test a different situation?  That's crazy.

Why don't we rename `recognize_in_subfield` to `_recognize_many_in_subfield` and add a `recognize_in_subfield` with a simpler docstring that does the list wrapping.  But please, I am the user who needs to recognize many elements in a subfield so I want that functionality to be available.



---

archive/issue_comments_048300.json:
```json
{
    "body": "Replying to [comment:12 ncalexan]:\n\n> it's as if you're not reading what's written.  The docstring explicitly says that if you're looking for the functionality that you want to reduce this function to, that section is how to get it.  And then it shows you what the differences are, including how the error message is more to your liking!\n\nI don't know what you mean by \"the functionality that you want to reduce this function to\" .  I didn't really want to change the functionality (apart from allowing single elements).\n\nI had read your first doctest, but\n\n1.  I couldn't see why you should start with a non-standard, slightly complicated instance of the function's use, followed by how to get the same answer a different way using \"exotic\" means, i.e., `coerce_map_from` and `section` (exotic anyway from the point of view of a number theorist who knows little about how SAGE works).\n\n2.  This first test is specifically about the base field as subfield, in some sense the only *genuine* subfield there is (along, I suppose, with its base field, and so on).  For SAGE's subfields, as given by the `subfield` and `subfields` functions, are just a field with a embedding (so also created by the `embeddings` function).\n\n3. AHAH! I see now that there must be a typo.  Where you wrote `m(a^3 + a)` and `m(a^2)`, you surely meant `n(a^3 + a)` and `n(a^2)` (and for the latter the error message is different).\n\n4. This way of getting an element into the base_field (if it's possible) is entirely unnecessary.  In your example:\n\n```\nsage: K.<a, b> = NumberField([x^3 + x + 1, x^2 + 100])\nsage: a^3 + a\n-1\n```\n\nso\n\n```\nsage: a^3 + a in K.base_field()\nTrue\n```\n\nwhile\n\n```\nsage: a^2 in K.base_field()\nFalse\n```\n\n\nCertainly we have\n\n```\nsage: z = a^3 + a\nsage: z.parent() == K\nTrue\n```\n\nBut if we want to think of `z` as an element of the base field, then we can convert it:\n\n```\nsage: w = K.base_field()(z)\nsage: w.parent()\nNumber Field in b with defining polynomial x^2 + 100\n```\n\nBut coercion means that we shouldn't usually need to do this.  For example\n\n```\nsage: K.base_field().gen() + z\nb - 1\n```\n\n\n> I would be happy to move lots of EXAMPLES:: to TESTS::.  But this is a tricky function -- even with me doctesting this in tons of situations, of large degree, varying numbers of elements, etc, relative extensions -- even with all that, you claim to have found a bug.  So removing doctests?  Each one of which I have written to test a different situation?  That's crazy.\n\nI don't think that in essence it is so tricky.  Once the problem is converted to linear algebra, using the `absolute_vector_space` function (which is hopefully sufficiently doctested), it's relatively straightforward.  Certainly the doctests need to contain a variety of cases, but I don't see why in your second example you need to run through *all* the quadratic subfields of `L`.  And what's the point of a random test with such a long output?\n\n> Why don't we rename `recognize_in_subfield` to `_recognize_many_in_subfield` and add a `recognize_in_subfield` with a simpler docstring that does the list wrapping.  But please, I am the user who needs to recognize many elements in a subfield so I want that functionality to be available.\n\nThis seems sensible.  But I don't actually see what's wrong with allowing *either* a single element *or* a list (as does `NumberField`).  Just have\n\n```\n        if not isinstance(elements_of_self, (list, tuple)):\n            elements_of_self = [elements_of_self]\n```\n\nat the beginning of the code and then at the end something like\n\n```\n        if len(answer) == 1:\n            answer = answer[0]\n        return answer\n```\n\n\nI'll try to look the rest of the patch tomorrow.",
    "created_at": "2009-05-22T19:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48300",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Replying to [comment:12 ncalexan]:

> it's as if you're not reading what's written.  The docstring explicitly says that if you're looking for the functionality that you want to reduce this function to, that section is how to get it.  And then it shows you what the differences are, including how the error message is more to your liking!

I don't know what you mean by "the functionality that you want to reduce this function to" .  I didn't really want to change the functionality (apart from allowing single elements).

I had read your first doctest, but

1.  I couldn't see why you should start with a non-standard, slightly complicated instance of the function's use, followed by how to get the same answer a different way using "exotic" means, i.e., `coerce_map_from` and `section` (exotic anyway from the point of view of a number theorist who knows little about how SAGE works).

2.  This first test is specifically about the base field as subfield, in some sense the only *genuine* subfield there is (along, I suppose, with its base field, and so on).  For SAGE's subfields, as given by the `subfield` and `subfields` functions, are just a field with a embedding (so also created by the `embeddings` function).

3. AHAH! I see now that there must be a typo.  Where you wrote `m(a^3 + a)` and `m(a^2)`, you surely meant `n(a^3 + a)` and `n(a^2)` (and for the latter the error message is different).

4. This way of getting an element into the base_field (if it's possible) is entirely unnecessary.  In your example:

```
sage: K.<a, b> = NumberField([x^3 + x + 1, x^2 + 100])
sage: a^3 + a
-1
```

so

```
sage: a^3 + a in K.base_field()
True
```

while

```
sage: a^2 in K.base_field()
False
```


Certainly we have

```
sage: z = a^3 + a
sage: z.parent() == K
True
```

But if we want to think of `z` as an element of the base field, then we can convert it:

```
sage: w = K.base_field()(z)
sage: w.parent()
Number Field in b with defining polynomial x^2 + 100
```

But coercion means that we shouldn't usually need to do this.  For example

```
sage: K.base_field().gen() + z
b - 1
```


> I would be happy to move lots of EXAMPLES:: to TESTS::.  But this is a tricky function -- even with me doctesting this in tons of situations, of large degree, varying numbers of elements, etc, relative extensions -- even with all that, you claim to have found a bug.  So removing doctests?  Each one of which I have written to test a different situation?  That's crazy.

I don't think that in essence it is so tricky.  Once the problem is converted to linear algebra, using the `absolute_vector_space` function (which is hopefully sufficiently doctested), it's relatively straightforward.  Certainly the doctests need to contain a variety of cases, but I don't see why in your second example you need to run through *all* the quadratic subfields of `L`.  And what's the point of a random test with such a long output?

> Why don't we rename `recognize_in_subfield` to `_recognize_many_in_subfield` and add a `recognize_in_subfield` with a simpler docstring that does the list wrapping.  But please, I am the user who needs to recognize many elements in a subfield so I want that functionality to be available.

This seems sensible.  But I don't actually see what's wrong with allowing *either* a single element *or* a list (as does `NumberField`).  Just have

```
        if not isinstance(elements_of_self, (list, tuple)):
            elements_of_self = [elements_of_self]
```

at the beginning of the code and then at the end something like

```
        if len(answer) == 1:
            answer = answer[0]
        return answer
```


I'll try to look the rest of the patch tomorrow.



---

archive/issue_comments_048301.json:
```json
{
    "body": "## More remarks\n\nThe verbose stack trace is certainly very useful.  I expect to make \nfrequent use of it.  I suggest that corresponding code is added to \n`pari_bnf`.\n\n----\n\nOn my earlier remarks about \"Isomorphism morphism\":  Having understood \nbetter the way that `repr(f)` is constructed for a number field  embedding \n`f`, I realise that making `f` a `Morphism` rather than a `Map` *is* an \nimprovement; the terminology is much more appropriate.  \nThe awkardness of \"Isomorphism morphism\" is caused by an\nearlier decision to make the `_repr_type` of an embedding \"Isomorphism\".  \nThis is distinctly out of line with the other values of `_repr_type` in \nSAGE:\n\n`Abelian variety`, `AbelianGroup`, `Affine`, `Affine Scheme`, \n`Affine Space`, `Call`, `Coercion`, `Composite`, `Conversion via ...`, `Generic`,\n`Identity`, `Identity map`, `MatrixGroup`, `Native`, `Natural`,\n`PermutationGroup`, `Projective Space`, `Projective`, `Quartic`,\n`Relative number field`, `Ring`, `Ring Coercion`, `Scheme`, `Section`,\n`Set-theoretic ring`, `Steal`.\n\n\nI note also that embeddings, the maps produced by `subfield` and `subfields`, automorphisms and\nelements of `Hom(K, L)` or `End(K, K)`  are all printed as \"Ring morphisms:\n...\"  or \"Ring endomorphisms ...\".  On the other hand, the maps given by\n`K.absolute_field('a').structure()` are given, after your patch, as \"Isomorphism morphism:\n...\"\n\n\nThis certainly needs sorting out at some point (as do other aspects of\nthe naming of morphisms), but it's not a matter for this patch.  \n\n----\n\nThe most important aspect, in my opinion, of your \n`NumberFieldBaseIntoExtensionMorphism` and \n`NumberFieldExtensionOntoBaseMap` code is that it allows the following \nusage:\n\n```\nsage: k.<a, b> = NumberField([x^2 + x + 1, x^3 - 2])\nsage: B = k.base_field(); B\nNumber Field in b with defining polynomial x^3 - 2\nsage: (b, parent(b))\n(b, Number Field in a with defining polynomial x^2 + x + 1 over its base field)\nsage: z = B(b)\nsage: z, parent(z)\n(b, Number Field in b with defining polynomial x^3 - 2)\n```\n\nIn 3.4.2 the `B(b)` conversion fails. \n\nThis feature is quite useful.  For example\n\n```\nsage: (b.norm(), B(b).norm())\n(4, 2)\n```\n\n\n\nBut one has to be careful.  If the field `k` above is constructed in a \ndifferent way, the element `b` has a different parent, and your code is \nnot needed for the conversions:\n\n```\nsage: B.<b> = NumberField(x^3 - 2)\nsage: k.<a> = B.extension(x^2 + x + 1)\nsage: parent(b)\nNumber Field in b with defining polynomial x^3 - 2\nsage: b.norm()\n2\nsage: k(b).norm()\n4\n```\n\n\n\nI think some, at least, of the doctests \nshould use the above conversion syntax, rather than expressions like\n`K.coerce_map_from(K.base_field()).section()` which are, of course, what \nis used to do conversions like `B(b)` above.  There are two reasons for  \nthis: (i) users should be made aware of this simple conversion syntax; \n(ii) it ensures that any future change to the coercion mechanism which \nwould mess up this case gets detected.\n\n\nI can't see any reason why one should want take a section of the partial\nmap from a field to its base field, but perhaps I'm missing something.\n\n\nI agree that it would be rather tricky to fix the parent of sections given \nthe way the Section class is defined.",
    "created_at": "2009-05-25T12:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48301",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

## More remarks

The verbose stack trace is certainly very useful.  I expect to make 
frequent use of it.  I suggest that corresponding code is added to 
`pari_bnf`.

----

On my earlier remarks about "Isomorphism morphism":  Having understood 
better the way that `repr(f)` is constructed for a number field  embedding 
`f`, I realise that making `f` a `Morphism` rather than a `Map` *is* an 
improvement; the terminology is much more appropriate.  
The awkardness of "Isomorphism morphism" is caused by an
earlier decision to make the `_repr_type` of an embedding "Isomorphism".  
This is distinctly out of line with the other values of `_repr_type` in 
SAGE:

`Abelian variety`, `AbelianGroup`, `Affine`, `Affine Scheme`, 
`Affine Space`, `Call`, `Coercion`, `Composite`, `Conversion via ...`, `Generic`,
`Identity`, `Identity map`, `MatrixGroup`, `Native`, `Natural`,
`PermutationGroup`, `Projective Space`, `Projective`, `Quartic`,
`Relative number field`, `Ring`, `Ring Coercion`, `Scheme`, `Section`,
`Set-theoretic ring`, `Steal`.


I note also that embeddings, the maps produced by `subfield` and `subfields`, automorphisms and
elements of `Hom(K, L)` or `End(K, K)`  are all printed as "Ring morphisms:
..."  or "Ring endomorphisms ...".  On the other hand, the maps given by
`K.absolute_field('a').structure()` are given, after your patch, as "Isomorphism morphism:
..."


This certainly needs sorting out at some point (as do other aspects of
the naming of morphisms), but it's not a matter for this patch.  

----

The most important aspect, in my opinion, of your 
`NumberFieldBaseIntoExtensionMorphism` and 
`NumberFieldExtensionOntoBaseMap` code is that it allows the following 
usage:

```
sage: k.<a, b> = NumberField([x^2 + x + 1, x^3 - 2])
sage: B = k.base_field(); B
Number Field in b with defining polynomial x^3 - 2
sage: (b, parent(b))
(b, Number Field in a with defining polynomial x^2 + x + 1 over its base field)
sage: z = B(b)
sage: z, parent(z)
(b, Number Field in b with defining polynomial x^3 - 2)
```

In 3.4.2 the `B(b)` conversion fails. 

This feature is quite useful.  For example

```
sage: (b.norm(), B(b).norm())
(4, 2)
```



But one has to be careful.  If the field `k` above is constructed in a 
different way, the element `b` has a different parent, and your code is 
not needed for the conversions:

```
sage: B.<b> = NumberField(x^3 - 2)
sage: k.<a> = B.extension(x^2 + x + 1)
sage: parent(b)
Number Field in b with defining polynomial x^3 - 2
sage: b.norm()
2
sage: k(b).norm()
4
```



I think some, at least, of the doctests 
should use the above conversion syntax, rather than expressions like
`K.coerce_map_from(K.base_field()).section()` which are, of course, what 
is used to do conversions like `B(b)` above.  There are two reasons for  
this: (i) users should be made aware of this simple conversion syntax; 
(ii) it ensures that any future change to the coercion mechanism which 
would mess up this case gets detected.


I can't see any reason why one should want take a section of the partial
map from a field to its base field, but perhaps I'm missing something.


I agree that it would be rather tricky to fix the parent of sections given 
the way the Section class is defined.



---

archive/issue_comments_048302.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48302",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_048303.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6079#issuecomment-48303",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_events_014270.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6079#event-14270"
}
```



---

archive/issue_events_014271.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6079#event-14271"
}
```



---

archive/issue_events_014272.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6079#event-14272"
}
```



---

archive/issue_events_014273.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6079#event-14273"
}
```



---

archive/issue_events_014274.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6079#event-14274"
}
```



---

archive/issue_events_014275.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6079#event-14275"
}
```



---

archive/issue_events_014276.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6079",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6079#event-14276"
}
```
