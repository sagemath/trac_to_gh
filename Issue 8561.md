# Issue 8561: Implement PicklableFunction(interactive_function)

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-03-19 15:52:59

Assignee: was

CC:  sage-combinat

Keywords: Pickling, lambda, interactively defined functions

Extend sage.misc.fpickle.pyx with a PicklableFunction class wrapping
interactively defined (simple) functions to make them picklable:


```
    sage: f = lambda x: x^2
    sage: loads(dumps(f))
    ------------------------------------------------------------
    Traceback (most recent call last):
      File "<ipython console>", line 1, in <module>
      File "sage_object.pyx", line 792, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8357)
    PicklingError: Can't pickle <type 'function'>: attribute lookup __builtin__.function failed

    sage: f = PicklableFunction(f)
    sage: f(3)
    9
    sage: f == loads(dumps(f))
    True
```




---

Comment by nthiery created at 2010-03-19 15:53:16

Changing assignee from was to nthiery.


---

Comment by nbruin created at 2013-01-09 23:45:48

See #11845 for some code in this direction and for warnings why this should never be allowed in "standard" pickles.
