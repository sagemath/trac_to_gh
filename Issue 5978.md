# Issue 5978: Can't construct the quotient of an univariate polynomial ring by it's zero ideal

Issue created by migration from Trac.

Original creator: jmbr

Original creation time: 2009-05-04 08:10:39

Assignee: tbd




---

Comment by mabshoff created at 2009-05-04 08:16:42

Do *not* attach the error message, but post it verbatim into the ticket.

Also *always* assign a milestone.


---

Comment by tscrim created at 2012-11-18 07:41:42

Changing status from new to needs_review.


---

Comment by tscrim created at 2012-11-18 07:41:42

Fixed by making the quotient by a zero ideal return the original ring.

```
sage: ZZ.quotient(ZZ.zero_ideal()) is ZZ
True
sage: R = QQ['x']
sage: R.quotient(R.zero_ideal()) is R
True
```



---

Comment by tscrim created at 2012-11-18 07:46:43

Fixed this for `quotient_by_principal_ideal()` method in polynomial ring as well.

For patchbot:

Apply: trac_5978-quotient_zero_ideal-ts.2.patch


---

Comment by tscrim created at 2012-11-18 19:05:37

Fixed other doctests.

For patchbot:

Apply: trac_5978-quotient_zero_ideal-ts.patch


---

Comment by lftabera created at 2013-02-20 18:33:48

Changing status from needs_review to positive_review.


---

Comment by lftabera created at 2013-02-20 18:33:48

the patch looks good to me. I have made also further tests. Positive review.

Apply: trac_5978-quotient_zero_ideal-ts.patch


---

Comment by tscrim created at 2013-02-20 18:35:16

Thank you for the review.

Travis


---

Attachment

Rebased to sage-5.8.beta0.


---

Comment by jdemeyer created at 2013-02-22 19:09:51

Resolution: fixed
