# Issue 6214: Polyhedra compute incorrect dimension when defined through inequalities

archive/issues_006214.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @vbraun\n\nNot always, but it is possible; the following is from \"Drini\" on sage-support:\n\nI was checking the new polytope commands\nspecifically a polytope in R^2   with points (a,b,c,d,e,f) such that\n\ne+b>= c+d\ne+c >= b+d\na+b+c+d+e+f =  31\n(this is a polytope I had worked on before so I know it very well)\n\nAfter several tries (documentation still sparse and incomplete) I\nmanaged to cosntruct it.\nChecked vertices:\n\nP.vertices()\n[[0, 0, 0, 0, 0, 31], [31, 0, 0, 0, 0, 0], [0, 0, 0, 31/2, 31/2, 0],\n[0,\n0, 31/2, 0, 31/2, 0], [0, 0, 0, 0, 31, 0], [0, 31/2, 0, 0, 31/2, 0],\n[0,\n31/2, 31/2, 0, 0, 0]]\n\nThat's right, 7 vertices, the right ones (again this is a polytope I\nknew before)\n\nP.ambiend_dim()\n6\n\nP.dim()\n6\n\n!!!!!\n======================================\nThe ambient dimension is indeed 6 (we're after all in R^6) but the\npolytope has dimension 5 for it's contained in the a+b+c+d+e+f=31\nhyperplane (and thus its dimension is 1 less than ambient) Notice all\nvertices have coordinates adding 31, therefore it's indeed contained\nin the hyperplane\nPolymake verified this as well saying dimension is 5\n\nNow I don't know how or where to submit a bug, but I suppose people\ninvolved with development here know\nso the least I can do is  comment there's a bug so it's known and\nforwarded (and then stop doing polytope computations in sagemath for a\nbit longer)\n======================================== \n\nIssue created by migration from https://trac.sagemath.org/ticket/6214\n\n",
    "created_at": "2009-06-04T21:27:34Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Polyhedra compute incorrect dimension when defined through inequalities",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6214",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mhampton

CC:  @vbraun

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

Issue created by migration from https://trac.sagemath.org/ticket/6214





---

