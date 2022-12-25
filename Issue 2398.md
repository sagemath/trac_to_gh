# Issue 2398: free modules over ZZ -- major bug

archive/issues_002398.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nm = lattice_polytope.read_palp_matrix(r\"\"\"4 9\n...    0  0  0  0  0  0  0  0  0\n...    0  3  0 -2  1 -2 -2  1 -2\n...    0  0  3  2  2  5  0  0  3\n...    0  0  0  0  0  0  0  0  0\"\"\")\n\nsage: Ns = (ZZ^4).submodule(m.columns())\nsage: Ns\n\nFree module of degree 4 and rank 2 over Integer Ring\nEchelon basis matrix:\n[0 0 0 0]\n[0 1 0 0]\n```\n\n\nWhat's with the 0 row above?!!?  That's insanely wrong.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2398\n\n",
    "created_at": "2008-03-05T20:23:03Z",
    "labels": [
        "component: linear algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "free modules over ZZ -- major bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2398",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
m = lattice_polytope.read_palp_matrix(r"""4 9
...    0  0  0  0  0  0  0  0  0
...    0  3  0 -2  1 -2 -2  1 -2
...    0  0  3  2  2  5  0  0  3
...    0  0  0  0  0  0  0  0  0""")

sage: Ns = (ZZ^4).submodule(m.columns())
sage: Ns

Free module of degree 4 and rank 2 over Integer Ring
Echelon basis matrix:
[0 0 0 0]
[0 1 0 0]
```


What's with the 0 row above?!!?  That's insanely wrong.

Issue created by migration from https://trac.sagemath.org/ticket/2398





---

archive/issue_comments_016146.json:
```json
{
    "body": "This was reported by Andrej Novoseltsov.",
    "created_at": "2008-03-05T20:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16146",
    "user": "https://github.com/williamstein"
}
```

This was reported by Andrej Novoseltsov.



---

archive/issue_comments_016147.json:
```json
{
    "body": "More interesting data points:\n\n\n```\nsage: (ZZ^4).submodule([(0, 0, 0, 0), (0, 0, 3, 0), (0, -2, 2, 0), (0, 1, 2, 0)])                         \n\nFree module of degree 4 and rank 2 over Integer Ring\nEchelon basis matrix:\n[0 2 1 0]\n[0 3 0 0]\nsage: (ZZ^4).submodule([(0, 0, 3, 0), (0, -2, 2, 0), (0, 1, 2, 0), (0, -2, 5, 0)])\n\nFree module of degree 4 and rank 2 over Integer Ring\nEchelon basis matrix:\n[0 0 0 0]\n[0 1 2 0]\n```\n",
    "created_at": "2008-03-05T23:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16147",
    "user": "https://github.com/jasongrout"
}
```

More interesting data points:


```
sage: (ZZ^4).submodule([(0, 0, 0, 0), (0, 0, 3, 0), (0, -2, 2, 0), (0, 1, 2, 0)])                         

Free module of degree 4 and rank 2 over Integer Ring
Echelon basis matrix:
[0 2 1 0]
[0 3 0 0]
sage: (ZZ^4).submodule([(0, 0, 3, 0), (0, -2, 2, 0), (0, 1, 2, 0), (0, -2, 5, 0)])

Free module of degree 4 and rank 2 over Integer Ring
Echelon basis matrix:
[0 0 0 0]
[0 1 2 0]
```




---

archive/issue_comments_016148.json:
```json
{
    "body": "And more:\n\n\n```\nDoes someone want to review the patch positively?  sage: (ZZ^3).span([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])\n\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[0 0 0]\n[0 1 2]\nsage: matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)]).echelon_form()\n\n[0 0 0]\n[0 1 2]\n[0 0 3]\n[0 0 0]\n```\n\n\nI think the problem is the first row of the matrix is the zero row, which is clearly wrong.",
    "created_at": "2008-03-05T23:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16148",
    "user": "https://github.com/jasongrout"
}
```

And more:


```
Does someone want to review the patch positively?  sage: (ZZ^3).span([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])

Free module of degree 3 and rank 2 over Integer Ring
Echelon basis matrix:
[0 0 0]
[0 1 2]
sage: matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)]).echelon_form()

