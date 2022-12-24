# Issue 9854: fix support for projection options in Tachyon

archive/issues_009854.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  vbraun\n\nKeywords: tachyon, raytracing\n\nCurrently the Tachyon object defined in plot3d/tachyon.py does not support projections other than the default.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/9855\n\n",
    "created_at": "2010-09-04T03:13:06Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "fix support for projection options in Tachyon",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9854",
    "user": "mhampton"
}
```
Assignee: jason, was

CC:  vbraun

Keywords: tachyon, raytracing

Currently the Tachyon object defined in plot3d/tachyon.py does not support projections other than the default.  

Issue created by migration from https://trac.sagemath.org/ticket/9855





---

archive/issue_comments_097261.json:
```json
{
    "body": "In addition to supporting depth-of-field projections and fisheye lens projections, textures can now use plane-, cylinder-, and sphere-wrapped bitmaps (ppm files).",
    "created_at": "2010-09-11T20:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97261",
    "user": "mhampton"
}
```

In addition to supporting depth-of-field projections and fisheye lens projections, textures can now use plane-, cylinder-, and sphere-wrapped bitmaps (ppm files).



---

archive/issue_comments_097262.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-11T20:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97262",
    "user": "mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097263.json:
```json
{
    "body": "Here's a somewhat recursive example that shows the use of the fisheye projection and then uses that image as a plane tiling.  This needs to be done in the notebook, or you need to change the DATA directory to something else.\n\n\n\n```\nT = Tachyon(xres = 800, yres = 600, camera_center = (-2.0,-.1,.3), projection='fisheye', frustum=(-1.0, 1.0, -1.0, 1.0))\nT.texture('t1',color=(0,0,1))\ncedges = [[[1, 1, 1], [-1, 1, 1]], [[1, 1, 1], [1, -1, 1]], [[1, 1, 1], [1, 1, -1]], [[-1, 1, 1], [-1, -1, 1]], [[-1, 1, 1],  [-1, 1, -1]], [[1, -1, 1], [-1, -1, 1]], [[1, -1, 1], [1, -1, -1]], [[-1, -1, 1], [-1, -1, -1]], [[1, 1, -1], [-1, 1, -1]], [[1, 1, -1],  [1, -1, -1]], [[-1, 1, -1], [-1, -1, -1]], [[1, -1, -1], [-1, -1, -1]]]\nfor ed in cedges:\n    T.fcylinder(ed[0],ed[1],.05,'t1')\nT.light((-4,-4,4),.1,(1,1,1))\nT.show()\n```\n\n\n\n```\nT.save(DATA+'t1.png')\nr2 = os.system('convert '+DATA+'t1.png '+DATA+'t1.ppm')\nT = Tachyon(xres = 800, yres = 600, camera_center = (-2.0,-.1,.3), projection='fisheye', frustum=(-1.0, 1.0, -1.0, 1.0))\nT.texture('t1',color=(0,0,1))\nT.texture('p1',color=(1,1,1),opacity = .1, imagefile=DATA+'t1.ppm', texfunc=9)\ncedges = [[[1, 1, 1], [-1, 1, 1]], [[1, 1, 1], [1, -1, 1]], [[1, 1, 1], [1, 1, -1]], [[-1, 1, 1], [-1, -1, 1]], [[-1, 1, 1],  [-1, 1, -1]], [[1, -1, 1], [-1, -1, 1]], [[1, -1, 1], [1, -1, -1]], [[-1, -1, 1], [-1, -1, -1]], [[1, 1, -1], [-1, 1, -1]], [[1, 1, -1],  [1, -1, -1]], [[-1, 1, -1], [-1, -1, -1]], [[1, -1, -1], [-1, -1, -1]]]\nT.plane((0,0,-1),(0,0,1),'p1')\nfor ed in cedges:\n    T.fcylinder(ed[0],ed[1],.05,'t1')\nT.light((-4,-4,4),.1,(1,1,1))\nT.show()\n```\n",
    "created_at": "2010-09-12T01:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97263",
    "user": "mhampton"
}
```

Here's a somewhat recursive example that shows the use of the fisheye projection and then uses that image as a plane tiling.  This needs to be done in the notebook, or you need to change the DATA directory to something else.



```
T = Tachyon(xres = 800, yres = 600, camera_center = (-2.0,-.1,.3), projection='fisheye', frustum=(-1.0, 1.0, -1.0, 1.0))
T.texture('t1',color=(0,0,1))
cedges = [[[1, 1, 1], [-1, 1, 1]], [[1, 1, 1], [1, -1, 1]], [[1, 1, 1], [1, 1, -1]], [[-1, 1, 1], [-1, -1, 1]], [[-1, 1, 1],  [-1, 1, -1]], [[1, -1, 1], [-1, -1, 1]], [[1, -1, 1], [1, -1, -1]], [[-1, -1, 1], [-1, -1, -1]], [[1, 1, -1], [-1, 1, -1]], [[1, 1, -1],  [1, -1, -1]], [[-1, 1, -1], [-1, -1, -1]], [[1, -1, -1], [-1, -1, -1]]]
for ed in cedges:
    T.fcylinder(ed[0],ed[1],.05,'t1')
