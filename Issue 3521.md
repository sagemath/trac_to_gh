# Issue 3521: Atkin-Lehner operator doesn't square to 1

Issue created by migration from https://trac.sagemath.org/ticket/3521

Original creator: roed

Original creation time: 2008-06-27 14:02:05

Assignee: craigcitro

Keywords: modular symbols, atkin-lehner

The following should produce the identity matrix:

```
sage: e = (DirichletGroup(13).0)^2
sage: M = ModularSymbols(e, 2)
sage: M.atkin_lehner_operator().matrix()^2
[         1          0          0          0]
[         0          1          0          0]
[-zeta6 - 1          0          1  zeta6 + 1]
[ zeta6 + 1          0          0     -zeta6]



---

Comment by was created at 2008-06-27 14:03:37

For me this illustrates the bug more clearly:

```
sage: M = ModularSymbols(Gamma1(13),2)
sage: M
Modular Symbols space of dimension 15 for Gamma_1(13) of weight 2 with sign 0 and over Rational Field
sage: M.atkin_lehner_operator(13).matrix()^2 == 1
True
sage: M = ModularSymbols(DirichletGroup(13).0^2)
sage: M.atkin_lehner_operator(13).matrix()^2 == 1
False
sage: M.atkin_lehner_operator(13).matrix()^2 

[         1          0          0          0]
[         0          1          0          0]
[-zeta6 - 1          0          1  zeta6 + 1]
[ zeta6 + 1          0          0     -zeta6]
```



---

Attachment

WARNING:

The atkin-lehner operator does *not* leave the space $M_k(N,\chi)$ invariant unless $\chi$ is quadratic. Really it sends $M_k(N,\chi)$ to $M_k(N,\chibar)$.   So Sage should give an error message when $\chi$ is not quadratic.


---

Attachment


---

Comment by craigcitro created at 2008-06-29 02:05:35

Looks good. I added a patch that actually corrects a bug (some statements were out of order), and just reformats/corrects typos. This is ready to go.


---

Comment by mabshoff created at 2008-07-02 19:30:33

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-02 19:30:33

Resolution: fixed
