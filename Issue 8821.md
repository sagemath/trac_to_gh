# Issue 8821: Adding a section on coercion to the tutorial (guided tour)

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-04-29 09:58:47

Assignee: mvngu

CC:  robertwb

Keywords: tutorial coercion

So far, the word "coercion" has only been used twice in the tutorial - without explanation or reference. I believe coercion is far too important to not cover it in the tutorial, and moreover some pitfalls may be confusing for mathematicians, while programmers might confuse it with implicit type conversion.

My patch adds such section.


---

Comment by SimonKing created at 2010-04-29 10:01:01

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-04-29 10:26:59

Looks good, and is much needed. I haven't finished reading it, but I have some comments: 

First, I might focus less on the types and isinstance corresponding to mathematical categories, as they can be misleading. For example, univarite polynomials are instances of PrincipalIdealDomainElement, even if they are. Another example, testing for RingElement could be deceptive. At least one of


```
sage: isinstance(matrix(ZZ, 2), RingElement)
True
sage: isinstance(matrix(ZZ, 2,3), RingElement)
True
```


is False. (I consider the first a bug.)

Second, we don't want to create the expectation that Python elements are unique, as they usually aren't: 


```
sage: a = -15r
sage: b = -15r
sage: a is b
False
```


Only some really common integers are.


---

Comment by SimonKing created at 2010-04-29 10:34:22

Hi Robert,

Replying to [comment:2 robertwb]:

> First, I might focus less on the types and isinstance corresponding to mathematical categories, as they can be misleading.

OK, I wanted to give a first approximation on how classes relate with mathematics. Perhaps I should emphasize that the analogy is not perfect (I already mention that different classes may also relate with different implementations of the same mathematical structure).

> ` sage: isinstance(matrix(ZZ, 2), RingElement) True sage: isinstance(matrix(ZZ, 2,3), RingElement) True ` is False. (I consider the first a bug.)

Really? The first is a square matrix, so, I think the second is wrong.

> Second, we don't want to create the expectation that Python elements are unique, as they usually aren't:

Right, that should be clarified.

Thank you!

Simon


---

Comment by leif created at 2010-04-29 11:15:18

Replying to [comment:3 SimonKing]:
> > Second, we don't want to create the expectation that Python elements are unique, as they usually aren't:
> 
> Right, that should be clarified.
Yes, that's what I suggested in the `sage-devel` thread. ;-)
(And Robert noted that this is implementation-specific even in plain Python.)
One should clarify that in general
  `a is b` => `a == b`
but not necessarily the opposite.

Regarding comparison:
It should be stressed that not only `a == b` returns `False` if coercion fails but also `a != b` (silently) returns `False` in that case.

Reading on...

Btw (ticket description), I'd still say Sage's coercion _is_ (a kind of) implicit type conversion...

It seems we've reached ultimate confusion in the `sage-devel` thread ("exact" and "inexact" domains); I unfortunately haven't been able to reply so far...

-Leif


---

Comment by leif created at 2010-04-29 11:45:57

Replying to [comment:4 leif]:
> Btw (ticket description), I'd still say Sage's coercion _is_ (a kind of) implicit type conversion...
Ok, one might clarify that an implicit conversion (coercion) in Sage can be performed even if the objects' types appear to be the same; but this is not really different to other object-oriented languages (cf. virtual functions).


---

Comment by SimonKing created at 2010-04-29 12:19:22

Replying to [comment:4 leif]:
> Regarding comparison:
> It should be stressed that not only `a == b` returns `False` if coercion fails but also `a != b` (silently) returns `False` in that case.

No, it doesn't:


```
sage: GF(5)(1) == GF(2)(1)
False
sage: GF(5)(1) != GF(2)(1)
True
sage: R.<x,a,b> = QQ[]
sage: S.<x,c,d> = QQ[]
sage: x == R('x')
False
sage: x != R('x')
True
```



---

Comment by SimonKing created at 2010-04-29 12:42:17

To be applied after the first patch


---

Attachment

I added another patch (on top of the first patch), taking into account some of your remarks. In particular, I try to clarify that "class <-> category" is nothing more than a weak analogy.


---

Comment by leif created at 2010-04-29 13:39:05

Replying to [comment:6 SimonKing]:
> No, it doesn't:
> sage: GF(5)(1) != GF(2)(1)
> True
Then document the opposite (of what *I* stated) ;-)

