# Issue 194: another ZZ[x] crash

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-16 05:45:56

Assignee: somebody


```
sage: R.<x> = ZZ['x']
sage: x^3 % 2
DivRem: quotient undefined over ZZ
/Users/nalexand/Devel/sage/local/bin/sage-sage: line 174: 13174 Abort
trap              sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"
 
Yikes!
Nick
```



---

Comment by was created at 2007-01-25 19:09:10

Resolution: fixed


---

Comment by was created at 2007-01-25 19:09:10

Fixed by re-enabling sig handling behavior.
