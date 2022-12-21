# Issue 5909: symbolics -- x.subs_expr({}) hangs sage

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-27 06:14:48

This might have been fixed by the pynac switch, but we will see:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 
sage: x.subs_expr({x:1})
1
sage: x.subs_expr({})
Control-C pressed.  Interrupting Maxima. Please wait a few seconds...
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 3.4.2.alpha0, Release Date: 2009-04-24                |
| Type notebook() for the GUI, and license() for information.        |
/home/mabshoff/.sage/temp/sage.math.washington.edu/10619/_home_mabshoff__sage_init_sage_0.py in <module>()

/scratch/mabshoff/sage-3.4.2.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in subs_expr(self, *equations)
   4579         v = ','.join(['%s=%s'%(x.lhs()._maxima_init_(), x.rhs()._maxima_init_()) \
   4580                       for x in equations])
-> 4581         return R(self._maxima_().subst(v))
   4582 
   4583     ###################################################################

/scratch/mabshoff/sage-3.4.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/maxima.pyc in subst(self, val)
   2096             342
   2097         """
-> 2098         return self.comma(val)
   2099 
   2100     def comma(self, args):

/scratch/mabshoff/sage-3.4.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/maxima.pyc in comma(self, args)
   2111         self._check_valid()
   2112         P = self.parent()
-> 2113         return P('%s, %s'%(self.name(), args))
   2114 
   2115     def _latex_(self):

/scratch/mabshoff/sage-3.4.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1021             
   1022         if isinstance(x, basestring):
-> 1023             return cls(self, x, name=name)
   1024         try:
   1025             return self._coerce_from_special_method(x)

/scratch/mabshoff/sage-3.4.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1396             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1397                 self._session_number = -1
-> 1398                 raise TypeError, x
   1399         self._session_number = parent._session_number
   1400 

TypeError: 
sage: 
```



---

Comment by mabshoff created at 2009-05-20 23:50:09

Resolution: fixed


---

Comment by mabshoff created at 2009-05-20 23:50:09

Fixed via the new symbolics at #5930:

```
mabshoff`@`sage:/scratch/mabshoff/sage-4.0.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x.subs_expr({x:1})
1
sage: x.subs_expr({})
x
sage: 
```

| Sage Version 4.0.alpha0, Release Date: 2009-05-15                  |
| Type notebook() for the GUI, and license() for information.        |
If someone wants to take credit for this personally let me know.

Cheers,

Michael
