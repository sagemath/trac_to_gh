# Issue 3374: some symbolic values cannot be printed [new symbolics]

archive/issues_003374.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n```\nsage: var('x', CC)\nx\nsage: h = sin(x)/(cos(x))^2\nsage: h\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/gfurnish/sage-3.0.2-symbolics/<ipython console> in <module>()\n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)\n    533 \n    534             # and now call a possibly user-defined print mechanism\n--> 535             manipulated_val = self.display(arg)\n    536             \n    537             # user display hooks can change the variable to be stored in\n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)\n    559             return IPython.generics.result_display(arg)\n    560         except TryNext:            \n--> 561             return self.shell.hooks.result_display(arg)\n    562 \n    563     # Assign the default display method:\n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)\n    132             #print \"prio\",prio,\"cmd\",cmd #dbg\n    133             try:\n--> 134                 ret = cmd(*args, **kw)\n    135                 return ret\n    136             except ipapi.TryNext, exc:\n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)\n    160     \n    161     if self.rc.pprint:\n--> 162         out = pformat(arg)\n    163         if '\\n' in out:\n    164             # So that multi-line strings line up with the left column of\n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in pformat(self, object)\n    109     def pformat(self, object):\n    110         sio = _StringIO()\n--> 111         self._format(object, sio, 0, 0, {}, 0)\n    112         return sio.getvalue()\n    113 \n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)\n    127             self._readable = False\n    128             return\n--> 129         rep = self._repr(object, context, level - 1)\n    130         typ = _type(object)\n    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)\n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in _repr(self, object, context, level)\n    193     def _repr(self, object, context, level):\n    194         repr, readable, recursive = self.format(object, context.copy(),\n--> 195                                                 self._depth, level)\n    196         if not readable:\n    197             self._readable = False\n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)\n    205         and whether the object represents a recursive construct.\n    206         \"\"\"\n--> 207         return _safe_repr(object, context, maxlevels, level)\n    208 \n    209 \n\n/home/gfurnish/sage-3.0.2-symbolics/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)\n    290         return format % _commajoin(components), readable, recursive\n    291 \n--> 292     rep = repr(object)\n    293     return rep, (rep and not rep.startswith('<')), False\n    294 \n\n/home/gfurnish/sage-3.0.2-symbolics/sage_object.pyx in sage.structure.sage_object.SageObject.__repr__ (devel/sage/sage/structure/sage_object.c:610)()\n\n/home/gfurnish/sage-3.0.2-symbolics/expression.pyx in sage.symbolics.expression.TypedSymbolicExpression._repr_ (devel/sage/sage/symbolics/expression.c:3463)()\n\n/home/gfurnish/sage-3.0.2-symbolics/expression.pyx in sage.symbolics.expression.TypedSymbolicExpression._repr_ (devel/sage/sage/symbolics/expression.c:3408)()\n\n/home/gfurnish/sage-3.0.2-symbolics/mularithmetic.pyx in sage.symbolics.operators.mularithmetic.SymbolicMulArithmetic._eval (devel/sage/sage/symbolics/operators/mularithmetic.c:5486)()\n\n/home/gfurnish/sage-3.0.2-symbolics/arithmetic.pyx in sage.symbolics.operators.arithmetic.SymbolicPowArithmetic._eval (devel/sage/sage/symbolics/operators/arithmetic.c:7626)()\n\n/home/gfurnish/sage-3.0.2-symbolics/constant.pyx in sage.symbolics.constant.SymbolicConstant.__getattr__ (devel/sage/sage/symbolics/constant.c:5378)()\n\n/home/gfurnish/sage-3.0.2-symbolics/expression.pyx in sage.symbolics.expression.TypedSymbolicExpression.__getattr__ (devel/sage/sage/symbolics/expression.c:8497)()\n\nAttributeError: Attribute _mul_c not found for class <type 'sage.symbolics.constant.SymbolicConstant'>\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3374\n\n",
    "closed_at": "2008-06-05T20:38:02Z",
    "created_at": "2008-06-05T20:20:37Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "title": "some symbolic values cannot be printed [new symbolics]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3374",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @garyfurnish

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

Issue created by migration from https://trac.sagemath.org/ticket/3374





---

archive/issue_events_007605.json:
```json
{
    "actor": "https://github.com/garyfurnish",
    "created_at": "2008-06-05T20:38:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3374",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3374#event-7605"
}
```



---

archive/issue_comments_023550.json:
```json
{
    "body": "This specific bug associated with the missing cast to symbolicexpression in symbolicpow.eval is fixed in rev 9864 , but there are still some issues remaining with trig functions and division (because simplification for trig functions is not fully implemented yet).",
    "created_at": "2008-06-05T20:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3374#issuecomment-23550",
    "user": "https://github.com/garyfurnish"
}
```

This specific bug associated with the missing cast to symbolicexpression in symbolicpow.eval is fixed in rev 9864 , but there are still some issues remaining with trig functions and division (because simplification for trig functions is not fully implemented yet).



---

archive/issue_comments_023551.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-05T20:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3374#issuecomment-23551",
    "user": "https://github.com/garyfurnish"
}
```

Resolution: fixed



---

archive/issue_comments_023552.json:
```json
{
    "body": "Milestone sage-symbolics deleted",
    "created_at": "2008-08-23T08:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3374#issuecomment-23552",
    "user": "https://github.com/williamstein"
}
```

Milestone sage-symbolics deleted
