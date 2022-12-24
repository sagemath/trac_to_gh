# Issue 4818: bug in list_plot3d -- invalid index?

archive/issues_004818.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: v = list_plot3d([(1,2,3)]).show(viewer=\"tachyon\")\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/home/wstein/<ipython console> in <module>()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d(v, interpolation_type, texture, point_list, **kwds)\n    124             return Graphics3d()\n    125         elif isinstance(v[0],tuple) or point_list==True and len(v[0]) == 3:\n--> 126             return list_plot3d_tuples(v,interpolation_type,texture=texture, **kwds)\n    127         else:\n    128             return list_plot3d_array_of_arrays(v, interpolation_type,texture, **kwds)\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d_tuples(v, interpolation_type, texture, **kwds)\n    222     if interpolation_type == 'nn'  or interpolation_type =='default':\n    223 \n--> 224         T=delaunay.Triangulation(x,y)\n    225         f=T.nn_interpolator(z)\n    226         f.default_value=0.0\n\n/home/wstein/sage/local/lib/python2.5/site-packages/delaunay/triangulate.pyc in __init__(self, x, y)\n     66             self.triangle_neighbors = delaunay(self.x, self.y)\n     67 \n---> 68         self.hull = self._compute_convex_hull()\n     69 \n     70     def _compute_convex_hull(self):\n\n/home/wstein/sage/local/lib/python2.5/site-packages/delaunay/triangulate.pyc in _compute_convex_hull(self)\n     77 \n     78         edges = {}\n---> 79         edges.update(dict(zip(self.triangle_nodes[border[:,0]][:,1],\n     80                               self.triangle_nodes[border[:,0]][:,2])))\n     81         edges.update(dict(zip(self.triangle_nodes[border[:,1]][:,2],\n\nIndexError: invalid index\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4818\n\n",
    "created_at": "2008-12-17T06:54:47Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "bug in list_plot3d -- invalid index?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4818",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: v = list_plot3d([(1,2,3)]).show(viewer="tachyon")
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/wstein/<ipython console> in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d(v, interpolation_type, texture, point_list, **kwds)
    124             return Graphics3d()
    125         elif isinstance(v[0],tuple) or point_list==True and len(v[0]) == 3:
--> 126             return list_plot3d_tuples(v,interpolation_type,texture=texture, **kwds)
    127         else:
    128             return list_plot3d_array_of_arrays(v, interpolation_type,texture, **kwds)

/home/wstein/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d_tuples(v, interpolation_type, texture, **kwds)
    222     if interpolation_type == 'nn'  or interpolation_type =='default':
    223 
--> 224         T=delaunay.Triangulation(x,y)
    225         f=T.nn_interpolator(z)
    226         f.default_value=0.0

/home/wstein/sage/local/lib/python2.5/site-packages/delaunay/triangulate.pyc in __init__(self, x, y)
     66             self.triangle_neighbors = delaunay(self.x, self.y)
     67 
---> 68         self.hull = self._compute_convex_hull()
     69 
     70     def _compute_convex_hull(self):

/home/wstein/sage/local/lib/python2.5/site-packages/delaunay/triangulate.pyc in _compute_convex_hull(self)
     77 
     78         edges = {}
---> 79         edges.update(dict(zip(self.triangle_nodes[border[:,0]][:,1],
     80                               self.triangle_nodes[border[:,0]][:,2])))
     81         edges.update(dict(zip(self.triangle_nodes[border[:,1]][:,2],

IndexError: invalid index

```


Issue created by migration from https://trac.sagemath.org/ticket/4818





---

archive/issue_comments_036534.json:
```json
{
    "body": "The attached patch fixes the reported bug by special casing the case of 1 or 2 input points by plotting a point or a line instead of a surface.  (Note that there are other bugs in list_plot3d that this patch doesn't fix.)",
    "created_at": "2009-01-22T13:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4818#issuecomment-36534",
    "user": "@williamstein"
}
```

The attached patch fixes the reported bug by special casing the case of 1 or 2 input points by plotting a point or a line instead of a surface.  (Note that there are other bugs in list_plot3d that this patch doesn't fix.)



---

archive/issue_comments_036535.json:
```json
{
    "body": "Attachment [trac_4818.patch](tarball://root/attachments/some-uuid/ticket4818/trac_4818.patch) by jkantor created at 2009-01-23 03:33:54\n\nThis does what it is supposed and has very sensible behaviour for the case of one or two points.",
    "created_at": "2009-01-23T03:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4818#issuecomment-36535",
    "user": "jkantor"
}
```

Attachment [trac_4818.patch](tarball://root/attachments/some-uuid/ticket4818/trac_4818.patch) by jkantor created at 2009-01-23 03:33:54

This does what it is supposed and has very sensible behaviour for the case of one or two points.



---

archive/issue_comments_036536.json:
```json
{
    "body": "+1 from me too. I need to get quicker at reviewing these things...",
    "created_at": "2009-01-23T03:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4818#issuecomment-36536",
    "user": "@robertwb"
}
```

+1 from me too. I need to get quicker at reviewing these things...



---

archive/issue_comments_036537.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T09:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4818#issuecomment-36537",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael



---

archive/issue_comments_036538.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4818#issuecomment-36538",
    "user": "mabshoff"
}
```

Resolution: fixed
