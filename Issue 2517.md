# Issue 2517: ignore bad values in plot

archive/issues_002517.json:
```json
{
    "body": "Assignee: was\n\n\n```\n> >  Hi,\n> >\n> >  With sage-2.10.3 the following plot fails:\n> >\n> >  plot(-x*log(x),0,1, plot_points=1000)\n> >\n> >  This worked fine in sage-2.10.2. Note that the left hand limit is\n> >  well-defined and can be approximated:\n> >\n> >  plot(-x*log(x),0.00000000000000001,1, plot_points=1000)\n> >\n> >  Is this a feature or a bug?\n\nIt fails because it used to be that there was a bug where when\nplotting the left and right endpoints were omitted, because the sample\npoints were *all* randomized!  This really\nannoyed a lot of people, especially people making animations,\nbut allowed the above example to work.\n\nI think the solution is to fix our plotting code so that it just automatically\ncompletely ignores a few bad values (like it used to), possibly printing\na warning.\n\n -- William\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2517\n\n",
    "created_at": "2008-03-14T16:58:53Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "ignore bad values in plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2517",
    "user": "jason"
}
```
Assignee: was


```
> >  Hi,
> >
> >  With sage-2.10.3 the following plot fails:
> >
> >  plot(-x*log(x),0,1, plot_points=1000)
> >
> >  This worked fine in sage-2.10.2. Note that the left hand limit is
> >  well-defined and can be approximated:
> >
> >  plot(-x*log(x),0.00000000000000001,1, plot_points=1000)
> >
> >  Is this a feature or a bug?

It fails because it used to be that there was a bug where when
plotting the left and right endpoints were omitted, because the sample
points were *all* randomized!  This really
annoyed a lot of people, especially people making animations,
but allowed the above example to work.

I think the solution is to fix our plotting code so that it just automatically
completely ignores a few bad values (like it used to), possibly printing
a warning.

 -- William
```



Issue created by migration from https://trac.sagemath.org/ticket/2517





---

archive/issue_comments_017165.json:
```json
{
    "body": "We should possible plot the endpoints *and* randomized values just inside the endpoints for cases like this.",
    "created_at": "2008-03-14T18:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17165",
    "user": "robertwb"
}
```

We should possible plot the endpoints *and* randomized values just inside the endpoints for cases like this.



---

archive/issue_comments_017166.json:
```json
{
    "body": "The patch above takes care of two things:\n* ignores points that have OverflowError when evaluated\n* deletes erroneous points from the plot, thereby solving the longstanding bug of \"float not subscriptable\" mentioned lots of times previously, for example, when plotting x^(1/3).",
    "created_at": "2008-03-14T21:21:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17166",
    "user": "jason"
}
```

The patch above takes care of two things:
* ignores points that have OverflowError when evaluated
* deletes erroneous points from the plot, thereby solving the longstanding bug of "float not subscriptable" mentioned lots of times previously, for example, when plotting x^(1/3).



---

archive/issue_comments_017167.json:
```json
{
    "body": "I think this line in the patch\n\n```\nprint i, data[i], i+1, data[i+1] \n```\n\nwas for debugging purposes and should be deleted.",
    "created_at": "2008-03-14T21:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17167",
    "user": "was"
}
```

I think this line in the patch

```
print i, data[i], i+1, data[i+1] 
```

was for debugging purposes and should be deleted.



---

archive/issue_comments_017168.json:
```json
{
    "body": "Attachment [plot_undefined.patch](tarball://root/attachments/some-uuid/ticket2517/plot_undefined.patch) by jason created at 2008-03-14 21:36:53",
    "created_at": "2008-03-14T21:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17168",
    "user": "jason"
}
```

Attachment [plot_undefined.patch](tarball://root/attachments/some-uuid/ticket2517/plot_undefined.patch) by jason created at 2008-03-14 21:36:53



---

archive/issue_comments_017169.json:
```json
{
    "body": "Sorry, I thought I uploaded a new patch before anyone saw :).  The current patch does not have that line.",
    "created_at": "2008-03-15T01:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17169",
    "user": "jason"
}
```

Sorry, I thought I uploaded a new patch before anyone saw :).  The current patch does not have that line.



---

archive/issue_comments_017170.json:
```json
{
    "body": "I applied your patch and it doesn't work.  The example above failes with `<type 'exceptions.TypeError'>: 'tuple' object is not callable`:\n\n\n```\n\nsage:  plot(-x*log(x),0,1, plot_points=1000)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/was/papers/current/modabvar/<ipython console> in <module>()\n\n/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)\n   3380             del kwds['show']\n   3381         if hasattr(funcs, 'plot'):\n-> 3382             G = funcs.plot(*args, **kwds)\n   3383         # if we are using the generic plotting method\n   3384         else:\n\n/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)\n    913         else:\n    914             f = self.function(param)\n--> 915         return plot(f, *args, **kwds)\n    916 \n    917     def __lt__(self, right):\n\n/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)\n   3380             del kwds['show']\n   3381         if hasattr(funcs, 'plot'):\n-> 3382             G = funcs.plot(*args, **kwds)\n   3383         # if we are using the generic plotting method\n   3384         else:\n\n/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)\n    913         else:\n    914             f = self.function(param)\n--> 915         return plot(f, *args, **kwds)\n    916 \n    917     def __lt__(self, right):\n\n/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)\n   3395                 xmax = args[1]\n   3396                 args = args[2:]\n-> 3397                 G = self._call(funcs, (xmin, xmax), *args, **kwds)\n   3398             else:\n   3399                 print \"there were %s extra arguments (besides %s)\" % (n, funcs)\n\n/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xrange, parametric, polar, label, **kwds)\n   3463                 exceptions += 1\n   3464                 exception_indices.append(i)\n-> 3465         data = [data[i] for i in xrange(len(data)) if i not in exception_indices]\n   3466             \n   3467         # adaptive refinement\n\n<type 'exceptions.TypeError'>: 'tuple' object is not callable\n\n```\n",
    "created_at": "2008-03-15T09:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17170",
    "user": "was"
}
```

I applied your patch and it doesn't work.  The example above failes with `<type 'exceptions.TypeError'>: 'tuple' object is not callable`:


```

