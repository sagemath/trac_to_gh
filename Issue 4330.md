# Issue 4330: interfaces function_call(...) function is a total MESS

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-20 15:39:25

Assignee: was

I just noticed that the functional_call function in the interfaces directory (defined in various files) is a bug-ridden mess.

For example

```
sage: a = mathematica('N[BesselK[1+I, 2+ 3*I], 20]')
sage: a.Re()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/was/build/sage-3.1.3.alpha3/<ipython console> in <module>()

/home/was/build/sage-3.1.3.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, *args, **kwds)
   1241
   1242     def __call__(self, *args, **kwds):
-> 1243         return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
   1244
   1245     def help(self):

TypeError: function_call() takes at most 3 arguments (4 given)
sage:
```


Also, I noticed that in expect.py the definition of function_call is:

```
def function_call(self, function, args=[], kwds={}):
```

This is the typical stupid Python newbiew mistake (of course I'm the newbie that is to blame here...), which leads to massive subtle bugs.  Things are done right in function_call in r.py, and that pattern should be used everywhere else.




---

Comment by mhansen created at 2008-10-23 16:48:27

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-10-23 16:48:27

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-21 21:27:15

I also included a fix which makes the GAP interface way more usable.  It makes the interface work when GAP functions don't return values so that you can do


```
sage: rws.MakeConfluent()
```


instead of 


```
sage: gap.eval("MakeConfluent(%s)"%rws.name()) 
```



---

Attachment

Positive review, though it would be nice to remove "import random" from gap.py
and it would be good to add my example

```
sage: a = mathematica('N[BesselK[1+I, 2+ 3*I], 20]')
sage: a.Re()
```

as an optional doctest.

William


---

Comment by mabshoff created at 2008-11-23 01:58:38

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-23 01:58:38

Resolution: fixed
