# Issue 364: Unnecessary exception when creating fraction field

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2007-05-14 04:21:52

Assignee: was

Keywords: fraction field exception, variable names exception

Some uses of a ring that has no variable names assigned will cause an exception to be raised, even though there need not be any  names.  An example is appended.  The problem is that row_space() will cause the creation of a ring's fraction field, if there is not already one.

My fix, in rings/ring.pyx:CommutativeRing.fraction_field(), is to return without setting variable names, if no names are assigned.

Thoughts:

1) In structures/parent_gens.pyx:ParentWithGens.variable_names(), an exception is raised if no names are assigned.  Is this the proper behavior?  If you call this function, is the presumption that you *know* there should be names assigned?

2) Are there cases where the creation of a fraction_field *should* raise an exception if there are no assigned names?

sage: m=Matrix(Integers(5),2,2,[2,2,2,2]);

sage: m.row_space()
 ------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/site-packages/IPython/Prompts.py", line 523, in __call__
    manipulated_val = self.display(arg)
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/site-packages/IPython/Prompts.py", line 547, in _display
    return self.shell.hooks.result_display(arg)
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/site-packages/IPython/hooks.py", line 134, in __call__
    ret = cmd(*args, **kw)
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/site-packages/IPython/hooks.py", line 162, in result_display
    out = pformat(arg)
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/pprint.py", line 111, in pformat
    self._format(object, sio, 0, 0, {}, 0)
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/pprint.py", line 129, in _format
    rep = self._repr(object, context, level - 1)
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/pprint.py", line 195, in _repr
    self._depth, level)
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/pprint.py", line 207, in format
    return _safe_repr(object, context, maxlevels, level)
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/pprint.py", line 292, in _safe_repr
    rep = repr(object)
  File "sage_object.pyx", line 87, in sage_object.SageObject.__repr__
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/site-packages/sage/modules/free_module.py", line 3500, in _repr_
    self.degree(), self.dimension(), self.base_field()) + \
  File "/SandBox/Justin/sb/sage-2.5/local/lib/python2.5/site-packages/sage/modules/free_module.py", line 1289, in base_field
    return self.base_ring().fraction_field()
  File "ring.pyx", line 593, in ring.CommutativeRing.fraction_field
  File "parent_gens.pyx", line 366, in parent_gens.ParentWithGens.variable_names
<type 'exceptions.ValueError'>: variable names have not yet been set using self._assign_names(...)




---

Comment by was created at 2007-05-18 13:21:13

Resolution: fixed


---

Comment by was created at 2007-05-18 13:21:13

I think all fraction fields should have their names assigned in the fraction field constructor.
I've modified 2.5.1 so this is the case.  

All fraction fields should have variable_names() set on creation.  It was a mistake to omit
that from the constructor.
