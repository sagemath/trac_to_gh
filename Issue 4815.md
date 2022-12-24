# Issue 4815: list_plot3d is broken (segfaults, zero division errors)

archive/issues_004815.json:
```json
{
    "body": "Assignee: was\n\nIn sage-3.2.1 the following segfaults.  Fortunately, in sage-3.2.2.alpha2 it gives only a traceback (as given below):\n\n```\nsage: sage: X = list_plot3d([(1,1,1), (1,2,3), (1,2,5), (1,1,1)])\nsage: sage: X.show(viewer='tachyon')\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n\n/Users/was/build/sage-3.2.2.alpha2/<ipython console> in <module>()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:8436)()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._prepare_for_tachyon (sage/plot/plot3d/base.c:5912)()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._box_for_aspect_ratio (sage/plot/plot3d/base.c:6124)()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._safe_bounding_box (sage/plot/plot3d/base.c:2743)()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.bounding_box (sage/plot/plot3d/parametric_surface.c:2133)()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.triangulate (sage/plot/plot3d/parametric_surface.c:2612)()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.triangulate (sage/plot/plot3d/parametric_surface.c:2551)()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.eval_grid (sage/plot/plot3d/parametric_surface.c:4108)()\n\n/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in g(x, y)\n    210         from parametric_surface import ParametricSurface\n    211         def g(x,y):\n--> 212             i=round( (x-xmin)/(xmax-xmin)*(num_points-1) )\n    213             j=round( (y-ymin)/(ymax-ymin)*(num_points-1) )\n    214             z=vals[int(j),int(i)]\n\nZeroDivisionError: float division\n```\n\n\nlist_plot3d is supposed to work on *any* input, so this is a bug. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4815\n\n",
    "created_at": "2008-12-16T16:37:42Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "list_plot3d is broken (segfaults, zero division errors)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4815",
    "user": "was"
}
```
Assignee: was

In sage-3.2.1 the following segfaults.  Fortunately, in sage-3.2.2.alpha2 it gives only a traceback (as given below):

```
sage: sage: X = list_plot3d([(1,1,1), (1,2,3), (1,2,5), (1,1,1)])
sage: sage: X.show(viewer='tachyon')
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/Users/was/build/sage-3.2.2.alpha2/<ipython console> in <module>()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:8436)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._prepare_for_tachyon (sage/plot/plot3d/base.c:5912)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._box_for_aspect_ratio (sage/plot/plot3d/base.c:6124)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._safe_bounding_box (sage/plot/plot3d/base.c:2743)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.bounding_box (sage/plot/plot3d/parametric_surface.c:2133)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.triangulate (sage/plot/plot3d/parametric_surface.c:2612)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.triangulate (sage/plot/plot3d/parametric_surface.c:2551)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.eval_grid (sage/plot/plot3d/parametric_surface.c:4108)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in g(x, y)
    210         from parametric_surface import ParametricSurface
    211         def g(x,y):
--> 212             i=round( (x-xmin)/(xmax-xmin)*(num_points-1) )
    213             j=round( (y-ymin)/(ymax-ymin)*(num_points-1) )
    214             z=vals[int(j),int(i)]

ZeroDivisionError: float division
```


list_plot3d is supposed to work on *any* input, so this is a bug. 

Issue created by migration from https://trac.sagemath.org/ticket/4815





---

archive/issue_comments_036502.json:
```json
{
    "body": "This is a dup of #4752.",
    "created_at": "2008-12-16T16:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36502",
    "user": "was"
}
```

This is a dup of #4752.



---

