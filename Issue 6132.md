# Issue 6132: cmp for number field elements

Issue created by migration from https://trac.sagemath.org/ticket/6132

Original creator: robertwb

Original creation time: 2009-05-26 18:20:57

Assignee: somebody

See discussion at http://groups.google.com/group/sage-nt/browse_thread/thread/422606e40805d5d0?hl=en

Note that `cmp(list(a), list(b))` can be slow...


---

Comment by rlm created at 2009-05-26 19:13:55

Minor, but I just fixed two of these elsewhere: it's spelled "consistent"


---

Attachment


---

Comment by AlexGhitza created at 2009-05-30 08:38:41

The patch applies with some fuzz to 4.0.rc2, but I'm seeing a bunch of doctest failures in sage/rings:


```
The following tests failed:


	sage -t  "devel/sage-main/sage/rings/number_field/number_field.py"
	sage -t  "devel/sage-main/sage/rings/number_field/number_field_rel.py"
	sage -t  "devel/sage-main/sage/rings/number_field/order.py"
	sage -t  "devel/sage-main/sage/rings/number_field/galois_group.py"
	sage -t  "devel/sage-main/sage/rings/number_field/number_field_element.pyx"
	sage -t  "devel/sage-main/sage/rings/number_field/number_field_ideal.py"
	sage -t  "devel/sage-main/sage/rings/number_field/number_field_ideal_rel.py"
	sage -t  "devel/sage-main/sage/rings/number_field/unit_group.py"
	sage -t  "devel/sage-main/sage/rings/polynomial/complex_roots.py"
	sage -t  "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
```



---

Comment by nbruin created at 2010-01-28 18:08:03

In Python 3, "greater than" etc. comparisons between objects where no natural ordering exist are supposed to raise a "TypeError"

Already, comparing complex numbers in Python 2.6.2 raises
`TypeError: no ordering relation is defined for complex numbers`

Changing this will probably lead to even more doctest failures, but brings us closer to Python's way of doing things and to mathematical sanity.


---

Comment by nbruin created at 2010-01-28 18:08:03

Changing assignee from somebody to nbruin.


---

Comment by nbruin created at 2010-01-28 19:03:51

Remove assignee nbruin.


---

Comment by robertwb created at 2010-01-28 19:05:18

Note that to follow this convention, we have to use __richcmp__ as == and != should still work for unordered elements.


---

Comment by kcrisman created at 2011-02-07 15:43:08

Apparently related to #7160 and #10064, see [this sage-devel discussion](http://groups.google.com/group/sage-support/browse_thread/thread/28bbd04a78dadb57/01168722573ff736).


---

Comment by was created at 2011-03-21 01:17:06

See also #9572.


---

Comment by kcrisman created at 2011-03-21 12:50:39

Replying to [comment:8 was]:
> See also #9572. 
That is a SageNB release ticket.  ?


---

Comment by was created at 2011-12-20 06:54:49

See #7160 for a related ticket/discussion.


---

Comment by mhansen created at 2013-07-22 15:02:22

I think we can close this as a duplicate of those other tickets now that they are merged.


---

Comment by mhansen created at 2013-07-22 15:02:22

Resolution: duplicate
