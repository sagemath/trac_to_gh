# Issue 5514: implement exclusions for parametric 3d plots

archive/issues_005514.json:
```json
{
    "body": "Assignee: wcauchois\n\nCC:  @jasongrout @rbeezer\n\nThis feature would emulate Mathematica's [RegionFunction](http://reference.wolfram.com/mathematica/ref/RegionFunction.html). The user should be able to provide a function to parametric_plot3d which, given a (u,v) coordinate, would return whether to include that point in the overall plot. In this way, the user can specify which region to include in the plot drawn.\n\nThe syntax would look something like this:\n\n```\nvar('u,v')\nparametric_plot3d([u,v,u^2+v^2], (-2, 2), (-2, 2), region_function=lambda u,v: u^2+v^2>1)\n```\n\nThis would draw a paraboloid with a circle cut out of the middle.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5514\n\n",
    "created_at": "2009-03-13T23:23:11Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "implement exclusions for parametric 3d plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5514",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```
Assignee: wcauchois

CC:  @jasongrout @rbeezer

This feature would emulate Mathematica's [RegionFunction](http://reference.wolfram.com/mathematica/ref/RegionFunction.html). The user should be able to provide a function to parametric_plot3d which, given a (u,v) coordinate, would return whether to include that point in the overall plot. In this way, the user can specify which region to include in the plot drawn.

The syntax would look something like this:

```
var('u,v')
parametric_plot3d([u,v,u^2+v^2], (-2, 2), (-2, 2), region_function=lambda u,v: u^2+v^2>1)
```

This would draw a paraboloid with a circle cut out of the middle.

Issue created by migration from https://trac.sagemath.org/ticket/5514





---

archive/issue_comments_042770.json:
```json
{
    "body": "Cool!  Also, it'd be cool to have this eventually work on plot3d and other plotting commands (even 2d plotting commands).",
    "created_at": "2009-03-14T09:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42770",
    "user": "https://github.com/jasongrout"
}
```

Cool!  Also, it'd be cool to have this eventually work on plot3d and other plotting commands (even 2d plotting commands).



---

