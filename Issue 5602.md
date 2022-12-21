# Issue 5602: make .lighter() and .darker() methods for Sage Color objects

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-03-24 21:28:09

Assignee: was

CC:  mvngu

See the end of http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675

For reference, here is what MMA does: 

http://reference.wolfram.com/mathematica/ref/Darker.html

http://reference.wolfram.com/mathematica/ref/Lighter.html


---

Comment by jason created at 2009-03-24 21:28:20

Changing priority from major to minor.


---

Comment by mpatel created at 2009-11-18 04:42:25

See the patch at #5601.


---

Comment by jason created at 2010-05-11 20:31:43

This works now:


```
sage: sage.plot.colors.red.lighter()
RGB color (1.0, 0.33333333333333331, 0.33333333333333331)
sage: sage.plot.colors.red.darker()
RGB color (0.66666666666666674, 0.0, 0.0)
```


So this ticket should be closed.


---

Comment by mvngu created at 2010-05-11 20:35:37

Resolution: fixed


---

Comment by mvngu created at 2010-05-11 20:35:37

Close as fixed:


```sh
[mvngu`@`sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: r = sage.plot.colors.red
sage: r
RGB color (1.0, 0.0, 0.0)
sage: r.darker()
RGB color (0.66666666666666674, 0.0, 0.0)
sage: r.lighter()
RGB color (1.0, 0.33333333333333331, 0.33333333333333331)
```

