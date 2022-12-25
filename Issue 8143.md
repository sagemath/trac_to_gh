# Issue 8143: Efficient Gram-Schmidt

archive/issues_008143.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @jasongrout\n\nAs a Crypto PhD, I enjoy using the many functionalities in SAGE that interface the NTL library, however an important function was left out, namely the Gram-Schmidt Orthogonalization.\n\nThere is an implementation in SAGE which is in pure python and very slow (but exact). I propose to add an option to use NTL for matrices of dimensions > 200.\n\nRichard\n\nIssue created by migration from https://trac.sagemath.org/ticket/8143\n\n",
    "created_at": "2010-02-01T17:09:40Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Efficient Gram-Schmidt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8143",
    "user": "https://trac.sagemath.org/admin/accounts/users/rlindner"
}
```
Assignee: @aghitza

CC:  @jasongrout

As a Crypto PhD, I enjoy using the many functionalities in SAGE that interface the NTL library, however an important function was left out, namely the Gram-Schmidt Orthogonalization.

There is an implementation in SAGE which is in pure python and very slow (but exact). I propose to add an option to use NTL for matrices of dimensions > 200.

Richard

Issue created by migration from https://trac.sagemath.org/ticket/8143





---

archive/issue_comments_071472.json:
```json
{
    "body": "Changing assignee from @aghitza to jason, was.",
    "created_at": "2010-09-02T10:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8143#issuecomment-71472",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @aghitza to jason, was.



---

archive/issue_comments_071473.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2010-09-02T10:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8143#issuecomment-71473",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_071474.json:
```json
{
    "body": "I have been working on the exact Gram-Schmidt routine and on matrices over double-precision floating point numbers (RDF, CDF).\n\nAre you interested in an exact routine, or a fast approximate one?\n\nI couldn't find Gram-Schmidt via the NTL website (didn't look real hard).  Can you provide a pointer to whichever file contains it?\n\nRob",
    "created_at": "2011-02-24T05:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8143#issuecomment-71474",
    "user": "https://github.com/rbeezer"
}
```

I have been working on the exact Gram-Schmidt routine and on matrices over double-precision floating point numbers (RDF, CDF).

Are you interested in an exact routine, or a fast approximate one?

I couldn't find Gram-Schmidt via the NTL website (didn't look real hard).  Can you provide a pointer to whichever file contains it?

Rob
