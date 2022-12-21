# Issue 5556: symbolic gamma function and symbolic log function are incoherent

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-03-18 05:54:30

CC:  burcin robertwb

Keywords: symbolic gamma log function numerical approximation

So this is incredibly awful:


```
sage: gamma(RealField(100)(3/4))
1.2254167024651776451290983034
sage: gamma(3/4).n(100)
1.2254167024651776429777783051
```


(for the record, the first one is correct)

and this doesn't agree with that:


```
sage: log(2).n(100)
0.69314718055994530941723212146
sage: log(RealField(2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/Devel/RiemannTheta/riemann_theta.py in <module>()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in log(x, base)
   9242             return x.log()
   9243         except AttributeError: 
-> 9244             return ln(x)
   9245     else:
   9246         try:

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in ln(x)
   9189         0.693147180559945
   9190     """
-> 9191     return function_log(x)
   9192 
   9193 def log(x, base=None):

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __call__(self, x, *args)
   7542             return getattr(x, self._repr_())(*args)
   7543         except AttributeError:
-> 7544             return SymbolicComposition(self, SR(x))
   7545 
   7546     def _approx_(self, x):  # must *always* be called with a float x as input.

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __call__(self, x)
    504                 msg, s, pos = err.args
    505                 raise TypeError, "%s: %s !!! %s" % (msg, s[:pos], s[pos:])
--> 506         return self._coerce_impl(x)
    507 
    508     def _coerce_impl(self, x):

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _coerce_impl(self, x)
    566             return self(x._sage_())
    567         else:
--> 568             raise TypeError, "cannot coerce type '%s' into a SymbolicExpression."%type(x)
    569 
    570     def _repr_(self):

TypeError: cannot coerce type '<type 'sage.rings.real_mpfr.RealField'>' into a SymbolicExpression.
sage: log(RealField(2))
```



---

Comment by ncalexan created at 2009-03-18 05:55:40

I just realized I goofed, I meant:


```
sage: log(2).n(100)
0.69314718055994530941723212146
sage: log(RealField(100)(2))
0.69314718055994530941723212146
```


which works as expected.  But the symbolic gamma function is still wrong, and egregiously wrong at that!


---

Comment by kcrisman created at 2009-09-29 16:17:10

The problem is that gamma(3/4) is automatically evaluated to precision 53, and then doing n(100) has only meaningless effect.  I don't know what happened between the original filing of this ticket and the Pynac update, but now Pynac automatically evaluates these.  See [http://groups.google.com/group/sage-devel/browse_thread/thread/f43fa9c900d06efd](http://groups.google.com/group/sage-devel/browse_thread/thread/f43fa9c900d06efd)


---

Comment by kcrisman created at 2009-09-30 14:02:04

Actually, belay that.  There are a few such functions out there.  E.g., 

```
sage: sin(SR(3/4))
sin(3/4)
sage: sin(3/4)
sin(3/4)
sage: gamma(SR(3/4))
gamma(3/4)
sage: gamma(3/4)
1.22541670246518
sage: zeta(SR(3/4))
zeta(3/4)
sage: zeta(3/4)
-3.44128538694522
```

So the problem lies in gamma itself (and friends).  Most likely fix at this point is adding a prec keyword, as in sqrt.


---

Comment by kcrisman created at 2009-09-30 17:00:35

This should fix all such things, with the change that rationals now default to symbolic output.  The sage-devel discussion above didn't seem to think this was a problem, so hopefully it won't be, as one can still use prec or .n() to get exact values when the input isn't a multiple of 1/2.

Note that this patch also fixes a NASTY hang error with negative integer CDF input into gamma.


---

Attachment

Based on 4.1.2.alpha4


---

Attachment


---

Comment by mhansen created at 2009-10-05 06:01:16

Looks good to me.  

I added a small little patch which cleans up the docstrings a little bit.  kcrisman, can you just go over them?


---

Comment by kcrisman created at 2009-10-05 13:20:19

Yup, those are all good changes.  I never know exactly how many characters are okay for the width of docstrings; it varies wildly by file, so I go short to be safe.  Also good eye with the n-1.


---

Comment by mhansen created at 2009-10-15 05:17:40

Resolution: fixed
