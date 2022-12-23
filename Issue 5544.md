# Issue 5544: multipolynomial __call__ not consistant

Issue created by migration from https://trac.sagemath.org/ticket/5544

Original creator: robertwb

Original creation time: 2009-03-17 06:21:40

Assignee: tbd


```
sage: parent(RR['x,y'].gen(1)(0,CC.0))
Complex Field with 53 bits of precision
sage: parent(RR['x,y'](0)(0,0))
Integer Ring
sage: parent(RR['x,y'](0)(0,CC.0))
Integer Ring
sage: parent(RR['x,y'](1)(0,CC.0))
Real Field with 53 bits of precision

sage: parent(QQ['x,y'](1)(0,CC.0))
Rational Field
sage: parent(QQ['x,y'](0)(0,0))
Rational Field
sage: parent(QQ['x,y'](0)(0,CC.0))
Rational Field
sage: parent(QQ['x,y'].gen(1)(0,CC.0))
Complex Field with 53 bits of precision
```


The result should not depend on the specific polynomial, only on its parent and the parent of the inputs. 

Univariate ones get it right:


```
sage: sage: parent(RR['x'](0)(0))
Real Field with 53 bits of precision
sage: sage: parent(RR['x'](0)(CC.0))
Complex Field with 53 bits of precision
```



---

Comment by cwitty created at 2009-03-17 06:25:18

According to this definition, there are bugs in univariate polynomials as well:

```
sage: parent(QQ['x'](0)(1))
Integer Ring
sage: parent(QQ['x'].gen(0)(1))
Rational Field
```