sage:  plot(-x*log(x),0,1, plot_points=1000)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/papers/current/modabvar/<ipython console> in <module>()

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3380             del kwds['show']
   3381         if hasattr(funcs, 'plot'):
-> 3382             G = funcs.plot(*args, **kwds)
   3383         # if we are using the generic plotting method
   3384         else:

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)
    913         else:
    914             f = self.function(param)
--> 915         return plot(f, *args, **kwds)
    916 
    917     def __lt__(self, right):

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3380             del kwds['show']
   3381         if hasattr(funcs, 'plot'):
-> 3382             G = funcs.plot(*args, **kwds)
   3383         # if we are using the generic plotting method
   3384         else:

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)
    913         else:
    914             f = self.function(param)
--> 915         return plot(f, *args, **kwds)
    916 
    917     def __lt__(self, right):

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3395                 xmax = args[1]
   3396                 args = args[2:]
-> 3397                 G = self._call(funcs, (xmin, xmax), *args, **kwds)
   3398             else:
   3399                 print "there were %s extra arguments (besides %s)" % (n, funcs)

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xrange, parametric, polar, label, **kwds)
   3463                 exceptions += 1
   3464                 exception_indices.append(i)
-> 3465         data = [data[i] for i in xrange(len(data)) if i not in exception_indices]
   3466             
   3467         # adaptive refinement

<type 'exceptions.TypeError'>: 'tuple' object is not callable

```




---

archive/issue_comments_017171.json:
```json
{
    "body": "Apply the second patch instead of the first.\n\nSecond patch is rebased against 2.10.4 and works correctly.",
    "created_at": "2008-03-18T21:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17171",
    "user": "jason"
}
```

Apply the second patch instead of the first.

Second patch is rebased against 2.10.4 and works correctly.



---

archive/issue_comments_017172.json:
```json
{
    "body": "Attachment [plot_undefined.2.patch](tarball://root/attachments/some-uuid/ticket2517/plot_undefined.2.patch) by jason created at 2008-03-18 21:52:00",
    "created_at": "2008-03-18T21:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17172",
    "user": "jason"
}
```

Attachment [plot_undefined.2.patch](tarball://root/attachments/some-uuid/ticket2517/plot_undefined.2.patch) by jason created at 2008-03-18 21:52:00



---

archive/issue_comments_017173.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-18T23:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17173",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_017174.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T00:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17174",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017175.json:
```json
{
    "body": "Merged plot_undefined.2.patch in Sage 2.11.alpha0",
    "created_at": "2008-03-19T00:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2517#issuecomment-17175",
    "user": "mabshoff"
}
```

Merged plot_undefined.2.patch in Sage 2.11.alpha0
