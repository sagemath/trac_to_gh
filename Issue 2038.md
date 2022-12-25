# Issue 2038: plotting -- error message when failing to evaluate at a point is now sucky (it used to be good)

archive/issues_002038.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt used to be that this would give a sensible error message about the number of points at which evaluating the function failed (and what the first error was):\n\n\n```\nsage: plot(factorial,(2,10))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)\n   3343             # if there is one extra arg, then it had better be a tuple\n   3344             elif n == 1:\n-> 3345                 G = self._call(funcs, *args, **kwds)\n   3346             elif n == 2:\n   3347             # if ther eare two extra args, then pull them out and pass them as a tuple\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xrange, parametric, polar, label, **kwds)\n   3419         del options['plot_division']\n   3420         while i < len(data) - 1:\n-> 3421             if abs(data[i+1][1] - data[i][1]) > max_bend:\n   3422                 x = (data[i+1][0] + data[i][0])/2\n   3423                 try:\n\n<type 'exceptions.TypeError'>: 'float' object is unsubscriptable\n```\n\n\nThe exception of course should mention that:\n\n\n```\nsage: factorial(1.5)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/rings/arith.py in factorial(n, algorithm)\n    273     Z = integer_ring.ZZ\n    274     if algorithm == 'gmp':\n--> 275         return Z(n).factorial()\n    276     elif algorithm == 'pari':\n    277         return Z(pari('%s!'%Z(n)))\n\n/Users/was/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()\n\n<type 'exceptions.TypeError'>: Attempt to coerce non-integral RealNumber to Integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2038\n\n",
    "created_at": "2008-02-03T20:00:23Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "plotting -- error message when failing to evaluate at a point is now sucky (it used to be good)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2038",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

It used to be that this would give a sensible error message about the number of points at which evaluating the function failed (and what the first error was):


```
sage: plot(factorial,(2,10))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3343             # if there is one extra arg, then it had better be a tuple
   3344             elif n == 1:
-> 3345                 G = self._call(funcs, *args, **kwds)
   3346             elif n == 2:
   3347             # if ther eare two extra args, then pull them out and pass them as a tuple

/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xrange, parametric, polar, label, **kwds)
   3419         del options['plot_division']
   3420         while i < len(data) - 1:
-> 3421             if abs(data[i+1][1] - data[i][1]) > max_bend:
   3422                 x = (data[i+1][0] + data[i][0])/2
   3423                 try:

<type 'exceptions.TypeError'>: 'float' object is unsubscriptable
```


The exception of course should mention that:


```
sage: factorial(1.5)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/rings/arith.py in factorial(n, algorithm)
    273     Z = integer_ring.ZZ
    274     if algorithm == 'gmp':
--> 275         return Z(n).factorial()
    276     elif algorithm == 'pari':
    277         return Z(pari('%s!'%Z(n)))

/Users/was/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: Attempt to coerce non-integral RealNumber to Integer
```


Issue created by migration from https://trac.sagemath.org/ticket/2038





---

archive/issue_comments_013157.json:
```json
{
    "body": "See also #2045.",
    "created_at": "2008-02-04T18:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13157",
    "user": "https://github.com/williamstein"
}
```

See also #2045.



---

archive/issue_comments_013158.json:
```json
{
    "body": "Attachment [plot.patch](tarball://root/attachments/some-uuid/ticket2038/plot.patch) by @bobmoretti created at 2008-02-08 00:03:20",
    "created_at": "2008-02-08T00:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13158",
    "user": "https://github.com/bobmoretti"
}
```

Attachment [plot.patch](tarball://root/attachments/some-uuid/ticket2038/plot.patch) by @bobmoretti created at 2008-02-08 00:03:20



---

archive/issue_comments_013159.json:
```json
{
    "body": "Please review this fix.",
    "created_at": "2008-02-08T00:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13159",
    "user": "https://github.com/bobmoretti"
}
```

Please review this fix.



---

archive/issue_comments_013160.json:
```json
{
    "body": "Actually, the fix that I posted only fixes http://trac.sagemath.org/sage_trac/ticket/2038 which was listed as a dupe of this bug, but in fact is not. I will fix the issue reported here and provide another fix.",
    "created_at": "2008-02-08T00:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13160",
    "user": "https://github.com/bobmoretti"
}
```

Actually, the fix that I posted only fixes http://trac.sagemath.org/sage_trac/ticket/2038 which was listed as a dupe of this bug, but in fact is not. I will fix the issue reported here and provide another fix.



---

archive/issue_comments_013161.json:
```json
{
    "body": "Check out empty_plot_list.patch; together with plot.patch it fixes both this ticket and http://trac.sagemath.org/sage_trac/ticket/2045.",
    "created_at": "2008-02-08T07:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13161",
    "user": "https://github.com/bobmoretti"
}
```

Check out empty_plot_list.patch; together with plot.patch it fixes both this ticket and http://trac.sagemath.org/sage_trac/ticket/2045.



---

archive/issue_comments_013162.json:
```json
{
    "body": "I can't tell what the issue was or what the corrected behaviour is, BECAUSE THERE ARE NO DOCTESTS.  I say do not apply.\n\nThe patch looks good, but I don't think it's been tested enough.  For example, what happens if there are *no* valid data points?",
    "created_at": "2008-02-15T04:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13162",
    "user": "https://github.com/ncalexan"
}
```

I can't tell what the issue was or what the corrected behaviour is, BECAUSE THERE ARE NO DOCTESTS.  I say do not apply.

The patch looks good, but I don't think it's been tested enough.  For example, what happens if there are *no* valid data points?



---

archive/issue_comments_013163.json:
```json
{
    "body": "This must get fixed.  This seems to be responsible for about 1/3 of bug/confusions on sage-support.",
    "created_at": "2008-03-12T05:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13163",
    "user": "https://github.com/williamstein"
}
```

This must get fixed.  This seems to be responsible for about 1/3 of bug/confusions on sage-support.



---

archive/issue_comments_013164.json:
```json
{
    "body": "Yet another fix of this is up at #2517.  The various patches should be combined into one good patch.",
    "created_at": "2008-03-18T21:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13164",
    "user": "https://github.com/jasongrout"
}
```

Yet another fix of this is up at #2517.  The various patches should be combined into one good patch.



---

archive/issue_comments_013165.json:
```json
{
    "body": "Where is the \"empty_plot_list.patch\" that is referred to above?  Is the above plot.patch and the patch at #2517 the only patches that address this problem (and the ones that should be combined?)",
    "created_at": "2008-03-18T22:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13165",
    "user": "https://github.com/jasongrout"
}
```

Where is the "empty_plot_list.patch" that is referred to above?  Is the above plot.patch and the patch at #2517 the only patches that address this problem (and the ones that should be combined?)



---

archive/issue_comments_013166.json:
```json
{
    "body": "This ticket is addressed now with #2517 and #2590 and should probably be marked a duplicate.",
    "created_at": "2008-03-19T01:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13166",
    "user": "https://github.com/jasongrout"
}
```

This ticket is addressed now with #2517 and #2590 and should probably be marked a duplicate.



---

archive/issue_events_002194.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-19T02:17:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2038#event-2194"
}
```



---

archive/issue_comments_013167.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-19T02:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2038#issuecomment-13167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate
