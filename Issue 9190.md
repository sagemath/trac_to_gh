# Issue 9190: plot options reset does not reset the options dictionary

Issue created by migration from https://trac.sagemath.org/ticket/9190

Original creator: jason

Original creation time: 2010-06-08 16:40:56

Assignee: jason, was

CC:  mhansen

Note:


```
sage: plot.options
{'fillalpha': 0.5, 'detect_poles': False, 'plot_points': 200, 'thickness': 1, 'alpha': 1, 'adaptive_tolerance': 0.01, 'fillcolor': 'automatic', 'adaptive_recursion': 5, 'exclude': None, 'rgbcolor': (0, 0, 1), 'fill': None}
sage: plot.defaults()
{'fillalpha': 0.5, 'detect_poles': False, 'plot_points': 200, 'thickness': 1, 'alpha': 1, 'adaptive_tolerance': 0.01, 'fillcolor': 'automatic', 'adaptive_recursion': 5, 'exclude': None, 'rgbcolor': (0, 0, 1), 'fill': None}
sage: plot.options['fill']=True
sage: plot.options
{'fillalpha': 0.5, 'detect_poles': False, 'plot_points': 200, 'thickness': 1, 'alpha': 1, 'adaptive_tolerance': 0.01, 'fillcolor': 'automatic', 'adaptive_recursion': 5, 'exclude': None, 'rgbcolor': (0, 0, 1), 'fill': True}
sage: plot.reset()
sage: plot.options
{'fillalpha': 0.5, 'detect_poles': False, 'plot_points': 200, 'thickness': 1, 'alpha': 1, 'adaptive_tolerance': 0.01, 'fillcolor': 'automatic', 'adaptive_recursion': 5, 'exclude': None, 'rgbcolor': (0, 0, 1), 'fill': True}
```


Note that the last plot.options should have fill=None, but instead is fill=True.  The funny thing is that the actual plots are correct (i.e., when the default fill is set to True, filling happens, but when reset, filling doesn't happen).