T.light((-4,-4,4),.1,(1,1,1))
T.show()
```



```
T.save(DATA+'t1.png')
r2 = os.system('convert '+DATA+'t1.png '+DATA+'t1.ppm')
T = Tachyon(xres = 800, yres = 600, camera_center = (-2.0,-.1,.3), projection='fisheye', frustum=(-1.0, 1.0, -1.0, 1.0))
T.texture('t1',color=(0,0,1))
T.texture('p1',color=(1,1,1),opacity = .1, imagefile=DATA+'t1.ppm', texfunc=9)
cedges = [[[1, 1, 1], [-1, 1, 1]], [[1, 1, 1], [1, -1, 1]], [[1, 1, 1], [1, 1, -1]], [[-1, 1, 1], [-1, -1, 1]], [[-1, 1, 1],  [-1, 1, -1]], [[1, -1, 1], [-1, -1, 1]], [[1, -1, 1], [1, -1, -1]], [[-1, -1, 1], [-1, -1, -1]], [[1, 1, -1], [-1, 1, -1]], [[1, 1, -1],  [1, -1, -1]], [[-1, 1, -1], [-1, -1, -1]], [[1, -1, -1], [-1, -1, -1]]]
T.plane((0,0,-1),(0,0,1),'p1')
for ed in cedges:
    T.fcylinder(ed[0],ed[1],.05,'t1')