(I thought this was said in some Sage documentation, but it seems I took this assumption from Robert's statement:

  "In Python, the convention is that == and != never raise an error, so  
  False is returned if coercion fails (the two domains are incompatible)."

in http://groups.google.com/group/sage-devel/msg/3ec75b62fcb3f295 and my reply: http://groups.google.com/group/sage-devel/msg/2f2e69bfb8623a4a)


---

Comment by SimonKing created at 2010-04-29 13:47:33

Replying to [comment:8 leif]:
> Replying to [comment:6 SimonKing]:
> > No, it doesn't:
> > sage: GF(5)(1) != GF(2)(1)
> > True
> Then document the opposite (of what *I* stated) ;-)

This is already part of the patch that I provided a few minutes ago.

Cheers,

Simon


---

Comment by robertwb created at 2010-04-29 17:25:46

What I should have said is that two incomparable elements are considered inequal (hence == returns False and != returns True). 

Perhaps a better way to describe the class <-> category relationship is to mention that the type system is not sufficiently expressive to capture the rich possibilities of mathematical relations (short of hackery like lots and lots of dynamic types), and that the *parent* of an object has to do with its place in the mathematical hierarchy, while the *type* of an object has to do with its underlying implementation.


---

Comment by leif created at 2010-04-29 20:33:35

`programming.rst` (only patched in the first changeset) still contains "comparing objects of `different types` in Sage"; here "different parents" or "different Sage meta-types/structures" or something like that would be more appropriate (perhaps just a footnote on "types"?).


---

Comment by jhpalmieri created at 2010-06-21 18:42:52

