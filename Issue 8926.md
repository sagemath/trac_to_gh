# Issue 8926: Family cannot completely handle a class as an argument

Issue created by migration from https://trac.sagemath.org/ticket/8926

Original creator: saliola

Original creation time: 2010-05-07 20:32:47

Assignee: sage-combinat

CC:  sage-combinat


```
sage: F = Family(NonNegativeIntegers(), PerfectMatchings)
sage: F
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
/home/saliola/Applications/sage-4.4/local/lib/python2.6/site-packages/sage/sets/family.pyc in _repr_(self)
    873             name = name+"(i)"
    874         else:
--> 875             name = self.function.__repr__()
    876             if isinstance(self.function, AttrCallObject):
    877                 name = "i"+name[1:]

TypeError: descriptor '__repr__' of 'sage.structure.sage_object.SageObject' object needs an argument
```




---

Attachment


---

Comment by hivert created at 2010-05-07 23:04:43

Changing status from new to needs_review.


---

Comment by hivert created at 2010-05-12 17:42:16

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-05-12 17:42:16

From a private e-mail from Nicolas M. Thiéry:

```
 - trac_8926_family_repr-fh.patch   # Positive review, assuming test pass
```

We had a all tests passed on the server massena. Therefore I allow myself to put a positive review on behalf of Nicolas.


---

Comment by hivert created at 2010-06-02 18:26:11

Changing assignee from sage-combinat to hivert.


---

Comment by mhansen created at 2010-06-05 22:12:38

Resolution: fixed
