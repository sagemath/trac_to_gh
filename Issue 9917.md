# Issue 9917: triangulate point configurations

archive/issues_009917.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  mhampton @novoselt\n\nThe attached patch implements triangulations of point configurations in arbitrary dimensions in Sage/Cython/C++ without relying on TOPCOM. \n\n```\nsage: points = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]]);\nsage: points\nA point configuration in QQ^2 consisting of 5 points. The \ntriangulations of this point configuration are assumed to \nbe connected, not necessarily fine, not necessarily regular.\nsage: triang = points.triangulate()   # find one triangulation       \nsage: triang\n(<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)\nsage: triang[0]\n(0, 1, 2)\nsage: list( points.triangulations() )\n[(<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>), \n (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>), \n (<1,2,3>, <1,2,4>), \n (<1,3,4>, <2,3,4>)]\nsage: triang.plot(axes=False)                                        \n```\n\nThe internal implementation covers finding a single triangulation as well as enumerating all triangulations connected to it by bistellar flips. TOPCOM is required to test for regularity and/or to find non-connected triangulations.\n\nWhile not quite as fast, my limited testing shows the performance to be in the same order of magnitude as TOPCOM:\n\n```\nsage: U=matrix([\n...      [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],\n...      [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],\n...      [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],\n...      [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],\n...      [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]\n...   ])\nsage: pc = PointConfiguration(U.columns())\nsage: pc.set_engine('internal')\nsage: time len(pc.triangulations_list())\nCPU times: user 23.26 s, sys: 0.02 s, total: 23.29 s\nWall time: 23.32 s\n9623\nsage: pc.set_engine('TOPCOM')\nsage: time len(pc.triangulations_list())\nCPU times: user 7.80 s, sys: 0.13 s, total: 7.93 s\nWall time: 8.37 s\n9623\n```\n\nSee also #8169: include TOPCOM, where an optional spkg is being worked on.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9918\n\n",
    "created_at": "2010-09-16T11:22:09Z",
    "labels": [
        "component: geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "triangulate point configurations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9917",
    "user": "https://github.com/vbraun"
}
```
Assignee: mhampton

CC:  mhampton @novoselt

The attached patch implements triangulations of point configurations in arbitrary dimensions in Sage/Cython/C++ without relying on TOPCOM. 

```
sage: points = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]]);
sage: points
A point configuration in QQ^2 consisting of 5 points. The 
triangulations of this point configuration are assumed to 
be connected, not necessarily fine, not necessarily regular.
sage: triang = points.triangulate()   # find one triangulation       
sage: triang
(<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>)
sage: triang[0]
(0, 1, 2)
sage: list( points.triangulations() )
[(<0,1,2>, <0,1,4>, <0,2,4>, <1,2,3>), 
 (<0,1,3>, <0,1,4>, <0,2,3>, <0,2,4>), 
 (<1,2,3>, <1,2,4>), 
 (<1,3,4>, <2,3,4>)]
