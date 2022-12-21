# Issue 9828: Implement implicitly multiplied output

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-08-28 01:11:35

Assignee: was

With `implicit_multiplication(True)`, we can enter expressions using spaces instead of `*` to separate multiplied subexpressions:


```python
sage: var('x, y, z')
sage: implicit_multiplication(True)
sage: 3 x^4 y + 2 z sin(x z 3 y) - 3 y^2
3*x^4*y - 3*y^2 + 2*z*sin(3*x*y*z)
```


This works similarly for polynomials.

But it's not yet possible to set an option so that Sage automatically postparses the output to multiply implicitly.  For example,


```python
sage: R.<a,b,c> = QQ[]; R
Multivariate Polynomial Ring in a, b, c over Rational Field
sage: implicit_multiplication_output(True)    # not implemented!
sage: R.random_element()
1/7 a b - 1/4 a c - c^2 + c 
```


Ideally, we would be able to use the output in later inputs with little or no modification.

[AskSage question](http://ask.sagemath.org/question/46/is-it-possible-to-get-implicitly-multiplied-output) (by me).


---

Comment by mpatel created at 2010-08-28 01:23:59

See [/sage/misc/preparser.py`@`13719#L1209](../tree/master//sage/misc/preparser.py`@`13719#L1209) for the input transformation.
