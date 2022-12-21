# Issue 669: Solaris 10: functions/constants.py doctests failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 00:29:53

Assignee: was

Keywords: Solaris 10, doctest


```
sage -t  functions/constants.py                             **********************************************************************
File "constants.py", line 498:
    sage: 1e8*I
Exception raised:
    Traceback (most recent call last):
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[10]>", line 1, in <module>
        RealNumber('1e8')*I###line 498:
    sage: 1e8*I
      File "sage_object.pyx", line 87, in sage_object.SageObject.__repr__
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2883, in _repr_
        return self.simplify()._repr_(simplify=False)
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2038, in simplify
        S = evaled_symbolic_expression_from_maxima_string(self._maxima_init_())
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4966, in evaled_symbolic_expression_from_maxima_string
        return symbolic_expression_from_maxima_string(maxima.eval(x))
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4940, in symbolic_expression_from_maxima_string
        w = sage_eval(s, syms)
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/misc/sage_eval.py", line 110, in sage_eval
        return eval(p, sage.all.__dict__, locals)
      File "<string>", line 1, in <module>
      File "real_mpfr.pyx", line 2711, in real_mpfr.create_RealNumber
      File "real_mpfr.pyx", line 610, in real_mpfr.RealNumber.__init__
      File "real_mpfr.pyx", line 659, in real_mpfr.RealNumber._set
    TypeError: Unable to convert x (='1.e') to real number.
**********************************************************************
```



---

Comment by mabshoff created at 2007-09-17 01:23:43

Changing component from packages to doctest.


---

Comment by mabshoff created at 2007-09-17 01:23:43

Changing assignee from was to failure.


---

Comment by mabshoff created at 2008-11-21 18:59:01

This has been fixed a while ago.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-21 18:59:01

Resolution: fixed
