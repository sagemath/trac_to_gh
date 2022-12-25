# Issue 3023: make apply_map deal with empty matrices

archive/issues_003023.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: m=matrix([])\nsage: m.apply_map?\nsage: m.apply_map(lambda x: x)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/grout/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()\n\n/home/grout/sage/devel/sage-main/sage/matrix/matrix_dense.pyx in sage.matrix.matrix_dense.Matrix_dense.apply_map (sage/matrix/matrix_dense.c:3098)()\n    307             v = sage.structure.sequence.Sequence(v)\n    308             R = v.universe()\n--> 309         M = sage.matrix.matrix_space.MatrixSpace(R, self._nrows,\n    310                    self._ncols, sparse=False)\n    311         image = M(v)\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in MatrixSpace(base_ring, nrows, ncols, sparse)\n    171     \"\"\"\n    172     if not sage.rings.ring.is_Ring(base_ring):\n--> 173         raise TypeError, \"base_ring (=%s) must be a ring\"%base_ring\n    174\n    175     if ncols is None: ncols = nrows\n\n<type 'exceptions.TypeError'>: base_ring (=Category of objects) must be a ring\n```\n\n\nm.apply_map(blah) should return an empty matrix in this case.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3023\n\n",
    "created_at": "2008-04-25T16:47:26Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "make apply_map deal with empty matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3023",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein


```
sage: m=matrix([])
sage: m.apply_map?
sage: m.apply_map(lambda x: x)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()

/home/grout/sage/devel/sage-main/sage/matrix/matrix_dense.pyx in sage.matrix.matrix_dense.Matrix_dense.apply_map (sage/matrix/matrix_dense.c:3098)()
    307             v = sage.structure.sequence.Sequence(v)
    308             R = v.universe()
--> 309         M = sage.matrix.matrix_space.MatrixSpace(R, self._nrows,
    310                    self._ncols, sparse=False)
    311         image = M(v)

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in MatrixSpace(base_ring, nrows, ncols, sparse)
    171     """
    172     if not sage.rings.ring.is_Ring(base_ring):
--> 173         raise TypeError, "base_ring (=%s) must be a ring"%base_ring
    174
    175     if ncols is None: ncols = nrows

<type 'exceptions.TypeError'>: base_ring (=Category of objects) must be a ring
```


m.apply_map(blah) should return an empty matrix in this case.

Issue created by migration from https://trac.sagemath.org/ticket/3023





---

archive/issue_comments_020750.json:
```json
{
    "body": "Attachment [trac-3023-matrix-applymap-empty.patch](tarball://root/attachments/some-uuid/ticket3023/trac-3023-matrix-applymap-empty.patch) by @jasongrout created at 2008-04-25 16:51:30\n\ndoctests in the matrix/ directory pass with the above patch.",
    "created_at": "2008-04-25T16:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3023#issuecomment-20750",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-3023-matrix-applymap-empty.patch](tarball://root/attachments/some-uuid/ticket3023/trac-3023-matrix-applymap-empty.patch) by @jasongrout created at 2008-04-25 16:51:30

doctests in the matrix/ directory pass with the above patch.



---

archive/issue_comments_020751.json:
```json
{
    "body": "\n```\n[19:04] <mabshoff> so, what is the verdict on #3023?\n[19:04] <jason> positive review from me :)  I don't think that counts, though\n[19:05] <mabshoff> Well, as author it is expected that you think your patch it a good idea.\n[19:05] <mabshoff> It seems like the sensible thing to do.\n[19:07] <dfdeshom> running testall now, but positive review from me\n[19:08] <dfdeshom> (and i'll put it in writing when the tests finish)\n```\n",
    "created_at": "2008-04-25T18:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3023#issuecomment-20751",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[19:04] <mabshoff> so, what is the verdict on #3023?
[19:04] <jason> positive review from me :)  I don't think that counts, though
[19:05] <mabshoff> Well, as author it is expected that you think your patch it a good idea.
[19:05] <mabshoff> It seems like the sensible thing to do.
[19:07] <dfdeshom> running testall now, but positive review from me
[19:08] <dfdeshom> (and i'll put it in writing when the tests finish)
```




---

archive/issue_comments_020752.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-25T18:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3023#issuecomment-20752",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020753.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-25T18:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3023#issuecomment-20753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha0
