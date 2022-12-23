# Issue 1827: plot3d/transform.pyx test failure

Issue created by migration from https://trac.sagemath.org/ticket/1827

Original creator: gfurnish

Original creation time: 2008-01-18 05:46:27

Assignee: was

Failure on make check

sage -t  devel/sage-main/sage/plot/plot3d/transform.pyx     �[?1034h**********************************************************************
File "transform.pyx", line 213:
    sage: m
Expected:
    [                                                                                                                                        (x<sup>2*z</sup>2 - (cos(theta)*x^2 - cos(theta))*z<sup>2)/z</sup>2                                                                                                          (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x*abs(z) - x*abs(z)) - sin(theta)*z^2)/abs(z)                                                                                                (-cos(theta)*x*z^2*abs(z) + x*z^2*abs(z) + sin(theta)*z<sup>2*sqrt(-z</sup>2 - x^2 + 1))/(z*abs(z))]
    [                                                                                                            (sin(theta)*z^2*abs(z) - sqrt(-z^2 - x^2 + 1)*(cos(theta)*x*z^2 - x*z<sup>2))/z</sup>2                                              ((-(x^2 + cos(theta) - 1)*z^2 - x^4 + 2*x^2 - 1)*abs(z) - (-cos(theta)*x<sup>2*z</sup>2 - cos(theta)*x^4 + cos(theta)*x<sup>2)*abs(z))/((x</sup>2 - 1)*abs(z)) (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x<sup>2*z</sup>2*abs(z) + (-x^2 - cos(theta) + 1)*z^2*abs(z)) + sin(theta)*x*z^4 - z<sup>2*(sin(theta)*x*z</sup>2 + sin(theta)*x^3 - sin(theta)*x))/((x^2 - 1)*z*abs(z))]
    [                                                                                                               (-sin(theta)*z*sqrt(-z^2 - x^2 + 1)*abs(z) - cos(theta)*x*z^3 + x*z<sup>3)/z</sup>2                                               (-sqrt(-z^2 - x^2 + 1)*(cos(theta)*x^2*z*abs(z) + (-x^2 - cos(theta) + 1)*z*abs(z)) - (sin(theta)*x - sin(theta)*x<sup>3)*z)/((x</sup>2 - 1)*abs(z))                                                                        (((x^2 + cos(theta) - 1)*z^2 + cos(theta)*x^2 - cos(theta))*abs(z) - cos(theta)*x<sup>2*z</sup>2*abs(z))/((x^2 - 1)*abs(z))]
Got:
    [                                                                                                                                                                                                              sage17*cos(theta)*sqrt(1 - x^2) + sage13*sage76                                                                                                                                                                               (sqrt(-z^2 - x^2 + 1)*(sage76*abs(z) - cos(theta)*x*z) - sin(theta)*z*abs(z))/z                                                                                                                                                                               (sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z) + sage76*z*abs(z) - cos(theta)*x*z^2)/z]
    [                                                                                                                 (sqrt(1 - x<sup>2)*sqrt(-z</sup>2 - x^2 + 1)*(sage17*cos(theta)*x*abs(z) + sage13*sage80*z) - sage17*sin(theta)*sqrt(1 - x<sup>2)*z</sup>2)/((x^2 - 1)*abs(z))                                          (-sqrt(1 - x<sup>2)*((-cos(theta)*x</sup>2*z^2 - cos(theta)*x^4 + cos(theta)*x^2)*abs(z) + cos(theta)*z^2*abs(z)) - ((sage80 - sage80*x<sup>2)*z</sup>2 - sage80*x^4 + 2*sage80*x^2 - sage80)*abs(z))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z)) (-sqrt(-z^2 - x^2 + 1)*(sqrt(1 - x<sup>2)*(cos(theta)*x</sup>2*z^2*abs(z) - cos(theta)*z^2*abs(z)) + (sage80*x^2 - sage80)*z^2*abs(z)) - sqrt(1 - x<sup>2)*(z</sup>2*(sin(theta)*x*z^2 + sin(theta)*x^3 - sin(theta)*x) - sin(theta)*x*z^4))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*z*abs(z))]
    [                                                                                                               (sqrt(1 - x^2)*(sage17*cos(theta)*x*z*abs(z) + sage13*sage80*z^2) + sage17*sin(theta)*sqrt(1 - x<sup>2)*z*sqrt(-z</sup>2 - x^2 + 1))/((x^2 - 1)*abs(z))                                                   (-sqrt(-z^2 - x^2 + 1)*(sqrt(1 - x<sup>2)*(cos(theta)*x</sup>2*z*abs(z) - cos(theta)*z*abs(z)) + (sage80*x^2 - sage80)*z*abs(z)) - sqrt(1 - x^2)*(sin(theta)*x - sin(theta)*x^3)*z)/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z))                                                                                       (sqrt(1 - x<sup>2)*((cos(theta)*z</sup>2 + cos(theta)*x^2 - cos(theta))*abs(z) - cos(theta)*x<sup>2*z</sup>2*abs(z)) + (sage80 - sage80*x<sup>2)*z</sup>2*abs(z))/(sqrt(1 - x<sup>2)*(x</sup>2 - 1)*abs(z))]
**********************************************************************

System is 64 bit gentoo, gcc 4.2.2


---

Comment by mabshoff created at 2008-01-18 05:47:32

Changing component from graphics to doctest.


---

Comment by mabshoff created at 2008-01-18 05:47:32

Changing assignee from was to failure.


---

Comment by mabshoff created at 2008-01-18 05:47:32

Changing priority from major to critical.


---

Attachment

this should completely fix the problem.  But I've only tested it on one 32-bit linux system.  it needs more testing


---

Comment by robertwb created at 2008-01-19 04:25:40

For _an_element_impl, it should return a very generic element. If it returns zero, then it may mess up the coercion model!


---

Comment by mabshoff created at 2008-01-19 04:30:48

Hi Robert,

can you provide a doctest that exposes the issue you describe?

Cheers,

Michael


---

Comment by was created at 2008-01-19 13:27:40

Resolution: fixed


---

Comment by robertwb created at 2008-01-19 19:41:49

OK, I take this back. 

It used to be that some multiplication code was written as 


```
def _lmul_(self, other):
    if not other:
        return other
    ...
```


This would succeed when other was ANY type with bool(other) == False, and an_element was used to construct `other` to pass in and try it out (in the action detection code) which would cause it to succeed and this "valid" action would get cached (resulting in a error or segfault when a non-zero `other` was passed. 

It now forces other to be an element of self.parent().base_ring(), which solves this problem.
