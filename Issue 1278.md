# Issue 1278: make R an optional Sage package that builds on everything (in prep for making it non-optional)

Issue created by migration from https://trac.sagemath.org/ticket/1278

Original creator: was

Original creation time: 2007-11-26 06:47:31

Assignee: was

See emails on sage-devel for details.   I'll post specific notes about what has to be done below.


---

Comment by was created at 2007-11-26 06:47:44


```
But, it doesn't look like my patch to rpy was applied:

sage: rpy.r(2r)
2.0
sage: rpy.r(2)
---------------------------------------------------------------------------
<class 'rpy.RException'>                  Traceback (most recent call last)

/home/mike/src/rpy-1.0-RC3/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/rpy.py in __call__(self, s)
   297
   298     def __call__(self, s):
--> 299         return self.eval(self.parse(text=s))
   300
   301     def __help__(self, *arg, **kw):

<class 'rpy.RException'>: cannot convert from type 'sage.rings.integer.Integer'

There should be an rpymodule.c in the patches/ directory in
rpy-1.0-RC3 in my home directory on sage.math which makes it so that
rpy will check for a _rpy_ method to convert a Sage object to an rpy
one.
```



---

Comment by mabshoff created at 2007-12-14 04:11:57

Resolution: fixed


---

Comment by mabshoff created at 2007-12-14 04:11:57

This happened a while ago.
