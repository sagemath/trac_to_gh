# Issue 2035: sage-2.10.1.rc5: transform.pyx is now broken (probably caused by other fixes)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-03 00:14:24

Assignee: was


```
sage -t  devel/sage-main/sage/plot/plot3d/transform.pyx     **********************************************************************
File "transform.pyx", line 212:
    sage: m
Expected: 
    [                                       (1 - cos(theta))*x^2 + cos(theta) (-sin(theta)*abs(z)^3 - (cos(theta) - 1)*x*z^2*sqrt(-z^2 - x^2 + 1))/z^2  (sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z)^3 + (1 - cos(theta))*x*z^4)/z^3]
    [             sin(theta)*abs(z) + (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1)                          (cos(theta) - 1)*z^2 + (cos(theta) - 1)*x^2 + 1     (-sin(theta)*x*abs(z) - (cos(theta) - 1)*z^2*sqrt(-z^2 - x^2 + 1))/z]
    [    (-sin(theta)*sqrt(-z^2 - x^2 + 1)*abs(z) - (cos(theta) - 1)*x*z^2)/z      (sin(theta)*x*abs(z) - (cos(theta) - 1)*z^2*sqrt(-z^2 - x^2 + 1))/z                                        (1 - cos(theta))*z^2 + cos(th
eta)]
Got:
    [                                              (1 - cos(theta))*x^2 + cos(theta)                  (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1) - sin(theta)*sqrt(z^2)          (sin(theta)*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) + 
(1 - cos(theta))*x*z^2)/z]
    [                 sin(theta)*sqrt(z^2) + (1 - cos(theta))*x*sqrt(-z^2 - x^2 + 1)                                 (cos(theta) - 1)*z^2 + (cos(theta) - 1)*x^2 + 1 (-(cos(theta) - 1)*z*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) - 
sin(theta)*x*z)/sqrt(z^2)]
    [        (-sin(theta)*sqrt(-z^2 - x^2 + 1)*sqrt(z^2) - (cos(theta) - 1)*x*z^2)/z  (sin(theta)*x*z - (cos(theta) - 1)*z*sqrt(-z^2 - x^2 + 1)*sqrt(z^2))/sqrt(z^2)                                               (1 - cos
(theta))*z^2 + cos(theta)]
**********************************************************************
1 items had failures:
   1 of  25 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_transform.pyx
```



---

Attachment


---

Comment by was created at 2008-02-03 00:46:15

Resolution: fixed
