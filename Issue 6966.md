# Issue 6966: Shimura subgroup

Issue created by migration from Trac.

Original creator: syazdani

Original creation time: 2009-09-20 03:51:08

Assignee: craigcitro

Keywords: shimura subgroup

small patch to compute the Shimura subgroup of an Abelian subvariety of $J_0(N)$.


```
J=J0(11)
J.shimura_subgroup()

Finite subgroup with invariants [5] over QQ of Abelian variety J0(11) of dimension 1
```




---

Comment by syazdani created at 2009-09-20 04:26:38

computes the Shimura subgroup of J0(N) and its subvarieties.


---

Attachment


---

Comment by mvngu created at 2009-09-22 22:09:19

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:36:46

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
