# Issue 775: filename misreported in tracebacks for .pyx files

archive/issues_000775.json:
```json
{
    "body": "Assignee: was\n\nIn tracebacks the filenames get misreported. As you see below, sometimes the filename gets prefixed by the current directory.\n\n```\nsage: os.system(\"pwd\")\n/tmp\n0\nsage: sage.misc.sageinspect.sage_getfile(matrix)\n'/usr/local/sage/default/local/lib/python2.5/site-packages/sage/matrix/constructor.py'\nsage: M=matrix([[1,1]])\nsage: M*M\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/tmp/<ipython console> in <module>()\n\n/tmp/element.pyx in element.Matrix.__mul__()\n\n/tmp/element.pyx in element.Matrix._matrix_times_matrix_c()\n\n<type 'exceptions.TypeError'>: incompatible dimensions\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/775\n\n",
    "created_at": "2007-10-01T21:04:24Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "title": "filename misreported in tracebacks for .pyx files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/775",
    "user": "nbruin"
}
```
Assignee: was

In tracebacks the filenames get misreported. As you see below, sometimes the filename gets prefixed by the current directory.

```
sage: os.system("pwd")
/tmp
0
sage: sage.misc.sageinspect.sage_getfile(matrix)
'/usr/local/sage/default/local/lib/python2.5/site-packages/sage/matrix/constructor.py'
sage: M=matrix([[1,1]])
sage: M*M
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/tmp/<ipython console> in <module>()

/tmp/element.pyx in element.Matrix.__mul__()

/tmp/element.pyx in element.Matrix._matrix_times_matrix_c()

<type 'exceptions.TypeError'>: incompatible dimensions
```


Issue created by migration from https://trac.sagemath.org/ticket/775





---

archive/issue_comments_004627.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2007-10-02T00:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/775#issuecomment-4627",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_004628.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-02T00:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/775#issuecomment-4628",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004629.json:
```json
{
    "body": "Changing assignee from mabshoff to was.",
    "created_at": "2007-10-02T00:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/775#issuecomment-4629",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to was.



---

archive/issue_comments_004630.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2007-10-02T00:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/775#issuecomment-4630",
    "user": "mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_004631.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-23T02:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/775#issuecomment-4631",
    "user": "rlm"
}
```

Resolution: invalid



---

archive/issue_comments_004632.json:
```json
{
    "body": "This no longer happens. The traceback could be more useful, but the paths pointed to are now correct.",
    "created_at": "2009-01-23T02:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/775",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/775#issuecomment-4632",
    "user": "rlm"
}
```

This no longer happens. The traceback could be more useful, but the paths pointed to are now correct.
