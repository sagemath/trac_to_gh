# Issue 82: bug in eigenvalues over a number field

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2006-09-24 19:43:16

Assignee: was

sage: M = MatrixSpace(RationalField(),2,2)

sage: A = M([1,-4,1, -1])

sage: p = A.charpoly()

sage: K = NumberField(p,'alpha')

sage: M = MatrixSpace(K,2,2)

sage: A = M([1,-4,1, -1])

sage: A.eigenvectors()

fails at the last step. However, 

sage: M = MatrixSpace(RationalField(),2,2)

sage: A = M([1,-4,1, -1])

sage: A.eigenvectors()

 [(1, a - 1)]

works, though "a" is undefined.


---

Comment by was created at 2006-09-25 23:12:32

Note.  In the second example a is not undefined.  It's the print representation of the generator
of a number field.  It's not supposed to suddenly be injected into the current scope. 

```
sage: V =A.eigenvectors()
sage: V[0][1].parent()
 Number Field in a with defining polynomial x^2 + 3
```



---

Comment by was created at 2007-01-12 22:20:47

Resolution: fixed


---

Comment by was created at 2007-01-12 22:20:47

It now works (though notation slightly different now):

```
sage: M = MatrixSpace(RationalField(),2,2)
sage: A = M([1,-4,1, -1])
sage: p = A.charpoly()
sage: K = NumberField(p,'alpha')
sage: M = MatrixSpace(K,2,2)
sage: A = M([1,-4,1, -1])
sage: A.eigenspaces()
[
(alpha, [
(1, alpha - 1)
]),
(-alpha, [
(1, -alpha - 1)
])
]
```

