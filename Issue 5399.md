# Issue 5399: FinanceDate class

Issue created by migration from Trac.

Original creator: psinis

Original creation time: 2009-02-28 03:34:23

Assignee: psinis

Keywords: finance, date

FinanceDate class extends datetime.date in the Python Standard Lib. The goal is to introduce business-day calculations in Sage, and to give the user an easy API for coding futures & options expiries, generating swap & bond payment dates, and calculating holidays in all the major markets.

To be attached soon:
FinanceDate.py
easter.py
relativedelta.py


---

Comment by jdemeyer created at 2016-04-26 09:52:14

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-04-26 09:52:14

Replying to [ticket:5399 psinis]:
> To be attached soon:
> FinanceDate.py
> easter.py
> relativedelta.py

I think it can be assumed that "soon" will never happen, given that 7 years have passed.


---

Comment by jdemeyer created at 2016-04-26 09:52:20

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