T.light((-4,-4,4),.1,(1,1,1))
T.show()
```




---

archive/issue_comments_097264.json:
```json
{
    "body": "This applied fine to 4.5.a.a1 on a 32 bit 10.4 ubuntu machine, and passes \nsage -testall.\n\nIt's a great patch (I've wondered how to implement it myself) but I worry that it will be too hard to use without further details in the documentation. Does that seem reasonable? If docstring tests are too complicated, maybe just a more complete docstring explanation?",
    "created_at": "2010-09-12T17:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97264",
    "user": "wdj"
}
```

This applied fine to 4.5.a.a1 on a 32 bit 10.4 ubuntu machine, and passes 
sage -testall.

It's a great patch (I've wondered how to implement it myself) but I worry that it will be too hard to use without further details in the documentation. Does that seem reasonable? If docstring tests are too complicated, maybe just a more complete docstring explanation?



---

archive/issue_comments_097265.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-09-12T17:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97265",
    "user": "wdj"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_097266.json:
```json
{
    "body": "The `aperture` option does not work for me:\n\n```\nsage: T = Tachyon(xres = 800, yres = 600, camera_center = (-1.5,-1.5,.3), projection='fisheye', frustum=(-1.0, 1.0, -1.0, 1.0), aperture = 1)\nsage: T.texture('t1',color=(0,0,1)) \nsage: cedges = [[[1, 1, 1], [-1, 1, 1]], [[1, 1, 1], [1, -1, 1]], [[1, 1, 1], [1, 1, -1]], [[-1, 1, 1], [-1, -1, 1]], [[-1, 1, 1],  [-1, 1, -1]], [[1, -1, 1], [-1, -1, 1]], [[1, -1, 1], [1, -1, -1]], [[-1, -1, 1], [-1, -1, -1]], [[1, 1, -1], [-1, 1, -1]], [[1, 1, -1],  [1, -1, -1]], [[-1, 1, -1], [-1, -1, -1]], [[1, -1, -1], [-1, -1, -1]]]\nsage: for ed in cedges: \n....:     T.fcylinder(ed[0],ed[1],.05,'t1') \n....:     \nsage: T.light((-4,-4,4),.1,(1,1,1)) \nsage: T.show() \n```\n\nand nothing appears. Works fine without the aperture option.",
    "created_at": "2010-09-23T12:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97266",
    "user": "vbraun"
}
```

The `aperture` option does not work for me:

```
sage: T = Tachyon(xres = 800, yres = 600, camera_center = (-1.5,-1.5,.3), projection='fisheye', frustum=(-1.0, 1.0, -1.0, 1.0), aperture = 1)
sage: T.texture('t1',color=(0,0,1)) 
sage: cedges = [[[1, 1, 1], [-1, 1, 1]], [[1, 1, 1], [1, -1, 1]], [[1, 1, 1], [1, 1, -1]], [[-1, 1, 1], [-1, -1, 1]], [[-1, 1, 1],  [-1, 1, -1]], [[1, -1, 1], [-1, -1, 1]], [[1, -1, 1], [1, -1, -1]], [[-1, -1, 1], [-1, -1, -1]], [[1, 1, -1], [-1, 1, -1]], [[1, 1, -1],  [1, -1, -1]], [[-1, 1, -1], [-1, -1, -1]], [[1, -1, -1], [-1, -1, -1]]]
sage: for ed in cedges: 
....:     T.fcylinder(ed[0],ed[1],.05,'t1') 
....:     
sage: T.light((-4,-4,4),.1,(1,1,1)) 
sage: T.show() 
```

and nothing appears. Works fine without the aperture option.



---

archive/issue_comments_097267.json:
```json
{
    "body": "Thanks for taking a look.\n\nObviously I need to add quite a bit of examples and more documentation; unfortunately most of these options aren't well (or at all) documented upstream.\n\nI think the aperture option only works with projection = 'perspective_dof', and then you also need the focallength parameter.  These don't work quite as I would expect but my knowledge of optics is limited.\n\n\n```\nT = Tachyon(xres=800,antialiasing=4, raydepth=10, projection = 'perspective_dof', focallength = '1.0', aperture = '.0025')\nT.light((0,5,7),1.0,(1,1,1))\nT.texture('t1', opacity=1, specular = .3)\nT.texture('t2', opacity=1, specular = .3, color = (0,0,1))\nT.texture('t3', opacity = 1, specular = 1, color = (1,.8,1), diffuse=0.2)\nT.plane((0,0,-1),(0,0,1),'t3')\nttlist = ['t1','t2']\ntt = 't1'\nT.cylinder((0,0,.1),(1,1/3,0),.05,'t3')\nfor q in srange(-3,100,.15):\n    if tt == 't1':\n        tt = 't2'\n    else:\n        tt = 't1'\n    T.sphere((q,q/3+.3*sin(3*q),.1+.3*cos(3*q)), .1, tt)\nT.show()\n```\n",
    "created_at": "2010-09-24T13:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97267",
    "user": "mhampton"
}
```

Thanks for taking a look.

Obviously I need to add quite a bit of examples and more documentation; unfortunately most of these options aren't well (or at all) documented upstream.

I think the aperture option only works with projection = 'perspective_dof', and then you also need the focallength parameter.  These don't work quite as I would expect but my knowledge of optics is limited.


```
T = Tachyon(xres=800,antialiasing=4, raydepth=10, projection = 'perspective_dof', focallength = '1.0', aperture = '.0025')
T.light((0,5,7),1.0,(1,1,1))
T.texture('t1', opacity=1, specular = .3)
T.texture('t2', opacity=1, specular = .3, color = (0,0,1))
T.texture('t3', opacity = 1, specular = 1, color = (1,.8,1), diffuse=0.2)
T.plane((0,0,-1),(0,0,1),'t3')
ttlist = ['t1','t2']
tt = 't1'
T.cylinder((0,0,.1),(1,1/3,0),.05,'t3')
for q in srange(-3,100,.15):
    if tt == 't1':
        tt = 't2'
    else:
        tt = 't1'
    T.sphere((q,q/3+.3*sin(3*q),.1+.3*cos(3*q)), .1, tt)
