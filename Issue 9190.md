# Issue 9190: plot options reset does not reset the options dictionary

archive/issues_009190.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @mwhansen\n\nNote:\n\n\n```\nsage: plot.options\n{'fillalpha': 0.5, 'detect_poles': False, 'plot_points': 200, 'thickness': 1, 'alpha': 1, 'adaptive_tolerance': 0.01, 'fillcolor': 'automatic', 'adaptive_recursion': 5, 'exclude': None, 'rgbcolor': (0, 0, 1), 'fill': None}\nsage: plot.defaults()\n{'fillalpha': 0.5, 'detect_poles': False, 'plot_points': 200, 'thickness': 1, 'alpha': 1, 'adaptive_tolerance': 0.01, 'fillcolor': 'automatic', 'adaptive_recursion': 5, 'exclude': None, 'rgbcolor': (0, 0, 1), 'fill': None}\nsage: plot.options['fill']=True\nsage: plot.options\n{'fillalpha': 0.5, 'detect_poles': False, 'plot_points': 200, 'thickness': 1, 'alpha': 1, 'adaptive_tolerance': 0.01, 'fillcolor': 'automatic', 'adaptive_recursion': 5, 'exclude': None, 'rgbcolor': (0, 0, 1), 'fill': True}\nsage: plot.reset()\nsage: plot.options\n{'fillalpha': 0.5, 'detect_poles': False, 'plot_points': 200, 'thickness': 1, 'alpha': 1, 'adaptive_tolerance': 0.01, 'fillcolor': 'automatic', 'adaptive_recursion': 5, 'exclude': None, 'rgbcolor': (0, 0, 1), 'fill': True}\n```\n\n\nNote that the last plot.options should have fill=None, but instead is fill=True.  The funny thing is that the actual plots are correct (i.e., when the default fill is set to True, filling happens, but when reset, filling doesn't happen).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9190\n\n",
    "created_at": "2010-06-08T16:40:56Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "plot options reset does not reset the options dictionary",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9190",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @mwhansen

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

Issue created by migration from https://trac.sagemath.org/ticket/9190


