# Issue 7482: provide a mode so that undeclared variables magically spring into existence and object oriented notation is not necessary

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-17 22:20:48

Assignee: tbd

College teacher often say that by far the biggest obstruction to people switching from Maple to Sage is that:

 (1) symbolic variables don't magically spring into existence when used

 (2) one has to use object oriented notation---foo.bar(...)---to access methods of an object.


---

Comment by was created at 2009-11-17 22:34:20

I have created a "mock up" of the above functionality, for people to play with, which doesn't even require applying a patch.  Just paste the following into a Sage notebook cell and press shift-enter:

```
class MagicVar(Expression):
    def __call__(self, *args, **kwds):
        return args[0].__getattribute__(str(self))(*args[1:], **kwds)

class MagicNames:
    def eval(self, s, globals, locals=None):
        x = preparse(s).strip()
        y = x.split('\n')
        if len(y) == 0:
            return ''
        s = '\n'.join(y[:-1]) + '\n'
        t = y[-1]
        try:
            z = compile(t + '\n', '', 'single')
        except SyntaxError:
            s += '\n' + t
            z = None
        while True:
            try:    
                self._eval_code(s, z, globals)
            except NameError, msg:
                nm = msg.args[0].split("'")[1]
                globals[nm] = MagicVar(SR, var(nm))
            else:
                return ''
                
    def _eval_code(self, s, z, globals):
        eval(compile(s, '', 'exec'), globals, globals)
        if z is not None:
            eval(z, globals)
        
magic = MagicNames()                 
```


Now if you put %magic at the top of an input cell, then symbolic variables magically spring into life, and object oriented notation is not necessary.   There isn't an easy way to make this permanent for all cells in a worksheet (without putting %magic) without actually changing the sage library with a patch.  This is because of a major annoying mistake I found just now (see #7483).


---

Comment by was created at 2009-11-18 02:51:04

I'm attaching a patch that fully implements this in the notebook, via a command automatic_names(True).   This depends on trac #7483.    I could not figure out how to implement this on the command line without making potentially major changes to IPython, which is a bad idea at this point.  So this will be notebook only.  Since the target audience is newbie calculus freshman, restricting to the notebook probably isn't much of a constraint.


---

Comment by was created at 2009-11-18 03:14:52

Here is a session (to be used in the notebook) that illustrates automatic_names:

```
sage: automatic_names(True)
sage: x + y + z + wxy
wxy + x + y + z
sage: y(y=10)
10
sage: type(y)
<class 'sagenb.misc.support.AutomaticVariable'>
sage: trig_expand((2*x + 4*y + sin(2*theta))^2)
4*(sin(theta)*cos(theta) + x + 2*y)^2
sage: type(trig_expand)
<class 'sagenb.misc.support.AutomaticVariable'>
sage: type(x)
<type 'sage.symbolic.expression.Expression'>
sage: type(y)
<class 'sagenb.misc.support.AutomaticVariable'>
```


Notice above that trig_expand, y, and theta were all automatically created.  Notice that substitution `y(y=10)` still works.   If an object obj had a y method, then y(obj) would be evaluated as obj.y().

Here's a test showing that we avoid infinite loops:

```
sage: raise NameError
Traceback (most recent call last):
...
NameError
sage: raise NameError, "'var'"
Traceback (most recent call last):
...
NameError: Too many automatic variable names and functions created (limit=10000)
```



---

Attachment

apply to the sagenb spkg


---

Attachment

apply to the core sage library


---

Comment by was created at 2009-11-18 03:30:01

Changing status from new to needs_review.


---

Comment by was created at 2009-11-18 03:38:23

I've put a new sagenb spkg with just this patch (and the one from 7483) here:

   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.3.p1.spkg


---

Comment by mpatel created at 2009-11-18 06:36:40

The Selenium test results are unchanged in FF3.5.5 on Linux.  

`make ptest` on sage.math passes.


---

Comment by was created at 2009-11-18 09:35:00

I'm making implementing this for IPython as trac #7486.


---

Comment by mpatel created at 2009-11-18 13:26:53

This looks good to and works for me, but it'd be great to get additional data.

Please try the demo at [alpha.sagenb.org](http://alpha.sagenb.org)!


---

Comment by mpatel created at 2009-12-10 00:40:08

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-12-10 00:40:08

This is very clever!  In

```
so that ``foo(bar, ...)`` gets transformed to ``foo.bar(...)``.
```

should the latter be ```bar.foo(...)```?

Should we advertise `automatic_names` on `sage-edu`?


---

Comment by mpatel created at 2009-12-10 01:13:56

Fix typo.  Replaces *sagenb* patch.


---

Attachment

V3 changes

```
            sage: automatic_names(True)
```

to

```
            sage: automatic_names(True)      # not tested
```



---

Attachment

Suppress a doctest (cf. #7650).  Replaces *sagenb* patch.


---

Comment by mhansen created at 2009-12-11 02:56:09

Once this is merged in sagenb, I'll merge the code in sagelib.


---

Comment by mpatel created at 2010-01-01 10:48:40

Rebased vs. #7514's "part3.2".  Replaces *sagenb* patch.


---

Attachment

I've merged the sagelib patch in 4.3.1.alpha0.


---

Comment by was created at 2010-01-04 06:43:58

Resolution: fixed


---

Comment by was created at 2010-01-04 06:43:58

Merged into sagenb-0.4.8.
