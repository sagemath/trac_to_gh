# Issue 7857: Arithmetic operations in fraction fields

Issue created by migration from https://trac.sagemath.org/ticket/7857

Original creator: spancratz

Original creation time: 2010-01-06 16:12:12

Assignee: spancratz

CC:  robertwb

Keywords: fraction field

To implement Henrici's algorithms (or the Henrici--Brown algorithms) for arithmetic operations in fraction fields.

See:
    http://groups.google.com/group/sage-devel/browse_thread/thread/65064ad496db9c75



---

Comment by spancratz created at 2010-01-06 16:13:11

Changing status from new to needs_work.


---

Attachment


---

Comment by spancratz created at 2010-01-06 17:38:46

I've made a three more changes to the previous patch:

- In two places I wrongfully used ``/`` instead of ``//``.
- In another place I had ``base_ring`` instead of ``ring``.

This should be working now.  I've successfully run the doctests in the folder ``sage/rings``, and am currently running a complete test, too.

Sebastian


---

Comment by spancratz created at 2010-01-06 17:38:46

Changing status from needs_work to needs_review.


---

Comment by spancratz created at 2010-01-06 17:39:29

Second patch


---

Attachment

First comment:  Note that the "second patch" replaces the first one!

I noticed a bare "except:"  which is bad style -- it should list the errors expected explicitly.

Question:  the code for sub is (of course) almost identical to that for add.  Would it not be better to implement sub by adding the inverse?  I would have thought that the overhead would be trivial, and itmakes the code easier to maintain.

The (second) patch applies fine to 4.3 and all tests in sage/rings and sage/schemes/elliptic_curves pass.  (I tested the latter since I seemed to remember some fraction field arithmetic somewhere in there).  I also checked the docs still build ok.

I'll tag this as "needs work" but it's very minor to fix the exception trapping and (perhaps) replace the subtraction code.


---

Comment by cremona created at 2010-01-06 18:22:17

Changing status from needs_review to needs_work.


---

Comment by spancratz created at 2010-01-06 19:30:08

This is only a brief message, in case someone is considering reviewing this tonight.  I've now tested the entire library (although without the "long" option), and this has flagged some type errors, so there isn't much point in reviewing this just yet.  I think this has to do with the fact that in the previous patch I only considered ``AttributeError``s and ``NotImplementedError``s, but forgot about ``TypeError``s.  (There are the only three types that are currently considered in the method ``reduce``.)  I'll fix this tonight and then run the tests again, so a hopefully correct version of the patch will be up tomorrow.

Sebastian


---

Comment by cremona created at 2010-01-06 19:57:28

OK -- sounds like you will be dealing with the first point I made anyway.  It should be quick to do a second review though.


---

Comment by spancratz created at 2010-01-06 21:51:45

Dear John,

Thank you for looking at the patch this quickly.

About your first point, I agree.  I followed the previous code of the method "reduce" in this part, which is why I am not completely sure I'll be able to find out exactly which exceptions might be raised.  But I will look into this.

I think you are also right with your second point.  Of course, when I wrote the code I simply copied the method and replaced the appropriate signs to avoid the unnecessary overhead, but in this context this is probably a bad habit, since the maintainability of the code should take priority over a simple sign swap plus an extra function call.  By the way, the same applies to multiplication and division, too.

I'll aim to complete this tonight or tomorrow.

Kind regards,

Sebastian

Replying to [comment:3 cremona]:
> First comment:  Note that the "second patch" replaces the first one!
> 
> I noticed a bare "except:"  which is bad style -- it should list the errors expected explicitly.
> 
> Question:  the code for sub is (of course) almost identical to that for add.  Would it not be better to implement sub by adding the inverse?  I would have thought that the overhead would be trivial, and itmakes the code easier to maintain.
> 
> The (second) patch applies fine to 4.3 and all tests in sage/rings and sage/schemes/elliptic_curves pass.  (I tested the latter since I seemed to remember some fraction field arithmetic somewhere in there).  I also checked the docs still build ok.
> 
> I'll tag this as "needs work" but it's very minor to fix the exception trapping and (perhaps) replace the subtraction code.


---

Attachment

Third patch (replacing all previous ones)


---

Comment by spancratz created at 2010-01-07 01:46:03

At the moment, the following tests still fail:


