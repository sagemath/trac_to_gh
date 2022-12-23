# Issue 1227: 2.8.13.rc1: sage/rings/polynomial/multi_polynomial_ideal.py doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/1227

Original creator: mabshoff

Original creation time: 2007-11-20 23:01:43

Assignee: malb

With Linux x86, FC7 we get:

```
[jaap@paix sage-2.8.13.rc1]$ ./sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py
sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py**********************************************************************
File "multi_polynomial_ideal.py", line 376:
     sage: GB.triangular_decomposition('singular:triangLfak')
Expected:
     [Ideal (a - 1, b - 1, c - 1, d^2 + 3*d + 1, e + d + 3) of
     Multivariate Polynomial Ring in e, d, c, b, a over
     Rational Field, Ideal (a - 1, b - 1, c^2 + 3*c + 1, d + c
     + 3, e - 1) of Multivariate Polynomial Ring in e, d, c, b,
     a over Rational Field, Ideal (a - 1, b^4 + b^3 + b^2 + b +
     1, c - b^2, d - b^3, e + b^3 + b^2 + b + 1) of
     Multivariate Polynomial Ring in e, d, c, b, a over
     Rational Field, Ideal (a - 1, b^2 + 3*b + 1, c + b + 3, d
     - 1, e - 1) of Multivariate Polynomial Ring in e, d, c, b,
     a over Rational Field, Ideal (a^4 + a^3 + a^2 + a + 1, b -
     1, c + a^3 + a^2 + a + 1, d - a^3, e - a^2) of
     Multivariate Polynomial Ring in e, d, c, b, a over
     Rational Field, Ideal (a^4 + a^3 + a^2 + a + 1, b - a, c -
     a, d^2 + 3*d*a + a^2, e + d + 3*a) of Multivariate
     Polynomial Ring in e, d, c, b, a over Rational Field,
     Ideal (a^4 + a^3 + a^2 + a + 1, b - a, c^2 + 3*c*a + a^2,
     d + c + 3*a, e - a) of Multivariate Polynomial Ring in e,
     d, c, b, a over Rational Field, Ideal (a^4 + a^3 + a^2 + a
     + 1, b^3 + b^2*a + b^2 + b*a^2 + b*a + b + a^3 + a^2 + a +
     1, c + b^2*a^3 + b^2*a^2 + b^2*a + b^2, d - b^2*a^2 -
     b^2*a - b^2 - b*a^2 - b*a - a^2, e - b^2*a^3 + b*a^2 + b*a
     + b + a^2 + a) of Multivariate Polynomial Ring in e, d, c,
     b, a over Rational Field, Ideal (a^4 + a^3 + a^2 + a + 1,
     b^2 + 3*b*a + a^2, c + b + 3*a, d - a, e - a) of
     Multivariate Polynomial Ring in e, d, c, b, a over
     Rational Field, Ideal (a^4 - 4*a^3 + 6*a^2 + a + 1, 11*b^2
     - 6*b*a^3 + 26*b*a^2 - 41*b*a + 4*b + 8*a^3 - 31*a^2 +
     40*a + 24, 11*c + 3*a^3 - 13*a^2 + 26*a - 2, 11*d + 3*a^3
     - 13*a^2 + 26*a - 2, 11*e + 11*b - 6*a^3 + 26*a^2 - 41*a +
     4) of Multivariate Polynomial Ring in e, d, c, b, a over
     Rational Field, Ideal (a^4 + a^3 + 6*a^2 - 4*a + 1, 11*b^2
     - 6*b*a^3 - 10*b*a^2 - 39*b*a - 2*b - 16*a^3 - 23*a^2 -
     104*a + 24, 11*c + 3*a^3 + 5*a^2 + 25*a + 1, 11*d + 3*a^3
     + 5*a^2 + 25*a + 1, 11*e + 11*b - 6*a^3 - 10*a^2 - 39*a -
     2) of Multivariate Polynomial Ring in e, d, c, b, a over
     Rational Field, Ideal (a^2 + 3*a + 1, b - 1, c - 1, d - 1,
     e + a + 3) of Multivariate Polynomial Ring in e, d, c, b,
     a over Rational Field, Ideal (a^2 + 3*a + 1, b + a + 3, c
     - 1, d - 1, e - 1) of Multivariate Polynomial Ring in e,
     d, c, b, a over Rational Field]
Got:
     [Ideal (a - 1, b - 1, c - 1, d^2 + 3*d + 1, e + d + 3) of Multivariate Polynomial Ring in e, d, c, b, a over Rational Field, Ideal (a - 1, b - 1, c^2 + 3*c 
+ 1, d + c + 3, e - 1) of Multivariate Polynomial Ring in e, d, c, b, a over Rational Field, Ideal (a - 1, b^4 + b^3 + b^2 + b + 1, c - b^2, d - b^3, e + b^3 + 
b^2 + b + 1) of Multivariate Polynomial Ring in e, d, c, b, a over Rational Field, Ideal (a - 1, b^2 + 3*b + 1, c + b + 3, d - 1, e - 1) of Multivariate 
Polynomial Ring in e, d, c, b, a over Rational Field, Ideal (a^4 + a^3 + a^2 + a + 1, b - 1, c + a^3 + a^2 + a + 1, d - a^3, e - a^2) of Multivariate Polynomial 
Ring in e, d, c, b, a over Rational Field, Ideal (a^4 + a^3 + a^2 + a + 1, b - a, c - a, d^2 + 3*d*a + a^2, e + d + 3*a) of Multivariate Polynomial Ring in e, 
d, c, b, a over Rational Field, Ideal (a^4 + a^3 + a^2 + a + 1, b - a, c^2 + 3*c*a + a^2, d + c + 3*a, e - a) of Multivariate Polynomial Ring in e, d, c, b, a 
over Rational Field, Ideal (a^4 + a^3 + a^2 + a + 1, b^3 + b^2*a + b^2 + b*a^2 + b*a + b + a^3 + a^2 + a + 1, c + b^2*a^3 + b^2*a^2 + b^2*a + b^2, d - b^2*a^2 - 
b^2*a - b^2 - b*a^2 - b*a - a^2, e - b^2*a^3 + b*a^2 + b*a + b + a^2 + a) of Multivariate Polynomial Ring in e, d, c, b, a over Rational Field, Ideal (a^4 + a^3 
+ a^2 + a + 1, b^2 + 3*b*a + a^2, c + b + 3*a, d - a, e - a) of Multivariate Polynomial Ring in e, d, c, b, a over Rational Field, Ideal (a^4 + a^3 + 6*a^2 - 
4*a + 1, 11*b^2 - 6*b*a^3 - 10*b*a^2 - 39*b*a - 2*b - 16*a^3 - 23*a^2 - 104*a + 24, 11*c + 3*a^3 + 5*a^2 + 25*a + 1, 11*d + 3*a^3 + 5*a^2 + 25*a + 1, 11*e + 
11*b - 6*a^3 - 10*a^2 - 39*a - 2) of Multivariate Polynomial Ring in e, d, c, b, a over Rational Field, Ideal (a^4 - 4*a^3 + 6*a^2 + a + 1, 11*b^2 - 6*b*a^3 + 
26*b*a^2 - 41*b*a + 4*b + 8*a^3 - 31*a^2 + 40*a + 24, 11*c + 3*a^3 - 13*a^2 + 26*a - 2, 11*d + 3*a^3 - 13*a^2 + 26*a - 2, 11*e + 11*b - 6*a^3 + 26*a^2 - 41*a + 
4) of Multivariate Polynomial Ring in e, d, c, b, a over Rational Field, Ideal (a^2 + 3*a + 1, b - 1, c - 1, d - 1, e + a + 3) of Multivariate Polynomial Ring 
in e, d, c, b, a over Rational Field, Ideal (a^2 + 3*a + 1, b + a + 3, c - 1, d - 1, e - 1) of Multivariate Polynomial Ring in e, d, c, b, a over Rational Field]
**********************************************************************
1 items had failures:
    1 of   4 in __main__.example_9
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_multi_polynomial_ideal.py
          [4.9 s]
exit code: 256
```

Same things happens on OSX 10.5, but not on sage.math.


---

Comment by cwitty created at 2007-11-21 06:30:40

I hand-checked, and the above difference is just an ordering difference.


---

Attachment

maybe a fix ?


---

Comment by mabshoff created at 2007-11-21 14:28:32

Let's hope so. I had to merge the doctest bit of the patch manually, but the doctest does pass on sage.math [which it did before anyway]

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-21 14:49:14

Resolution: fixed


---

Comment by mabshoff created at 2007-11-21 14:49:14

Merged in 2.8.13.rc2.
