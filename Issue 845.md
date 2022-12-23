# Issue 845: Can't pass boolean as parameter to Magma

Issue created by migration from https://trac.sagemath.org/ticket/845

Original creator: jvoight

Original creation time: 2007-10-10 06:56:01

Assignee: was

sage: magma('false')
false
sage: f = magma('Polynomial([-2,0,1])')
sage: f.NumberField(Check = false)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/jvoight/totallyreal/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, *args, **kwds)
    552                                [self._obj.name()] + list(args),
    553                                params = kwds,
--> 554                                nvals = nvals)
    555
    556     def _sage_doc_(self):

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in function_call(self, function, args, params, nvals)
    405             ans = None
    406         elif nvals == 1:
--> 407             return self(fun)
    408         else:
    409             v = [self._next_var_name() for _ in range(nvals)]

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/magma.py in __call__(self, x, gens)
    315         """
    316         if gens is None:
--> 317             return Expect.__call__(self, x)
    318         return self.objgens(x, gens)
    319

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    679             return x
    680         if isinstance(x, basestring):
--> 681             return cls(self, x)
    682         try:
    683             return self._coerce_from_special_method(x)

/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    920             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    921                 self._session_number = -1
--> 922                 raise TypeError, x
    923         self._session_number = parent._session_number
    924

<type 'exceptions.TypeError'>: Error evaluation Magma code.
IN:_sage_[5] := NumberField(_sage_[4] : Check:=False);
OUT:
>> _sage_[5] := NumberField(_sage_[4] : Check:=False);
                                               ^
User error: Identifier 'False' has not been declared or assigned



---

Attachment


---

Comment by malb created at 2007-10-30 16:38:52

Changing status from new to assigned.


---

Comment by malb created at 2007-10-30 16:38:52

fixed in attached patch. A Magma guru should look at this patch, though.


---

Comment by malb created at 2007-10-30 16:38:52

Changing assignee from was to malb.


---

Comment by mabshoff created at 2007-11-01 23:22:54

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 23:22:54

applied to 2.8.11.rc1
