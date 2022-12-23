# Issue 1041: latex representation of fractional ideals in a number field is totally stupid

Issue created by migration from https://trac.sagemath.org/ticket/1041

Original creator: was

Original creation time: 2007-10-31 20:47:32

Assignee: was


```
sage: K.<a> = NumberField(x^2 + 1)
sage: latex(K.fractional_ideal(3, a))
\left(3, a\right)\mathbf{Q}[a]/(a^{2} + 1)     
```


'nuff said. 


---

Comment by was created at 2007-11-03 23:18:49

Resolution: fixed


---

Attachment
