# Issue 6309: miscellaneous additions to simplicial complex class; clique complex method for graphs

archive/issues_006309.json:
```json
{
    "body": "Assignee: @antieau\n\nFirst, I cached the graph() of a simplicial complex. These get very big and tedious to compute as the complexes get bigger.\n\nI added the method clique_complex to the graph class. This returns the largest simplicial complex whose 1-skeleton is the given graph. Such simplicial complexes are called flag complexes.\n\nI added is_flag_complex, is_connected, and remove_facet methods to the simplicial complex class.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6309\n\n",
    "created_at": "2009-06-16T06:37:33Z",
    "labels": [
        "component: algebraic topology",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "miscellaneous additions to simplicial complex class; clique complex method for graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6309",
    "user": "https://github.com/antieau"
}
```
Assignee: @antieau

First, I cached the graph() of a simplicial complex. These get very big and tedious to compute as the complexes get bigger.

I added the method clique_complex to the graph class. This returns the largest simplicial complex whose 1-skeleton is the given graph. Such simplicial complexes are called flag complexes.

I added is_flag_complex, is_connected, and remove_facet methods to the simplicial complex class.

Issue created by migration from https://trac.sagemath.org/ticket/6309





---

archive/issue_comments_050254.json:
```json
{
    "body": "Attachment [6309.patch](tarball://root/attachments/some-uuid/ticket6309/6309.patch) by @antieau created at 2009-06-16 06:41:40",
    "created_at": "2009-06-16T06:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50254",
    "user": "https://github.com/antieau"
}
```

