# Issue 921: Exception error for divergent integral looks bad

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-10-18 17:20:39

Assignee: was

When asking for a divergent integral, a big exception backtrace is printed.  This seems like it would be intimidating for students when a simple statement like at the end, "Integral is divergent" suffices.


```
sage:   integrate(1/x^3,x,0,1)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)
    173     """
    174     try:
--> 175         return f.integral(*args, **kwds)
    176     except AttributeError:
    177         pass

/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in integral(self, v, a, b)
   1663             return self.parent()(self._maxima_().integrate(v))
   1664         else:
-> 1665             return self.parent()(self._maxima_().integrate(v, a, b))
   1666
   1667     integrate = integral

/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in integral(self, var, min, max)
   1389             if max is None:
   1390                 raise ValueError, "neither or both of min/max must be specified."
-> 1391             return I(var, min, max)
   1392
   1393     integrate = integral

/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, *args)
    885
    886     def __call__(self, *args):
--> 887         return self._obj.parent().function_call(self._name, [self._obj] + list(args))
    888
    889     def help(self):

/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in function_call(self, function, args)
    832             if not isinstance(args[i], ExpectElement):
    833                 args[i] = self.new(args[i])
--> 834         return self.new("%s(%s)"%(function, ",".join([s.name() for s in args])))
    835
    836     def call(self, function_name, *args):

/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in new(self, code)
    734
    735     def new(self, code):
--> 736         return self(code)
    737
    738     ###################################################################

/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/maxima.py in __call__(self, x)
    374     def __call__(self, x):
    375         import sage.rings.all
--> 376         return Expect.__call__(self, x)
    377
    378     def __init__(self, script_subdirectory=None, logfile=None, server=None):

/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    679             return x
    680         if isinstance(x, basestring):
--> 681             return cls(self, x)
    682         try:
    683             return self._coerce_from_special_method(x)

/home/grout/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __init__(self, parent, value, is_name)
    920             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
    921                 self._session_number = -1
--> 922                 raise TypeError, x
    923         self._session_number = parent._session_number
    924

<type 'exceptions.TypeError'>: Error executing code in Maxima
CODE:
        sage22 : integrate(sage19,sage1,sage20,sage21)$
Maxima ERROR:

Integral is divergent
```



---

Comment by mhansen created at 2007-10-24 00:36:59

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-10-24 00:36:59

I'm attaching a patch which catches the divergence error and moves it farther up the chain so that the user isn't presented with such a huge error.

Here is the behavior after the patch:


```
sage: integrate(1/x^3,x,0,1)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/opt/sage/devel/sage-calc/sage/calculus/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/calculus/functional.py in integral(f, *args, **kwds)
    175         return f.integral(*args, **kwds)
    176     except ValueError, err:
--> 177         raise err
    178     except AttributeError:
    179         pass

<type 'exceptions.ValueError'>: Integral is divergent.
```



---

Attachment


---

Comment by was created at 2007-10-24 02:20:24

Looks good to me.


---

Comment by malb created at 2007-10-24 19:24:33

applied to 2.8.9.alpha1


---

Comment by malb created at 2007-10-24 19:25:17

Resolution: fixed
