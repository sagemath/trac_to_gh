# Issue 666: add spacing in latex output of matrices for increasing readbility

archive/issues_000666.json:
```json
{
    "body": "Assignee: was\n\nCurrently, printing of matrices in Latex form is difficult to read. I'm submitting a (trivial) patch\nthat adds more spacing to increase readibility.\n\nExample: \n\n```\nsage: M=MatrixSpace(QQ,2,2)\nsage: A=M([[2,3],[4,5]])\nsage: latex(A)\n```\n\ncurrently gives:\n\n```\n\\left(\\begin{array}{rr}\n2&3\\\\\n4&5\n\\end{array}\\right)\n```\n\nMy patch changes this to \n\n```\n\\left(\\begin{array}{rr}\n2 & 3 \\\\\n4 & 5\n\\end{array}\\right)\n```\n\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/666\n\n",
    "created_at": "2007-09-16T18:43:39Z",
    "labels": [
        "linear algebra",
        "trivial",
        "bug"
    ],
    "title": "add spacing in latex output of matrices for increasing readbility",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/666",
    "user": "pdenapo"
}
```
Assignee: was

Currently, printing of matrices in Latex form is difficult to read. I'm submitting a (trivial) patch
that adds more spacing to increase readibility.

Example: 

```
sage: M=MatrixSpace(QQ,2,2)
sage: A=M([[2,3],[4,5]])
sage: latex(A)
```

currently gives:

```
\left(\begin{array}{rr}
2&3\\
4&5
\end{array}\right)
```

My patch changes this to 

```
\left(\begin{array}{rr}
2 & 3 \\
4 & 5
\end{array}\right)
```






Issue created by migration from https://trac.sagemath.org/ticket/666





---

archive/issue_comments_003454.json:
```json
{
    "body": "Attachment [matrix_latex_spacing.patch](tarball://root/attachments/some-uuid/ticket666/matrix_latex_spacing.patch) by pdenapo created at 2007-09-16 18:44:31",
    "created_at": "2007-09-16T18:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/666#issuecomment-3454",
    "user": "pdenapo"
}
```

Attachment [matrix_latex_spacing.patch](tarball://root/attachments/some-uuid/ticket666/matrix_latex_spacing.patch) by pdenapo created at 2007-09-16 18:44:31



---

archive/issue_comments_003455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T02:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/666#issuecomment-3455",
    "user": "was"
}
```

Resolution: fixed
