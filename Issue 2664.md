# Issue 2664: [with patch, needs review] implement a symplectic form for finding symplectic bases

archive/issues_002664.json:
```json
{
    "body": "Assignee: was\n\nCC:  ncalexan\n\nKeywords: symplectic basis form integer matrix\n\nImplement a `symplectic_form` for computing symplectic bases for alternating, anti-symmetric matrices.  This is essential for computing with polarized Abelian varieties.\n\nThe attached patch computes symplectic forms over fields and the integers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2664\n\n",
    "created_at": "2008-03-25T19:26:39Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] implement a symplectic form for finding symplectic bases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2664",
    "user": "ncalexan"
}
```
Assignee: was

CC:  ncalexan

Keywords: symplectic basis form integer matrix

Implement a `symplectic_form` for computing symplectic bases for alternating, anti-symmetric matrices.  This is essential for computing with polarized Abelian varieties.

The attached patch computes symplectic forms over fields and the integers.

Issue created by migration from https://trac.sagemath.org/ticket/2664





---

archive/issue_comments_018331.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-25T19:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2664#issuecomment-18331",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_018332.json:
```json
{
    "body": "Patch looks **great**! There are one or two tiny things I'd like to see fixed:\n\n* I don't like the line `alternating_form = symplectic_form`, for the same reasons as my similar comment on #2707.\n\n* Should the new `matrix/symplectic_basis.py` file have a copyright notice at the top?\n\n* Given that there's this nice code for computing symplectic bases, it might be nice for someone to write a `SymplecticSpace` class that inherits from some kind of vector space class, and uses this code behind the scenes where necessary. (Do we already have an inner product space class?) I'm not saying you should implement this right now, of course! But maybe file a trac ticket? Would you use this in what you're doing with this code? (I don't personally have any need of it right now, but it seems like it would be useful in general.)",
    "created_at": "2008-03-28T21:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2664#issuecomment-18332",
    "user": "craigcitro"
}
```

Patch looks **great**! There are one or two tiny things I'd like to see fixed:

* I don't like the line `alternating_form = symplectic_form`, for the same reasons as my similar comment on #2707.

* Should the new `matrix/symplectic_basis.py` file have a copyright notice at the top?

* Given that there's this nice code for computing symplectic bases, it might be nice for someone to write a `SymplecticSpace` class that inherits from some kind of vector space class, and uses this code behind the scenes where necessary. (Do we already have an inner product space class?) I'm not saying you should implement this right now, of course! But maybe file a trac ticket? Would you use this in what you're doing with this code? (I don't personally have any need of it right now, but it seems like it would be useful in general.)



---

archive/issue_comments_018333.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-28T21:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2664#issuecomment-18333",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_018334.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T21:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2664#issuecomment-18334",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_018335.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T21:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2664#issuecomment-18335",
    "user": "mabshoff"
}
```

Resolution: fixed
