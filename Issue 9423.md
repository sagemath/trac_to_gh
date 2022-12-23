# Issue 9423: Gap interface for number fields

Issue created by migration from https://trac.sagemath.org/ticket/9423

Original creator: SimonKing

Original creation time: 2010-07-04 12:18:57

Assignee: was

Keywords: gap interface number field

Originally motivated by work on #5618, I found two bugs in the Gap interface for number fields, reported [here](http://groups.google.com/group/sage-devel/browse_thread/thread/6518e7f30c02e534).

#8909 has a positive review and seems partially relevant here, so, I started work with the patch from #8909 applied.

With the new patch, the following works (and is doctested):

```
sage: L.<tau> = NumberField(x^3-2)
sage: gap(tau)^3  # note the exclamation mark used by GAP
!2
sage: L(gap(tau)^3) # this used to fail
2
```


```
sage: P.<z> = QQ[]  # Note: The var'name is z, not x
sage: K.<zeta> = NumberField(z^2 - 2)
sage: k = gap(K)  # this used to fail, as only var'name x was accepted
```


Fixing the second problem, it is needed to avoid a conflict with an internal variable name of a GAP function, namely "E". This tests that the conflict is indeed avoided:

```
sage: P.<E> = QQ[]
sage: L.<tau> = NumberField(E^3-2)
sage: gap(L)
<algebraic extension over the Rationals of degree 3>
```




---

Comment by SimonKing created at 2010-07-04 12:23:07

Fixing two bugs (doctested) in the GAP interface of number fields


---

Attachment


---

Comment by SimonKing created at 2010-07-04 12:23:57

Changing status from new to needs_review.


---

Comment by lftabera created at 2010-12-04 15:32:23

The code corrects a couple of bugs in the gap interface of number fields. Since ! cannot be part of the name of a generator of a number field, then eliminating "!" from the gap representation is correct.

The solution to the "E" variable problem is correct, althought there should be a more system-wide solution to this kind of problems.

I will not give it a positive review until #5618 is also ready to merge, since this patch eliminates a doctest that after #5618 will be obsolete.


---

Attachment

Updated headers


---

Comment by lftabera created at 2010-12-29 14:28:03

Positive review, I have only updated the patch header to add the ticket number

Apply: 

trac_9423_gap_for_numberfields.2.patch

Note to the release manager: ticket #5618 depends on this. This ticket should be merged together with #5618.


---

Comment by lftabera created at 2010-12-29 14:28:03

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-25 08:14:51

Resolution: fixed