I think this looks good.  [Leif's comment 11](http://trac.sagemath.org/sage_trac/ticket/8821#comment:11) might be worth addressing.  Also, in the new coercion section, perhaps in `X.__add__(Y), X.__sub__, X.__mul__`, every term should have `(Y)`?

Otherwise, I think this should get a positive review.


---

Comment by leif created at 2010-06-21 21:28:40

There's a typo (missing space) in one headline ("Parents,types and categories"[sic]).

----

I've actually given up thinking about Sage's "coercion model", because IMHO still different people seem to have different ideas of what it is and how it does or should work (including different interpretations of terms).

If you want to have fun, compare this description to that in [William's and Burcin's recent paper](http://wstein.org/papers/icms/icms_2010.pdf) (page 12)... ;-)

(Reading that, one would think _every_ coercion in Sage is a type 
*promotion*. "only from exact to inexact" suggests the opposite, type *demotion*, and does, e.g., not include `QQ.has_coerce_map_from(ZZ)`, where I'd consider `ZZ` the [more] "inexact" domain.)

----

I'd write that Sage implements its own _type system_, which must not be confused with *Python's* (as opposed to "... type conversion and type coercion known from, e.g., the C programming language").

The explanation that there can only be a finite number of classes in Python is somewhat wrong; in fact, classes can be created dynamically (regarding finite memory, there can only be finitely many instances of a class, too).


---

Comment by jhpalmieri created at 2010-06-21 21:43:46

Replying to [comment:13 leif]:

> If you want to have fun, compare this description to that in [William's and Burcin's recent paper](http://wstein.org/papers/icms/icms_2010.pdf) (page 12)... ;-)
> 
> (Reading that, one would think _every_ coercion in Sage is a type 
> *promotion*. "only from exact to inexact" suggests the opposite, type *demotion*, and does, e.g., not include `QQ.has_coerce_map_from(ZZ)`, where I'd consider `ZZ` the [more] "inexact" domain.)

ZZ and QQ are equally exact: any element of them can be represented exactly on a computer.  Because of the presence of some transcendental numbers with no exact representation, RR is inherently inexact: when you work in RR, you're only working up to some level of precision.

Reading p. 12 of the Stein-Erocal paper, I would think that every coercion comes from an embedding, but this is not true.  Every coercion should come from a mathematically canonical map (like mapping Z to any ring, or the inclusion of Q into R).  Thinking about it mathematically makes sense to me, and I think this is the whole point.

Also, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other "consumers" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.


---

Comment by jhpalmieri created at 2010-06-21 22:14:08

See also #9300.


---

Comment by leif created at 2010-06-21 23:48:28

Replying to [comment:14 jhpalmieri]:
> [...] ZZ and QQ are equally exact: any element of them can be represented exactly on a computer.  Because of the presence of some transcendental numbers with no exact representation, RR is inherently inexact: when you work in RR, you're only working up to some level of precision.
Well, irrational numbers and limited precision are different aspects; in principle, "the" real field should contain QQ. And at least some irrational numbers (I personally don't consider them numbers ;-) , or at least not "real" in the sense of existence) _can_ be represented - in general as (symbolic) constants or as limits.

(On the other hand, `NaN in RR`, but `infinity` is not, `RR.pi` is a method, `RR.pi() == pi` - where `parent(pi)` is `Symbolic Ring` - evaluates to `True`...)

> Reading p. 12 of the Stein-Erocal paper, I would think that every coercion comes from an embedding, but this is not true.  Every coercion should come from a mathematically canonical map (like mapping Z to any ring, or the inclusion of Q into R).  Thinking about it mathematically makes sense to me, and I think this is the whole point.
If it's clear to everyone what is meant by "exact" and "inexact"...

Mapping Q into R is not the same as mapping `QQ` into `RR`; in fact, Sage supports the direction that is sound in the mathematical domains, i.e. that is valid for Q and R, though the implementation (the actual domains considered mathematically; floating-point numbers in the case of `RR`) would suggest the opposite, because every element of `RR` (except some symbolic constants) can be represented in `QQ`. IMHO coercions (as opposed to conversions) should be injective; the natural embedding of Q in R does _not_ hold for "Sage's" Q and R, `QQ` and `RR`.

> Also, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other "consumers" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.
I'm not sure what that refers to; nevertheless the reader will (or should) be familiar with Python, including the concept of its types and classes, and will be confronted with the differences between Python types (including classes) and Sage's types, namely "parents".


---

Comment by jhpalmieri created at 2010-06-22 03:39:09

Coercions in Sage are supposed to model the underlying mathematics.  So a coercion from QQ to RR is defined, as it should be.

Replying to [comment:16 leif]:
> And at least some irrational numbers _can_ be represented - in general as (symbolic) constants or as limits.

That's why I used the qualifier "some" in "the presence of some transcendental numbers".  And of course every real number can be represented as a limit of rationals...

> IMHO coercions (as opposed to conversions) should be injective.

No.  The natural map from ZZ to ZZ/nZZ should be a coercion, as indeed should be the natural map from ZZ to any ring.  The same for the standard map from an object (ring, group, module, ...) to any of its quotients.  These are typically not injective, but they are also completely canonical.  Any canonical map should be a coercion.

> the natural embedding of Q in R does _not_ hold for "Sage's" Q and R, `QQ` and `RR`.

I'm willing to believe this, but can you provide evidence?

> > Also, remember that a document like the Sage tutorial is aimed to a large degree at mathematicians and math students (and other "consumers" of mathematics), moreso than to people with a computer science focus.  So focusing on types, etc., is not appropriate.
> I'm not sure what that refers to; nevertheless the reader will (or should) be familiar with Python, including the concept of its types and classes, and will be confronted with the differences between Python types (including classes) and Sage's types, namely "parents".

It refers to, for example, your statement "I'd write that Sage implements its own type system ...".  I think this sort of statement puts more of a programming-type focus than a mathematical one.


---

Comment by SimonKing created at 2010-06-22 16:35:36

Dear John, dear Leif,

thank you for not forgetting this ticket (I almost did). Currently I am hardly able to work on it, since I am at some conference, and the internet access in my hotel is a bit restricted.

Cheers, Simon


---

Comment by SimonKing created at 2011-06-15 07:40:58

I just noticed that this very ancient ticket is still unresolved.

I still think that a text on coercion should be added to the guided tour. I think, after a break of 12 months, one should have a fresh look at the texts.

In addition, I think that there should also be a thematic tutorial (i.e., not just a chapter in the guided tour) covering coercion and categories. I therefore opened #11490.


---

Attachment

ONLY APPLY THIS PATCH: Insert a section on coercion into the guided tour.


---

Comment by SimonKing created at 2011-06-16 07:58:06

I have combined the two patches, so that only trac_8821-tutorial-coercion.patch is relevant now. I re-structured the text slightly, and I also refer to my worksheet on coercion that is attached to #11490.

Note that the text we are considering here is not about implementing coercion. The implementation aspect is addressed in #11490.

For the patchbot:

Apply trac_8821-tutorial-coercion.patch


---

Comment by jhpalmieri created at 2011-07-22 23:56:16

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2011-07-22 23:56:16

Here's a referee's patch.  Positive review.


---

Attachment


---

Comment by jdemeyer created at 2011-08-02 19:44:52

Resolution: fixed
