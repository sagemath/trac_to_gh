# Issue 6214: Polyhedra compute incorrect dimension when defined through inequalities

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-06-04 21:27:34

Assignee: mhampton

CC:  vbraun

Not always, but it is possible; the following is from "Drini" on sage-support:

I was checking the new polytope commands
specifically a polytope in R^2   with points (a,b,c,d,e,f) such that

e+b>= c+d
e+c >= b+d
a+b+c+d+e+f =  31
(this is a polytope I had worked on before so I know it very well)

After several tries (documentation still sparse and incomplete) I
managed to cosntruct it.
Checked vertices:

P.vertices()
[[0, 0, 0, 0, 0, 31], [31, 0, 0, 0, 0, 0], [0, 0, 0, 31/2, 31/2, 0],
[0,
0, 31/2, 0, 31/2, 0], [0, 0, 0, 0, 31, 0], [0, 31/2, 0, 0, 31/2, 0],
[0,
31/2, 31/2, 0, 0, 0]]

That's right, 7 vertices, the right ones (again this is a polytope I
knew before)

P.ambiend_dim()
6

P.dim()
6

!!!!!
======================================
The ambient dimension is indeed 6 (we're after all in R^6) but the
polytope has dimension 5 for it's contained in the a+b+c+d+e+f=31
hyperplane (and thus its dimension is 1 less than ambient) Notice all
vertices have coordinates adding 31, therefore it's indeed contained
in the hyperplane
Polymake verified this as well saying dimension is 5

Now I don't know how or where to submit a bug, but I suppose people
involved with development here know
so the least I can do is  comment there's a bug so it's known and
forwarded (and then stop doing polytope computations in sagemath for a
bit longer)
======================================== 


---

Comment by mhampton created at 2009-06-04 21:34:43

Also the linearities keyword needs to be added to the Polyhedra class keyword.


---

Comment by mhampton created at 2009-11-13 03:19:43

This will be fixed once #7109 is completed.


---

Comment by mhampton created at 2010-02-27 19:11:48

Unfortunately this is still incorrect even after #7109.


```
sage: pdata=[[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0,0],[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1],[0,0, 1, -1, -1, 1, 0], [0, 0, -1, 1, -1, 1, 0], [-31, -1, -1, -1, -1, -1, -1],[31, 1, 1, 1, 1, 1, 1]] 
sage: p = Polyhedron(ieqs = DATA)
sage: p.dim()
6
```


But its really dimension 5.  If a second polyhedron is compute from the vertices of the one above, it will have the correct dimension.


---

Comment by mhampton created at 2010-02-27 19:14:09

Oops, in the above, DATA should be pdata.  I had renamed things to not conflict with the DATA directory.


---

Comment by vbraun created at 2010-03-11 14:17:52

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-03-11 14:17:52

mhampton: Something is wrong with your example, the two inequalities [-31, -1, -1, -1, -1, -1, -1], [31, 1, 1, 1, 1, 1, 1] mean sum(x_i)+31=0. The other inequalities imply positive x_i, so there is no solution.


```
sage: Polyhedron(ieqs=pdata).dim()
-1
```


The original example also works as it should:


```
sage: positive_coords = Polyhedron(ieqs=[[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
sage: P = Polyhedron(ieqs=positive_coords.inequalities() + [[0,0,1,-1,-1,1,0], [0,0,-1,1,-1,1,0]], eqns=[This is the Trac macro *-31,1,1,1,1,1,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-31,1,1,1,1,1,1-macro))
sage: P
A 5-dimensional polyhedron in QQ^6 defined as the convex hull of 7 vertices.
sage: P.dim()
5
sage: P.Vrepresentation()
[A vertex at (0, 31/2, 31/2, 0, 0, 0), A vertex at (0, 31/2, 0, 0, 31/2, 0), A vertex at (0, 0, 0, 0, 31, 0), A vertex at (0, 0, 31/2, 0, 31/2, 0), A vertex at (0, 0, 0, 31/2, 31/2, 0), A vertex at (31, 0, 0, 0, 0, 0), A vertex at (0, 0, 0, 0, 0, 31)]
```


I think it is a good example to add to the Polyhdedron documentation, patch is included.

The patch also adds a Polyhedron.contains(point) and Polyhedron.interior_contains(point) method, as that is probably a common use. Finally, I removed some spurious assignments to docstrings that overwrote previously-defined docstrings. 

I'm sorry for bunching patches together, but I think that the other changes are uncontroversial. If anybody feels strongly about that I can disentangle them.


---

Attachment


---

Comment by mhampton created at 2010-04-03 14:57:56

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-04-03 14:57:56

Weird, I must have checked that on an older version by accident.  Sorry about that.

Patch looks good, all doctests passed.  Thanks for adding those functions.


---

Comment by jhpalmieri created at 2010-04-15 04:15:15

The patch file should be produced with Mercurial, not with diff: it should include the author's name and also a commit message beginning with the trac number.   See [http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change) for more information.  It also helps if the name of the patch file starts with the trac number: this one could be called: "trac_6214-polyhedron-v9.patch", for example.

(I've fixed this one.)


---

Comment by jhpalmieri created at 2010-04-15 05:21:18

Merged in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 05:21:18

Resolution: fixed
