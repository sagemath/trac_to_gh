# Issue 8856: Reinstate cached one in algebra_with_basis

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-05-03 14:39:53

Assignee: hivert

CC:  sage-combinat

Keywords: cached one_basis

From `algebra_with_basis.py`:

```
#`@`cached_method   # todo: reinstate once #5843 is fixed
def one_from_one_basis(self):
    """
    Returns the one of the algebra, as per
            ``Monoids.ParentMethods.one``
    [...]
    """
    return self.monomial(self.one_basis()) #.
```

So I'm removing the comment since #5843 is fixed.



---

Attachment


---

Comment by hivert created at 2010-05-03 14:54:53

Changing status from new to needs_review.


---

Comment by hivert created at 2010-05-03 14:54:53

Ready for review...


---

Comment by nthiery created at 2010-05-03 15:30:31

I had ask for this change, and the extra tests are good. Thanks for handling this!

Please double check that all test pass (they should), and then you can put a positive review on my behalf.


---

Comment by hivert created at 2010-05-03 15:40:24

I got a all test on massena (upto usual synchro problem which I rechecked...)...


---

Comment by hivert created at 2010-05-03 15:40:24

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 21:37:18

Resolution: fixed
