# Issue 9854: fix support for projection options in Tachyon

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2010-09-04 03:13:06

Assignee: jason, was

CC:  vbraun

Keywords: tachyon, raytracing

Currently the Tachyon object defined in plot3d/tachyon.py does not support projections other than the default.  


---

Comment by mhampton created at 2010-09-11 20:59:31

In addition to supporting depth-of-field projections and fisheye lens projections, textures can now use plane-, cylinder-, and sphere-wrapped bitmaps (ppm files).


---

Comment by mhampton created at 2010-09-11 20:59:41

Changing status from new to needs_review.


---

Comment by mhampton created at 2010-09-12 01:18:10

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

Comment by wdj created at 2010-09-12 17:29:53

This applied fine to 4.5.a.a1 on a 32 bit 10.4 ubuntu machine, and passes 
sage -testall.

It's a great patch (I've wondered how to implement it myself) but I worry that it will be too hard to use without further details in the documentation. Does that seem reasonable? If docstring tests are too complicated, maybe just a more complete docstring explanation?


---

Comment by wdj created at 2010-09-12 17:29:53

Changing status from needs_review to needs_info.


---

Comment by vbraun created at 2010-09-23 12:08:25

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

Comment by mhampton created at 2010-09-24 13:09:21

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

Comment by mhampton created at 2010-09-24 13:09:30

Changing status from needs_info to needs_work.


---

Comment by mhampton created at 2011-01-16 21:59:38

Improves tachyon support


---

Attachment

Added more examples and documentation, I think is ready for review again.


---

Comment by mhampton created at 2011-01-16 22:00:33

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2011-01-17 14:34:45

Changing status from needs_review to needs_info.


---

Comment by wdj created at 2011-01-17 14:34:45

This installs on 4.6.1.rc1 and passes sage -testall on an ubuntu linux machine with imagemagik loaded.

I am not seeing where it is documented that the `# optional` lines require imagemagik (and linux?). Am I missing something? ALso, I could not het vbraun's example to work, even with `projection = 'perspective_dof`. Am I doing something wrong?


---

Comment by chapoton created at 2014-12-28 14:16:04

Here is a git branch, still working after so many years ! I just made a quick refreshing.

There remains to make the #optional more precise. Can one use #optional - convert ?
----
New commits:


---

Comment by chapoton created at 2014-12-28 14:21:00

result of texture mapping


---

Attachment

Here is one example image

<img src="texture_mapping.png" width=400px>


---

Comment by git created at 2014-12-28 14:28:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-12-28 14:29:38

I have now added the correct optional tag. Back to *Needs review* !


---

Comment by chapoton created at 2014-12-28 14:29:38

Changing status from needs_info to needs_review.


---

Comment by vbraun created at 2014-12-28 16:24:48

lgtm


---

Comment by vbraun created at 2014-12-28 16:24:48

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-02 22:12:30

Resolution: fixed
