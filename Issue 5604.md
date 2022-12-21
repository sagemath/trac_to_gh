# Issue 5604: average Color objects when adding them together

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-03-24 21:30:49

Assignee: was

CC:  mvngu

This would make it easy to create purple, for example, as red+blue.


---

Comment by jason created at 2010-05-11 20:34:39

This is done now:


```
sage: sage.plot.colors.red+sage.plot.colors.blue
RGB color (0.5, 0.0, 0.5)

```


So this ticket should be closed.


---

Comment by mvngu created at 2010-05-11 20:49:39

This looks like fixed, but the averaging operator "+" is binary:

```
[mvngu`@`sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: r = sage.plot.colors.red
sage: g = sage.plot.colors.green
sage: b = sage.plot.colors.blue
sage: r; g; b
RGB color (1.0, 0.0, 0.0)
RGB color (0.0, 0.50196078431372548, 0.0)
RGB color (0.0, 0.0, 1.0)
sage: r + g; r + b
RGB color (0.5, 0.25098039215686274, 0.0)
RGB color (0.5, 0.0, 0.5)
sage: (r + g) + b; r + g + b
RGB color (0.25, 0.12549019607843137, 0.5)
RGB color (0.25, 0.12549019607843137, 0.5)
sage: (r + b) + g; r + b + g
RGB color (0.25, 0.25098039215686274, 0.25)
RGB color (0.25, 0.25098039215686274, 0.25)
sage: (g + b) + r; g + b + r
RGB color (0.5, 0.12549019607843137, 0.25)
RGB color (0.5, 0.12549019607843137, 0.25)
```

For more than two operands, I thought that "+" would average over the number of operands. Instead, "+" averages the first two, then average the result with the last operand.


---

Comment by mvngu created at 2010-05-11 20:49:39

Resolution: fixed


---

Comment by jason created at 2010-05-11 21:10:21

That's because the blending is not associative.  We are just providing a simple way to blend colors together.  That's a limitation of the method---is there a reason why we should insist on the addition being associative?

Mixing colors and color theory in general is a very involved topic; we are just scratching the surface here with suboptimal, but still useful, methods and shortcuts.


---

Comment by mvngu created at 2010-05-11 21:14:29

Replying to [comment:4 jason]:
> That's because the blending is not associative.  We are just providing a simple way to blend colors together.  That's a limitation of the method---is there a reason why we should insist on the addition being associative?

No reason I can think of. My surprise as expressed above has more to do with my lack of understanding.
