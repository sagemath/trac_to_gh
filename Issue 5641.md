# Issue 5641: plotting of matrices with 0 rows or columns is broken in multiple ways

archive/issues_005641.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: matrix(QQ,0).plot()\nTraceback (most recent call last):\n...\nIndexError: index out of bounds\n\nsage: matrix(QQ,0,5).plot()\nTraceback (most recent call last):\n...\nIndexError: index out of bounds\n\nsage: matrix(QQ,5,0).plot()\nTraceback (most recent call last):\n...\nValueError: zero-size array to ufunc.reduce without identity\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5641\n\n",
    "created_at": "2009-03-30T03:18:23Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "plotting of matrices with 0 rows or columns is broken in multiple ways",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5641",
    "user": "was"
}
```
Assignee: was


```
sage: matrix(QQ,0).plot()
Traceback (most recent call last):
...
IndexError: index out of bounds

sage: matrix(QQ,0,5).plot()
Traceback (most recent call last):
...
IndexError: index out of bounds

sage: matrix(QQ,5,0).plot()
Traceback (most recent call last):
...
ValueError: zero-size array to ufunc.reduce without identity
```


Issue created by migration from https://trac.sagemath.org/ticket/5641





---

archive/issue_comments_044064.json:
```json
{
    "body": "Still broken, though now all three have the latter error message.  I'm not sure I like this even being possible:\n\n```\nsage: A = matrix(QQ,5,0)\nsage: A.rows()\n[(), (), (), (), ()]\n```\n\nDoes this have meaning?\n\nAnyway, the error is raised while trying to acquire a colormap in matplotlib in imshow, and then Numpy doesn't like one of the inputs.  Having a Numpy or matplotlib-native version of this would be helpful - maybe the problem is upstream?  Or maybe we're just using it wrong and should have a special thing for plotting empty matrices... ??",
    "created_at": "2012-06-01T18:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5641#issuecomment-44064",
    "user": "kcrisman"
}
```

Still broken, though now all three have the latter error message.  I'm not sure I like this even being possible:

```
sage: A = matrix(QQ,5,0)
sage: A.rows()
[(), (), (), (), ()]
```

Does this have meaning?

Anyway, the error is raised while trying to acquire a colormap in matplotlib in imshow, and then Numpy doesn't like one of the inputs.  Having a Numpy or matplotlib-native version of this would be helpful - maybe the problem is upstream?  Or maybe we're just using it wrong and should have a special thing for plotting empty matrices... ??
