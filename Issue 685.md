# Issue 685: Make Eisenstein series code handle eisenstein series with character

Issue created by migration from https://trac.sagemath.org/ticket/685

Original creator: craigcitro

Original creation time: 2007-09-18 05:14:14

Assignee: craigcitro

The eisenstein_series_qexp function currently only handles eisenstein series for level 1. It wouldn't be hard to make this handle eisenstein series for higher level and with character. I'm going to take care of this soon, but this is here in case I forget. ;)


---

Comment by craigcitro created at 2007-10-02 00:29:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-05 18:56:58

Craig,

isn't this implemented by now?

Cheers,

Michael


---

Comment by pbruin created at 2014-04-24 20:23:08

Do we want any more functionality than in the following example?

```
sage: G=DirichletGroup(4)
sage: chi=G[1]
sage: E=EisensteinForms(chi,1)
sage: f=E.eisenstein_series()[0]
sage: f.q_expansion(40)
1/4 + q + q^2 + q^4 + 2*q^5 + q^8 + q^9 + 2*q^10 + 2*q^13 + q^16 + 2*q^17 + q^18 + 2*q^20 + 3*q^25 + 2*q^26 + 2*q^29 + q^32 + 2*q^34 + q^36 + 2*q^37 + O(q^40)
```

If not, maybe we can close this as fixed/wontfix/whatever_is_appropriate.


---

Comment by pbruin created at 2014-04-24 20:23:08

Changing status from new to needs_review.


---

Comment by rws created at 2014-06-06 06:18:25

Yes, that leaves nothing to desire.


---

Comment by rws created at 2014-06-06 06:18:25

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-06-06 11:01:15

Resolution: fixed
