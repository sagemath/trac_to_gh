# Issue 5511: arbitrary mesh functions

archive/issues_005511.json:
```json
{
    "body": "Assignee: was\n\nCC:  wcauchois\n\nThe following worksheet implements arbitrary mesh functions for 3d graphics objects that are triangulated.  This could probably ought to go into sage somewhere:\n\nArbitrary Mesh Functions\nsystem:sage\n\n\n```\nid=15|\nfrom sage.ext.fast_eval import fast_float\n///\n```\n\n\n<p>Simple bisection root finder for a function of 3 variables.</p>\n\n\n```\nid=16|\n%hide\n%auto\n%cython\n\ncpdef find_root(f, double target, point_1, point_2, double epsilon=1e-4):\n    \"\"\"\n    Given two 3d points point_1 and point_2, find a point (x,y,z) on the segment between them where abs(f(x,y,z)-target)<=epsilon.\n    \n    Returns (x,y,z) if the point lies on the segment between point_1 and point_2 and satisfies the above inequality, otherwise returns None.    \n    \n    The code assumes the function f is continuous.\n    \"\"\"\n    cdef double s0,s1,s2\n    cdef double e0,e1,e2\n    cdef double new_0,new_1,new_2\n    cdef double target_0 = target-epsilon\n    cdef double target_1 = target+epsilon\n    cdef double val\n    cdef int i\n    \n    cdef double min = f(*point_1)\n    cdef double max = f(*point_2)\n    s0,s1,s2 = point_1\n    e0,e1,e2 = point_2\n    if min>max:\n        min,max=max,min\n        s0,s1,s2,e0,e1,e2 = e0,e1,e2,s0,s1,s2\n    # Check to see if one of the endpoints satisfies it\n    if target_0<=min and min<=target_1:\n        return (s0,s1,s2)\n    if target_0<=max and max<=target_0:\n        return (e0,e1,e2)\n    if min>target_1 or max<target_0:\n        return None\n    i=0\n    while True:\n        if i>100:\n            return None\n        else:\n            i+=1\n        # Get half-way point\n        new_0 = s0+(e0-s0)/2.0\n        new_1 = s1+(e1-s1)/2.0\n        new_2 = s2+(e2-s2)/2.0\n        val = f(new_0, new_1, new_2)\n        if val<target_0:\n            s0, s1, s2 = new_0, new_1, new_2\n            min = val\n        elif target_1<val:\n            e0, e1, e2 = new_0, new_1, new_2\n            max=val\n        else:\n            return (new_0,new_1,new_2)\n///\n```\n\n\n\n```\nid=24|\n\n///\n```\n\n\n\n```\nid=41|\ndef calculate_crossing(f,target,v0,v1,vertices, cache_dict):\n    \"\"\"\n    Calculate, for an edge (v0,v1), where f is \"close\" to target.  Use cache_dict to cache the values.\n    \"\"\"\n    # Make a canonical ordering of the vertices since (v0,v1) is the same edge as (v1,v0)\n    if v0>v1:\n        v0,v1=v1,v0\n    if (v0,v1) in cache_dict:\n        return cache_dict[(v0,v1)]\n    else:\n        pt = find_root(f, target, vertices[v0], vertices[v1])\n        cache_dict[(v0,v1)]=pt\n        return pt\n///\n```\n\n\n\n```\nid=34|\n%time\nvar('x,y,z')\np=parametric_plot((x,y,9-x^2-y^2), (x,-3,3), (y,-3,3), mesh=True)\nf=x^2-sin(x*y^2)+cos(z)\nff=fast_float(f, 'x', 'y','z')\np.triangulate()\nvertices=p.vertex_list()\n\n# I am still calculating the function on each vertex multiple times; that could be optimized\n# vertex_values=[ff(*v) for v in vertices]\n\nmesh=[]\nfor target in [0,2,..,20]:\n    cache={}\n    for face in [f+[f[0]] for f in p.index_faces()]:\n        # Adding the [0] takes care of the edge from vertices[0] to vertices[-1]\n        pts = [calculate_crossing(ff,target,face[i], face[i+1],vertices=vertices, cache_dict=cache) for i in range(len(face)-1)]\n        pts = [i for i in pts if i is not None]\n        mesh+=[line([pt1,pt2],thickness=3, color='black') for pt1,pt2 in Subsets(pts, 2)]\n///\n\nCPU time: 0.91 s,  Wall time: 1.26 s\n```\n\n\n\n```\nid=39|\np+sum(mesh)\n///\n```\n\n\n\n```\nid=42|\n(p+sum(mesh)).show(viewer='tachyon')\n///\n```\n\n\n\n```\nid=44|\n\n///\n```\n\n\n\n```\nid=45|\n\n///\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5511\n\n",
    "created_at": "2009-03-13T16:25:22Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "arbitrary mesh functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5511",
    "user": "jason"
}
```
Assignee: was

CC:  wcauchois

The following worksheet implements arbitrary mesh functions for 3d graphics objects that are triangulated.  This could probably ought to go into sage somewhere:

Arbitrary Mesh Functions
system:sage


```
id=15|
from sage.ext.fast_eval import fast_float
///
```


<p>Simple bisection root finder for a function of 3 variables.</p>


```
id=16|
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
```



```
id=24|

///
```



```
id=41|
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
```



```
id=34|
%time
var('x,y,z')
p=parametric_plot((x,y,9-x^2-y^2), (x,-3,3), (y,-3,3), mesh=True)
f=x^2-sin(x*y^2)+cos(z)
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
```



```
id=39|
p+sum(mesh)
///
```



```
id=42|
(p+sum(mesh)).show(viewer='tachyon')
///
```



```
id=44|

