# Issue 5655: [with patch, needs review] Improved enumeration of vertices and 0-dimensional faces

Issue created by migration from https://trac.sagemath.org/ticket/5655

Original creator: novoselt

Original creation time: 2009-04-01 02:55:09

Assignee: mhampton

Current behaviour of 0-dimensional faces of LatticePolytope's is a bit confusing:

```
sage: ReflexivePolytope(2,0).faces(dim=0)
[[2], [1], [0]]
```

This means that the 0-th 0-dimensional face of this polytope is spanned by the 2-nd vertex. (The reason behind this is that poly.x orders faces according to facets containing them.)

The patch adds a line of code sorting the 0-dimensional faces so that the 0-th 0-dimensional face is spanned by the 0-th vertex.

While this is quite trivial, I found the current enumeration very confusing when it is necessary to keep track of face correspondenses for several related polytopes. (In fact, I was unable to keep track of it correctly and instead made this change as an easier solution.)


---

Attachment


---

Comment by mhampton created at 2009-04-13 19:28:34

There is some danger that this will break old code; otherwise I approve of the changes and I have tested that they seem to work correctly.

I believe that the polytope code, both here and in polyhedra.py, is still in a relatively immature state and that it is better for us to improve it than worry too much about backwards compatibility.  Currently not many people are using it heavily, so I think this sort of change in behavior is OK - only very fragile code would be affected by this.


---

Comment by mabshoff created at 2009-04-15 01:01:55

Ok, can either one of you add a not to what changed at

  http://wiki.sagemath.org/sage-3.4.1

so that we can point people to that in case they complain?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 01:03:34

Resolution: fixed


---

Comment by mabshoff created at 2009-04-15 01:03:34

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
