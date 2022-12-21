# Issue 6800: [with patch, needs review] formal/lazy/infinite powerseries

Issue created by migration from Trac.

Original creator: Henryk.Trappmann

Original creation time: 2009-08-22 07:32:14

Assignee: burcin

CC:  sage-combinat mantepse

New code that implements lazy power and Laurant series.


---

Attachment

patch adds the file formal_powerseries.py


---

Comment by AlexGhitza created at 2009-12-08 10:03:09

Changing status from needs_review to needs_work.


---

Comment by AlexGhitza created at 2009-12-08 10:03:09

The documentation needs some serious reformatting to adhere to the ReST format.  I am cc-ing sage-combinat because a lot of people there would be interested in formal power and Laurent series.


---

Comment by AlexGhitza created at 2009-12-08 10:03:09

Changing component from calculus to algebra.


---

Comment by mantepse created at 2014-01-10 20:48:44

Changing keywords from "" to "LazyPowerSeries".


---

Comment by rws created at 2014-03-15 17:01:31

I think although there is `combinat.species.series.LazyPowerSeries` this implementation would still be good to have, as the implementation in combinat misses many features included here. It is also needed for P-finite sequences. 

However, I don't think it's right to define all special functions anew: the ring or a static function should be able to create a series from a symbolic expression (interpreted as e.g.f.), and , in case of a rational polynomial, delegate to CFiniteSequence (#15714).

There were a few failures:

```
   1 of  39 in sage.rings.formal_powerseries.FormalPowerSeries
   1 of   6 in sage.rings.formal_powerseries.FormalPowerSeries.nipow
   1 of   6 in sage.rings.formal_powerseries.FormalPowerSeries.pow
   3 of   8 in sage.rings.formal_powerseries.FormalPowerSeries0.abel
   1 of   4 in sage.rings.formal_powerseries.decidable0
```



---

Comment by mantepse created at 2022-08-11 17:48:51

This is subsumed by #32324.


---

Comment by mantepse created at 2022-08-11 17:49:25

Changing status from needs_work to needs_review.


---

Comment by mantepse created at 2022-08-11 17:49:46

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2022-09-01 02:30:35

Resolution: invalid
