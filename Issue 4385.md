# Issue 4385: Sage 3.1.4: optional doctest failure in sage/rings/polynomial/multi_polynomial.pyx

archive/issues_004385.json:
```json
{
    "body": "Assignee: mhampton\n\n\n```\nsage -t -long -optional devel/sage/sage/rings/polynomial/multi_polynomial.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/multi_polynomial.py\", line 712:\n    sage: P\nExpected:\n    A Polyhedron with 4 vertices.\nGot:\n    A Polyhedron with 3 vertices.\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/multi_polynomial.py\", line 721:\n    sage: R(1).newton_polytope()\nExpected:\n    A Polyhedron with 1 vertices.\nGot:\n    A Polyhedron with 1 vertex.\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4385\n\n",
    "created_at": "2008-10-30T04:16:25Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 3.1.4: optional doctest failure in sage/rings/polynomial/multi_polynomial.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4385",
    "user": "mabshoff"
}
```
Assignee: mhampton


```
sage -t -long -optional devel/sage/sage/rings/polynomial/multi_polynomial.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/multi_polynomial.py", line 712:
    sage: P
Expected:
    A Polyhedron with 4 vertices.
Got:
    A Polyhedron with 3 vertices.
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/multi_polynomial.py", line 721:
    sage: R(1).newton_polytope()
Expected:
    A Polyhedron with 1 vertices.
Got:
    A Polyhedron with 1 vertex.
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4385





---

archive/issue_comments_032277.json:
```json
{
    "body": "simple fixes",
    "created_at": "2008-10-31T12:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4385#issuecomment-32277",
    "user": "mhampton"
}
```

simple fixes



---

archive/issue_comments_032278.json:
```json
{
    "body": "Attachment [trac_4385.patch](tarball://root/attachments/some-uuid/ticket4385/trac_4385.patch) by mhampton created at 2008-10-31 12:38:56\n\nThis is very simple, those optional tests just hadn't been hit in a while and the output needed to be changed.  The \"vertices\" to \"vertex\" was just a grammatical fix.  The 4 vertices to 3 is because Polyhedron objects now remove redundant vertices immediately.",
    "created_at": "2008-10-31T12:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4385#issuecomment-32278",
    "user": "mhampton"
}
```

Attachment [trac_4385.patch](tarball://root/attachments/some-uuid/ticket4385/trac_4385.patch) by mhampton created at 2008-10-31 12:38:56

This is very simple, those optional tests just hadn't been hit in a while and the output needed to be changed.  The "vertices" to "vertex" was just a grammatical fix.  The 4 vertices to 3 is because Polyhedron objects now remove redundant vertices immediately.



---

archive/issue_comments_032279.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-10-31T12:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4385#issuecomment-32279",
    "user": "mhampton"
}
```

Changing priority from major to minor.



---

archive/issue_comments_032280.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T12:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4385#issuecomment-32280",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_032281.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T13:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4385#issuecomment-32281",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032282.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T13:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4385#issuecomment-32282",
    "user": "mabshoff"
}
```

Resolution: fixed
