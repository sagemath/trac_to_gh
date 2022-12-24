# Issue 4256: [with patch, needs review] polyhedral improvements: Schlegel diagrams, standard 4d polytopes

archive/issues_004256.json:
```json
{
    "body": "Assignee: mhampton\n\nCC:  anakha\n\nKeywords: polytopes, geometry\n\nThis patch adds Schlegel diagrams for 4d polytopes (via the render_wireframe function), as well as built-in definitions of the 24-cell and 600-cell.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4256\n\n",
    "created_at": "2008-10-09T18:49:18Z",
    "labels": [
        "geometry",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] polyhedral improvements: Schlegel diagrams, standard 4d polytopes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4256",
    "user": "mhampton"
}
```
Assignee: mhampton

CC:  anakha

Keywords: polytopes, geometry

This patch adds Schlegel diagrams for 4d polytopes (via the render_wireframe function), as well as built-in definitions of the 24-cell and 600-cell.

Issue created by migration from https://trac.sagemath.org/ticket/4256





---

archive/issue_comments_030970.json:
```json
{
    "body": "apply versus 3.1.2; conflicts with #4164 patches",
    "created_at": "2008-10-09T18:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30970",
    "user": "mhampton"
}
```

apply versus 3.1.2; conflicts with #4164 patches



---

archive/issue_comments_030971.json:
```json
{
    "body": "Attachment [trac_4256_v2.patch](tarball://root/attachments/some-uuid/ticket4256/trac_4256_v2.patch) by mhampton created at 2008-10-15 23:02:12\n\nApply to a vanilla 3.1.2 or 3.1.3; supercedes previous patch",
    "created_at": "2008-10-15T23:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30971",
    "user": "mhampton"
}
```

Attachment [trac_4256_v2.patch](tarball://root/attachments/some-uuid/ticket4256/trac_4256_v2.patch) by mhampton created at 2008-10-15 23:02:12

Apply to a vanilla 3.1.2 or 3.1.3; supercedes previous patch



---

archive/issue_comments_030972.json:
```json
{
    "body": "This adds several enhancements such as Schegel diagrams, scalar dilation of polytopes, translation by a vector, built-in regular polytopes such as the 24-cell and cross-polytopes, and generation of polar duals.  To make it easier to review this patch includes changes from #4164, so you just need one patch.",
    "created_at": "2008-10-15T23:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30972",
    "user": "mhampton"
}
```

This adds several enhancements such as Schegel diagrams, scalar dilation of polytopes, translation by a vector, built-in regular polytopes such as the 24-cell and cross-polytopes, and generation of polar duals.  To make it easier to review this patch includes changes from #4164, so you just need one patch.



---

archive/issue_comments_030973.json:
```json
{
    "body": "improved and re-based against 3.1.4",
    "created_at": "2008-10-21T21:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30973",
    "user": "mhampton"
}
```

improved and re-based against 3.1.4



---

archive/issue_comments_030974.json:
```json
{
    "body": "Attachment [trac_4256_v3.patch](tarball://root/attachments/some-uuid/ticket4256/trac_4256_v3.patch) by mhampton created at 2008-10-21 21:50:10\n\nThe trac_4256_v3.patch also incorporates the changes in #4164.  Polyhedra can now be multiplied, scaled, translated, and the polar (dual) constructed.  Several standard polytope families have been added.",
    "created_at": "2008-10-21T21:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30974",
    "user": "mhampton"
}
```

Attachment [trac_4256_v3.patch](tarball://root/attachments/some-uuid/ticket4256/trac_4256_v3.patch) by mhampton created at 2008-10-21 21:50:10

The trac_4256_v3.patch also incorporates the changes in #4164.  Polyhedra can now be multiplied, scaled, translated, and the polar (dual) constructed.  Several standard polytope families have been added.



---

archive/issue_comments_030975.json:
```json
{
    "body": "The ambient_dim function overwrites the content self._dim thus making dim() return a wrong answer:\n\n\n```\nsage: p = Polyhedron(vertices = [[0,0,1]])\nsage: p.dim()\n0\nsage: p.ambiant_dim()\n3\nsage: p.dim()\n3\n```\n\n\nIn the vertex_adjacency_matrix() docstring, maybe you should use 'binary' rather than '0/1'\n\nIn render_solid(), since you now have ambient_dim(), why not use it?  It could replace the ugly test I put there.\n\nAlso for the 'special' polyhedron creation methods, it could be good to reuse the approach taken for graphs, where you have the Graph class and an instance of a special class called graphs where you have building methods for most interesting types of graphs.\n\nThe first item is a must-fix, the other three would be nice, but are not stricly essential.",
    "created_at": "2008-10-23T02:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30975",
    "user": "anakha"
}
```

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

archive/issue_comments_030976.json:
```json
{
    "body": "supercedes previous patches, addresses review",
    "created_at": "2008-10-24T04:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30976",
    "user": "mhampton"
}
```

supercedes previous patches, addresses review



---

archive/issue_comments_030977.json:
```json
{
    "body": "Attachment [trac_4256_v4.patch](tarball://root/attachments/some-uuid/ticket4256/trac_4256_v4.patch) by mhampton created at 2008-10-24 04:05:35",
    "created_at": "2008-10-24T04:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30977",
    "user": "mhampton"
}
```

Attachment [trac_4256_v4.patch](tarball://root/attachments/some-uuid/ticket4256/trac_4256_v4.patch) by mhampton created at 2008-10-24 04:05:35



---

archive/issue_comments_030978.json:
```json
{
    "body": "The only thing left to do is to mark the lrs_volume() tests as optional.  I forgot that in my initial review.\n\nAnyway, apart from that, positive review",
    "created_at": "2008-10-24T16:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30978",
    "user": "anakha"
}
```

The only thing left to do is to mark the lrs_volume() tests as optional.  I forgot that in my initial review.

Anyway, apart from that, positive review



---

archive/issue_comments_030979.json:
```json
{
    "body": "Attachment [4256_v5.patch](tarball://root/attachments/some-uuid/ticket4256/4256_v5.patch) by mhampton created at 2008-10-24 19:06:21\n\nsupercedes previous patches, addresses final review (optional tests)",
    "created_at": "2008-10-24T19:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30979",
    "user": "mhampton"
}
```

Attachment [4256_v5.patch](tarball://root/attachments/some-uuid/ticket4256/4256_v5.patch) by mhampton created at 2008-10-24 19:06:21

supercedes previous patches, addresses final review (optional tests)



---

archive/issue_comments_030980.json:
```json
{
    "body": "OK, I made the lrs_volume tests optional.  Thanks very much for reviewing this.",
    "created_at": "2008-10-24T19:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30980",
    "user": "mhampton"
}
```

OK, I made the lrs_volume tests optional.  Thanks very much for reviewing this.



---

archive/issue_comments_030981.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T01:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30981",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030982.json:
```json
{
    "body": "Merged 4256_v5.patch in Sage 3.2.alpha1",
    "created_at": "2008-10-26T01:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4256#issuecomment-30982",
    "user": "mabshoff"
}
```

Merged 4256_v5.patch in Sage 3.2.alpha1
