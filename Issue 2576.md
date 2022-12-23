# Issue 2576: preserve docstrings of decorated methods

Issue created by migration from https://trac.sagemath.org/ticket/2576

Original creator: was

Original creation time: 2008-03-17 18:50:10

Assignee: tba


```

Hi,

How does one preserve the behavior of docstrings when using
decorators?  I just noticed, for example, that I couldn't easily
access the docstring of various things in rings/polynomial/
multi_polynomial_ideal.py because they have been decorated.  It is
unclear to me how to easily fix that - does anyone know a simple
solution?

Thanks,
M. Hampton
```



---

Comment by was created at 2008-03-17 18:51:14

this fixes one particular instance of the problem


---

Attachment

To test the attached:

```
R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
p = z^2 + 1; q = z^3 + 2
I = (p*q^2, y-z^2)*R
pd = I.complete_primary_decomposition?
```



---

Comment by malb created at 2008-03-17 23:17:41

Michael Brickenstein on [sage-devel]:

```
By the way
wrapper.__name__=func.__name__
is usually also a good practice.
```



---

Comment by mabshoff created at 2008-03-18 00:31:51

Replying to [comment:1 was]:
> To test the attached:
> {{{
> R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
> p = z^2 + 1; q = z^3 + 2
> I = (p*q^2, y-z^2)*R
> pd = I.complete_primary_decomposition?
> }}}

To test you need 

```
R.<x,y,z> = PolynomialRing(QQ, 3, order='lex')
p = z^2 + 1; q = z^3 + 2
I = (p*q^2, y-z^2)*R
I.complete_primary_decomposition?
}}} 
At least I did. Anyway, the patch applies and does what it is supposed to do. Positive review.


---

Comment by mabshoff created at 2008-03-18 00:32:49

Resolution: fixed


---

Comment by mabshoff created at 2008-03-18 00:32:49

Merged in Sage 2.11.alpha0
