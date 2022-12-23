# Issue 3374: some symbolic values cannot be printed [new symbolics]

Issue created by migration from https://trac.sagemath.org/ticket/3374

Original creator: cwitty

Original creation time: 2008-06-05 20:20:37

Assignee: gfurnish


```
sage: var('x', CC)
x
sage: h = sin(x)/(cos(x))^2
sage: h
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/gfurnish/sage-3.0.2-symbolics/<ipython console> in <module>()

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)
    533 
    534             # and now call a possibly user-defined print mechanism
--> 535             manipulated_val = self.display(arg)
    536             
    537             # user display hooks can change the variable to be stored in

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)
    559             return IPython.generics.result_display(arg)
    560         except TryNext:            
--> 561             return self.shell.hooks.result_display(arg)
    562 
    563     # Assign the default display method:

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)
    132             #print "prio",prio,"cmd",cmd #dbg
    133             try:
--> 134                 ret = cmd(*args, **kw)
    135                 return ret
    136             except ipapi.TryNext, exc:

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)
    160     
    161     if self.rc.pprint:
--> 162         out = pformat(arg)
    163         if '\n' in out:
    164             # So that multi-line strings line up with the left column of

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113 

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208 
    209 

/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291 
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294 

/home/gfurnish/sage-3.0.2-symbolics/sage_object.pyx in sage.structure.sage_object.SageObject.__repr__ (devel/sage/sage/structure/sage_object.c:610)()

/home/gfurnish/sage-3.0.2-symbolics/expression.pyx in sage.symbolics.expression.TypedSymbolicExpression._repr_ (devel/sage/sage/symbolics/expression.c:3463)()

/home/gfurnish/sage-3.0.2-symbolics/expression.pyx in sage.symbolics.expression.TypedSymbolicExpression._repr_ (devel/sage/sage/symbolics/expression.c:3408)()

/home/gfurnish/sage-3.0.2-symbolics/mularithmetic.pyx in sage.symbolics.operators.mularithmetic.SymbolicMulArithmetic._eval (devel/sage/sage/symbolics/operators/mularithmetic.c:5486)()

/home/gfurnish/sage-3.0.2-symbolics/arithmetic.pyx in sage.symbolics.operators.arithmetic.SymbolicPowArithmetic._eval (devel/sage/sage/symbolics/operators/arithmetic.c:7626)()

/home/gfurnish/sage-3.0.2-symbolics/constant.pyx in sage.symbolics.constant.SymbolicConstant.__getattr__ (devel/sage/sage/symbolics/constant.c:5378)()

/home/gfurnish/sage-3.0.2-symbolics/expression.pyx in sage.symbolics.expression.TypedSymbolicExpression.__getattr__ (devel/sage/sage/symbolics/expression.c:8497)()

AttributeError: Attribute _mul_c not found for class <type 'sage.symbolics.constant.SymbolicConstant'>
```



---

Comment by gfurnish created at 2008-06-05 20:38:02

This specific bug associated with the missing cast to symbolicexpression in symbolicpow.eval is fixed in rev 9864 , but there are still some issues remaining with trig functions and division (because simplification for trig functions is not fully implemented yet).


---

Comment by gfurnish created at 2008-06-05 20:38:02

Resolution: fixed


---

Comment by was created at 2008-08-23 08:14:14

Milestone sage-symbolics deleted
