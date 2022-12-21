# Issue 5605: Construct Color objects using hsl and hsv values

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-03-24 21:36:56

Assignee: was

CC:  mvngu

See http://en.wikipedia.org/wiki/HSL_and_HSV

See also this thread, where the idea came up: http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675


---

Comment by mpatel created at 2009-11-16 05:39:54

On the RGB converters:

```python
sage: from sage.plot.colors import rgbcolor, to_mpl_color
sage: rgbcolor('#ffffff')
(0.99609375, 0.99609375, 0.99609375)
sage: to_mpl_color('#ffffff')
(1.0, 1.0, 1.0)
```

Both

```
Color(rgbcolor(hx)).html_color() == hx
Color(to_mpl_color(hx)).html_color() == hx
```

are `True` for all hex colors `hx`, but we should fix `rgbcolor` and/or unify it with `to_mpl_color`.  I'll do this as part of #5601's patch, which may also cover #5602 and, perhaps, this ticket.


---

Comment by mpatel created at 2009-11-18 04:42:11

See the patch at #5601.


---

Comment by jason created at 2010-05-11 20:37:23

This works now.  From the doctests of sage.plot.colors.Color:


```
          sage: Color(0.5, 1.0, 1, space='hsv')
          RGB color (0.0, 1.0, 1.0)
          sage: Color(0.25, 0.5, 0.5, space='hls')
          RGB color (0.50000000000000011, 0.75, 0.25)
```


So this should be closed.


---

Comment by mvngu created at 2010-05-11 20:53:43

Resolution: fixed


---

Comment by mvngu created at 2010-05-11 20:53:43

Close as fixed:


```
[mvngu`@`sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Color(0.5, 1.0, 1, space='hsv')
RGB color (0.0, 1.0, 1.0)
sage: Color(0.5, 1.0, 1, space='hls')
RGB color (1.0, 1.0, 1.0)
sage: Color(0.25, 0.5, 0.5, space='hls')
RGB color (0.50000000000000011, 0.75, 0.25)
sage: Color(0.25, 0.5, 0.5, space='hsv')
RGB color (0.375, 0.5, 0.25)
```

