# Issue 3116: 1x1 symbolic matrices don't work right

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-05-07 01:12:37

Assignee: was

As reported by seeitcoming on IRC:

```
sage: a = matrix(3,[1/sqrt(3),1/3,1/3])
sage: A = a.transpose()
sage: A*a
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/cwitty/sage/<ipython console> in <module>()

/home/cwitty/sage/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)
    521 
    522             # and now call a possibly user-defined print mechanism
--> 523             manipulated_val = self.display(arg)
    524             
    525             # user display hooks can change the variable to be stored in

/home/cwitty/sage/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)
    545         """
    546 
--> 547         return self.shell.hooks.result_display(arg)
    548 
    549     # Assign the default display method:

/home/cwitty/sage/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)
    132             #print "prio",prio,"cmd",cmd #dbg
    133             try:
--> 134                 ret = cmd(*args, **kw)
    135                 return ret
    136             except ipapi.TryNext, exc:

/home/cwitty/sage/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)
    160     
    161     if self.rc.pprint:
--> 162         out = pformat(arg)
    163         if '\n' in out:
    164             # So that multi-line strings line up with the left column of

/home/cwitty/sage/local/lib/python2.5/pprint.py in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113 

/home/cwitty/sage/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/home/cwitty/sage/local/lib/python2.5/pprint.py in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/home/cwitty/sage/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208 
    209 

/home/cwitty/sage/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291 
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294 

/home/cwitty/sage/matrix0.pyx in sage.matrix.matrix0.Matrix.__repr__ (sage/matrix/matrix0.c:4508)()

/home/cwitty/sage/matrix0.pyx in sage.matrix.matrix0.Matrix.str (sage/matrix/matrix0.c:4810)()

/home/cwitty/sage/matrix0.pyx in sage.matrix.matrix0.Matrix.list (sage/matrix/matrix0.c:1577)()

/home/cwitty/sage/matrix_symbolic_dense.pyx in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense._list()

/home/cwitty/sage/matrix_symbolic_dense.pyx in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense.get_unsafe()

/home/cwitty/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in symbolic_expression_from_maxima_string(x, equals_sub, maxima)
   8267         return symbolic_expression_from_string(s, syms, accept_sequence=True)
   8268     except SyntaxError:
-> 8269         raise TypeError, "unable to make sense of Maxima expression '%s' in SAGE"%s
   8270     finally:
   8271         is_simplified = False

<type 'exceptions.TypeError'>: unable to make sense of Maxima expression '(5/9)[1,1]' in SAGE
```




---

Comment by mhansen created at 2008-05-07 01:47:57

Changing status from new to assigned.


---

Comment by mhansen created at 2008-05-07 01:47:57

Changing assignee from was to mhansen.


---

Attachment


---

Comment by cwitty created at 2008-05-10 20:31:40

Code looks good, doctests pass in sage/matrix.  Positive review.


---

Comment by mabshoff created at 2008-05-11 08:46:26

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 08:46:26

Resolution: fixed
