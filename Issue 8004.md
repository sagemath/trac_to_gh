# Issue 8004: region_plot does not handle lambda functions

archive/issues_008004.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman\n\n\n```\nsage: sage: region_plot(lambda x,y: x>y, (-4,4), (-4,4))\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/devel/sage-main/sage/<ipython console> in <module>()\n\n/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)\n    136                 options['__original_opts'] = kwds\n    137             options.update(kwds)\n--> 138             return func(*args, **options)\n    139 \n    140         \n\n/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/contour_plot.pyc in region_plot(f, xrange, yrange, plot_points, incol, outcol, bordercol, borderstyle, borderwidth)\n    561         f = [f]\n    562 \n--> 563     f = [equify(g) for g in f]\n    564 \n    565     g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)\n\n/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/contour_plot.pyc in equify(f)\n    626     import operator\n    627     from sage.calculus.all import symbolic_expression\n--> 628     op = f.operator()\n    629     if op is operator.gt or op is operator.ge:\n    630         return symbolic_expression(f.rhs() - f.lhs())\n\nAttributeError: 'function' object has no attribute 'operator'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8004\n\n",
    "created_at": "2010-01-19T22:59:50Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "region_plot does not handle lambda functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8004",
    "user": "jason"
}
```
Assignee: was

CC:  kcrisman


```
sage: sage: region_plot(lambda x,y: x>y, (-4,4), (-4,4))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/devel/sage-main/sage/<ipython console> in <module>()

/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    136                 options['__original_opts'] = kwds
    137             options.update(kwds)
--> 138             return func(*args, **options)
    139 
    140         

/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/contour_plot.pyc in region_plot(f, xrange, yrange, plot_points, incol, outcol, bordercol, borderstyle, borderwidth)
    561         f = [f]
    562 
--> 563     f = [equify(g) for g in f]
    564 
    565     g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)

/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/contour_plot.pyc in equify(f)
    626     import operator
    627     from sage.calculus.all import symbolic_expression
--> 628     op = f.operator()
    629     if op is operator.gt or op is operator.ge:
    630         return symbolic_expression(f.rhs() - f.lhs())

AttributeError: 'function' object has no attribute 'operator'
```


Issue created by migration from https://trac.sagemath.org/ticket/8004





---

archive/issue_comments_069943.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-20T00:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8004#issuecomment-69943",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_069944.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T00:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8004#issuecomment-69944",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069945.json:
```json
{
    "body": "This also resolves #7807",
    "created_at": "2010-01-20T00:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8004#issuecomment-69945",
    "user": "jason"
}
```

This also resolves #7807



---

archive/issue_comments_069946.json:
```json
{
    "body": "See also #4677 for a related issue.",
    "created_at": "2010-01-20T02:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8004#issuecomment-69946",
    "user": "kcrisman"
}
```

See also #4677 for a related issue.



---

archive/issue_comments_069947.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T09:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8004#issuecomment-69947",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069948.json:
```json
{
    "body": "Despite a depreciation message, this worked as expected for all the cases I tried.\n\n\n```\nsage: var('x y')\n(x, y)\n\nsage: region_plot(lambda x,y: x>y, (-4,4), (-4,4)) # works\n\nsage: region_plot([lambda x,y: x>y, lambda x,y: x^2+y^2<10], (-4,4), (-4,4)) # a list of lambdas also work\n\n#\n# Tried mixing the forms of the functions (one being a lamba and one an expression)\n# - got a depreciation message! (But still displayed the plot correctly) \n#\nsage: region_plot([lambda x,y: x>y, x^2+y^2<10], (-4,4), (-4,4))\n/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/plot/contour_plot.py:569: DeprecationWarning: Unnamed ranges for more than one variable is deprecated and will be removed from a future release of Sage; you can used named ranges instead, like (x,0,2)\n  g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)\n\n# ...but parentheses also produced the same plot correctly without the message \nsage: region_plot([(lambda x,y: x>y), (x^2+y^2<10)], (-4,4), (-4,4))\n\n# tried the former example again - no depreciated message this time (!?)\n# (Does sage only show depreciations once?) \nsage: region_plot([lambda x,y: x>y, x^2+y^2<10], (-4,4), (-4,4))\n\n# this worked too\nsage: region_plot([lambda x,y: x>y, lambda x,y: x^2+y^2<10], (-4,4), (-4,4), aspect_ratio=1)\n```\n",
    "created_at": "2010-01-31T09:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8004#issuecomment-69948",
    "user": "rossk"
}
```

Despite a depreciation message, this worked as expected for all the cases I tried.


```
sage: var('x y')
(x, y)

sage: region_plot(lambda x,y: x>y, (-4,4), (-4,4)) # works

sage: region_plot([lambda x,y: x>y, lambda x,y: x^2+y^2<10], (-4,4), (-4,4)) # a list of lambdas also work

#
# Tried mixing the forms of the functions (one being a lamba and one an expression)
# - got a depreciation message! (But still displayed the plot correctly) 
#
sage: region_plot([lambda x,y: x>y, x^2+y^2<10], (-4,4), (-4,4))
/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/plot/contour_plot.py:569: DeprecationWarning: Unnamed ranges for more than one variable is deprecated and will be removed from a future release of Sage; you can used named ranges instead, like (x,0,2)
  g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)

# ...but parentheses also produced the same plot correctly without the message 
sage: region_plot([(lambda x,y: x>y), (x^2+y^2<10)], (-4,4), (-4,4))

# tried the former example again - no depreciated message this time (!?)
# (Does sage only show depreciations once?) 
sage: region_plot([lambda x,y: x>y, x^2+y^2<10], (-4,4), (-4,4))

# this worked too
sage: region_plot([lambda x,y: x>y, lambda x,y: x^2+y^2<10], (-4,4), (-4,4), aspect_ratio=1)
```




---

archive/issue_comments_069949.json:
```json
{
    "body": "I've refreshed the commit string to\n\n```\n#8004: Make region_plot accept lambda functions\n```\n\nin the queue for 4.3.3.alpha0.",
    "created_at": "2010-02-10T15:27:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8004#issuecomment-69949",
    "user": "mpatel"
}
```

I've refreshed the commit string to

```
#8004: Make region_plot accept lambda functions
```

in the queue for 4.3.3.alpha0.



---

archive/issue_comments_069950.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8004#issuecomment-69950",
    "user": "mpatel"
}
```

Resolution: fixed
