# Issue 4: should exist a conversion from Integers(p**N) to pAdicField(p)

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-12 00:41:16

Assignee: somebody

Currently this:

pAdicField(5)(Integers(125)(13))

produces this:

Traceback (most recent call last):
...
TypeError: unable to compute ordp

I think SAGE should be able to perform such a conversion.



---

Comment by dmharvey created at 2006-09-26 22:25:41

Changing assignee from somebody to dmharvey.


---

Comment by roed created at 2007-04-13 03:59:59

Resolution: fixed


---

Comment by roed created at 2007-04-13 03:59:59

Works in new p-adic architecture
