# Issue 5798: _singular_() for matrices doesn't always work

Issue created by migration from https://trac.sagemath.org/ticket/5798

Original creator: ddrake

Original creation time: 2009-04-16 04:18:36

Assignee: was

With 3.4.1.rc2:


```
sage: m = matrix(RR, 4, [pi, sqrt(2), exp(1), -1])
sage: m._singular_()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/drake/.sage/temp/klee/7627/_home_drake__sage_init_sage_0.py in <module>()

/var/tmp/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/matrix/matrix1.so in sage.matrix.matrix1.Matrix._singular_ (sage/matrix/matrix1.c:3280)()

/var/tmp/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._singular_ (sage/structure/sage_object.c:5346)()

/var/tmp/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3018)()

/var/tmp/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in __call__(self, x, type)
    652             x = str(x)[1:-1]
    653 
--> 654         return SingularElement(self, type, x, False)
    655 
    656 

/var/tmp/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in __init__(self, parent, type, value, is_name)
   1101             except (RuntimeError, TypeError, KeyboardInterrupt), x:
   1102                 self._session_number = -1
-> 1103                 raise TypeError, x
   1104         else:
   1105             self._name = value

TypeError: Singular error:
   ? `Real` is undefined
   ? error occurred in STDIN line 3: `def sage0=Real Field with 53 bits of precision;`
```


The same thing also fails with a rational matrix.

Also, the docstring for `_singular_` is really bad -- it sounds like it's talking about a singular (noninvertible) matrix.
