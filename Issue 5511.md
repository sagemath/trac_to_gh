# Issue 5511: arbitrary mesh functions

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-03-13 16:25:22

Assignee: was

CC:  wcauchois

The following worksheet implements arbitrary mesh functions for 3d graphics objects that are triangulated.  This could probably ought to go into sage somewhere:

Arbitrary Mesh Functions
system:sage

{{{id=15|
from sage.ext.fast_eval import fast_float
///
}}}

<p>Simple bisection root finder for a function of 3 variables.</p>

{{{id=16|
%hide
%auto
%cython

cpdef find_root(f, double target, point_1, point_2, double epsilon=1e-4):
    """
    Given two 3d points point_1 and point_2, find a point (x,y,z) on the segment between them where abs(f(x,y,z)-target)<=epsilon.
    
    Returns (x,y,z) if the point lies on the segment between point_1 and point_2 and satisfies the above inequality, otherwise returns None.    
    
    The code assumes the function f is continuous.
    """
    cdef double s0,s1,s2
    cdef double e0,e1,e2
    cdef double new_0,new_1,new_2
    cdef double target_0 = target-epsilon
    cdef double target_1 = target+epsilon
    cdef double val
    cdef int i
    
    cdef double min = f(*point_1)
    cdef double max = f(*point_2)
    s0,s1,s2 = point_1
    e0,e1,e2 = point_2
    if min>max:
        min,max=max,min
        s0,s1,s2,e0,e1,e2 = e0,e1,e2,s0,s1,s2
    # Check to see if one of the endpoints satisfies it
    if target_0<=min and min<=target_1:
        return (s0,s1,s2)
    if target_0<=max and max<=target_0:
        return (e0,e1,e2)
    if min>target_1 or max<target_0:
        return None
    i=0
    while True:
        if i>100:
            return None
        else:
            i+=1
        # Get half-way point
        new_0 = s0+(e0-s0)/2.0
        new_1 = s1+(e1-s1)/2.0
        new_2 = s2+(e2-s2)/2.0
        val = f(new_0, new_1, new_2)
        if val<target_0:
            s0, s1, s2 = new_0, new_1, new_2
            min = val
        elif target_1<val:
            e0, e1, e2 = new_0, new_1, new_2
            max=val
        else:
            return (new_0,new_1,new_2)
///
}}}

{{{id=24|

///
}}}

{{{id=41|
def calculate_crossing(f,target,v0,v1,vertices, cache_dict):
    """
    Calculate, for an edge (v0,v1), where f is "close" to target.  Use cache_dict to cache the values.
    """
    # Make a canonical ordering of the vertices since (v0,v1) is the same edge as (v1,v0)
    if v0>v1:
        v0,v1=v1,v0
    if (v0,v1) in cache_dict:
        return cache_dict[(v0,v1)]
    else:
        pt = find_root(f, target, vertices[v0], vertices[v1])
        cache_dict[(v0,v1)]=pt
        return pt
///
}}}

{{{id=34|
%time
var('x,y,z')
p=parametric_plot((x,y,9-x<sup>2-y</sup>2), (x,-3,3), (y,-3,3), mesh=True)
f=x<sup>2-sin(x*y</sup>2)+cos(z)
ff=fast_float(f, 'x', 'y','z')
p.triangulate()
vertices=p.vertex_list()

# I am still calculating the function on each vertex multiple times; that could be optimized
# vertex_values=[ff(*v) for v in vertices]

mesh=[]
for target in [0,2,..,20]:
    cache={}
    for face in [f+[f[0]] for f in p.index_faces()]:
        # Adding the [0] takes care of the edge from vertices[0] to vertices[-1]
        pts = [calculate_crossing(ff,target,face[i], face[i+1],vertices=vertices, cache_dict=cache) for i in range(len(face)-1)]
        pts = [i for i in pts if i is not None]
        mesh+=[line([pt1,pt2],thickness=3, color='black') for pt1,pt2 in Subsets(pts, 2)]
///

CPU time: 0.91 s,  Wall time: 1.26 s
}}}

{{{id=39|
p+sum(mesh)
///
}}}

{{{id=42|
(p+sum(mesh)).show(viewer='tachyon')
///
}}}

{{{id=44|

///
}}}

{{{id=45|

///
}}}


---

Comment by jason created at 2009-03-13 16:26:10

Boy, that was all mes


---

Comment by jason created at 2009-03-13 16:44:03

Changing status from new to assigned.


---

Comment by jason created at 2009-03-13 16:44:03

Changing assignee from was to jason.


---

Attachment


---

Comment by jason created at 2009-03-14 09:16:09

See the images at the bottom of http://sagenb.org/home/pub/361/ for examples!


---

Comment by jason created at 2009-04-16 04:13:52

Bill,

If I can take the liberty of CCing you on this, it sounds like something you might be interested in.  At least, if you are going to work a lot more on the low-level graphics stuff, it'd be great if we could support arbitrary mesh functions, like mathematica or this worksheet, for example.


---

Comment by wcauchois created at 2009-04-23 00:09:18

This is really neat. So is an arbitrary mesh function like the intersection between the contour of a function and another graph? It looks like your method is generic enough to apply to any IndexFaceSet. Would that be accurate? I will let you know if I can find time to work on this; I would like to!


---

Comment by jason created at 2009-04-23 02:59:29

Yes, it should be generic enough for any IndexFaceSet.  See http://reference.wolfram.com/mathematica/ref/MeshFunctions.html.


---

Attachment

An example of an arbitrary mesh


---

Comment by jason created at 2010-11-06 01:10:36

I just noticed in Wolfram's explanation of algorithms that they do not overlay their mesh on their figure (like in this ticket).  Instead, it appears that they build their triangles based on their mesh: "Mesh lines and contour lines are an integral part of the geometry, not overlays. As a consequence, large numbers of mesh lines or contours will generate a large number of polygons in the corresponding GraphicsComplex." (see http://reference.wolfram.com/mathematica/note/SomeNotesOnInternalImplementation.html)


---

Comment by jason created at 2010-11-06 01:10:43

Changing status from new to needs_work.


---

Comment by jason created at 2010-11-06 01:11:57

I guess one advantage to Wolfram's approach is that if you want fine mesh lines, you probably also want the detail afforded by lots of triangles.