Attachment [6309.patch](tarball://root/attachments/some-uuid/ticket6309/6309.patch) by @antieau created at 2009-06-16 06:41:40



---

archive/issue_comments_050255.json:
```json
{
    "body": "tweak to be compatibe with #6141, which changes facets to facets().",
    "created_at": "2009-06-17T00:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50255",
    "user": "https://github.com/antieau"
}
```

tweak to be compatibe with #6141, which changes facets to facets().



---

archive/issue_comments_050256.json:
```json
{
    "body": "Attachment [6309-2.patch](tarball://root/attachments/some-uuid/ticket6309/6309-2.patch) by @jhpalmieri created at 2009-06-17 17:19:24\n\nThe patch doesn't apply cleanly; does this depend on #6099?\n\nThe `remove_facet` method needs some doctests.  It also seems to have a line using self.facets, not self.facets().  Would it in fact make sense to just combine this with `remove_face`?  That is, rewrite `remove_face`: first check if the face being removed is a facet, in which case use your code.  Otherwise, use the old, presumably slower, code. I don't think we need two separate methods.  And before removing it, you should probably check that it's actually a facet: make sure it's not a face of any other facet.\n\nSimilarly, the `is_connected` method might fail if the complex was constructed with `maximality_check` False.\n\nYou might check your `is_connected` method for speed -- compare to this:\n\n```\nreturn self.graph().is_connected()\n```\nI expect that yours will be faster, even after the maximality check.  If you keep your code, you could put in a doctest like\n\n```\nsage: K = simplicial_complexes.RandomComplex(8,1)     [or some other simplicial complex]\nsage: K.is_connected() == K.graph().is_connected()\nTrue\n```",
    "created_at": "2009-06-17T17:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50256",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [6309-2.patch](tarball://root/attachments/some-uuid/ticket6309/6309-2.patch) by @jhpalmieri created at 2009-06-17 17:19:24

The patch doesn't apply cleanly; does this depend on #6099?

The `remove_facet` method needs some doctests.  It also seems to have a line using self.facets, not self.facets().  Would it in fact make sense to just combine this with `remove_face`?  That is, rewrite `remove_face`: first check if the face being removed is a facet, in which case use your code.  Otherwise, use the old, presumably slower, code. I don't think we need two separate methods.  And before removing it, you should probably check that it's actually a facet: make sure it's not a face of any other facet.

Similarly, the `is_connected` method might fail if the complex was constructed with `maximality_check` False.

You might check your `is_connected` method for speed -- compare to this:

```
return self.graph().is_connected()
```
I expect that yours will be faster, even after the maximality check.  If you keep your code, you could put in a doctest like

```
sage: K = simplicial_complexes.RandomComplex(8,1)     [or some other simplicial complex]
sage: K.is_connected() == K.graph().is_connected()
True
```



---

archive/issue_comments_050257.json:
```json
{
    "body": "It does not (shouldn't) rely on 6099. It applied cleanly for me to 4.0.2.rc1 once I created the second patch.\n\nI agree with merging remove_facet() with remove_face(). And, I will try to make things robust with the maximality_check=False.\n\nAs for is_connected(), consider the following behavior:\n\n```\nsage: T = SimplicialComplex(5,[[1,2,3],[4]])\nsage: T.graph().is_connected()\nTrue\nsage: T.is_connected()\nFalse\n```\nWhich should be correct?",
    "created_at": "2009-06-17T19:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50257",
    "user": "https://github.com/antieau"
}
```

It does not (shouldn't) rely on 6099. It applied cleanly for me to 4.0.2.rc1 once I created the second patch.

I agree with merging remove_facet() with remove_face(). And, I will try to make things robust with the maximality_check=False.

As for is_connected(), consider the following behavior:

```
sage: T = SimplicialComplex(5,[[1,2,3],[4]])
sage: T.graph().is_connected()
True
sage: T.is_connected()
False
```
Which should be correct?



---

archive/issue_comments_050258.json:
```json
{
    "body": "It looks like there's a bug in the graph method -- it shouldn't ignore isolated vertices.  I'll attach a patch for it.  \n\nWhen I applied the patch, the last part didn't apply because it couldn't find the line\n\n```\n     return SimplicialComplex(sub_vertex_set,faces,maximality_check=True) \n```\nwhich I think is added by #6099.",
    "created_at": "2009-06-17T19:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50258",
    "user": "https://github.com/jhpalmieri"
}
```

It looks like there's a bug in the graph method -- it shouldn't ignore isolated vertices.  I'll attach a patch for it.  

When I applied the patch, the last part didn't apply because it couldn't find the line

```
     return SimplicialComplex(sub_vertex_set,faces,maximality_check=True) 
```
which I think is added by #6099.



---

archive/issue_comments_050259.json:
```json
{
    "body": "Attachment [simp_cx_graph.patch](tarball://root/attachments/some-uuid/ticket6309/simp_cx_graph.patch) by @jhpalmieri created at 2009-06-17 19:40:00",
    "created_at": "2009-06-17T19:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50259",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [simp_cx_graph.patch](tarball://root/attachments/some-uuid/ticket6309/simp_cx_graph.patch) by @jhpalmieri created at 2009-06-17 19:40:00



---

archive/issue_comments_050260.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-06T19:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50260",
    "user": "https://github.com/antieau"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050261.json:
```json
{
    "body": "Attachment [6309-merged.patch](tarball://root/attachments/some-uuid/ticket6309/6309-merged.patch) by @antieau created at 2009-11-06 19:13:40\n\nAdded a hopefully final patch: 6309-merged. This contains the above patches, and merges well on a fresh branch of 4.2.\n\nThe methods graph() and remove_face() now both work correctly. My method for is_connected() was completely wrong. So, for the moment, is_connected() calls graph().is_connected(). This will not give the correct answer for simplicial complexes created with maximal_check=False.\n\nI also updated the changes to graphs/graph.py to reflect the depreciation of the cliques() method.",
    "created_at": "2009-11-06T19:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50261",
    "user": "https://github.com/antieau"
}
```

Attachment [6309-merged.patch](tarball://root/attachments/some-uuid/ticket6309/6309-merged.patch) by @antieau created at 2009-11-06 19:13:40

Added a hopefully final patch: 6309-merged. This contains the above patches, and merges well on a fresh branch of 4.2.

The methods graph() and remove_face() now both work correctly. My method for is_connected() was completely wrong. So, for the moment, is_connected() calls graph().is_connected(). This will not give the correct answer for simplicial complexes created with maximal_check=False.

I also updated the changes to graphs/graph.py to reflect the depreciation of the cliques() method.



---

archive/issue_comments_050262.json:
```json
{
    "body": "Attachment [trac_6309-referee.patch](tarball://root/attachments/some-uuid/ticket6309/trac_6309-referee.patch) by @jhpalmieri created at 2009-11-06 21:09:55\n\napply on top of 6309-merged.patch",
    "created_at": "2009-11-06T21:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50262",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6309-referee.patch](tarball://root/attachments/some-uuid/ticket6309/trac_6309-referee.patch) by @jhpalmieri created at 2009-11-06 21:09:55

apply on top of 6309-merged.patch



---

archive/issue_comments_050263.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T21:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50263",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050264.json:
```json
{
    "body": "Looks good to me.  I'm attaching a referee's patch which fixes a few formatting issues.",
    "created_at": "2009-11-06T21:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50264",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me.  I'm attaching a referee's patch which fixes a few formatting issues.



---

archive/issue_comments_050265.json:
```json
{
    "body": "To the release manager: apply only \"6309-merged.patch\" and \"trac_6309-referee.patch\".",
    "created_at": "2009-11-06T21:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50265",
    "user": "https://github.com/jhpalmieri"
}
```

To the release manager: apply only "6309-merged.patch" and "trac_6309-referee.patch".



---

archive/issue_comments_050266.json:
```json
{
    "body": "Attachment [trac_6309-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket6309/trac_6309-doctest-fix.patch) by @mwhansen created at 2009-11-07 06:12:20",
    "created_at": "2009-11-07T06:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50266",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6309-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket6309/trac_6309-doctest-fix.patch) by @mwhansen created at 2009-11-07 06:12:20



---

archive/issue_comments_050267.json:
```json
{
    "body": "I had to merge the above patch as well since the ordering between Simplex objects and Integer objects seems to vary from machine to machine.",
    "created_at": "2009-11-07T06:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50267",
    "user": "https://github.com/mwhansen"
}
```

I had to merge the above patch as well since the ordering between Simplex objects and Integer objects seems to vary from machine to machine.



---

archive/issue_events_014751.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-07T06:13:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6309#event-14751"
}
```



---

archive/issue_comments_050268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-07T06:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50268",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