sage: triang.plot(axes=False)                                        
```

The internal implementation covers finding a single triangulation as well as enumerating all triangulations connected to it by bistellar flips. TOPCOM is required to test for regularity and/or to find non-connected triangulations.

While not quite as fast, my limited testing shows the performance to be in the same order of magnitude as TOPCOM:

```
sage: U=matrix([
...      [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],
...      [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],
...      [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],
...      [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],
...      [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]
...   ])
sage: pc = PointConfiguration(U.columns())
sage: pc.set_engine('internal')
sage: time len(pc.triangulations_list())
CPU times: user 23.26 s, sys: 0.02 s, total: 23.29 s
Wall time: 23.32 s
9623
sage: pc.set_engine('TOPCOM')
sage: time len(pc.triangulations_list())
CPU times: user 7.80 s, sys: 0.13 s, total: 7.93 s
Wall time: 8.37 s
9623
```

See also #8169: include TOPCOM, where an optional spkg is being worked on.

Issue created by migration from https://trac.sagemath.org/ticket/9918





---

archive/issue_comments_098525.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-16T11:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98525",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098526.json:
```json
{
    "body": "Passes tests, coverage, documentation looks good.  Nice work!  I haven't tested with TOPCOM but I don't think that's necessary since everything works without it.",
    "created_at": "2011-01-13T01:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98526",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Passes tests, coverage, documentation looks good.  Nice work!  I haven't tested with TOPCOM but I don't think that's necessary since everything works without it.



---

archive/issue_comments_098527.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T01:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98527",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_025009.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-13T04:59:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9917#event-25009"
}
```



---

archive/issue_comments_098528.json:
```json
{
    "body": "For the record:\n\n```\n/disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/triangulation/point_configuration.rst:638: WARNING: duplicate citation BSS, other instance in /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/polyhedra.rst\n```\n\nI am not sure what we are supposed to do with this (personally, I like to have references in the file where they are referenced), but the documentation does not build without warnings...",
    "created_at": "2011-01-22T21:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98528",
    "user": "https://github.com/novoselt"
}
```

For the record:

```
/disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/triangulation/point_configuration.rst:638: WARNING: duplicate citation BSS, other instance in /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/polyhedra.rst
```

I am not sure what we are supposed to do with this (personally, I like to have references in the file where they are referenced), but the documentation does not build without warnings...



---

archive/issue_comments_098529.json:
```json
{
    "body": "See also:\n\nhttps://groups.google.com/d/topic/sage-devel/26YSkYOztus/discussion\n\nUntil there is a proper way of dealing with duplicate references, I think it is best to keep the warning around. The alternatives all suck...",
    "created_at": "2011-01-23T05:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98529",
    "user": "https://github.com/vbraun"
}
```

See also:

https://groups.google.com/d/topic/sage-devel/26YSkYOztus/discussion

Until there is a proper way of dealing with duplicate references, I think it is best to keep the warning around. The alternatives all suck...



---

archive/issue_comments_098530.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-26T17:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98530",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_098531.json:
```json
{
    "body": "Replying to [comment:4 novoselt]:\n> For the record:\n> {{{\n> /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/triangulation/point_configuration.rst:638: WARNING: duplicate citation BSS, other instance in /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/polyhedra.rst\n> }}}\n> I am not sure what we are supposed to do with this (personally, I like to have references in the file where they are referenced), but the documentation does not build without warnings...\n\nI'm afraid a Sphinx warning is sufficient reason for needs_work...",
    "created_at": "2011-01-26T17:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98531",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:4 novoselt]:
> For the record:
> {{{
> /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/triangulation/point_configuration.rst:638: WARNING: duplicate citation BSS, other instance in /disk/scratch/novoselt/sage/devel/sage/doc/en/reference/sage/geometry/polyhedra.rst
> }}}
> I am not sure what we are supposed to do with this (personally, I like to have references in the file where they are referenced), but the documentation does not build without warnings...

I'm afraid a Sphinx warning is sufficient reason for needs_work...



---

archive/issue_comments_098532.json:
```json
{
    "body": "Attachment [trac_9918_triangulate_point_configurations.patch](tarball://root/attachments/some-uuid/ticket9918/trac_9918_triangulate_point_configurations.patch) by @vbraun created at 2011-01-26 22:44:17\n\nUpdated patch",
    "created_at": "2011-01-26T22:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98532",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9918_triangulate_point_configurations.patch](tarball://root/attachments/some-uuid/ticket9918/trac_9918_triangulate_point_configurations.patch) by @vbraun created at 2011-01-26 22:44:17

Updated patch



---

archive/issue_comments_098533.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-26T22:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98533",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_098534.json:
```json
{
    "body": "Fine, if lack of warnings is more important than usefulness of the documentation. I removed the text of the citation, leaving only the link to the same citation a different module. Now Sphinx doesn't complain any more.",
    "created_at": "2011-01-26T22:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98534",
    "user": "https://github.com/vbraun"
}
```

Fine, if lack of warnings is more important than usefulness of the documentation. I removed the text of the citation, leaving only the link to the same citation a different module. Now Sphinx doesn't complain any more.



---

archive/issue_comments_098535.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-27T13:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9917#issuecomment-98535",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_025010.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-27T13:14:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9917",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9917#event-25010"
}
```
