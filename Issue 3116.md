# Issue 3116: [with patch, positive review] 1x1 symbolic matrices don't work right

archive/issues_003116.json:
```json
{
    "body": "Assignee: @mwhansen\n\nAs reported by seeitcoming on IRC:\n\n```\nsage: a = matrix(3,[1/sqrt(3),1/3,1/3])\nsage: A = a.transpose()\nsage: A*a\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/cwitty/sage/<ipython console> in <module>()\n\n/home/cwitty/sage/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)\n    521 \n    522             # and now call a possibly user-defined print mechanism\n--> 523             manipulated_val = self.display(arg)\n    524             \n    525             # user display hooks can change the variable to be stored in\n\n/home/cwitty/sage/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)\n    545         \"\"\"\n    546 \n--> 547         return self.shell.hooks.result_display(arg)\n    548 \n    549     # Assign the default display method:\n\n/home/cwitty/sage/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)\n    132             #print \"prio\",prio,\"cmd\",cmd #dbg\n    133             try:\n--> 134                 ret = cmd(*args, **kw)\n    135                 return ret\n    136             except ipapi.TryNext, exc:\n\n/home/cwitty/sage/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)\n    160     \n    161     if self.rc.pprint:\n--> 162         out = pformat(arg)\n    163         if '\\n' in out:\n    164             # So that multi-line strings line up with the left column of\n\n/home/cwitty/sage/local/lib/python2.5/pprint.py in pformat(self, object)\n    109     def pformat(self, object):\n    110         sio = _StringIO()\n--> 111         self._format(object, sio, 0, 0, {}, 0)\n    112         return sio.getvalue()\n    113 \n\n/home/cwitty/sage/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)\n    127             self._readable = False\n    128             return\n--> 129         rep = self._repr(object, context, level - 1)\n    130         typ = _type(object)\n    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)\n\n/home/cwitty/sage/local/lib/python2.5/pprint.py in _repr(self, object, context, level)\n    193     def _repr(self, object, context, level):\n    194         repr, readable, recursive = self.format(object, context.copy(),\n--> 195                                                 self._depth, level)\n    196         if not readable:\n    197             self._readable = False\n\n/home/cwitty/sage/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)\n    205         and whether the object represents a recursive construct.\n    206         \"\"\"\n--> 207         return _safe_repr(object, context, maxlevels, level)\n    208 \n    209 \n\n/home/cwitty/sage/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)\n    290         return format % _commajoin(components), readable, recursive\n    291 \n--> 292     rep = repr(object)\n    293     return rep, (rep and not rep.startswith('<')), False\n    294 \n\n/home/cwitty/sage/matrix0.pyx in sage.matrix.matrix0.Matrix.__repr__ (sage/matrix/matrix0.c:4508)()\n\n/home/cwitty/sage/matrix0.pyx in sage.matrix.matrix0.Matrix.str (sage/matrix/matrix0.c:4810)()\n\n/home/cwitty/sage/matrix0.pyx in sage.matrix.matrix0.Matrix.list (sage/matrix/matrix0.c:1577)()\n\n/home/cwitty/sage/matrix_symbolic_dense.pyx in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense._list()\n\n/home/cwitty/sage/matrix_symbolic_dense.pyx in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense.get_unsafe()\n\n/home/cwitty/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py in symbolic_expression_from_maxima_string(x, equals_sub, maxima)\n   8267         return symbolic_expression_from_string(s, syms, accept_sequence=True)\n   8268     except SyntaxError:\n-> 8269         raise TypeError, \"unable to make sense of Maxima expression '%s' in SAGE\"%s\n   8270     finally:\n   8271         is_simplified = False\n\n<type 'exceptions.TypeError'>: unable to make sense of Maxima expression '(5/9)[1,1]' in SAGE\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3116\n\n",
    "closed_at": "2008-05-11T08:46:26Z",
    "created_at": "2008-05-07T01:12:37Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, positive review] 1x1 symbolic matrices don't work right",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3116",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @mwhansen

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


Issue created by migration from https://trac.sagemath.org/ticket/3116





---

archive/issue_comments_021528.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-07T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3116#issuecomment-21528",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021529.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-05-07T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3116#issuecomment-21529",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_021530.json:
```json
{
    "body": "Attachment [3116.patch](tarball://root/attachments/some-uuid/ticket3116/3116.patch) by @mwhansen created at 2008-05-07 01:47:57",
    "created_at": "2008-05-07T01:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3116#issuecomment-21530",
    "user": "https://github.com/mwhansen"
}
```

Attachment [3116.patch](tarball://root/attachments/some-uuid/ticket3116/3116.patch) by @mwhansen created at 2008-05-07 01:47:57



---

archive/issue_comments_021531.json:
```json
{
    "body": "Code looks good, doctests pass in sage/matrix.  Positive review.",
    "created_at": "2008-05-10T20:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3116#issuecomment-21531",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good, doctests pass in sage/matrix.  Positive review.



---

archive/issue_comments_021532.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T08:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3116#issuecomment-21532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_events_007040.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-11T08:46:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3116",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3116#event-7040"
}
```



---

archive/issue_comments_021533.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T08:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3116",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3116#issuecomment-21533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
