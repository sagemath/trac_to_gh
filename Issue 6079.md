# Issue 6079: modernize base inclusion morphism of relative number fields

Issue created by migration from https://trac.sagemath.org/ticket/6079

Original creator: ncalexan

Original creation time: 2009-05-19 02:18:22

Assignee: was

CC:  robertwb craigcitro was mstreng

Keywords: base inclusion morphism relative number field

The patch adds a class for the morphism embedding the base into a relative number field extension, and (much more useful) the partially defined section going back.

It also adds a verbose(level=4) stack trace whenever nfinit and rnfinit are called.  It's a huge pain trying to work around such calls without a mechanism to see them, so here it is.


---

Attachment

Second patch relies on first; might as well be on same ticket.  Adds a subfield_containing that tries to do a bit more than naive trial and error to find the smallest subfield of a number field containing the specified elements.


---

Comment by fwclarke created at 2009-05-19 06:52:49

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

Comment by ncalexan created at 2009-05-19 16:07:52

For point 1, removing the "map" at the end is not hard but really isn't worth it.  Notice that I'm defining _repr_type_; it's the base class's _repr_ that's adding map/morphism.  Just not worth it.

For point 2, subfield and subfield_containing do not do the same thing.  subfield guarantees that your element is a generator of the returned field; subfield_containing does no such thing.  Also, subfield_containing is not yet implemented for relative fields, while subfield is (And, I think, would mean different things in that case.)  Finally, having a single element vs. list of elements option causes problems -- it's annoying to use with iterators, for example.  (Although I rule out using iterators precisely to catch errors when you give me a single element.)

Thanks for the quick review, can I have another?


---

Comment by ncalexan created at 2009-05-19 23:44:14

Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.

The first patch should still be good.


---

Comment by fwclarke created at 2009-05-20 06:03:56

Replying to [comment:6 ncalexan]:
> Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.

I would have thought that the simplest way to implement the function would be by a recursive use of `relativize`.  *Except* this function does not, in my opinion, work correctly with relative extensions.  If L/K is a relative extensions, and alpha is in L, then `L.relativize(alpha, 'alpha') returns the relative extension L/QQ(alpha).  I think it would be much more useful if it returned L/K(alpha).  This should be easy to fix, and then `subfields_containing` would follow, including the relative case.

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

Comment by ncalexan created at 2009-05-20 06:46:21

I'm withdrawing the second patch for the time being (even though the uniqueness problem was wrong -- it was unique, I was confused).  All of these comments seem to be about the second patch; if that's true, can we just review the first patch?  I've responded to your comments anyway.

Replying to [comment:7 fwclarke]:
> Replying to [comment:6 ncalexan]:
> > Please disregard the second patch for the time being.  The result is not unique, at least not in some cases I thought it would be, and I have to deduce the correct conditions on the embeddings to make it unique.
> 
> I would have thought that the simplest way to implement the function would be by a recursive use of `relativize`.

So did I.  After trying to do a recursive relativize, I came to this.  (I found this method to work a lot better, but that was before my patches making relativize work quickly were in place.)

  *Except* this function does not, in my opinion, work correctly with relative extensions.  If L/K is a relative extensions, and alpha is in L, then `L.relativize(alpha, 'alpha') returns the relative extension L/QQ(alpha).  I think it would be much more useful if it returned L/K(alpha).  This should be easy to fix, and then `subfields_containing` would follow, including the relative case.

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

Comment by ncalexan created at 2009-05-20 07:31:19

I've made a new ticket, #6092, for discussing the second part of this patch.  I'd really like to get the first part merged before it rots, but it seems clear that the second part needs work.


---

Comment by mabshoff created at 2009-05-20 11:04:48

Nick: I deleted trac_6079-subfield-containing.patch from this trac ticket.

Cheers,

Michael


---

Comment by fwclarke created at 2009-05-22 07:08:38

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
don't think it should be defined to apply to a _list_ of elements.  Conceptually
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

Comment by ncalexan created at 2009-05-22 14:36:09

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

Comment by fwclarke created at 2009-05-22 19:09:15

Replying to [comment:12 ncalexan]:

> it's as if you're not reading what's written.  The docstring explicitly says that if you're looking for the functionality that you want to reduce this function to, that section is how to get it.  And then it shows you what the differences are, including how the error message is more to your liking!

I don't know what you mean by "the functionality that you want to reduce this function to" .  I didn't really want to change the functionality (apart from allowing single elements).

I had read your first doctest, but

1.  I couldn't see why you should start with a non-standard, slightly complicated instance of the function's use, followed by how to get the same answer a different way using "exotic" means, i.e., `coerce_map_from` and `section` (exotic anyway from the point of view of a number theorist who knows little about how SAGE works).

2.  This first test is specifically about the base field as subfield, in some sense the only _genuine_ subfield there is (along, I suppose, with its base field, and so on).  For SAGE's subfields, as given by the `subfield` and `subfields` functions, are just a field with a embedding (so also created by the `embeddings` function).

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

I don't think that in essence it is so tricky.  Once the problem is converted to linear algebra, using the `absolute_vector_space` function (which is hopefully sufficiently doctested), it's relatively straightforward.  Certainly the doctests need to contain a variety of cases, but I don't see why in your second example you need to run through _all_ the quadratic subfields of `L`.  And what's the point of a random test with such a long output?

> Why don't we rename `recognize_in_subfield` to `_recognize_many_in_subfield` and add a `recognize_in_subfield` with a simpler docstring that does the list wrapping.  But please, I am the user who needs to recognize many elements in a subfield so I want that functionality to be available.

This seems sensible.  But I don't actually see what's wrong with allowing _either_ a single element _or_ a list (as does `NumberField`).  Just have

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

Comment by fwclarke created at 2009-05-25 12:33:18

## More remarks

The verbose stack trace is certainly very useful.  I expect to make 
frequent use of it.  I suggest that corresponding code is added to 
`pari_bnf`.

----

On my earlier remarks about "Isomorphism morphism":  Having understood 
better the way that `repr(f)` is constructed for a number field  embedding 
`f`, I realise that making `f` a `Morphism` rather than a `Map` _is_ an 
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

Comment by davidloeffler created at 2009-07-21 08:19:46

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:19:46

Changing assignee from was to davidloeffler.
