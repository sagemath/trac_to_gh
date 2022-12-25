# Issue 223: problem plotting piecewise defined functions

archive/issues_000223.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\n```\nx = PolynomialRing(RationalField(), 'x').gen()\nf1 = x^0\nf2 = 1-x\nf3 = 2*x\nf4 = 10*x-x^2\nf = Piecewise([[(0,1),f1],[(1,2),f2],[(2,3),f3],[(3,10),f4]])\nplot(f)\n///\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/Users/was/sage_notebook/worksheets/doc_browser/code/35.py\", line 10, in <module>\n    exec compile(ur'plot(f)' + '\\n', '', 'single')\n  File \"/Users/was/\", line 1, in <module>\n    \n  File \"/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 2132, in __call__\n    G = funcs.plot(xmin=xmin, xmax=xmax, **kwds)\n  File \"/Users/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 707, in plot\n    return sum([plot(p[1], p[0][0], p[0][1], **kwds ) for p in self.list()])\nTypeError: __call__() got multiple values for keyword argument 'xmin'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/223\n\n",
    "created_at": "2007-01-27T08:19:21Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "title": "problem plotting piecewise defined functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/223",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



```
x = PolynomialRing(RationalField(), 'x').gen()
f1 = x^0
f2 = 1-x
f3 = 2*x
f4 = 10*x-x^2
f = Piecewise([[(0,1),f1],[(1,2),f2],[(2,3),f3],[(3,10),f4]])
plot(f)
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/was/sage_notebook/worksheets/doc_browser/code/35.py", line 10, in <module>
    exec compile(ur'plot(f)' + '\n', '', 'single')
  File "/Users/was/", line 1, in <module>
    
  File "/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py", line 2132, in __call__
    G = funcs.plot(xmin=xmin, xmax=xmax, **kwds)
  File "/Users/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 707, in plot
    return sum([plot(p[1], p[0][0], p[0][1], **kwds ) for p in self.list()])
TypeError: __call__() got multiple values for keyword argument 'xmin'
```


Issue created by migration from https://trac.sagemath.org/ticket/223





---

archive/issue_comments_000991.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-01-27T08:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/223#issuecomment-991",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_comments_000992.json:
```json
{
    "body": "Changing component from algebraic geometry to calculus.",
    "created_at": "2007-01-27T08:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/223#issuecomment-992",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to calculus.



---

archive/issue_comments_000993.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-08-21T12:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/223#issuecomment-993",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: worksforme



---

archive/issue_comments_000994.json:
```json
{
    "body": "With Sage 2.8.2pre this works for me:\n\n```\nsage: x = PolynomialRing(RationalField(), 'x').gen()\nsage: f1 = x^0\nsage: f2 = 1-x\nsage: f3 = 2*x\nsage: f4 = 10*x-x^2\nsage: f = Piecewise([[(0,1),f1],[(1,2),f2],[(2,3),f3],[(3,10),f4]])\nsage: plot(f)\nGraphics object consisting of 4 graphics primitives\n```\n",
    "created_at": "2007-08-21T12:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/223#issuecomment-994",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With Sage 2.8.2pre this works for me:

```
sage: x = PolynomialRing(RationalField(), 'x').gen()
sage: f1 = x^0
sage: f2 = 1-x
sage: f3 = 2*x
sage: f4 = 10*x-x^2
sage: f = Piecewise([[(0,1),f1],[(1,2),f2],[(2,3),f3],[(3,10),f4]])
sage: plot(f)
Graphics object consisting of 4 graphics primitives
```

