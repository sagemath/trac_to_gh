# Issue 2398: free modules over ZZ -- major bug

archive/issues_002398.json:
```json
{
    "body": "Assignee: was\n\n\n```\nm = lattice_polytope.read_palp_matrix(r\"\"\"4 9\n...    0  0  0  0  0  0  0  0  0\n...    0  3  0 -2  1 -2 -2  1 -2\n...    0  0  3  2  2  5  0  0  3\n...    0  0  0  0  0  0  0  0  0\"\"\")\n\nsage: Ns = (ZZ^4).submodule(m.columns())\nsage: Ns\n\nFree module of degree 4 and rank 2 over Integer Ring\nEchelon basis matrix:\n[0 0 0 0]\n[0 1 0 0]\n```\n\n\nWhat's with the 0 row above?!!?  That's insanely wrong.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2398\n\n",
    "created_at": "2008-03-05T20:23:03Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "title": "free modules over ZZ -- major bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2398",
    "user": "was"
}
```
Assignee: was


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

archive/issue_comments_016181.json:
```json
{
    "body": "This was reported by Andrej Novoseltsov.",
    "created_at": "2008-03-05T20:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16181",
    "user": "was"
}
```

This was reported by Andrej Novoseltsov.



---

archive/issue_comments_016182.json:
```json
{
    "body": "More interesting data points:\n\n\n```\nsage: (ZZ^4).submodule([(0, 0, 0, 0), (0, 0, 3, 0), (0, -2, 2, 0), (0, 1, 2, 0)])                         \n\nFree module of degree 4 and rank 2 over Integer Ring\nEchelon basis matrix:\n[0 2 1 0]\n[0 3 0 0]\nsage: (ZZ^4).submodule([(0, 0, 3, 0), (0, -2, 2, 0), (0, 1, 2, 0), (0, -2, 5, 0)])\n\nFree module of degree 4 and rank 2 over Integer Ring\nEchelon basis matrix:\n[0 0 0 0]\n[0 1 2 0]\n```\n",
    "created_at": "2008-03-05T23:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16182",
    "user": "jason"
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

archive/issue_comments_016183.json:
```json
{
    "body": "And more:\n\n\n```\nDoes someone want to review the patch positively?  sage: (ZZ^3).span([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])\n\nFree module of degree 3 and rank 2 over Integer Ring\nEchelon basis matrix:\n[0 0 0]\n[0 1 2]\nsage: matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)]).echelon_form()\n\n[0 0 0]\n[0 1 2]\n[0 0 3]\n[0 0 0]\n```\n\n\nI think the problem is the first row of the matrix is the zero row, which is clearly wrong.",
    "created_at": "2008-03-05T23:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16183",
    "user": "jason"
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

archive/issue_comments_016184.json:
```json
{
    "body": "Okay, I've traced it back to William's code.  He can take it from there:\n\n\n```\nsage: a=matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])\nsage: import sage.matrix.matrix_integer_dense_hnf             \nsage: sage.matrix.matrix_integer_dense_hnf.hnf(a)             \n\n([0 0 0]\n[0 1 2]\n[0 0 3]\n[0 0 0], [0, 1, 2])\n```\n",
    "created_at": "2008-03-05T23:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16184",
    "user": "jason"
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

archive/issue_comments_016185.json:
```json
{
    "body": "Changing the title accordingly.  After fixing this, someone ought to check the first example works correctly.",
    "created_at": "2008-03-05T23:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16185",
    "user": "jason"
}
```

Changing the title accordingly.  After fixing this, someone ought to check the first example works correctly.



---

archive/issue_comments_016186.json:
```json
{
    "body": "I'm changing this to a block -- it gives wrong answers, which is really serious!",
    "created_at": "2008-03-05T23:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16186",
    "user": "was"
}
```

I'm changing this to a block -- it gives wrong answers, which is really serious!



---

archive/issue_comments_016187.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-03-05T23:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16187",
    "user": "was"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_016188.json:
```json
{
    "body": "this fixes the bug",
    "created_at": "2008-03-06T02:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16188",
    "user": "was"
}
```

this fixes the bug



---

archive/issue_comments_016189.json:
```json
{
    "body": "Attachment [sage-2398.patch](tarball://root/attachments/some-uuid/ticket2398/sage-2398.patch) by was created at 2008-03-06 02:49:23\n\nI've attached a patch that fixes the problem.  It was actually potentially fairly\nserious, though something one wouldn't see much on \"random\" input.\n\nThe fix involves changing one line (the patch is longer, but only for cosmetic reasons and because of adding a doctest).\n\nI ran the sanity check scripts and this code still works after the patch, by the way.  So that one tiny patch, which is clearly right, doesn't break things.",
    "created_at": "2008-03-06T02:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16189",
    "user": "was"
}
```

Attachment [sage-2398.patch](tarball://root/attachments/some-uuid/ticket2398/sage-2398.patch) by was created at 2008-03-06 02:49:23

I've attached a patch that fixes the problem.  It was actually potentially fairly
serious, though something one wouldn't see much on "random" input.

The fix involves changing one line (the patch is longer, but only for cosmetic reasons and because of adding a doctest).

I ran the sanity check scripts and this code still works after the patch, by the way.  So that one tiny patch, which is clearly right, doesn't break things.



---

archive/issue_comments_016190.json:
```json
{
    "body": "The patch fixes all of the above examples (and includes the minimal example as a doctest).  It looks good to me.",
    "created_at": "2008-03-06T03:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16190",
    "user": "jason"
}
```

The patch fixes all of the above examples (and includes the minimal example as a doctest).  It looks good to me.



---

archive/issue_comments_016191.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-07T04:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16191",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016192.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc3",
    "created_at": "2008-03-07T04:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2398#issuecomment-16192",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc3
