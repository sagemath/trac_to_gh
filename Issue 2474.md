# Issue 2474: RealIntervalField should have a round method (maybe ComplexIntervalField should too)

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-11 22:09:18

Assignee: somebody

CC:  ncalexan

Keywords: RIF CIF RealIntervalField ComplexIntervalField round


```
sage: round(RIF(10))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/sage-2.10.3.rc3/<ipython console> in <module>()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/misc/functional.py in round(x, ndigits)
    864     else:
    865         try: return x.round()
--> 866         except AttributeError: return RealDoubleElement(__builtin__.round(x, 0))
    867 
    868 def quotient(x, y, *args, **kwds):

<type 'exceptions.TypeError'>: a float is required
```



---

Comment by cwitty created at 2008-03-12 01:28:55

But what should it return?  In particular, what should round(RIF(1.5, 12345.678)) return, and why?

My vote is that RIF should not have a round method, since I can't think of a definition that's sensible and useful.


---

Comment by chapoton created at 2017-09-13 19:38:04

This now exists, with some definition.


---

Comment by chapoton created at 2017-09-13 19:38:04

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2017-09-15 08:18:34

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2017-09-15 08:18:34

Indeed!


---

Comment by embray created at 2017-12-12 08:23:33

Resolution: wontfix


---

Comment by zimmerma created at 2017-12-12 09:21:13

I wonder why "wontfix" since this now seems to work:

```
sage: sage.rings.real_mpfi.printing_style = 'brackets'
sage: round(RIF(1.5, 12345.678)) 
[2.0000000000000000 .. 12346.000000000000]
```



---

Comment by embray created at 2017-12-12 13:19:45

It was a batch edit; it doesn't make a lot of difference either way but I suppose "worksforme" would be more appropriate (but "wontfix" could also be read as "won't fix because it's already fixed" :)


---

Comment by embray created at 2017-12-12 13:19:45

Resolution changed from wontfix to worksforme
