# Issue 9638: Interact sliders should be able to have negative step size

Issue created by migration from https://trac.sagemath.org/ticket/9638

Original creator: kcrisman

Original creation time: 2010-07-29 13:13:46

Assignee: itolkov, jason

Stepping backwards on sliders.  Currently, 

```
@interact 
def _(n=slider(100,0,-1,1)): 
    print n 
```

gives the error 

```
ValueError, "invalid negative step size -- step size must be 
positive" 
```

as far as I know.  Allowing this could be very helpful, but maybe 
there was a reason not to do this I am unaware of - the explicit 
ValueError leads me to think so, since whoever wrote it put knew this 
could happen! 


---

Comment by jdemeyer created at 2017-03-21 11:23:44

This also fails in Jupyter:

```
@interact 
def _(n=slider(100,0,-1,1)): 
    print n
---------------------------------------------------------------------------
TraitError                                Traceback (most recent call last)
<ipython-input-1-155f54a47ddc> in <module>()
      1 @interact
----> 2 def _(n=slider(Integer(100),Integer(0),-Integer(1),Integer(1))):
      3     print n

/usr/local/src/sage-git/local/lib/python2.7/site-packages/sage/repl/ipython_kernel/widgets_sagenb.pyc in slider(vmin, vmax, step_size, default, label, display_value, _range)
    333     if step_size is not None:
    334         kwds["step"] = step_size
--> 335     return cls(**kwds)
    336 
    337 

/usr/local/src/sage-git/local/lib/python2.7/site-packages/sage/repl/ipython_kernel/widgets.pyc in __init__(self, *args, **kwds)
     68         """
     69         self.__transform = kwds.pop("transform", None)
---> 70         return super(TransformWidget, self).__init__(*args, **kwds)
     71 
     72     def get_value(self):

/usr/local/src/sage-git/local/lib/python2.7/site-packages/ipywidgets/widgets/widget_int.pyc in __init__(self, value, min, max, step, **kwargs)
     60         if step is not None:
     61             kwargs['step'] = step
---> 62         super(cls, self).__init__(**kwargs)
     63 
     64     __init__.__doc__ = _bounded_int_doc_t

/usr/local/src/sage-git/local/lib/python2.7/site-packages/ipywidgets/widgets/widget_int.pyc in __init__(self, value, min, max, step, **kwargs)
     97         if step is not None:
     98             kwargs['step'] = step
---> 99         super(_BoundedInt, self).__init__(**kwargs)
    100 
    101     @validate('value')

/usr/local/src/sage-git/local/lib/python2.7/site-packages/ipywidgets/widgets/widget_int.pyc in __init__(self, value, **kwargs)
     78         if value is not None:
     79             kwargs['value'] = value
---> 80         super(_Int, self).__init__(**kwargs)
     81 
     82 

/usr/local/src/sage-git/local/lib/python2.7/site-packages/ipywidgets/widgets/widget.pyc in __init__(self, **kwargs)
    226         """Public constructor"""
    227         self._model_id = kwargs.pop('model_id', None)
--> 228         super(Widget, self).__init__(**kwargs)
    229 
    230         Widget._call_widget_constructed(self)

/usr/local/src/sage-git/local/lib/python2.7/site-packages/traitlets/config/configurable.pyc in __init__(self, **kwargs)
     71 
     72         # load kwarg traits, other than config
---> 73         super(Configurable, self).__init__(**kwargs)
     74 
     75         # load config

/usr/local/src/sage-git/local/lib/python2.7/site-packages/traitlets/traitlets.pyc in __init__(self, *args, **kwargs)
    996                 else:
    997                     # passthrough args that don't set traits to super
--> 998                     super_kwargs[key] = value
    999         try:
   1000             super(HasTraits, self).__init__(*super_args, **super_kwargs)

/usr/local/src/sage-git/local/lib/python/contextlib.pyc in __exit__(self, type, value, traceback)
     22         if type is None:
     23             try:
---> 24                 self.gen.next()
     25             except StopIteration:
     26                 return

/usr/local/src/sage-git/local/lib/python2.7/site-packages/traitlets/traitlets.pyc in hold_trait_notifications(self)
   1118                                 self._trait_values.pop(name)
   1119                 cache = {}
-> 1120                 raise e
   1121             finally:
   1122                 self._cross_validation_lock = False

TraitError: setting max < min
```

