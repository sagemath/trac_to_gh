# Issue 666: add spacing in latex output of matrices for increasing readbility

archive/issues_000666.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrently, printing of matrices in Latex form is difficult to read. I'm submitting a (trivial) patch\nthat adds more spacing to increase readibility.\n\nExample: \n\n```\nsage: M=MatrixSpace(QQ,2,2)\nsage: A=M([[2,3],[4,5]])\nsage: latex(A)\n```\n\ncurrently gives:\n\n```\n\\left(\\begin{array}{rr}\n2&3\\\\\n4&5\n\\end{array}\\right)\n```\n\nMy patch changes this to \n\n```\n\\left(\\begin{array}{rr}\n2 & 3 \\\\\n4 & 5\n\\end{array}\\right)\n```\n\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/666\n\n",
    "created_at": "2007-09-16T18:43:39Z",
    "labels": [
        "component: linear algebra",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "add spacing in latex output of matrices for increasing readbility",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/666",
    "user": "https://github.com/pdenapo"
}
```
Assignee: @williamstein

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

archive/issue_comments_003441.json:
```json
{
    "body": "Attachment [matrix_latex_spacing.patch](tarball://root/attachments/some-uuid/ticket666/matrix_latex_spacing.patch) by @pdenapo created at 2007-09-16 18:44:31",
    "created_at": "2007-09-16T18:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/666#issuecomment-3441",
    "user": "https://github.com/pdenapo"
}
```

Attachment [matrix_latex_spacing.patch](tarball://root/attachments/some-uuid/ticket666/matrix_latex_spacing.patch) by @pdenapo created at 2007-09-16 18:44:31



---

archive/issue_events_000734.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-21T02:40:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/666",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/666#event-734"
}
```



---

archive/issue_comments_003442.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T02:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/666",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/666#issuecomment-3442",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