T.show()
```




---

archive/issue_comments_097268.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-09-24T13:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97268",
    "user": "mhampton"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_097269.json:
```json
{
    "body": "Improves tachyon support",
    "created_at": "2011-01-16T21:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97269",
    "user": "mhampton"
}
```

Improves tachyon support



---

archive/issue_comments_097270.json:
```json
{
    "body": "Attachment [trac_9855_tachyon.patch](tarball://root/attachments/some-uuid/ticket9855/trac_9855_tachyon.patch) by mhampton created at 2011-01-16 22:00:33\n\nAdded more examples and documentation, I think is ready for review again.",
    "created_at": "2011-01-16T22:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97270",
    "user": "mhampton"
}
```

Attachment [trac_9855_tachyon.patch](tarball://root/attachments/some-uuid/ticket9855/trac_9855_tachyon.patch) by mhampton created at 2011-01-16 22:00:33

Added more examples and documentation, I think is ready for review again.



---

archive/issue_comments_097271.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-16T22:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97271",
    "user": "mhampton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097272.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-01-17T14:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97272",
    "user": "wdj"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_097273.json:
```json
{
    "body": "This installs on 4.6.1.rc1 and passes sage -testall on an ubuntu linux machine with imagemagik loaded.\n\nI am not seeing where it is documented that the `# optional` lines require imagemagik (and linux?). Am I missing something? ALso, I could not het vbraun's example to work, even with `projection = 'perspective_dof`. Am I doing something wrong?",
    "created_at": "2011-01-17T14:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97273",
    "user": "wdj"
}
```

This installs on 4.6.1.rc1 and passes sage -testall on an ubuntu linux machine with imagemagik loaded.

I am not seeing where it is documented that the `# optional` lines require imagemagik (and linux?). Am I missing something? ALso, I could not het vbraun's example to work, even with `projection = 'perspective_dof`. Am I doing something wrong?



---

archive/issue_comments_097274.json:
```json
{
    "body": "Here is a git branch, still working after so many years ! I just made a quick refreshing.\n\nThere remains to make the #optional more precise. Can one use #optional - convert ?\n----\nNew commits:",
    "created_at": "2014-12-28T14:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97274",
    "user": "chapoton"
}
```

Here is a git branch, still working after so many years ! I just made a quick refreshing.

There remains to make the #optional more precise. Can one use #optional - convert ?
----
New commits:



---

archive/issue_comments_097275.json:
```json
{
    "body": "result of texture mapping",
    "created_at": "2014-12-28T14:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97275",
    "user": "chapoton"
}
```

result of texture mapping



---

archive/issue_comments_097276.json:
```json
{
    "body": "Attachment [texture_mapping.png](tarball://root/attachments/some-uuid/ticket9855/texture_mapping.png) by chapoton created at 2014-12-28 14:23:14\n\nHere is one example image\n\n<img src=\"texture_mapping.png\" width=400px>",
    "created_at": "2014-12-28T14:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97276",
    "user": "chapoton"
}
```

Attachment [texture_mapping.png](tarball://root/attachments/some-uuid/ticket9855/texture_mapping.png) by chapoton created at 2014-12-28 14:23:14

Here is one example image

<img src="texture_mapping.png" width=400px>



---

archive/issue_comments_097277.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-12-28T14:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97277",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_097278.json:
```json
{
    "body": "I have now added the correct optional tag. Back to **Needs review** !",
    "created_at": "2014-12-28T14:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97278",
    "user": "chapoton"
}
```

I have now added the correct optional tag. Back to **Needs review** !



---

archive/issue_comments_097279.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-12-28T14:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97279",
    "user": "chapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_097280.json:
```json
{
    "body": "lgtm",
    "created_at": "2014-12-28T16:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97280",
    "user": "vbraun"
}
```

lgtm



---

archive/issue_comments_097281.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-28T16:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97281",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097282.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-02T22:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9854#issuecomment-97282",
    "user": "vbraun"
}
```

Resolution: fixed
