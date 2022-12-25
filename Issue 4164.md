# Issue 4164: [with patch, positive review] Make triangulated_facial_incidences() work better

archive/issues_004164.json:
```json
{
    "body": "Assignee: anakha\n\nKeywords: polyhedra, graphics\n\nThe attached patch switches from random lifting to the fan algorithm for triangularization which work in all cases and should work with all dimensions.\n\nI left some safeguard code in there just in case I made assumptions that aren't always true (or have some bugs).\n\nFor the record the assumptions are:\n* faces are always convex\n* there won't ever be faces with no vertices\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4164\n\n",
    "closed_at": "2008-10-26T01:07:14Z",
    "created_at": "2008-09-21T20:35:40Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, positive review] Make triangulated_facial_incidences() work better",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4164",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```
Assignee: anakha

Keywords: polyhedra, graphics

The attached patch switches from random lifting to the fan algorithm for triangularization which work in all cases and should work with all dimensions.

I left some safeguard code in there just in case I made assumptions that aren't always true (or have some bugs).

For the record the assumptions are:
* faces are always convex
* there won't ever be faces with no vertices


Issue created by migration from https://trac.sagemath.org/ticket/4164





---

archive/issue_comments_030157.json:
```json
{
    "body": "Attachment [trac_4164.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164.patch) by anakha created at 2008-09-21 20:36:21",
    "created_at": "2008-09-21T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30157",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_4164.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164.patch) by anakha created at 2008-09-21 20:36:21



---

archive/issue_comments_030158.json:
```json
{
    "body": "Changing assignee from @williamstein to anakha.",
    "created_at": "2008-09-22T22:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30158",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Changing assignee from @williamstein to anakha.



---

archive/issue_comments_030159.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-22T22:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30159",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030160.json:
```json
{
    "body": "(reviewing myself)\n\nThis breaks sometimes for dimensions above 3 because vertex_adajcencies() will list adjacencies that are not on the current face, but still in the polygon.  \n\nI was just lucky with my earlier tests.  Expect an updated patch later tonight.",
    "created_at": "2008-09-22T22:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30160",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

(reviewing myself)

This breaks sometimes for dimensions above 3 because vertex_adajcencies() will list adjacencies that are not on the current face, but still in the polygon.  

I was just lucky with my earlier tests.  Expect an updated patch later tonight.



---

archive/issue_comments_030161.json:
```json
{
    "body": "Attachment [trac_4164_corrections.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_corrections.patch) by anakha created at 2008-09-23 06:02:18\n\nNow it works in all cases, all the time.  It is faster for dimensions 2 and 3.\n\nDimensions higher than that can take really long (like 1 second in dimension 4) to compute, but at least they work.\n\nI would like someone familiar with polyhedrons and their triangularization to do a sanity check on the output for dimensions 4 or 5 since my level of understanding of this topic is a bit lacking.",
    "created_at": "2008-09-23T06:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30161",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_4164_corrections.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_corrections.patch) by anakha created at 2008-09-23 06:02:18

Now it works in all cases, all the time.  It is faster for dimensions 2 and 3.

Dimensions higher than that can take really long (like 1 second in dimension 4) to compute, but at least they work.

I would like someone familiar with polyhedrons and their triangularization to do a sanity check on the output for dimensions 4 or 5 since my level of understanding of this topic is a bit lacking.



---

archive/issue_comments_030162.json:
```json
{
    "body": "Attachment [trac_4164_corrections2.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_corrections2.patch) by anakha created at 2008-09-23 06:03:17\n\nCrap, I forgot to remove the part that disabled the cache for the timings I did.  trac_4164_corrections2.patch fixes that.",
    "created_at": "2008-09-23T06:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30162",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_4164_corrections2.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_corrections2.patch) by anakha created at 2008-09-23 06:03:17

Crap, I forgot to remove the part that disabled the cache for the timings I did.  trac_4164_corrections2.patch fixes that.



---

archive/issue_comments_030163.json:
```json
{
    "body": "First of all let me say thanks for working on this.  There are some problems with these patches though:\n\n1) They don't pass doctesting on my machine.  This is because of some output order differences.  Did you test the final combination of all three patches?  Otherwise it might be architecture-specific but looking at your code that seems unlikely.\n\n2) In higher dimensions, \"triangulation\" usually means a decomposition into simplices - so in four dimensions the elements of a triangulation of a face should be tetrahedra.  It occurs to me that it would perhaps be best to write a function in the Polyhedra class that triangulates (in this sense) the polyhedra itself, and then for .triangulated_facial_incideneces() call this function on the polyhedrons generated by each face.\n\n3) Things seem to break for bigger examples.  For instance, an octohedron:\n\n```\nsage: p_oct = Polyhedron(vertices = [[0,1],[0,2],[1,0],[2,0],[3,1],[3,2],[1,3],[2,3]])\nsage: p_oct.triangulated_facial_incidences()\n\n[[0, [3, 4, 3]],\n [1, [2, 3, 2]],\n [2, [0, 2, 0]],\n [3, [0, 1, 0]],\n [4, [1, 6, 1]],\n [5, [6, 7, 6]],\n [6, [5, 7, 5]],\n [7, [4, 5, 4]]]\n```\n\nNotice that the triangulation consists of the edges.\n\nDo you have a reference for the algorithm you are using, or are you coming up with one yourself?",
    "created_at": "2008-09-23T12:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30163",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

First of all let me say thanks for working on this.  There are some problems with these patches though:

1) They don't pass doctesting on my machine.  This is because of some output order differences.  Did you test the final combination of all three patches?  Otherwise it might be architecture-specific but looking at your code that seems unlikely.

2) In higher dimensions, "triangulation" usually means a decomposition into simplices - so in four dimensions the elements of a triangulation of a face should be tetrahedra.  It occurs to me that it would perhaps be best to write a function in the Polyhedra class that triangulates (in this sense) the polyhedra itself, and then for .triangulated_facial_incideneces() call this function on the polyhedrons generated by each face.

