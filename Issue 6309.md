# Issue 6309: miscellaneous additions to simplicial complex class; clique complex method for graphs

archive/issues_006309.json:
```json
{
    "body": "Assignee: bantieau\n\nFirst, I cached the graph() of a simplicial complex. These get very big and tedious to compute as the complexes get bigger.\n\nI added the method clique_complex to the graph class. This returns the largest simplicial complex whose 1-skeleton is the given graph. Such simplicial complexes are called flag complexes.\n\nI added is_flag_complex, is_connected, and remove_facet methods to the simplicial complex class.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6309\n\n",
    "created_at": "2009-06-16T06:37:33Z",
    "labels": [
        "algebraic topology",
        "minor",
        "enhancement"
    ],
    "title": "miscellaneous additions to simplicial complex class; clique complex method for graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6309",
    "user": "bantieau"
}
```
Assignee: bantieau

First, I cached the graph() of a simplicial complex. These get very big and tedious to compute as the complexes get bigger.

I added the method clique_complex to the graph class. This returns the largest simplicial complex whose 1-skeleton is the given graph. Such simplicial complexes are called flag complexes.

I added is_flag_complex, is_connected, and remove_facet methods to the simplicial complex class.

Issue created by migration from https://trac.sagemath.org/ticket/6309





---

archive/issue_comments_050350.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-16T06:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50350",
    "user": "bantieau"
}
```

Attachment



---

archive/issue_comments_050351.json:
```json
{
    "body": "tweak to be compatibe with #6141, which changes facets to facets().",
    "created_at": "2009-06-17T00:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50351",
    "user": "bantieau"
}
```

tweak to be compatibe with #6141, which changes facets to facets().



---

archive/issue_comments_050352.json:
```json
{
    "body": "Attachment\n\nThe patch doesn't apply cleanly; does this depend on #6099?\n\nThe `remove_facet` method needs some doctests.  It also seems to have a line using self.facets, not self.facets().  Would it in fact make sense to just combine this with `remove_face`?  That is, rewrite `remove_face`: first check if the face being removed is a facet, in which case use your code.  Otherwise, use the old, presumably slower, code. I don't think we need two separate methods.  And before removing it, you should probably check that it's actually a facet: make sure it's not a face of any other facet.\n\nSimilarly, the `is_connected` method might fail if the complex was constructed with `maximality_check` False.\n\nYou might check your `is_connected` method for speed -- compare to this:\n\n```\nreturn self.graph().is_connected()\n```\n\nI expect that yours will be faster, even after the maximality check.  If you keep your code, you could put in a doctest like\n\n```\nsage: K = simplicial_complexes.RandomComplex(8,1)     [or some other simplicial complex]\nsage: K.is_connected() == K.graph().is_connected()\nTrue\n```\n",
    "created_at": "2009-06-17T17:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50352",
    "user": "jhpalmieri"
}
```

Attachment

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

archive/issue_comments_050353.json:
```json
{
    "body": "It does not (shouldn't) rely on 6099. It applied cleanly for me to 4.0.2.rc1 once I created the second patch.\n\nI agree with merging remove_facet() with remove_face(). And, I will try to make things robust with the maximality_check=False.\n\nAs for is_connected(), consider the following behavior:\n\n```\nsage: T = SimplicialComplex(5,[[1,2,3],[4]])\nsage: T.graph().is_connected()\nTrue\nsage: T.is_connected()\nFalse\n```\n\nWhich should be correct?",
    "created_at": "2009-06-17T19:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50353",
    "user": "bantieau"
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

archive/issue_comments_050354.json:
```json
{
    "body": "It looks like there's a bug in the graph method -- it shouldn't ignore isolated vertices.  I'll attach a patch for it.  \n\nWhen I applied the patch, the last part didn't apply because it couldn't find the line\n\n```\n     return SimplicialComplex(sub_vertex_set,faces,maximality_check=True) \n```\n\nwhich I think is added by #6099.",
    "created_at": "2009-06-17T19:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50354",
    "user": "jhpalmieri"
}
```

It looks like there's a bug in the graph method -- it shouldn't ignore isolated vertices.  I'll attach a patch for it.  

When I applied the patch, the last part didn't apply because it couldn't find the line

```
     return SimplicialComplex(sub_vertex_set,faces,maximality_check=True) 
```

which I think is added by #6099.



---

archive/issue_comments_050355.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-17T19:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50355",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_050356.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-06T19:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50356",
    "user": "bantieau"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050357.json:
```json
{
    "body": "Attachment\n\nAdded a hopefully final patch: 6309-merged. This contains the above patches, and merges well on a fresh branch of 4.2.\n\nThe methods graph() and remove_face() now both work correctly. My method for is_connected() was completely wrong. So, for the moment, is_connected() calls graph().is_connected(). This will not give the correct answer for simplicial complexes created with maximal_check=False.\n\nI also updated the changes to graphs/graph.py to reflect the depreciation of the cliques() method.",
    "created_at": "2009-11-06T19:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50357",
    "user": "bantieau"
}
```

Attachment

Added a hopefully final patch: 6309-merged. This contains the above patches, and merges well on a fresh branch of 4.2.

The methods graph() and remove_face() now both work correctly. My method for is_connected() was completely wrong. So, for the moment, is_connected() calls graph().is_connected(). This will not give the correct answer for simplicial complexes created with maximal_check=False.

I also updated the changes to graphs/graph.py to reflect the depreciation of the cliques() method.



---

archive/issue_comments_050358.json:
```json
{
    "body": "Attachment\n\napply on top of 6309-merged.patch",
    "created_at": "2009-11-06T21:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50358",
    "user": "jhpalmieri"
}
```

Attachment

apply on top of 6309-merged.patch



---

archive/issue_comments_050359.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T21:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50359",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050360.json:
```json
{
    "body": "Looks good to me.  I'm attaching a referee's patch which fixes a few formatting issues.",
    "created_at": "2009-11-06T21:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50360",
    "user": "jhpalmieri"
}
```

Looks good to me.  I'm attaching a referee's patch which fixes a few formatting issues.



---

archive/issue_comments_050361.json:
```json
{
    "body": "To the release manager: apply only \"6309-merged.patch\" and \"trac_6309-referee.patch\".",
    "created_at": "2009-11-06T21:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50361",
    "user": "jhpalmieri"
}
```

To the release manager: apply only "6309-merged.patch" and "trac_6309-referee.patch".



---

archive/issue_comments_050362.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-07T06:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50362",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_050363.json:
```json
{
    "body": "I had to merge the above patch as well since the ordering between Simplex objects and Integer objects seems to vary from machine to machine.",
    "created_at": "2009-11-07T06:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50363",
    "user": "mhansen"
}
```

I had to merge the above patch as well since the ordering between Simplex objects and Integer objects seems to vary from machine to machine.



---

archive/issue_comments_050364.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-07T06:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6309#issuecomment-50364",
    "user": "mhansen"
}
```

Resolution: fixed
