# Issue 5117: remove (or enhance an rename) the Polyhedron.union()) method

archive/issues_005117.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  mhampton @vbraun\n\nThe Polyhedron class (in the polyhedra module) has a union method\n\n```\ndef union(self, other):\n    \"\"\"\n    Returns a polyhedron whose vertices are the union of the vertices\n    of the two polyhedra.\n    ....\n```\nThe name is misleading as the method does not return the union of `self` and `other` (which would not be a convex polyhedron).\n\nThe method should then be removed or renamed. As the method itself consists in one single line of code (and as I have no idea of a proper name), I would tend to remove it.\n\nThe attached patch removes it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5117\n\n",
    "created_at": "2009-01-28T13:00:55Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "remove (or enhance an rename) the Polyhedron.union()) method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5117",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```
Assignee: mhampton

CC:  mhampton @vbraun

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

Issue created by migration from https://trac.sagemath.org/ticket/5117





---

archive/issue_comments_039033.json:
```json
{
    "body": "patch that removes the union method",
    "created_at": "2009-01-28T13:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39033",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```

patch that removes the union method



---

archive/issue_comments_039034.json:
```json
{
    "body": "Attachment [remove_union.diff](tarball://root/attachments/some-uuid/ticket5117/remove_union.diff) by mhampton created at 2009-01-28 16:01:07\n\nI disagree that this should be removed.  I created it because I use it!\n\nI think the docstring makes it pretty clear what it does, but I do not object to renaming it.  Perhaps union_of_vertices? Or union_by_vertices?\n\nMarshall",
    "created_at": "2009-01-28T16:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39034",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [remove_union.diff](tarball://root/attachments/some-uuid/ticket5117/remove_union.diff) by mhampton created at 2009-01-28 16:01:07

I disagree that this should be removed.  I created it because I use it!

I think the docstring makes it pretty clear what it does, but I do not object to renaming it.  Perhaps union_of_vertices? Or union_by_vertices?

Marshall



---

archive/issue_comments_039035.json:
```json
{
    "body": "Replying to [comment:1 mhampton]:\n> I disagree that this should be removed.  I created it because I use it!\n\n\nusing \n\n```\np = Polyhedron(p1.vertices() + p2.vertices())\n```\ninstead of\n\n```\np = p1.union(p2)\n```\ndoes not make a big difference ;)\n\n> I think the docstring makes it pretty clear what it does,\n\nagreed\n\n> but I do not object to renaming it.  Perhaps union_of_vertices? Or union_by_vertices?\n\n\nwhat about extending ot to handle unbounded polyhedra as well in this way:\n\n```\np = Polyhedron(p1.vertices() + p2.vertices(), p1.rays() + p2.rays())\n```\nWe could then name it convex_hull() or something like that?\n\n-- \nSebastien",
    "created_at": "2009-01-28T16:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39035",
    "user": "https://trac.sagemath.org/admin/accounts/users/sbarthelemy"
}
```

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

archive/issue_comments_039036.json:
```json
{
    "body": "Renaming in convex_hull is fine with me.  The extension to rays is a good idea.",
    "created_at": "2009-01-28T16:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39036",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Renaming in convex_hull is fine with me.  The extension to rays is a good idea.



---

archive/issue_events_011834.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T07:04:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5117#event-11834"
}
```



---

archive/issue_comments_039037.json:
```json
{
    "body": "Current version is doing this:\n\n```\nnew_vertices = self.vertices() + other.vertices()\nnew_rays = self.rays() + other.rays()\nnew_lines = self.lines() + other.lines()\nreturn Polyhedron(vertices=new_vertices,\n                      rays=new_rays, lines=new_lines, field=self.field())\n\n```\nwhich is great, but I STRONGLY support the idea of renaming the method to something else.\n\nI was once working with an algorithm where the *union* of polytopes was used, but I interpreted it exactly as the convex hull and of course got wrong results. I was not using this function, that was my own mistake, but since it is so easy to do, I don't think there should be an extra opportunity for confusion. I agree, that the result is described in the documentation, but I don't always read it for \"obvious\" functions and perhaps there are other users like me.\n\nHow about \"extend\"? \"convex_hull\" is also great, although it seems more natural to me to have a global function with such a name called like\n\n```\nconvex_hull(polyhedron1, polyhedron2, polyhedron3, ...)\n```\n(There is a function with this name in lattice_polytope which works with points and thinking about it now I suspect that I have chosen not the best name for it either... At least it is not imported into global namespace...)",
    "created_at": "2010-04-03T15:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39037",
    "user": "https://github.com/novoselt"
}
```

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

archive/issue_comments_039038.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-04-03T15:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39038",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_039039.json:
```json
{
    "body": "So we could make a convex_hull method and deprecate the union function.  To make a union function in the sense that you and sbarthelemy want, I think we need to make some sort of PolyhedralUnion class to do computations on such objects.",
    "created_at": "2010-04-03T19:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39039",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

So we could make a convex_hull method and deprecate the union function.  To make a union function in the sense that you and sbarthelemy want, I think we need to make some sort of PolyhedralUnion class to do computations on such objects.



---

archive/issue_comments_039040.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-09T14:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39040",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_039041.json:
```json
{
    "body": "Patch renames `self.union()` to `self.convex_hull()` and improves the handling of the underlying field for various operations, for example\n\n```\nsage: triangle = Polyhedron(vertices=[[1,0],[0,1],[-1,-1]])\nsage: (1 * triangle).field()\nRational Field\nsage: (1.0 * triangle).field()\nReal Double Field\n```",
    "created_at": "2010-05-09T14:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39041",
    "user": "https://github.com/vbraun"
}
```

Patch renames `self.union()` to `self.convex_hull()` and improves the handling of the underlying field for various operations, for example

```
sage: triangle = Polyhedron(vertices=[[1,0],[0,1],[-1,-1]])
sage: (1 * triangle).field()
Rational Field
sage: (1.0 * triangle).field()
Real Double Field
```



---

archive/issue_comments_039042.json:
```json
{
    "body": "Attachment [14261.patch](tarball://root/attachments/some-uuid/ticket5117/14261.patch) by @vbraun created at 2010-05-09 14:13:09",
    "created_at": "2010-05-09T14:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39042",
    "user": "https://github.com/vbraun"
}
```

Attachment [14261.patch](tarball://root/attachments/some-uuid/ticket5117/14261.patch) by @vbraun created at 2010-05-09 14:13:09



---

archive/issue_comments_039043.json:
```json
{
    "body": "Apply this patch first",
    "created_at": "2010-05-09T15:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39043",
    "user": "https://github.com/novoselt"
}
```

Apply this patch first



---

archive/issue_comments_039044.json:
```json
{
    "body": "Attachment [trac_5117_rename_union_to_convex_hull_add_coerce_field_for polyhedra.patch](tarball://root/attachments/some-uuid/ticket5117/trac_5117_rename_union_to_convex_hull_add_coerce_field_for polyhedra.patch) by @novoselt created at 2010-05-09 15:40:00\n\nApply this patch second (and last)",
    "created_at": "2010-05-09T15:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39044",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_5117_rename_union_to_convex_hull_add_coerce_field_for polyhedra.patch](tarball://root/attachments/some-uuid/ticket5117/trac_5117_rename_union_to_convex_hull_add_coerce_field_for polyhedra.patch) by @novoselt created at 2010-05-09 15:40:00

Apply this patch second (and last)



---

archive/issue_comments_039045.json:
```json
{
    "body": "Attachment [trac_5117_reviewer_docfixes.patch](tarball://root/attachments/some-uuid/ticket5117/trac_5117_reviewer_docfixes.patch) by @novoselt created at 2010-05-09 15:45:03\n\nLooks good to me. I have renamed the original patch file to include the ticket number and its description. On top of that I have made the documentation look nicer and added a message to the TyperError exception. Passes all doctests, so I am giving this a positive review.\n\nMy only concern is whether or not we need to use some framework for deprecating functions or what is done for \"union\" is enough.",
    "created_at": "2010-05-09T15:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39045",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_5117_reviewer_docfixes.patch](tarball://root/attachments/some-uuid/ticket5117/trac_5117_reviewer_docfixes.patch) by @novoselt created at 2010-05-09 15:45:03

Looks good to me. I have renamed the original patch file to include the ticket number and its description. On top of that I have made the documentation look nicer and added a message to the TyperError exception. Passes all doctests, so I am giving this a positive review.

My only concern is whether or not we need to use some framework for deprecating functions or what is done for "union" is enough.



---

archive/issue_comments_039046.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-09T15:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39046",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_011835.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-09T02:19:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5117#event-11835"
}
```



---

archive/issue_comments_039047.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T02:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5117#issuecomment-39047",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
