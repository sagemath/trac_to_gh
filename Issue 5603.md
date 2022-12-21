# Issue 5603: make a .mix() method for Sage color objects

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-03-24 21:29:56

Assignee: was

CC:  mvngu

See the end of http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675

We could also call it .blend() to agree with MMA's terminology:

http://reference.wolfram.com/mathematica/ref/Blend.html


---

Comment by jason created at 2010-05-11 20:33:30

This is now implemented as "blend":


```
sage: sage.plot.colors.red.blend(sage.plot.colors.blue)
RGB color (0.5, 0.0, 0.5)

```


So this ticket should be closed.


---

Comment by mvngu created at 2010-05-11 20:39:29

Close as fixed:


```
[mvngu`@`sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: b = sage.plot.colors.blue
sage: r = sage.plot.colors.red
sage: g = sage.plot.colors.green
sage: b.blend(r)
RGB color (0.5, 0.0, 0.5)
sage: r.blend(b)
RGB color (0.5, 0.0, 0.5)
sage: r.blend(g)
RGB color (0.5, 0.25098039215686274, 0.0)
sage: g.blend(r)
RGB color (0.5, 0.25098039215686274, 0.0)
sage: g.blend(b)
RGB color (0.0, 0.25098039215686274, 0.5)
sage: b.blend(g)
RGB color (0.0, 0.25098039215686274, 0.5)
```



---

Comment by mvngu created at 2010-05-11 20:39:29

Resolution: fixed
