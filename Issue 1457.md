# Issue 1457: Somewhere in a short computation: "BUG:  Rational.__pow__ called on a non-Rational"

archive/issues_001457.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following took place on an Intel Core Duo (32 bit) running Ubuntu 7.10. Hopefully the cause is obvious for someone familiar with the calculus/plotting code.\n\n(Note: replacing `f(x)` with `f(x) = 2.0 * sqrt(x^2.0 + 300.0^2.0) - x + 1000.0` is a suitable workaround.)\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.15, Release Date: 2007-12-03                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: f(x) = 2 * sqrt(x^2 + 300^2) - x + 1000\nsage: P = f.diff(x).diff(x).plot(xmin=0,xmax=1000)\n---------------------------------------------------------------------------\n<type 'exceptions.AssertionError'>        Traceback (most recent call last)\n\n/home/bober/sage-2.8.15.alpha1/<ipython console> in <module>()\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)\n    602         else:\n    603             f = self.function(param)\n--> 604         return plot(f, *args, **kwds)\n    605 \n    606     def __lt__(self, right):\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)\n   2303             G = funcs.plot(*args, **kwds)\n   2304         else:\n-> 2305             G = self._call(funcs, *args, **kwds)\n   2306         if do_show:\n   2307             G.show()\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xmin, xmax, parametric, polar, label, show, **kwds)\n   2353 \n   2354             try:\n-> 2355                 y = f(x)\n   2356                 data.append((x, float(y)))\n   2357             except (ZeroDivisionError, TypeError, ValueError), msg:\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in <lambda>(x)\n    591                 else:\n    592                     param = A[0]\n--> 593                 f = lambda x: self(x)\n    594             else:\n    595                 A = self.variables()\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, *args)\n   4012         vars = self.args()\n   4013         dct = dict( (vars[i], args[i]) for i in range(len(args)) )\n-> 4014         return self._expr.substitute(dct)\n   4015 \n   4016     def _repr_(self, simplify=True):\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in substitute(self, in_dict, **kwds)\n   2589         kwds = self.__parse_in_dict(in_dict, kwds)\n   2590         kwds = self.__varify_kwds(kwds)\n-> 2591         return X._recursive_sub(kwds)\n   2592 \n   2593     def subs(self, *args, **kwds):\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)\n   3424         \"\"\"\n   3425         ops = self._operands\n-> 3426         new_ops = [SR(op._recursive_sub(kwds)) for op in ops]\n   3427 \n   3428         #Check to see if all of the new_ops are symbolic constants\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)\n   3424         \"\"\"\n   3425         ops = self._operands\n-> 3426         new_ops = [SR(op._recursive_sub(kwds)) for op in ops]\n   3427 \n   3428         #Check to see if all of the new_ops are symbolic constants\n\n/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)\n   3430         is_constant = all(map(lambda x: isinstance(x, SymbolicConstant), new_ops))\n   3431         if is_constant:\n-> 3432             return SymbolicConstant( self._operator(*map(lambda x: x._obj, new_ops)) )\n   3433         else:\n   3434             return self._operator(*new_ops)\n\n/home/bober/sage-2.8.15.alpha1/rational.pyx in sage.rings.rational.Rational.__pow__()\n\n<type 'exceptions.AssertionError'>: BUG:  Rational.__pow__ called on a non-Rational\nsage: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1457\n\n",
    "created_at": "2007-12-11T01:26:33Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "Somewhere in a short computation: \"BUG:  Rational.__pow__ called on a non-Rational\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1457",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```
Assignee: @williamstein

The following took place on an Intel Core Duo (32 bit) running Ubuntu 7.10. Hopefully the cause is obvious for someone familiar with the calculus/plotting code.

(Note: replacing `f(x)` with `f(x) = 2.0 * sqrt(x^2.0 + 300.0^2.0) - x + 1000.0` is a suitable workaround.)


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.15, Release Date: 2007-12-03                      |
| Type notebook() for the GUI, and license() for information.        |
sage: f(x) = 2 * sqrt(x^2 + 300^2) - x + 1000
sage: P = f.diff(x).diff(x).plot(xmin=0,xmax=1000)
---------------------------------------------------------------------------
<type 'exceptions.AssertionError'>        Traceback (most recent call last)

/home/bober/sage-2.8.15.alpha1/<ipython console> in <module>()

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)
    602         else:
    603             f = self.function(param)
--> 604         return plot(f, *args, **kwds)
    605 
    606     def __lt__(self, right):

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   2303             G = funcs.plot(*args, **kwds)
   2304         else:
-> 2305             G = self._call(funcs, *args, **kwds)
   2306         if do_show:
   2307             G.show()

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xmin, xmax, parametric, polar, label, show, **kwds)
   2353 
   2354             try:
-> 2355                 y = f(x)
   2356                 data.append((x, float(y)))
   2357             except (ZeroDivisionError, TypeError, ValueError), msg:

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in <lambda>(x)
    591                 else:
    592                     param = A[0]
--> 593                 f = lambda x: self(x)
    594             else:
    595                 A = self.variables()

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in __call__(self, *args)
   4012         vars = self.args()
   4013         dct = dict( (vars[i], args[i]) for i in range(len(args)) )
-> 4014         return self._expr.substitute(dct)
   4015 
   4016     def _repr_(self, simplify=True):

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in substitute(self, in_dict, **kwds)
   2589         kwds = self.__parse_in_dict(in_dict, kwds)
   2590         kwds = self.__varify_kwds(kwds)
-> 2591         return X._recursive_sub(kwds)
   2592 
   2593     def subs(self, *args, **kwds):

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)
   3424         """
   3425         ops = self._operands
-> 3426         new_ops = [SR(op._recursive_sub(kwds)) for op in ops]
   3427 
   3428         #Check to see if all of the new_ops are symbolic constants

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)
   3424         """
   3425         ops = self._operands
-> 3426         new_ops = [SR(op._recursive_sub(kwds)) for op in ops]
   3427 
   3428         #Check to see if all of the new_ops are symbolic constants

/home/bober/sage-2.8.15.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _recursive_sub(self, kwds)
   3430         is_constant = all(map(lambda x: isinstance(x, SymbolicConstant), new_ops))
   3431         if is_constant:
-> 3432             return SymbolicConstant( self._operator(*map(lambda x: x._obj, new_ops)) )
   3433         else:
   3434             return self._operator(*new_ops)

/home/bober/sage-2.8.15.alpha1/rational.pyx in sage.rings.rational.Rational.__pow__()

<type 'exceptions.AssertionError'>: BUG:  Rational.__pow__ called on a non-Rational
sage: 
```


