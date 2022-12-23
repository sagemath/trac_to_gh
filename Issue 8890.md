# Issue 8890: map_support modifies the zero element of a free module!

Issue created by migration from https://trac.sagemath.org/ticket/8890

Original creator: jbandlow

Original creation time: 2010-05-05 16:12:51

Assignee: AlexGhitza

CC:  sage-combinat


```
sage: B = CombinatorialFreeModule(ZZ, ['a','b'])
sage: B.an_element().map_support(lambda i: i)
2*B['a'] + 2*B['b']
sage: B.zero()
2*B['a'] + 2*B['b']
```


Looking at the code exposes the problem:

```
        res = self.parent()(0)
        z_elt = {}
        for m,c in self.monomial_coefficients().iteritems():
            z_elt[f(m)] = c
        res._monomial_coefficients = z_elt
        return res
```


We should not change the dictionary of zero!


---

Comment by nthiery created at 2010-05-05 17:02:27

Changing status from new to needs_work.


---

Comment by nthiery created at 2010-05-05 17:02:27

Changing keywords from "" to "free modules".


---

Comment by nthiery created at 2010-06-01 20:44:39

Changing status from needs_work to needs_review.


---

Comment by jbandlow created at 2010-06-01 23:59:52

Changing status from needs_review to positive_review.


---

Comment by jbandlow created at 2010-06-01 23:59:52

Looks good to me.  Thanks Nicolas!  Positive review.


---

Comment by jbandlow created at 2010-06-02 01:49:24

Oops, I forgot to mention that this depends on #8881.


---

Attachment


---

Comment by mhansen created at 2010-06-06 01:11:50

Resolution: fixed
