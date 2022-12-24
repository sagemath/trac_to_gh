# Issue 6947: [with patch, needs review] make complex_plot() work for for fast_callable functions

archive/issues_006947.json:
```json
{
    "body": "Assignee: was\n\nThis current behavior of Sage demonstrates a bug, which probably also affects other complex valued functions that cannot be converted into real valued functions.\n\n\n\n```\nsage: f(x) = x^2                               \nsage: g = fast_callable(f, domain=CC, vars='x')\nsage: P = complex_plot(f, (-10, 10), (-10, 10))\nsage: Q = complex_plot(g, (-10, 10), (-10, 10))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (35, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/bober/.sage/temp/bober/1740/_home_bober__sage_init_sage_0.py in <module>()\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)\n    133                 options['__original_opts'] = kwds\n    134             options.update(kwds)\n--> 135             return func(*args, **options)\n    136 \n    137         \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/complex_plot.so in sage.plot.complex_plot.complex_plot (sage/plot/complex_plot.c:4104)()\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/plot.pyc in setup_for_eval_on_grid(v, xrange, yrange, plot_points)\n   2874             from sage.plot.plot3d.parametric_plot3d import adapt_to_callable\n   2875             if xvar is None:\n-> 2876                 k, _ = adapt_to_callable([f], 2)\n   2877                 g.append(k[0])\n   2878             else:\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/parametric_plot3d.pyc in adapt_to_callable(f, nargs)\n    649     except TypeError:\n    650         vars = ()\n--> 651         f = [fast_float_constant(x) for x in f]\n    652     \n    653     if nargs is not None and len(vars) != nargs:\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/ext/fast_eval.so in sage.ext.fast_eval.fast_float_constant (sage/ext/fast_eval.c:8030)()\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/ext/fast_eval.so in sage.ext.fast_eval.FastDoubleFunc.__init__ (sage/ext/fast_eval.c:3492)()\n\nTypeError: a float is required\n```\n\n\n\nThe attached patch fixes this. (It is a one character fix, but someone who knows the plotting code should make sure it is the right fix.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6947\n\n",
    "created_at": "2009-09-16T21:08:42Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] make complex_plot() work for for fast_callable functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6947",
    "user": "bober"
}
```
Assignee: was

This current behavior of Sage demonstrates a bug, which probably also affects other complex valued functions that cannot be converted into real valued functions.



```
sage: f(x) = x^2                               
sage: g = fast_callable(f, domain=CC, vars='x')
sage: P = complex_plot(f, (-10, 10), (-10, 10))
sage: Q = complex_plot(g, (-10, 10), (-10, 10))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (35, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/bober/.sage/temp/bober/1740/_home_bober__sage_init_sage_0.py in <module>()

/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    133                 options['__original_opts'] = kwds
    134             options.update(kwds)
--> 135             return func(*args, **options)
    136 
    137         

/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/complex_plot.so in sage.plot.complex_plot.complex_plot (sage/plot/complex_plot.c:4104)()

/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/plot.pyc in setup_for_eval_on_grid(v, xrange, yrange, plot_points)
   2874             from sage.plot.plot3d.parametric_plot3d import adapt_to_callable
   2875             if xvar is None:
-> 2876                 k, _ = adapt_to_callable([f], 2)
   2877                 g.append(k[0])
   2878             else:

/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/parametric_plot3d.pyc in adapt_to_callable(f, nargs)
    649     except TypeError:
    650         vars = ()
--> 651         f = [fast_float_constant(x) for x in f]
    652     
    653     if nargs is not None and len(vars) != nargs:

/home/bober/sage/local/lib/python2.6/site-packages/sage/ext/fast_eval.so in sage.ext.fast_eval.fast_float_constant (sage/ext/fast_eval.c:8030)()

/home/bober/sage/local/lib/python2.6/site-packages/sage/ext/fast_eval.so in sage.ext.fast_eval.FastDoubleFunc.__init__ (sage/ext/fast_eval.c:3492)()

TypeError: a float is required
```



The attached patch fixes this. (It is a one character fix, but someone who knows the plotting code should make sure it is the right fix.)


Issue created by migration from https://trac.sagemath.org/ticket/6947





---

archive/issue_comments_057440.json:
```json
{
    "body": "Attachment [trac6947.patch](tarball://root/attachments/some-uuid/ticket6947/trac6947.patch) by jason created at 2009-09-22 14:33:18\n\nThis looks great.  The reviewer patch just adds the tests above as doctests.\n\nAs another ticket, complex_plot really needs to convert it's arguments to fast_callable(..., domain=CDF).  See #6985 for timing examples.",
    "created_at": "2009-09-22T14:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6947#issuecomment-57440",
    "user": "jason"
}
```

Attachment [trac6947.patch](tarball://root/attachments/some-uuid/ticket6947/trac6947.patch) by jason created at 2009-09-22 14:33:18

This looks great.  The reviewer patch just adds the tests above as doctests.

As another ticket, complex_plot really needs to convert it's arguments to fast_callable(..., domain=CDF).  See #6985 for timing examples.



---

archive/issue_comments_057441.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2009-09-22T14:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6947#issuecomment-57441",
    "user": "jason"
}
```

apply on top of previous patch



---

archive/issue_comments_057442.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-23T07:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6947#issuecomment-57442",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057443.json:
```json
{
    "body": "Attachment [trac-6947-review.patch](tarball://root/attachments/some-uuid/ticket6947/trac-6947-review.patch) by mvngu created at 2009-09-23 07:10:10",
    "created_at": "2009-09-23T07:10:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6947#issuecomment-57443",
    "user": "mvngu"
}
```

Attachment [trac-6947-review.patch](tarball://root/attachments/some-uuid/ticket6947/trac-6947-review.patch) by mvngu created at 2009-09-23 07:10:10



---

archive/issue_comments_057444.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6947#issuecomment-57444",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