archive/issue_comments_036503.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-12-16T16:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36503",
    "user": "was"
}
```

Resolution: duplicate



---

archive/issue_comments_036504.json:
```json
{
    "body": "I am re-opening this, since interestingly it isn't the same bug as is exposed by #4752's example.",
    "created_at": "2008-12-16T16:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36504",
    "user": "was"
}
```

I am re-opening this, since interestingly it isn't the same bug as is exposed by #4752's example.



---

archive/issue_comments_036505.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-12-16T16:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36505",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_036506.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-12-16T16:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36506",
    "user": "was"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_036507.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-15T07:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36507",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_036508.json:
```json
{
    "body": "Ok, this ticket was hiding in the dupe milestone and given it rather grisly nature of segfaulting Sage I am making it a blocker against 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T07:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36508",
    "user": "mabshoff"
}
```

Ok, this ticket was hiding in the dupe milestone and given it rather grisly nature of segfaulting Sage I am making it a blocker against 3.3.

Cheers,

Michael



---

archive/issue_comments_036509.json:
```json
{
    "body": "The patch at #4752 keeps this from segfaulting, etc\n\n\n```\nsage: version()\n'Sage Version 3.3.rc1, Release Date: 2009-02-16'\nsage: sage: sage: X = list_plot3d([(1,1,1), (1,2,3), (1,2,5), (1,1,1)])\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/mhansen/.sage/temp/sage.math.washington.edu/28849/_home_mhansen__sage_init_sage_0.py in <module>()\n\n/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d(v, interpolation_type, texture, point_list, **kwds)\n    189             return line3d(v, **kwds)\n    190         elif isinstance(v[0],tuple) or point_list==True and len(v[0]) == 3:\n--> 191             return list_plot3d_tuples(v,interpolation_type,texture=texture, **kwds)\n    192         else:\n    193             return list_plot3d_array_of_arrays(v, interpolation_type,texture, **kwds)\n\n/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d_tuples(v, interpolation_type, texture, **kwds)\n    248             if x[i]==x[j] and y[i]==y[j]:\n    249                 if z[i]!=z[j]:\n--> 250                     raise ValueError, \"Two points with same x,y coordinates and different z coordinates were given. Interpolation cannot handle this.\"\n    251                 elif z[i]==z[j]:\n    252                     drop_list.append(j)\n\nValueError: Two points with same x,y coordinates and different z coordinates were given. Interpolation cannot handle this.\n```\n",
    "created_at": "2009-02-19T11:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36509",
    "user": "mhansen"
}
```

The patch at #4752 keeps this from segfaulting, etc


```
sage: version()
'Sage Version 3.3.rc1, Release Date: 2009-02-16'
sage: sage: sage: X = list_plot3d([(1,1,1), (1,2,3), (1,2,5), (1,1,1)])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mhansen/.sage/temp/sage.math.washington.edu/28849/_home_mhansen__sage_init_sage_0.py in <module>()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d(v, interpolation_type, texture, point_list, **kwds)
    189             return line3d(v, **kwds)
    190         elif isinstance(v[0],tuple) or point_list==True and len(v[0]) == 3:
--> 191             return list_plot3d_tuples(v,interpolation_type,texture=texture, **kwds)
    192         else:
    193             return list_plot3d_array_of_arrays(v, interpolation_type,texture, **kwds)

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d_tuples(v, interpolation_type, texture, **kwds)
    248             if x[i]==x[j] and y[i]==y[j]:
    249                 if z[i]!=z[j]:
--> 250                     raise ValueError, "Two points with same x,y coordinates and different z coordinates were given. Interpolation cannot handle this."
    251                 elif z[i]==z[j]:
    252                     drop_list.append(j)

ValueError: Two points with same x,y coordinates and different z coordinates were given. Interpolation cannot handle this.
```




---

archive/issue_comments_036510.json:
```json
{
    "body": "Ok, closing as fixed by #4752. Thanks Mike.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T07:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36510",
    "user": "mabshoff"
}
```

Ok, closing as fixed by #4752. Thanks Mike.

Cheers,

Michael



---

archive/issue_comments_036511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T07:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4815#issuecomment-36511",
    "user": "mabshoff"
}
```

Resolution: fixed
