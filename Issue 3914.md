# Issue 3914: error in parsing maxima output

Issue created by migration from https://trac.sagemath.org/ticket/3914

Original creator: jason

Original creation time: 2008-08-20 18:19:22

Assignee: was


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.1, Release Date: 2008-08-17                       |
| Type notebook() for the GUI, and license() for information.        |
sage: var('s,t')
(s, t)
sage: f=function('f', t)
sage: f.diff(t,2)
diff(f(t), t, 2)
sage: f.diff(t,2).laplace(t,s)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in laplace(self, t, s)
   2290             sage: (p1+p2).save()
   2291         """
-> 2292         return self.parent()(self._maxima_().laplace(var(t), var(s)))
   2293
   2294     def inverse_laplace(self, t, s):

/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, x)
    449                 msg, s, pos = err.args
    450                 raise TypeError, "%s: %s !!! %s" % (msg, s[:pos], s[pos:])
--> 451         return self._coerce_impl(x)
    452
    453     def _coerce_impl(self, x):

/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _coerce_impl(self, x)
    467             return x
    468         elif isinstance(x, MaximaElement):
--> 469             return symbolic_expression_from_maxima_element(x)
    470         # if "x" is a SymPy object, convert it to a SAGE object
    471         elif is_Polynomial(x) or is_MPolynomial(x):

/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in symbolic_expression_from_maxima_element(x)
   8314         x^(sqrt(y) + pi) - sin(e)
   8315     """
-> 8316     return symbolic_expression_from_maxima_string(x.name())
   8317
   8318 def evaled_symbolic_expression_from_maxima_string(x):

/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in symbolic_expression_from_maxima_string(x, equals_sub, maxima)
   8298         # evaluation of maxima code are assumed pre-simplified
   8299         is_simplified = True
-> 8300         return symbolic_expression_from_string(s, syms, accept_sequence=True)
   8301     except SyntaxError:
   8302         raise TypeError, "unable to make sense of Maxima expression '%s' in SAGE"%s

/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in symbolic_expression_from_string(s, syms, accept_sequence)
   8431             global _augmented_syms
   8432             _augmented_syms = syms
-> 8433             return parse_func(s)
   8434         finally:
   8435             _augmented_syms = {}

/home/grout/parser.pyx in sage.misc.parser.Parser.parse_sequence (sage/misc/parser.c:3012)()

/home/grout/parser.pyx in sage.misc.parser.Parser.parse_sequence (sage/misc/parser.c:2911)()

/home/grout/parser.pyx in sage.misc.parser.Parser.p_sequence (sage/misc/parser.c:3304)()

/home/grout/parser.pyx in sage.misc.parser.Parser.p_eqn (sage/misc/parser.c:3929)()

/home/grout/parser.pyx in sage.misc.parser.Parser.p_expr (sage/misc/parser.c:4214)()

/home/grout/parser.pyx in sage.misc.parser.Parser.p_term (sage/misc/parser.c:4423)()

/home/grout/parser.pyx in sage.misc.parser.Parser.p_factor (sage/misc/parser.c:4737)()

/home/grout/parser.pyx in sage.misc.parser.Parser.p_factor (sage/misc/parser.c:4763)()

/home/grout/parser.pyx in sage.misc.parser.Parser.p_power (sage/misc/parser.c:4858)()

/home/grout/parser.pyx in sage.misc.parser.Parser.p_atom (sage/misc/parser.c:5234)()

TypeError: __call__() got an unexpected keyword argument 't'
```



---

Comment by kcrisman created at 2009-09-28 18:20:42

The errors are now slightly different post-Pynac switch, but here is the real issue.

```
sage: var('t,s')
(t, s)
sage: f = function('f',t)
sage: g = f.diff(t,2)
sage: h = f.diff(t,1)
sage: f.laplace(t,s)
laplace(f(t), t, s)
sage: h.laplace(t,s)
s*laplace(f(t), t, s) - f(0)
sage: SR(f)._maxima_().laplace(var('t'), var('s'))
'laplace('f(t),t,s)
sage: SR(h)._maxima_().laplace(var('t'), var('s'))
s*'laplace('f(t),t,s)-'f(0)
sage: SR(g)._maxima_().laplace(var('t'), var('s'))
-?%at('diff('f(t),t,1),t=0)+s^2*'laplace('f(t),t,s)-'f(0)*s
```

Sage has no chance to parse that!  And here is what it means:

```
Maxima 5.19.1 http://maxima.sourceforge.net
Using Lisp SBCL 1.0.30
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) diff(f(t),t,2);
                                   2
                                  d
(%o1)                             --- (f(t))
                                    2
                                  dt
(%i2) laplace(%,t,s);
                         !
                d        !         2
(%o2)         - -- (f(t))!      + s  laplace(f(t), t, s) - f(0) s
                dt       !
                         !t = 0
```

So Maxima is trying to evaluate the derivative of f at t=0, which Sage doesn't know how to evaluate.  Do we have syntax for that?  I think that 

```
sage: h.subs(t=0)
D[0](f)(0)
```

might not be what we are looking for.   Anyway, we definitely would have to improve our handling of the output from Maxima in order to get this right.


---

Comment by kcrisman created at 2009-10-05 13:55:21

Just to clarify, fixing #385 would solve this.


---

Comment by kcrisman created at 2009-10-20 06:48:26

Also to clarify, there is in fact a doctest already in #385 for this, so a reviewer can close two for the price of one...


---

Comment by kcrisman created at 2009-10-20 06:48:26

Changing status from new to needs_review.


---

Comment by robert.marik created at 2009-10-25 20:53:43

Resolution: duplicate


---

Comment by robert.marik created at 2009-10-25 20:53:43

Has been fixed by trac #385


---

Comment by mvngu created at 2009-10-28 12:28:21

Replying to [comment:4 robert.marik]:
> Has been fixed by trac #385
Robert, please don't close tickets. That's the job of the release manager. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for conventions on closing tickets.
