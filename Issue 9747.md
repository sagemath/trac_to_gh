# Issue 9747: assigment to 1x1 submatrices specified by slices fails

archive/issues_009747.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  jason\n\nKeywords: matrix assignment slicing __setitem__\n\nAssigment to 1x1 submatrices specified by slices fails:\n\n## Example\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: A=matrix([[1,2],[3,4]])\nsage: B=matrix([[1,3],[5,7]])\nsage: A[1:2,1:2]=B[1:2,1:2]\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.5.2, Release Date: 2010-08-05                       |\n| Type notebook() for the GUI, and license() for information.        |\n/Users/phil/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5926)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:7044)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6807)()\n\nTypeError: unable to coerce <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'> to an integer\n\n```\n\nThe problem seems to be that the method !__setitem!__ treats 1x1 submatices as elements of the rings over which the matrix is defined, while the method !__getitem!__ treats 1x1 submatices as 1x1 matrices.\n\nBelow I will attach a patch which changes the method !__setitem!__ to treat 1x1 submatices specified by slices as 1x1 matrices.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9747\n\n",
    "created_at": "2010-08-14T15:11:51Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "assigment to 1x1 submatrices specified by slices fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9747",
    "user": "phil"
}
```
Assignee: jason, was

CC:  jason

Keywords: matrix assignment slicing __setitem__

Assigment to 1x1 submatrices specified by slices fails:

## Example

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A=matrix([[1,2],[3,4]])
sage: B=matrix([[1,3],[5,7]])
sage: A[1:2,1:2]=B[1:2,1:2]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.5.2, Release Date: 2010-08-05                       |
| Type notebook() for the GUI, and license() for information.        |
/Users/phil/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:5926)()

/Applications/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:7044)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6807)()

TypeError: unable to coerce <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'> to an integer

```

The problem seems to be that the method !__setitem!__ treats 1x1 submatices as elements of the rings over which the matrix is defined, while the method !__getitem!__ treats 1x1 submatices as 1x1 matrices.

Below I will attach a patch which changes the method !__setitem!__ to treat 1x1 submatices specified by slices as 1x1 matrices.

Issue created by migration from https://trac.sagemath.org/ticket/9747





---

archive/issue_comments_095464.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-14T15:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95464",
    "user": "phil"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095465.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-14T15:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95465",
    "user": "phil"
}
```

Attachment



---

archive/issue_comments_095466.json:
```json
{
    "body": "Can you add your example as a doctest?",
    "created_at": "2010-08-14T16:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95466",
    "user": "jason"
}
```

Can you add your example as a doctest?



---

archive/issue_comments_095467.json:
```json
{
    "body": "Attachment\n\nOk. Did I do it right? (this is my fist sage patch)",
    "created_at": "2010-08-14T16:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95467",
    "user": "phil"
}
```

Attachment

Ok. Did I do it right? (this is my fist sage patch)



---

archive/issue_comments_095468.json:
```json
{
    "body": "Fix bug in another case",
    "created_at": "2010-08-14T20:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95468",
    "user": "phil"
}
```

Fix bug in another case



---

archive/issue_comments_095469.json:
```json
{
    "body": "Attachment\n\nI added another patch (including a doctest) which fixes the bug in the case that only the second index is a slice. The following example works only after the second patch is applied:\n\n## Example\n\n\n```\nsage: A=matrix([[1,2],[3,4]]); B=matrix([[1,3],[5,7]])\nsage: A[1,0:1]=B[1,1:2]\nsage: A\n[1 2]\n[7 4]\n\n```\n",
    "created_at": "2010-08-14T20:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95469",
    "user": "phil"
}
```

Attachment

I added another patch (including a doctest) which fixes the bug in the case that only the second index is a slice. The following example works only after the second patch is applied:

## Example


```
sage: A=matrix([[1,2],[3,4]]); B=matrix([[1,3],[5,7]])
sage: A[1,0:1]=B[1,1:2]
sage: A
[1 2]
[7 4]

```




---

archive/issue_comments_095470.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-16T12:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95470",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095471.json:
```json
{
    "body": "Excellent -- positive review. Apply all three patches.",
    "created_at": "2010-12-16T12:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95471",
    "user": "davidloeffler"
}
```

Excellent -- positive review. Apply all three patches.



---

archive/issue_comments_095472.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9747#issuecomment-95472",
    "user": "jdemeyer"
}
```

Resolution: fixed
