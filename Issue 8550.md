# Issue 8550: Infinite matrix groups over QQ fail for is_finite()

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-03-17 05:17:38

Assignee: AlexGhitza

CC:  vdelecroix


```
sage: H=SL(2,QQ)
sage: H.is_finite()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/sage/dev/<ipython console> in <module>()

/sage/dev/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in is_finite(self)
    343         if self.base_ring().is_finite():
    344             return True
--> 345         return self._gap_().IsFinite().bool()
    346
    347     def cardinality(self):

/sage/dev/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in _gap_(self, G)
    217             return SageObject._gap_(self, G)
    218         except TypeError:
--> 219             raise NotImplementedError, "Matrix group over %s not implemented."%self.__R
    220
    221     def __cmp__(self, H):

NotImplementedError: Matrix group over Rational Field not implemented.
```


GL fails similarly.  Other rings (ZZ, finite fields) seem to work OK, so perhaps this is restricted to something peculiar to the rationals?


---

Comment by davidloeffler created at 2010-09-23 14:03:18

From the Gap manual, I get the impression that Gap won't allow you to construct a group unless it is finitely generated (and it knows how to calculate a set of generators). That's why Gap will allow you to work with GL(2, ZZ) but not GL(2, QQ).


---

Comment by chapoton created at 2017-11-30 14:43:05

New commits:


---

Comment by chapoton created at 2017-11-30 14:43:05

Changing status from new to needs_review.


---

Comment by chapoton created at 2017-11-30 21:19:36

green bot, please review


---

Comment by tscrim created at 2017-11-30 23:42:11

LGTM.


---

Comment by tscrim created at 2017-11-30 23:42:11

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2017-12-01 07:36:58

thanks


---

Comment by vbraun created at 2017-12-14 12:40:14

Resolution: fixed
