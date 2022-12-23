# Issue 4256: [with patch, needs review] polyhedral improvements: Schlegel diagrams, standard 4d polytopes

Issue created by migration from https://trac.sagemath.org/ticket/4256

Original creator: mhampton

Original creation time: 2008-10-09 18:49:18

Assignee: mhampton

CC:  anakha

Keywords: polytopes, geometry

This patch adds Schlegel diagrams for 4d polytopes (via the render_wireframe function), as well as built-in definitions of the 24-cell and 600-cell.


---

Comment by mhampton created at 2008-10-09 18:50:05

apply versus 3.1.2; conflicts with #4164 patches


---

Attachment

Apply to a vanilla 3.1.2 or 3.1.3; supercedes previous patch


---

Comment by mhampton created at 2008-10-15 23:04:59

This adds several enhancements such as Schegel diagrams, scalar dilation of polytopes, translation by a vector, built-in regular polytopes such as the 24-cell and cross-polytopes, and generation of polar duals.  To make it easier to review this patch includes changes from #4164, so you just need one patch.


---

Comment by mhampton created at 2008-10-21 21:47:03

improved and re-based against 3.1.4


---

Attachment

The trac_4256_v3.patch also incorporates the changes in #4164.  Polyhedra can now be multiplied, scaled, translated, and the polar (dual) constructed.  Several standard polytope families have been added.


---

Comment by anakha created at 2008-10-23 02:02:42

The ambient_dim function overwrites the content self._dim thus making dim() return a wrong answer:


```
sage: p = Polyhedron(vertices = [[0,0,1]])
sage: p.dim()
0
sage: p.ambiant_dim()
3
sage: p.dim()
3
```


In the vertex_adjacency_matrix() docstring, maybe you should use 'binary' rather than '0/1'

In render_solid(), since you now have ambient_dim(), why not use it?  It could replace the ugly test I put there.

Also for the 'special' polyhedron creation methods, it could be good to reuse the approach taken for graphs, where you have the Graph class and an instance of a special class called graphs where you have building methods for most interesting types of graphs.

The first item is a must-fix, the other three would be nice, but are not stricly essential.


---

Comment by mhampton created at 2008-10-24 04:03:49

supercedes previous patches, addresses review


---

Attachment


---

Comment by anakha created at 2008-10-24 16:56:57

The only thing left to do is to mark the lrs_volume() tests as optional.  I forgot that in my initial review.

Anyway, apart from that, positive review


---

Attachment

supercedes previous patches, addresses final review (optional tests)


---

Comment by mhampton created at 2008-10-24 19:07:35

OK, I made the lrs_volume tests optional.  Thanks very much for reviewing this.


---

Comment by mabshoff created at 2008-10-26 01:35:14

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 01:35:14

Merged 4256_v5.patch in Sage 3.2.alpha1
