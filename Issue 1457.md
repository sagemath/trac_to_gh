# Issue 1457: Somewhere in a short computation: "BUG:  Rational.__pow__ called on a non-Rational"

Issue created by migration from Trac.

Original creator: bober

Original creation time: 2007-12-11 01:26:33

Assignee: was

The following took place on an Intel Core Duo (32 bit) running Ubuntu 7.10. Hopefully the cause is obvious for someone familiar with the calculus/plotting code.

(Note: replacing `f(x)` with `f(x) = 2.0 * sqrt(x^2.0 + 300.0^2.0) - x + 1000.0` is a suitable workaround.)


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.15, Release Date: 2007-12-03                      |
| Type notebook() for the GUI, and license() for information.        |
sage: f(x) = 2 * sqrt(x^2 + 300^2) - x + 1000
sage: P = f.diff(x).diff(x).plot(xmin=0,xmax=1000)
---------------------------------------------------------------------------
<type 'exceptions.AssertionError'>        Traceback (most recent call last)

/home/bober/sage-2.8.15.alpha1/<ipython console> in <module>()

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)
    602         else:
    603             f = self.function(param)
--> 604         return plot(f, *args, **kwds)
    605 
    606     def __lt__(self, right):

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   2303             G = funcs.plot(*args, **kwds)
   2304         else:
-> 2305             G = self._call(funcs, *args, **kwds)
   2306         if do_show:
   2307             G.show()

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xmin, xmax, parametric, polar, label, show, **kwds)
   2353 
   2354             try:
-> 2355                 y = f(x)
   2356                 data.append((x, float(y)))
   2357             except (ZeroDivisionError, TypeError, ValueError), msg:

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in <lambda>(x)
    591                 else:
    592                     param = A[0]
--> 593                 f = lambda x: self(x)
    594             else:
    595                 A = self.variables()

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, *args)
   4012         vars = self.args()
   4013         dct = dict( (vars[i], args[i]) for i in range(len(args)) )
-> 4014         return self._expr.substitute(dct)
   4015 
   4016     def _repr_(self, simplify=True):

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in substitute(self, in_dict, **kwds)
   2589         kwds = self.__parse_in_dict(in_dict, kwds)
   2590         kwds = self.__varify_kwds(kwds)
-> 2591         return X._recursive_sub(kwds)
   2592 
   2593     def subs(self, *args, **kwds):

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)
   3424         """
   3425         ops = self._operands
-> 3426         new_ops = [SR(op._recursive_sub(kwds)) for op in ops]
   3427 
   3428         #Check to see if all of the new_ops are symbolic constants

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)
   3424         """
   3425         ops = self._operands
-> 3426         new_ops = [SR(op._recursive_sub(kwds)) for op in ops]
   3427 
   3428         #Check to see if all of the new_ops are symbolic constants

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)
   3430         is_constant = all(map(lambda x: isinstance(x, SymbolicConstant), new_ops))
   3431         if is_constant:
-> 3432             return SymbolicConstant( self._operator(*map(lambda x: x._obj, new_ops)) )
   3433         else:
   3434             return self._operator(*new_ops)

/home/bober/sage-2.8.15.alpha1/rational.pyx in sage.rings.rational.Rational.__pow__()

<type 'exceptions.AssertionError'>: BUG:  Rational.__pow__ called on a non-Rational
sage: 
```



---

Comment by robertwb created at 2007-12-11 02:53:06

This was introduced in the massive 0^0 change--I know where to fix this.


---

Comment by was created at 2007-12-11 05:58:10

I've fixed the bug correctly. Now this draws a nice picture:

```
sage: f(x) = 2 * sqrt(x^2 + 300^2) - x + 1000
sage: P = f.diff(x).diff(x).plot(xmin=0,xmax=1000)
sage: P.show(ymax=0.01, ymin=0)
```



---

Attachment


---

Attachment


---

Comment by was created at 2007-12-11 06:29:26

Be sure to apply *both* patches, one after the other.


---

Comment by was created at 2007-12-15 23:52:19

this replaces the previous part 2


---

Attachment

It (still) works for me, when merged against rc0.


---

Comment by mabshoff created at 2007-12-16 00:38:58

Merged in 2.9.rc2.


---

Comment by mabshoff created at 2007-12-16 00:38:58

Resolution: fixed
