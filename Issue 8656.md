# Issue 8656: face_lattice does not seem to work for unbounded polyhedra

archive/issues_008656.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  vbraun\n\nRecent ticket #8650 (required for the output below) fixed a bug in face_lattice computation for polytopes. However, I think that both of the following examples for unbounded polyhedra are incorrect.\n\n\n```\nsage: for lset in Polyhedron(rays=[(1,0)]).face_lattice().level_sets(): lset\n[(None, (0, 1))]\n[((0,), (0,)), ((1,), (0, 1))]\n[((0, 1), (0,))]\n[((0, 1), None)]\n```\n\nThis ray has three faces: empty, vertex, and the whole ray (including the vertex at which it originates). Five are shown, including a face containing the ray, but not the vertex from which it originates.\n\n\n```\nsage: for lset in Polyhedron(rays=[(1,0), (0,1)]).face_lattice().level_sets(): lset\n[(None, (0, 1))]\n[((1,), (0,)), ((0,), (1,)), ((2,), (0, 1))]\n[((1, 2), (0,)), ((0, 2), (1,))]\n[((0, 1, 2), None)]\n```\n\nFor the quadrant we have five faces: empty, vertex, two rays, and the whole quadrant. The above output has seven.\n\nThe easiest fix is probably to raise an exception if the polyhedron is unbounded and state in the documentation that face_lattice works only for polytopes, but of course it would be nice to be able to compute correct faces in all cases.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8656\n\n",
    "created_at": "2010-04-06T20:26:33Z",
    "labels": [
        "geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "face_lattice does not seem to work for unbounded polyhedra",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8656",
    "user": "novoselt"
}
```
Assignee: mhampton

CC:  vbraun

Recent ticket #8650 (required for the output below) fixed a bug in face_lattice computation for polytopes. However, I think that both of the following examples for unbounded polyhedra are incorrect.


```
sage: for lset in Polyhedron(rays=[(1,0)]).face_lattice().level_sets(): lset
[(None, (0, 1))]
[((0,), (0,)), ((1,), (0, 1))]
[((0, 1), (0,))]
[((0, 1), None)]
```

This ray has three faces: empty, vertex, and the whole ray (including the vertex at which it originates). Five are shown, including a face containing the ray, but not the vertex from which it originates.


```
sage: for lset in Polyhedron(rays=[(1,0), (0,1)]).face_lattice().level_sets(): lset
[(None, (0, 1))]
[((1,), (0,)), ((0,), (1,)), ((2,), (0, 1))]
[((1, 2), (0,)), ((0, 2), (1,))]
[((0, 1, 2), None)]
```

For the quadrant we have five faces: empty, vertex, two rays, and the whole quadrant. The above output has seven.

The easiest fix is probably to raise an exception if the polyhedron is unbounded and state in the documentation that face_lattice works only for polytopes, but of course it would be nice to be able to compute correct faces in all cases.

Issue created by migration from https://trac.sagemath.org/ticket/8656





---

archive/issue_comments_078546.json:
```json
{
    "body": "The non-compactness is not the issue, the 1-d interval in a 2-d ambient space fails as well:\n\n\n```\nsage: for lset in Polyhedron(vertices=[(1,0),(0,1)]).face_lattice().level_sets(): print lset\n....: \n[(None, (0, 1, 2))]\n[((1,), (0, 2)), ((0,), (0, 1))]\n[((0, 1), (0,))]\n[((0, 1), None)]\n```\n\n\nOn the other hand, I would argue that the novoselt's Quadrant example is correct: The rays stand for points at infinite distance and are properly counted as points. A triangle would have 8 faces. The edge at infinity is not counted as a face of the quadrant (=double infinite triangle), hence the quadrant does have 7 faces.\n\nThe fundamental flaw of the face_lattice() function is that \n1) its description does not explain in detail what is computed\n2) The result should be returned by means of the H/Vrepresentation objects, and not by their indices.",
    "created_at": "2010-05-08T20:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78546",
    "user": "vbraun"
}
```

The non-compactness is not the issue, the 1-d interval in a 2-d ambient space fails as well:


```
sage: for lset in Polyhedron(vertices=[(1,0),(0,1)]).face_lattice().level_sets(): print lset
....: 
[(None, (0, 1, 2))]
[((1,), (0, 2)), ((0,), (0, 1))]
[((0, 1), (0,))]
[((0, 1), None)]
```


On the other hand, I would argue that the novoselt's Quadrant example is correct: The rays stand for points at infinite distance and are properly counted as points. A triangle would have 8 faces. The edge at infinity is not counted as a face of the quadrant (=double infinite triangle), hence the quadrant does have 7 faces.

The fundamental flaw of the face_lattice() function is that 
1) its description does not explain in detail what is computed
2) The result should be returned by means of the H/Vrepresentation objects, and not by their indices.



---

archive/issue_comments_078547.json:
```json
{
    "body": "Well, what exactly is a face of a convex polyhedron in an affine space? I take as the definition \"an intersection of a supporting hyperplane with the polyhedron.\" In this case rays cannot appear \"by themselves,\" without the vertex from which they are going.\n\nI think that you actually agree with me ;-) Why did you throw away the \"edge at infinity?\" I think, because it is \"completely at infinity.\" But the same is true for a standalone ray representing \"a vertex at infinity\" - this face has no points in the affine space. On the other hand, \"a half-infinite\" edge defined by a vertex and a ray lives in the affine space except for one endpoint. So I would argue that we should throw away all faces generated by infinite point only. Or at least do this by default and have an option to include them, but then I think that ALL infinite faces should be included.\n\nActually, just a couple of days ago I have implemented the algorithm used for face_lattice following the reference in the documentation (and my implementation seems to be faster, but it is not yet ready for inclusion).\n\nThis algorithm computes the Hasse diagram of an atomic and coatomic lattice starting from incidences. In the case of a bounded full-dimensional polyhedron vertices are atoms and facets are coatoms. If the polytope includes rays and lines in addition to vertices and equations in addition to inequalities, one should be more careful.\n\nAndrey",
    "created_at": "2010-05-08T21:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78547",
    "user": "novoselt"
}
```

Well, what exactly is a face of a convex polyhedron in an affine space? I take as the definition "an intersection of a supporting hyperplane with the polyhedron." In this case rays cannot appear "by themselves," without the vertex from which they are going.

I think that you actually agree with me ;-) Why did you throw away the "edge at infinity?" I think, because it is "completely at infinity." But the same is true for a standalone ray representing "a vertex at infinity" - this face has no points in the affine space. On the other hand, "a half-infinite" edge defined by a vertex and a ray lives in the affine space except for one endpoint. So I would argue that we should throw away all faces generated by infinite point only. Or at least do this by default and have an option to include them, but then I think that ALL infinite faces should be included.

Actually, just a couple of days ago I have implemented the algorithm used for face_lattice following the reference in the documentation (and my implementation seems to be faster, but it is not yet ready for inclusion).

This algorithm computes the Hasse diagram of an atomic and coatomic lattice starting from incidences. In the case of a bounded full-dimensional polyhedron vertices are atoms and facets are coatoms. If the polytope includes rays and lines in addition to vertices and equations in addition to inequalities, one should be more careful.

Andrey



---

archive/issue_comments_078548.json:
```json
{
    "body": "I tend to think of non-compact polyhedra in `R^n` as compact polyhedra in `RP^n`. This is also what TOPCOM and, I think, cdd do (though its never spelled out in the cdd manual).  The faces of the non-compact polyhedron consist of all faces of the projective polyhedron that can be spanned by affine points and rays.\n\nI think the rationale is that you tend to do this if you naively apply an algorithm for compact polyhedra in the non-compact case. \n\nThough I agree that, from a user perspective, your definition of faces (always including at least one vertex) would be nicer. However, I think you can not derive it from the incidence matrix alone but you will have to distinguish cases for the different H/V-representation objects. It would be great if you could polish your implementation for inclusion. Let me know if I can help with anything. I do need a working face lattice for non-compact polyhedra for the toric varieties package I'm currently working on...",
    "created_at": "2010-05-09T12:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78548",
    "user": "vbraun"
}
```

I tend to think of non-compact polyhedra in `R^n` as compact polyhedra in `RP^n`. This is also what TOPCOM and, I think, cdd do (though its never spelled out in the cdd manual).  The faces of the non-compact polyhedron consist of all faces of the projective polyhedron that can be spanned by affine points and rays.

I think the rationale is that you tend to do this if you naively apply an algorithm for compact polyhedra in the non-compact case. 

Though I agree that, from a user perspective, your definition of faces (always including at least one vertex) would be nicer. However, I think you can not derive it from the incidence matrix alone but you will have to distinguish cases for the different H/V-representation objects. It would be great if you could polish your implementation for inclusion. Let me know if I can help with anything. I do need a working face lattice for non-compact polyhedra for the toric varieties package I'm currently working on...



---

archive/issue_comments_078549.json:
```json
{
    "body": "Actually, it is a part of my modules for cones/fans/toric varieties/fano toric varieties/Calabi-Yau hypersurfaces and complete intersections inside them. We should probably coordinate our efforts. At what stage is your work?",
    "created_at": "2010-05-09T15:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78549",
    "user": "novoselt"
}
```

Actually, it is a part of my modules for cones/fans/toric varieties/fano toric varieties/Calabi-Yau hypersurfaces and complete intersections inside them. We should probably coordinate our efforts. At what stage is your work?



---

archive/issue_comments_078550.json:
```json
{
    "body": "I've implemented all the fan/lattice basics, cohomology and Chern clases, Chow ring, divisors, Mori cone.\n\nThe current status is at [http://www.stp.dias.ie/~vbraun/Sage/](http://www.stp.dias.ie/~vbraun/Sage/), documentation is at [http://www.stp.dias.ie/~vbraun/Sage/html/en/reference/sage/geometry/toricvariety.html](http://www.stp.dias.ie/~vbraun/Sage/html/en/reference/sage/geometry/toricvariety.html)",
    "created_at": "2010-05-09T15:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78550",
    "user": "vbraun"
}
```

I've implemented all the fan/lattice basics, cohomology and Chern clases, Chow ring, divisors, Mori cone.

The current status is at [http://www.stp.dias.ie/~vbraun/Sage/](http://www.stp.dias.ie/~vbraun/Sage/), documentation is at [http://www.stp.dias.ie/~vbraun/Sage/html/en/reference/sage/geometry/toricvariety.html](http://www.stp.dias.ie/~vbraun/Sage/html/en/reference/sage/geometry/toricvariety.html)



---

archive/issue_comments_078551.json:
```json
{
    "body": "Fixed by the patch in #9954:\n\n```\nsage: for lset in Polyhedron(rays=[(1,0)]).face_lattice().level_sets(): lset\n....: \n[<>]\n[<1>]\n[<0,1>]\nsage: sage: for lset in Polyhedron(rays=[(1,0), (0,1)]).face_lattice().level_sets(): lset\n....: \n[<>]\n[<2>]\n[<1,2>, <0,2>]\n[<0,1,2>]\n```\n\nThis ticket can be closed once #9954 is merged.",
    "created_at": "2010-10-25T14:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78551",
    "user": "vbraun"
}
```

Fixed by the patch in #9954:

```
sage: for lset in Polyhedron(rays=[(1,0)]).face_lattice().level_sets(): lset
....: 
[<>]
[<1>]
[<0,1>]
sage: sage: for lset in Polyhedron(rays=[(1,0), (0,1)]).face_lattice().level_sets(): lset
....: 
[<>]
[<2>]
[<1,2>, <0,2>]
[<0,1,2>]
```

This ticket can be closed once #9954 is merged.



---

archive/issue_comments_078552.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-25T14:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78552",
    "user": "vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078553.json:
```json
{
    "body": "Indeed, #9954 fixes the problem, so this ticket should be closed.",
    "created_at": "2010-11-08T21:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78553",
    "user": "novoselt"
}
```

Indeed, #9954 fixes the problem, so this ticket should be closed.



---

archive/issue_comments_078554.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-08T21:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78554",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078555.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-11-10T08:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8656#issuecomment-78555",
    "user": "jdemeyer"
}
```

Resolution: duplicate
