# Issue 5259: invalid array elements sent to matplotlib quiver, causing blank plot

archive/issues_005259.json:
```json
{
    "body": "Assignee: was\n\nA student noticed that sometimes, when a function evaluation gave Inf or NaN, the vector field plot was blank.  Discussing this on the matplotlib-users list revealed that we ought to mask our arrays before sending them to the matplotlib quiver function.  This patch corrects this, so that the plot:\n\n\n```\nplot_vector_field( (-x/sqrt(x^2+y^2), -y/sqrt(x^2+y^2)), (x, -10, 10), (y, -10, 10))\n```\n\n\nnow plots (before it was a blank plot, now it just skips the problematic vectors).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5259\n\n",
    "created_at": "2009-02-13T20:50:21Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "invalid array elements sent to matplotlib quiver, causing blank plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5259",
    "user": "jason"
}
```
Assignee: was

A student noticed that sometimes, when a function evaluation gave Inf or NaN, the vector field plot was blank.  Discussing this on the matplotlib-users list revealed that we ought to mask our arrays before sending them to the matplotlib quiver function.  This patch corrects this, so that the plot:


```
plot_vector_field( (-x/sqrt(x^2+y^2), -y/sqrt(x^2+y^2)), (x, -10, 10), (y, -10, 10))
```


now plots (before it was a blank plot, now it just skips the problematic vectors).


Issue created by migration from https://trac.sagemath.org/ticket/5259





---

archive/issue_comments_040362.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-13T20:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40362",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040363.json:
```json
{
    "body": "To test this, you might try the following plots before and after the patch:\n\n\n```\n        sage: var('x,y')\n        sage: plot_vector_field( (-x/sqrt(x^2+y^2), -y/sqrt(x^2+y^2)), (x, -10, 10), (y, -10, 10))\n        sage: plot_vector_field( (-x/sqrt(x+y), -y/sqrt(x+y)), (x, -10, 10), (y, -10, 10))\n```\n",
    "created_at": "2009-02-13T20:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40363",
    "user": "jason"
}
```

To test this, you might try the following plots before and after the patch:


```
        sage: var('x,y')
        sage: plot_vector_field( (-x/sqrt(x^2+y^2), -y/sqrt(x^2+y^2)), (x, -10, 10), (y, -10, 10))
        sage: plot_vector_field( (-x/sqrt(x+y), -y/sqrt(x+y)), (x, -10, 10), (y, -10, 10))
```




---

archive/issue_comments_040364.json:
```json
{
    "body": "Changing assignee from was to jason.",
    "created_at": "2009-02-13T20:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40364",
    "user": "jason"
}
```

Changing assignee from was to jason.



---

archive/issue_comments_040365.json:
```json
{
    "body": "For the matplotlib-users discussion, see the messages with subject \"quiver and Inf values\" here: http://sourceforge.net/mailarchive/forum.php?forum_name=matplotlib-users&max_rows=25&style=ultimate&viewmonth=200902&viewday=13",
    "created_at": "2009-02-13T21:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40365",
    "user": "jason"
}
```

For the matplotlib-users discussion, see the messages with subject "quiver and Inf values" here: http://sourceforge.net/mailarchive/forum.php?forum_name=matplotlib-users&max_rows=25&style=ultimate&viewmonth=200902&viewday=13



---

archive/issue_comments_040366.json:
```json
{
    "body": "Attachment [trac_5259-mask-invalid-quiver-data.patch](tarball://root/attachments/some-uuid/ticket5259/trac_5259-mask-invalid-quiver-data.patch) by jason created at 2009-02-13 21:26:13\n\nupdated patch corrects the silly mistake in the doctest (I didn't account for the output of var('x,y')).  Now doctests pass in plot/*.py.",
    "created_at": "2009-02-13T21:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40366",
    "user": "jason"
}
```

Attachment [trac_5259-mask-invalid-quiver-data.patch](tarball://root/attachments/some-uuid/ticket5259/trac_5259-mask-invalid-quiver-data.patch) by jason created at 2009-02-13 21:26:13

updated patch corrects the silly mistake in the doctest (I didn't account for the output of var('x,y')).  Now doctests pass in plot/*.py.



---

archive/issue_comments_040367.json:
```json
{
    "body": "Everything look good !",
    "created_at": "2009-02-13T22:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40367",
    "user": "hivert"
}
```

Everything look good !



---

archive/issue_comments_040368.json:
```json
{
    "body": "Robert Nelson should be listed as the reporter of this bug.",
    "created_at": "2009-02-13T22:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40368",
    "user": "jason"
}
```

Robert Nelson should be listed as the reporter of this bug.



---

archive/issue_comments_040369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T09:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40369",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040370.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T09:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5259#issuecomment-40370",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael
