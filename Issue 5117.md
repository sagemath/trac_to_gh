# Issue 5117: remove (or enhance an rename) the Polyhedron.union()) method

Issue created by migration from Trac.

Original creator: sbarthelemy

Original creation time: 2009-01-28 13:00:55

Assignee: mhampton

CC:  mhampton vbraun

The Polyhedron class (in the polyhedra module) has a union method

```
def union(self, other):
    """
    Returns a polyhedron whose vertices are the union of the vertices
    of the two polyhedra.
    ....
```

The name is misleading as the method does not return the union of `self` and `other` (which would not be a convex polyhedron).

The method should then be removed or renamed. As the method itself consists in one single line of code (and as I have no idea of a proper name), I would tend to remove it.

The attached patch removes it.


---

Comment by sbarthelemy created at 2009-01-28 13:03:06

patch that removes the union method


---

Attachment

I disagree that this should be removed.  I created it because I use it!

I think the docstring makes it pretty clear what it does, but I do not object to renaming it.  Perhaps union_of_vertices? Or union_by_vertices?

Marshall


---

Comment by sbarthelemy created at 2009-01-28 16:18:41

Replying to [comment:1 mhampton]:
> I disagree that this should be removed.  I created it because I use it!

using 

```
p = Polyhedron(p1.vertices() + p2.vertices())
```

instead of

```
p = p1.union(p2)
```

does not make a big difference ;)

> I think the docstring makes it pretty clear what it does,
agreed

> but I do not object to renaming it.  Perhaps union_of_vertices? Or union_by_vertices?

what about extending ot to handle unbounded polyhedra as well in this way:

```
p = Polyhedron(p1.vertices() + p2.vertices(), p1.rays() + p2.rays())
```

We could then name it convex_hull() or something like that?

-- 
Sebastien


---

Comment by mhampton created at 2009-01-28 16:36:49

Renaming in convex_hull is fine with me.  The extension to rays is a good idea.


---

Comment by novoselt created at 2010-04-03 15:14:06

Current version is doing this:

```
new_vertices = self.vertices() + other.vertices()
new_rays = self.rays() + other.rays()
new_lines = self.lines() + other.lines()
return Polyhedron(vertices=new_vertices,
                      rays=new_rays, lines=new_lines, field=self.field())

```

which is great, but I STRONGLY support the idea of renaming the method to something else.

I was once working with an algorithm where the *union* of polytopes was used, but I interpreted it exactly as the convex hull and of course got wrong results. I was not using this function, that was my own mistake, but since it is so easy to do, I don't think there should be an extra opportunity for confusion. I agree, that the result is described in the documentation, but I don't always read it for "obvious" functions and perhaps there are other users like me.

How about "extend"? "convex_hull" is also great, although it seems more natural to me to have a global function with such a name called like

```
convex_hull(polyhedron1, polyhedron2, polyhedron3, ...)
```

(There is a function with this name in lattice_polytope which works with points and thinking about it now I suspect that I have chosen not the best name for it either... At least it is not imported into global namespace...)


---

Comment by novoselt created at 2010-04-03 15:14:06

Changing status from new to needs_info.


---

Comment by mhampton created at 2010-04-03 19:05:48

So we could make a convex_hull method and deprecate the union function.  To make a union function in the sense that you and sbarthelemy want, I think we need to make some sort of PolyhedralUnion class to do computations on such objects.


---

Comment by vbraun created at 2010-05-09 14:12:29

Changing status from needs_info to needs_review.


---

Comment by vbraun created at 2010-05-09 14:12:29

Patch renames `self.union()` to `self.convex_hull()` and improves the handling of the underlying field for various operations, for example


```
sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[-1,-1]])
sage: (1 * triangle).field()
Rational Field
sage: (1.0 * triangle).field()
Real Double Field
```



---

Attachment


---

Comment by novoselt created at 2010-05-09 15:39:41

Apply this patch first


---

Attachment

Apply this patch second (and last)


---

Attachment

Looks good to me. I have renamed the original patch file to include the ticket number and its description. On top of that I have made the documentation look nicer and added a message to the TyperError exception. Passes all doctests, so I am giving this a positive review.

My only concern is whether or not we need to use some framework for deprecating functions or what is done for "union" is enough.


---

Comment by novoselt created at 2010-05-09 15:45:03

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-09 02:19:36

Resolution: fixed
