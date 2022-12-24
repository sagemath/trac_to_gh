# Issue 6258: Improve accuracy of graph eigenvalues

archive/issues_006258.json:
```json
{
    "body": "Assignee: @rbeezer\n\nCC:  @jasongrout\n\nEigenspaces and eigenvalues of graphs are computed by converting the adjacency matrix to have RDF as the base ring, but there are now better routines in place for eigenvalues of integer matrices, so the `eigenspaces()` and `eigenvalues()` methods should be using those.\n\nAt present, the approximate values of the eigenvalues lead to eigenspaces \"splitting\" into pieces (i.e. several eigenspaces that should all be one), so in that regard current results are inaccurate.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6258\n\n",
    "created_at": "2009-06-11T03:02:30Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Improve accuracy of graph eigenvalues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6258",
    "user": "@rbeezer"
}
```
Assignee: @rbeezer

CC:  @jasongrout

Eigenspaces and eigenvalues of graphs are computed by converting the adjacency matrix to have RDF as the base ring, but there are now better routines in place for eigenvalues of integer matrices, so the `eigenspaces()` and `eigenvalues()` methods should be using those.

At present, the approximate values of the eigenvalues lead to eigenspaces "splitting" into pieces (i.e. several eigenspaces that should all be one), so in that regard current results are inaccurate.

Issue created by migration from https://trac.sagemath.org/ticket/6258





---

archive/issue_comments_049981.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2009-06-30T06:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6258#issuecomment-49981",
    "user": "@rbeezer"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_049982.json:
```json
{
    "body": "Attachment [trac_6258_graph_eigenvalues.patch](tarball://root/attachments/some-uuid/ticket6258/trac_6258_graph_eigenvalues.patch) by @rbeezer created at 2009-06-30 06:07:47\n\nThe patch generally improves graph eigenvalues by not altering the adjacency matrix and therefore allowing new routines to take advantage of the adjacency matrix being a matrix of integers.  It also corrects a serious bug for eigenvalues of digraphs.  More specifically\n\n1.  The adjacency matrix is no longer converted to a matrix of reals or complexes.\n\n2.  Eigenspaces are now more abstract (but are exact).  More numerical results come from the new `eigenvectors()` method.\n\n3.  Any complex part of an eigenvalue was previously being stripped, as if a graph could never be a digraph.  This has been corrected and a simple doctest added.\n\n4.  While in the neighborhood, the `characteristic_polynomial()` got some cosmetic changes in its docstring.\n\n5.  Long-term, the `spectrum()` command should return some sort of object, like a `Factorization` object, as discussed on sage-devel.  Then the current `spectrum()` could be renamed as `eigenvalues()`.",
    "created_at": "2009-06-30T06:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6258#issuecomment-49982",
    "user": "@rbeezer"
}
```

Attachment [trac_6258_graph_eigenvalues.patch](tarball://root/attachments/some-uuid/ticket6258/trac_6258_graph_eigenvalues.patch) by @rbeezer created at 2009-06-30 06:07:47

The patch generally improves graph eigenvalues by not altering the adjacency matrix and therefore allowing new routines to take advantage of the adjacency matrix being a matrix of integers.  It also corrects a serious bug for eigenvalues of digraphs.  More specifically

1.  The adjacency matrix is no longer converted to a matrix of reals or complexes.

2.  Eigenspaces are now more abstract (but are exact).  More numerical results come from the new `eigenvectors()` method.

3.  Any complex part of an eigenvalue was previously being stripped, as if a graph could never be a digraph.  This has been corrected and a simple doctest added.

4.  While in the neighborhood, the `characteristic_polynomial()` got some cosmetic changes in its docstring.

5.  Long-term, the `spectrum()` command should return some sort of object, like a `Factorization` object, as discussed on sage-devel.  Then the current `spectrum()` could be renamed as `eigenvalues()`.



---

archive/issue_comments_049983.json:
```json
{
    "body": "Looks good. And great job with the documentation!\n\nPatch applies cleanly to 4.1.alpha2; testing in progress on sage-math. I'll report back soon.",
    "created_at": "2009-06-30T09:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6258#issuecomment-49983",
    "user": "@saliola"
}
```

Looks good. And great job with the documentation!

Patch applies cleanly to 4.1.alpha2; testing in progress on sage-math. I'll report back soon.



---

archive/issue_comments_049984.json:
```json
{
    "body": "No new doctest failures are introduced by this patch on 4.1.alpha2. \n\nPositive review.",
    "created_at": "2009-06-30T11:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6258#issuecomment-49984",
    "user": "@saliola"
}
```

No new doctest failures are introduced by this patch on 4.1.alpha2. 

Positive review.



---

archive/issue_comments_049985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T20:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6258",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6258#issuecomment-49985",
    "user": "@rlmill"
}
```

Resolution: fixed