archive/issue_comments_042771.json:
```json
{
    "body": "I will not be able to work on this until after March 30th.",
    "created_at": "2009-03-20T19:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42771",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

I will not be able to work on this until after March 30th.



---

archive/issue_comments_042772.json:
```json
{
    "body": "Attachment [trac5514.patch](tarball://root/attachments/some-uuid/ticket5514/trac5514.patch) by wcauchois created at 2009-04-03 00:38:49",
    "created_at": "2009-04-03T00:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42772",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac5514.patch](tarball://root/attachments/some-uuid/ticket5514/trac5514.patch) by wcauchois created at 2009-04-03 00:38:49



---

archive/issue_comments_042773.json:
```json
{
    "body": "Here's an implementation of region_function that simply removes all faces which do not satisfy the predicate. It looks pretty bad unless you use a high plot resolution, but it works!\n\nYesterday William brought to light some issues that made me realize the task of creating a better looking region_function is frought with some subtlety. Since region_function can be any Python callable, we cannot make any assumptions -- it could, for example, return a random boolean. However, I would like to implement some kind of heuristic that at least smooths the edges around the excluded region. In any case, we are not really responsible for the accuracy of the region beyond the plotting resolution.\n\nCheers,\nBill",
    "created_at": "2009-04-03T00:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42773",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Here's an implementation of region_function that simply removes all faces which do not satisfy the predicate. It looks pretty bad unless you use a high plot resolution, but it works!

Yesterday William brought to light some issues that made me realize the task of creating a better looking region_function is frought with some subtlety. Since region_function can be any Python callable, we cannot make any assumptions -- it could, for example, return a random boolean. However, I would like to implement some kind of heuristic that at least smooths the edges around the excluded region. In any case, we are not really responsible for the accuracy of the region beyond the plotting resolution.

Cheers,
Bill



---

archive/issue_comments_042774.json:
```json
{
    "body": "Attachment [trac-5514-region-function.patch](tarball://root/attachments/some-uuid/ticket5514/trac-5514-region-function.patch) by @jasongrout created at 2009-04-22 19:36:55\n\napply instead of previous patch.",
    "created_at": "2009-04-22T19:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42774",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5514-region-function.patch](tarball://root/attachments/some-uuid/ticket5514/trac-5514-region-function.patch) by @jasongrout created at 2009-04-22 19:36:55

apply instead of previous patch.



---

archive/issue_comments_042775.json:
```json
{
    "body": "You're right that it is really choppy.  I had a go at it: apply trac-5514-region-function.patch instead of the first patch.\n\nThis implements region_function for indexed face sets, as well as a specialized version for parametric surfaces.  The nice thing about making it available for indexed face sets is that *any* surface can use it now, and it will be easier after some more glue code is written.\n\nTo encourage reviews, here is what is possible (and it looks a lot smoother now; I don't just delete faces, I just delete bad vertices and redefine faces):\n\n\n```\n    We use a region function to plot a figure with a circular region (in u,v coordinates) excluded\n    from its center::\n\n        sage: u, v = var('u, v')\n        sage: parametric_plot3d([u, v*u, u^2 + v^2], (u, -2, 2), (v, -2, 2), region_function=lambda u,v: u^2+v^2>3, plot_points=(150,150)) \n\n    Plot part of a sphere (using spherical coordinates):\n        sage: theta, phi = var('theta, phi')\n        sage: p=parametric_plot3d([cos(theta)*sin(phi), sin(theta)*sin(phi), cos(phi)], (theta, 0, 2*pi), (phi, 0, pi), region_function=lambda theta, phi: phi<math.pi/2, plot_points=(100,100))\n        sage: show(p)\n        sage: p.clip_region(lambda theta,phi: theta<math.pi/2)\n        sage: show(p)\n        sage: p.clip_region(lambda x,y,z: z<0.5)\n        sage: show(p)\n\n    A region of a function::\n        sage: var('x,y')\n        (x,y)\n        sage: plot3d(sin(x)*cos(y),(x,-3,3),(y,-3,3), region_function=lambda x,y: x<y^2, plot_points=(100,100))     \n        sage: plot3d(sin(x)*cos(y),(x,-3,3),(y,-3,3), region_function=lambda x,y,z: z<0 and not x>y, plot_points=(100,100))\n        sage: plot3d(sin(x)*cos(y),(x,-3,3),(y,-3,3), region_function=lambda x,y: x^2+y^2<1 or x^2+y^2>4 , plot_points=(100,100))\n        sage: plot3d(sin(x)*cos(y),(x,-3,3),(y,-3,3), region_function=lambda x,y: x^2+y^2>1 and x^2+y^2<4 , plot_points=(100,100))\n        \n    A region of the xy plane::\n        sage: var('x,y')\n        sage: plot3d(1, (x,-3,3), (y,-3,3), region_function=lambda x,y: x^2+y^2<7 and x<y, plot_points=(100,100))\n        sage: plot3d(1, (x,-3,3), (y,-3,3), region_function=lambda x,y: x^2+y^2<7 and x<y, adaptive=True, initial_depth=7)\n\n```\n\n\nAlso, with some glue code written, this should be possible\n\n```\na=sphere()\na.clip_region(lambda x,y,z:z<0)\nshow(a)\n```\n\n\n\nTHIS PATCH IS NOT READY YET.\n\nHere are some things that still need to be done:\n\n* Several functions need doctests (like the indexed face set clip_region)\n* I had to comment out _clean_point_list() in line ~300 of parametric_surface.pyx because it destroyed the relationship between the vertices and the u,v coordinates that generated the vertex.  We really ought to maintain that information separately for a parametric surface, and then update it.  Once we have a way of retrieving that information (i.e, for a vertex, give me the u and v that generated the vertex), we can enable _clean_point_list().  This should probably be done before this patch is merged.",
    "created_at": "2009-04-22T19:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42775",
    "user": "https://github.com/jasongrout"
}
```

You're right that it is really choppy.  I had a go at it: apply trac-5514-region-function.patch instead of the first patch.

This implements region_function for indexed face sets, as well as a specialized version for parametric surfaces.  The nice thing about making it available for indexed face sets is that *any* surface can use it now, and it will be easier after some more glue code is written.

To encourage reviews, here is what is possible (and it looks a lot smoother now; I don't just delete faces, I just delete bad vertices and redefine faces):


```
    We use a region function to plot a figure with a circular region (in u,v coordinates) excluded
    from its center::

        sage: u, v = var('u, v')
        sage: parametric_plot3d([u, v*u, u^2 + v^2], (u, -2, 2), (v, -2, 2), region_function=lambda u,v: u^2+v^2>3, plot_points=(150,150)) 

    Plot part of a sphere (using spherical coordinates):
        sage: theta, phi = var('theta, phi')
        sage: p=parametric_plot3d([cos(theta)*sin(phi), sin(theta)*sin(phi), cos(phi)], (theta, 0, 2*pi), (phi, 0, pi), region_function=lambda theta, phi: phi<math.pi/2, plot_points=(100,100))
        sage: show(p)
        sage: p.clip_region(lambda theta,phi: theta<math.pi/2)
        sage: show(p)
        sage: p.clip_region(lambda x,y,z: z<0.5)
        sage: show(p)

    A region of a function::
        sage: var('x,y')
        (x,y)
        sage: plot3d(sin(x)*cos(y),(x,-3,3),(y,-3,3), region_function=lambda x,y: x<y^2, plot_points=(100,100))     
        sage: plot3d(sin(x)*cos(y),(x,-3,3),(y,-3,3), region_function=lambda x,y,z: z<0 and not x>y, plot_points=(100,100))
        sage: plot3d(sin(x)*cos(y),(x,-3,3),(y,-3,3), region_function=lambda x,y: x^2+y^2<1 or x^2+y^2>4 , plot_points=(100,100))
        sage: plot3d(sin(x)*cos(y),(x,-3,3),(y,-3,3), region_function=lambda x,y: x^2+y^2>1 and x^2+y^2<4 , plot_points=(100,100))
        
    A region of the xy plane::
        sage: var('x,y')
        sage: plot3d(1, (x,-3,3), (y,-3,3), region_function=lambda x,y: x^2+y^2<7 and x<y, plot_points=(100,100))
        sage: plot3d(1, (x,-3,3), (y,-3,3), region_function=lambda x,y: x^2+y^2<7 and x<y, adaptive=True, initial_depth=7)

```


Also, with some glue code written, this should be possible

```
a=sphere()
a.clip_region(lambda x,y,z:z<0)
show(a)
```



THIS PATCH IS NOT READY YET.

Here are some things that still need to be done:

* Several functions need doctests (like the indexed face set clip_region)
* I had to comment out _clean_point_list() in line ~300 of parametric_surface.pyx because it destroyed the relationship between the vertices and the u,v coordinates that generated the vertex.  We really ought to maintain that information separately for a parametric surface, and then update it.  Once we have a way of retrieving that information (i.e, for a vertex, give me the u and v that generated the vertex), we can enable _clean_point_list().  This should probably be done before this patch is merged.



---

archive/issue_comments_042776.json:
```json
{
    "body": "Maybe this function should be called just \"clip\" instead of \"clip_region\"?",
    "created_at": "2009-04-22T19:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42776",
    "user": "https://github.com/jasongrout"
}
```

Maybe this function should be called just "clip" instead of "clip_region"?



---

archive/issue_comments_042777.json:
```json
{
    "body": "I can't work on this anymore right now.  wcauchois, feel free to do the remaining bits if you want.  You'll probably beat me to it.",
    "created_at": "2009-04-22T19:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42777",
    "user": "https://github.com/jasongrout"
}
```

I can't work on this anymore right now.  wcauchois, feel free to do the remaining bits if you want.  You'll probably beat me to it.



---

archive/issue_comments_042778.json:
```json
{
    "body": "Great work, Jason! There's still alot of work to do to make the excluded regions smooth, but we can address that in another patch. I can definitely work on this.\n\nAbout _clean_point_list(): We don't _have_ to deallocate unused vertices. I took a look at some parametric plots, and in most cases the number of vertices deleted in _clean_point_list() was under 100. The overhead for a list mapping vertex indices to their (u, v) coordinates would be much greater than the memory saved by _clean_point_list(). Does that sound reasonable to you? Of course, there may be other reasons for maintaining such a list or ensuring that all the vertices in the IFS are used...",
    "created_at": "2009-04-22T23:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42778",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Great work, Jason! There's still alot of work to do to make the excluded regions smooth, but we can address that in another patch. I can definitely work on this.

About _clean_point_list(): We don't _have_ to deallocate unused vertices. I took a look at some parametric plots, and in most cases the number of vertices deleted in _clean_point_list() was under 100. The overhead for a list mapping vertex indices to their (u, v) coordinates would be much greater than the memory saved by _clean_point_list(). Does that sound reasonable to you? Of course, there may be other reasons for maintaining such a list or ensuring that all the vertices in the IFS are used...



---

archive/issue_comments_042779.json:
```json
{
    "body": "Bill,\n\nYou might ask Robert Bradshaw about the clean_point_list function; I think he was the original author, and might have some insight.  Also, when making things better (i.e., smoother boundaries), we'll probably subdivide regions, which means that we'll evaluate more u,v coordinates to get more vertices.  Those vertices could mess up a nice numbering grid that exists now, so it might be nice to just store the u,v coordinates of each vertex anyway.  Of course, we could just cross that bridge when it comes, too.",
    "created_at": "2009-04-23T02:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42779",
    "user": "https://github.com/jasongrout"
}
```

Bill,

You might ask Robert Bradshaw about the clean_point_list function; I think he was the original author, and might have some insight.  Also, when making things better (i.e., smoother boundaries), we'll probably subdivide regions, which means that we'll evaluate more u,v coordinates to get more vertices.  Those vertices could mess up a nice numbering grid that exists now, so it might be nice to just store the u,v coordinates of each vertex anyway.  Of course, we could just cross that bridge when it comes, too.



---

archive/issue_comments_042780.json:
```json
{
    "body": "Great progress on this, Bill and Jason!  I had a go with a few of the commands in the doctests and a couple of my own.  Two thoughts.\n\n1.  The JMOL bounding box may be computed pre-clip?  Compare\n\n`plot3d(6-2*x<sup>2-5*y</sup>2, (x, -10, 10), (y, -10, 10), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n\nwith\n\n`plot3d(6-2*x<sup>2-5*y</sup>2, (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n\nThe former would seem to use the unseen faces near inputs like (-10,10) to compute the vertical axis and the plot is then a really, really insignificant portion of the bounding box.\n\n2.  I thought maybe something like\n\n`plot3d(sqrt(6-2*x<sup>2-5*y</sup>2), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n\nwould now be possible, but it appears the clip comes after the evaluations, thus this raises an error for the negatives in the square root.  So maybe this should be handled with some sort of piecewise definition for the function and then the excess would be clipped by a `region_function` before showing it.\n\nOK, thinking while I write - here's a hack - insert an absolute value, then trim:\n\n`plot3d(sqrt(abs(6-2*x<sup>2-5*y</sup>2)), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n\nNicely done.  Holler if I can provide more testing as you finish this up.\n\nRob",
    "created_at": "2009-04-24T05:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42780",
    "user": "https://github.com/rbeezer"
}
```

Great progress on this, Bill and Jason!  I had a go with a few of the commands in the doctests and a couple of my own.  Two thoughts.

1.  The JMOL bounding box may be computed pre-clip?  Compare

`plot3d(6-2*x<sup>2-5*y</sup>2, (x, -10, 10), (y, -10, 10), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`

with

`plot3d(6-2*x<sup>2-5*y</sup>2, (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`

The former would seem to use the unseen faces near inputs like (-10,10) to compute the vertical axis and the plot is then a really, really insignificant portion of the bounding box.

2.  I thought maybe something like

`plot3d(sqrt(6-2*x<sup>2-5*y</sup>2), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`

would now be possible, but it appears the clip comes after the evaluations, thus this raises an error for the negatives in the square root.  So maybe this should be handled with some sort of piecewise definition for the function and then the excess would be clipped by a `region_function` before showing it.

OK, thinking while I write - here's a hack - insert an absolute value, then trim:

`plot3d(sqrt(abs(6-2*x<sup>2-5*y</sup>2)), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`

Nicely done.  Holler if I can provide more testing as you finish this up.

Rob



---

archive/issue_comments_042781.json:
```json
{
    "body": "Replying to [comment:12 rbeezer]:\n> Great progress on this, Bill and Jason!  I had a go with a few of the commands in the doctests and a couple of my own.  Two thoughts.\n\nThanks for looking at this!\n\n> 1.  The JMOL bounding box may be computed pre-clip?  Compare\n\n> `plot3d(6-2*x<sup>2-5*y</sup>2, (x, -10, 10), (y, -10, 10), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n\n> with\n\n> `plot3d(6-2*x<sup>2-5*y</sup>2, (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n> \n> The former would seem to use the unseen faces near inputs like (-10,10) to compute the vertical axis and the plot is then a really, really insignificant portion of the bounding box.\n\nIndexFaceSet computes the bounding box by finding the min/max of its vertices. The problem you describe appears to occur because we don't remove all of the unused vertices. The issue is somewhat subtle since if we remove a face, that does not necessarily mean the vertices that it references are not in use by another face. One way to solve this problem would be to maintain an array of reference counts for every vertex while we are clipping the region. At the end of the method, we could delete vertices with a reference count of 0. This seems like overkill though -- perhaps we can use assumptions about the structure of the parametric surface (a rectangular grid).\n\n> 2.  I thought maybe something like\n\n> `plot3d(sqrt(6-2*x<sup>2-5*y</sup>2), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n\n> would now be possible, but it appears the clip comes after the evaluations, thus this raises an error for the negatives in the square root.  So maybe this should be handled with some sort of piecewise definition for the function and then the excess would be clipped by a `region_function` before showing it.\n> \n> OK, thinking while I write - here's a hack - insert an absolute value, then trim:\n\n> `plot3d(sqrt(abs(6-2*x<sup>2-5*y</sup>2)), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n\nThat's because the clipping is done after the function is evaluated at every (u,v) coordinate. Maybe we should modify eval_grid so that it does not perform this unecessary (and sometimes troublesome) computation.\n\n> Nicely done.  Holler if I can provide more testing as you finish this up.\n> \n> Rob\n\nI'm uploading a patch that makes some cosmetic changes, including renaming \"clip_region\" to \"clip\" and \"region_function\" to \"region\" (following the convention adopted in implicit_plot3d). I'm hoping to get some work done on this ticket this week!",
    "created_at": "2009-05-11T22:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42781",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:12 rbeezer]:
> Great progress on this, Bill and Jason!  I had a go with a few of the commands in the doctests and a couple of my own.  Two thoughts.

Thanks for looking at this!

> 1.  The JMOL bounding box may be computed pre-clip?  Compare

> `plot3d(6-2*x<sup>2-5*y</sup>2, (x, -10, 10), (y, -10, 10), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`

> with

> `plot3d(6-2*x<sup>2-5*y</sup>2, (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`
> 
> The former would seem to use the unseen faces near inputs like (-10,10) to compute the vertical axis and the plot is then a really, really insignificant portion of the bounding box.

IndexFaceSet computes the bounding box by finding the min/max of its vertices. The problem you describe appears to occur because we don't remove all of the unused vertices. The issue is somewhat subtle since if we remove a face, that does not necessarily mean the vertices that it references are not in use by another face. One way to solve this problem would be to maintain an array of reference counts for every vertex while we are clipping the region. At the end of the method, we could delete vertices with a reference count of 0. This seems like overkill though -- perhaps we can use assumptions about the structure of the parametric surface (a rectangular grid).

> 2.  I thought maybe something like

> `plot3d(sqrt(6-2*x<sup>2-5*y</sup>2), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`

> would now be possible, but it appears the clip comes after the evaluations, thus this raises an error for the negatives in the square root.  So maybe this should be handled with some sort of piecewise definition for the function and then the excess would be clipped by a `region_function` before showing it.
> 
> OK, thinking while I write - here's a hack - insert an absolute value, then trim:

> `plot3d(sqrt(abs(6-2*x<sup>2-5*y</sup>2)), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`

That's because the clipping is done after the function is evaluated at every (u,v) coordinate. Maybe we should modify eval_grid so that it does not perform this unecessary (and sometimes troublesome) computation.

> Nicely done.  Holler if I can provide more testing as you finish this up.
> 
> Rob

I'm uploading a patch that makes some cosmetic changes, including renaming "clip_region" to "clip" and "region_function" to "region" (following the convention adopted in implicit_plot3d). I'm hoping to get some work done on this ticket this week!



---

archive/issue_comments_042782.json:
```json
{
    "body": "Attachment [trac-5514-cosmetic-changes.patch](tarball://root/attachments/some-uuid/ticket5514/trac-5514-cosmetic-changes.patch) by wcauchois created at 2009-05-11 22:22:28",
    "created_at": "2009-05-11T22:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42782",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac-5514-cosmetic-changes.patch](tarball://root/attachments/some-uuid/ticket5514/trac-5514-cosmetic-changes.patch) by wcauchois created at 2009-05-11 22:22:28



---

archive/issue_comments_042783.json:
```json
{
    "body": "Replying to [comment:13 wcauchois]:\n> \n> IndexFaceSet computes the bounding box by finding the min/max of its vertices. The problem you describe appears to occur because we don't remove all of the unused vertices. The issue is somewhat subtle since if we remove a face, that does not necessarily mean the vertices that it references are not in use by another face. One way to solve this problem would be to maintain an array of reference counts for every vertex while we are clipping the region. At the end of the method, we could delete vertices with a reference count of 0. This seems like overkill though -- perhaps we can use assumptions about the structure of the parametric surface (a rectangular grid).\n\n\nI believe the `_clean_point_list` function clears out unused points (implementing the functionality that Bill describes above).  However, we don't call this (i.e., we commented out the existing call to this) so that we can still get an easy correspondence between the parameter values and the points generated (i.e., the points are still in a grid of parameter values, as long as none are missing).  \n\n* We could bolt one more thing on---a bitset of the points that are used.  We could use the bitset class in misc/bitset.pxi for that.  \n* Or we could just store the parameter values with each point.  This would also make us more flexible in handling the situation below.\n\nWe need this correspondence between vertices and parameter values so that we can clip based on the parameter values.\n\n> \n> > 2.  I thought maybe something like\n\n> > `plot3d(sqrt(6-2*x<sup>2-5*y</sup>2), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n\n> > would now be possible, but it appears the clip comes after the evaluations, thus this raises an error for the negatives in the square root.  So maybe this should be handled with some sort of piecewise definition for the function and then the excess would be clipped by a `region_function` before showing it.\n> > \n> > OK, thinking while I write - here's a hack - insert an absolute value, then trim:\n\n> > `plot3d(sqrt(abs(6-2*x<sup>2-5*y</sup>2)), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`\n> \n> That's because the clipping is done after the function is evaluated at every (u,v) coordinate. Maybe we should modify eval_grid so that it does not perform this unecessary (and sometimes troublesome) computation.\n\nSo, we could:\n\n* make it so that the region passed into the plot3d command is used during the initial evaluation; if the point passes the region function, then a vertex is calculated from it.  This would probably save time anyway.  If we do this, we need to take into account the different signatures of region functions.  For a two-argument function, check before the vertex is calculated, and for a three- or five-argument region function, check after the vertex is calculated (because the arguments to the region function include the vertex coordinates).  Because of this last possibility, we probably also want to also\n* make the indexed face sets handle evaluations which throw errors, in a similar way that 2d plotting handles undefined values.  This would also probably necessitate storing the parameter values with the vertices.\n\nEither way, we violate the assumption that the vertices are from a grid of parameter values.  We probably will have to store the parameter values that generate each vertex.",
    "created_at": "2009-05-12T12:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42783",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:13 wcauchois]:
> 
> IndexFaceSet computes the bounding box by finding the min/max of its vertices. The problem you describe appears to occur because we don't remove all of the unused vertices. The issue is somewhat subtle since if we remove a face, that does not necessarily mean the vertices that it references are not in use by another face. One way to solve this problem would be to maintain an array of reference counts for every vertex while we are clipping the region. At the end of the method, we could delete vertices with a reference count of 0. This seems like overkill though -- perhaps we can use assumptions about the structure of the parametric surface (a rectangular grid).


I believe the `_clean_point_list` function clears out unused points (implementing the functionality that Bill describes above).  However, we don't call this (i.e., we commented out the existing call to this) so that we can still get an easy correspondence between the parameter values and the points generated (i.e., the points are still in a grid of parameter values, as long as none are missing).  

* We could bolt one more thing on---a bitset of the points that are used.  We could use the bitset class in misc/bitset.pxi for that.  
* Or we could just store the parameter values with each point.  This would also make us more flexible in handling the situation below.

We need this correspondence between vertices and parameter values so that we can clip based on the parameter values.

> 
> > 2.  I thought maybe something like

> > `plot3d(sqrt(6-2*x<sup>2-5*y</sup>2), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`

> > would now be possible, but it appears the clip comes after the evaluations, thus this raises an error for the negatives in the square root.  So maybe this should be handled with some sort of piecewise definition for the function and then the excess would be clipped by a `region_function` before showing it.
> > 
> > OK, thinking while I write - here's a hack - insert an absolute value, then trim:

> > `plot3d(sqrt(abs(6-2*x<sup>2-5*y</sup>2)), (x, -sqrt(3), sqrt(3)), (y, -1, 1), region_function=lambda x,y: 6-2*x<sup>2-6*y</sup>2>0)`
> 
> That's because the clipping is done after the function is evaluated at every (u,v) coordinate. Maybe we should modify eval_grid so that it does not perform this unecessary (and sometimes troublesome) computation.

So, we could:

* make it so that the region passed into the plot3d command is used during the initial evaluation; if the point passes the region function, then a vertex is calculated from it.  This would probably save time anyway.  If we do this, we need to take into account the different signatures of region functions.  For a two-argument function, check before the vertex is calculated, and for a three- or five-argument region function, check after the vertex is calculated (because the arguments to the region function include the vertex coordinates).  Because of this last possibility, we probably also want to also
* make the indexed face sets handle evaluations which throw errors, in a similar way that 2d plotting handles undefined values.  This would also probably necessitate storing the parameter values with the vertices.

Either way, we violate the assumption that the vertices are from a grid of parameter values.  We probably will have to store the parameter values that generate each vertex.



---

archive/issue_comments_042784.json:
```json
{
    "body": "Replying to [comment:14 jason]:\n\nI had overlooked `_clean_point_list`; the solution was right there under my nose :). I agree that keeping track of the (u,v) coordinates for every vertex will be necessary.\n\n> make it so that the region passed into the plot3d command is used during the initial evaluation; if the point passes the region function, then a vertex is calculated from it. This would probably save time anyway. If we do this, we need to take into account the different signatures of region functions. For a two-argument function, check before the vertex is calculated, and for a three- or five-argument region function, check after the vertex is calculated (because the arguments to the region function include the vertex coordinates). Because of this last possibility, we probably also want to also make the indexed face sets handle evaluations which throw errors, in a similar way that 2d plotting handles undefined values. This would also probably necessitate storing the parameter values with the vertices.\n\nOne concern I have about implementing this is, have you seen ParametricSurface.eval_grid? There's a lot of duplicated code, since it branches for every type of function and then replicates the nested loop. I feel like I would have to implement this logic in several places. Do you have any ideas for how to factor eval_grid? Or any general suggestions?",
    "created_at": "2009-05-14T03:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42784",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:14 jason]:

I had overlooked `_clean_point_list`; the solution was right there under my nose :). I agree that keeping track of the (u,v) coordinates for every vertex will be necessary.

> make it so that the region passed into the plot3d command is used during the initial evaluation; if the point passes the region function, then a vertex is calculated from it. This would probably save time anyway. If we do this, we need to take into account the different signatures of region functions. For a two-argument function, check before the vertex is calculated, and for a three- or five-argument region function, check after the vertex is calculated (because the arguments to the region function include the vertex coordinates). Because of this last possibility, we probably also want to also make the indexed face sets handle evaluations which throw errors, in a similar way that 2d plotting handles undefined values. This would also probably necessitate storing the parameter values with the vertices.

One concern I have about implementing this is, have you seen ParametricSurface.eval_grid? There's a lot of duplicated code, since it branches for every type of function and then replicates the nested loop. I feel like I would have to implement this logic in several places. Do you have any ideas for how to factor eval_grid? Or any general suggestions?



---

archive/issue_comments_042785.json:
```json
{
    "body": "Attachment [trac5514-new.patch](tarball://root/attachments/some-uuid/ticket5514/trac5514-new.patch) by wcauchois created at 2009-05-28 08:43:09\n\nbased on sage 4.0.rc0",
    "created_at": "2009-05-28T08:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42785",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac5514-new.patch](tarball://root/attachments/some-uuid/ticket5514/trac5514-new.patch) by wcauchois created at 2009-05-28 08:43:09

based on sage 4.0.rc0



---

archive/issue_comments_042786.json:
```json
{
    "body": "I've done some work on this issue, including implementing code to store the uv coordinates for every vertex in a separate array, and it SEEMS to work. Everything is in trac5514-new.patch, which I've rebased for Sage 4.0.rc0. HOWEVER, I was just looking through the IndexFaceSet code and I realized that _separate_creases() and _clean_point_list() both rejigger the list of vertices. I added an array to ParametricSurface called _coords, where self._coords[i] is supposed to store the uv coordinates for the vertex self.vs[i]. But after an operation like the two I just mentioned, self.vs[i] could have moved to a completely different index. I don't understand exactly what _separate_creases() does, but it looks like it could even add NEW vertices to the IndexFaceSet. How would we clip these new vertices based on uv coordinates?\n\nMaybe there is some way to get around these issues, but I think we could eliminate this problem by removing the specialized version of clip() in ParametricSurface. So if you call clip() on a ParametricSurface object, you will only be able to use the xy and xyz variants of the region function. You would still be able to use the uv or xyzuv variants by passing the region function to the constructor of ParametricSurface, since in that case we could do all the clipping inside triangulate(), before _clean_point_list() and _separate_creases() are potentially called (by our code, or by client code, or by the viewing code). I should hope that in the vast majority of use cases this will be acceptable.",
    "created_at": "2009-05-28T08:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5514#issuecomment-42786",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

I've done some work on this issue, including implementing code to store the uv coordinates for every vertex in a separate array, and it SEEMS to work. Everything is in trac5514-new.patch, which I've rebased for Sage 4.0.rc0. HOWEVER, I was just looking through the IndexFaceSet code and I realized that _separate_creases() and _clean_point_list() both rejigger the list of vertices. I added an array to ParametricSurface called _coords, where self._coords[i] is supposed to store the uv coordinates for the vertex self.vs[i]. But after an operation like the two I just mentioned, self.vs[i] could have moved to a completely different index. I don't understand exactly what _separate_creases() does, but it looks like it could even add NEW vertices to the IndexFaceSet. How would we clip these new vertices based on uv coordinates?

Maybe there is some way to get around these issues, but I think we could eliminate this problem by removing the specialized version of clip() in ParametricSurface. So if you call clip() on a ParametricSurface object, you will only be able to use the xy and xyz variants of the region function. You would still be able to use the uv or xyzuv variants by passing the region function to the constructor of ParametricSurface, since in that case we could do all the clipping inside triangulate(), before _clean_point_list() and _separate_creases() are potentially called (by our code, or by client code, or by the viewing code). I should hope that in the vast majority of use cases this will be acceptable.
