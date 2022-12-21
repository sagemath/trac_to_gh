# Issue 192: polynomial arithmetic bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-15 08:40:06

Assignee: was

From Nick A:

```
Here's a similar error.  I haven't tried with that patch, but my
spidey-sense suggests a different issue:
 
sage: R.<x> = Integers(5**2)['x']
sage: S.<xbar> = R.quo(x^5 - x + 1)
sage: (5*xbar + 1).lift() % 5
ZZ_p: division by non-invertible element
/Users/nalexand/Devel/sage/local/bin/sage-sage: line 174: 10371 Abort
trap              sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"
 
Nick
```



---

Comment by was created at 2007-01-15 08:40:12

Changing assignee from was to somebody.


---

Comment by was created at 2007-01-15 08:40:12

Changing component from algebraic geometry to basic arithmetic.


---

Comment by was created at 2007-01-19 09:54:51

This will be fixed automatically by fixing trac #196.


---

Comment by was created at 2007-01-21 21:51:17

Fixed by fixing trac #196.


---

Comment by was created at 2007-01-21 21:51:17

Resolution: fixed
