# Issue 2858: parametric_plot3d doesn't like "-u"

archive/issues_002858.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following two plots should give the same thing.\n\n```\nsage: parametric_plot3d((u,-u,v), (-10,10),(-10,10))\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/grout/.sage/sage_notebook/worksheets/admin/43/code/101.py\", line 6, in <module>\n    parametric_plot3d((u,-u,v), (-Integer(10),Integer(10)),(-Integer(10),Integer(10)))\n  File \"/home/grout/sage/local/lib/python2.5/site-packages/sympy/plotting/\", line 1, in <module>\n    \n  File \"/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py\", line 362, in parametric_plot3d\n    G = parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)\n  File \"/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py\", line 423, in parametric_plot3d_surface\n    g, (u,v) = adapt_to_callable(f, 2)\n  File \"/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py\", line 492, in adapt_to_callable\n    return fast_float(f, *vars), vars\n  File \"fast_eval.pyx\", line 1276, in sage.ext.fast_eval.fast_float\n  File \"fast_eval.pyx\", line 1288, in sage.ext.fast_eval.fast_float\n  File \"/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 5102, in _fast_float_\n    raise ValueError, \"free variable: %s\" % self._name\nValueError: free variable: u\n\nsage: parametric_plot3d((u,(-2*u+2)/2-1,v), (-10,10),(-10,10))\n(this works)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2858\n\n",
    "created_at": "2008-04-08T21:08:25Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "parametric_plot3d doesn't like \"-u\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2858",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

The following two plots should give the same thing.

```
sage: parametric_plot3d((u,-u,v), (-10,10),(-10,10))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/grout/.sage/sage_notebook/worksheets/admin/43/code/101.py", line 6, in <module>
    parametric_plot3d((u,-u,v), (-Integer(10),Integer(10)),(-Integer(10),Integer(10)))
  File "/home/grout/sage/local/lib/python2.5/site-packages/sympy/plotting/", line 1, in <module>
    
  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py", line 362, in parametric_plot3d
    G = parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)
  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py", line 423, in parametric_plot3d_surface
    g, (u,v) = adapt_to_callable(f, 2)
  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py", line 492, in adapt_to_callable
    return fast_float(f, *vars), vars
  File "fast_eval.pyx", line 1276, in sage.ext.fast_eval.fast_float
  File "fast_eval.pyx", line 1288, in sage.ext.fast_eval.fast_float
  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5102, in _fast_float_
    raise ValueError, "free variable: %s" % self._name
ValueError: free variable: u

sage: parametric_plot3d((u,(-2*u+2)/2-1,v), (-10,10),(-10,10))
(this works)
```


Issue created by migration from https://trac.sagemath.org/ticket/2858





---

archive/issue_events_006540.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-09T01:02:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2858#event-6540"
}
```



---

archive/issue_comments_019561.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-04-09T01:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19561",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_019562.json:
```json
{
    "body": "This is a duplicate of #1877. I think it should be possible to use a variable mutliple times in the range, i.e. `x,x` or also `x,-x`. Since this description is far from precise, i.e. one would never find it looking for the issue, I am closing this.\n\nJason: feel free to reopen if you disagree. \n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T01:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19562",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a duplicate of #1877. I think it should be possible to use a variable mutliple times in the range, i.e. `x,x` or also `x,-x`. Since this description is far from precise, i.e. one would never find it looking for the issue, I am closing this.

Jason: feel free to reopen if you disagree. 

Cheers,

Michael



---

archive/issue_comments_019563.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-04-09T01:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19563",
    "user": "https://github.com/jasongrout"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_019564.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-09T01:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19564",
    "user": "https://github.com/jasongrout"
}
```

Changing status from closed to reopened.



---

archive/issue_events_006541.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2008-04-09T01:30:51Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2858#event-6541"
}
```



---

archive/issue_comments_019565.json:
```json
{
    "body": "To my understanding, the issue in #1877 was the specifying of the same variable in two different ranges.  This issue is different: when I use \"-u\", I get an error, but when I use an expression that is equivalent to \"-u\", I don't get an error.  In either case, I'm not specifying two of the same variable for the ranges.\n\nI think these issues are different.  They may be symptoms of the same thing, but I doubt it.",
    "created_at": "2008-04-09T01:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19565",
    "user": "https://github.com/jasongrout"
}
```

To my understanding, the issue in #1877 was the specifying of the same variable in two different ranges.  This issue is different: when I use "-u", I get an error, but when I use an expression that is equivalent to "-u", I don't get an error.  In either case, I'm not specifying two of the same variable for the ranges.

I think these issues are different.  They may be symptoms of the same thing, but I doubt it.



---

archive/issue_events_006542.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2008-04-09T01:30:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2858#event-6542"
}
```



---

archive/issue_comments_019566.json:
```json
{
    "body": "Changing the issue title to be more descriptive.\n\nTo elaborate on the reopening: the issue here is not with the ranges (to my knowledge, it isn't even possible to specify variables for the ranges in parametric_plot3d).  The issue here is with the components of the function being plotted.",
    "created_at": "2008-04-09T01:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19566",
    "user": "https://github.com/jasongrout"
}
```

Changing the issue title to be more descriptive.

