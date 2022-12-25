# Issue 6554: [with patch, needs review] plotting sparse matrices converts the matrix to a dense matrix

archive/issues_006554.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rbeezer @mwhansen @williamstein wcauchois @robertwb\n\nPlotting big sparse matrices doesn't even work since it automatically converts the matrix to a dense matrix, instead of calling the spy() function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6554\n\n",
    "created_at": "2009-07-18T14:00:55Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, needs review] plotting sparse matrices converts the matrix to a dense matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6554",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @rbeezer @mwhansen @williamstein wcauchois @robertwb

Plotting big sparse matrices doesn't even work since it automatically converts the matrix to a dense matrix, instead of calling the spy() function.

Issue created by migration from https://trac.sagemath.org/ticket/6554





---

archive/issue_comments_053348.json:
```json
{
    "body": "Attachment [trac-6554-sparse-matrix-plot.patch](tarball://root/attachments/some-uuid/ticket6554/trac-6554-sparse-matrix-plot.patch) by @jasongrout created at 2009-07-18 14:54:27\n\nThis took a very long time before, if it was even possible.\n\n\n```\n        sage: A=random_matrix(ZZ,100000,density=.00001,sparse=True)\n        sage: matrix_plot(A,marker=',')\n```\n",
    "created_at": "2009-07-18T14:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53348",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-6554-sparse-matrix-plot.patch](tarball://root/attachments/some-uuid/ticket6554/trac-6554-sparse-matrix-plot.patch) by @jasongrout created at 2009-07-18 14:54:27

This took a very long time before, if it was even possible.


```
        sage: A=random_matrix(ZZ,100000,density=.00001,sparse=True)
        sage: matrix_plot(A,marker=',')
```




---

archive/issue_comments_053349.json:
```json
{
    "body": "(To those I'm adding as CC): if you have time, could you review this ticket?  This is a simple change that makes plotting sparse matrices possible.  Currently, it is very, very slow or is not even really possible to plot large sparse matrices because Sage immediately converts the matrix to a dense matrix.",
    "created_at": "2009-07-21T17:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53349",
    "user": "https://github.com/jasongrout"
}
```

(To those I'm adding as CC): if you have time, could you review this ticket?  This is a simple change that makes plotting sparse matrices possible.  Currently, it is very, very slow or is not even really possible to plot large sparse matrices because Sage immediately converts the matrix to a dense matrix.



---

archive/issue_comments_053350.json:
```json
{
    "body": "It would be really great if this was reviewed in time for the Monday deadline for 4.1.1.  This is a simple change that makes plotting sparse matrices possible. Currently, it is very, very slow or is not even really possible to plot large sparse matrices because Sage immediately converts the matrix to a dense matrix.",
    "created_at": "2009-07-26T09:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53350",
    "user": "https://github.com/jasongrout"
}
```

It would be really great if this was reviewed in time for the Monday deadline for 4.1.1.  This is a simple change that makes plotting sparse matrices possible. Currently, it is very, very slow or is not even really possible to plot large sparse matrices because Sage immediately converts the matrix to a dense matrix.



---

archive/issue_comments_053351.json:
```json
{
    "body": "This installs fine (amd64 ubuntu 9.04, sage 4.1.1.alpha0) and I'm running tests now. However, why is it that\n\n\n```\nsage: B = random_matrix(ZZ, 10, 20, density=.4, sparse=True, x = 10)\nsage: matrix_plot(B, cmap='hsv').show(axes=False)\n```\n\nreturns a ble-and white scatterplot, but\n\n\n```\nsage: C = random_matrix(ZZ, 10, 20, x = 10)\nsage: matrix_plot(C, cmap='hsv').show(axes=False)\n```\n\nreturns a multi-colored plot? The docstring indicates that the colors plotted\nindicate the relative difference in sizes between the matrix entries. This seems\nto be incorrect, unless I am missing something, in the sparse case. Should a \ncomment to this effect be added to the docstring?",
    "created_at": "2009-07-26T12:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53351",
    "user": "https://github.com/wdjoyner"
}
```

This installs fine (amd64 ubuntu 9.04, sage 4.1.1.alpha0) and I'm running tests now. However, why is it that


```
sage: B = random_matrix(ZZ, 10, 20, density=.4, sparse=True, x = 10)
sage: matrix_plot(B, cmap='hsv').show(axes=False)
```

returns a ble-and white scatterplot, but


```
sage: C = random_matrix(ZZ, 10, 20, x = 10)
sage: matrix_plot(C, cmap='hsv').show(axes=False)
```

returns a multi-colored plot? The docstring indicates that the colors plotted
indicate the relative difference in sizes between the matrix entries. This seems
to be incorrect, unless I am missing something, in the sparse case. Should a 
comment to this effect be added to the docstring?



---

archive/issue_comments_053352.json:
```json
{
    "body": "Attachment [trac-6554-matrix-plot-docs.patch](tarball://root/attachments/some-uuid/ticket6554/trac-6554-matrix-plot-docs.patch) by @jasongrout created at 2009-07-27 16:04:40\n\napply on top of previous patch",
    "created_at": "2009-07-27T16:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53352",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-6554-matrix-plot-docs.patch](tarball://root/attachments/some-uuid/ticket6554/trac-6554-matrix-plot-docs.patch) by @jasongrout created at 2009-07-27 16:04:40

apply on top of previous patch



---

archive/issue_comments_053353.json:
```json
{
    "body": "Good point; the docstring should be updated.  I've attached a small patch that updates the docstring.  Can you review this docstring change?",
    "created_at": "2009-07-27T16:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53353",
    "user": "https://github.com/jasongrout"
}
```

Good point; the docstring should be updated.  I've attached a small patch that updates the docstring.  Can you review this docstring change?



---

archive/issue_comments_053354.json:
```json
{
    "body": "Yes, looks good and passes sage -testall (intel macbook, OS 10.4.11) except for\n\n\n```\n        sage -t  \"devel/sage/sage/parallel/decorate.py\"\n        sage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n```\n\nThey seem unrelated. As far as I am concerned, this gets a positive review.",
    "created_at": "2009-07-27T18:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53354",
    "user": "https://github.com/wdjoyner"
}
```

Yes, looks good and passes sage -testall (intel macbook, OS 10.4.11) except for


```
        sage -t  "devel/sage/sage/parallel/decorate.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

They seem unrelated. As far as I am concerned, this gets a positive review.



---

archive/issue_events_006791.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-29T12:57:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6554#event-6791"
}
```



---

archive/issue_comments_053355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-29T12:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053356.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-07-29T12:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6554#issuecomment-53356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches.