[0 0 0]
[0 1 2]
[0 0 3]
[0 0 0]
```


I think the problem is the first row of the matrix is the zero row, which is clearly wrong.



---

archive/issue_comments_016149.json:
```json
{
    "body": "Okay, I've traced it back to William's code.  He can take it from there:\n\n\n```\nsage: a=matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])\nsage: import sage.matrix.matrix_integer_dense_hnf             \nsage: sage.matrix.matrix_integer_dense_hnf.hnf(a)             \n\n([0 0 0]\n[0 1 2]\n[0 0 3]\n[0 0 0], [0, 1, 2])\n```\n",
    "created_at": "2008-03-05T23:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16149",
    "user": "https://github.com/jasongrout"
}
```

Okay, I've traced it back to William's code.  He can take it from there:


```
sage: a=matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])
sage: import sage.matrix.matrix_integer_dense_hnf             
sage: sage.matrix.matrix_integer_dense_hnf.hnf(a)             

([0 0 0]
[0 1 2]
[0 0 3]
[0 0 0], [0, 1, 2])
```




---

archive/issue_comments_016150.json:
```json
{
    "body": "Changing the title accordingly.  After fixing this, someone ought to check the first example works correctly.",
    "created_at": "2008-03-05T23:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16150",
    "user": "https://github.com/jasongrout"
}
```

Changing the title accordingly.  After fixing this, someone ought to check the first example works correctly.



---

archive/issue_comments_016151.json:
```json
{
    "body": "I'm changing this to a block -- it gives wrong answers, which is really serious!",
    "created_at": "2008-03-05T23:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16151",
    "user": "https://github.com/williamstein"
}
```

I'm changing this to a block -- it gives wrong answers, which is really serious!



---

archive/issue_comments_016152.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-03-05T23:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16152",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_016153.json:
```json
{
    "body": "this fixes the bug",
    "created_at": "2008-03-06T02:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16153",
    "user": "https://github.com/williamstein"
}
```

this fixes the bug



---

archive/issue_comments_016154.json:
```json
{
    "body": "Attachment [sage-2398.patch](tarball://root/attachments/some-uuid/ticket2398/sage-2398.patch) by @williamstein created at 2008-03-06 02:49:23\n\nI've attached a patch that fixes the problem.  It was actually potentially fairly\nserious, though something one wouldn't see much on \"random\" input.\n\nThe fix involves changing one line (the patch is longer, but only for cosmetic reasons and because of adding a doctest).\n\nI ran the sanity check scripts and this code still works after the patch, by the way.  So that one tiny patch, which is clearly right, doesn't break things.",
    "created_at": "2008-03-06T02:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16154",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2398.patch](tarball://root/attachments/some-uuid/ticket2398/sage-2398.patch) by @williamstein created at 2008-03-06 02:49:23

I've attached a patch that fixes the problem.  It was actually potentially fairly
serious, though something one wouldn't see much on "random" input.

The fix involves changing one line (the patch is longer, but only for cosmetic reasons and because of adding a doctest).

I ran the sanity check scripts and this code still works after the patch, by the way.  So that one tiny patch, which is clearly right, doesn't break things.



---

archive/issue_comments_016155.json:
```json
{
    "body": "The patch fixes all of the above examples (and includes the minimal example as a doctest).  It looks good to me.",
    "created_at": "2008-03-06T03:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16155",
    "user": "https://github.com/jasongrout"
}
```

The patch fixes all of the above examples (and includes the minimal example as a doctest).  It looks good to me.



---

archive/issue_comments_016156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-07T04:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016157.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc3",
    "created_at": "2008-03-07T04:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc3
