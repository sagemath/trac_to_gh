# Issue 7596: QQ.number_field() does not behave like any other NumberField

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-12-03 20:06:43

Assignee: davidloeffler

CC:  slelievre

Here's an example:


```
sage: K.<a> = NumberField(x)
sage: K.ideal(5)
Fractional ideal (5)
sage: QQ.ideal(5)
Principal ideal (1) of Rational Field
sage: QQ.number_field().ideal(5)
Principal ideal (1) of Rational Field
```



---

Comment by mderickx created at 2011-02-10 14:10:57

sorry modified the wrong ticket, i meant to edit #9414 which is a duplicate of this one


---

Attachment

here is already a ticket for the easy part : a method "places" for QQ


---

Comment by chapoton created at 2013-07-26 12:23:19

I have imported a patch trying to have QQ and number fields in the same categories:

```
sage: K.<phi> = NumberField(x**2-x-1)
sage: K.categories() == QQ.categories()
True
```

but this breaks the lcm and gcd in a bad way..


---

Attachment


---

Comment by cremona created at 2021-02-08 13:50:51

As of 9.3.beta3, certainly QQ.places() does work.  What I usually do is, when I find a method which QQ does not have but a general number field does have, in the course of implementing something, I just add an aimplementation for QQ.  I think this is more efficient than trying to make QQ work like a number field.  There will be a large number of users who get to see QQ who never use more general number fields.  For such people it does not matter at all to have methods like QQ.places() whose use they may not know.  There were many arguments about what QQ.ideal(5) should return, since the pedantic aswer (as for any field, with a nonzero generator) is that it has to be "Principal ideal (1) of ...".  Number theorists are quite happy to have K.ideal(...) meaning K.fractional_ideal(...).

Is there any reason not to mark this as invalid/won't fix?


---

Comment by cremona created at 2021-02-09 11:03:30

Changing status from new to needs_review.


---

Comment by @DaveWitteMorris created at 2021-02-09 20:31:38

-1 for closing. I think comment:11 discloses a serious problem, though not exactly what is emphasized in the ticket description.  Number fields are rings:

```
sage: K.<a> = NumberField(x)
sage: isinstance(K, Ring)
True
```

Thus, the `ideal` method of a number field needs to return an ideal of `self` (not an ideal of some subring of `self`), because that is what is expected by the `ideal` method of a `Ring`. Otherwise, well-written code involving rings will be buggy. 

I think that if number theorists are not willing to accept this, then `NumberField` should not inherit from `Ring`. But I think it would be better to introduce a new method (maybe `integer_ideal`) to the `NumberField` class, or add a keyword flag to the `ideal` method.


---

Comment by cremona created at 2021-02-10 10:30:36

We have had this discussion many times over the years.  I think I first had it in Jan 2008.  There are correct term for these: "integral ideals" and "fractional ideals". Calling them "ideals" is an abuse of language (agreed), just a common one.  There is no reason at all not to use "fractional_ideal" as the method name -- the class name is already `NumberFieldFractionalIdeal`.  But it would break a lot of users' code (including mine) so it is not a high priority for me.

This ticket has been open for 11 years...


---

Comment by nbruin created at 2021-08-02 16:54:03

I think I can live with the practical effect of the implementation of `is_prime` on number field elements, but note that its documentation says:

```
        Is ``self`` a prime element?

        A *prime* element is a non-zero, non-unit element `p` such that,
        whenever `p` divides `ab` for some `a` and `b`, then `p`
        divides `a` or `p` divides `b`.
...
        In fields, an element is never prime::
...
```

so its documentation directly contradicts its behaviour. This is due to the fact that the method is inherited from `Ring`, but the `ideal` protocol is not compatibly implemented. That obviously needs fixing. In this case, it probably means equipping number field elements with a fresh implementation of `is_prime` with appropriate doc.

Reassigning this ticket to a milestone, because having documentation directly contradict behaviour is obviously something that not just generic "low priority" or "not a bug".


---

Comment by lorenz created at 2021-08-12 05:45:30

Replying to [comment:15 nbruin]:
> In this case, it probably means equipping number field elements with a fresh implementation of `is_prime` with appropriate doc.

I had a shot at this over at #32340.


---

Comment by mkoeppe created at 2021-12-18 19:53:12

Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.


---

Comment by slelievre created at 2022-03-01 22:52:08

Changing status from needs_review to needs_work.
