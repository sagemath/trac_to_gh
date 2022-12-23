# Issue 8878: Use Dijkstra to discover shortest coercion path

Issue created by migration from https://trac.sagemath.org/ticket/8878

Original creator: nthiery

Original creation time: 2010-05-04 23:35:06

Assignee: robertwb

CC:  sage-combinat

Keywords: coercion, morphism

In #7420, it was discussed that the current coercion model is using depth first search to find for coercion paths between different parents, and that it would be better to use breath-first / Dijkstra to get a shortest coercion path. For example, we obtained once a coercion path of length 20 among symmetric functions.

Patch under development on the Sage-Combinat server.

Note: the following issue is probably related:

```
A = CombinatorialFreeModule(QQ, ZZ, prefix = "A")
B = CombinatorialFreeModule(QQ, ZZ, prefix = "B")
C = CombinatorialFreeModule(QQ, ZZ, prefix = "C")
D = CombinatorialFreeModule(QQ, ZZ, prefix = "D")

def make_morph(X, Y):
    X.module_morphism(Y.monomial).register_as_coercion()

make_morph(A,B)
make_morph(B,A)

make_morph(C,A)

make_morph(D,C)

d = D.monomial(1)

A(d)
B(d)
```



---

Comment by nthiery created at 2010-05-04 23:36:02

Changing status from new to needs_work.


---

Comment by darij created at 2013-06-22 23:29:04

The link to sage-combinat is dead.

(Posting this mainly to get a CC on this ticket.)
