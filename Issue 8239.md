# Issue 8239: misleading teichmuller behaviour

Issue created by migration from https://trac.sagemath.org/ticket/8239

Original creator: dmharvey

Original creation time: 2010-02-11 19:45:25

Assignee: roed

CC:  roed

This is kind of misleading:


```
sage: K.<a> = Qq(25)
sage: K.teichmuller(K(2/5))
2*5^-1 + 1 + 2*5 + 5^2 + 3*5^3 + 4*5^4 + 2*5^5 + 3*5^6 + 3*5^8 + 2*5^9 + 2*5^10 + 4*5^12 + 5^13 + 3*5^14 + 2*5^15 + 4*5^16 + 4*5^18 + O(5^19)
```


It should raise an exception.

The prime case behaves as I would expect:


```
sage: K = Qp(5)
sage: K.teichmuller(K(2/5))
Traceback (click to the left of this block for traceback)
...
ValueError: cannot set negative valuation element to Teichmuller
representative.
```




---

Attachment


---

Comment by roed created at 2011-11-11 02:20:41

Changing status from new to needs_review.


---

Comment by johanbosman created at 2011-11-12 14:13:01

Changing status from needs_review to positive_review.


---

Comment by johanbosman created at 2011-11-12 14:13:01

This looks okay and passes all tests. :).


---

Comment by jdemeyer created at 2011-11-15 08:55:20

Resolution: fixed