///
```



```
id=45|

///
```


Issue created by migration from https://trac.sagemath.org/ticket/5511





---

archive/issue_comments_042798.json:
```json
{
    "body": "Boy, that was all mes",
    "created_at": "2009-03-13T16:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42798",
    "user": "jason"
}
```

Boy, that was all mes



---

archive/issue_comments_042799.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-13T16:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42799",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042800.json:
```json
{
    "body": "Changing assignee from was to jason.",
    "created_at": "2009-03-13T16:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42800",
    "user": "jason"
}
```

Changing assignee from was to jason.



---

archive/issue_comments_042801.json:
```json
{
    "body": "Attachment [Arbitrary_Mesh_Functions.sws](tarball://root/attachments/some-uuid/ticket5511/Arbitrary_Mesh_Functions.sws) by jason created at 2009-03-13 16:44:03",
    "created_at": "2009-03-13T16:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42801",
    "user": "jason"
}
```

Attachment [Arbitrary_Mesh_Functions.sws](tarball://root/attachments/some-uuid/ticket5511/Arbitrary_Mesh_Functions.sws) by jason created at 2009-03-13 16:44:03



---

archive/issue_comments_042802.json:
```json
{
    "body": "See the images at the bottom of http://sagenb.org/home/pub/361/ for examples!",
    "created_at": "2009-03-14T09:16:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42802",
    "user": "jason"
}
```

See the images at the bottom of http://sagenb.org/home/pub/361/ for examples!



---

archive/issue_comments_042803.json:
```json
{
    "body": "Bill,\n\nIf I can take the liberty of CCing you on this, it sounds like something you might be interested in.  At least, if you are going to work a lot more on the low-level graphics stuff, it'd be great if we could support arbitrary mesh functions, like mathematica or this worksheet, for example.",
    "created_at": "2009-04-16T04:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42803",
    "user": "jason"
}
```

Bill,

If I can take the liberty of CCing you on this, it sounds like something you might be interested in.  At least, if you are going to work a lot more on the low-level graphics stuff, it'd be great if we could support arbitrary mesh functions, like mathematica or this worksheet, for example.



---

archive/issue_comments_042804.json:
```json
{
    "body": "This is really neat. So is an arbitrary mesh function like the intersection between the contour of a function and another graph? It looks like your method is generic enough to apply to any IndexFaceSet. Would that be accurate? I will let you know if I can find time to work on this; I would like to!",
    "created_at": "2009-04-23T00:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42804",
    "user": "wcauchois"
}
```

This is really neat. So is an arbitrary mesh function like the intersection between the contour of a function and another graph? It looks like your method is generic enough to apply to any IndexFaceSet. Would that be accurate? I will let you know if I can find time to work on this; I would like to!



---

archive/issue_comments_042805.json:
```json
{
    "body": "Yes, it should be generic enough for any IndexFaceSet.  See http://reference.wolfram.com/mathematica/ref/MeshFunctions.html.",
    "created_at": "2009-04-23T02:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42805",
    "user": "jason"
}
```

Yes, it should be generic enough for any IndexFaceSet.  See http://reference.wolfram.com/mathematica/ref/MeshFunctions.html.



---

archive/issue_comments_042806.json:
```json
{
    "body": "Attachment [mesh_function.jpeg](tarball://root/attachments/some-uuid/ticket5511/mesh_function.jpeg) by jason created at 2009-09-25 16:23:50\n\nAn example of an arbitrary mesh",
    "created_at": "2009-09-25T16:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42806",
    "user": "jason"
}
```

Attachment [mesh_function.jpeg](tarball://root/attachments/some-uuid/ticket5511/mesh_function.jpeg) by jason created at 2009-09-25 16:23:50

An example of an arbitrary mesh



---

archive/issue_comments_042807.json:
```json
{
    "body": "I just noticed in Wolfram's explanation of algorithms that they do not overlay their mesh on their figure (like in this ticket).  Instead, it appears that they build their triangles based on their mesh: \"Mesh lines and contour lines are an integral part of the geometry, not overlays. As a consequence, large numbers of mesh lines or contours will generate a large number of polygons in the corresponding GraphicsComplex.\" (see http://reference.wolfram.com/mathematica/note/SomeNotesOnInternalImplementation.html)",
    "created_at": "2010-11-06T01:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42807",
    "user": "jason"
}
```

I just noticed in Wolfram's explanation of algorithms that they do not overlay their mesh on their figure (like in this ticket).  Instead, it appears that they build their triangles based on their mesh: "Mesh lines and contour lines are an integral part of the geometry, not overlays. As a consequence, large numbers of mesh lines or contours will generate a large number of polygons in the corresponding GraphicsComplex." (see http://reference.wolfram.com/mathematica/note/SomeNotesOnInternalImplementation.html)



---

archive/issue_comments_042808.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-11-06T01:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42808",
    "user": "jason"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_042809.json:
```json
{
    "body": "I guess one advantage to Wolfram's approach is that if you want fine mesh lines, you probably also want the detail afforded by lots of triangles.",
    "created_at": "2010-11-06T01:11:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5511#issuecomment-42809",
    "user": "jason"
}
```

I guess one advantage to Wolfram's approach is that if you want fine mesh lines, you probably also want the detail afforded by lots of triangles.