archive/issue_comments_049547.json:
```json
{
    "body": "Also the linearities keyword needs to be added to the Polyhedra class keyword.",
    "created_at": "2009-06-04T21:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Also the linearities keyword needs to be added to the Polyhedra class keyword.



---

archive/issue_comments_049548.json:
```json
{
    "body": "This will be fixed once #7109 is completed.",
    "created_at": "2009-11-13T03:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49548",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This will be fixed once #7109 is completed.



---

archive/issue_comments_049549.json:
```json
{
    "body": "Unfortunately this is still incorrect even after #7109.\n\n\n```\nsage: pdata=[[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0,0],[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1],[0,0, 1, -1, -1, 1, 0], [0, 0, -1, 1, -1, 1, 0], [-31, -1, -1, -1, -1, -1, -1],[31, 1, 1, 1, 1, 1, 1]] \nsage: p = Polyhedron(ieqs = DATA)\nsage: p.dim()\n6\n```\n\n\nBut its really dimension 5.  If a second polyhedron is compute from the vertices of the one above, it will have the correct dimension.",
    "created_at": "2010-02-27T19:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49549",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Unfortunately this is still incorrect even after #7109.


```
sage: pdata=[[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0,0],[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1],[0,0, 1, -1, -1, 1, 0], [0, 0, -1, 1, -1, 1, 0], [-31, -1, -1, -1, -1, -1, -1],[31, 1, 1, 1, 1, 1, 1]] 
sage: p = Polyhedron(ieqs = DATA)
sage: p.dim()
6
```


But its really dimension 5.  If a second polyhedron is compute from the vertices of the one above, it will have the correct dimension.



---

archive/issue_comments_049550.json:
```json
{
    "body": "Oops, in the above, DATA should be pdata.  I had renamed things to not conflict with the DATA directory.",
    "created_at": "2010-02-27T19:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Oops, in the above, DATA should be pdata.  I had renamed things to not conflict with the DATA directory.



---

archive/issue_comments_049551.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T14:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49551",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049552.json:
```json
{
    "body": "mhampton: Something is wrong with your example, the two inequalities [-31, -1, -1, -1, -1, -1, -1], [31, 1, 1, 1, 1, 1, 1] mean sum(x_i)+31=0. The other inequalities imply positive x_i, so there is no solution.\n\n\n```\nsage: Polyhedron(ieqs=pdata).dim()\n-1\n```\n\n\nThe original example also works as it should:\n\n\n```\nsage: positive_coords = Polyhedron(ieqs=[[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])\nsage: P = Polyhedron(ieqs=positive_coords.inequalities() + [[0,0,1,-1,-1,1,0], [0,0,-1,1,-1,1,0]], eqns=[[-31,1,1,1,1,1,1]])\nsage: P\nA 5-dimensional polyhedron in QQ^6 defined as the convex hull of 7 vertices.\nsage: P.dim()\n5\nsage: P.Vrepresentation()\n[A vertex at (0, 31/2, 31/2, 0, 0, 0), A vertex at (0, 31/2, 0, 0, 31/2, 0), A vertex at (0, 0, 0, 0, 31, 0), A vertex at (0, 0, 31/2, 0, 31/2, 0), A vertex at (0, 0, 0, 31/2, 31/2, 0), A vertex at (31, 0, 0, 0, 0, 0), A vertex at (0, 0, 0, 0, 0, 31)]\n```\n\n\nI think it is a good example to add to the Polyhdedron documentation, patch is included.\n\nThe patch also adds a Polyhedron.contains(point) and Polyhedron.interior_contains(point) method, as that is probably a common use. Finally, I removed some spurious assignments to docstrings that overwrote previously-defined docstrings. \n\nI'm sorry for bunching patches together, but I think that the other changes are uncontroversial. If anybody feels strongly about that I can disentangle them.",
    "created_at": "2010-03-11T14:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49552",
    "user": "https://github.com/vbraun"
}
```

mhampton: Something is wrong with your example, the two inequalities [-31, -1, -1, -1, -1, -1, -1], [31, 1, 1, 1, 1, 1, 1] mean sum(x_i)+31=0. The other inequalities imply positive x_i, so there is no solution.


```
sage: Polyhedron(ieqs=pdata).dim()
-1
```


The original example also works as it should:


```
sage: positive_coords = Polyhedron(ieqs=[[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]])
sage: P = Polyhedron(ieqs=positive_coords.inequalities() + [[0,0,1,-1,-1,1,0], [0,0,-1,1,-1,1,0]], eqns=[[-31,1,1,1,1,1,1]])
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

archive/issue_comments_049553.json:
```json
{
    "body": "Attachment [polyhedron-v9.patch](tarball://root/attachments/some-uuid/ticket6214/polyhedron-v9.patch) by @vbraun created at 2010-03-11 14:21:22",
    "created_at": "2010-03-11T14:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49553",
    "user": "https://github.com/vbraun"
}
```

Attachment [polyhedron-v9.patch](tarball://root/attachments/some-uuid/ticket6214/polyhedron-v9.patch) by @vbraun created at 2010-03-11 14:21:22



---

archive/issue_comments_049554.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-03T14:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49554",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_049555.json:
```json
{
    "body": "Weird, I must have checked that on an older version by accident.  Sorry about that.\n\nPatch looks good, all doctests passed.  Thanks for adding those functions.",
    "created_at": "2010-04-03T14:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49555",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Weird, I must have checked that on an older version by accident.  Sorry about that.

Patch looks good, all doctests passed.  Thanks for adding those functions.



---

archive/issue_comments_049556.json:
```json
{
    "body": "The patch file should be produced with Mercurial, not with diff: it should include the author's name and also a commit message beginning with the trac number.   See [http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change) for more information.  It also helps if the name of the patch file starts with the trac number: this one could be called: \"trac_6214-polyhedron-v9.patch\", for example.\n\n(I've fixed this one.)",
    "created_at": "2010-04-15T04:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49556",
    "user": "https://github.com/jhpalmieri"
}
```

The patch file should be produced with Mercurial, not with diff: it should include the author's name and also a commit message beginning with the trac number.   See [http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change](http://www.sagemath.org/doc/developer/walk_through.html#submitting-a-change) for more information.  It also helps if the name of the patch file starts with the trac number: this one could be called: "trac_6214-polyhedron-v9.patch", for example.

(I've fixed this one.)



---

archive/issue_comments_049557.json:
```json
{
    "body": "Merged in 4.4.alpha0.",
    "created_at": "2010-04-15T05:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49557",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0.



---

archive/issue_comments_049558.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6214#issuecomment-49558",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
