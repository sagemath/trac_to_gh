# Issue 9947: Conversion of p-adic to gp is buggy because of "+Infinity" exponent

Issue created by migration from https://trac.sagemath.org/ticket/9948

Original creator: jdemeyer

Original creation time: 2010-09-19 11:02:53

Assignee: was

CC:  mstreng


```
sage: gp(pAdicField(5)(0))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jdemeyer/<ipython console> in <module>()

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1032             return cls(self, x, name=name)
   1033         try:
-> 1034             return self._coerce_from_special_method(x)
   1035         except TypeError:
   1036             raise

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)
   1056             s = '_gp_'
   1057         try:
-> 1058             return (x.__getattribute__(s))(self)
   1059         except AttributeError:
   1060             return self(x._interface_init_())

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._gp_ (sage/structure/sage_object.c:4092)()

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3501)()

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1030
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/usr/local/src/sage-4.6.prealpha4/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453

TypeError: Error executing code in GP/PARI:
CODE:
        sage[2]=0 + O(5^+Infinity);
GP/PARI ERROR:
  ***   at top-level: sage[2]=0+O(5^+Infinity)
  ***                                ^---------
  ***   gtos expected an integer, got 'Infinity'.
```



---

Attachment


---

Comment by mstreng created at 2012-01-06 12:38:53

Changing keywords from "" to "sd35".


---

Comment by pbruin created at 2014-04-10 23:30:42

This seems to have been fixed in the meantime.  In Sage 6.2.beta6:

```
sage: gp(pAdicField(5)(0))
0
sage: pari(pAdicField(5)(0))
0
```

I propose to close this as invalid/worksforme/whatever...


---

Comment by pbruin created at 2014-04-10 23:30:42

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-04-11 08:09:56

Yes, seems fixed.


---

Comment by jdemeyer created at 2014-04-11 08:09:56

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-04-12 07:34:25

Resolution: fixed
