# Issue 8613: __dir__() / tab completion returns nonexistent attributes

Issue created by migration from https://trac.sagemath.org/ticket/8613

Original creator: mmezzarobba

Original creation time: 2010-03-26 21:46:19

Assignee: somebody

On the following example, tab completion suggests ``sum``, which is not an attribute of ``R``.


```
sage: R = QQ['t']
sage: R.su       
R.sum                               R.summation
R.summation_from_element_class_add             
sage: R.sum                                    
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/marc/co/sage-4.3.4/<ipython console> in <module>()

/home/marc/co/sage-4.3.4/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:5120)()

/home/marc/co/sage-4.3.4/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2638)()                                                                             

AttributeError: 'PolynomialRing_field' object has no attribute 'sum'
sage: 'sum' in R.__dir__()
True
```



---

Comment by was created at 2010-03-29 04:56:49

Notice also that other longer summation_from_element_class_add:

```
sage: search_src('summation_from_element_class_add')
categories/commutative_additive_semigroups.py:121:        summation_from_element_class_add = summation
categories/commutative_additive_semigroups.py:136:            if (self.summation != self.summation_from_element_class_add) and hasattr(self, "element_class") and hasattr(self.element_class, "_add_parent"):

```


So, this suggests that this bug has something to do with Nicolas's category theory rewrite?  I'll post to sage-combinat.


---

Comment by was created at 2010-03-29 04:57:38

This issue happens in both the notebook and command line.


---

Comment by nthiery created at 2010-06-07 07:26:51

This should be fixed once #9138 will be implemented.


---

Comment by SimonKing created at 2011-04-10 15:06:32

Changing status from new to needs_review.


---

Comment by SimonKing created at 2011-04-10 15:09:04

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2011-04-10 15:09:04

Indeed, it is a duplicate.

With the patches from #9944 and #9138, one obtains:

```
sage: R = QQ['t']
sage: R.sum
<bound method PolynomialRing_field_with_category.sum of Univariate Polynomial Ring in t over Rational Field>
sage: R.summ
R.summation                         R.summation_from_element_class_add
sage: R.summation_from_element_class_add
<bound method PolynomialRing_field_with_category.summation of Univariate Polynomial Ring in t over Rational Field>
```



I learnt: In that case, one should give a ticket a positive review and choose the milestone "duplicate", so that the release manager may close it.


---

Comment by SimonKing created at 2011-04-10 15:10:09

PS: #9138 needs review (hint...)


---

Comment by jdemeyer created at 2011-04-11 14:59:48

Resolution: duplicate