3) Things seem to break for bigger examples.  For instance, an octohedron:

```
sage: p_oct = Polyhedron(vertices = [[0,1],[0,2],[1,0],[2,0],[3,1],[3,2],[1,3],[2,3]])
sage: p_oct.triangulated_facial_incidences()

[[0, [3, 4, 3]],
 [1, [2, 3, 2]],
 [2, [0, 2, 0]],
 [3, [0, 1, 0]],
 [4, [1, 6, 1]],
 [5, [6, 7, 6]],
 [6, [5, 7, 5]],
 [7, [4, 5, 4]]]
```

Notice that the triangulation consists of the edges.

Do you have a reference for the algorithm you are using, or are you coming up with one yourself?



---

archive/issue_comments_030164.json:
```json
{
    "body": "Replying to [comment:4 mhampton]:\n> First of all let me say thanks for working on this.  There are some problems with these patches though:\n> \n> 1) They don't pass doctesting on my machine.  This is because of some output order differences.  Did you test the final combination of all three patches?  Otherwise it might be architecture-specific but looking at your code that seems unlikely.\n\n\nI think I should never post patches past midnight, because this is when I always forget something like this.\n\n> 2) In higher dimensions, \"triangulation\" usually means a decomposition into simplices - so in four dimensions the elements of a triangulation of a face should be tetrahedra.  It occurs to me that it would perhaps be best to write a function in the Polyhedra class that triangulates (in this sense) the polyhedra itself, and then for .triangulated_facial_incideneces() call this function on the polyhedrons generated by each face.\n\n\nI can't think right now of an algorithm that will triangulate according to your description in an arbitrary dimension.  I will think about it for a while though. \n\n> 3) Things seem to break for bigger examples.  For instance, an octohedron:\n> \n> ```\n> sage: p_oct = Polyhedron(vertices = [[0,1],[0,2],[1,0],[2,0],[3,1],[3,2],[1,3],[2,3]])\n> sage: p_oct.triangulated_facial_incidences()\n> \n> [[0, [3, 4, 3]],\n>  [1, [2, 3, 2]],\n>  [2, [0, 2, 0]],\n>  [3, [0, 1, 0]],\n>  [4, [1, 6, 1]],\n>  [5, [6, 7, 6]],\n>  [6, [5, 7, 5]],\n>  [7, [4, 5, 4]]]\n> ```\n> \n> Notice that the triangulation consists of the edges.\n\n\nThis is what I expected.  Since the polyhedron itself is in 2D the edges are in 1D so they correspond to the edges.  I asked you this question before with a square and you told me it was normal.  \n\nIf it is not supposed to do that, then facial_incidences() is broken.  Take a look at it.\n\n> Do you have a reference for the algorithm you are using, or are you coming up with one yourself?\n\n\nI am more or less coming up with it myself.  The actual triangulation of 2D surfaces is pretty standard in computer graphics (walk the points of the polygon building a triangle strip) but it obviously does not cover the cases where surfaces are in 4D.  That's where I innovate (or just do something random it seems).",
    "created_at": "2008-09-23T16:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30164",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Replying to [comment:4 mhampton]:
> First of all let me say thanks for working on this.  There are some problems with these patches though:
> 
> 1) They don't pass doctesting on my machine.  This is because of some output order differences.  Did you test the final combination of all three patches?  Otherwise it might be architecture-specific but looking at your code that seems unlikely.


I think I should never post patches past midnight, because this is when I always forget something like this.

> 2) In higher dimensions, "triangulation" usually means a decomposition into simplices - so in four dimensions the elements of a triangulation of a face should be tetrahedra.  It occurs to me that it would perhaps be best to write a function in the Polyhedra class that triangulates (in this sense) the polyhedra itself, and then for .triangulated_facial_incideneces() call this function on the polyhedrons generated by each face.


I can't think right now of an algorithm that will triangulate according to your description in an arbitrary dimension.  I will think about it for a while though. 

> 3) Things seem to break for bigger examples.  For instance, an octohedron:
> 
> ```
> sage: p_oct = Polyhedron(vertices = [[0,1],[0,2],[1,0],[2,0],[3,1],[3,2],[1,3],[2,3]])
> sage: p_oct.triangulated_facial_incidences()
> 
> [[0, [3, 4, 3]],
>  [1, [2, 3, 2]],
>  [2, [0, 2, 0]],
>  [3, [0, 1, 0]],
>  [4, [1, 6, 1]],
>  [5, [6, 7, 6]],
>  [6, [5, 7, 5]],
>  [7, [4, 5, 4]]]
> ```
> 
> Notice that the triangulation consists of the edges.


This is what I expected.  Since the polyhedron itself is in 2D the edges are in 1D so they correspond to the edges.  I asked you this question before with a square and you told me it was normal.  

If it is not supposed to do that, then facial_incidences() is broken.  Take a look at it.

> Do you have a reference for the algorithm you are using, or are you coming up with one yourself?


I am more or less coming up with it myself.  The actual triangulation of 2D surfaces is pretty standard in computer graphics (walk the points of the polygon building a triangle strip) but it obviously does not cover the cases where surfaces are in 4D.  That's where I innovate (or just do something random it seems).



---

archive/issue_comments_030165.json:
```json
{
    "body": "I'm sorry, I don't know what I was thinking - about my point (3).  I guess I was thrown off by the edge having three coordinates.  I retested this on a pyramid with an octahedral base (what I really had in mind) and it was fine.  But on a 2D polytope, the \"triangulation\" of the faces would just be the edges.\n\nI will post a patch soon so you can take a look if you want at what I've been doing.  It might be useful for testing at least.",
    "created_at": "2008-09-23T21:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I'm sorry, I don't know what I was thinking - about my point (3).  I guess I was thrown off by the edge having three coordinates.  I retested this on a pyramid with an octahedral base (what I really had in mind) and it was fine.  But on a 2D polytope, the "triangulation" of the faces would just be the edges.

I will post a patch soon so you can take a look if you want at what I've been doing.  It might be useful for testing at least.



---

archive/issue_comments_030166.json:
```json
{
    "body": "Attachment [trac_4164_tfi.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_tfi.patch) by anakha created at 2008-09-24 04:05:30",
    "created_at": "2008-09-24T04:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30166",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_4164_tfi.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_tfi.patch) by anakha created at 2008-09-24 04:05:30



---

archive/issue_comments_030167.json:
```json
{
    "body": "New patch, and new method.  This time it should work in all cases and behave like one would expect.  \n\nThis does not include a render_solid() method because it is late and I don't want to work on it right now (plus the fact that I am not quite certain about what it should do for polyhedra of dimension > 3)\n\nTo try (or merge) only apply trac_4164_tfi.patch",
    "created_at": "2008-09-24T04:09:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30167",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

New patch, and new method.  This time it should work in all cases and behave like one would expect.  

This does not include a render_solid() method because it is late and I don't want to work on it right now (plus the fact that I am not quite certain about what it should do for polyhedra of dimension > 3)

To try (or merge) only apply trac_4164_tfi.patch



---

archive/issue_comments_030168.json:
```json
{
    "body": "This passed all tests, and seems to work well for 3D polytopes, which was the original request.  It does fail for some 4D polytopes, for example for one with vertices:\n\n```\n[[99, 19, 38, 0],\n [-85, -86, -72, 0],\n [11, 31, 97, 0],\n [61, 99, 28, 0],\n [-50, -85, -90, 0],\n [-29, -56, 96, 0],\n [-48, 56, -83, 0],\n [97, -42, 60, 0],\n [-77, 73, 28, 0],\n [41, -92, 27, 0],\n [-34, 82, -58, 0],\n [-81, 37, -93, 0],\n [-96, 6, 11, 0],\n [-93, 66, 88, 0],\n [-35, -84, 77, 0],\n [82, 83, -66, 0],\n [-68, -72, -99, 0],\n [89, -96, -97, 0],\n [84, -92, -46, 0],\n [88, 67, -18, 0],\n [28, 93, 73, 0],\n [-97, -14, -84, 0],\n [97, 15, -61, 0],\n [39, 92, -36, 0],\n [-40, 99, 41, 0],\n [-39, 56, 99, 0],\n [-96, -85, -35, 0],\n [-48, -18, 99, 0],\n [91, 69, -95, 0],\n [-73, 60, -36, 0],\n [-65, -99, -32, 0],\n [100, 4, 65, 0],\n [32, 17, 94, 0],\n [-86, -93, 34, 0],\n [83, 48, -100, 0],\n [75, -75, 100, 0],\n [0, 0, 0, 1]]\n```\nI am happy to work on that if you (Arnaud) want; I didn't figure out why it fails on that example.",
    "created_at": "2008-09-25T23:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This passed all tests, and seems to work well for 3D polytopes, which was the original request.  It does fail for some 4D polytopes, for example for one with vertices:

```
[[99, 19, 38, 0],
 [-85, -86, -72, 0],
 [11, 31, 97, 0],
 [61, 99, 28, 0],
 [-50, -85, -90, 0],
 [-29, -56, 96, 0],
 [-48, 56, -83, 0],
 [97, -42, 60, 0],
 [-77, 73, 28, 0],
 [41, -92, 27, 0],
 [-34, 82, -58, 0],
 [-81, 37, -93, 0],
 [-96, 6, 11, 0],
 [-93, 66, 88, 0],
 [-35, -84, 77, 0],
 [82, 83, -66, 0],
 [-68, -72, -99, 0],
 [89, -96, -97, 0],
 [84, -92, -46, 0],
 [88, 67, -18, 0],
 [28, 93, 73, 0],
 [-97, -14, -84, 0],
 [97, 15, -61, 0],
 [39, 92, -36, 0],
 [-40, 99, 41, 0],
 [-39, 56, 99, 0],
 [-96, -85, -35, 0],
 [-48, -18, 99, 0],
 [91, 69, -95, 0],
 [-73, 60, -36, 0],
 [-65, -99, -32, 0],
 [100, 4, 65, 0],
 [32, 17, 94, 0],
 [-86, -93, 34, 0],
 [83, 48, -100, 0],
 [75, -75, 100, 0],
 [0, 0, 0, 1]]
```
I am happy to work on that if you (Arnaud) want; I didn't figure out why it fails on that example.



---

archive/issue_comments_030169.json:
```json
{
    "body": "First, sorry for the delay, I got swamped with other work to do.\n\nThe failure is due to me (cluelessly) assuming that every vertex is only connected to dim()-1 other vertices.  So basically almost all the other test cases worked by luck.\n\nI think there should be a quick and easy method for 3d polygons to have fast rendering.  \n\nBut I'm still working on the general method and discovering that your example breaks almost all assumptions I had left.  It should work for real after that.",
    "created_at": "2008-09-29T03:40:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30169",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

First, sorry for the delay, I got swamped with other work to do.

The failure is due to me (cluelessly) assuming that every vertex is only connected to dim()-1 other vertices.  So basically almost all the other test cases worked by luck.

I think there should be a quick and easy method for 3d polygons to have fast rendering.  

But I'm still working on the general method and discovering that your example breaks almost all assumptions I had left.  It should work for real after that.



---

archive/issue_comments_030170.json:
```json
{
    "body": "Final version (apply only this)",
    "created_at": "2008-09-29T05:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30170",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Final version (apply only this)



---

archive/issue_comments_030171.json:
```json
{
    "body": "Attachment [trac_4164_final.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_final.patch) by anakha created at 2008-09-29 05:48:19\n\nI now consider the general case to be impossible.  I don't have a formal proof for that though, only experience.  I had almost fixed all of the problems with your 4D example and just to test, tried it with a 5D example.  This broke a lot of things. I kind of realized that even if I managed to fix the 5D case, there would be still more problems in nD (for any n > 5).\n\nSo I restricted the input to polyhedrons of three dimensions or less which works fine and is sensible.  It also fits better with the original function definition which was to produce only triangles.\n\nAny attempt to make a more general version of this should go in a separate ticket/patch and have a different function name.",
    "created_at": "2008-09-29T05:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30171",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Attachment [trac_4164_final.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_final.patch) by anakha created at 2008-09-29 05:48:19

I now consider the general case to be impossible.  I don't have a formal proof for that though, only experience.  I had almost fixed all of the problems with your 4D example and just to test, tried it with a 5D example.  This broke a lot of things. I kind of realized that even if I managed to fix the 5D case, there would be still more problems in nD (for any n > 5).

So I restricted the input to polyhedrons of three dimensions or less which works fine and is sensible.  It also fits better with the original function definition which was to produce only triangles.

Any attempt to make a more general version of this should go in a separate ticket/patch and have a different function name.



---

archive/issue_comments_030172.json:
```json
{
    "body": "Attachment [trac_4164_merge.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_merge.patch) by mhampton created at 2008-09-30 02:48:58\n\nOnly patch needed; merges A.B. and M.H. improvements",
    "created_at": "2008-09-30T02:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_4164_merge.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_merge.patch) by mhampton created at 2008-09-30 02:48:58

Only patch needed; merges A.B. and M.H. improvements



---

archive/issue_comments_030173.json:
```json
{
    "body": "OK, I've combined your code in 3D with my improvements for higher dimensions.  I've also added you (Arnaud) as an author.  I've also based this against 3.1.2, with some improvements related to #4060.  I am putting it all as one patch to make review easier.  Since this is now combined work of me and Arnaud, we need to get another reviewer.",
    "created_at": "2008-09-30T02:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, I've combined your code in 3D with my improvements for higher dimensions.  I've also added you (Arnaud) as an author.  I've also based this against 3.1.2, with some improvements related to #4060.  I am putting it all as one patch to make review easier.  Since this is now combined work of me and Arnaud, we need to get another reviewer.



---

archive/issue_comments_030174.json:
```json
{
    "body": "Attachment [trac_4164_merge2.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_merge2.patch) by mhampton created at 2008-10-07 21:11:30\n\nanother merged contribution; no other patch is necessary",
    "created_at": "2008-10-07T21:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_4164_merge2.patch](tarball://root/attachments/some-uuid/ticket4164/trac_4164_merge2.patch) by mhampton created at 2008-10-07 21:11:30

another merged contribution; no other patch is necessary



---

archive/issue_comments_030175.json:
```json
{
    "body": "Changing component from graphics to geometry.",
    "created_at": "2008-10-16T15:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing component from graphics to geometry.



---

archive/issue_comments_030176.json:
```json
{
    "body": "You can get 2 reviews for 1 by using the patch from #4256.",
    "created_at": "2008-10-16T15:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

You can get 2 reviews for 1 by using the patch from #4256.



---

archive/issue_comments_030177.json:
```json
{
    "body": "Changing keywords from \"\" to \"polyhedra, graphics\".",
    "created_at": "2008-10-16T15:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing keywords from "" to "polyhedra, graphics".



---

archive/issue_events_009459.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-26T01:07:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4164#event-9459"
}
```



---

archive/issue_comments_030178.json:
```json
{
    "body": "Merged in Sage 3.2 via the unified patch at #4256.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T01:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30178",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2 via the unified patch at #4256.

Cheers,

Michael



---

archive/issue_comments_030179.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T01:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30179",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030180.json:
```json
{
    "body": "And since #4256 has a positive review so does this one :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T01:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4164#issuecomment-30180",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And since #4256 has a positive review so does this one :)

Cheers,

Michael