```
sage -t  devel/sage-ff/sage/combinat/sf/hall_littlewood.py
sage -t  devel/sage-ff/sage/combinat/sf/macdonald.py
sage -t  devel/sage-ff/sage/combinat/sf/sf.py
sage -t  devel/sage-ff/sage/combinat/sf/jack.py
sage -t  devel/sage-ff/sage/coding/linear_code.py
sage -t  devel/sage-ff/sage/algebras/quatalg/quaternion_algebra_element.pyx
sage -t  devel/sage-ff/sage/matrix/matrix2.pyx
```


After taking a first look, it seems that some of these are just positive docstring changes (e.g. a previous ``(-1)/(-1)`` which is now correctly displayed as a ``1``), others are negative changes (e.g. a previous ``1`` now displayed as ``(1/3)/(1/3)``).  However, some ``AttributeError``s are raised for fraction field elements, suggesting that sometimes the numerator or denominator isn't in the ring (of the fraction field).  However, *assuming* that the numerators and denominators of the input to the arithmetic methods belong to the correct ring, I think the code should preserve this and so I should be right to always pass ``coerce=False``.  I could pass ``coerce=True`` to fix these, but assuming I am right (which might not be the case), this would just hide mistakes elsewhere.  In any case, I'll look at these points tomorrow.

Sebastian


---

Comment by spancratz created at 2010-01-07 02:36:57

Fourth patch (replacing all previous ones)


---

Attachment

This patch should now fix the previously remaining doctest failures.  But I am currently testing everything again tonight and will report back tomorrow.

Sebastian


---

Comment by robertwb created at 2010-01-07 06:25:41

You seem to be catching and silencing a huge number of errors, without explanation (though the code before wasn't too good at that either). Also, what if inverse_of_unit raises a NotImplementedError, shouldn't it still be as reduced as possible?


---

Comment by spancratz created at 2010-01-07 11:26:16

Firstly, I wanted to say that the most recent patch file now passes all doctests on my machine.

It is definitely true that a lot of errors are silenced.  But this is done in essentially the same way as before, where, whenever ``reduce`` was called from ``__init__``, the three kinds of errors (``AttributeError``, ``NotImplementedError``, and ``TypeError``) were converted to an ``ArithmeticError``, which was then silenced in ``__init__``.  That is, the user would only actually see the errors if he called ``reduce`` directly.

Of course, I am not entirely sure about this, but I think the behaviour might have been intended.  For example, I don't think someone using fraction fields of non-Euclidean PIDs or Euclidean domains without a GCD implementation should have to wrap all his basic arithmetic calls in ``try ... except``.  On the other hand, if someone explicitly calls ``reduce``, the exceptions should be raised and the caller ought to deal with them.  What do you think, Robert?

About the second point, I had the impression that for rings the method ``inverse_of_unit`` was either implemented or not, rather than it being implemented only to return a ``NotImplementedError``, which is why I am only catching ``AttributeError``s.  However, if this is not the case, then I agree with you, ``NotImplementedError``s should be handled in exactly the same way as ``AttributeError``s in this place.  Could you please comment on this?

Thanks,

Sebastian

Replying to [comment:10 robertwb]:
> You seem to be catching and silencing a huge number of errors, without explanation (though the code before wasn't too good at that either). Also, what if inverse_of_unit raises a NotImplementedError, shouldn't it still be as reduced as possible?


---

Comment by spancratz created at 2010-01-07 11:26:16

Changing status from needs_work to needs_review.


---

Comment by spancratz created at 2010-01-09 02:37:58

Fifth patch (replacing all previous ones)


---

Attachment

I've made three further improvements:

- I've now incorporated Robert's suggestion to catch ``NotImplementedError``s, too.  
- I've improved the method for computing the derivative further, noting that the second GCD computation was unnecessary since at that point in the computation the result was in lowest terms already.
- I've added some test cases to the method ``_derivative``.

Sebastian


---

Comment by cremona created at 2010-01-10 14:20:26

This looks pretty good, and I am checking it now (as it touches so many places I am doing a full test on both 32 and 64 bit machines).

Two small points:
    1. If you have several "except" clauses each with the same action, you can combine them thus:

```
    except (AttributeError, NotImplementedError, TypeError):
```

   2. It's a bit perverse to call the num and den of "self" rnum and rden whle calling those of "right" snum and sden.   However, swapping the over without introducing any bugs would not be trivial!

I will report back when the full tests have finished.


---

Comment by cremona created at 2010-01-10 15:48:41

OK, all tests pass on both 32 and 64 bit.  Hence positive review, as the points I made above are purely cosmetic.


---

Comment by cremona created at 2010-01-10 15:48:41

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 08:10:46

Resolution: fixed
