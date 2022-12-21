# Issue 2360: Strange Polynomial substitution problem

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-03-01 16:52:49

Assignee: was

I made a stupid error plugging a list into a polynomial, but it uncovered this very strange bug:


```
sage: R.<x,y,z,u,v,w>=ZZ[]
sage: P.<a>=ZZ[]
sage: e=[x^2,y^3]
sage: f=6*a^4
sage: f(x)
6*x^4
sage: f(e)
Exception exceptions.TypeError: "can't multiply sequence by non-int of type 'list'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand type(s) for *: 'NoneType' and 'NoneType'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored
sage: f(x)
Exception exceptions.TypeError: "can't multiply sequence by non-int of type 'list'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand type(s) for *: 'NoneType' and 'NoneType'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored
```


Notice that the plugging in the list seemed to ruin the polynomial good and proper.


---

Comment by jbmohler created at 2008-03-01 16:53:01

Changing assignee from was to somebody.


---

Comment by jbmohler created at 2008-03-01 16:53:01

Changing component from algebraic geometry to basic arithmetic.


---

Comment by jbmohler created at 2008-03-01 16:55:03

Ah, it's even easier.  No second mpoly ring required!


```
sage: P.<a>=ZZ[]
sage: f=6*a^4
sage: f(1)
6
sage: f([1,2,3])
Exception exceptions.TypeError: "can't multiply sequence by non-int of type 'list'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand type(s) for *: 'NoneType' and 'NoneType'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored
sage: f(1)  #  WHAT HAPPENED -- this worked before.
Exception exceptions.TypeError: "can't multiply sequence by non-int of type 'list'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand type(s) for *: 'NoneType' and 'NoneType'" in 'sage.rings.polynomial.polynomial_compiled.sqr_pd.eval' ignored
Exception exceptions.TypeError: "unsupported operand parent(s) for '*': 'Integer Ring' and '<type 'NoneType'>'" in 'sage.rings.polynomial.polynomial_compiled.mul_pd.eval' ignored
```



---

Comment by malb created at 2009-01-22 06:59:56

The attached patch fixes the issue. Credit goes to Tom Boothby too.


---

Comment by robertwb created at 2009-01-23 22:34:35

The patch fixes the issue, but I'd rather have the original error about multiplying lists propagate up instead of a generic "RuntimeError: Polynomial evaluation error in val()!"


---

Attachment


---

Comment by malb created at 2009-01-24 12:42:42

I updated the patch.


---

Comment by robertwb created at 2009-01-24 21:53:05

OK, that looks good.


---

Comment by mabshoff created at 2009-01-24 23:00:31

Merged in Sage 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 23:00:31

Resolution: fixed
