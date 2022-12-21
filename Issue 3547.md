# Issue 3547: create a polygon3d function

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-07-03 21:28:47

Assignee: was

This should be the 3d analogue of the polygon function.


---

Comment by mabshoff created at 2008-07-06 20:22:36

Please remember to assign milestones to all tickets.

Cheers,

Michael


---

Comment by mhansen created at 2008-07-06 20:23:21

Oops :-)


---

Comment by robertwb created at 2008-12-16 18:49:57

Also, the polygon function should defer to this when the input is 3d points 


```

On Dec 16, 2008, at 8:28 AM, philt wrote:

Hello,

I got some trouble trying to draw polygons in JMol because the
function looks not available easily.
Sage is featuring the following:
point() -> try point2d else point3d
line() -> try line2d else line3d
polygon() -> only 2d
but many fancy volumes are available in 3D...

I think it'd be more natural to have polygon working in a similar
flexible way.
Something like:

try:
        return polygon2d(points, **kwds)
    except ValueError:
        from sage.plot.plot3d.platonic import IndexFaceSet as
polygon3d
        return polygon3d(points, **kwds)

with polygon2d being the current code of polygon()
```



---

Attachment


---

Comment by abergeron created at 2008-12-24 23:01:19

I did a trial implementation using IndexFaceSet.  The code is really simple (and dumb).

It works with any number of points and just draws triangles as in a triangle strip.  

The alternative would have been to draw the enclosed space, but that functionality is already provided by Polyhedron and does not mimick what polygon[2d] does.


---

Comment by abergeron created at 2008-12-24 23:01:19

Changing assignee from was to abergeron.


---

Comment by shumow created at 2009-01-24 12:27:41

looks good to me


---

Comment by mabshoff created at 2009-01-28 16:17:32

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 16:17:32

Resolution: fixed


---

Comment by mvngu created at 2009-02-07 04:21:44

Is it possible for someone to attach an image or two to this ticket to illustrate the sort of images one can get from using the new function `polygon3d()`? I'm looking for an image of a plot resulting from using the function `polygon3d()`. What I have in mind is something along the line of the images attached to #2770 and #4976. Such images should serve as a high-level summary of what a (new) plotting function can do. And having such images mean that they can be referred to from a release tour note on the Sage wiki. The point is: when introducing new functionalities one would upload a patch to trac, together with doctests and examples. But when a new function deals with graphics and plots, I think it's a good idea to upload an image or two whenever possible. I don't always have the latest alpha on my work machine, only the latest stable version, so can someone please upload an image?
