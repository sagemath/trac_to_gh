# Issue 650: serious modular forms bug

Issue created by migration from https://trac.sagemath.org/ticket/650

Original creator: was

Original creation time: 2007-09-13 18:47:19

Assignee: was or craigcitro


```
sage: d = ModularSymbols(Gamma0(43), 2, sign=1).cuspidal_subspace().new_subspace().decomposition()
sage: d

[
Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 4 for Gamma_0(43) of weight 2 with sign 1 over Rational Field,
Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 4 for Gamma_0(43) of weight 2 with sign 1 over Rational Field
]
sage: for a in d: print a.q_eigenform(10)
....:
q - 2*q^2 - 2*q^3 + 2*q^4 - 4*q^5 + 4*q^6 + q^9 + O(q^10)
q + alpha*q^2 + -alpha*q^3 + (-alpha + 2)*q^5 + -2*q^6 + (alpha - 2)*q^7 + -2*alpha*q^8 + -q^9 + O(q^10)
```



---

Comment by craigcitro created at 2007-09-13 23:07:43

Added a patch that turns this into a NotImplementedError. The problem is that the code for computing newspaces of modular forms is written ... oddly. We're going to fix this in the near future, but this will at least stop giving wrong answers in the interim.


---

Comment by craigcitro created at 2007-10-02 00:38:50

Changing assignee from was or craigcitro to craigcitro.


---

Comment by craigcitro created at 2007-10-02 00:38:50

Changing status from new to assigned.


---

Comment by craigcitro created at 2007-10-12 21:58:49

Actually, I discovered a second place where this needed to be turned into a NotImplementedError. I replaced the above bundle with a fix for both.


---

Attachment


---

Comment by was created at 2007-10-13 06:00:06


```
22:55 < cwitty_> #650: applies cleanly, but the doctests fail.  It's odd...unless Mercurial is screwing 
                 up the history somehow, it looks like the doctests never could have worked after this 
                 patch.
22:57 < williamstein> I think the doctests were wrong.
22:57 < williamstein> I.e., they claimed a result that was mathematically wrong.
22:59 < cwitty_> Right.  But the patch comments out the doctest "N = ...", but leaves the next doctest 
                 alone, "N.basis()".  Why didn't he comment out that doctest too?
22:59 < williamstein> It's a mistake on his part.
```



---

Comment by craigcitro created at 2007-10-14 07:52:03

As the comments above point out, I was too hasty in commenting out the other doctests, and didn't test it due to lack of time. I updated the patch to comment out the last three doctests I missed on the first run, and I'm about to upload it.


---

Comment by was created at 2007-10-19 01:48:40

Resolution: fixed


---

Attachment