Issue created by migration from https://trac.sagemath.org/ticket/1457





---

archive/issue_comments_009364.json:
```json
{
    "body": "This was introduced in the massive 0^0 change--I know where to fix this.",
    "created_at": "2007-12-11T02:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9364",
    "user": "https://github.com/robertwb"
}
```

This was introduced in the massive 0^0 change--I know where to fix this.



---

archive/issue_comments_009365.json:
```json
{
    "body": "I've fixed the bug correctly. Now this draws a nice picture:\n\n```\nsage: f(x) = 2 * sqrt(x^2 + 300^2) - x + 1000\nsage: P = f.diff(x).diff(x).plot(xmin=0,xmax=1000)\nsage: P.show(ymax=0.01, ymin=0)\n```\n",
    "created_at": "2007-12-11T05:58:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9365",
    "user": "https://github.com/williamstein"
}
```

I've fixed the bug correctly. Now this draws a nice picture:

```
sage: f(x) = 2 * sqrt(x^2 + 300^2) - x + 1000
sage: P = f.diff(x).diff(x).plot(xmin=0,xmax=1000)
sage: P.show(ymax=0.01, ymin=0)
```




---

archive/issue_comments_009366.json:
```json
{
    "body": "Attachment [trac-1457.patch](tarball://root/attachments/some-uuid/ticket1457/trac-1457.patch) by @williamstein created at 2007-12-11 06:00:52",
    "created_at": "2007-12-11T06:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9366",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1457.patch](tarball://root/attachments/some-uuid/ticket1457/trac-1457.patch) by @williamstein created at 2007-12-11 06:00:52



---

archive/issue_comments_009367.json:
```json
{
    "body": "Attachment [trac-1457-part2.patch](tarball://root/attachments/some-uuid/ticket1457/trac-1457-part2.patch) by @williamstein created at 2007-12-11 06:28:56",
    "created_at": "2007-12-11T06:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9367",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1457-part2.patch](tarball://root/attachments/some-uuid/ticket1457/trac-1457-part2.patch) by @williamstein created at 2007-12-11 06:28:56



---

archive/issue_comments_009368.json:
```json
{
    "body": "Be sure to apply *both* patches, one after the other.",
    "created_at": "2007-12-11T06:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9368",
    "user": "https://github.com/williamstein"
}
```

Be sure to apply *both* patches, one after the other.



---

archive/issue_comments_009369.json:
```json
{
    "body": "this replaces the previous part 2",
    "created_at": "2007-12-15T23:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9369",
    "user": "https://github.com/williamstein"
}
```

this replaces the previous part 2



---

archive/issue_comments_009370.json:
```json
{
    "body": "Attachment [trac-1457-part2.2.patch](tarball://root/attachments/some-uuid/ticket1457/trac-1457-part2.2.patch) by @williamstein created at 2007-12-15 23:53:18\n\nIt (still) works for me, when merged against rc0.",
    "created_at": "2007-12-15T23:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9370",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1457-part2.2.patch](tarball://root/attachments/some-uuid/ticket1457/trac-1457-part2.2.patch) by @williamstein created at 2007-12-15 23:53:18

It (still) works for me, when merged against rc0.



---

archive/issue_comments_009371.json:
```json
{
    "body": "Merged in 2.9.rc2.",
    "created_at": "2007-12-16T00:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9371",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc2.



---

archive/issue_comments_009372.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-16T00:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1457#issuecomment-9372",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003718.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-16T00:38:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1457",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1457#event-3718"
}
```
