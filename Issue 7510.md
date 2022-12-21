# Issue 7510: Primes is missing is_finite.

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-11-21 15:20:15

Assignee: was

Keywords: Primes, is_finite

Primes has no methods `is_finite`. This breaks several thing including: 

```
sage: contre_exemples = (p for p in Primes() and not is_prime(mersenne(p)))

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/averell/.sage/temp/tomahawk/25868/_home_averell__sage_init_sage_0.py in <module>()

/usr/local/sage/sage-4.2/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Set_generic.__nonzero__ (sage/structure/parent.c:14641)()

AttributeError: 'Primes_with_category' object has no attribute 'is_finite'
```



---

Comment by hivert created at 2009-11-21 15:20:27

Changing assignee from was to hivert.


---

Comment by hivert created at 2009-11-21 15:44:39

Changing component from number theory to categories.


---

Comment by hivert created at 2009-11-21 15:45:15

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-21 19:18:58

For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?


---

Attachment


---

Comment by hivert created at 2009-11-21 22:45:18

Replying to [comment:4 mhansen]:
> For the second example, don't you want an EnumeratedSet and not a FiniteEnumeratedSet?

Sure ! The example didn't even pass the test... I forgot to re-export before uploading the patch... Thank for pointing this out and sorry for the trouble...


---

Comment by mhansen created at 2009-12-01 05:30:54

Looks good.


---

Comment by mhansen created at 2009-12-01 05:30:54

Resolution: fixed
