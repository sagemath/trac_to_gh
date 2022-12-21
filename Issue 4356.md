# Issue 4356: modular forms -- echelon_form broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-24 02:03:06

Assignee: craigcitro

This used to work (e.g., it is in my modular forms book), but now it doesn't.  No clue why it is broken:

```
sage: M = ModularForms(1,36, prec=10).echelon_form()
Traceback (most recent call last):
...
ValueError: The given basis vectors must be linearly independent.
```



---

Comment by craigcitro created at 2008-10-24 08:54:18

So I can't find any examples that don't work ... in my copy of 3.1.4, I get:


```
sage: M = ModularForms(1, 36, prec=6).echelon_form()
sage: M.basis()
[
1 + 6218175600*q^4 + 15281788354560*q^5 + O(q^6),
q + 57093088*q^4 + 37927345230*q^5 + O(q^6),
q^2 + 194184*q^4 + 7442432*q^5 + O(q^6),
q^3 - 72*q^4 + 2484*q^5 + O(q^6)
]
```


What machine were you running into this on?


---

Comment by was created at 2008-10-30 16:52:08

This is invalid.  I was thrown off by a my messed up #4347!


---

Comment by was created at 2008-10-30 16:52:08

Resolution: invalid
