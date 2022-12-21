# Issue 6267: Same typesetting for two different variables:

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-06-12 15:19:15

Assignee: cwitty

CC:  mvngu

Keywords: latex, variables

Sage (4.0.1) typesets two different variables as same latex string


```
var('xi, xi_')
latex(xi)
\xi
latex(xi_)
\xi
```



---

Comment by jason created at 2009-06-12 18:06:19

Is this a bug?  I thought it was a design decision.


---

Comment by jason created at 2009-06-12 18:07:18

Note the following choice Sage makes (by design):


```
sage: latex(var('x0'))
x_{0}
sage: latex(var('x_0'))
x_{0}
```



---

Comment by gmhossain created at 2009-06-12 22:24:12

Changing priority from major to trivial.


---

Comment by gmhossain created at 2009-06-12 22:24:12

I agree. Sage does typeset two different objects as same latex string
by design. Sorry for the false alarm.


---

Comment by mpatel created at 2010-02-02 05:01:50

Should we close this?


---

Comment by mvngu created at 2010-02-02 05:04:52

Resolution: invalid
