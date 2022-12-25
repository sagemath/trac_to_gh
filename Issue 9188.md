# Issue 9188: lattice_polytope.facet_normal bug with polytopes of less that full dimension

archive/issues_009188.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  @novoselt\n\nIn general, `lattice_polytope._embedding_matrix` is not orthogonal. But `facet_normal()` implicitly makes this assumption by embedding the normals (which live in the dual vector space) by the transpose of the `_embedding_matrix`. \n\nHere is an example of the incorrect result:\n\n```\nsage: lp = LatticePolytope(matrix([[1,1,-1,0],[1,-1,-1,0],[1,1,1,0],[3,3,3,0]]))\nsage: lp.vertices()\n[ 1  1 -1  0]\n[ 1 -1 -1  0]\n[ 1  1  1  0]\n[ 3  3  3  0]\nsage: lp.facet_normal(0)\n(-1, 0, 1, 3)\nsage: lp.vertices() * lp.facet_normal(0)\n(-2, -2, 0, 0)\nsage: lp.facet_constant(0)\n-9\n```\n\nIf `lp.facet_normal(0)` would define a facet then its equation would be satisfied at 3 out of 4 vertices. \n\nThe attached patch fixes this issue. A scale factor for the dual embedding is introduced to keep the facet normal coordinates integral. Moreover, a suitable doctest is added.\n\nNOTE: This bug impacts the toric variety code under development in #8986, #8987:\n\n```\nsage: c = Cone([(1,0,0,0),(0,1,0,0),(0,0,1,0)])\nsage: c.faces()\n((0-dimensional face of 3-dimensional cone,), (1-dimensional face of 3-dimensional cone, 1-dimensional face of 3-dimensional cone, 1-dimensional face of 3-dimensional cone), (2-dimensional face of 3-dimensional cone, 2-dimensional face of 3-dimensional cone, 2-dimensional face of 3-dimensional cone), (3-dimensional face of 3-dimensional cone,))\nsage: c = Cone([(1,1,1,3),(1,-1,1,3),(-1,-1,1,3)])\nsage: c.faces()\n((0-dimensional face of 3-dimensional cone,), (2-dimensional face of 3-dimensional cone,), (3-dimensional face of 3-dimensional cone,))\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9188\n\n",
    "created_at": "2010-06-08T10:39:56Z",
    "labels": [
        "component: geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "lattice_polytope.facet_normal bug with polytopes of less that full dimension",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9188",
    "user": "https://github.com/vbraun"
}
```
Assignee: mhampton

CC:  @novoselt

In general, `lattice_polytope._embedding_matrix` is not orthogonal. But `facet_normal()` implicitly makes this assumption by embedding the normals (which live in the dual vector space) by the transpose of the `_embedding_matrix`. 

Here is an example of the incorrect result:

```
sage: lp = LatticePolytope(matrix([[1,1,-1,0],[1,-1,-1,0],[1,1,1,0],[3,3,3,0]]))
sage: lp.vertices()
[ 1  1 -1  0]
[ 1 -1 -1  0]
[ 1  1  1  0]
[ 3  3  3  0]
sage: lp.facet_normal(0)
(-1, 0, 1, 3)
sage: lp.vertices() * lp.facet_normal(0)
(-2, -2, 0, 0)
sage: lp.facet_constant(0)
-9
```

If `lp.facet_normal(0)` would define a facet then its equation would be satisfied at 3 out of 4 vertices. 

The attached patch fixes this issue. A scale factor for the dual embedding is introduced to keep the facet normal coordinates integral. Moreover, a suitable doctest is added.

NOTE: This bug impacts the toric variety code under development in #8986, #8987:

```
sage: c = Cone([(1,0,0,0),(0,1,0,0),(0,0,1,0)])
sage: c.faces()
((0-dimensional face of 3-dimensional cone,), (1-dimensional face of 3-dimensional cone, 1-dimensional face of 3-dimensional cone, 1-dimensional face of 3-dimensional cone), (2-dimensional face of 3-dimensional cone, 2-dimensional face of 3-dimensional cone, 2-dimensional face of 3-dimensional cone), (3-dimensional face of 3-dimensional cone,))
sage: c = Cone([(1,1,1,3),(1,-1,1,3),(-1,-1,1,3)])
sage: c.faces()
((0-dimensional face of 3-dimensional cone,), (2-dimensional face of 3-dimensional cone,), (3-dimensional face of 3-dimensional cone,))
```



Issue created by migration from https://trac.sagemath.org/ticket/9188





---

archive/issue_comments_085836.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-08T10:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85836",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085837.json:
```json
{
    "body": "I missed two doctests that were failing; Some of the old doctests actually did give the wrong facet normals :-) Also, I improved my new doctest to also check the `facet_constant()`.",
    "created_at": "2010-06-08T11:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85837",
    "user": "https://github.com/vbraun"
}
```

I missed two doctests that were failing; Some of the old doctests actually did give the wrong facet normals :-) Also, I improved my new doctest to also check the `facet_constant()`.



---

archive/issue_comments_085838.json:
```json
{
    "body": "Changing assignee from mhampton to @novoselt.",
    "created_at": "2010-06-08T15:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85838",
    "user": "https://github.com/novoselt"
}
```

Changing assignee from mhampton to @novoselt.



---

archive/issue_comments_085839.json:
```json
{
    "body": "This is very embarrassing... Will look over and take care of propagated errors.",
    "created_at": "2010-06-08T15:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85839",
    "user": "https://github.com/novoselt"
}
```

This is very embarrassing... Will look over and take care of propagated errors.



---

archive/issue_comments_085840.json:
```json
{
    "body": "I forgot one more transposition of a matrix %-)  This version should be correct now. Added another doctest.",
    "created_at": "2010-06-08T18:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85840",
    "user": "https://github.com/vbraun"
}
```

I forgot one more transposition of a matrix %-)  This version should be correct now. Added another doctest.



---

archive/issue_comments_085841.json:
```json
{
    "body": "Attachment [trac_9188_fix_facet_normal.patch](tarball://root/attachments/some-uuid/ticket9188/trac_9188_fix_facet_normal.patch) by @vbraun created at 2010-06-08 18:45:30\n\nUpdated patch",
    "created_at": "2010-06-08T18:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85841",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_9188_fix_facet_normal.patch](tarball://root/attachments/some-uuid/ticket9188/trac_9188_fix_facet_normal.patch) by @vbraun created at 2010-06-08 18:45:30

Updated patch



---

archive/issue_comments_085842.json:
```json
{
    "body": "Yeap, the first version was definitely wrong...",
    "created_at": "2010-06-08T18:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85842",
    "user": "https://github.com/novoselt"
}
```

Yeap, the first version was definitely wrong...



---

archive/issue_comments_085843.json:
```json
{
    "body": "Apply on top of the original patch.",
    "created_at": "2010-06-08T20:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85843",
    "user": "https://github.com/novoselt"
}
```

Apply on top of the original patch.



---

archive/issue_comments_085844.json:
```json
{
    "body": "Attachment [trac_9188_fix_facet_normal_reviewer.patch](tarball://root/attachments/some-uuid/ticket9188/trac_9188_fix_facet_normal_reviewer.patch) by @novoselt created at 2010-06-08 20:55:14\n\nOK, my patch looks big, but the only real change to the original is taking the absolute value of the dual scaling factor, so that normals remain inner.\n\nIn addition I (hopefully) made doctests more clear, since they do appear in the documentation. Polytopes are now created using coordinates of points with all the necessary transpositions after that. I also made doctest lines shorter for better looks of the documentation.\n\nI have changed \"parallel\" to \"orthogonal to integer kernel\" in the description of normals (and now I do remember that I didn't like this \"parallel\" when I wrote it...).\n\nIf you are fine with all these changes, I will switch it to positive review. Thank you for catching this bug!",
    "created_at": "2010-06-08T20:55:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85844",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9188_fix_facet_normal_reviewer.patch](tarball://root/attachments/some-uuid/ticket9188/trac_9188_fix_facet_normal_reviewer.patch) by @novoselt created at 2010-06-08 20:55:14

OK, my patch looks big, but the only real change to the original is taking the absolute value of the dual scaling factor, so that normals remain inner.

In addition I (hopefully) made doctests more clear, since they do appear in the documentation. Polytopes are now created using coordinates of points with all the necessary transpositions after that. I also made doctest lines shorter for better looks of the documentation.

I have changed "parallel" to "orthogonal to integer kernel" in the description of normals (and now I do remember that I didn't like this "parallel" when I wrote it...).

If you are fine with all these changes, I will switch it to positive review. Thank you for catching this bug!



---

archive/issue_comments_085845.json:
```json
{
    "body": "Good idea to make sure that the scaling factor is positive. I also like your work on the doctests. Looks good to me!\n\nNote to release manager: apply both patches in order!",
    "created_at": "2010-06-08T21:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85845",
    "user": "https://github.com/vbraun"
}
```

Good idea to make sure that the scaling factor is positive. I also like your work on the doctests. Looks good to me!

Note to release manager: apply both patches in order!



---

archive/issue_comments_085846.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-08T21:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85846",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085847.json:
```json
{
    "body": "Patch at #8986 still applies fine and does not expose any errors in doctests, so let's leave it as is. I will add your example from this ticket into the next patch for #8987 which I am working on now.",
    "created_at": "2010-06-08T21:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85847",
    "user": "https://github.com/novoselt"
}
```

Patch at #8986 still applies fine and does not expose any errors in doctests, so let's leave it as is. I will add your example from this ticket into the next patch for #8987 which I am working on now.



---

archive/issue_comments_085848.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9188#issuecomment-85848",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
