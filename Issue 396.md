# Issue 396: vector-vector produc ts

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-06-28 23:46:25

Assignee: was

Multiplying a mix of vectors and matrices is allowed presently in sage, but it is not associative:

```
v=vector([1,2,3])
M=matrix([[1,0],[0,1],[1,1]])
w=vector([1,2])

print v*M*w
print (v*M)*w
print v*(M*w)
///
(4, 10)
(4, 10)
(1, 4, 9)
```

It is a combination of vectors not knowing whether they are row- or column vectors (probably good)
and that v * w has the odd meaning of doing a component-wise multiplication. Perhaps it inherits the method from lists or something? It would be safest to explicitly cast an error if one tries to multiply vectors.


---

Comment by mhansen created at 2007-09-06 17:31:07

The multiplication comes from FreeModule:

sage: F = FreeModule(QQ, 3)
sage: a = F([1,2,3])
sage: b = F([1,2,3])
sage: a*b
(1, 4, 9)

I think that this is wrong.


---

Comment by was created at 2007-09-06 20:59:33

Changing component from algebraic geometry to linear algebra.


---

Attachment


---

Comment by was created at 2007-09-07 00:04:44

Resolution: fixed
