# Issue 320: RealField.is_field() is broken

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-03-14 04:58:31

Assignee: somebody


```
sage: RealField.is_field()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/gauss-manin-de/<ipython console> in <module>()

<type 'exceptions.TypeError'>: descriptor 'is_field' of 'sage.rings.ring.Field' object needs an argument

```




---

Comment by was created at 2007-03-21 22:49:19

Resolution: invalid


---

Comment by was created at 2007-03-21 22:49:19

This doesn't make any sense.  RealField is a function that returns a real field of given
precision.  You can't call a method on it.  You mean, e.g., 

   RealField(53).is_field(),

which isn't broken.
