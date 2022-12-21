# Issue 307: vector/vector multiplication should return a scalar

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2007-03-04 06:20:56

Assignee: was

Currently vector/vector multiplication returns a vector, when it should just return a scalar:

```
sage: b = vector([0,1,2]); u= vector([1,3,5]);
sage: u*b
(0, 3, 10)
```


In this particular case, the answer should just be 13
 


---

Comment by was created at 2007-03-04 21:22:08

No it shouldn't.  If you want the dot product, you should do this:

```
sage:  b = vector([0,1,2]); u= vector([1,3,5]);
sage: b.dot_product(u)
13
```



---

Comment by was created at 2007-03-04 21:22:08

Resolution: invalid
