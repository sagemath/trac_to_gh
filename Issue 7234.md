# Issue 7234: [with patch, needs work] Unit groups for finite fields (and more generally)

Issue created by migration from https://trac.sagemath.org/ticket/7234

Original creator: fwclarke

Original creation time: 2009-10-16 14:30:18

Assignee: tbd

CC:  rbeezer cremona kcrisman slelievre

Keywords: unit group finite field ring

The attached patch implements unit groups for finite fields.  It is 
modelled on John Cremona's code for the unit groups of number fields.  One 
difference is that if F is a finite field,  while F.unit_group() yields 
the group of units (just as for a number field), F.unit_group(n) gives the 
group of n-th roots of unity.

I have designated it as "needs work" for two reasons:

1.  Both pieces of code deserve generalising to more general rings.  In
particular, Rob Beezer has
[expressed](http://groups.google.com/group/sage-devel/browse_thread/thread/4f903f830aed653d) 
a need to have the group of units of the integers modulo n.

2.  There are certain aspects of the notation/terminology/implementation
that I am not totally happy with.  Maybe `F.unit_group(n)` is not such a
good idea.  Also it seems
odd that one has

```
sage: F.<g> = FiniteField(16)
sage: UF = F.unit_group()
sage: UF.gen()
g
sage: g in UF
True
```

but

```
sage: UF(g)
u
sage: UF(1 + g + g^3)
u^7
```

It's similar for number fields:

```
sage: K.<a> = NumberField(x^3 - 39*x - 91)
sage: UK = K.unit_group()
sage: UK.gens()
[-1, a^2 - 4*a - 22, a + 3]
sage: UK(a + 3)
u2
```

Note also that `UF(UF(g))` and `UK(UK(a + 3))` both lead to errors.

Deciding how to be more consistent probably needs to be done at a more
general level and will most likely best be done by introducing a class
`UnitGroupElement` based (for commutative rings anyway) on
`AbelianGroupElement`, something that has been avoided in the finite field
and number field cases.



---

Comment by AlexGhitza created at 2009-11-15 13:21:41

Changing status from new to needs_work.


---

Attachment


---

Comment by cremona created at 2009-11-15 15:48:54

When I implemented that for number fields I ran into these issues.  Initially I tried to construct a UnitGroupElement but gave up -- the problem I faced was the underlying AbelianGroup class, and that has not (yet) improved.

Concerning `(Z/nZ)^*`, note that this is implemented over number fields (by me and Maite) using pari functions for that, including generalised discrete logs.  Sage already has Integers(n).unit_group_gens() using some native code; it could also use pari.


---

Comment by slelievre created at 2018-06-25 06:31:37

This feature is requested in

- [Ask Sage question 42726: Multiplicative group of a field](https://ask.sagemath.org/question/42726)

Francis or John, would you turn the patch into a branch?

The group of roots of unity could be for another ticket
if that is the blocking point.


---

Comment by slelievre created at 2018-06-25 06:31:37

Changing keywords from "unit group finite field ring" to "unit group, finite field, ring".


---

Comment by chapoton created at 2018-06-26 09:04:51

here is a branch, refreshed, but not working
----
New commits:


---

Comment by git created at 2018-06-26 09:07:05

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2018-06-26 09:07:19

now working again


---

Comment by slelievre created at 2018-08-25 16:51:38

Another use case:

- [math stack exchange question 2893434: Character table of multiplicative group of ZZ/9ZZ](https://math.stackexchange.com/q/2893434)


---

Comment by slelievre created at 2022-06-15 05:03:07

This came up again at

- [Ask Sage question 62822: Morphism between multiplicative groups of GF(p^2) and GF(p)](https://ask.sagemath.org/question/62822)
