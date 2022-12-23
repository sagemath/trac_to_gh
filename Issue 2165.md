# Issue 2165: MPolynomialRing(BooleanPolynomial) not as general as it should be

Issue created by migration from https://trac.sagemath.org/ticket/2165

Original creator: ncalexan

Original creation time: 2008-02-14 23:35:39

Assignee: malb

Keywords: polybori boolean polynomial coercion call

Coercion of BooleanPolynomials in subsets of variables should be allowed.

See #2055 with reference to the following IRC snippet:


```
ncalexan: malb: in 2055, is this right?
[3:26pm] ncalexan: if PY_TYPE_CHECK(element, BooleanPolynomial) and \
[3:26pm] ncalexan:  578              element.parent().ngens() == _ring.N and \
[3:26pm] ncalexan:  579              element.parent().variable_names() == self.variable_names():
[3:26pm] ncalexan: This is in a __call__, right?
[3:26pm] ncalexan: Shouldn't the variable names just be a subset?
[3:26pm] ncalexan: And then, even just the names in the polynomial?
[3:26pm] malb: it could be that general, yes
[3:26pm] ncalexan: eg, sage: QQ['x'](QQ['x', 'y'].0)
[3:26pm] ncalexan: x
[3:26pm] ncalexan: sage: QQ['y', 'x'](QQ['x', 'y'].0)
[3:26pm] ncalexan: x
[3:27pm] ncalexan: It's inconsistent if not.  Other than that, I say apply.
[3:27pm] ncalexan: Hopefully it's easy to tell what vars actually appear in any partic. poly.
[3:27pm] malb: to be honest, I'd like to have it applied and open another ticket for that
[3:28pm] malb: because you definitely want to solve equations in MPolys with PolyBoRi
[3:28pm] malb: and your rings will be identical except for the implementation
[3:28pm] ncalexan: mabshoff: is that okay with you?  Apply and another ticket for additional generality?
[3:28pm] mabshoff: Sure
```



---

Comment by malb created at 2008-09-20 15:53:35

Changing status from new to assigned.
