# Issue 6946: Duplicated mpmath <-> sympy/mpmath and delaunay <-> matplotlib/delaunay

archive/issues_006946.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  jason\n\nThe delaunay packages appears to be the same, with just some name changes.\n\nBut the mpmath while providing the same feature, has a significant large amount of patches.\n\nIn either case, if patching sage to use sympy/mpmath and mpatplotlib/delaunay, the doctests works, but there may exit some special reason to use mpmath instead of sympy/mpmath.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6946\n\n",
    "created_at": "2009-09-16T20:19:33Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Duplicated mpmath <-> sympy/mpmath and delaunay <-> matplotlib/delaunay",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6946",
    "user": "pcpa"
}
```
Assignee: mabshoff

CC:  jason

The delaunay packages appears to be the same, with just some name changes.

But the mpmath while providing the same feature, has a significant large amount of patches.

In either case, if patching sage to use sympy/mpmath and mpatplotlib/delaunay, the doctests works, but there may exit some special reason to use mpmath instead of sympy/mpmath.

Issue created by migration from https://trac.sagemath.org/ticket/6946





---

archive/issue_comments_057430.json:
```json
{
    "body": "Attachment [sage-4.1.1-list_plot.patch](tarball://root/attachments/some-uuid/ticket6946/sage-4.1.1-list_plot.patch) by pcpa created at 2009-09-16 20:20:40\n\ndelaunay rpm patch",
    "created_at": "2009-09-16T20:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57430",
    "user": "pcpa"
}
```

Attachment [sage-4.1.1-list_plot.patch](tarball://root/attachments/some-uuid/ticket6946/sage-4.1.1-list_plot.patch) by pcpa created at 2009-09-16 20:20:40

delaunay rpm patch



---

archive/issue_comments_057431.json:
```json
{
    "body": "(Sorry, accidentally changed the description instead of posting a comment. Restored the original description.)\n\nsympy/mpmath should probably be regarded as an internal module of sympy. It includes some sympy-specific changes and is updated less frequently. More likely sympy/mpmath will go away some time in the future.",
    "created_at": "2009-09-17T16:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57431",
    "user": "fredrik.johansson"
}
```

(Sorry, accidentally changed the description instead of posting a comment. Restored the original description.)

sympy/mpmath should probably be regarded as an internal module of sympy. It includes some sympy-specific changes and is updated less frequently. More likely sympy/mpmath will go away some time in the future.



---

archive/issue_comments_057432.json:
```json
{
    "body": "Replying to [comment:2 fredrik.johansson]:\n> (Sorry, accidentally changed the description instead of posting a comment. Restored the original description.)\n> \n> sympy/mpmath should probably be regarded as an internal module of sympy. It includes some sympy-specific changes and is updated less frequently. More likely sympy/mpmath will go away some time in the future.\n\nMany thanks for the reply. I was unsure if I should create a mandriva package for mpmath, or assume it was unintended duplication of code. I even just updated the mpmath patch to also use sympy.mpmath from sage/libs/mpmath/utils.pyx\n\nI will add a python-mpmath package to mandriva, and revert the patch to use sympy.mpmath from my rpm. Guess for now it will also have duplicated %py_platsitedir/sympy/mpath and %py_platsitedir/mpath, what may be a source of confusion...",
    "created_at": "2009-09-17T23:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57432",
    "user": "pcpa"
}
```

Replying to [comment:2 fredrik.johansson]:
> (Sorry, accidentally changed the description instead of posting a comment. Restored the original description.)
> 
> sympy/mpmath should probably be regarded as an internal module of sympy. It includes some sympy-specific changes and is updated less frequently. More likely sympy/mpmath will go away some time in the future.

Many thanks for the reply. I was unsure if I should create a mandriva package for mpmath, or assume it was unintended duplication of code. I even just updated the mpmath patch to also use sympy.mpmath from sage/libs/mpmath/utils.pyx

I will add a python-mpmath package to mandriva, and revert the patch to use sympy.mpmath from my rpm. Guess for now it will also have duplicated %py_platsitedir/sympy/mpath and %py_platsitedir/mpath, what may be a source of confusion...



---

archive/issue_comments_057433.json:
```json
{
    "body": "just for documentation - but this patch should be no longer applied, and instead, create the python-mpmath rpm package",
    "created_at": "2009-09-17T23:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57433",
    "user": "pcpa"
}
```

just for documentation - but this patch should be no longer applied, and instead, create the python-mpmath rpm package



---

archive/issue_comments_057434.json:
```json
{
    "body": "Attachment [sage-4.1.1-mpmath.patch](tarball://root/attachments/some-uuid/ticket6946/sage-4.1.1-mpmath.patch) by jason created at 2011-03-15 05:34:41",
    "created_at": "2011-03-15T05:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57434",
    "user": "jason"
}
```

Attachment [sage-4.1.1-mpmath.patch](tarball://root/attachments/some-uuid/ticket6946/sage-4.1.1-mpmath.patch) by jason created at 2011-03-15 05:34:41



---

archive/issue_comments_057435.json:
```json
{
    "body": "Apparently `sympy.mpmath` no longer exists, nor does `delaunay`.",
    "created_at": "2015-04-13T13:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57435",
    "user": "mmezzarobba"
}
```

Apparently `sympy.mpmath` no longer exists, nor does `delaunay`.



---

archive/issue_comments_057436.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T13:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57436",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057437.json:
```json
{
    "body": "But it is still mentioned in the sympy documentation [http://docs.sympy.org/dev/modules/mpmath/setup.html#mpmath-under-sympy](http://docs.sympy.org/dev/modules/mpmath/setup.html#mpmath-under-sympy). Weird!",
    "created_at": "2015-04-24T21:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57437",
    "user": "vdelecroix"
}
```

But it is still mentioned in the sympy documentation [http://docs.sympy.org/dev/modules/mpmath/setup.html#mpmath-under-sympy](http://docs.sympy.org/dev/modules/mpmath/setup.html#mpmath-under-sympy). Weird!



---

archive/issue_comments_057438.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-05-29T02:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57438",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057439.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-06-19T08:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6946",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6946#issuecomment-57439",
    "user": "vbraun"
}
```

Resolution: fixed