To elaborate on the reopening: the issue here is not with the ranges (to my knowledge, it isn't even possible to specify variables for the ranges in parametric_plot3d).  The issue here is with the components of the function being plotted.



---

archive/issue_comments_019567.json:
```json
{
    "body": "Ok, agreed that this is a different bug than #1877:\n\n```\nsage: var('u v t')\n(u, v, t)\nsage: parametric_plot3d((u,-v,t), (-10,10),(-10,10))\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha3/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in parametric_plot3d(f, urange, vrange, plot_points, **kwds)\n    360         if plot_points == \"automatic\":\n    361             plot_points = [40,40]\n--> 362         G = parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)\n    363     G._set_extra_kwds(kwds)\n    364     return G\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)\n    421\n    422         try:\n--> 423             g, (u,v) = adapt_to_callable(f, 2)\n    424         except TypeError:\n    425             g = tuple(f)\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in adapt_to_callable(f, nargs)\n    488\n    489     if nargs is not None and len(vars) != nargs:\n    490         vars = (vars + ('_',)*nargs)[:nargs]\n    491\n--> 492     return fast_float(f, *vars), vars\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha3/fast_eval.pyx in sage.ext.fast_eval.fast_float()\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha3/fast_eval.pyx in sage.ext.fast_eval.fast_float()\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _fast_float_(self, *vars)\n   4598             1.0\n   4599         \"\"\"\n-> 4600         fops = [op._fast_float_(*vars) for op in self._operands]\n   4601         return self._operator(*fops)\n   4602\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _fast_float_(self, *vars)\n   5112             return fast_float.fast_float_constant(float(self))\n   5113         except TypeError:\n-> 5114             raise ValueError, \"free variable: %s\" % self._name\n   5115\n   5116     def _recursive_sub(self, kwds):\n\n<type 'exceptions.ValueError'>: free variable: v\nsage:\n```\nUsing u twice in the range might have obscured the real bug from my POV. Mea culpa.\n\n+1 on the better description.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-09T01:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19567",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, agreed that this is a different bug than #1877:

```
sage: var('u v t')
(u, v, t)
sage: parametric_plot3d((u,-v,t), (-10,10),(-10,10))
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in parametric_plot3d(f, urange, vrange, plot_points, **kwds)
    360         if plot_points == "automatic":
    361             plot_points = [40,40]
--> 362         G = parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)
    363     G._set_extra_kwds(kwds)
    364     return G

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)
    421
    422         try:
--> 423             g, (u,v) = adapt_to_callable(f, 2)
    424         except TypeError:
    425             g = tuple(f)

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in adapt_to_callable(f, nargs)
    488
    489     if nargs is not None and len(vars) != nargs:
    490         vars = (vars + ('_',)*nargs)[:nargs]
    491
--> 492     return fast_float(f, *vars), vars

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/fast_eval.pyx in sage.ext.fast_eval.fast_float()

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/fast_eval.pyx in sage.ext.fast_eval.fast_float()

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _fast_float_(self, *vars)
   4598             1.0
   4599         """
-> 4600         fops = [op._fast_float_(*vars) for op in self._operands]
   4601         return self._operator(*fops)
   4602

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _fast_float_(self, *vars)
   5112             return fast_float.fast_float_constant(float(self))
   5113         except TypeError:
-> 5114             raise ValueError, "free variable: %s" % self._name
   5115
   5116     def _recursive_sub(self, kwds):

<type 'exceptions.ValueError'>: free variable: v
sage:
```
Using u twice in the range might have obscured the real bug from my POV. Mea culpa.

+1 on the better description.

Cheers,

Michael



---

archive/issue_comments_019568.json:
```json
{
    "body": "The problem seems to be in parametric_plot3d.py in adapt_to_callable, in the line \"s=sum(f)\".  If there is a u and a -u as components of f, then sum(f) cancels these and the variable disappears.",
    "created_at": "2008-04-09T02:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19568",
    "user": "https://github.com/jasongrout"
}
```

The problem seems to be in parametric_plot3d.py in adapt_to_callable, in the line "s=sum(f)".  If there is a u and a -u as components of f, then sum(f) cancels these and the variable disappears.



---

archive/issue_comments_019569.json:
```json
{
    "body": "Attachment [trac_2858.patch](tarball://root/attachments/some-uuid/ticket2858/trac_2858.patch) by @williamstein created at 2009-01-24 11:41:22\n\nmike found one bug which this fixes.",
    "created_at": "2009-01-24T11:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19569",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_2858.patch](tarball://root/attachments/some-uuid/ticket2858/trac_2858.patch) by @williamstein created at 2009-01-24 11:41:22

mike found one bug which this fixes.



---

archive/issue_comments_019570.json:
```json
{
    "body": "Attachment [trac_2858-part2.patch](tarball://root/attachments/some-uuid/ticket2858/trac_2858-part2.patch) by @mwhansen created at 2009-01-24 11:45:53",
    "created_at": "2009-01-24T11:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19570",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_2858-part2.patch](tarball://root/attachments/some-uuid/ticket2858/trac_2858-part2.patch) by @mwhansen created at 2009-01-24 11:45:53



---

archive/issue_comments_019571.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-24T11:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19571",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_019572.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T14:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19572",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019573.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha3",
    "created_at": "2009-01-28T14:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2858#issuecomment-19573",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha3



---

archive/issue_events_006543.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T14:11:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2858#event-6543"
}
```



---

archive/issue_events_006544.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T14:11:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2858#event-6544"
}
```



---

archive/issue_events_006545.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-28T14:11:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2858",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2858#event-6545"
}
```
