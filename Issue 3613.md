# Issue 3613: symbolic equations are not passed to Maple correctly

Issue created by migration from https://trac.sagemath.org/ticket/3613

Original creator: mhansen

Original creation time: 2008-07-08 17:58:37

Assignee: was


```
sage: maple(x==2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x, name)
    945             return cls(self, x, name=name)
    946         try:
--> 947             return self._coerce_from_special_method(x)
    948         except TypeError:
    949             raise

/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _coerce_from_special_method(self, x)
    969             s = '_gp_'
    970         try:
--> 971             return (x.__getattribute__(s))(self)
    972         except AttributeError:
    973             return self(x._interface_init_())

/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/sage_object.pyx in sage.structure.sage_object.SageObject._maple_ (sage/structure/sage_object.c:3342)()

/opt/sage-3.0.3.rc0/devel/sage-coerce/sage/sage_object.pyx in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2009)()

/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x, name)
    943             return x
    944         if isinstance(x, basestring):
--> 945             return cls(self, x, name=name)
    946         try:
    947             return self._coerce_from_special_method(x)

/opt/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name, name)
   1208             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1209                 self._session_number = -1
-> 1210                 raise TypeError, x
   1211         self._session_number = parent._session_number
   1212 

TypeError: An error occured running a Maple command:
INPUT:
read "/home/mike/.sage//temp/mike_laptop/21257//interface//tmp";
OUTPUT:
on line 1, syntax error, `=` unexpected:
sage1:=x == 2:;
          ^
Error, while reading `/home/mike/.sage//temp/mike_laptop/21257//interface//tmp`
```



---

Comment by mhansen created at 2008-07-09 00:46:21

Changing status from new to assigned.


---

Comment by mhansen created at 2008-07-09 00:46:21

Changing assignee from was to mhansen.


---

Attachment

Fine by me, apply!


---

Comment by mabshoff created at 2008-08-11 05:15:22

Resolution: fixed


---

Comment by mabshoff created at 2008-08-11 05:15:22

Merged in Sage 3.1.alpha1
