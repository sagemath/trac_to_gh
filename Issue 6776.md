# Issue 6776: [with patch, needs review] plot3d improvement for lattice polytopes

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2009-08-19 20:11:21

Assignee: mhampton

This patch allows to

- use plot3d for 1- and 2-dimensional polytopes

- specify different colors for different facets

- specify labels for vertices other than their numbers


```
sage: lattice_polytope.octahedron(2).plot3d(vlabels=["A", "B", "C", "D"])
sage: o = lattice_polytope.octahedron(3)
sage: o.plot3d(facet_colors=sage.plot.plot.rainbow(o.nfacets(), 'rgbtuple'))
```


The positioning of labels is slightly improved 0 they are now shifted away from the barycenter of the polytope, not just the origin.


---

Attachment


---

Comment by mhampton created at 2009-09-22 17:43:52

Looks good, passes tests and coverage.  I did notice that the code for vertices for 1-D polytopes is broken in plot3d.  I.e., the line:

```
vertices = [vector(ZZ, list(self.vertex(i))+[0]*(3-dim)) for i in range(self.nvertices())]
```


raises an error, but it isn't the fault of this code.  It turns out that line3d can modify the type of its arguments, which is a totally separate bug which I will make a new ticket for.  So I think that issue is OK for this patch, it should get resolved separately.

I do have one comment about the vertex labels - if the vertex is at the barycenter, then it isn't shifted at all and the label is right on top of the vertex point.  Since its not directly addressed by this patch I don't think that should affect this review though.

Also, someday soon the polytope code should be unified (i.e. in polyhedra.py and lattice_polytope.py) and refactored.  There are so many functions in both that depend on dimension I think it does make sense to have a polytope-factory class with dimension-specific subclasses.  But that will be a relatively big job and it will be almost impossible not to break backward compatibility.


---

Comment by mvngu created at 2009-09-22 21:35:32

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:33:22

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
